#!/usr/bin/env python3
"""Verification for SRC-0823-AFFIRM."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCORECARD = ROOT / "data" / "scorecard.json"
KIGGANS_HTML = ROOT / "candidates" / "va" / "jen-kiggans.html"


def main():
    data = json.loads(SCORECARD.read_text())
    errors = []

    cats = {c["id"]: c for c in data.get("categories", [])}
    for cid, key, idx in (
        ("sanctity_of_life", "questions", 4),
        ("foreign_policy_restraint", "questions", 3),
    ):
        q = (cats.get(cid) or {}).get(key, [None] * 5)[idx]
        if not q or "search found no" not in q.lower():
            errors.append(f"{cid} federal q missing affirmative wording: {q!r}")
        if q and "has never accepted" in q.lower():
            errors.append(f"{cid} federal q still has negative framing: {q!r}")

    kiggans = next((c for c in data["candidates"] if c.get("slug") == "jen-kiggans"), None)
    if not kiggans:
        errors.append("jen-kiggans not found in scorecard")
    else:
        cell = (kiggans.get("scores") or {}).get("foreign_policy_restraint", [None] * 5)[3]
        if cell is not False:
            errors.append(f"jen-kiggans foreign_policy_restraint[3] = {cell!r}, expected False")

    if KIGGANS_HTML.exists():
        html = KIGGANS_HTML.read_text()
        if "has never accepted donations from foreign-backed lobbies" in html:
            errors.append("jen-kiggans.html still contains old foreign-lobby question text")
        if "has never accepted Planned Parenthood" in html:
            errors.append("jen-kiggans.html still contains old sanctity PAC question text")
        if "search found no AIPAC" not in html:
            errors.append("jen-kiggans.html missing new affirmative foreign-lobby question")
        if "FALSE (0)" not in html.split("search found no AIPAC")[1][:500] if "search found no AIPAC" in html else True:
            # simpler check: foreign lobby section should show FALSE near AIPAC question
            idx = html.find("search found no AIPAC")
            if idx == -1:
                pass  # already flagged
            elif "FALSE (0)" not in html[idx : idx + 400]:
                errors.append("jen-kiggans.html AIPAC cell not showing FALSE (0)")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        sys.exit(1)

    print("PASS")
    print(f"  sanctity q5: {cats['sanctity_of_life']['questions'][4][:80]}...")
    print(f"  foreign q4:  {cats['foreign_policy_restraint']['questions'][3][:80]}...")
    print(f"  kiggans foreign_policy_restraint[3] = False")


if __name__ == "__main__":
    main()
