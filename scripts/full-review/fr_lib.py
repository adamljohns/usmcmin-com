"""fr_lib.py — shared helpers for the RESOLUTE Citizen FULL REVIEW mode.

Everything that decides whether a proposed change survives lives here, so the patch builder,
the applier, and the tests all use one copy of each gate:

  * literal-quote matching (normalize case/whitespace/curly quotes only; nothing else)
  * the published rule text for every rubric cell (fetched from usmcmin.com, never invented)
  * per-question topic lexicons (deny-only: they can drop a finding, never create one)
  * the scope gate (this person, this office) and joint-statement detection
  * evidence ranking (roll call / bill sponsor > own official site > campaign > orgs > news)
  * the headline-grade calculation, copied from generate-profiles.py by import

Fetched pages are untrusted data. Nothing in this module executes or follows page content.
"""
import hashlib
import html as htmlmod
import importlib.util
import json
import os
import re
import ssl
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STATE_HOME = os.environ.get("FULL_REVIEW_HOME",
                            os.path.expanduser("~/.openclaw/state/scorecard-full-review"))
SCORECARD = os.path.join(REPO, "data", "scorecard.json")
PUBLIC_STATS = os.path.join(REPO, "data", "full-review-stats.json")

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
CTX = ssl.create_default_context()
CTX_LAX = ssl._create_unverified_context()

# Published methodology. Rule text for a score must be found on one of these pages.
METHOD_URL = "https://usmcmin.com/scoring-system.html"
CATEGORY_PAGE = {
    "sanctity_of_life": "sanctity-of-life", "biblical_marriage": "biblical-marriage",
    "family_child_sovereignty": "family-child-sovereignty", "christian_liberty": "christian-liberty",
    "economic_stewardship": "economic-stewardship", "election_integrity": "election-integrity",
    "border_immigration": "border-immigration", "self_defense": "self-defense-2a",
    "foreign_policy_restraint": "foreign-policy-restraint", "industry_capture": "industry-capture",
    "public_justice": "public-justice", "refuse_federal_overreach": "refuse-federal-overreach",
    "refuse_state_overreach": "refuse-state-overreach",
}
# The binary rule as printed on every category page, and the blank/slogan rules on the
# methodology page. These are quoted (and re-verified on the live page) in every score change.
BINARY_RULE = "Each question is binary (True / False / null). True earns +2 points."
BLANK_RULE = ("when our research finds no public position on a question, we leave it blank")
SLOGAN_RULE = 'Vague slogans ("fighting for families," "common sense") are not a position and stay blank.'
EVIDENCE_RULE = ("We use voting records, official statements, sponsored bills, campaign websites, "
                 "social media posts, and live debate or council-meeting footage.")
CURRENCY_RULE = ("When the record shows a candidate has withdrawn or been defeated, we mark it rather "
                 "than leave a stale")

# PAC / foreign-lobby cells are affirmative database searches (FEC / OpenSecrets / TrackAIPAC).
# Page text can never answer them; the review only reports hit / no-hit / not-run.
PAC_CELLS = {("sanctity_of_life", 4), ("foreign_policy_restraint", 3)}
MAX_CELLS_PER_QUOTE = 2


# ----------------------------------------------------------------------------- text
_QUOTES = {"‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
           "“": '"', "”": '"', "„": '"', "″": '"',
           "–": "-", "—": "-", "‒": "-", "−": "-", " ": " ",
           "…": "..."}


def norm_with_map(s):
    """Normalized string (lowercase, straight quotes, single spaces) plus, for every output
    character, the index of the source character it came from. Lets us cut the EXACT page
    substring that matched, so the stored quote is literally what the page says."""
    out, idx = [], []
    prev_space = True
    for i, ch in enumerate(s or ""):
        ch = _QUOTES.get(ch, ch)
        ch = unicodedata.normalize("NFKC", ch)
        for c in ch:
            if c.isspace():
                if prev_space:
                    continue
                out.append(" "); idx.append(i); prev_space = True
            else:
                out.append(c.lower()); idx.append(i); prev_space = False
    while out and out[-1] == " ":
        out.pop(); idx.pop()
    return "".join(out), idx


def norm(s):
    return norm_with_map(s)[0]


def find_literal(quote, text):
    """Return (start, end) of quote inside text under normalization, else None."""
    nq = norm(quote).strip(" .\"'")
    if len(nq) < 12:
        return None
    nt, idx = norm_with_map(text)
    k = nt.find(nq)
    if k < 0:
        return None
    return idx[k], idx[k + len(nq) - 1] + 1


