#!/usr/bin/env python3
"""local-source-discover.py — Brave/SearXNG source discovery for the local grind.

THE FRONTIER PROBLEM this solves: a state legislator's scorecard `website` is their
official legislature bio (mgaleg.maryland.gov/Members/Details/... — committees + contact,
zero position statements), so local-politician-extract.py fetches it, finds nothing
quotable, and honestly scores nothing. Their actual position prose lives on a CAMPAIGN
site that isn't in the record (e.g. aaronkaufmand18.com — "Aaron Kaufman For Delegate").
This asks Brave for that site and enriches the batch so the extractor has something to read.

SAFETY: a discovered URL is only a HINT about where to look. The extractor still
verbatim-verifies every quote against the page it actually fetched and Gemma still
cross-checks polarity — so a wrong guess here can never produce a wrong score, only a
wasted fetch. Discovery widens coverage; it does not widen trust.

Brave access = openclaw.json → plugins.entries.brave.config.webSearch. `apiKey` may be a
plain string OR a SecretRef dict, and `baseUrl` normally points at the loopback budget
gate, which injects the key itself. Both are handled in brave_config(); do not go direct
to api.search.brave.com, that bypasses the metered budget.

SEARXNG FALLBACK (2026-10-14, MBP-1014-BURN): per the 10-08 search doctrine, SearXNG
(127.0.0.1:8888, self-hosted, no meter) is the bulk/grind lane. Brave is tried only when
it is configured AND not gated (plugin enabled). If Brave is gated, unconfigured, raises,
or returns 0 results, the same query goes to SearXNG's JSON API. Before this, a gated
Brave meant `SystemExit` and every round since 10-08 extracted from on-file sources only.
SearXNG is throttled (>= --searx-sleep s between queries, default 12.0) and is dropped for
the rest of the round after 3 consecutive failures, any HTTP 429, or junk answers that
outlast 2 waits on Google's own suspension (see Searcher). No CAPTCHA solving, no IP
rotation, no hammering a refusing engine. Override the URL with SEARXNG_URL.

Usage: local-source-discover.py BATCH.json OUT_BATCH.json [--max N] [--sleep S]
                                [--searx-sleep S] [--no-brave]
"""
import json, os, re, sys, time, urllib.parse, urllib.request

# Aggregators/news/socials/official pages — never a candidate's own position prose.
BAD_HOST = re.compile(
    r"ballotpedia|wikipedia|legiscan|pluralpolicy|votesmart|opensecrets|followthemoney|"
    r"vote411|justfacts|facebook|twitter|x\.com|linkedin|instagram|youtube|tiktok|"
    r"\.gov$|\.gov/|patch\.com|magazine|matters\.org|mymcmedia|axios|politico|nytimes|"
    r"washingtonpost|apnews|reuters|wusa9|wtop|baltimoresun|nbcwashington|actblue|winred|"
    r"campaignpartner|nationbuilder\.com$|linktr\.ee", re.I)
# A real campaign site announces itself in the title.
GOOD_TITLE = re.compile(
    r"\bfor (delegate|state senate|senate|senator|congress|house|governor|assembly|"
    r"representative|council|attorney general)\b|committee to elect|\bre-?elect\b|"
    r"\belect [A-Z]|for (md|va|tx|ga|pa|nc|az|wi|mi|oh|nv|mn)\b", re.I)
OFFICE_HINT = re.compile(r"delegate|senator|senate|representative|house|governor|assembly|council", re.I)


DEFAULT_BRAVE_BASE = "https://api.search.brave.com"


def _resolve_secret(v):
    """openclaw.json values may be a plain string OR a SecretRef dict. Resolve to a
    string or None — NEVER return the dict, which urllib would reject as a header
    value (`expected string or bytes-like object, got 'dict'`). That TypeError was
    caught per-candidate and swallowed, so the grind ran 47 days with 0 Brave queries
    (2026-08-22 → 2026-10-03) while logging a benign `+0 campaign site(s) found`."""
    if isinstance(v, str):
        return v or None
    if isinstance(v, dict):
        # {"source":"env","provider":"default","id":"OPENCLAW_BRAVE_API_KEY"}
        if v.get("source") == "env" and v.get("id"):
            return os.environ.get(v["id"]) or None
        return None
    return None


