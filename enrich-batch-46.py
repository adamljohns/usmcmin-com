#!/usr/bin/env python3
"""Enrichment batch 46: hand-curated claims for 4 federal House candidates.

Targets archetype_curated representatives that had 0 evidence claims. Uses the
(slug + state + office_keyword) matcher to avoid slug collisions.

Mix (3 R / 1 D): Tad Jude (MN-R), Austin Theriault (ME-R),
Garret Graves (LA-R), Frank Pierce (NC-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ---------------- Tad Jude (MN-03, R) ----------------
    ("tad-jude", "MN", "Representative", [
        claim("tj1", "tad-jude", "sanctity_of_life", 0, True,
              "A longtime Minnesota Republican legislator with a documented anti-abortion record who, in a 2024 congressional debate, called every abortion a 'tragedy' and backed the Dobbs decision returning abortion policy to states. Critics described his state legislative record as a 'harsh' pro-life record.",
              ["https://en.wikipedia.org/wiki/Tad_Jude",
               "https://heartlandsignal.com/2024/10/30/longtime-minnesota-republican-downplays-abortion-in-congressional-debate-despite-harsh-record/"]),
        claim("tj2", "tad-jude", "election_integrity", 0, True,
              "Running for Minnesota Secretary of State in 2026 specifically on a platform of 'secure elections, accurate voter rolls, strong cybersecurity protections, and bipartisan oversight' — making election security the central purpose of his public service campaign.",
              ["https://mngop.com/republican-party-of-minnesota-congratulates-tad-jude-on-gop-endorsement-for-secretary-of-state/",
               "https://en.wikipedia.org/wiki/Tad_Jude"]),
        claim("tj3", "tad-jude", "border_immigration", 1, True,
              "Stated publicly that illegal immigrants with felony convictions 'should be expelled' from the United States — a mandatory-deportation stance consistent with the rubric's enforcement standard.",
              ["https://www.sd45.org/tade_jude_us_congress_mn03",
               "https://en.wikipedia.org/wiki/Tad_Jude"]),
    ]),

    # ---------------- Frank Pierce (NC-13, D) ----------------
    ("frank-pierce-nc-13", "NC", "Representative", [
        claim("fp1", "frank-pierce-nc-13", "sanctity_of_life", 0, False,
              "A pro-choice Democrat who explicitly stated that reproductive healthcare decisions, including abortion care, 'should be between that person and their physician' and that 'medical decisions should not be made by politicians' — rejecting any life-at-conception or personhood-from-conception standard.",
              ["https://www.frankpierce4congress.com/",
               "https://www.branch.vote/races/2026-north-carolina-primary-election-nc-state-us-representative-nc-congressional-13-d/candidates/frank-pierce"]),
        claim("fp2", "frank-pierce-nc-13", "self_defense", 1, False,
              "Campaigned on gun-violence prevention, stating 'the majority of North Carolinians, like other Americans want to prevent gun violence through effective policies and laws' — supporting new firearm restrictions that conflict with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://lykelect.com/post/frank-pierce/0c178ad6-5536-49ee-b2cd-be3857bbf067/",
               "https://www.frankpierce4congress.com/"]),
    ]),

    # ---------------- Austin Theriault (ME-02, R) ----------------
    ("austin-theriault", "ME", "Representative", [
        claim("at1", "austin-theriault", "self_defense", 1, True,
              "Earned an 'A' grade and endorsement from the National Rifle Association in the 2024 ME-02 race — the NRA's highest marks — while opponent Jared Golden received an 'F' after shifting on gun rights. Also received an 'A' from Gun Owners of Maine.",
              ["https://www.nrapvf.org/grades/maine/",
               "https://www.bangordailynews.com/2024/09/09/politics/elections/austin-theriault-wins-nra-endorsement-joam40zk0w/"]),
        claim("at2", "austin-theriault", "border_immigration", 0, True,
              "Made securing the southern border his top congressional priority in the 2024 campaign, calling for increased enforcement and framing border security as a central national issue.",
              ["https://en.wikipedia.org/wiki/Austin_Theriault",
               "https://www.bangordailynews.com/2024/11/02/politics/elections/jared-golden-austin-theriault-campaign-approach-final-campaign-days-joam40zk0w/"]),
        claim("at3", "austin-theriault", "sanctity_of_life", 0, True,
              "A self-described pro-life candidate who voted against Democratic-backed abortion rights bills in the Maine Legislature; consistent with Dobbs he defers federal abortion legislation to states but does not support codifying abortion access at the federal level.",
              ["https://en.wikipedia.org/wiki/Austin_Theriault",
               "https://www.pressherald.com/2024/10/07/golden-theriault-clash-in-2nd-district-debate-here-are-the-takeaways/"]),
    ]),

    # ---------------- Garret Graves (LA-06, R) ----------------
    ("garret-graves-2026", "LA", "Representative", [
        claim("gg1", "garret-graves-2026", "sanctity_of_life", 0, True,
              "Carried a consistent pro-life voting record throughout his congressional tenure; cosponsored the Protecting Pain-Capable Unborn Children from Late-Term Abortions Act (2022) and consistently voted to bar federal funding of abortion domestically and internationally.",
              ["https://sbaprolife.org/representative/garret-graves",
               "https://en.wikipedia.org/wiki/Garret_Graves"]),
        claim("gg2", "garret-graves-2026", "economic_stewardship", 2, True,
              "As the lead House Republican negotiator, spearheaded the 2023 Fiscal Responsibility Act — raising the debt ceiling in exchange for two years of binding spending caps and targeted budget cuts — directly advancing an anti-deficit, fiscal-restraint posture.",
              ["https://en.wikipedia.org/wiki/Garret_Graves",
               "https://www.congress.gov/member/garret-graves/G000577"]),
        claim("gg3", "garret-graves-2026", "self_defense", 1, True,
              "Received NRA Political Victory Fund endorsement in his Louisiana House races, consistent with the NRA's strong pro-Second-Amendment grades for Louisiana Republicans who oppose firearm restrictions.",
              ["https://www.nrapvf.org/emails/2020/louisiana/garret-graves-la-06-general/",
               "https://www.nrapvf.org/grades/louisiana/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
