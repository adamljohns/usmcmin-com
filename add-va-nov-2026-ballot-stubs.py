#!/usr/bin/env python3
"""Seed race-board stubs for people on Virginia's certified 2026-11-03 ballot who had no
scorecard record (MBP-1003-NIGHT r3).

Source, and the only source: the official Virginia Department of Elections ENR feed
    https://enr.elections.virginia.gov/results/public/api/elections/virginia/2026-November-General/data
Every name, party and contest below is checked against that feed at run time; a name
that is not on the ballot under the stated contest aborts the run.

Stubs only, the same shape as the 2026-07-24 race stubs (736323d293f): blank scores,
confidence null, NOT evidence-scored. Nothing about a person's positions is asserted.
The grind / a dossier must evidence-score them. N/A masking follows the engine's own
rule (refine-records.py: tier rubric x categories[].applicable_at).

Idempotent: slugs already present are skipped.
Usage:  /opt/homebrew/bin/python3 add-va-nov-2026-ballot-stubs.py [--dry-run] [--feed FILE]
"""
from __future__ import annotations

import importlib.util
import json
import sys
import urllib.request
from datetime import date

FEED = ("https://enr.elections.virginia.gov/results/public/api/elections/virginia/"
        "2026-November-General/data")
SCORECARD = "data/scorecard.json"
RACES = "data/races.json"
TODAY = date.today().isoformat()

# slug, display name, exact ballot name, ballot party abbr, contest (English), district, kind
STUBS = [
    ("geral-staten", "Geral Staten", 'Geral D. "Bishop" Staten', "I",
     "Member, House of Representatives (2nd District)", 2, "us_house"),
    ("robert-murray-jr", "Robert Murray Jr.", 'Robert P. "Family Man" Murray, Jr.', "R",
     "Member, House of Representatives (4th District)", 4, "us_house"),
    ("joan-bell", "Joan Bell", 'Joan E. "Andrews" Bell', "I",
     "Member, House of Representatives (4th District)", 4, "us_house"),
    ("randall-terry", "Randall Terry", "Randall A. Terry", "I",
     "Member, House of Representatives (7th District)", 7, "us_house"),
    ("tim-sharman", "Tim Sharman", "Tim S. Sharman", "I",
     "Member, House of Representatives (8th District)", 8, "us_house"),
    ("ahsen-mujeeb-malik", "Ahsen Mujeeb Malik", "Ahsen Mujeeb Malik", "I",
     "Member, House of Representatives (10th District)", 10, "us_house"),
    ("dianne-blais", "Dianne Blais", "Dianne L. Blais", "G",
     "Member, House of Representatives (11th District)", 11, "us_house"),
    # HD-20 special election (Michelle Maldonado resigned eff. 2026-05-31 per her record)
    ("sonia-vasquez-luna", "Sonia Ruth Vasquez Luna", "Sonia Ruth Vasquez Luna", "D",
     "Member, House of Delegates (20th District)", 20, "va_house_special"),
    ("nate-fritzen", "Nate Fritzen", 'Nathaniel "Nate" Fritzen', "R",
     "Member, House of Delegates (20th District)", 20, "va_house_special"),
]


def en(arr):
    return next((x.get("text") for x in (arr or []) if x.get("languageId") == "en"), None)


def load_ballot(path: str | None) -> dict[str, list[tuple[str, str | None]]]:
    if path:
        d = json.load(open(path))
    else:
        req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
    out = {}
    for bi in d.get("ballotItems") or []:
        out[en(bi.get("name"))] = [
            (en(o.get("name")), (o.get("party") or {}).get("abbreviation"))
            for o in (bi.get("summaryResults") or {}).get("ballotOptions") or []]
    return out