def exact_quote(quote, text):
    """The page's own characters for a normalized match (or None)."""
    span = find_literal(quote, text)
    if not span:
        return None
    return text[span[0]:span[1]]


def context_of(quote, text, width=300):
    span = find_literal(quote, text)
    if not span:
        return ""
    a, b = max(0, span[0] - width), min(len(text), span[1] + width)
    return text[a:b]


def html_to_text(raw):
    """Readable page text. Menus, headers, footers and sidebars are dropped so the model reads the
    page's own content; quotes are still verified against this same text."""
    raw = re.sub(r"<(script|style|noscript|svg|template)[^>]*>.*?</\1>", " ", raw or "", flags=re.S | re.I)
    raw = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    m = re.search(r"<main\b[^>]*>(.*)</main>", raw, flags=re.S | re.I)
    if m and len(re.sub(r"<[^>]+>", "", m.group(1)).strip()) > 400:
        raw = m.group(1)
    else:
        raw = re.sub(r"<(nav|header|footer|aside)\b[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    raw = re.sub(r"<br\s*/?>|</(p|div|li|h[1-6]|tr|section|article)>", "\n", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", " ", raw)
    t = htmlmod.unescape(raw)
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()


def sha(s):
    return hashlib.sha1(s.encode("utf-8", "replace")).hexdigest()[:16]