def brave_config():
    """(base_url, key_or_None), or None when Brave is gated or unusable. The key is
    optional when base_url is the loopback budget gate (`brave-search-budget.py
    serve-proxy`), which injects the real key itself and enforces the metered budget
    (soft_switch → DDG, hard_block). Going direct to api.search.brave.com would bypass
    that gate, so honour baseUrl. `plugins.entries.brave.enabled: false` is how the
    budget enforcer gates Brave — respect it. None means: SearXNG lane only."""
    base, key, enabled = DEFAULT_BRAVE_BASE, None, True
    try:
        cfg = json.load(open(os.path.expanduser("~/.openclaw/openclaw.json")))
        ent = cfg["plugins"]["entries"]["brave"]
        enabled = ent.get("enabled", True) is not False
        ws = ent["config"]["webSearch"]
        base = (ws.get("baseUrl") or DEFAULT_BRAVE_BASE).rstrip("/")
        key = _resolve_secret(ws.get("apiKey"))
    except Exception:
        pass
    if not enabled:
        print("brave: gated (plugins.entries.brave.enabled=false, budget switch) "
              "— using SearXNG")
        return None
    key = os.environ.get("BRAVE_API_KEY") or key
    is_loopback = urllib.parse.urlparse(base).hostname in ("127.0.0.1", "localhost", "::1")
    if not key and not is_loopback:
        print("brave: unavailable — API key not found (env BRAVE_API_KEY, or a resolvable "
              "openclaw.json plugins.entries.brave.config.webSearch.apiKey) "
              f"and baseUrl {base} is not the local budget proxy — using SearXNG")
        return None
    return base, key


def brave_search(cfg, q, count=8):
    base, key = cfg
    u = (f"{base}/res/v1/web/search?q=" + urllib.parse.quote(q)
         + f"&count={count}&country=us&result_filter=web")
    headers = {"Accept": "application/json"}
    if key:
        headers["X-Subscription-Token"] = key
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as r:
        j = json.load(r)
    return (j.get("web", {}) or {}).get("results") or []


DEFAULT_SEARX = "http://127.0.0.1:8888"


def searx_search(q, count=8):
    """SearXNG JSON API → ([{url,title}], unresponsive_engines). Results use the same
    shape the pickers read from Brave."""
    base = (os.environ.get("SEARXNG_URL") or DEFAULT_SEARX).rstrip("/")
    u = (f"{base}/search?q=" + urllib.parse.quote(q)
         + "&format=json&language=en-US&safesearch=0")
    req = urllib.request.Request(u, headers={"Accept": "application/json",
                                             "User-Agent": "moop-scorecard-discover/1"})
    with urllib.request.urlopen(req, timeout=25) as r:
        j = json.load(r)
    res = [{"url": x.get("url") or "", "title": x.get("title") or ""}
           for x in (j.get("results") or [])[:count]]
    return res, (j.get("unresponsive_engines") or [])


def _mentions(results, toks):
    """True if any result names the person (a surname token in url or title)."""
    for x in results:
        hay = (x.get("url", "") + " " + x.get("title", "")).lower().replace("-", "")
        if any(t in hay for t in toks):
            return True
    return False