def engine():
    spec = importlib.util.spec_from_file_location("rr", "refine-records.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def blank_scores(categories, rubric, tier):
    cats = set(rubric["pillar_a"] + rubric["pillar_b"])
    out = {}
    for cat in categories:
        aa = cat.get("applicable_at") or []
        out[cat["id"]] = [None if (cat["id"] in cats and q < len(aa) and tier in (aa[q] or []))
                          else "N/A" for q in range(5)]
    return out


def main():
    dry = "--dry-run" in sys.argv
    feed_file = sys.argv[sys.argv.index("--feed") + 1] if "--feed" in sys.argv else None
    ballot = load_ballot(feed_file)
    sc = json.load(open(SCORECARD))
    races = json.load(open(RACES))
    rr = engine()
    have = {c["slug"] for c in sc["candidates"]}
    added = []
    for slug, name, ballot_name, party, contest, district, kind in STUBS:
        if (ballot_name, party) not in ballot.get(contest, []):
            sys.exit(f"ABORT: {ballot_name!r} ({party}) not on the ballot for {contest!r}")
        if slug in have:
            print(f"skip {slug}: already present")
            continue
        if kind == "us_house":
            office = f"U.S. Representative VA-{district:02d} (2026 candidate)"
            race_id = f"va-us-house-{district:02d}-2026"
            race_office = f"U.S. House — Virginia District {district}"
            level, jurisdiction = "federal", "Commonwealth of Virginia"
        else:
            office = f"House of Delegates — District {district} (2026-11-03 special election candidate)"
            race_id = None
            race_office = f"Virginia House of Delegates — District {district} (special)"
            level, jurisdiction = "state", "Virginia House of Delegates"
        rec = {
            "name": name, "slug": slug, "state": "VA", "office": office,
            "jurisdiction": jurisdiction, "party": party, "level": level,
            "district": district, "id": f"{slug}-va", "status": "active",
            "candidacy_status": "general_candidate", "website": "", "photo": "",
            "sources": [FEED],
            "notes": (f"Stub seeded {TODAY} (MBP-1003-NIGHT r3) from the official Virginia "
                      f"Department of Elections ENR feed for the 2026-11-03 general: on the "
                      f"certified ballot for {contest} as {ballot_name} ({party}). "
                      f"Not evidence-scored."),
            "footnotes": {}, "answer_footnotes": {}, "scores": None,
            "profile": {
                "next_election": 2026,
                "next_election_type": "general" if kind == "us_house" else "special",
                "seat_up_next": True, "next_election_date": "2026-11-03",
                "confidence": None,
                "confidence_note": "Seeded from the certified ballot for race pages only — not evidence-reviewed.",
                "last_curated": TODAY,
                "candidacy": {"race_id": race_id, "office": race_office, "is_incumbent": False,
                              "primary_date": "", "general_date": "2026-11-03"},
            },
            "claims": [],
        }
        if race_id:
            rec["race_id"] = race_id
        tier = rr.classify_office_tier(rec)
        assert tier == level, (slug, tier, level)
        rec["scores"] = blank_scores(sc["categories"], sc["meta"]["rubrics"][tier], tier)
        sc["candidates"].append(rec)
        added.append(slug)
        if race_id:
            race = races["races"].get(race_id)
            if race is None:
                sys.exit(f"ABORT: race {race_id} missing from {RACES}")
            lst = race.setdefault("candidates_by_party", {}).setdefault(party, [])
            if slug not in lst:
                lst.append(slug)
            if FEED not in race.setdefault("sources", []):
                race["sources"].append(FEED)
        print(f"+ {slug:22} {party}  {office}")

    # VA-04's board note predates the GOP nomination; the certified ballot settles it.
    r4 = races["races"].get("va-us-house-04-2026") or {}
    old = "GOP had no filed candidate as of May 28 2026 filing; committee may still name one."
    if old in (r4.get("incumbent_note") or ""):
        r4["incumbent_note"] = r4["incumbent_note"].replace(
            old, "Certified November ballot (VA Dept of Elections) lists Robert P. Murray Jr. "
                 "as the Republican nominee.")
        print("~ va-us-house-04-2026 incumbent_note updated")

    print(f"{len(added)} stub(s) added")
    if dry or not added:
        return
    # match the on-disk format (indent=2, raw UTF-8, trailing newline) so the diff is
    # only the new records; a format flip would rewrite every line of an 85 MB file
    for path, obj in ((SCORECARD, sc), (RACES, races)):
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
