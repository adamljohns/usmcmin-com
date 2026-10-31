#!/usr/bin/env python3
"""Emit commerce directory stats for hub footer / grind reports."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"

# Total-target: Census County Business Patterns 2023, employer establishments (all NAICS),
# https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip . Principal 2026-10-31.
TARGET = {
    "total": 7778,
    "localities": {
        "Fredericksburg city": 1477,
        "Spotsylvania County": 2811,
        "Stafford County": 2570,
        "King George County": 496,
        "Caroline County": 424,
    },
    "source": "U.S. Census Bureau, County Business Patterns 2023",
    "source_url": "https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip",
    "note": "Employer establishments; excludes no-employee sole proprietors.",
}

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
    biz = [b for b in data.get("businesses") or [] if b.get("publish") is not False]
    overall = Counter(str(b.get("overall", "gray")).lower() for b in biz)
    cats = Counter(b.get("category", "?") for b in biz)
    type_a = sum(
        1
        for b in biz
        if (b.get("scores") or {}).get("christ_centered_brand") == "green"
    )
    adam = sum(1 for b in biz if b.get("adam_visited"))
    # principal_reviewed: {"date": "YYYY-MM-DD", "note": "..."} set ONLY when Adam has personally
    # read the listing and given feedback on it. Never inferred from adam_visited/adam_connection.
    reviewed = sum(1 for b in biz if isinstance(b.get("principal_reviewed"), dict) and b["principal_reviewed"].get("date"))
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
        "principal_reviewed": reviewed,
        "target": TARGET,
        "progress": {
            "listed": len(biz),
            "listed_pct": round(100 * len(biz) / TARGET["total"], 1),
            "principal_reviewed": reviewed,
            "principal_reviewed_pct": round(100 * reviewed / TARGET["total"], 2),
        },
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