class Searcher:
    """Brave (only when configured + not gated) → SearXNG fallback, with a polite
    SearXNG throttle and a per-round circuit breaker. Never raises on a lane failure
    that the other lane can absorb; raises only when no lane could answer.

    Observed 10-14: SearXNG's Google engine answers "unusual traffic" after a few quick
    queries and self-suspends ~180 s; meanwhile Bing (the only other live engine) returns
    first-word junk ("Guy" → dictionary pages). A junk answer (no result names the person)
    while Google is suspended → wait out that suspension once and retry the query once
    (at most SEARX_MAX_BACKOFF times a round), then stop: better blank than junk."""

    SUSPEND_WAIT = 200          # > SearXNG's 180 s too-many-requests suspension
    SEARX_MAX_BACKOFF = 2

    def __init__(self, brave_cfg, searx_sleep=12.0):
        self.brave = brave_cfg
        self.searx_sleep = searx_sleep
        self.searx_ok = True
        self.searx_fails = 0
        self.backoffs = 0
        self._last_searx = 0.0
        self.n = {"brave": 0, "searxng": 0, "brave_err": 0, "brave_empty": 0,
                  "searx_err": 0, "searx_junk": 0}

    def _searx_once(self, q, count):
        wait = self.searx_sleep - (time.time() - self._last_searx)
        if wait > 0:
            time.sleep(wait)
        self._last_searx = time.time()
        try:
            res, unresp = searx_search(q, count)
        except Exception as e:
            self.n["searx_err"] += 1
            self.searx_fails += 1
            code = getattr(e, "code", None)
            if code == 429 or self.searx_fails >= 3:
                self.searx_ok = False   # back off; never hammer a refusing engine
                print(f"  searxng: circuit open ({'HTTP 429' if code == 429 else '3 consecutive failures'})"
                      " — no more SearXNG queries this round")
            raise
        self.searx_fails = 0
        if os.environ.get("DISCOVER_DEBUG"):
            print(f"      searxng unresponsive: {unresp}")
            for x in res[:5]:
                print(f"      searxng> {x['url'][:90]} | {x['title'][:50]}")
        return res, unresp

    def _searx(self, q, count, toks):
        if not self.searx_ok:
            raise RuntimeError("searxng disabled for this round (circuit open)")
        res, unresp = self._searx_once(q, count)
        if toks and not _mentions(res, toks):
            google_down = any("google" in (e[0] if isinstance(e, (list, tuple)) else str(e)).lower()
                              for e in unresp)
            if google_down and self.backoffs < self.SEARX_MAX_BACKOFF:
                self.backoffs += 1
                print(f"  searxng: junk answer while Google is suspended — waiting "
                      f"{self.SUSPEND_WAIT}s, then one retry (backoff {self.backoffs}/{self.SEARX_MAX_BACKOFF})")
                time.sleep(self.SUSPEND_WAIT)
                res, unresp = self._searx_once(q, count)
            if not _mentions(res, toks):
                self.n["searx_junk"] += 1
                if google_down and self.backoffs >= self.SEARX_MAX_BACKOFF:
                    self.searx_ok = False
                    print("  searxng: Google still suspended after backoff, Bing returning junk "
                          "— no more SearXNG queries this round (better blank than junk)")
        self.n["searxng"] += 1
        return res

    def search(self, q, count=8, toks=None):
        if self.brave is not None:
            try:
                res = brave_search(self.brave, q, count)
                if res:
                    self.n["brave"] += 1
                    return res, "brave"
                self.n["brave_empty"] += 1
            except Exception as e:
                self.n["brave_err"] += 1
                code = getattr(e, "code", None)
                print(f"  brave error ({str(e)[:60]}) — falling back to SearXNG")
                if code in (401, 402, 403, 429):
                    self.brave = None   # gated / out of budget: stop paying for errors
        return self._searx(q, count, toks), "searxng"


def surname_toks(c):
    """Lower-case surname-ish tokens (4+ letters, not a suffix) for the junk check."""
    toks = [t for t in name_tokens(c.get("name")) if t not in ("iii", "junior", "senior")]
    return toks[-1:] or toks


def name_tokens(name):
    return [t.lower() for t in re.findall(r"[A-Za-z]{4,}", name or "")]


def pick_campaign_site(results, name):
    """Best plausible campaign/issues site, or None. Never guesses — no score, no pick."""
    toks = name_tokens(name)
    best, best_score = None, 0
    for r in results:
        url = r.get("url") or ""
        title = r.get("title") or ""
        host = urllib.parse.urlparse(url).netloc.lower()
        if not host or BAD_HOST.search(host) or BAD_HOST.search(url):
            continue
        score = 0
        if GOOD_TITLE.search(title):
            score += 5
        if any(t in host.replace("-", "") for t in toks):
            score += 3
        if OFFICE_HINT.search(title):
            score += 1
        if score > best_score:
            best, best_score = url.rstrip("/"), score
    return best if best_score >= 4 else None   # require a real signal, not a coincidence


