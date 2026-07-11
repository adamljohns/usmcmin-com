#!/usr/bin/env python3
"""Enrichment batch 647: hand-curated claims for 2 Mississippi State Senators.

Senators: Michael McLendon (SD-1), Kathy Chism (SD-3).
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
    # --- Michael McLendon (MS SD-1, State Senator — DeSoto County/NW MS, in office since Jan 2020) ---
    ("michael-mclendon", "MS", "State Senator", [
        claim("mm1", "michael-mclendon", "family_child_sovereignty", 0, True,
              "McLendon authored and floor-managed SB 2113 (2022), barring Mississippi K-12 schools, community colleges, and universities from requiring students to personally affirm that any race, sex, or ethnicity is inherently superior or inferior and prohibiting schools from making adverse racial classifications of students — with state funding loss as the enforcement mechanism; the Senate passed it 32-2 on January 21, 2022, and Gov. Reeves signed it March 14, 2022.",
              ["https://thegrio.com/2022/01/21/mississippi-senate-passes-ban-on-crt/",
               "https://www.cnn.com/2022/03/14/politics/mississippi-critical-race-theory-law/index.html"]),
        claim("mm2", "michael-mclendon", "biblical_marriage", 2, True,
              "McLendon was a named co-sponsor of SB 2536 (2021), the Mississippi Fairness Act, requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting biological males from competing on female teams; the co-sponsorship is confirmed in the enrolled bill text; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021, making Mississippi the first state in the nation to enact such a law.",
              ["https://legiscan.com/MS/text/SB2536/id/2271648",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("mm3", "michael-mclendon", "family_child_sovereignty", 0, True,
              "McLendon is individually named in the official Senate roll call (vote record 0500004) as voting Yea on HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 along party lines on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/votes/senate/0500004.pdf",
               "https://www.pbs.org/newshour/politics/mississippi-senate-passes-limit-on-gender-affirming-health-care"]),
    ]),

    # --- Kathy Chism (MS SD-3, State Senator — Benton/Pontotoc/Union counties, in office since Jan 2020) ---
    ("kathy-chism", "MS", "State Senator", [
        claim("kc1", "kathy-chism", "biblical_marriage", 2, True,
              "Chism was a named co-sponsor of SB 2536 (2021), the Mississippi Fairness Act, requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting biological males from competing on female teams; Chism's co-sponsorship is confirmed in the enrolled bill text; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021.",
              ["https://legiscan.com/MS/text/SB2536/id/2271648",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("kc2", "kathy-chism", "family_child_sovereignty", 0, True,
              "Chism is individually named in the official Senate roll call (vote record 0500004) as voting Yea on HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 along party lines on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/votes/senate/0500004.pdf",
               "https://southernequality.org/mississippi-senate-sends-bill-restricting-healthcare-for-transgender-youth-to-governor/"]),
        claim("kc3", "kathy-chism", "family_child_sovereignty", 0, True,
              "Chism was a named co-sponsor of SB 2113 (2022), authored by Sen. McLendon, prohibiting Mississippi public schools, community colleges, and universities from mandating adherence to any doctrine asserting that any race, sex, or ethnicity is inherently superior or inferior and barring adverse racial classifications of students — with state funding loss as the enforcement mechanism; the Senate passed it 32-2 on January 21, 2022, and Gov. Reeves signed it March 14, 2022.",
              ["https://legiscan.com/MS/text/SB2113/id/2546132",
               "https://thegrio.com/2022/01/21/mississippi-senate-passes-ban-on-crt/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
