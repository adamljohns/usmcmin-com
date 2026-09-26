#!/usr/bin/env python3
"""Fetch websites + social links for listings (OSM stubs first). Updates sources + digital_integrity."""
from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"

UA = {"User-Agent": "C5iSR-CommerceBot/0.4 (+https://usmcmin.com/fxbg/commerce/)"}
CTX = ssl.create_default_context()
SOCIAL_RE = re.compile(
    r"https?://(?:www\.)?(facebook\.com|instagram\.com|linkedin\.com)/[^\s\"'<>]+",
    re.I,
)


def fetch(url: str, timeout: int = 12) -> tuple[int | None, str]:
    req = urllib.request.Request(url, headers=UA, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.status, r.read(250_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        try:
            body = e.read(100_000).decode("utf-8", "replace")
        except Exception:
            body = ""
        return e.code, body
    except Exception:
        return None, ""


def source_exists(sources: list, url: str) -> bool:
    u = (url or "").rstrip("/").lower()
    for s in sources or []:
        if (s.get("url") or "").rstrip("/").lower() == u:
            return True
    return False


def priority(biz: dict) -> tuple:
    osm = 0 if biz.get("ingest_source") == "osm" else 1
    web = 0 if (biz.get("web") or "").startswith("http") else 1
    strikes = int(biz.get("discover_strikes") or 0)
    return (strikes, osm, web, biz.get("slug") or "")


def process(biz: dict) -> bool:
    url = (biz.get("web") or "").strip()
    if not url.startswith("http"):
        biz["discover_strikes"] = int(biz.get("discover_strikes") or 0) + 1
        return False
    status, html = fetch(url)
    scores = biz.setdefault("scores", {})
    sources = biz.setdefault("sources", [])
    touched = False
    if status and 200 <= status < 400:
        scores["digital_integrity"] = "green"
        scores["digital_integrity_meta"] = {
            "band": "green",
            "reason": "affirmative",
            "source_count": len(sources) + 1,
            "concern_count": 0,
            "verified": date.today().isoformat(),
        }
        touched = True
    elif status:
        scores["digital_integrity"] = "yellow"
        scores["digital_integrity_meta"] = {
            "band": "yellow",
            "reason": "concern",
            "source_count": len(sources),
            "concern_count": 1,
            "verified": date.today().isoformat(),
        }
        touched = True
    if html:
        for m in SOCIAL_RE.finditer(html):
            link = m.group(0).split("&")[0].rstrip(")")
            host = m.group(1).lower()
            label = {"facebook.com": "Facebook", "instagram.com": "Instagram", "linkedin.com": "LinkedIn"}[host]
            if not source_exists(sources, link):
                sources.append({"label": f"{label} (from official site)", "url": link})
                touched = True
    biz["last_discover"] = date.today().isoformat()
    return touched


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    slugs = [s.strip() for s in sys.argv[2:] if s.strip()]
    data = json.loads(DATA.read_text())
    pool = [b for b in data.get("businesses") or [] if b.get("publish", True)]
    if slugs:
        pool = [b for b in pool if b.get("slug") in slugs]
    else:
        pool = [b for b in pool if (b.get("web") or "").startswith("http")]
        pool.sort(key=priority)
    touched_slugs = []
    for biz in pool[:n]:
        if process(biz):
            touched_slugs.append(biz.get("slug"))
    data["updated"] = date.today().isoformat()
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"discover: {len(touched_slugs)} updated -> {', '.join(touched_slugs[:10])}")


if __name__ == "__main__":
    main()
