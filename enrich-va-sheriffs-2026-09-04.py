#!/usr/bin/env python3
"""
enrich-va-sheriffs-2026-09-04.py — website + social discovery for VA sheriffs.

Sitting sheriffs were roster-only scaffolds (VSA directory harvest). This pass
adds verifiable official links only — no invented scores or party tags.

Sources: Brave web search (county/city sheriff office pages, verified social).
VSA person pages are captcha-blocked to curl; Brave finds the same .gov offices.

Usage:
  python3 enrich-va-sheriffs-2026-09-04.py [--dry] [--max N] [--sleep S]
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = Path(__file__).parent
SCORECARD = BASE / "data" / "scorecard.json"

SKIP_HOST = re.compile(
    r"ballotpedia|wikipedia|vasheriff\.org|linkedin|instagram|youtube|tiktok|"
    r"patch\.com|news|fox|nbc|cbs|abc|usnews|govtech|indeed|glassdoor|"
    r"yellowpages|yelp|mapquest|zoominfo|muckrack|dcjs\.virginia\.gov|"
    r"middlesexsheriff\.org|\.il\.gov|tazewell-il",
    re.I,
)
GOV_HINT = re.compile(r"\.(gov|us)(/|$)", re.I)
SHERIFF_HINT = re.compile(r"sheriff|so\s|sheriff'?s?\s+office", re.I)


def brave_key() -> str:
    for env in ("BRAVE_API_KEY", "OPENCLAW_BRAVE_API_KEY"):
        if os.environ.get(env):
            return os.environ[env]
    cfg = json.load(open(os.path.expanduser("~/.openclaw/openclaw.json")))
    raw = cfg["plugins"]["entries"]["brave"]["config"]["webSearch"]["apiKey"]
    if isinstance(raw, str):
        return raw
    if isinstance(raw, dict):
        import subprocess

        sid = raw.get("id") or "OPENCLAW_BRAVE_API_KEY"
        return subprocess.check_output(
            ["security", "find-generic-password", "-s", sid, "-w"], text=True
        ).strip()
    raise SystemExit("Brave API key not found")


def brave_search(key: str, q: str, count: int = 10) -> list[dict]:
    u = (
        "https://api.search.brave.com/res/v1/web/search?q="
        + urllib.parse.quote(q)
        + f"&count={count}&country=us&result_filter=web"
    )
    req = urllib.request.Request(
        u, headers={"Accept": "application/json", "X-Subscription-Token": key}
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        j = json.load(r)
    return (j.get("web", {}) or {}).get("results") or []


def name_tokens(name: str) -> list[str]:
    return [t.lower() for t in re.findall(r"[A-Za-z]{3,}", name or "")]


def jurisdiction_tokens(jurisdiction: str) -> list[str]:
    j = jurisdiction.lower()
    j = re.sub(r"\b(city|county|of)\b", " ", j)
    j = re.sub(r"[^a-z0-9]+", " ", j)
    return [t for t in j.split() if len(t) >= 3]


FB_RESERVED = frozenset(
    {"p", "pages", "public", "profile.php", "groups", "people", "watch", "events", "share", "sharer"}
)


def parse_facebook(url: str) -> str | None:
    host = urllib.parse.urlparse(url).netloc.lower()
    if "facebook.com" not in host:
        return None
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.strip("/")
    if not path or path.startswith("sharer"):
        return None
    if path.startswith("profile.php"):
        q = urllib.parse.parse_qs(parsed.query)
        if q.get("id"):
            return f"profile.php?id={q['id'][0]}"
        return None
    handle = path.split("/")[0]
    if handle.lower() in FB_RESERVED or len(handle) < 3:
        return None
    return handle


def parse_twitter(url: str) -> str | None:
    host = urllib.parse.urlparse(url).netloc.lower()
    if host not in ("twitter.com", "x.com", "www.twitter.com", "www.x.com"):
        return None
    parts = urllib.parse.urlparse(url).path.strip("/").split("/")
    if not parts or parts[0] in ("home", "search", "intent", "share", "i"):
        return None
    handle = parts[0]
    if handle.lower() in ("pages", "groups"):
        return None
    return "@" + handle


def score_website(url: str, title: str, jurisdiction: str) -> int:
    if SKIP_HOST.search(url):
        return -99
    host = urllib.parse.urlparse(url).netloc.lower()
    score = 0
    jtoks = jurisdiction_tokens(jurisdiction)
    host_flat = host.replace("-", "").replace(".", "")
    if GOV_HINT.search(host) or host.endswith(".us"):
        score += 8
    if SHERIFF_HINT.search(url) or SHERIFF_HINT.search(title):
        score += 5
    for t in jtoks:
        if t in host_flat or t in (title or "").lower():
            score += 2
    if "sheriff" in host:
        score += 3
    return score


def score_social(url: str, name: str, jurisdiction: str, kind: str) -> int:
    if SKIP_HOST.search(url):
        return -99
    blob = (url + " ").lower()
    # Wrong-state Middlesex trap (MA sheriff office vs Middlesex County VA)
    if "middlesex" in jurisdiction.lower():
        if re.search(r"\b(ma|massachusetts|woburn)\b", blob):
            return -99
    if re.search(r"middlesexsheriff\.org|msosheriff", blob) and "middlesex county" in jurisdiction.lower():
        return -99
    score = 0
    toks = name_tokens(name)
    jtoks = jurisdiction_tokens(jurisdiction)
    if kind == "facebook" and "facebook.com" not in blob:
        return -99
    if kind == "twitter" and "twitter.com" not in blob and "x.com" not in blob:
        return -99
    for t in toks:
        if t in blob:
            score += 2
    for t in jtoks:
        if t in blob:
            score += 1
    if kind == "facebook" and "sheriff" in blob:
        score += 3
    if kind == "facebook" and GOV_HINT.search(blob):
        score += 2
    return score


def discover(key: str, name: str, jurisdiction: str, sleep: float) -> dict:
    queries = [
        f"{jurisdiction} sheriff office virginia site:.gov",
        f"{name} sheriff {jurisdiction} virginia",
        f"{jurisdiction} sheriff facebook",
    ]
    website, facebook, twitter = None, None, None
    best_web = -99
    best_fb = -99
    best_tw = -99

    seen: set[str] = set()
    for q in queries:
        try:
            results = brave_search(key, q)
        except Exception as e:
            print(f"    search error: {e}", file=sys.stderr)
            time.sleep(sleep)
            continue
        for r in results:
            url = (r.get("url") or "")
            if isinstance(url, dict):
                url = url.get("url") or url.get("href") or ""
            url = str(url).strip()
            title = r.get("title") or ""
            if isinstance(title, dict):
                title = title.get("title") or ""
            title = str(title)
            if not url or url in seen:
                continue
            seen.add(url)

            ws = score_website(url, title, jurisdiction)
            if ws > best_web:
                best_web = ws
                website = url.rstrip("/")

            fb = parse_facebook(url)
            if fb:
                fs = score_social(url, name, jurisdiction, "facebook")
                if fs > best_fb:
                    best_fb = fs
                    facebook = fb

            tw = parse_twitter(url)
            if tw:
                ts = score_social(url, name, jurisdiction, "twitter")
                if ts > best_tw:
                    best_tw = ts
                    twitter = tw

        time.sleep(sleep)

    out: dict = {}
    if website and best_web >= 6:
        out["website"] = website
    if facebook and best_fb >= 5:
        out["facebook"] = facebook
    if twitter and best_tw >= 3:
        out["twitter"] = twitter
    return out


def main() -> None:
    dry = "--dry" in sys.argv
    max_n = None
    sleep = 0.35
    for i, arg in enumerate(sys.argv):
        if arg == "--max" and i + 1 < len(sys.argv):
            max_n = int(sys.argv[i + 1])
        if arg == "--sleep" and i + 1 < len(sys.argv):
            sleep = float(sys.argv[i + 1])

    key = brave_key()
    with open(SCORECARD, encoding="utf-8") as f:
        data = json.load(f)

    targets = [
        c
        for c in data["candidates"]
        if c.get("state") == "VA"
        and "sheriff" in (c.get("office") or "").lower()
        and (
            not c.get("website")
            or not (c.get("profile") or {}).get("facebook")
            or not (c.get("profile") or {}).get("twitter")
        )
    ]
    if max_n:
        targets = targets[:max_n]

    print(f"Enriching {len(targets)} VA sheriff(s)…")
    updated = 0
    for i, c in enumerate(targets, 1):
        slug = c["slug"]
        prof = c.setdefault("profile", {})
        print(f"[{i}/{len(targets)}] {c['name']} ({slug})")
        found = discover(key, c["name"], c.get("jurisdiction") or "", sleep)
        changed = False
        if found.get("website") and not c.get("website"):
            c["website"] = found["website"]
            changed = True
            print(f"  website: {found['website']}")
        if found.get("facebook") and not prof.get("facebook"):
            prof["facebook"] = found["facebook"]
            changed = True
            print(f"  facebook: {found['facebook']}")
        if found.get("twitter") and not prof.get("twitter"):
            prof["twitter"] = found["twitter"]
            changed = True
            print(f"  twitter: {found['twitter']}")
        if found.get("website"):
            src = found["website"]
            if src not in (c.get("sources") or []):
                c.setdefault("sources", []).append(src)
        if changed:
            updated += 1
        elif not found:
            print("  (no new links)")

    print(f"\nUpdated {updated} record(s)")
    if dry:
        print("DRY RUN — scorecard not written")
        return

    data.setdefault("meta", {})["last_updated"] = "2026-09-04"
    with open(SCORECARD, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    import subprocess

    subprocess.run([sys.executable, str(BASE / "build-data.py"), "--quiet"], check=True)
    subprocess.run([sys.executable, str(BASE / "generate-profiles.py")], check=True)


if __name__ == "__main__":
    main()
