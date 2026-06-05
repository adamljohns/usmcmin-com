#!/usr/bin/env python3
"""Enrichment batch 62: hand-curated claims for 5 House candidates (bottom of alphabet).

Targets archetype_curated House candidates with 0 evidence claims, taken from
the bottom of the alphabet in the representative bucket:
Tim Greimel (MI-10-D), Adrian Boafo (MD-05-D), Wala Blegay (MD-05-D),
William Lawrence (MI-07-D), Matt Maasdam (MI-07-D).

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
    # ---------------- Tim Greimel (MI-10, D, House) ----------------
    ("tim-greimel", "MI", "Representative", [
        claim("tg1", "tim-greimel", "sanctity_of_life", 0, False,
              "As Michigan House Minority Leader (2013–2017), Greimel led Democratic opposition to Republican-backed abortion restrictions and championed reproductive rights; his 2026 congressional campaign commits to protecting abortion access, rejecting any life-from-conception standard.",
              ["https://ballotpedia.org/Tim_Greimel",
               "https://en.wikipedia.org/wiki/Tim_Greimel"]),
        claim("tg2", "tim-greimel", "economic_stewardship", 2, False,
              "Championed the Healthy Michigan Medicaid expansion adding more than 650,000 residents to government health insurance rolls, and passed two state laws raising Michigan's minimum wage and indexing it to inflation — expanding government entitlement spending rather than pursuing fiscal discipline or a balanced budget.",
              ["https://ballotpedia.org/Tim_Greimel",
               "https://en.wikipedia.org/wiki/Tim_Greimel"]),
    ]),

    # ---------------- Adrian Boafo (MD-05, D, House) ----------------
    ("adrian-boafo", "MD", "Representative", [
        claim("ab1", "adrian-boafo", "sanctity_of_life", 0, False,
              "As a Maryland state delegate (2023–), Boafo cosponsored SB975 providing state security grants to abortion clinics facing pro-life protest threats — directly supporting abortion provider infrastructure — and his 2026 congressional campaign platform pledges to protect 'a woman's right to choose,' rejecting any personhood-from-conception framework.",
              ["https://ballotpedia.org/Adrian_Boafo",
               "https://en.wikipedia.org/wiki/Adrian_Boafo"]),
        claim("ab2", "adrian-boafo", "foreign_policy_restraint", 1, False,
              "During his 2026 congressional campaign, Boafo stated he supports strengthening US–Israel relations and ensuring Israel 'has the security assistance it needs to defend itself' — endorsing continued American foreign military aid and entangling commitments rather than the non-interventionist, end-forever-wars posture the rubric calls for.",
              ["https://ballotpedia.org/Adrian_Boafo"]),
    ]),

    # ---------------- Wala Blegay (MD-05, D, House) ----------------
    ("wala-blegay", "MD", "Representative", [
        claim("wb1", "wala-blegay", "sanctity_of_life", 0, False,
              "A progressive Democrat and longtime advocate for 'women's rights' and reproductive health care access — an explicit pillar of her congressional campaign — Blegay is firmly aligned with the pro-choice movement, having championed civil rights, women's rights, and reproductive health access throughout her tenure on the Prince George's County Council.",
              ["https://ballotpedia.org/Wala_Blegay",
               "https://www.nbcwashington.com/news/local/prince-georges-county/prince-georges-county-council-member-wala-blegay-announces-run-for-congress/4054270/"]),
        claim("wb2", "wala-blegay", "economic_stewardship", 2, False,
              "Blegay's congressional platform calls for expanding public transit infrastructure across Prince George's, Charles, and St. Mary's Counties and directing government investment in economic development — prioritizing increased government spending and intervention over balanced-budget fiscal restraint.",
              ["https://ballotpedia.org/Wala_Blegay",
               "https://dbknews.com/2026/02/04/prince-georges-county-wala-blegay-congress/"]),
    ]),

    # ---------------- William Lawrence (MI-07, D, House) ----------------
    ("william-lawrence-mi-07", "MI", "Representative", [
        claim("wl1", "william-lawrence-mi-07", "foreign_policy_restraint", 1, True,
              "Co-founder of the Sunrise Movement who has sharply criticized U.S. military involvement in the 2026 Iran war and the Gaza conflict, Lawrence has called to 'stop spending our money on wars' — an anti-interventionist posture consistent with the rubric's goal of ending forever wars and restraining foreign military entanglements.",
              ["https://michiganadvance.com/2025/08/27/lansing-activist-joins-the-democratic-fray-for-michigans-7th-congressional-district/",
               "https://ballotpedia.org/William_Lawrence_(Michigan)"]),
        claim("wl2", "william-lawrence-mi-07", "border_immigration", 1, False,
              "Actively opposed ICE operations in Michigan, speaking out against construction of a new ICE detention and processing center in Romulus — a stance directly at odds with the rubric's call for mandatory deportation of illegal immigrants and robust border enforcement.",
              ["https://michiganadvance.com/2025/08/27/lansing-activist-joins-the-democratic-fray-for-michigans-7th-congressional-district/",
               "https://ballotpedia.org/William_Lawrence_(Michigan)"]),
    ]),

    # ---------------- Matt Maasdam (MI-07, D, House) ----------------
    ("matt-maasdam", "MI", "Representative", [
        claim("mm1", "matt-maasdam", "self_defense", 1, False,
              "A retired Navy SEAL and VoteVets-endorsed candidate who explicitly supports 'commonsense gun safety' measures as a self-described 'responsible gun owner' — a framework encompassing background-check expansions and firearm restrictions the rubric opposes as encroachments on Second Amendment rights.",
              ["https://votevets.org/candidates/matt-maasdam",
               "https://ballotpedia.org/Matt_Maasdam"]),
        claim("mm2", "matt-maasdam", "economic_stewardship", 2, False,
              "Maasdam's healthcare platform centers on protecting Medicaid and the Affordable Care Act from cuts and expanding access to government-backed insurance — prioritizing growth of government entitlement rolls over the balanced-budget fiscal discipline the rubric calls for.",
              ["https://ballotpedia.org/Matt_Maasdam",
               "https://www.michiganpublic.org/politics-government/2025-07-01/second-democrat-announces-primary-campaign-to-unseat-gop-congressman-in-competitive-michigan-7th-district"]),
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
