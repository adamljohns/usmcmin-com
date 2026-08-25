#!/usr/bin/env python3
"""Emit commerce directory stats for hub footer / grind reports."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"

FACTORS = [
    "ownership",
    "truth",
    "christ_centered_brand",
    "family_safety",
    "worker_dignity",
    "community_fruit",
    "reliability",
    "financial_integrity",
    "digital_integrity",
    "network_worthiness",
]


def main() -> None:
    data = json.loads(DATA.read_text())
    biz = data.get("businesses") or []
    overall = Counter(str(b.get("overall", "gray")).lower() for b in biz)
    cats = Counter(b.get("category", "?") for b in biz)
    type_a = sum(
        1
        for b in biz
        if (b.get("scores") or {}).get("christ_centered_brand") == "green"
    )
    adam = sum(1 for b in biz if b.get("adam_visited"))
    with_sources = sum(1 for b in biz if b.get("sources"))
    stats = {
        "total": len(biz),
        "rubric_version": data.get("rubric_version"),
        "updated": data.get("updated"),
        "overall": dict(overall),
        "categories": len(cats),
        "top_categories": cats.most_common(8),
        "type_a_or_b_green_brand": type_a,
        "adam_visited": adam,
        "with_sources": with_sources,
        "factor_green_counts": {
            f: sum(1 for b in biz if (b.get("scores") or {}).get(f) == "green")
            for f in FACTORS
        },
    }
    out = ROOT / "data" / "stats.json"
    out.write_text(json.dumps(stats, indent=2))
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
