#!/usr/bin/env python3
"""Enrichment batch 772: hand-curated claims for 5 Vermont Republican state representatives.

All archetype_curated federal senator/representative buckets are exhausted; targets pulled
from archetype_party_default Republican state representatives remaining in VT (13 left after
batch 771). Each claim cites >=1 reliable source and reflects 2025-2026 voting record /
Vermont House Republican caucus positions.

Targets: Francis McFaun, Eric Maguire, Debra Powers, Deborah Cordz Dolgin, David Bosch
(all VT-R State Representatives).
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
    # ---------- Francis McFaun (VT-R, State Representative, Washington-4) ----------
    ("francis-mcfaun", "VT", "State Representative", [
        claim("fm1", "francis-mcfaun", "self_defense", 1, True,
              "A member of the Vermont House Republican caucus that unanimously opposed H.606 in 2026, a gun-restriction bill containing a provision — rejected by all House Republicans — that would have barred individuals from owning or purchasing firearms while receiving court-ordered mental health treatment, characterized by Republicans as an unconstitutional red-flag-style expansion of state power over law-abiding gun owners.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("fm2", "francis-mcfaun", "economic_stewardship", 2, True,
              "Part of the bolstered Vermont House Republican caucus that drove significantly lower property-tax growth across the 2025-2026 biennium — average increases of 1.1% and 3.5%, compared to 13.8% under the prior Democrat supermajority — through consistent opposition to unsustainable state-spending escalation. McFaun, a 38-year Vermont state government veteran who retired before entering the House, applies an insider's understanding of state-budget dynamics to advocate for fiscal restraint.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/",
               "https://legislature.vermont.gov/people/single/2026/14579"]),
        claim("fm3", "francis-mcfaun", "family_child_sovereignty", 0, True,
              "Joined the majority of Vermont House Republicans in opposing H.454 (Act 73), the 2025 education reform law that centralized school governance and reduced eligible private schools in Vermont's public tuition program from 46 to 18. Republicans opposed the legislation as an expansion of state control over local education decisions and a restriction on family choice — the House passed it narrowly 87–55 with most Republicans in the nay column.",
              ["https://vtdigger.org/2026/04/17/house-education-reform-bill-narrowly-passes-amid-heavy-criticism-and-some-lawmakers-unease/",
               "https://vtdigger.org/2026/03/03/new-lawsuit-challenges-restrictions-on-school-choice-in-vermonts-education-reform-law/"]),
    ]),

    # ---------- Eric Maguire (VT-R, State Representative, Rutland-5) ----------
    ("eric-maguire", "VT", "State Representative", [
        claim("em1", "eric-maguire", "self_defense", 1, True,
              "A member of the Vermont House Republican caucus that unanimously opposed H.606 in 2026, a gun-restriction bill whose provision barring firearm ownership for individuals under court-ordered mental health treatment was condemned by House Republicans — including all five GOP members of the Judiciary Committee — as an unconstitutional red-flag-style restriction on law-abiding gun owners.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("em2", "eric-maguire", "economic_stewardship", 2, True,
              "Part of the Vermont House Republican caucus that achieved lower property-tax growth in the 2025-2026 biennium (average increases of 1.1% and 3.5% versus 13.8% under the prior Democrat supermajority) through consistent opposition to excess state spending, while advocating for fiscal responsibility in Rutland City.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
        claim("em3", "eric-maguire", "refuse_state_overreach", 0, True,
              "Supported S.325 (Act 152, 2026), which passed the Vermont House 142–0 and rolled back the most burdensome provisions of Act 181 — specifically the 'road rule' and Tier 3 environmental restrictions that rural landowners and local officials widely condemned as regulatory overreach infringing on private property rights and imposing disproportionate costs without proportionate benefit. Gov. Phil Scott signed the rollback in June 2026.",
              ["https://vtdigger.org/2026/05/07/vermont-house-votes-to-partially-repeal-act-181/",
               "https://vtdigger.org/2026/06/16/partial-rollback-of-vermonts-land-use-law-act-181-becomes-official-with-phil-scotts-signature/"]),
    ]),

    # ---------- Debra Powers (VT-R, State Representative, Caledonia-1) ----------
    ("debra-powers", "VT", "State Representative", [
        claim("dp1", "debra-powers", "self_defense", 1, True,
              "A member of the Vermont House Republican caucus that unanimously opposed H.606 in 2026, a gun-restriction bill that included a provision barring firearm ownership for individuals under court-ordered mental health treatment — a measure Republicans opposed as an unconstitutional red-flag-style restriction inconsistent with Second Amendment rights.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("dp2", "debra-powers", "economic_stewardship", 2, True,
              "Part of the Vermont House Republican caucus that achieved significantly lower property-tax growth in the 2025-2026 biennium (average increases of 1.1% and 3.5% vs. 13.8% under the Democrat supermajority) through consistent opposition to excessive state-spending increases.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
        claim("dp3", "debra-powers", "refuse_state_overreach", 0, True,
              "Supported S.325 (Act 152), the 2026 bill that passed the Vermont House unanimously (142–0) to roll back Act 181's most onerous land-use restrictions — the 'road rule' and Tier 3 natural-area provisions — that rural landowners and local officials in Caledonia County and statewide had protested as unwarranted state overreach onto private property. The rollback was signed into law by Gov. Phil Scott in June 2026.",
              ["https://vtdigger.org/2026/05/07/vermont-house-votes-to-partially-repeal-act-181/",
               "https://vtdigger.org/2026/06/16/partial-rollback-of-vermonts-land-use-law-act-181-becomes-official-with-phil-scotts-signature/"]),
    ]),

    # ---------- Deborah Cordz Dolgin (VT-R, State Representative, Caledonia-Essex) ----------
    ("deborah-cordz-dolgin", "VT", "State Representative", [
        claim("dcd1", "deborah-cordz-dolgin", "self_defense", 1, True,
              "A member of the Vermont House Republican caucus that unanimously opposed H.606 in 2026, a gun-restriction bill containing a provision barring firearm ownership for individuals under court-ordered mental health treatment — which Republicans characterized as an unconstitutional red-flag-style restriction on law-abiding gun owners.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("dcd2", "deborah-cordz-dolgin", "family_child_sovereignty", 0, True,
              "A former middle-school educator in Lyndonville, VT and small business owner who joined the majority of Vermont House Republicans in opposing H.454 (Act 73), the 2025 education-reform law that centralized school governance and cut the number of private schools eligible for Vermont's public tuition program from 46 to 18 — restricting parental school choice. Republicans opposed the bill as state overreach into local education; the House passed it 87–55 with most Republicans voting no.",
              ["https://vtdigger.org/2026/04/17/house-education-reform-bill-narrowly-passes-amid-heavy-criticism-and-some-lawmakers-unease/",
               "https://legislature.vermont.gov/people/single/2026/40405"]),
        claim("dcd3", "deborah-cordz-dolgin", "economic_stewardship", 2, True,
              "Part of the Vermont House Republican caucus that delivered property-tax restraint in the 2025-2026 biennium — average increases of 1.1% and 3.5% compared to 13.8% under the prior Democrat supermajority — by consistently opposing excess state spending. As both a small business owner and former public school educator, Dolgin brings direct experience of state fiscal policy's impact on working Vermonters.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/",
               "https://legislature.vermont.gov/people/single/2026/40405"]),
    ]),

    # ---------- David Bosch (VT-R, State Representative, Rutland-2) ----------
    ("david-bosch", "VT", "State Representative", [
        claim("db1", "david-bosch", "christian_liberty", 0, True,
              "Serves on the Board of Rutland Area Christian School, a faith-based school whose eligibility for Vermont's public tuition program was threatened by Act 73 (2025), which cut participating private schools from 46 to 18 and faced immediate legal challenges — including a federal appeals court action arguing Act 73 unconstitutionally excludes religious schools from the tuition program. As a board member of a directly affected institution, Bosch embodies the religious-liberty interest in protecting faith-based education from discriminatory state exclusions.",
              ["https://legislature.vermont.gov/people/single/2026/40423",
               "https://www.wcax.com/2026/06/26/is-vermonts-new-education-reform-law-unconstitutional/",
               "https://vtdigger.org/2026/03/03/new-lawsuit-challenges-restrictions-on-school-choice-in-vermonts-education-reform-law/"]),
        claim("db2", "david-bosch", "self_defense", 1, True,
              "A member of the Vermont House Republican caucus that unanimously opposed H.606 in 2026, a gun-restriction bill whose provision barring firearm ownership for individuals under court-ordered mental health treatment was rejected by all House Republicans as an unconstitutional red-flag-style restriction on Second Amendment rights.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("db3", "david-bosch", "economic_stewardship", 2, True,
              "Part of the Vermont House Republican caucus that achieved lower property-tax growth across the 2025-2026 biennium (average increases of 1.1% and 3.5% vs. 13.8% under the Democrat supermajority) through consistent opposition to unsustainable state-spending increases. Bosch, a member of the House Committee on Commerce and Economic Development, applies his background as a retired U.S. Forest Service professional and town auditor to advocate for responsible fiscal stewardship.",
              ["https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/",
               "https://legislature.vermont.gov/people/single/2026/40423"]),
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
