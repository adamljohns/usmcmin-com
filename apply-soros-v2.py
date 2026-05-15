#!/usr/bin/env python3
"""Apply expanded Soros adjustments — both to existing scorecard candidates
matched by slug, and add new candidate records for the Soros-funded DAs
not currently in scorecard.

Reads data/soros_adjustments.json and writes profile.score_adjustments.soros
on every entry. New records are inserted with party-default baseline scores
(D = all-False in life/marriage/heritage; party_default confidence chip).
"""
import json
import re
import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
SOROS = ROOT / "data" / "soros_adjustments.json"

BRACKET_DELTA = {
    "verified_zero": +7,
    "zero": +7,
    "1_to_50k": -5,
    "50k_to_250k": -15,
    "250k_to_1m": -30,
    "1m_to_3m": -50,
    "3m_plus": -75,
}

DESCRIPTOR = (
    "The Open Society Foundations and the Democracy PAC vehicles tied to "
    "George Soros / Alex Soros direct hundreds of millions toward "
    "progressive prosecutors, judges, and ballot measures. RESOLUTE Citizen "
    "treats documented contributions as foreign-linked dark-money funding "
    "hostile to the historically orthodox Christian moral order. The "
    "specific failure mode is on life q4 — Soros-funded DAs systematically "
    "decline to prosecute attacks on pro-life pregnancy centers and refuse "
    "to enforce state abortion restrictions."
)


def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def party_default_scores_d():
    """Democrat-default baseline used by seed-state-assemblies.py and
    add-soros-prosecutors.py — every question False except a small set of
    consensus issues. Generates the 'party_default' confidence chip."""
    return {
        "america_first": [False, False, False, False, False],
        "life": [False, False, False, False, False],
        "immigration": [False, False, False, False, False],
        "marriage": [False, False, False, False, False],
        "christian_heritage": [None, None, None, None, None],
        "self_defense": [False, False, False, False, False],
        "education": [False, False, False, False, False],
    }


def main():
    sx = json.loads(SOROS.read_text())
    scorecard = json.loads(SCORECARD.read_text())
    today = date.today().isoformat()

    # 1) Apply to existing scorecard candidates by slug match
    entries = sx.get("entries", {})
    existing_set = 0
    not_found = []
    for slug, info in entries.items():
        matches = [c for c in scorecard["candidates"] if c.get("slug") == slug]
        if not matches:
            not_found.append(slug)
            continue
        bracket = info["category"]
        delta = BRACKET_DELTA.get(bracket, 0)
        for c in matches:
            profile = c.setdefault("profile", {}) or {}
            if not isinstance(profile, dict):
                profile = {}
                c["profile"] = profile
            adj = profile.setdefault("score_adjustments", {})
            adj["soros"] = {
                "delta": delta,
                "bracket": bracket,
                "dollars": info["dollars"],
                "note": info["note"],
                "sources": info.get("sources", []),
                "applied_on": today,
                "descriptor": DESCRIPTOR,
            }
            existing_set += 1

    # 2) Add new candidate records for DAs not currently in scorecard
    new_records = sx.get("new_records", {})
    added = 0
    skipped_dupe = 0
    next_id = max((c.get("id", 0) for c in scorecard["candidates"]), default=0) + 1
    existing_slugs = {c.get("slug") for c in scorecard["candidates"]}
    for slug, rec in new_records.items():
        if slug.startswith("_"):
            continue
        if slug in existing_slugs:
            skipped_dupe += 1
            continue
        bracket = rec["category"]
        delta = BRACKET_DELTA.get(bracket, 0)
        scores = party_default_scores_d()  # all these DAs are D
        new_cand = {
            "name": rec["name"],
            "slug": rec["slug"],
            "office": rec["office"],
            "jurisdiction": rec["jurisdiction"],
            "level": rec["level"],
            "party": rec["party"],
            "district": None,
            "id": next_id,
            "state": rec["state"],
            "scores": scores,
            "notes": "Added 2026-05-14 as part of foreign-influence-v2 expansion. Party-default Democrat baseline; refine with primary-source review.",
            "profile": {
                "confidence": "party_default",
                "score_adjustments": {
                    "soros": {
                        "delta": delta,
                        "bracket": bracket,
                        "dollars": rec["dollars"],
                        "note": rec["note"],
                        "sources": rec.get("sources", []),
                        "applied_on": today,
                        "descriptor": DESCRIPTOR,
                    }
                },
            },
            "sources": rec.get("sources", []),
            "claims": [],
            "footnotes": {},
            "answer_footnotes": {},
        }
        scorecard["candidates"].append(new_cand)
        existing_slugs.add(slug)
        next_id += 1
        added += 1

    SCORECARD.write_text(json.dumps(scorecard, indent=2))

    print(f"Existing scorecard candidates: Soros adjustment set on {existing_set} records")
    if not_found:
        print(f"Could not find {len(not_found)} entries by slug:")
        for s in not_found:
            print(f"  - {s}")
    print(f"\nNew DA records added: {added} (skipped {skipped_dupe} duplicates)")


if __name__ == "__main__":
    main()
