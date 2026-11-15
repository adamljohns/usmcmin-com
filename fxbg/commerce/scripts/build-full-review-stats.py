#!/usr/bin/env python3
"""Public COUNTS for the commerce full review (ops view): reviewed, changed, held, applied.

Reads the private round files under FR_HOME (never published) and writes only
numbers to data/full-review-stats.json, which build-stats.py folds into
data/stats.json and the hub's Directory snapshot panel renders. No slugs, quotes,
URLs or HOLD contents leave FR_HOME.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import full_review_common as fr  # noqa: E402


def main() -> None:
    rounds = sorted((fr.FR_HOME / "rounds").glob("*/review-patch.json")) if (fr.FR_HOME / "rounds").exists() else []
    reviewed, changed = set(), set()
    last = None
    proposed = auto = 0
    for p in rounds:
        try:
            patch = json.load(open(p))
        except Exception:
            continue
        if patch.get("superseded"):
            continue
        last = patch
        for e in patch.get("businesses", []):
            reviewed.add(e["slug"])
            if e.get("changes"):
                changed.add(e["slug"])
    if last:
        proposed = last["counts"]["changes_proposed"]
        auto = last["counts"]["auto"]
    q = fr.FR_HOME / "hold-queue.json"
    held = len(json.load(open(q)).get("rows", [])) if q.exists() else 0
    led = fr.FR_HOME / "applied-ledger.json"
    applied = len(json.load(open(led)).get("applied", [])) if led.exists() else 0
    out = {
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mode": "dry-run only (live apply waits for Adam's GO)" if not applied else "live",
        "reviewed": len(reviewed),
        "changed": len(changed),
        "held": held,
        "applied": applied,
        "last_round": {"id": last["round_id"], "reviewed": last["counts"]["reviewed"], "changes_proposed": proposed,
                       "auto": auto, "hold_rows": last["counts"]["hold_rows"]} if last else None,
        "note": "Counts only. Patches and the HOLD queue are private (QA: Sheriff Roy).",
    }
    fr.PUBLIC_STATS.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
