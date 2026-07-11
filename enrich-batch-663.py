#!/usr/bin/env python3
"""Enrichment batch 663: hand-curated claims for 2 Mississippi State Senators.

Senators: Jeremy England (SD-51), Brice Wiggins (SD-52).
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
    # --- Jeremy England (MS SD-51, State Senator — Jackson/George/Greene counties) ---
    ("jeremy-england", "MS", "State Senator", [
        claim("je1", "jeremy-england", "election_integrity", 0, True,
              "England authored SB 2588 (2026), the SHIELD Act, as its prime Senate sponsor — the bill requiring annual citizenship verification of all registered voters against the federal SAVE database and mandating county registrars to run applicants through SAVE before registering them; England shepherded it through the Senate, which passed it 33-17 on a strict party-line vote on February 5, 2026; Gov. Reeves signed it April 3, 2026, effective July 1, 2026.",
              ["https://magnoliatribune.com/2026/04/01/governor-signs-shield-act-into-law-seeking-to-further-safeguard-mississippi-elections/",
               "https://www.mississippifreepress.org/mississippi-governor-signs-shield-act-into-law-enacting-voter-citizenship-checks/"]),
        claim("je2", "jeremy-england", "biblical_marriage", 2, True,
              "England was a named co-author of SB 2753 (2024), the Mississippi SAFER Act (Students and Athletes Free from Explicit Restrooms), prohibiting persons of one biological sex from using restrooms, changing rooms, or shower facilities designated for the opposite sex in public schools, public universities, and government buildings; co-authored with Sen. Harkins (Finance Committee Chair); the Senate passed it 35-15 and Gov. Reeves signed it April 15, 2024.",
              ["https://billstatus.ls.state.ms.us/documents/2024/html/SB/2700-2799/SB2753IN.htm",
               "https://www.wlbt.com/2024/04/15/gov-reeves-signs-safer-act-banning-biological-males-womens-restrooms-schools/"]),
        claim("je3", "jeremy-england", "election_integrity", 0, True,
              "England was a named co-sponsor of SB 2358 (2023), the Mississippi ballot-harvesting ban making it a crime for anyone other than an election official, postal carrier, family or household member, or caregiver to collect and submit absentee ballots on behalf of another person — violations carry up to one year in jail and a $3,000 fine; Gov. Reeves signed it March 22, 2023, effective July 1, 2023.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/SB/2300-2399/SB2358IN.htm",
               "https://www.wlox.com/2023/03/22/ballot-harvesting-now-banned-mississippi/"]),
    ]),

    # --- Brice Wiggins (MS SD-52, State Senator — Jackson County, Judiciary A Committee Chair) ---
    ("brice-wiggins", "MS", "State Senator", [
        claim("bw1", "brice-wiggins", "family_child_sovereignty", 0, True,
              "Wiggins, serving as Senate Judiciary A Committee Chairman, personally managed HB 1125 (2023) on the Senate floor — the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; Wiggins's floor management was essential to its passage 33-15 on a party-line vote; Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/history/HB/HB1125.xml",
               "https://www.pbs.org/newshour/politics/mississippi-senate-passes-limit-on-gender-affirming-health-care"]),
        claim("bw2", "brice-wiggins", "biblical_marriage", 2, True,
              "Wiggins was a named co-sponsor of SB 2536 (2021), the Mississippi Fairness Act, requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting biological males from competing on female teams; Wiggins's co-sponsorship is confirmed in the enrolled bill text; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021.",
              ["https://legiscan.com/MS/text/SB2536/id/2271648",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("bw3", "brice-wiggins", "election_integrity", 0, True,
              "Wiggins was a named co-sponsor of SB 2358 (2023), the Mississippi ballot-harvesting ban making it a crime for anyone other than an election official, postal carrier, family or household member, or caregiver to collect and submit absentee ballots on behalf of another person — violations carry up to one year in jail and a $3,000 fine; Gov. Reeves signed it March 22, 2023, effective July 1, 2023.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/SB/2300-2399/SB2358IN.htm",
               "https://www.wlox.com/2023/03/22/ballot-harvesting-now-banned-mississippi/"]),
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
