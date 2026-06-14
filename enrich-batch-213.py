#!/usr/bin/env python3
"""Enrichment batch 213: 4th claims for 5 sitting U.S. Senators from the bottom
of the alphabet (SD x2, SC x2, RI). archetype_curated bucket exhausted;
continuing the evidence_curated 3→4 claim track.

Targets: Mike Rounds (SD-R), John Thune (SD-R), Tim Scott (SC-R),
         Lindsey Graham (SC-R), Sheldon Whitehouse (RI-D).
Each adds one sourced claim in a distinct rubric category not yet covered.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------------- Mike Rounds (SD-R, US Senator) ----------------
    ("mike-rounds", "SD", "Senator", [
        claim("mr4", "mike-rounds", "economic_stewardship", 2, True,
              "From his first days in Washington, Rounds co-sponsored a Balanced Budget Amendment to the U.S. Constitution, explicitly comparing the federal budget to South Dakota's constitutionally mandated balanced budget, and voted against deficit-expanding legislation including the American Rescue Plan Act of 2021 ($1.9 trillion) and the Inflation Reduction Act of 2022 — a consistent anti-deficit posture aligning with the rubric's balanced-budget standard.",
              ["https://www.rounds.senate.gov/issues/list/budget",
               "https://ballotpedia.org/Mike_Rounds",
               "https://www.govtrack.us/congress/members/mike_rounds/412669"]),
    ]),

    # ---------------- John Thune (SD-R, US Senator) ----------------
    ("john-thune", "SD", "Senator", [
        claim("jt4", "john-thune", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (H.R. 8404) on November 29, 2022 (Senate roll-call vote #362; final tally 61–36), which federally codified recognition of same-sex unions and effectively repealed the Defense of Marriage Act — maintaining his opposition to the federal redefinition of marriage. Thune also co-sponsored an amendment to add religious-liberty protections for those holding sincerely held beliefs about marriage.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1172/vote_117_2_00362.htm",
               "https://ballotpedia.org/John_Thune"]),
    ]),

    # ---------------- Tim Scott (SC-R, U.S. Senator) ----------------
    ("tim-scott", "SC", "Senator", [
        claim("ts4", "tim-scott", "biblical_marriage", 0, True,
              "Affirms the one-man-one-woman definition of marriage and voted against the Respect for Marriage Act of 2022 (Senate vote #362), which federalized recognition of same-sex unions. His official Senate website states: 'The people of South Carolina have voted overwhelmingly to protect the traditional definition of marriage, and I stand with their decision' — a direct affirmation of the biblical marriage standard the rubric measures.",
              ["https://www.scott.senate.gov/issues/conservative-values/",
               "https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://ballotpedia.org/Tim_Scott"]),
    ]),

    # ---------------- Lindsey Graham (SC-R, U.S. Senator) ----------------
    ("lindsey-graham", "SC", "Senator", [
        claim("lg4", "lindsey-graham", "border_immigration", 1, False,
              "As one of the bipartisan 'Gang of Eight,' Graham co-authored and co-sponsored the Border Security, Economic Opportunity, and Immigration Modernization Act of 2013 (S.744), which offered a 13-year path to citizenship for an estimated 11 million undocumented immigrants already in the United States. The bill passed the Senate 68–32 but died in the House. This path-to-citizenship framework directly contradicts the rubric's mandatory-deportation standard.",
              ["https://www.congress.gov/bill/113th-congress/senate-bill/744",
               "https://en.wikipedia.org/wiki/Gang_of_Eight_(immigration)",
               "https://ballotpedia.org/Lindsey_Graham"]),
    ]),

    # ---------------- Sheldon Whitehouse (RI-D, US Senator) ----------------
    ("sheldon-whitehouse", "RI", "Senator", [
        claim("sw4", "sheldon-whitehouse", "border_immigration", 0, False,
              "A consistent opponent of military-style border-wall construction: opposed President Trump's 2019 national-emergency declaration to redirect DoD funds for wall-building, voted against wall appropriations in omnibus packages, and in 2024 supported the bipartisan Border Act of 2024 (S.4361) — which emphasized technology, immigration judges, and asylum reform rather than physical barriers or military deployment — opposing the rubric's wall-and-military enforcement model.",
              ["https://www.govtrack.us/congress/members/sheldon_whitehouse/412247",
               "https://ballotpedia.org/Sheldon_Whitehouse",
               "https://www.congress.gov/bill/118th-congress/senate-bill/4361"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
