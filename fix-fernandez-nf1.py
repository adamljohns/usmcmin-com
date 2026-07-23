#!/usr/bin/env python3
"""One-shot fixup: remove the erroneous nf1 claim for Nathalia Fernandez.

The nf1 claim incorrectly stated she voted on Senate bill S51001 (Concealed
Carry Improvement Act, July 2022) as a State Senator — but she was an Assembly
Member (AD-80) until December 2022 and didn't join the Senate until January 2023.
The corrected nf1b claim (Assembly companion bill A41001) is added by
enrich-batch-840.py re-run. This script only removes the stale nf1 claim.

Also corrects nf2 text which incorrectly said "since January 2021" (should be
Senate tenure start January 2023).
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"

BAD_ID = "nathalia-fernandez-self_defense-1-nf1"
FIX_ID = "nathalia-fernandez-biblical_marriage-2-nf2"
FIX_OLD = "since January 2021"
FIX_NEW = "since January 2023 (when she was first elected to the State Senate)"

scorecard = json.loads(SCORECARD.read_text())
found = False
for c in scorecard["candidates"]:
    if c.get("slug") != "nathalia-fernandez":
        continue
    claims = c.get("claims") or []
    before = len(claims)
    claims = [cl for cl in claims if cl.get("id") != BAD_ID]
    removed = before - len(claims)
    # Fix nf2 text
    fixed_text = 0
    for cl in claims:
        if cl.get("id") == FIX_ID and FIX_OLD in cl.get("text", ""):
            cl["text"] = cl["text"].replace(FIX_OLD, FIX_NEW)
            fixed_text += 1
    c["claims"] = claims
    print(f"  Nathalia Fernandez: removed {removed} bad claim(s), fixed {fixed_text} text(s)")
    print(f"  Claims remaining: {len(claims)}")
    found = True
    break

if not found:
    print("  ERROR: nathalia-fernandez not found in scorecard")

SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
print("Done.")
