#!/usr/bin/env python3
"""Enrichment batch 543: 5 claims across 5 active 2026 federal candidates.

Targets evidence_curated U.S. Congress / Senate candidates with exactly 2 claims,
taken from the bottom of the alphabet (MI, ME, IL, IA) after the archetype_curated
senator/representative buckets reached 0 remaining entries.

Targets (reverse alpha by state):
  Carl Marlinga       (MI-10, D nominee — 3rd run; former Macomb Co prosecutor/judge)
  Matthew Dunlap      (ME-02, D nominee — former ME SecState + SAM exec dir; faces LePage)
  La Shawn Ford       (IL-07, D nominee — IL state rep; Davis-endorsed)
  Christina Bohannan  (IA-01, D candidate — 3rd run; former IA state rep/law prof)
  Clint Twedt-Ball    (IA, D — 2026 U.S. Senate candidate, Ernst seat)

One distinct rubric-category claim per target (adding to their existing 2 claims).
Sources: ballotpedia.org, elections.bradyunited.org, mainepublic.org, wttw.com,
newsfromthestates.com, chicago.suntimes.com, clintforiowa.com.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub 50MB limit.
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
    # ------------ Carl Marlinga (MI-10, D nominee) ------------
    ("carl-marlinga-2026", "MI", "MI-10", [
        claim("cm2026sd1", "carl-marlinga-2026", "self_defense", 1, False,
              "Earned the endorsement of the Brady Campaign to Prevent Gun Violence for the 2024 and 2026 MI-10 races, and stated explicit support for universal background checks, mandatory safe-storage laws, and restrictions on assault-style weapons — directly opposing the rubric's anti-AWB / anti-registry ideal.",
              ["https://elections.bradyunited.org/candidates/carl-marlinga",
               "https://www.wxyz.com/news/national-politics/america-votes/one-on-one-with-carl-marlinga-on-the-economy-election-integrity-immigration-more"]),
    ]),

    # ------------ Matthew Dunlap (ME-02, D nominee) ------------
    ("matthew-dunlap", "ME", "ME-02", [
        claim("mdes2a", "matthew-dunlap", "economic_stewardship", 2, False,
              "Campaigns on Medicare for All, eliminating the payroll-tax cap to expand Social Security, and robust federal investments in affordable housing and rural infrastructure — a pro-spending platform that expands federal outlays and contradicts the rubric's anti-deficit / balanced-budget standard.",
              ["https://www.mainepublic.org/politics/2026-04-19/your-vote-2026-profile-matt-dunlap-democrat-for-2nd-district",
               "https://www.pressherald.com/2026/04/17/how-matt-dunlap-seeks-to-win-maines-trump-voting-congressional-district-as-a-progressive/"]),
    ]),

    # ------------ La Shawn Ford (IL-07, D nominee) ------------
    ("la-shawn-ford", "IL", "IL-07", [
        claim("lsfbi1a", "la-shawn-ford", "border_immigration", 1, False,
              "Explicitly advocates for 'a path to citizenship for longtime residents, Dreamers, and essential workers,' expanded legal work visas, and faster asylum processing — framing immigration reform as 'humane, fair, and practical' and directly rejecting the mandatory-deportation standard the rubric demands.",
              ["https://chicago.suntimes.com/elections/2026/candidate-questionnaires/la-shawn-k-ford-illinois-primary-7th-congressional-district",
               "https://news.wttw.com/elections/voters-guide/2026-primary/lashawn-k-ford"]),
    ]),

    # ------------ Christina Bohannan (IA-01, D candidate) ------------
    ("christina-bohannan", "IA", "IA-01", [
        claim("cbbi1a", "christina-bohannan", "border_immigration", 1, False,
              "Stated that 'we do need to secure our border, but we do need to provide a path to citizenship' and criticized Congress for failing on immigration — explicitly opposing mandatory deportation and supporting a legalization pathway for undocumented residents.",
              ["https://www.newsfromthestates.com/article/democratic-congressional-candidate-christina-bohannan-calls-immigration-reform-education",
               "https://iowacapitaldispatch.com/2025/06/17/christina-bohannan-launches-bid-for-1st-congressional-district-seat/"]),
    ]),

    # ------------ Clint Twedt-Ball (IA, D Senate candidate — Ernst seat) ------------
    ("clint-twedt-ball", "IA", "Ernst", [
        claim("ctbes2a", "clint-twedt-ball", "economic_stewardship", 2, False,
              "Runs on expanding federal conservation funding, government-backed regional energy investment programs for rural communities, and robust farm-support spending — a pro-federal-outlays platform inconsistent with the rubric's anti-deficit / balanced-budget ideal.",
              ["https://www.clintforiowa.com/",
               "https://ballotpedia.org/Clint_Twedt-Ball"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
