#!/usr/bin/env python3
"""
add-tx-local-roster-2026-08-16.py — Glen Rose / Somervell / Johnson /
Josephine–Collin–Hunt local officials for RESOLUTE Citizen.

Roster-only scaffolds: local-tier N/A mask, all score cells null,
profile.confidence null. No party, no invented TRUE/FALSE.

Verified this turn from official sources only. Skipped (not on current
official roster): Stuart Mann, Candace Scholz (Glen Rose TML city profile
1112 lists Boles / Freas / Bruning / Mapes / Comer / Hawkins — Mann and
Scholz absent).

Sources cited per record below.
"""
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


def rec(name, slug, office, jurisdiction, sources):
    return {
        "name": name,
        "slug": slug,
        "office": office,
        "jurisdiction": jurisdiction,
        "level": "local",
        "party": None,
        "district": None,
        "state": "TX",
        "status": "active",
        "scores": {k: list(v) for k, v in LOCAL_SCORES.items()},
        "notes": SCaffold_NOTE,
        "photo": None,
        "website": None,
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
    # Glen Rose — TML city profile 1112 (directory.tml.org)
    rec(
        "Joe Boles",
        "joe-boles",
        "Mayor",
        "City of Glen Rose",
        [
            "https://directory.tml.org/profile/city/1112",
            "https://www.glenrosetexas.org/city-council",
        ],
    ),
    rec(
        "George Freas",
        "george-freas",
        "Mayor Pro Tem",
        "City of Glen Rose",
        ["https://directory.tml.org/profile/city/1112"],
    ),
    rec(
        "Laurin Mapes",
        "laurin-mapes",
        "City Council",
        "City of Glen Rose",
        ["https://directory.tml.org/profile/city/1112"],
    ),
    rec(
        "Richard Bruning",
        "richard-bruning",
        "City Council",
        "City of Glen Rose",
        ["https://directory.tml.org/profile/city/1112"],
    ),
    # Somervell County — somervell.co
    rec(
        "Danny L. Chambers",
        "danny-l-chambers",
        "Somervell County Judge",
        "Somervell County",
        [
            "https://www.somervell.co/341/County-Judge",
            "https://www.sos.state.tx.us/elections/voter/judges.shtml",
        ],
    ),
    rec(
        "Jeff Harris",
        "jeff-harris",
        "Somervell County Commissioner, Precinct 1",
        "Somervell County",
        ["https://www.somervell.co/362/Precinct-1"],
    ),
    rec(
        "Richard Talavera",
        "richard-talavera",
        "Somervell County Commissioner, Precinct 2",
        "Somervell County",
        ["https://www.somervell.co/363/Precinct-2"],
    ),
    rec(
        "Chip Joslin",
        "chip-joslin",
        "Somervell County Commissioner, Precinct 3",
        "Somervell County",
        ["https://www.somervell.co/175/Commissioners-Court"],
    ),
    rec(
        "Wade Busch",
        "wade-busch",
        "Somervell County Commissioner, Precinct 4",
        "Somervell County",
        ["https://www.somervell.co/175/Commissioners-Court"],
    ),
    # Johnson County — johnsoncountytx.org
    rec(
        "Christopher Boedeker",
        "christopher-boedeker",
        "Johnson County Judge",
        "Johnson County",
        [
            "https://www.johnsoncountytx.org/government/county-judge",
            "https://www.sos.state.tx.us/elections/voter/judges.shtml",
        ],
    ),
    rec(
        "Rick Bailey",
        "rick-bailey",
        "Johnson County Commissioner, Precinct 1",
        "Johnson County",
        [
            "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-1",
        ],
    ),
    rec(
        "Kenny Howell",
        "kenny-howell",
        "Johnson County Commissioner, Precinct 2",
        "Johnson County",
        [
            "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-2",
        ],
    ),
    rec(
        "Mike White",
        "mike-white",
        "Johnson County Commissioner, Precinct 3",
        "Johnson County",
        [
            "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-3",
        ],
    ),
    rec(
        "Larry Woolley",
        "larry-woolley",
        "Johnson County Commissioner, Precinct 4",
        "Johnson County",
        [
            "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-4",
        ],
    ),
    # Josephine / Collin / Hunt
    rec(
        "Jason Turney",
        "jason-turney",
        "Mayor",
        "City of Josephine",
        [
            "https://directory.tml.org/profile/individual/83337",
            "https://cityofjosephinetx.com/government/city-council/",
        ],
    ),
    rec(
        "Chris Hill",
        "chris-hill",
        "Collin County Judge",
        "Collin County",
        [
            "https://www.collincountytx.gov/Government/Commissioners-Court/county-judge",
        ],
    ),
    rec(
        "Bobby W. Stovall",
        "bobby-w-stovall",
        "Hunt County Judge",
        "Hunt County",
        ["https://www.huntcounty.net/page/hunt.countyjudge"],
    ),
]


def main():
    with open(SCORECARD, encoding="utf-8") as f:
        data = json.load(f)

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
    data["meta"]["last_updated"] = "2026-08-16"

    with open(SCORECARD, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nAdded {len(added)} record(s). Total candidates: {len(data['candidates'])}")
    print("Skipped (not verified this turn): stuart-mann, candace-scholz")

    subprocess.run([sys.executable, str(BASE / "build-data.py"), "--quiet"], check=True)


if __name__ == "__main__":
    main()
