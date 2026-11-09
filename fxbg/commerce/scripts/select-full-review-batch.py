#!/usr/bin/env python3
"""Select the next FULL REVIEW batch (commerce ticket 2026-11-09).

Selection order (ticket): (a) listings with no website or no verified-at date;
(b) licensed trades; (c) oldest verified first; (d) the rest. Within a tier,
licensed trades first, then published before hidden, then oldest `updated`.
Listings fully reviewed in the last FULL_REVIEW_COOLDOWN_DAYS (30) are skipped.

verified-at = the newest of full_review.verified_at and every scores.*_meta.verified.

Read-only on data/businesses.json. Refuses to run while the commerce grind holds
its lock (/tmp/commerce-enrichment-round.lock.d) so the two never overlap.

--spread (sample mode for dry runs/QA) round-robins tiers a,b,c,d instead of the strict order.

Usage: select-full-review-batch.py [N=25] OUT.json [--include slug,slug] [--spread] [--allow-during-grind]
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from full_review_common import DATA, FR_HOME, GRIND_LOCK, LICENSED_TRADES, load_data, sha256_file  # noqa: E402

DEFAULT_N, MAX_N = 25, 60
COOLDOWN = int(os.environ.get("FULL_REVIEW_COOLDOWN_DAYS", "30"))


def verified_at(b: dict) -> str | None:
    ds = [v.get("verified") for k, v in (b.get("scores") or {}).items()
          if k.endswith("_meta") and isinstance(v, dict) and v.get("verified")]
    fr = (b.get("full_review") or {}).get("verified_at")
    if fr:
        ds.append(fr)
    return max(ds) if ds else None


def has_web(b: dict) -> bool:
    return str(b.get("web") or "").startswith("http")


def tier(b: dict) -> str:
    if not has_web(b) or not verified_at(b):
        return "a"
    if b.get("category") in LICENSED_TRADES:
        return "b"
    if verified_at(b):
        return "c"
    return "d"


def sort_key(b: dict) -> tuple:
    t = tier(b)
    trade = 0 if b.get("category") in LICENSED_TRADES else 1
    hidden = 1 if b.get("publish") is False else 0
    when = verified_at(b) or b.get("updated") or "0000"
    return ("abcd".index(t), trade, hidden, when, b.get("slug") or "")


def main() -> None:
    args = [a for a in sys.argv[1:]]
    include: list[str] = []
    if "--include" in args:
        i = args.index("--include")
        include = [s for s in args[i + 1].split(",") if s]
        del args[i:i + 2]
    allow = "--allow-during-grind" in args
    spread = "--spread" in args
    args = [a for a in args if not a.startswith("--")]
    n = int(args[0]) if args and args[0].isdigit() else DEFAULT_N
    out = Path(args[1] if len(args) > 1 else (args[0] if args and not args[0].isdigit() else "/tmp/commerce-full-review-batch.json"))
    if n > MAX_N:
        sys.exit(f"batch {n} > max {MAX_N}")
    if GRIND_LOCK.exists() and not allow:
        sys.exit(f"GRIND_RUNNING: {GRIND_LOCK} exists — a commerce grind round is in progress; not overlapping it")

    data = load_data()
    biz = data.get("businesses") or []
    by_slug = {b["slug"]: b for b in biz}
    missing = [s for s in include if s not in by_slug]
    if missing:
        sys.exit(f"unknown slug(s): {missing}")
    cutoff = (date.today() - timedelta(days=COOLDOWN)).isoformat()
    picked = [by_slug[s] for s in include]
    pool = [b for b in biz if b["slug"] not in include
            and ((b.get("full_review") or {}).get("verified_at") or "0000") < cutoff]
    pool.sort(key=sort_key)
    if spread:
        # Sample mode (dry runs / QA): round-robin across tiers a,b,c,d, each tier in its own order,
        # so one batch exercises every path. The default is the strict ticket order.
        buckets = {t: [b for b in pool if tier(b) == t] for t in "abcd"}
        while len(picked) < n and any(buckets.values()):
            for t in "abcd":
                if buckets[t] and len(picked) < n:
                    picked.append(buckets[t].pop(0))
    else:
        picked += pool[: max(0, n - len(picked))]

    rows = []
    for b in picked:
        rows.append({
            "slug": b["slug"], "name": b.get("name"), "category": b.get("category"),
            "selection_tier": (tier(b) + (" (spread sample)" if spread else "")) if b["slug"] not in include else f"forced ({tier(b)})",
            "licensed_trade": b.get("category") in LICENSED_TRADES,
            "verified_at": verified_at(b), "web": b.get("web") or "", "publish": b.get("publish", True),
        })
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"selected_on": date.today().isoformat(), "data_file": str(DATA),
                               "data_sha256": sha256_file(DATA), "n": len(rows), "batch": rows}, indent=1))
    tiers = {}
    for r in rows:
        tiers[r["selection_tier"]] = tiers.get(r["selection_tier"], 0) + 1
    print(f"selected {len(rows)} -> {out} tiers={tiers}")


if __name__ == "__main__":
    main()
