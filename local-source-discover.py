#!/usr/bin/env python3
"""local-source-discover.py — Brave-powered source discovery for the local grind.

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

Brave key = the ONE fleet key (openclaw.json → plugins.entries.brave.config.webSearch.apiKey).

Usage: local-source-discover.py BATCH.json OUT_BATCH.json [--max N] [--sleep S]
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


def brave_key():
    if os.environ.get("BRAVE_API_KEY"):
        return os.environ["BRAVE_API_KEY"]
    cfg = json.load(open(os.path.expanduser("~/.openclaw/openclaw.json")))
    try:
        return cfg["plugins"]["entries"]["brave"]["config"]["webSearch"]["apiKey"]
    except Exception:
        raise SystemExit("Brave API key not found (env BRAVE_API_KEY or openclaw.json "
                         "plugins.entries.brave.config.webSearch.apiKey)")


def brave_search(key, q, count=8):
    u = ("https://api.search.brave.com/res/v1/web/search?q=" + urllib.parse.quote(q)
         + f"&count={count}&country=us&result_filter=web")
    req = urllib.request.Request(u, headers={"Accept": "application/json",
                                             "X-Subscription-Token": key})
    with urllib.request.urlopen(req, timeout=15) as r:
        j = json.load(r)
    return (j.get("web", {}) or {}).get("results") or []


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
    batch = json.load(open(src))
    key = brave_key()
    found = spent = 0
    for c in batch:
        if not looks_thin(c) or spent >= mx:
            continue
        office = (c.get("office") or "").split("(")[0].strip()
        q = f'"{c.get("name")}" {c.get("state")} {office} campaign issues'
        try:
            res = brave_search(key, q)
            spent += 1
        except Exception as e:
            print(f"  brave error for {c['slug']}: {str(e)[:70]}")
            time.sleep(slp)
            continue
        site = pick_campaign_site(res, c.get("name"))
        if site:
            c["campaign_website"] = site
            c["source_discovered"] = True
            found += 1
            print(f"  + {c['slug']:26} -> {site}")
        else:
            print(f"  . {c['slug']:26} (no campaign site found)")
        time.sleep(slp)
    json.dump(batch, open(out, "w"), indent=1)
    print(f"wrote {out}: {found} campaign site(s) discovered on {spent} Brave quer(ies), "
          f"{len(batch)} candidates in batch")


if __name__ == "__main__":
    main()
