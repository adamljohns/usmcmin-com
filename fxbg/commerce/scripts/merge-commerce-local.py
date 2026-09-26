#!/usr/bin/env python3
"""Apply verbatim-verified local-commerce-extract findings to businesses.json."""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"


def source_exists(sources: list, url: str) -> bool:
    u = (url or "").rstrip("/").lower()
    for s in sources or []:
        if (s.get("url") or "").rstrip("/").lower() == u:
            return True
    return False


def apply_finding(biz: dict, f: dict) -> bool:
    factor = f["factor"]
    band = f["band"]
    quote = f.get("quote") or ""
    url = f.get("source_url") or biz.get("web")
    scores = biz.setdefault("scores", {})
    old = scores.get(factor, "gray")
    if old not in (None, "", "gray") and band == "green":
        return False
    scores[factor] = band
    src_count = len(biz.get("sources") or [])
    scores[f"{factor}_meta"] = {
        "band": band,
        "reason": "affirmative" if band == "green" else "concern",
        "source_count": max(src_count, 1),
        "concern_count": 1 if band == "yellow" else 0,
        "verified": date.today().isoformat(),
        "quote": quote[:400],
    }
    sources = biz.setdefault("sources", [])
    label = f"Official site — grind {date.today().isoformat()}"
    if url and not source_exists(sources, url):
        sources.insert(0, {"url": url, "label": label})
    blob = biz.get("owner_operator") or ""
    if quote and quote not in blob:
        biz["owner_operator"] = (blob + " Evidence: " + quote).strip()[:2000]
    return True


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: merge-commerce-local.py EXTRACT.json", file=sys.stderr)
        sys.exit(2)
    extract = json.loads(Path(sys.argv[1]).read_text())
    by_slug = {b["slug"]: b for b in extract.get("businesses") or []}

    data = json.loads(DATA.read_text())
    touched = []
    for biz in data.get("businesses") or []:
        slug = biz.get("slug")
        row = by_slug.get(slug)
        if not row:
            continue
        findings = row.get("findings") or []
        if findings:
            biz["grind_strikes"] = 0
            for f in findings:
                if apply_finding(biz, f):
                    touched.append(slug)
            biz["last_grind"] = date.today().isoformat()
        elif row.get("fetch_error"):
            biz["grind_strikes"] = int(biz.get("grind_strikes") or 0) + 1
            biz["last_grind"] = date.today().isoformat()

    data["updated"] = date.today().isoformat()
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    uniq = sorted(set(touched))
    print(f"merged: {len(uniq)} listing(s) with score updates -> {', '.join(uniq[:12])}")


if __name__ == "__main__":
    main()
