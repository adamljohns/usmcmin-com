"""Shared helpers for the commerce FULL REVIEW mode (ticket 2026-11-09, Max / Adam order).

Pipeline (one round):
  select-full-review-batch.py -> full-review-fetch.py -> full-review-build-patch.py
  -> (only on Adam's GO) apply-full-review-patch.py --live

Nothing in this module writes data/businesses.json. Review patches, HOLD rows and
cached page text are written OUTSIDE the repository (FR_HOME, default
~/commerce-full-review) because this repo is public on GitHub and its root is
synced to R2. Only counts (data/full-review-stats.json) are written inside it.
"""
from __future__ import annotations

import hashlib
import html as htmlmod
import json
import os
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # fxbg/commerce
DATA = ROOT / "data" / "businesses.json"
METHODOLOGY = ROOT / "methodology.html"
METHODOLOGY_URL = "https://usmcmin.com/fxbg/commerce/methodology.html"
PUBLIC_STATS = ROOT / "data" / "full-review-stats.json"   # counts only
FR_HOME = Path(os.environ.get("COMMERCE_FR_HOME", str(Path.home() / "commerce-full-review")))
GRIND_LOCK = Path("/tmp/commerce-enrichment-round.lock.d")  # held by ~/Scripts/commerce-enrichment-round.sh
FR_LOCK = Path("/tmp/commerce-full-review.lock.d")

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36 C5iSR-CommerceReview/1.0 (+https://usmcmin.com/fxbg/commerce/)"}
CTX = ssl.create_default_context()
HOST_GAP = float(os.environ.get("FULL_REVIEW_HOST_GAP", "1.1"))   # >= 1 s per host, always

LOCAL_TOWNS = {
    "fredericksburg", "spotsylvania", "stafford", "king george", "caroline", "falmouth", "thornburg",
    "partlow", "locust grove", "ladysmith", "bowling green", "ruther glen", "woodford", "garrisonville",
    "aquia", "massaponax", "brooke", "hartwood", "milford", "port royal", "corbin", "chancellor",
}

# Licensed trades: DPOR contractor / tradesman boards (ticket item 3).
LICENSED_TRADES = {
    "hvac", "plumbing", "electrical", "electrical-contractor", "roofing", "home-builder", "home-services",
    "remodeling", "flooring", "fence", "contractor", "general-contractor", "paving", "pool", "septic",
    "well-drilling", "inspection", "appliance-repair", "gas-fitting", "solar",
}

DPOR_LOOKUP_URL = "https://dporweb.dpor.virginia.gov/LicenseLookup/"
SCC_LOOKUP_URL = "https://cis.scc.virginia.gov/EntitySearch/Index"
# Recorded 2026-11-09 by probing both forms (see GRIND/runbook note). If either
# stops requiring a CAPTCHA, set the env flag and implement the lookup; until
# then the round records the skip reason and the lookup URL for a human.
LOOKUP_SKIPS = {
    "scc": ("skipped: the SCC Clerk's Information System entity search submits through Google "
            "reCAPTCHA v3 (grecaptcha.execute on the Search button) after a cookie-consent "
            "redirect; automated lookup would mean defeating a CAPTCHA. Checked 2026-11-09."),
    "dpor": ("skipped: DPOR License Lookup (dporweb.dpor.virginia.gov/LicenseLookup) requires the "
             "reCAPTCHA checkbox before every search ('Please check the reCAPTCHA checkbox'). "
             "Checked 2026-11-09."),
}


# ── hashing / io ─────────────────────────────────────────────────────────────
def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_data(path: Path = DATA) -> dict:
    return json.loads(Path(path).read_text())


def dump(obj, path: Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n")
    tmp.replace(path)


# ── polite fetch ─────────────────────────────────────────────────────────────
_last_hit: dict[str, float] = {}


def host_of(u: str) -> str:
    return urllib.parse.urlparse(u or "").netloc.lower().removeprefix("www.")


def polite_fetch(url: str, timeout: int = 15, max_bytes: int = 700_000):
    """(final_url, status, raw_html). Never raises. At most one request per HOST_GAP per host."""
    h = host_of(url)
    wait = HOST_GAP - (time.time() - _last_hit.get(h, 0))
    if wait > 0:
        time.sleep(wait)
    _last_hit[h] = time.time()
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            ctype = r.headers.get("Content-Type", "")
            if ctype and "html" not in ctype and "text" not in ctype and "json" not in ctype:
                return r.geturl(), r.status, ""
            return r.geturl(), r.status, r.read(max_bytes).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return url, e.code, ""
    except Exception as e:  # DNS, TLS, timeout, reset
        return url, "error:" + type(e).__name__, ""


# ── text helpers ─────────────────────────────────────────────────────────────
_QMAP = str.maketrans({"\u00b7": " ", "’": "'", "‘": "'", "“": '"', "”": '"', " ": " ",
                       "–": "-", "—": "-", "…": "...", " ": " ", " ": " "})


def nrm(s) -> str:
    return re.sub(r"\s+", " ", str(s or "").translate(_QMAP)).strip().lower()


_JSONISH = re.compile(r'":|\\/|\{"|"\}|\\u[0-9a-f]{4}|[{}\[\]]{2,}', re.I)


def display_quote(q: str) -> str:
    """page_text marks element boundaries with ' · '; in a published quote show them as line
    breaks so the passage matches the live page (matching ignores whitespace)."""
    return re.sub(r"\s*\u00b7\s*", "\n", str(q or "")).strip()


def page_text(raw: str) -> str:
    """Visible text only: scripts, styles, templates, svg, head and inline JSON blobs removed."""
    raw = re.sub(r"<(script|style|noscript|template|svg|head)[^>]*>.*?</\1>", " ", raw or "", flags=re.S | re.I)
    raw = re.sub(r"<br\s*/?>|</(p|div|li|h\d|tr|td|section|footer|header)>", " · ", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", " ", raw)
    txt = htmlmod.unescape(raw)
    toks = [t for t in txt.split() if len(t) <= 60 and not _JSONISH.search(t)]
    txt = " ".join(toks)
    txt = re.sub(r"(\s*·\s*)+", " · ", txt)
    return txt.strip(" ·")


def locate(quote: str, pages: list[dict]):
    """URL of the first fetched page containing quote verbatim (normalized), else None."""
    q = nrm(quote).strip(" .,;:\"'·")
    if len(q) < 4:
        return None
    for p in pages:
        if q in p["norm"]:
            return p["url"]
    return None


def snippet(text: str, start: int, end: int, cap: int = 240) -> str:
    """Verbatim window around [start,end) — on the page by construction."""
    a = max(0, start - 120)
    cut = max(text.rfind(". ", a, start), text.rfind(" · ", a, start))
    s = cut + 2 if cut >= 0 else a
    while s > 0 and s < len(text) and not text[s - 1].isspace():
        s += 1
    b = min(len(text), end + 140)
    ends = [i for i in (text.find(". ", end, b), text.find(" · ", end, b)) if i >= 0]
    e = (min(ends) + 1) if ends else b
    while e < len(text) and e > end and not text[e - 1].isspace() and text[e - 1].isalnum():
        e -= 1
    out = text[s:e].strip(" ·")
    if len(out) > cap:
        rel = max(0, start - s)
        lo = max(0, rel - cap // 3)
        out = out[lo:lo + cap]
        out = out.strip(" ·")
    return out


def digits(s) -> str:
    d = re.sub(r"\D", "", str(s or ""))
    return d[1:] if len(d) == 11 and d.startswith("1") else d


def junk_phone(d: str) -> bool:
    """Template / fictional numbers: 555-555-5555, 555-01xx, 123-456-7890, one repeated digit."""
    d = digits(d)
    return (len(d) != 10 or d[3:6] == "555" or d[:3] == "555" or d in ("1234567890", "0123456789")
            or len(set(d)) <= 2)


PHONE_RE = re.compile(r"(?<!\d)(?:\+?1[\s.\-]?)?\(?([2-9]\d{2})\)?[\s.\-]?(\d{3})[\s.\-](\d{4})(?!\d)")
ZIP_RE = re.compile(r"\b(2[0-4]\d{3})(?:-\d{4})?\b")   # Virginia-ish ZIPs (20xxx-24xxx)
STREET_SUFFIX = r"(?:st|street|rd|road|ave|avenue|blvd|boulevard|hwy|highway|pkwy|parkway|dr|drive|ln|lane|ct|court|pl|place|way|tpke|turnpike|cir|circle|sq|square|trl|trail|pike|row|ter|terrace)"
STREET_RE = re.compile(r"\b(\d{1,6})\s+((?:[NSEW]\.?\s+)?[A-Z0-9][A-Za-z0-9.'\-]*(?:\s+[A-Z][A-Za-z.'\-]*){0,3})\s+" + STREET_SUFFIX + r"\b\.?", re.I)


def stored_street(biz: dict) -> tuple[str | None, str | None]:
    """(house number, first significant street word) from the stored address."""
    a = str(biz.get("address") or "")
    m = re.match(r"\s*(\d{1,6})[A-Za-z]?\s+(?:[NSEW]\.?\s+)?([A-Za-z0-9]+)", a)
    if not m:
        return None, None
    return m.group(1), m.group(2)


def identity_hits(biz: dict, text: str) -> list[str]:
    """Which stored identifiers a page prints: street (number + street word), ZIP, phone."""
    hits = []
    no, word = stored_street(biz)
    if no and word and re.search(r"\b" + re.escape(no) + r"\s+(?:[NSEW]\.?\s+)?" + re.escape(word), text, re.I):
        hits.append(f"street:{no} {word}")
    z = str(biz.get("zip") or "").strip()
    if re.fullmatch(r"\d{5}", z) and re.search(r"\b" + z + r"\b", text):
        hits.append("zip:" + z)
    ph = digits(biz.get("phone"))
    if len(ph) == 10 and ph in re.sub(r"\D", "", text):
        hits.append("phone")
    return hits


NAME_STOP = {"the", "and", "of", "inc", "llc", "co", "company", "fredericksburg", "fxbg", "va", "virginia",
             "stafford", "spotsylvania", "store", "shop", "services", "service", "restaurant", "center", "group"}


def name_tokens(name: str) -> list[str]:
    t = re.sub(r"['’]", "", str(name or "").lower())
    return [w for w in re.findall(r"[a-z0-9]+", t) if len(w) >= 3 and w not in NAME_STOP]


def name_on_page(biz: dict, text: str) -> bool:
    toks = name_tokens(biz.get("name"))
    if not toks:
        return False
    nt = nrm(text)
    hit = sum(1 for t in toks if re.search(r"\b" + re.escape(t) + r"\b", nt))
    return hit >= max(1, (len(toks) + 1) // 2)


def name_slugs(name: str) -> list[str]:
    """Candidate own-domain names: '2400 Diner' -> ['2400diner', '2400dinerva'];
    'James G. Sibley Electrical, Inc.' -> ['jamesgsibleyelectrical', 'jamessibleyelectrical', 'sibleyelectrical', ...]."""
    t = re.sub(r"['\u2019]", "", str(name or "").lower()).replace("&", " and ")
    toks = [w for w in re.findall(r"[a-z0-9]+", t) if w not in ("the", "inc", "llc", "co", "corp", "ltd", "company", "and")]
    out = []

    def add(v):
        if 4 <= len(v) <= 40 and v not in out:
            out.append(v)
    add("".join(toks))
    add("".join(toks) + "va")
    no_initials = [w for w in toks if len(w) > 1]
    add("".join(no_initials))
    if len(no_initials) >= 3:
        add("".join(no_initials[1:]))      # drop a leading first name
    return out[:4]


# ── socials ──────────────────────────────────────────────────────────────────
SOCIAL_RE = {
    "facebook": re.compile(r"https?://(?:www\.|m\.)?facebook\.com/[A-Za-z0-9_.\-/%]+(?:\?(?:amp;)?id=\d+)?", re.I),
    "instagram": re.compile(r"https?://(?:www\.)?instagram\.com/[A-Za-z0-9_.\-]+", re.I),
    "linkedin": re.compile(r"https?://(?:www\.)?linkedin\.com/(?:company|in)/[A-Za-z0-9_.\-%]+", re.I),
    "youtube": re.compile(r"https?://(?:www\.)?youtube\.com/(?:@|c/|channel/|user/)[A-Za-z0-9_.\-]+", re.I),
    "x": re.compile(r"https?://(?:www\.)?(?:twitter|x)\.com/[A-Za-z0-9_]+", re.I),
}
BAD_SOCIAL = re.compile(r"/(sharer|share|dialog|plugins|tr\?|intent|hashtag|login|policies|help|privacy|"
                        r"legal|watch|embed|p/|reel|events?/|groups/|photo|story\.php|permalink|home\.php|"
                        r"profile\.php\?id=$|wix|squarespace|godaddy|shopify|weebly|about)\b", re.I)
SOCIAL_LABEL = {"facebook": "Facebook", "instagram": "Instagram", "linkedin": "LinkedIn", "youtube": "YouTube", "x": "X"}


def harvest_socials(raw: str, page_url: str, found: dict) -> None:
    """Record each social account with WHERE it was found: the exact <a ...> tag when the
    HTML links it (html_link), else the raw config/JSON snippet (site-config). An html_link
    anywhere beats a config-only find. Junk such as facebook.com/2008 (xmlns:fb) is skipped."""
    for k, rx in SOCIAL_RE.items():
        for m in rx.finditer(raw or ""):
            u = m.group(0).rstrip("/&\"'\\")
            if BAD_SOCIAL.search(u + "/"):
                continue
            clean = u.split("#")[0]
            if "profile.php" in clean:
                pid = re.search(r"[?&]id=(\d{5,})", clean)
                if not pid:
                    continue          # bare profile.php is not an account
                clean = clean.split("?")[0] + "?id=" + pid.group(1)
            else:
                clean = clean.split("?")[0].rstrip("/")
            seg = urllib.parse.urlparse(clean).path.strip("/").split("/")[0]
            if not seg or re.fullmatch(r"\d{1,6}", seg) or seg.lower() in ("pages", "people", "pg"):
                continue
            lt = raw.rfind("<", 0, m.start())
            gt = raw.find(">", m.end())
            tag = raw[lt:gt + 1] if lt >= 0 and gt >= 0 and raw.rfind(">", 0, m.start()) < lt else ""
            is_href = bool(re.match(r"<a\b", tag, re.I)) and re.search(r"href\s*=\s*[\"']?" + re.escape(m.group(0)[:40]), tag, re.I)
            kind = "html_link" if is_href else "site-config"
            quote = tag[:400] if is_href else raw[max(0, m.start() - 60):min(len(raw), m.end() + 30)]
            prev = found.get(k)
            if prev and (prev["kind"] == "html_link" or kind == "site-config"):
                continue
            found[k] = {"url": clean, "kind": kind, "quote": quote, "page": page_url}


# ── hours: parse to day+time token sets ──────────────────────────────────────
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_DAY_RX = r"(mon(?:day)?s?|tue(?:s(?:day)?)?s?|wed(?:nesday)?s?|thu(?:r(?:s(?:day)?)?)?s?|fri(?:day)?s?|sat(?:urday)?s?|sun(?:day)?s?)\.?"
_DAY_IDX = {"mo": 0, "tu": 1, "we": 2, "th": 3, "fr": 4, "sa": 5, "su": 6}
_TIME_RX = r"(?<![\d.:])(\d{1,2})(?:[:.](\d{2}))?\s*(a\.?\s?m\.?|p\.?\s?m\.?|am|pm|a|p)?(?![\d\w])|(noon|midnight)"
_TOKEN_RX = re.compile(
    r"(?P<day>\b" + _DAY_RX + r"\b)"
    r"|(?P<daily>\b(?:daily|every ?day|7 days a week|seven days a week|open daily)\b)"
    r"|(?P<closed>\bclosed\b)"
    r"|(?P<h24>\b(?:open )?24 ?(?:hours|hrs|/7)\b)"
    r"|(?P<appt>\b(?:open )?by appointment(?: only)?\b|\bappointment only\b)"
    r"|(?P<range>(?:" + _TIME_RX + r")\s*(?:-|–|—|to|until|till)\s*(?:" + _TIME_RX + r"))"
    r"|(?P<dsep>\s*(?:-|–|—|\bthrough\b|\bthru\b|\bto\b)\s*)"
    r"|(?P<amp>\s*(?:&|\band\b|,|/)\s*)",
    re.I,
)


def _day_index(tok: str) -> int | None:
    t = tok.lower().strip(".")[:2]
    return _DAY_IDX.get(t)


def _to_min(h: str, mm: str | None, ap: str | None, word: str | None):
    if word:
        return (12 * 60, "x") if word.lower() == "noon" else (24 * 60, "x")
    hh = int(h)
    m = int(mm or 0)
    if hh > 24 or m > 59:
        return None
    a = (ap or "").lower().replace(".", "").replace(" ", "")
    if a.startswith("a"):
        if hh == 12:
            hh = 0
        return hh * 60 + m, "x"
    if a.startswith("p"):
        if hh != 12:
            hh += 12
        return hh * 60 + m, "x"
    return hh * 60 + m, ("24h" if hh > 12 or (h.startswith("0") and len(h) == 2) or hh == 0 else "?")


def _range_minutes(s: str):
    m = re.match(r"\s*(?:" + _TIME_RX + r")\s*(?:-|–|—|to|until|till)\s*(?:" + _TIME_RX + r")", s, re.I)
    if not m:
        return None
    g = m.groups()
    a = _to_min(g[0], g[1], g[2], g[3]) if (g[0] or g[3]) else None
    b = _to_min(g[4], g[5], g[6], g[7]) if (g[4] or g[7]) else None
    if not a or not b:
        return None
    (o, fo), (c, fc) = a, b
    inferred = False
    if fo == "?" and fc == "x":
        # "11-9pm": open takes am unless that would put it after close
        if o >= 12 * 60:
            o -= 12 * 60
        if o + 12 * 60 < c and o < 6 * 60:
            o += 12 * 60
            inferred = True
    elif fo == "x" and fc == "?":
        if c <= o:
            c += 12 * 60
            inferred = True
    elif fo == "?" and fc == "?":
        inferred = True
        if o < 6 * 60:
            o += 12 * 60          # "5-9" is an evening, not 5 am
        while c <= o and c + 12 * 60 <= o + 24 * 60:
            c += 12 * 60
    if c == 0:
        c = 24 * 60
    if c <= o:
        c += 24 * 60 if c + 12 * 60 <= o else 12 * 60
    return o, c, inferred


def fmt_min(m: int) -> str:
    m %= 24 * 60
    h, mm = divmod(m, 60)
    ap = "AM" if h < 12 else "PM"
    h = h % 12 or 12
    return f"{h}:{mm:02d} {ap}"


def parse_hours(text: str) -> dict:
    """Parse an hours passage. Returns {"days": {Mon: [(o,c)] | "closed"}, "inferred": bool,
    "complete": all 7 days stated, "ok": parsed something}. Deterministic; no model.
    A time not printed with am/pm (or 24h form) sets inferred=True, which keeps any
    resulting change on HOLD."""
    days: dict[str, object] = {}
    inferred = False
    pending: list[int] = []      # days the next time range belongs to
    last_day: int | None = None
    mode = "new"                 # new | range (after "Mon -") | group (after "Mon &")
    after_time = False
    last_end = 0
    t = (text or "").replace("–", "-").replace("—", "-")
    # "Closed on Saturdays" -> "Saturdays closed" (the closure word comes before the day)
    t = re.sub(r"\bclosed (?:on )?((?:mon|tue|wed|thu|fri|sat|sun)[a-z]*)", r"\1 closed", t, flags=re.I)
    for m in _TOKEN_RX.finditer(t):
        kind = m.lastgroup
        if m.start() - last_end > 25 and kind not in ("day", "daily"):
            pending, mode, after_time = [], "new", False   # stray time far from any day word
        if kind in ("dsep", "amp") and not pending:
            continue
        last_end = m.end()
        if kind == "day":
            idx = _day_index(m.group("day"))
            if idx is None:
                continue
            if mode == "range" and last_day is not None and not after_time:
                span = [(last_day + k) % 7 for k in range(1, (idx - last_day) % 7 + 1)]
                pending.extend(d for d in span if d not in pending)
            elif mode == "group" and not after_time:
                pending.append(idx)
            else:
                pending = [idx]
            last_day, mode, after_time = idx, "new", False
        elif kind == "dsep":
            mode = "range" if not after_time else "new"
        elif kind == "amp":
            mode = "group" if not after_time else "new"
        elif kind == "daily":
            pending, last_day, mode, after_time = list(range(7)), None, "new", False
        else:  # closed | appt | h24 | range
            if not pending:
                continue
            if kind in ("closed", "appt"):
                if after_time:
                    continue          # "closed on holidays" / "or by appointment" after a day's hours is not that day's value
                val = kind if kind == "closed" else "appointment"
            elif kind == "h24":
                val = [(0, 24 * 60)]
            else:
                r = _range_minutes(m.group("range"))
                if not r:
                    continue
                o, c, inf = r
                inferred = inferred or inf
                val = [(o, c)]
            for d in pending:
                cur = days.get(DAYS[d])
                if after_time and cur is not None and not isinstance(cur, list):
                    continue          # "Sunday Closed · Available 24/7": a day already closed/by appointment keeps that value
                if isinstance(cur, list) and isinstance(val, list) and after_time:
                    if val[0] not in cur:
                        cur.extend(val)  # split shift right after, e.g. "11-2 & 5-9"
                else:
                    days[DAYS[d]] = list(val) if isinstance(val, list) else val
            after_time, mode = True, "new"
    return {"days": days, "inferred": inferred, "complete": len(days) == 7, "ok": bool(days)}


def hours_tokens(parsed: dict) -> list[str]:
    out = []
    for d in DAYS:
        v = parsed["days"].get(d)
        if v is None:
            continue
        if v == "closed":
            out.append(f"{d} closed")
        elif v == "appointment":
            out.append(f"{d} by appointment")
        else:
            for o, c in sorted(v):
                out.append(f"{d} {fmt_min(o)}-{fmt_min(c)}")
    return out


def hours_lines(parsed: dict) -> list[str]:
    """Structured value in the stored format: ['Mon–Fri: 7:00 AM–8:00 PM', 'Sat: Closed']."""
    def span_str(v):
        if v == "closed":
            return "Closed"
        if v == "appointment":
            return "By appointment"
        if v == [(0, 24 * 60)]:
            return "Open 24 hours"
        return ", ".join(f"{fmt_min(o)}–{fmt_min(c)}" for o, c in sorted(v))
    lines, i = [], 0
    while i < 7:
        d = DAYS[i]
        v = parsed["days"].get(d)
        if v is None:
            i += 1
            continue
        j = i
        while j + 1 < 7 and parsed["days"].get(DAYS[j + 1]) == v:
            j += 1
        label = d if i == j else f"{d}–{DAYS[j]}"
        lines.append(f"{label}: {span_str(v)}")
        i = j + 1
    return lines


def osm_hours_text(oh: str) -> str:
    """OSM opening_hours -> plain text the same parser reads ('Mo-Fr 08:00-18:00; Sa off')."""
    t = (oh or "").replace(";", " · ").replace(" off", " closed")
    t = re.sub(r"\bPH\b[^·]*", "", t)
    for two, three in (("Mo", "Mon"), ("Tu", "Tue"), ("We", "Wed"), ("Th", "Thu"), ("Fr", "Fri"), ("Sa", "Sat"), ("Su", "Sun")):
        t = re.sub(r"\b" + two + r"\b", three, t)
    return "Daily 00:00-24:00" if t.strip() == "24/7" else t


# ── methodology rules (scores come ONLY from these written texts) ───────────
RULES = {
    "green": {"text": "Affirmative evidence this factor passes. Absence of bad news is not Green.", "context": "Color lock: Green (Recommended)"},
    "yellow": {"text": "Unresolved concern or mixed evidence.", "context": "Color lock: Yellow (Caution)"},
    "red": {"text": "Documented material failure (URL or dated public document).", "context": "Color lock: Red (Not recommended)"},
    "gray": {"text": "Insufficient public evidence. Neutral — not guilt, not soft Red.", "context": "Color lock: Gray (Unrated)"},
    "no_scandal_gray": {"text": "Hard rule: “We looked and found no scandal” = Gray, never Green.", "context": "Color lock: hard rule"},
    "type_a": {"text": "Explicitly Christian business — faith is public identity", "context": "Factor #3 identity type A — #3 score: Green with affirmative evidence"},
    "type_a_score": {"text": "Green with affirmative evidence", "context": "Factor #3 identity type A, #3 score column"},
    "f1": {"text": "Who owns/operates it? Real address?", "context": "Factor #1 Ownership clarity"},
    "f8": {"text": "Scam-adjacent? Licensed/transparent?", "context": "Factor #8 Financial integrity"},
    "f9": {"text": "Can a neighbor actually reach them?", "context": "Factor #9 Digital integrity"},
    "franchise": {"text": "Franchise: local operator + national brand both described.", "context": "Evidence rules"},
    "red_needs_url": {"text": "Red/Black require URLs or dated public documents.", "context": "Evidence rules"},
}


def _meth_norm(s: str) -> str:
    s = nrm(s)
    s = re.sub(r"\s+([,.?:;])", r"\1", s)
    return s


def methodology_text() -> str:
    raw = METHODOLOGY.read_text()
    raw = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", "", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return htmlmod.unescape(raw)


def check_rules() -> dict:
    """Every cited rule text must be printed on methodology.html; fail closed otherwise."""
    page = _meth_norm(methodology_text())
    missing = [k for k, r in RULES.items() if _meth_norm(r["text"]).replace("hard rule: ", "") not in page]
    if missing:
        raise SystemExit(f"METHODOLOGY_DRIFT: rule text no longer on methodology.html: {missing}")
    return {k: dict(v, url=METHODOLOGY_URL) for k, v in RULES.items()}


def rule(*keys: str) -> list[dict]:
    return [dict(RULES[k], key=k, url=METHODOLOGY_URL) for k in keys]


# ── hours passages: runs of day/time tokens, split at street addresses ──────
_SIG = ("day", "daily", "range", "closed", "appt", "h24")
_CLOSED_ON = re.compile(r"\bclosed (?:on )?((?:mon|tue|wed|thu|fri|sat|sun)[a-z]*)", re.I)


def hours_runs(text: str) -> list[tuple[int, int]]:
    """Spans of `text` that read as an hours listing: consecutive day/time tokens with gaps
    <= 60 chars, broken at any street address (so two locations' hours never merge).
    Handles one-day-per-line ("Monday 10am-4pm · Tuesday ..."), ranges, Closed, by appointment."""
    text = text or ""
    streets = [m.start() for m in STREET_RE.finditer(text)]
    closed_on = {m.start(1): m.start() for m in _CLOSED_ON.finditer(text)}   # day pos -> "Closed on" pos
    runs, cur = [], None
    for m in _TOKEN_RX.finditer(text):
        if m.lastgroup not in _SIG:
            continue
        if cur and (m.start() - cur[1] > 60 or any(cur[1] <= sp < m.start() for sp in streets)):
            runs.append(tuple(cur))
            cur = None
        if cur is None:
            if m.lastgroup not in ("day", "daily"):
                continue
            cur = [m.start(), m.end()]
        else:
            cur[1] = m.end()
        if m.lastgroup == "day" and m.start() in closed_on and cur[0] == m.start():
            cur[0] = closed_on[m.start()]
    if cur:
        runs.append(tuple(cur))
    out = []
    for a, b in runs:
        p = parse_hours(text[a:b])
        if len(p["days"]) >= 2 and any(isinstance(v, list) for v in p["days"].values()):
            out.append((a, b))
    return out


# ── multi-location detection and location sections ─────────────────────────
MULTI_LOC_TEXT = re.compile(r"\b(our (other )?locations|all (of our )?locations|other locations|find a location|store locator|"
                            r"location finder|select (a |your )?location|choose (a |your )?location|change location|"
                            r"(two|three|four|five|six|several|multiple|\d{1,2}) (convenient )?locations\b)", re.I)
UP_TO_LOC = re.compile(r"up to [\d,]+ locations", re.I)


def _street_key(m) -> tuple[str, str]:
    return m.group(1), re.sub(r"^[nsew]\.?\s+", "", m.group(2).lower()).split()[0]


def address_anchors(text: str) -> list[tuple[int, str, str]]:
    return [(m.start(),) + _street_key(m) for m in STREET_RE.finditer(text or "")]


def local_addresses(text: str) -> set:
    """Distinct street addresses followed within 80 chars by a VA ZIP."""
    return {_street_key(m) for m in STREET_RE.finditer(text or "") if ZIP_RE.search(text[m.end(): m.end() + 80])}


def detect_multi(pages: list[dict], flags: dict | None = None) -> dict | None:
    """Multi-location site: 'N Locations' / 'two locations' wording, a location picker or
    menu, or several street+ZIP addresses across the site."""
    for p in pages:
        for m in MULTI_LOC_TEXT.finditer(p["text"]):
            if UP_TO_LOC.search(p["text"][max(0, m.start() - 20): m.end() + 5]):
                continue           # widget boilerplate ("up to 3 locations or up to 10,000 locations")
            return {"url": p["url"], "quote": snippet(p["text"], m.start(), m.end(), 200), "why": "site names several locations"}
    lm = (flags or {}).get("location_menu")
    if lm:
        return {"url": lm["url"], "quote": lm["quote"], "why": "location picker / locations menu in the page HTML", "evidence_type": "html_link"}
    addrs = set()
    for p in pages:
        addrs |= local_addresses(p["text"])
    if len(addrs) >= 2:
        return {"url": pages[0]["url"], "quote": None, "why": f"{len(addrs)} different street addresses with ZIPs across the site: "
                + "; ".join(f"{a} {b}" for a, b in sorted(addrs)[:4])}
    return None


def own_location(biz: dict, text: str, quote: str) -> str | None:
    """'own-page' when every street address on the page is the stored one; 'own-section' when
    the nearest street address before the quote (within 400 chars), and every address inside
    it, is the stored one; else None."""
    no, word = stored_street(biz)
    if not (no and word):
        return None
    nt, nq = nrm(text), nrm(quote).strip(" .,;:")
    anchors = address_anchors(nt)
    is_stored = lambda a: a[1] == no and a[2] == word.lower()
    if anchors and all(is_stored(a) for a in anchors):
        return "own-page"
    pos = nt.find(nq) if nq else -1
    if pos < 0:
        return None
    inside = [a for a in anchors if pos <= a[0] < pos + len(nq)]
    if inside:
        return "own-section" if all(is_stored(a) for a in inside) else None
    before = [a for a in anchors if pos - 400 <= a[0] < pos]
    if before and is_stored(before[-1]):
        return "own-section"
    return None


# ── contractor licence numbers (DPOR format 27xxxxxxxx) ──────────────────────
LIC_CTX = re.compile(r"licen[sc]|\blic\b|\blic\.|class [abc]\b|contractor|dpor", re.I)


def license_numbers(text: str) -> list[dict]:
    """'#2705069928' anywhere (footers), or a 27xxxxxxxx number within 80 chars of licence wording."""
    out = []
    for m in re.finditer(r"(?<![\d\-().])(27\d{8})(?![\d\-])", text or ""):
        pre = text[max(0, m.start() - 3): m.start()]
        ctx = text[max(0, m.start() - 80): m.end() + 20]
        if "#" in pre or LIC_CTX.search(ctx):
            if m.group(1) not in [x["number"] for x in out]:
                out.append({"number": m.group(1), "pos": m.start(), "why": "printed with '#'" if "#" in pre else "next to licence wording"})
    return out


def hours_disagree(a: dict, b: dict) -> list[str]:
    """Days both listings state with different values (a partial listing that agrees is not a conflict)."""
    return [d for d in DAYS if d in a["days"] and d in b["days"] and
            (sorted(a["days"][d]) if isinstance(a["days"][d], list) else a["days"][d]) !=
            (sorted(b["days"][d]) if isinstance(b["days"][d], list) else b["days"][d])]


def location_identity(biz: dict, text: str) -> list[str]:
    """Identity strong enough to tie a page to THIS location (location gate for auto):
    the stored street, or the stored ZIP printed in address form ("VA 22407"). A ZIP in a
    service-area list or a shared phone number does not count."""
    out = [h for h in identity_hits(biz, text) if h.startswith("street:")]
    z = str(biz.get("zip") or "").strip()
    if re.fullmatch(r"\d{5}", z) and re.search(r"\b(?:VA|Va\.?|Virginia),?\s+" + z + r"\b", text or ""):
        out.append("zip:" + z + " (address form)")
    return out
