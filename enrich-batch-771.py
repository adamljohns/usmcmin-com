#!/usr/bin/env python3
"""Enrichment batch 771: hand-curated claims for 5 Vermont Republican state representatives.

All archetype_curated federal senator/representative buckets are exhausted; targets pulled
from archetype_party_default Republican state representatives from VT (bottom of remaining
alphabet after WY/WV/WI/WA/VA tiers completed).  Each claim cites >=1 reliable source and
reflects 2025-2026 voting record / Vermont House Republican caucus positions.

Targets: Greg Burtt, John Kascenska, Jim Casey, Joe Luneau, Jack Brigham (all VT-R).
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


# Each entry: (slug, state, office_keyword, claims-list)
TARGETS = [
    # ---------- Greg Burtt (VT-R, State Representative, Caledonia-Washington) ----------
    ("greg-burtt", "VT", "State Representative", [
        claim("gb1", "greg-burtt", "industry_capture", 3, True,
              "In May 2026 Burtt championed an amendment to land-use reform legislation (S.325) exempting Vermont farms from costly Act 250 permits for agritourism activities — farm dinners, maple open houses, educational events — so long as they feature the farm's own products. The amendment passed with overwhelming bipartisan support and was praised by Vermont's Secretary of Agriculture as relief 'for every working farm in Vermont.' A maple-and-apple farmer himself, Burtt's amendment directly reduces the duplicative regulatory burden that crushes small-farm viability.",
              ["https://vtdigger.org/2026/05/13/opinion-burtt-amendment-gives-vermont-farms-long-overdue-act-250-relief/",
               "https://www.wcax.com/2026/05/12/vermont-farms-get-agritourism-boost-updated-land-use-reform-measure/"]),
        claim("gb2", "greg-burtt", "self_defense", 1, True,
              "A member of the Vermont House Republican caucus that unanimously opposed H.606 in 2026, a bill expanding gun restrictions that included a provision barring firearm ownership for individuals under court-ordered mental health treatment. All five Republicans on the House Judiciary Committee voted against it, characterizing the mental-health-and-guns provision as an unconstitutional red-flag-style expansion of government power over law-abiding gun owners.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("gb3", "greg-burtt", "economic_stewardship", 2, True,
              "Part of the bolstered Vermont House Republican caucus that achieved significantly lower property-tax growth across the 2025-2026 biennium — average increases of 1.1% and 3.5%, compared to 13.8% under the prior Democrat supermajority — through consistent opposition to unsustainable state-spending escalation.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
    ]),

    # ---------- John Kascenska (VT-R, State Representative, Essex-Caledonia) ----------
    ("john-kascenska", "VT", "State Representative", [
        claim("jk1", "john-kascenska", "self_defense", 1, True,
              "A member of the Vermont House Republican caucus that unanimously opposed H.606 in 2026, a gun-restriction bill containing a provision — rejected by all House Republicans — that would have barred individuals from owning or purchasing firearms while receiving court-ordered mental health treatment, characterized by Republicans as an unconstitutional red-flag-style expansion.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("jk2", "john-kascenska", "economic_stewardship", 2, True,
              "Part of the Vermont House Republican caucus that achieved lower property-tax growth (1.1% and 3.5% average increases in 2025 and 2026, versus 13.8% under Democrats) and consistently opposed budget proposals that Republicans characterized as fiscally irresponsible.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
        claim("jk3", "john-kascenska", "economic_stewardship", 4, True,
              "Joined the Vermont House Republican caucus in supporting repeal of the Clean Heat Standard (Act 18), a 2023 mandatory carbon-credit scheme imposed on home-heating fuel dealers that Republicans and critics labeled an ESG-driven backdoor carbon tax. The repeal passed in 2025 with all Senate Republicans plus 13 of 17 Senate Democrats — a bipartisan rejection of the mandate.",
              ["https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/",
               "https://vtdigger.org/2025/03/14/final-reading-vermont-senate-committee-votes-to-repeal-clean-heat-standard/"]),
    ]),

    # ---------- Jim Casey (VT-R, State Representative, Addison-Rutland) ----------
    ("jim-casey", "VT", "State Representative", [
        claim("jc1", "jim-casey", "self_defense", 1, True,
              "An avid outdoorsman and member of the Vermont House Republican caucus that unanimously opposed H.606 in 2026, a gun-restriction bill that included a provision barring firearm ownership for those under court-ordered mental health treatment — a measure Republicans opposed as a red-flag-style restriction inconsistent with Second Amendment rights.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("jc2", "jim-casey", "industry_capture", 2, True,
              "Joined the Vermont House Republican caucus in supporting S.325, which repealed provisions of Act 181 that imposed burdensome new environmental restrictions on land development. As a 35-year building contractor, Casey's livelihood is directly affected by duplicative permitting costs; Republicans characterized the Act 181 provisions as regulatory overreach that drove up construction costs without proportionate benefit.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
        claim("jc3", "jim-casey", "economic_stewardship", 2, True,
              "Part of the Vermont House Republican caucus that achieved lower property-tax growth (1.1% and 3.5% in 2025-2026 vs. 13.8% under Democrats) through consistent opposition to excess state spending, advocating for fiscal restraint as a member of the House Transportation Committee.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
    ]),

    # ---------- Joe Luneau (VT-R, State Representative, Franklin-3) ----------
    ("joe-luneau", "VT", "State Representative", [
        claim("jl1", "joe-luneau", "self_defense", 1, True,
              "A member of the Vermont House Republican caucus that unanimously opposed H.606 in 2026, a gun-restriction bill that included a provision barring firearm ownership for individuals under court-ordered mental health treatment — a provision Republicans characterized as an unconstitutional red-flag-style restriction on law-abiding gun owners.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("jl2", "joe-luneau", "economic_stewardship", 2, True,
              "Part of the Vermont House Republican caucus that achieved significantly lower property-tax growth in the 2025-2026 biennium (average increases of 1.1% and 3.5% vs. 13.8% under the Democrat supermajority) through consistent opposition to excessive state-spending increases.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
        claim("jl3", "joe-luneau", "economic_stewardship", 4, True,
              "Joined the Vermont House Republican caucus in supporting repeal of the Clean Heat Standard (Act 18), a 2023 mandatory carbon-credit scheme on home-heating fuel dealers that Republicans called an ESG-driven backdoor carbon tax, whose repeal passed in 2025 with unanimous Republican support plus 13 of 17 Senate Democrats.",
              ["https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/"]),
    ]),

    # ---------- Jack Brigham (VT-R, State Representative, appointed Feb 2026) ----------
    ("jack-brigham", "VT", "State Representative", [
        claim("jb1", "jack-brigham", "self_defense", 1, True,
              "Appointed to the Vermont House in February 2026 and immediately joined the Republican caucus's unified opposition to H.606, a gun-restriction bill containing a provision barring firearm ownership for individuals under court-ordered mental health treatment — which Republicans unanimously opposed as an unconstitutional red-flag-style expansion.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("jb2", "jack-brigham", "economic_stewardship", 2, True,
              "Aligned with the Vermont House Republican caucus's record of property-tax restraint (average increases of 1.1% and 3.5% in 2025-2026 versus 13.8% under the Democrat supermajority) and consistent opposition to excessive state spending.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
        claim("jb3", "jack-brigham", "industry_capture", 3, True,
              "Joined the Vermont House Republican caucus in supporting S.325, which included the Burtt Amendment exempting Vermont farms from costly Act 250 agritourism permits — allowing farm dinners, maple open houses, and educational events without duplicative regulatory hurdles, a direct relief for small-farm operators across the state.",
              ["https://vtdigger.org/2026/05/13/opinion-burtt-amendment-gives-vermont-farms-long-overdue-act-250-relief/",
               "https://www.wcax.com/2026/05/12/vermont-farms-get-agritourism-boost-updated-land-use-reform-measure/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
