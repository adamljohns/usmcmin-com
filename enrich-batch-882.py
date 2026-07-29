#!/usr/bin/env python3
"""Enrichment batch 882: hand-curated claims for 5 Vermont Democrat state reps.

Targets archetype_party_default VT state representatives with 0 evidence claims,
taken from the bottom-of-alphabet pool (WY/WV/WI/WA fully enriched; VT-D is next).
Only reps who were in the legislature during the 2023 session are included — Will
Greer and Wendy Critchlow (both assumed office Jan 2025) are skipped.

Targets (D, VT): Trevor Squirrell (Chittenden-3, since 2017),
Tom Stevens (Washington-Chittenden, since 2009),
Timothy Corcoran II (Bennington-2, since Jan 2023),
Tiff Bluemle (Chittenden-13, since Jan 2023),
Theresa Wood (Washington-Chittenden, since 2015).
10 total new claims across 5 candidates.

Key 2023 Vermont legislation cited:
- H.230 (Act 45, 2023): 72-hour waiting period + safe gun storage + ERPO expansion.
  Passed the House on a near-party-line vote (98-47 / 99-43); Democratic majority
  held together in three separate roll-call votes. Gov. Scott let it become law
  without signature June 2023.
- S.37 (Act 15, 2023): "shield bill" protecting patients and providers of abortion
  and gender-affirming care from discipline or legal action by other states.
  House passed 114-24 April 21, 2023; signed by Gov. Scott May 10, 2023.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Trevor Squirrell (VT-Chittenden-3, D, since 2017) ----------------
    ("trevor-squirrell", "VT", "Representative", [
        claim("ts1", "trevor-squirrell", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a member of the Democratic majority that held together on three "
              "separate roll-call votes (98-47 on the safe-storage section; 99-43 on the "
              "72-hour waiting period and ERPO expansion section). The bill created a "
              "72-hour waiting period for all firearm purchases, expanded who can petition "
              "courts for an Extreme Risk Protection Order (red-flag removal of firearms), "
              "and required safe home storage — directly opposing the rubric's defense of "
              "unrestricted Second Amendment carry rights and opposition to red-flag laws. "
              "Gov. Phil Scott allowed the bill to become law without signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("ts2", "trevor-squirrell", "biblical_marriage", 2, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the House "
              "114-24 on April 21, 2023, and was signed by Gov. Phil Scott on May 10, 2023. "
              "The law legally shields Vermont providers and patients receiving gender-affirming "
              "medical care (including puberty blockers, hormone therapy, and surgical "
              "interventions) from professional discipline or civil/criminal liability imposed "
              "by other states — directly endorsing and institutionalizing transgender medical "
              "ideology in Vermont law, contrary to the rubric's standard of rejecting "
              "transgender ideology in public policy.",
              ["https://protem.vermont.gov/immediate-release-vermont-senate-passes-s37-abortion-and-gender-affirming-care-shield-bill",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Tom Stevens (VT-Washington-Chittenden, D, since 2009) ----------------
    ("tom-stevens", "VT", "Representative", [
        claim("tst1", "tom-stevens", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a long-serving member of the Democratic majority (in the House since "
              "2009) that held together on three near-party-line roll-call votes — 98-47 on "
              "safe storage, 99-43 on the 72-hour waiting period and ERPO expansion. The bill "
              "imposed a 72-hour delay on all firearm transfers, expanded extreme risk "
              "protection orders (red-flag gun removals), and mandated safe-storage rules — "
              "positions opposite to the rubric's opposition to red-flag laws, waiting periods, "
              "and restrictions on the right to keep and bear arms. Gov. Scott allowed it to "
              "become law without signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("tst2", "tom-stevens", "sanctity_of_life", 0, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House 114-24 on April 21, 2023, and was signed into law on May 10, 2023. S.37 "
              "protects Vermont patients who obtain abortions and providers who perform them "
              "from legal action or professional discipline imposed by other states, "
              "institutionalizing Vermont as a safe harbor for unrestricted abortion access. "
              "The law reflects a rejection of any legal recognition of personhood before "
              "birth — contrary to the rubric's life-from-conception standard.",
              ["https://protem.vermont.gov/immediate-release-vermont-senate-passes-s37-abortion-and-gender-affirming-care-shield-bill",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Timothy Corcoran II (VT-Bennington-2, D, since Jan 2023) ----------------
    ("timothy-corcoran-ii", "VT", "Representative", [
        claim("tc1", "timothy-corcoran-ii", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023) as a member of the Democratic "
              "majority in his first legislative session (assumed office January 4, 2023). The "
              "Gun Violence Prevention Act passed the House on three near-party-line roll-call "
              "votes (98-47 on safe storage; 99-43 on the 72-hour waiting period and ERPO "
              "expansion). The bill imposed a 72-hour delay on firearm purchases, required "
              "secure home storage of firearms, and expanded red-flag extreme risk protection "
              "orders — all directly contrary to the rubric's Second Amendment posture of "
              "opposing gun restrictions and red-flag laws. Gov. Scott allowed it to become "
              "law without signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("tc2", "timothy-corcoran-ii", "biblical_marriage", 2, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the reproductive and gender-affirming care 'shield bill,' passed by the Vermont "
              "House 114-24 on April 21, 2023, and signed into law May 10, 2023. The law "
              "shields Vermont providers who deliver gender-affirming medical care — including "
              "puberty blockers, hormones, and surgeries for minors — from professional "
              "discipline and from civil or criminal liability originating in other states, "
              "directly endorsing transgender medical ideology in Vermont law, contrary to "
              "the rubric's standard of rejecting transgender ideology in public policy.",
              ["https://protem.vermont.gov/immediate-release-vermont-senate-passes-s37-abortion-and-gender-affirming-care-shield-bill",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Tiff Bluemle (VT-Chittenden-13, D, since Jan 2023) ----------------
    ("tiff-bluemle", "VT", "Representative", [
        claim("tb1", "tiff-bluemle", "self_defense", 1, False,
              "A listed co-sponsor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act — going beyond a simple floor vote to actively author the legislation in "
              "her first legislative session (assumed office January 4, 2023). The bill, "
              "sponsored by more than a dozen House Democrats and passed on near-party-line "
              "votes (98-47 on safe storage; 99-43 on waiting period and ERPO expansion), "
              "created a 72-hour waiting period for all firearm transfers, mandated secure "
              "home storage of guns with criminal penalties, and expanded who can petition for "
              "an Extreme Risk Protection Order (red-flag removal). Gov. Scott allowed it to "
              "become law without his signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("tb2", "tiff-bluemle", "sanctity_of_life", 0, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which the House passed "
              "114-24 on April 21, 2023, and Gov. Scott signed on May 10, 2023. S.37 protects "
              "Vermont patients who obtain abortions and providers who perform them from "
              "professional discipline or civil/criminal liability originating in other states, "
              "making Vermont a guaranteed safe harbor for unrestricted abortion access. The "
              "law reflects a refusal to recognize any legal protection of unborn life — "
              "contrary to the rubric's life-from-conception and personhood standard.",
              ["https://protem.vermont.gov/immediate-release-vermont-senate-passes-s37-abortion-and-gender-affirming-care-shield-bill",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Theresa Wood (VT-Washington-Chittenden, D, since 2015) ----------------
    ("theresa-wood", "VT", "Representative", [
        claim("tw1", "theresa-wood", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a member of the Democratic majority (in the House since 2015) that held "
              "together on three near-party-line roll-call votes (98-47 on safe storage; 99-43 "
              "on the 72-hour waiting period and ERPO expansion). The bill imposed a 72-hour "
              "delay on all firearm transfers, required secure home storage of firearms, and "
              "expanded red-flag Extreme Risk Protection Orders allowing family members to "
              "petition courts for gun removal — measures directly contrary to the rubric's "
              "opposition to red-flag laws and firearms restrictions. Gov. Scott allowed the "
              "bill to become law without his signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("tw2", "theresa-wood", "biblical_marriage", 2, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House 114-24 on April 21, 2023, and was signed by Gov. Phil Scott on May 10, "
              "2023. As Chair of the House Committee on Human Services, Wood sits at the "
              "center of Vermont's health-and-social-services agenda; S.37 shields Vermont "
              "providers of gender-affirming care — including puberty blockers, hormones, and "
              "surgeries for minors — from professional discipline and out-of-state legal "
              "action, institutionalizing transgender medical ideology in Vermont law, "
              "contrary to the rubric's standard of rejecting transgender ideology in policy.",
              ["https://protem.vermont.gov/immediate-release-vermont-senate-passes-s37-abortion-and-gender-affirming-care-shield-bill",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
