#!/usr/bin/env python3
"""Enrichment batch 649: hand-curated claims for 2 Mississippi State Senators.

Senators: Chad McMahan (SD-6), Benjamin Suber (SD-8).
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
    # --- Chad McMahan (MS SD-6, State Senator — Lee/Itawamba counties, in office since Jan 2016) ---
    ("chad-mcmahan", "MS", "State Senator", [
        claim("cm1", "chad-mcmahan", "biblical_marriage", 2, True,
              "McMahan was a named co-author of SB 2536 (2021), the Mississippi Fairness Act, requiring public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting males from competing on female teams regardless of gender identity; the Senate passed it 34-9 on February 12, 2021, and Gov. Reeves signed it effective July 1, 2021, making Mississippi the first state in the nation to enact such a law.",
              ["https://billstatus.ls.state.ms.us/documents/2021/html/SB/2500-2599/SB2536IN.htm",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("cm2", "chad-mcmahan", "election_integrity", 0, True,
              "McMahan was a named co-sponsor of SB 2358 (2023), the ballot-harvesting ban making it a crime for anyone other than an election official, postal carrier, family or household member, or caregiver to collect and submit mail-in or absentee ballots on behalf of another person — violations carry up to one year in jail and a $3,000 fine; Gov. Reeves signed it March 22, 2023, effective July 1, 2023.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/SB/2300-2399/SB2358IN.htm",
               "https://www.wlox.com/2023/03/22/ballot-harvesting-now-banned-mississippi/"]),
        claim("cm3", "chad-mcmahan", "family_child_sovereignty", 0, True,
              "McMahan was a named co-sponsor of SB 2113 (2022), the Education Content Restriction Act, prohibiting all Mississippi public schools, community colleges, and universities from directing or compelling students to personally affirm that any sex, race, ethnicity, religion, or national origin is inherently superior or inferior, and from making adverse distinctions among students based on race; schools that violate the act face loss of state funding; Gov. Reeves signed it into law in March 2022.",
              ["https://billstatus.ls.state.ms.us/documents/2022/html/SB/2100-2199/SB2113IN.htm",
               "https://mississippitoday.org/2022/03/15/anti-crt-bill-signed-into-law/"]),
    ]),

    # --- Benjamin Suber (MS SD-8, State Senator — Calhoun/Chickasaw/Lafayette/Pontotoc/Yalobusha counties, in office since Jan 2020) ---
    ("benjamin-suber", "MS", "State Senator", [
        claim("bs1", "benjamin-suber", "biblical_marriage", 2, True,
              "Suber was a named co-author of SB 2536 (2021), the Mississippi Fairness Act, requiring public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting males from competing on female teams regardless of gender identity — co-authoring in his second year in office; the Senate passed it 34-9 on February 12, 2021, and Gov. Reeves signed it effective July 1, 2021, making Mississippi the first state in the nation to enact such a law.",
              ["https://billstatus.ls.state.ms.us/documents/2021/html/SB/2500-2599/SB2536IN.htm",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("bs2", "benjamin-suber", "election_integrity", 0, True,
              "Suber was a named co-sponsor of SB 2358 (2023), the ballot-harvesting ban making it a crime for anyone other than an election official, postal carrier, family or household member, or caregiver to collect and submit absentee ballots on behalf of another person — violations carry up to one year in county jail and a $3,000 fine; Gov. Reeves signed it March 22, 2023, effective July 1, 2023.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/SB/2300-2399/SB2358IN.htm",
               "https://trackbill.com/bill/mississippi-senate-bill-2358-ballot-harvesting-ban/2314450/"]),
        claim("bs3", "benjamin-suber", "family_child_sovereignty", 0, True,
              "Suber was a named co-sponsor of SB 2113 (2022), the Education Content Restriction Act, prohibiting all Mississippi public schools, community colleges, and universities from compelling students to personally affirm that any race, sex, religion, ethnicity, or national origin is inherently superior or inferior, and from making adverse distinctions among students based on race; schools that violate the act face loss of state funding; Gov. Reeves signed it into law in March 2022.",
              ["https://billstatus.ls.state.ms.us/documents/2022/html/SB/2100-2199/SB2113IN.htm",
               "https://mississippitoday.org/2022/03/15/anti-crt-bill-signed-into-law/"]),
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
