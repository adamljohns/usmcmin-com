#!/usr/bin/env python3
"""Pick the next FXBG commerce listings for a local evidence grind (v0.4).

Prioritize fetchable official sites with gray factors and fewest prior strikes.
Usage: select-commerce-batch.py [N] [OUT.json]
"""
from __future__ import annotations

import json
import os
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


LOW_YIELD_HOSTS = ("facebook.com", "instagram.com", "yelp.com", "linktr.ee", "/locations/")


def low_yield(biz: dict) -> int:
    w = (biz.get("web") or "").lower()
    return 1 if any(h in w for h in LOW_YIELD_HOSTS) else 0


def priority_score(biz: dict) -> tuple:
    # 2026-11-22: every eligible listing had >=3 strikes, so all fell into one bucket that
    # sorted by slug alone — the same ten listings (2400 Diner + 7-Eleven locators) were
    # picked every round for weeks. Rotate by last_grind (never-ground first, then oldest),
    # and push social/chain-locator URLs to the back.
    grays = gray_factors(biz)
    if not grays or not web_ok(biz):
        return (99, 1, "9999", 99, 99, biz.get("slug") or "")
    fi_first = 0 if "financial_integrity" in grays else 1
    trade = 0 if biz.get("category") in TRADE_CATS else 1
    featured = 0 if biz.get("featured") else 1
    bucket = 1 if strikes(biz) >= 3 else 0
    last = biz.get("last_grind") or "0000"
    return (bucket, low_yield(biz), last, fi_first, trade + featured, biz.get("slug") or "")


def main() -> None:
    data = json.loads(DATA.read_text())
    pool = [b for b in data.get("businesses") or [] if web_ok(b) and gray_factors(b)]
    pool.sort(key=priority_score)
    # Operator re-run of named listings (comma-separated slugs); still limited to eligible ones.
    only = [s.strip() for s in os.environ.get("COMMERCE_ONLY_SLUGS", "").split(",") if s.strip()]
    if only:
        pool = [b for b in pool if b.get("slug") in only]
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