# ----------------------------------------------------------------------------- fetch
class Fetcher:
    """Polite fetcher: browser UA, at most one request per second per host, page cache on disk.
    Pages are stored as files so the independent verifier can read exactly what we read."""

    def __init__(self, page_dir, min_interval=1.05):
        self.page_dir = page_dir
        os.makedirs(page_dir, exist_ok=True)
        self.last = {}
        self.min_interval = min_interval
        self.index_path = os.path.join(page_dir, "index.json")
        self.index = json.load(open(self.index_path)) if os.path.exists(self.index_path) else {}

    def _wait(self, host):
        t = self.last.get(host, 0)
        d = time.time() - t
        if d < self.min_interval:
            time.sleep(self.min_interval - d)
        self.last[host] = time.time()

    def save_index(self):
        tmp = self.index_path + ".tmp"
        json.dump(self.index, open(tmp, "w"), indent=0)
        os.replace(tmp, self.index_path)

    def get(self, url, timeout=25, max_bytes=2_500_000, allow_archive=True):
        """-> dict(url, final_url, status, ok, kind, text_file, raw_file, archive_of, error)."""
        if url in self.index:
            return self.index[url]
        rec = self._get(url, timeout, max_bytes)
        if allow_archive and not rec["ok"] and rec.get("status") in (403, 429, 503, None) \
                and "web.archive.org" not in url:
            arch = self._archive(url, timeout, max_bytes)
            if arch and arch["ok"]:
                rec["archive_fallback"] = arch["url"]
                self.index[url] = rec
                self.index[arch["url"]] = arch
                self.save_index()
                return arch
        self.index[url] = rec
        self.save_index()
        return rec

    def _get(self, url, timeout, max_bytes):
        host = urllib.parse.urlparse(url).netloc.lower()
        self._wait(host)
        rec = {"url": url, "final_url": url, "status": None, "ok": False, "fetched": time.strftime("%Y-%m-%dT%H:%M:%S")}
        req = urllib.request.Request(url, headers={
            "User-Agent": UA, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9"})
        try:
            try:
                r = urllib.request.urlopen(req, timeout=timeout, context=CTX)
            except urllib.error.URLError as e:
                if isinstance(getattr(e, "reason", None), ssl.SSLError):
                    r = urllib.request.urlopen(req, timeout=timeout, context=CTX_LAX)
                else:
                    raise
            with r:
                raw_b = r.read(max_bytes)
                rec["status"] = r.status
                rec["final_url"] = r.geturl()
                ctype = r.headers.get("Content-Type", "")
                charset = "utf-8"
                m = re.search(r"charset=([\w-]+)", ctype)
                if m:
                    charset = m.group(1)
                raw = raw_b.decode(charset, "replace")
        except urllib.error.HTTPError as e:
            rec["status"] = e.code
            rec["error"] = f"HTTP {e.code}"
            return rec
        except Exception as e:
            rec["error"] = f"{type(e).__name__}: {str(e)[:120]}"
            return rec
        if "pdf" in ctype.lower():
            rec["error"] = "pdf (not parsed)"
            return rec
        is_xml = "xml" in ctype.lower() and "html" not in ctype.lower()
        text = raw if is_xml else html_to_text(raw)
        if re.search(r"Attention Required! \| Cloudflare|Just a moment\.\.\.|Sorry, you have been blocked",
                     raw[:4000]):
            rec["status"] = 403
            rec["error"] = "bot wall"
            return rec
        key = sha(url)
        rf = os.path.join(self.page_dir, key + (".xml" if is_xml else ".html"))
        tf = os.path.join(self.page_dir, key + ".txt")
        open(rf, "w").write(raw)
        open(tf, "w").write(text)
        rec.update(ok=True, kind="xml" if is_xml else "html", raw_file=os.path.basename(rf),
                   text_file=os.path.basename(tf), chars=len(text))
        return rec

    def _archive(self, url, timeout, max_bytes):
        """Wayback copy of an official page that blocks us (e.g. CivicPlus/Cloudflare). The copy is
        cited by its own web.archive.org URL; evidence from it is never auto-applied."""
        api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
        r = self._get(api, timeout, 200_000)
        if not r["ok"]:
            return None
        try:
            j = json.loads(open(os.path.join(self.page_dir, r["raw_file"])).read())
            snap = j["archived_snapshots"]["closest"]
            if not snap.get("available") or str(snap.get("status")) != "200":
                return None
            ts = snap["timestamp"]
        except Exception:
            return None
        aurl = f"https://web.archive.org/web/{ts}id_/{url}"
        rec = self._get(aurl, timeout, max_bytes)
        rec["archive_of"] = url
        rec["archive_timestamp"] = ts
        return rec

    def text(self, rec):
        if not rec or not rec.get("ok"):
            return ""
        return open(os.path.join(self.page_dir, rec["text_file"]), encoding="utf-8", errors="replace").read()

    def raw(self, rec):
        if not rec or not rec.get("ok"):
            return ""
        return open(os.path.join(self.page_dir, rec["raw_file"]), encoding="utf-8", errors="replace").read()


# ----------------------------------------------------------------------------- scorecard
_GP = None


def gp():
    """generate-profiles.py imported as a module, so headline math is the site's own math."""
    global _GP
    if _GP is None:
        if REPO not in sys.path:
            sys.path.insert(0, REPO)
        spec = importlib.util.spec_from_file_location("generate_profiles", os.path.join(REPO, "generate-profiles.py"))
        mod = importlib.util.module_from_spec(spec)
        cwd = os.getcwd()
        os.chdir(REPO)
        try:
            spec.loader.exec_module(mod)
        finally:
            os.chdir(cwd)
        _GP = mod
    return _GP


def tier_of(c):
    return gp().classify_office_tier(c) or "federal"


def headline(c, categories):
    """(pct, letter, answered, backed) exactly as generate-profiles.py renders the headline.
    letter is None when the grade is withheld (thin record)."""
    g = gp()
    tier = tier_of(c)
    total = g.calc_total(c.get("scores") or {}, categories, tier)
    adj = sum(int((v or {}).get("delta") or 0) for v in ((c.get("profile") or {}).get("score_adjustments") or {}).values())
    adjusted = total["score"] + adj
    answered = total["answered"]
    backed = g.backed_answer_count(c)
    if answered < 10 or backed < 5:
        return {"pct": max(0, min(100, round(adjusted / g.MAX_TOTAL * 100))), "letter": None,
                "answered": answered, "backed": backed}
    mx = answered * g.POINTS_PER_TRUE
    pct = max(0, min(100, round(adjusted / mx * 100))) if mx else 0
    return {"pct": pct, "letter": g.letter_grade(pct), "answered": answered, "backed": backed}


def applicable_cells(categories, rubrics, tier):
    """[(cat_id, qi, question_text)] — tier rubric, applicable_at, per-entry tier wording."""
    qkey = {"federal": "questions", "state": "questions_state", "local": "questions_local"}[tier]
    rub = set(rubrics[tier]["pillar_a"] + rubrics[tier]["pillar_b"])
    out = []
    for cat in categories:
        if cat["id"] not in rub:
            continue
        base = cat.get("questions") or []
        var = cat.get(qkey) or []
        appl = cat.get("applicable_at") or []
        for qi in range(5):
            q = (var[qi] if qi < len(var) else None) or (base[qi] if qi < len(base) else None)
            if q and qi < len(appl) and tier in (appl[qi] or []):
                out.append((cat["id"], qi, q))
    return out


def cell_citations(c, cat, qi):
    """URLs that currently back cell (cat, qi): answer_footnotes refs + claims[] sources."""
    urls = []
    fns = c.get("footnotes") or {}
    refs = ((c.get("answer_footnotes") or {}).get(cat) or [])
    for fid in (refs[qi] if qi < len(refs) else []) or []:
        u = (fns.get(fid) or {}).get("url")
        if u:
            urls.append(u)
    for cl in c.get("claims") or []:
        if cl.get("category") == cat and cl.get("question_idx") == qi:
            urls.extend(cl.get("sources") or [])
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u); out.append(u)
    return out


def cell_kind(c, cat, qi):
    for cl in c.get("claims") or []:
        if cl.get("category") == cat and cl.get("question_idx") == qi and cl.get("kind"):
            return cl["kind"]
    fns = c.get("footnotes") or {}
    refs = ((c.get("answer_footnotes") or {}).get(cat) or [])
    for fid in (refs[qi] if qi < len(refs) else []) or []:
        if "platform" in str((fns.get(fid) or {}).get("title", "")).lower():
            return "party_platform"
    return None


def is_fxbg_or_va(c):
    blob = " ".join(str(c.get(k) or "") for k in ("jurisdiction", "office", "district")).lower()
    return (c.get("state") or "").upper() == "VA" or "fredericksburg" in blob


def is_fxbg(c):
    blob = " ".join(str(c.get(k) or "") for k in ("jurisdiction", "office")).lower()
    return "fredericksburg" in blob


# ----------------------------------------------------------------------------- rules
class Rules:
    """Rule text comes only from the published pages. load() fetches them live; a cell whose
    question text cannot be found on its published category page has no rule and cannot score."""

    def __init__(self, fetcher):
        self.f = fetcher
        self.pages = {}

    def load(self):
        urls = [METHOD_URL] + [f"https://usmcmin.com/citizen/{s}.html" for s in CATEGORY_PAGE.values()]
        for u in urls:
            rec = self.f.get(u, allow_archive=False)
            self.pages[u] = self.f.text(rec) if rec.get("ok") else ""
        return {u: bool(t) for u, t in self.pages.items()}

    def find(self, url, needle):
        t = self.pages.get(url) or ""
        return exact_quote(needle, t)

    def for_cell(self, cat, qi, question):
        url = f"https://usmcmin.com/citizen/{CATEGORY_PAGE[cat]}.html"
        variants = [question]
        stripped = re.sub(r"^(Candidate|Official)(\s*\([^)]*\))?\s+", "", question.strip())
        variants += [stripped, re.sub(r"\s*\([^)]*\)\s*", " ", stripped).strip()]
        for v in variants:
            hit = self.find(url, v)
            if hit:
                ctx = self.find(url, BINARY_RULE)
                return {"text": hit, "context": ctx or None, "url": url}
        # federal wording is also printed on the methodology page
        for v in variants:
            hit = self.find(METHOD_URL, v)
            if hit:
                return {"text": hit, "context": self.find(url, BINARY_RULE), "url": METHOD_URL}
        return None

    def general(self, which):
        txt = {"blank": BLANK_RULE, "slogan": SLOGAN_RULE, "evidence": EVIDENCE_RULE,
               "currency": CURRENCY_RULE}[which]
        hit = self.find(METHOD_URL, txt)
        return {"text": hit, "url": METHOD_URL} if hit else None


# ----------------------------------------------------------------------------- topic gate
# Deny-only: a finding whose quote has none of its cell's words is off topic and is dropped.
# "t" words are needed for a TRUE verdict, "f" words for FALSE ("a" counts for both).
W = lambda *xs: [re.compile(x, re.I) for x in xs]
LEX = {
    ("sanctity_of_life", 0): {"a": W(r"concep", r"personhood", r"unborn", r"pre-?born", r"pro-?life", r"abortion",
                                     r"life begins", r"right to life", r"heartbeat", r"sanctity of (human )?life", r"roe\b",
                                     r"reproductive (freedom|rights|health)", r"right to choose", r"pro-?choice")},
    ("sanctity_of_life", 1): {"t": W(r"abolish", r"abolition", r"end abortion", r"(ban|outlaw|prohibit)\w*\s+(all\s+)?abortion",
                                     r"abortion\s+ban", r"criminaliz"),
                              "f": W(r"abortion", r"roe\b", r"reproductive (freedom|rights|health|care)", r"right to choose",
                                     r"pro-?choice", r"women'?s health protection act")},
    ("sanctity_of_life", 2): {"a": W(r"stem[- ]cell", r"embryo", r"\bivf\b", r"in vitro", r"chimer", r"clon")},
    ("sanctity_of_life", 3): {"a": W(r"euthanas", r"assisted (suicide|death|dying)", r"aid in dying", r"death with dignity",
                                     r"end[- ]of[- ]life", r"rationing")},
    ("biblical_marriage", 0): {"a": W(r"marriage", r"one man and one woman", r"husband and wife")},
    ("biblical_marriage", 1): {"a": W(r"same[- ]sex", r"civil union", r"domestic partner", r"marriage equality",
                                      r"respect for marriage", r"obergefell", r"gay marriage", r"marriage")},
    ("biblical_marriage", 2): {"a": W(r"transgender", r"gender identity", r"biological (sex|male|female|girls|boys|women|men)",
                                      r"gender[- ]affirming", r"sex change", r"(women|girls)'?s? sports", r"bathroom",
                                      r"locker room", r"pronoun", r"two sexes", r"gender transition")},
    ("biblical_marriage", 3): {"a": W(r"divorce", r"covenant marriage", r"marriage penalty", r"strengthen\w*[^.]{0,30}marriage")},
    ("biblical_marriage", 4): {"a": W(r"lgbt", r"\bpride\b", r"\bgay\b", r"lesbian", r"transgender", r"sexual orientation",
                                      r"gender identity", r"equality act", r"\bdrag\b", r"queer")},
    ("family_child_sovereignty", 0): {"a": W(r"school choice", r"voucher", r"home[- ]?school", r"charter school",
                                             r"education savings", r"\besas?\b", r"parental choice", r"educational freedom",
                                             r"education freedom", r"tuition", r"backpack")},
    ("family_child_sovereignty", 1): {"a": W(r"parental (rights|notification|consent|involvement)", r"parents'? (right|bill of rights)",
                                             r"notify (the )?parents", r"parents? (must|should) (be|know|consent)",
                                             r"without (their )?parents'? (knowledge|consent)")},
    ("family_child_sovereignty", 2): {"a": W(r"\bcrt\b", r"critical race", r"\bsogi\b", r"sex(ual)? ed", r"gender ideology",
                                             r"curricul", r"indoctrinat", r"\bdei\b", r"diversity, equity")},
    ("family_child_sovereignty", 3): {"a": W(r"pornograph", r"age[- ]verification", r"obscen", r"sexuali[sz]", r"\bcsam\b",
                                             r"child sexual abuse material", r"sexually explicit")},
    ("family_child_sovereignty", 4): {"a": W(r"adopt", r"foster")},
    ("christian_liberty", 0): {"a": W(r"\bfaith", r"christ", r"religious (freedom|liberty|expression)", r"\bpray", r"\bgod\b",
                                      r"jesus", r"free exercise", r"church")},
    ("christian_liberty", 1): {"a": W(r"conscience", r"religious (exemption|freedom|liberty)", r"\brfra\b",
                                      r"religious freedom restoration")},
    ("christian_liberty", 2): {"a": W(r"compelled speech", r"pronoun", r"hate[- ]speech", r"free speech", r"censor")},
    ("christian_liberty", 3): {"a": W(r"\bprayer", r"ten commandments", r"nativity", r"in god we trust", r"chaplain",
                                      r"sabbath", r"blue law", r"christian (symbol|display)", r"religious display", r"\bcross\b")},
    ("christian_liberty", 4): {"a": W(r"ramadan", r"satanic", r"diwali", r"\beid\b", r"islamic", r"religious (display|holiday)",
                                      r"non-christian")},
    ("economic_stewardship", 0): {"a": W(r"\bcbdc\b", r"central bank digital", r"digital (currency|dollar)", r"\bcash\b",
                                         r"crypto", r"bitcoin", r"stablecoin")},
    ("economic_stewardship", 1): {"a": W(r"\bgold\b", r"silver", r"sound money", r"federal reserve", r"audit the fed",
                                         r"end the fed")},
    ("economic_stewardship", 2): {"a": W(r"deficit", r"balanced budget", r"national debt", r"\bdebt\b", r"spending",
                                         r"borrow", r"tax (increase|hike|rate)", r"bond issu")},
    ("economic_stewardship", 3): {"a": W(r"usury", r"interest[- ]rate cap", r"payday", r"predatory lend", r"tithe",
                                         r"charitable deduction")},
    ("economic_stewardship", 4): {"a": W(r"\besg\b", r"\bwef\b", r"davos", r"world economic forum", r"anti-?trust",
                                         r"monopol", r"blackrock", r"cartel", r"debank")},
    ("election_integrity", 0): {"a": W(r"paper ballot", r"hand[- ]count", r"voting machine", r"electronic voting", r"tabulator")},
    ("election_integrity", 1): {"a": W(r"voter id", r"photo id", r"photo identification", r"proof of citizenship",
                                       r"citizenship (verification|check)", r"\bsave act\b", r"non-?citizen")},
    ("election_integrity", 2): {"a": W(r"early voting", r"election day", r"absentee", r"same[- ]day")},
    ("election_integrity", 3): {"a": W(r"mail[- ]in", r"mail ballot", r"drop box", r"ballot harvest", r"vote by mail",
                                       r"universal mail")},
    ("election_integrity", 4): {"a": W(r"zuckerbucks", r"private (funding|money|grants?)", r"\bctcl\b",
                                       r"foreign[^.]{0,30}(interference|money|influence)")},
    ("border_immigration", 0): {"a": W(r"border wall", r"\bwall\b", r"border (security|barrier|patrol)", r"national guard",
                                       r"secure (the|our) border")},
    ("border_immigration", 1): {"a": W(r"deport", r"illegal (alien|immigra)", r"undocumented", r"amnesty", r"\bdaca\b",
                                       r"dreamers?", r"\bice\b", r"immigration enforcement", r"path(way)? to citizenship")},
    ("border_immigration", 2): {"a": W(r"sanctuary", r"detainer", r"287\(g\)", r"cooperat\w*[^.]{0,30}(ice|immigration)")},
    ("border_immigration", 3): {"a": W(r"e-?verify")},
    ("border_immigration", 4): {"a": W(r"birthright", r"foreign ownership", r"farmland", r"foreign adversar\w*[^.]{0,40}land",
                                       r"chin\w*[^.]{0,40}land")},
    ("self_defense", 0): {"a": W(r"constitutional carry", r"permitless", r"concealed carry", r"carry permit", r"right to carry")},
    ("self_defense", 1): {"a": W(r"red[- ]flag", r"magazine", r"assault (weapon|rifle)", r"registr", r"background check",
                                 r"gun (control|safety|violence)", r"firearm", r"second amendment", r"\b2a\b", r"\bguns?\b")},
    ("self_defense", 2): {"a": W(r"\bnfa\b", r"national firearms act", r"gun control act", r"suppressor", r"short[- ]barrel")},
    ("self_defense", 3): {"a": W(r"castle doctrine", r"stand[- ]your[- ]ground", r"self[- ]defense")},
    ("self_defense", 4): {"a": W(r"\batf\b", r"arms trade treaty", r"disarm", r"pistol brace", r"confiscat")},
    ("foreign_policy_restraint", 0): {"a": W(r"war powers", r"article i\b", r"declar\w* war",
                                             r"(congressional|congress)[^.]{0,30}authori[sz]")},
    ("foreign_policy_restraint", 1): {"a": W(r"\baumf\b", r"forever war", r"endless war", r"withdraw", r"bring (our )?troops home")},
    ("foreign_policy_restraint", 2): {"a": W(r"foreign aid", r"aid to", r"persecut", r"assistance to")},
    ("foreign_policy_restraint", 4): {"a": W(r"\bwho\b", r"world health", r"united nations", r"\bu\.n\.", r"\bnato\b",
                                             r"globalis", r"supranational", r"sovereignty")},
    ("industry_capture", 0): {"a": W(r"mandate", r"vaccin", r"informed consent", r"medical freedom", r"covid")},
    ("industry_capture", 1): {"a": W(r"liability", r"\bncvia\b", r"prep act", r"vaccine injur")},
    ("industry_capture", 2): {"a": W(r"big ag", r"monsanto", r"bayer", r"cargill", r"meatpack", r"anti-?trust",
                                     r"consolidation")},
    ("industry_capture", 3): {"a": W(r"raw milk", r"small farm", r"family farm", r"farmers?\b", r"\busda\b", r"\bepa\b")},
    ("industry_capture", 4): {"a": W(r"pentagon audit", r"defense contractor", r"revolving door", r"\baudit",
                                     r"military[- ]industrial")},
    ("public_justice", 0): {"a": W(r"police", r"law enforcement", r"officers", r"defund", r"sheriff", r"first responders",
                                   r"back the blue")},
    ("public_justice", 1): {"a": W(r"\bbail\b", r"soft[- ]on[- ]crime", r"prosecutor", r"cashless", r"criminal justice reform")},
    ("public_justice", 2): {"a": W(r"victim", r"restitution", r"punish", r"sentenc")},
    ("public_justice", 3): {"a": W(r"violent crime", r"public health")},
    ("public_justice", 4): {"a": W(r"\bsword\b", r"romans 13", r"magistrate", r"punish\w* (evil|wrongdo)")},
    ("refuse_federal_overreach", 0): {"a": W(r"tenth amendment", r"10th amendment", r"nullif", r"anti-?commandeer")},
    ("refuse_federal_overreach", 1): {"a": W(r"federal (mandate|strings|funds|overreach)", r"unconstitutional")},
    ("refuse_federal_overreach", 2): {"a": W(r"federal overreach", r"federal government", r"washington")},
    ("refuse_federal_overreach", 3): {"a": W(r"state sovereignty", r"tenth amendment", r"10th amendment", r"states'? rights",
                                             r"federal overreach")},
    ("refuse_federal_overreach", 4): {"a": W(r"federal[^.]{0,40}(election|data|land)", r"real id")},
    ("refuse_state_overreach", 0): {"a": W(r"local control", r"state mandate", r"general assembly", r"dillon", r"home rule")},
    ("refuse_state_overreach", 1): {"a": W(r"state (mandate|strings|funds)", r"unfunded mandate")},
    ("refuse_state_overreach", 2): {"a": W(r"lockdown", r"mandate", r"\besg\b", r"state overreach")},
    ("refuse_state_overreach", 3): {"a": W(r"subsidiarity", r"local control", r"home rule", r"closest to the people")},
    ("refuse_state_overreach", 4): {"a": W(r"state directive", r"refus\w* to enforce", r"unconstitutional")},
}


def on_topic(cat, qi, verdict, quote):
    lx = LEX.get((cat, qi))
    if not lx:
        return False, "no topic lexicon for this cell"
    pats = list(lx.get("a", [])) + list(lx.get("t" if verdict else "f", []))
    hits = [p.pattern for p in pats if p.search(quote or "")]
    return (bool(hits), hits[:3] if hits else "quote has no word on this question's topic")


SLOGAN = re.compile(r"^\W*(fighting for (families|you|our)|common[- ]sense|freedom\W*$|liberty\W*$|"
                    r"putting (people|families|virginia|america) first|working for you)", re.I)


def is_slogan(quote):
    words = re.findall(r"[A-Za-z']+", quote or "")
    return len(words) < 6 or bool(SLOGAN.search(quote or "") and len(words) < 12)


# ----------------------------------------------------------------------------- scope gate
SUFFIX = re.compile(r"\s+(jr|sr|ii|iii|iv)\.?$", re.I)


def name_parts(name):
    n = SUFFIX.sub("", re.sub(r"\([^)]*\)|\"[^\"]*\"", " ", name or "")).strip()
    parts = [p for p in re.split(r"[\s,]+", n) if p and not re.match(r"^[A-Z]\.?$", p)]
    if not parts:
        return "", ""
    return parts[0], parts[-1]


def domain(u):
    h = urllib.parse.urlparse(u or "").netloc.lower()
    return h[4:] if h.startswith("www.") else h


def own_domains(c):
    p = c.get("profile") or {}
    ds = set()
    for u in (c.get("website"), p.get("campaign_website")):
        d = domain(u)
        # a shared city/county/legislature host is NOT the person's own domain
        if d and not re.search(r"(fredericksburgva\.gov|virginia\.gov|vga\.virginia|\.state\.|legis|ballotpedia|"
                               r"wikipedia|facebook|twitter|x\.com|linkedin)", d):
            ds.add(d)
    return ds


def page_names_person(text, c):
    first, last = name_parts(c.get("name"))
    t = norm(text)
    if not last or norm(last) not in t:
        return False
    nf, nl = norm(first), norm(last)
    # first name (or its first 3 letters, Rob/Robert) within two tokens of the surname, or "Last, First"
    if first and (re.search(r"\b" + re.escape(nf[:3]) + r"[\w'.-]*\s+([\w'.\"-]+\s+){0,2}" + re.escape(nl) + r"\b", t)
                  or re.search(r"\b" + re.escape(nl) + r",\s*" + re.escape(nf[:3]), t)):
        return True
    # nickname / initial forms: surname next to a title word
    return bool(re.search(r"(rep\.|representative|senator|sen\.|delegate|del\.|mayor|councilm|supervisor|sheriff|"
                          r"governor|judge|commissioner)\s+(\w+\s+){0,2}" + re.escape(norm(last)), t))


JOINT = re.compile(r"joint statement|joined (by )?(senators?|reps?\.|representatives?|colleagues)|along with (senators?|reps?\.|"
                   r"representatives?|delegates?|colleagues)|led by (senators?|reps?\.|representatives?)|"
                   r"(senators?|reps?\.|representatives?|delegates?) [A-Z][a-z]+ and [A-Z][a-z]+", re.I)


def scope_check(c, page_url, page_text, quote, context):
    """-> (ok, reason, flags). ok=False drops the finding. 'joint' flags send it to HOLD."""
    first, last = name_parts(c.get("name"))
    own = domain(page_url) in own_domains(c) or any(domain(page_url).endswith("." + d) for d in own_domains(c))
    flags = []
    if not page_names_person(page_text, c):
        return False, "page does not name this official (first + last name)", flags
    lq, lc = norm(quote), norm(context)
    first_person = bool(re.search(r"\b(i|i'm|i've|i'll|my|me)\b", lq))
    names_them = norm(last) in lq or norm(last) in lc
    if not own and not names_them:
        return False, "third-party page: quote and its context do not name this official", flags
    if own and not (first_person or names_them or norm(last) in norm(page_text[:3000])):
        return False, "own-site page but passage is not attributable to this official", flags
    if JOINT.search(context or ""):
        flags.append("joint-statement")
    # another person's name as the actor right before the quote (predecessor / colleague)
    m = re.search(r"([A-Z][a-z]+ [A-Z][a-z]+)\s+(said|stated|introduced|sponsored|voted|wrote)\b",
                  (context or "")[:max(0, (context or "").find(quote[:20]))] if quote else "")
    if m and norm(last) not in norm(m.group(1)):
        flags.append(f"other actor named: {m.group(1)}")
    return True, ("own site" if own else "names official"), flags


# ----------------------------------------------------------------------------- ranking
ROLLCALL = re.compile(r"clerk\.house\.gov/(evs|votes)|senate\.gov/legislative/lis/roll_call|lis\.virginia\.gov/.*vote|"
                      r"/roll-?call", re.I)
SPONSOR = re.compile(r"congress\.gov/bill/|lis\.virginia\.gov/bill-details|lis\.virginia\.gov/cgi-bin/legp604", re.I)
ORGS = re.compile(r"sbaprolife|nrapvf|nra-?ila|ivoterguide|vote411|heritageaction|plannedparenthood|hrc\.org|"
                  r"emilyslist|reproductivefreedom|everytown|momsdemand|giffords", re.I)
NEWS = re.compile(r"ballotpedia|wikipedia|patch\.com|fxbgadvance|freelancestar|fredericksburg\.com|richmond\.com|"
                  r"virginiamercury|cardinalnews|apnews|thehill|washingtonpost|nytimes|politico|vpap", re.I)


def source_rank(url, c):
    """1 roll call / sponsor field · 2 the official's own government site · 3 campaign site ·
    4 endorsing or rating organization · 5 news / aggregator (Ballotpedia, Wikipedia, press)."""
    u = url or ""
    if "web.archive.org" in u:
        u = re.sub(r"^https?://web\.archive\.org/web/\d+(id_)?/", "", u)
    if ROLLCALL.search(u) or SPONSOR.search(u):
        return 1, "official roll-call / bill record"
    d = domain(u)
    off = domain(c.get("website"))
    camp = domain((c.get("profile") or {}).get("campaign_website"))
    govish = bool(re.search(r"\.gov$|\.state\.[a-z]{2}\.us$|\.va\.us$|legis", d))
    if govish and d == off:
        return 2, "official's own government page"
    if (camp and d == camp) or d in own_domains(c):
        return 3, "campaign / personal site"
    if ORGS.search(d):
        return 4, "endorsing / rating organization"
    if govish:
        return 2, "government page naming the official"
    return 5, "news / aggregator"


def load_json(p, default=None):
    try:
        return json.load(open(p))
    except Exception:
        return default


def dump_json(p, obj, indent=1):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=indent, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, p)
