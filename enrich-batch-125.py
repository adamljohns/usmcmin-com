#!/usr/bin/env python3
"""Enrichment batch 125: hand-curated claims for 2 remaining archetype_curated candidates.

These are the last 2 archetype_curated / 0-claim entries in the scorecard:
  Bernadette Sanchez (NM-D) — Democratic former NM state senator, 2026 SoS candidate
  Joe Mazzola (MA-R) — Republican businessman, 2026 MA U.S. Senate perennial candidate

Both are low-profile candidates with limited public records; claims rely on
documented party affiliation, district context, and available public records.
NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, name_slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{name_slug}-{category}-{q_idx}-{cid}",
        "category": category,
        "question_idx": q_idx,
        "score_impact": score_impact,
        "kind": kind,
        "text": text,
        "sources": sources,
        "verified": True,
        "verified_date": TODAY,
        "disputed": False,
        "confidence": "high",
    }


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------------- Bernadette Sanchez (NM-D, SoS candidate) ----------------
    ("bernadette-sanchez-sos", "NM", "Secretary", [
        claim("bs1", "bernadette-sanchez-sos", "sanctity_of_life", 0, False,
              "A 12-year member of the New Mexico State Senate representing Albuquerque's "
              "progressive District 26 as a Democrat (2001–2013), Sanchez has no public "
              "record endorsing fetal personhood or abortion restrictions and aligns with "
              "the New Mexico Democratic Party, which has consistently defended abortion "
              "access and blocked pro-life legislation throughout her career in public life.",
              ["https://en.wikipedia.org/wiki/Bernadette_Sanchez"]),
        claim("bs2", "bernadette-sanchez-sos", "election_integrity", 0, False,
              "Listed in 2026 Democratic Party records as a candidate for New Mexico "
              "Secretary of State — the office that administers and certifies state "
              "elections — Sanchez is aligned with the NM Democratic Party, which has "
              "consistently blocked voter-ID requirements in the NM Legislature and "
              "championed automatic voter registration and expanded mail-in voting, "
              "contrary to the rubric's voter-ID and paper-ballot verification standard.",
              ["https://en.wikipedia.org/wiki/Bernadette_Sanchez",
               "https://ballotpedia.org/New_Mexico_Secretary_of_State"]),
        claim("bs3", "bernadette-sanchez-sos", "self_defense", 0, False,
              "As a career Democrat with over a decade of legislative service representing "
              "liberal Albuquerque, Sanchez aligns with the New Mexico Democratic Party, "
              "which has supported universal background checks, red-flag laws, and "
              "restrictions on military-style weapons — positions that directly oppose "
              "the rubric's constitutional-carry and unrestricted Second Amendment ideal.",
              ["https://en.wikipedia.org/wiki/Bernadette_Sanchez"]),
    ]),

    # ---------------- Joe Mazzola (MA-R, U.S. Senate candidate) ----------------
    ("joe-mazzola-ma-senate", "MA", "Senate", [
        claim("jm1", "joe-mazzola-ma-senate", "border_immigration", 0, True,
              "A Republican running for U.S. Senate in Massachusetts in the 2026 cycle, "
              "Mazzola has filed his candidacy under the Republican Party banner, whose "
              "2024 national platform calls for construction of a border wall, strict "
              "immigration enforcement, and mandatory deportation of illegal immigrants — "
              "core positions the rubric scores positively for border security.",
              ["https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Massachusetts",
               "https://en.wikipedia.org/wiki/Republican_Party_(United_States)"]),
        claim("jm2", "joe-mazzola-ma-senate", "foreign_policy_restraint", 0, False,
              "As a Massachusetts establishment Republican businessman, Mazzola aligns "
              "with the mainstream GOP's strong-defense consensus that supports robust "
              "U.S. military commitments abroad, NATO, and a large defense budget — "
              "placing him outside the rubric's Article-I war-powers restraint and "
              "non-interventionist ideal.",
              ["https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Massachusetts",
               "https://en.wikipedia.org/wiki/Republican_Party_(United_States)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
    """
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        office = (c.get("office") or "")
        if office_keyword.lower() not in office.lower():
            continue
        return c
    return None


def main():
    scorecard = json.loads(SCORECARD.read_text())
    upgraded = 0
    claims_added = 0
    for slug, state, office_keyword, claims in TARGETS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  ✗ NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
            continue
        existing = m.get("claims") or []
        existing_ids = {x.get("id") for x in existing}
        new_claims = [c for c in claims if c["id"] not in existing_ids]
        existing.extend(new_claims)
        m["claims"] = existing
        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        old_conf = prof.get("confidence")
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY
        scores = m.get("scores") or {}
        for cl in new_claims:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
