#!/usr/bin/env python3
"""Seed a race stub for Troy Jackson, the Maine Democratic U.S. Senate nominee
(MBP-1003-NIGHT r3).

Graham Platner won the June 9 primary and withdrew in July; Maine Democrats chose
Troy Jackson by convention on 2026-07-25 to replace him on the November ballot. The
scorecard had only Jackson's governor record (troy-jackson-gov, lost the June
primary), so the Collins race showed no Democratic nominee.

Sources: https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Maine
(Democratic nominee list); NPR 2026-07-26; NYT 2026-07-25 (URLs below).
Stub only: blank scores, confidence null, not evidence-scored. Idempotent.
Usage: /opt/homebrew/bin/python3 add-me-senate-2026-jackson-stub.py [--dry-run]
"""
from __future__ import annotations

import importlib.util
import json
import sys
from datetime import date

SCORECARD = "data/scorecard.json"
SLUG = "troy-jackson-senate"
SOURCES = [
    "https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Maine",
    "https://www.npr.org/2026/07/26/nx-s1-5906372/troy-jackson-replaces-graham-platner-as-democratic-candidate-in-maines-senate-race",
    "https://www.nytimes.com/2026/07/25/us/politics/troy-jackson-maine-senate-democrats-platner.html",
]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    today = date.today().isoformat()
    sc = json.load(open(SCORECARD, encoding="utf-8"))
    if any(c["slug"] == SLUG for c in sc["candidates"]):
        print(f"skip {SLUG}: already present")
        return
    rr = load("refine-records.py", "rr")
    seed = load("add-va-nov-2026-ballot-stubs.py", "seed")
    rec = {
        "name": "Troy Jackson", "slug": SLUG, "state": "ME",
        "office": "U.S. Senate Maine (2026 D nominee · chosen by convention 2026-07-25 after Graham Platner withdrew)",
        "jurisdiction": "State of Maine", "party": "D", "level": "federal",
        "id": f"{SLUG}-me", "status": "active", "candidacy_status": "general_candidate",
        "website": "", "photo": "", "sources": SOURCES,
        "notes": (f"Stub seeded {today} (MBP-1003-NIGHT r3). Maine Democrats nominated Troy Jackson "
                  "by state convention on 2026-07-25 to replace primary winner Graham Platner, who "
                  "withdrew, on the November 3, 2026 ballot (Wikipedia race page; NPR; NYT). Same "
                  "person as troy-jackson-gov (lost the June 9 governor primary). Not evidence-scored."),
        "footnotes": {}, "answer_footnotes": {}, "scores": None,
        "profile": {
            "next_election": 2026, "next_election_type": "general", "seat_up_next": True,
            "next_election_date": "2026-11-03", "confidence": None,
            "confidence_note": "Seeded for the race only — not evidence-reviewed.",
            "last_curated": today,
        },
        "claims": [],
    }
    tier = rr.classify_office_tier(rec)
    assert tier == "federal", tier
    rec["scores"] = seed.blank_scores(sc["categories"], sc["meta"]["rubrics"][tier], tier)
    sc["candidates"].append(rec)
    print(f"+ {SLUG}  D  {rec['office']}")
    if "--dry-run" in sys.argv:
        return
    with open(SCORECARD, "w", encoding="utf-8") as f:
        f.write(json.dumps(sc, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