def looks_thin(c):
    """True when the record's only 'website' is an official bio / nothing — i.e. the
    extractor has no quotable position source and discovery is worth a query."""
    if c.get("campaign_website"):
        return False
    w = (c.get("website") or "").lower()
    if not w:
        return True
    return bool(re.search(r"\.gov|legis|assembly|senate\.|house\.|mgaleg|capitol", w))


def main():
    src, out = sys.argv[1], sys.argv[2]
    mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 25
    slp = float(sys.argv[sys.argv.index("--sleep") + 1]) if "--sleep" in sys.argv else 0.4
    ssl = float(sys.argv[sys.argv.index("--searx-sleep") + 1]) if "--searx-sleep" in sys.argv else 12.0
    batch = json.load(open(src))
    bcfg = None if "--no-brave" in sys.argv else brave_config()
    S = Searcher(bcfg, searx_sleep=ssl)
    found = spent = rec_found = errors = 0

    # ---- Pass 2 target: the voting-RECORD page (LegiScan). For the ~2/3 of state legislators
    # with no campaign site, sponsorships/roll-calls are the quotable evidence — bill titles
    # appear verbatim on legiscan.com person pages, so the verbatim gate works unchanged.
    LEGISCAN_RE = re.compile(r"https?://legiscan\.com/[A-Z]{2}/people/[A-Za-z0-9_\-]+", re.I)

    lanes = {"brave": 0, "searxng": 0}
    for c in batch:
        if S.brave is None and not S.searx_ok:
            print("  no search lane left this round (Brave gated, SearXNG circuit open) — stopping")
            break
        if (c.get("level") == "state" and not c.get("records_website") and spent < mx):
            q2 = f'"{c.get("name")}" {c.get("state")} site:legiscan.com'
            try:
                res2, lane = S.search(q2, count=5, toks=surname_toks(c))
                spent += 1
                lanes[lane] += 1
                hit = next((m.group(0) for r in res2
                            for m in [LEGISCAN_RE.search(r.get("url") or "")] if m), None)
                if hit:
                    c["records_website"] = hit
                    c["records_discovered"] = True
                    rec_found += 1
                    print(f"  R {c['slug']:26} -> {hit}  [{lane}]")
            except Exception as e:
                errors += 1
                print(f"  search error (records) for {c['slug']}: {str(e)[:60]}")
            time.sleep(slp)
        if not looks_thin(c) or spent >= mx:
            continue
        office = (c.get("office") or "").split("(")[0].strip()
        q = f'"{c.get("name")}" {c.get("state")} {office} campaign issues'
        try:
            res, lane = S.search(q, toks=surname_toks(c))
            spent += 1
            lanes[lane] += 1
        except Exception as e:
            errors += 1
            print(f"  search error for {c['slug']}: {str(e)[:70]}")
            time.sleep(slp)
            continue
        site = pick_campaign_site(res, c.get("name"))
        if site:
            c["campaign_website"] = site
            c["source_discovered"] = True
            found += 1
            print(f"  + {c['slug']:26} -> {site}  [{lane}]")
        else:
            print(f"  . {c['slug']:26} (no campaign site found)  [{lane}]")
        time.sleep(slp)
    json.dump(batch, open(out, "w"), indent=1)
    print(f"wrote {out}: {found} campaign site(s) + {rec_found} records page(s) discovered "
          f"on {spent} quer(ies) (brave {lanes['brave']}, searxng {lanes['searxng']}; "
          f"brave errors {S.n['brave_err']}, brave empty {S.n['brave_empty']}, "
          f"searxng errors {S.n['searx_err']}, searxng off-target {S.n['searx_junk']}), {len(batch)} candidates in batch")

    # A round where EVERY query failed is a broken-search round, not a legitimately
    # empty one. Exit non-zero so the orchestrator logs "source discovery failed"
    # instead of the indistinguishable "+0 campaign site(s) found". This is the
    # signal that was missing for 47 days (see _resolve_secret).
    if errors and spent == 0:
        print(f"DISCOVERY BROKEN: all {errors} search attempt(s) raised; 0 queries "
              f"completed. Check SearXNG ({os.environ.get('SEARXNG_URL') or DEFAULT_SEARX}) "
              f"and the Brave key/baseUrl in openclaw.json.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
