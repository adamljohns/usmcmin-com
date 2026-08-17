#!/usr/bin/env python3
"""Add Stuart Mann and Candace Scholz Glen Rose scaffolds (2026-08-17)."""
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
SCORECARD = BASE / "data" / "scorecard.json"

LOCAL_SCORES = {
    "sanctity_of_life": [None, None, "N/A", "N/A", "N/A"],
    "biblical_marriage": [None, "N/A", None, "N/A", None],
    "family_child_sovereignty": [None, None, None, "N/A", "N/A"],
    "christian_liberty": [None, "N/A", None, None, None],
    "economic_stewardship": ["N/A", "N/A", None, "N/A", "N/A"],
    "election_integrity": [None, None, "N/A", "N/A", None],
    "border_immigration": ["N/A", None, None, "N/A", "N/A"],
    "self_defense": [None, None, "N/A", "N/A", "N/A"],
    "foreign_policy_restraint": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "industry_capture": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "public_justice": [None, None, None, None, None],
    "refuse_federal_overreach": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "refuse_state_overreach": [None, None, None, None, None],
}

SCaffold_NOTE = (
    "Roster-only scaffold pending grind evidence — sitting official verified "
    "from an official source this turn; not scored."
)


def rec(name, slug, office, sources):
    return {
        "name": name,
        "slug": slug,
        "office": office,
        "jurisdiction": "City of Glen Rose",
        "level": "local",
        "party": None,
        "district": None,
        "state": "TX",
        "status": "active",
        "scores": {k: list(v) for k, v in LOCAL_SCORES.items()},
        "notes": SCaffold_NOTE,
        "photo": None,
        "website": "https://www.glenrosetexas.org/city-council",
        "sources": sources,
        "profile": {
            "religion": None,
            "net_worth": None,
            "birthplace": None,
            "education": None,
            "background": None,
            "twitter": None,
            "prev_election_opponent": None,
            "next_election_year": None,
            "next_election_contenders": [],
            "confidence": None,
        },
        "claims": [],
    }


NEW = [
    rec(
        "Stuart Mann",
        "stuart-mann",
        "Mayor Pro Tem",
        [
            "https://www.glenrosetexas.org/city-council",
            "https://www.glenrosetexas.org/city-council/directory-listing/stuart-mann",
        ],
    ),
    rec(
        "Candace Scholz",
        "candace-scholz",
        "City Council",
        [
            "https://www.glenrosetexas.org/city-council",
            "https://www.glenrosetexas.org/city-council/directory-listing/candace-scholz",
        ],
    ),
]


def main():
    data = json.loads(SCORECARD.read_text(encoding="utf-8"))
    existing = {(c.get("slug"), c.get("state")) for c in data["candidates"]}
    next_id = max(c.get("id", 0) for c in data["candidates"] if isinstance(c.get("id"), int)) + 1
    added = []
    for candidate in NEW:
        key = (candidate["slug"], candidate["state"])
        if key in existing:
            print(f"  SKIP (exists): {candidate['slug']}")
            continue
        candidate["id"] = next_id
        next_id += 1
        data["candidates"].append(candidate)
        added.append(candidate["slug"])
        print(f"  ADD: {candidate['name']} ({candidate['slug']})")
    data.setdefault("meta", {})
    data["meta"]["total_candidates"] = len(data["candidates"])
    data["meta"]["last_updated"] = "2026-08-17"
    SCORECARD.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nAdded {len(added)} record(s). Total candidates: {len(data['candidates'])}")
    subprocess.run([sys.executable, str(BASE / "build-data.py"), "--quiet"], check=True)


if __name__ == "__main__":
    main()
