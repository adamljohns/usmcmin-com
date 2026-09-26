#!/usr/bin/env python3
"""Pick the next FXBG commerce listings for a local evidence grind (v0.4).

Prioritize fetchable official sites with gray factors and fewest prior strikes.
Usage: select-commerce-batch.py [N] [OUT.json]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"

N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("/tmp/commerce-local-batch.json")

TRADE_CATS = {
    "plumbing", "hvac", "roofing", "electrical", "electrical-contractor",
    "pest-control", "auto-repair", "home-services", "home-builder", "landscaping",
    "orthodontics", "appliance-repair", "home-cleaning", "remodeling",
}

FACTOR_PRIORITY = (
    "financial_integrity",
    "christ_centered_brand",
    "community_fruit",
    "worker_dignity",
)


def strikes(biz: dict) -> int:
    try:
        return int(biz.get("grind_strikes") or 0)
    except (TypeError, ValueError):
        return 0


def web_ok(biz: dict) -> bool:
    w = (biz.get("web") or "").strip()
    return w.startswith("http")


def gray_factors(biz: dict) -> list[str]:
    scores = biz.get("scores") or {}
    out = []
    for f in FACTOR_PRIORITY:
        if scores.get(f) in (None, "", "gray"):
            out.append(f)
    return out


def priority_score(biz: dict) -> tuple:
    grays = gray_factors(biz)
    if not grays or not web_ok(biz):
        return (99, 99, 99, biz.get("slug") or "")
    if strikes(biz) >= 3:
        return (98, 99, 99, biz.get("slug") or "")
    fi_first = 0 if "financial_integrity" in grays else 1
    trade = 0 if biz.get("category") in TRADE_CATS else 1
    featured = 0 if biz.get("featured") else 1
    return (strikes(biz), fi_first, trade + featured, biz.get("slug") or "")


def main() -> None:
    data = json.loads(DATA.read_text())
    pool = [b for b in data.get("businesses") or [] if web_ok(b) and gray_factors(b)]
    pool.sort(key=priority_score)
    batch = []
    for b in pool[:N]:
        batch.append(
            {
                "slug": b["slug"],
                "name": b.get("name"),
                "category": b.get("category"),
                "web": b.get("web"),
                "grind_strikes": strikes(b),
                "gray_factors": gray_factors(b),
            }
        )
    OUT.write_text(json.dumps(batch, indent=2))
    print(f"selected {len(batch)} of {len(pool)} eligible -> {OUT}")


if __name__ == "__main__":
    main()
