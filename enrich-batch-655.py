#!/usr/bin/env python3
"""Enrichment batch 655: hand-curated claims for 2 Mississippi State Senators.

Senators: Dean Kirby (SD-30), Tyler McCaughn (SD-31).
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
    # --- Dean Kirby (MS SD-30, State Senator — Rankin/Scott counties, Senate President Pro Tempore) ---
    ("dean-kirby", "MS", "State Senator", [
        claim("dk1", "dean-kirby", "family_child_sovereignty", 0, True,
              "Kirby, serving as Senate President Pro Tempore, voted for HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 on a strict party-line vote on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/votes/senate/0500004.pdf",
               "https://www.pbs.org/newshour/politics/mississippi-senate-passes-limit-on-gender-affirming-health-care"]),
        claim("dk2", "dean-kirby", "election_integrity", 0, True,
              "Kirby has a long record supporting voter identification requirements; VoteSmart records confirm Kirby supported voter ID legislation going back to 2008, and Mississippi voters passed Initiative 27 in 2012 — the constitutional voter ID amendment — with Kirby as a consistent advocate for requiring photo identification at the polls to prevent fraud.",
              ["https://votesmart.org/candidate/key-votes/9248/dean-kirby",
               "https://ballotpedia.org/Mississippi_Voter_Identification_Amendment,_Initiative_27_(2011)"]),
    ]),

    # --- Tyler McCaughn (MS SD-31, State Senator — Rankin County) ---
    ("tyler-mccaughn", "MS", "State Senator", [
        claim("tm1", "tyler-mccaughn", "election_integrity", 0, True,
              "McCaughn was a named co-sponsor of SB 2358 (2023), the Mississippi ballot-harvesting ban making it a crime for anyone other than an election official, postal carrier, family or household member, or caregiver to collect and submit absentee ballots on behalf of another person — violations carry up to one year in jail and a $3,000 fine; Gov. Reeves signed it March 22, 2023, effective July 1, 2023.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/SB/2300-2399/SB2358IN.htm",
               "https://www.wlox.com/2023/03/22/ballot-harvesting-now-banned-mississippi/"]),
        claim("tm2", "tyler-mccaughn", "biblical_marriage", 2, True,
              "McCaughn was a named co-sponsor of SB 2536 (2021), the Mississippi Fairness Act, requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting biological males from competing on female teams; McCaughn's co-sponsorship is confirmed in the enrolled bill text; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021.",
              ["https://legiscan.com/MS/text/SB2536/id/2271648",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("tm3", "tyler-mccaughn", "family_child_sovereignty", 0, True,
              "McCaughn voted with the Republican caucus for HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 on a strict party-line vote on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/history/HB/HB1125.xml",
               "https://magnoliatribune.com/2023/02/23/mississippi-legislature-sends-bill-preventing-gender-reassignment-for-minors-to-governor/"]),
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
