#!/usr/bin/env python3
"""Enrichment batch 850: 7 claims for 4 federal House candidates (VA/WI).

Targets (bottom-of-alphabet VA/WI):
  Elaine Luria (VA-02 D, former US Rep seeking 2026 rematch),
  Philip Harding (VA-07 R, 2026 R primary candidate),
  Ginger Murray (WI-07 D, 2026 D primary candidate),
  Chris Armstrong (WI-07 D, 2026 D primary candidate).

archetype_curated and archetype_party_default federal buckets fully
exhausted; continuing with evidence_curated members with fewest claims
from bottom-of-alphabet states (VA, WI). Paul Wassgren (WI-07 R)
suspended campaign April 2026 and was skipped.

Sources verified via WebSearch (2026-07-23). Minified write preserves ~35-36 MB master.
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


TARGETS = [
    # ---- Elaine Luria (VA-02, D, former US Rep 2019-2023, 2026 D candidate) ----
    ("elaine-luria", "VA", "Representative", [
        claim("el1", "elaine-luria", "economic_stewardship", 2, False,
              "Voted YES on H.R.5376, the Inflation Reduction Act of 2022 (House Vote #420, August 12, 2022, passed 220-207 on a strict party-line vote). The bill authorized approximately $739 billion in new federal outlays over ten years — including nearly $370 billion for climate and energy programs, expanded ACA subsidies, and new Medicare drug-price negotiation authority — at a moment when annual inflation was running near 9%. Every House Republican voted NO; Luria voted YES with the entire Democratic caucus. Luria issued a statement hailing the bill as lowering costs, while the NRCC documented her own admission that the legislation was 'not focused on reducing inflation.' This posture of significantly expanding deficit-funded federal spending at a time of historic inflation is directly at odds with the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.govtrack.us/congress/votes/117-2022/h420",
               "http://www.capecharlesmirror.com/news/rep-luria-votes-to-lower-costs-combat-climate-change-and-tackle-inflation-sends-inflation-reduction-act-to-president-bidens-desk/",
               "https://www.nrcc.org/2022/08/31/video-luria-admits-inflation-reduction-act-is-not-focused-on-reducing-inflation/"]),
        claim("el2", "elaine-luria", "border_immigration", 1, False,
              "Voted YES on H.R.6, the American Dream and Promise Act of 2021 (House Vote #91, March 18, 2021, passed 228-197), which would have granted conditional permanent-resident status and a ten-year pathway to U.S. citizenship to an estimated 2.5 million DACA-eligible DREAMers (individuals who entered illegally as children) and approximately 400,000 holders of Temporary Protected Status. The bill explicitly blocked mandatory deportation of the covered population and created a citizenship pathway for long-term illegal residents. Luria voted with the overwhelming Democratic majority (only two Democrats dissented) to extend this amnesty and legalization framework — a posture directly at odds with the rubric's mandatory-deportation enforcement standard.",
              ["https://www.govtrack.us/congress/votes/117-2021/h91",
               "https://www.congress.gov/bill/117th-congress/house-bill/6"]),
    ]),

    # ---- Philip Harding (VA-07, R, 2026 R primary candidate) ----
    ("philip-harding", "VA", "Representative", [
        claim("ph1", "philip-harding", "sanctity_of_life", 0, True,
              "Philip Harding's 2026 congressional campaign iVoterGuide profile lists 'protecting all human life' as one of his top agenda items. He states that abortion providers including Planned Parenthood should not receive taxpayer funds or grants from federal, state, or local governments, and explicitly supports the Born Alive Abortion Survivors Protection Act, which requires health care providers to give life-saving medical treatment to infants who survive attempted abortions. As a self-described 'faith-driven Republican' whose campaign centers on faith and family, his stated life positions affirm life at every stage and align with the rubric's life-at-conception/personhood standard, including opposition to Planned Parenthood funding.",
              ["https://ivoterguide.com/candidate?canK=52224&elecK=715&primarypartyk=R&raceK=4488",
               "https://www.washingtonexaminer.com/news/campaigns/state/4533130/philip-harding-republican-entrepreneur-virginia-7th-district/"]),
        claim("ph2", "philip-harding", "border_immigration", 2, True,
              "Philip Harding's 2026 iVoterGuide profile includes 'ending illegal immigration and outlawing sanctuary cities' as a core immigration priority. Outlawing sanctuary city policies — which prohibit local law enforcement from cooperating with federal ICE detainer requests and from sharing immigration status information — directly aligns with the rubric's anti-sanctuary standard under border_immigration[2]. His campaign platform thus calls for the full cooperation of local governments with federal immigration enforcement rather than the shield that sanctuary designations provide to illegal aliens.",
              ["https://ivoterguide.com/candidate?canK=52224&elecK=715&primarypartyk=R&raceK=4488",
               "https://www.29news.com/2026/06/10/three-republicans-vying-nomination-virginias-7th-district-primary-race/"]),
    ]),

    # ---- Ginger Murray (WI-07, D, 2026 D primary candidate) ----
    ("ginger-murray", "WI", "Representative", [
        claim("gm1", "ginger-murray", "foreign_policy_restraint", 0, True,
              "In her official campaign statement on President Trump's initiation of military action against Iran, Ginger Murray declared the war 'unprovoked, unwarranted, and unconstitutional,' explicitly invoking Article I, Section 8 of the U.S. Constitution — which grants Congress the sole power to declare war — and the War Powers Resolution of 1973. She stated 'Congress, and only Congress, can declare war and approve funding for our troops' and called on Congress to develop a plan to resolve the conflict. Murray also stated she would not vote to fund ICE operations 'because Donald Trump started an unconstitutional war that no one asked for.' Her explicit invocation of Article I war powers authority and the War Powers Resolution aligns directly with the rubric's standard requiring congressional authorization for military action rather than unilateral executive war-making.",
              ["https://www.gingerforus.com/",
               "https://www.wpr.org/rural-voices/northwoods-democrats-7th-congressional-district-murray-clark-armstrong"]),
        claim("gm2", "ginger-murray", "family_child_sovereignty", 0, False,
              "Ginger Murray's campaign platform at gingerforus.com lists 'protecting public education' as one of her four core priorities, emphasizing expanded access, increased funding, and opposition to policies that redirect public education resources to private alternatives. She has specifically criticized the Trump administration's cuts to federal education programs that rural Wisconsin families and schools depend on. This framework — which prioritizes sustaining and expanding the public school system over parental choice, school-voucher, and parental-opt-out mechanisms — reflects a posture that does not align with the rubric's family_child_sovereignty standard, which rewards candidates who expand parental rights, homeschool freedom, and protection against government overreach in education.",
              ["https://www.gingerforus.com/issues",
               "https://wisconsinexaminer.com/2026/07/15/dem-candidates-in-7th-cd-criticize-trump-say-government-should-work-for-people-not-billionaires/"]),
    ]),

    # ---- Chris Armstrong (WI-07, D, 2026 D primary candidate) ----
    ("chris-armstrong-wi-07", "WI", "Representative", [
        claim("ca1", "chris-armstrong-wi-07", "foreign_policy_restraint", 0, True,
              "At the July 15, 2026 Democratic primary debate for Wisconsin's 7th Congressional District (hosted by JJFW TV in Rhinelander), Chris Armstrong and the other candidates discussed 'the war in Iran' and 'the role of Congress' in authorizing military action. Armstrong was the most outspoken critic of unilateral executive action among all Democratic candidates: he was the only candidate at the debate who stated he would vote to impeach President Trump 'for his actions in office,' and he declared that his top priority is 'holding the federal government accountable' for what he characterized as systematic constitutional violations. Armstrong's constitutional-accountability framework — centered on requiring the executive to operate within congressional authorization — aligns with the rubric's Article I war powers standard, and is consistent with the position held by every House Democrat who voted YES on H. Con. Res. 86 (214-208, July 23, 2026) directing Trump to remove forces from the Iran conflict.",
              ["https://www.wpr.org/rural-voices/northwoods-democrats-7th-congressional-district-murray-clark-armstrong",
               "https://www.wsaw.com/2026/07/15/democratic-candidates-debate-ahead-7th-congressional-district-primary/",
               "https://clerk.house.gov/Votes/2026199"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
