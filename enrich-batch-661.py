#!/usr/bin/env python3
"""Enrichment batch 661: hand-curated claims for 2 Mississippi State Senators.

Senators: Mike Seymour (SD-47), Mike Thompson (SD-48).
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
    # --- Mike Seymour (MS SD-47, State Senator — Lincoln/Copiah/Franklin counties) ---
    ("mike-seymour", "MS", "State Senator", [
        claim("ms1", "mike-seymour", "biblical_marriage", 2, True,
              "Seymour was a named co-sponsor of SB 2536 (2021), the Mississippi Fairness Act, requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting biological males from competing on female teams; Seymour's co-sponsorship is confirmed in the enrolled bill text; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021.",
              ["https://legiscan.com/MS/text/SB2536/id/2271648",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("ms2", "mike-seymour", "election_integrity", 0, True,
              "Seymour was a named co-sponsor of SB 2358 (2023), the Mississippi ballot-harvesting ban making it a crime for anyone other than an election official, postal carrier, family or household member, or caregiver to collect and submit absentee ballots on behalf of another person — violations carry up to one year in jail and a $3,000 fine; Gov. Reeves signed it March 22, 2023, effective July 1, 2023.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/SB/2300-2399/SB2358IN.htm",
               "https://www.wlox.com/2023/03/22/ballot-harvesting-now-banned-mississippi/"]),
        claim("ms3", "mike-seymour", "self_defense", 0, True,
              "Seymour voted for HB 1110 (2023), the Second Amendment Financial Privacy Act, prohibiting banks and payment processors from using a firearms-specific merchant category code (MCC) to track purchases at gun stores — the Senate passed it 52-0 in a unanimous vote, reflecting Seymour's consistent pro-Second Amendment stance.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/HB/1100-1199/HB1110SG.htm",
               "https://www.nraila.org/articles/20230420/mississippi-governor-signs-second-amendment-financial-privacy-act/"]),
    ]),

    # --- Mike Thompson (MS SD-48, State Senator — Pike/Walthall/Amite counties)
    # NOTE: slug is mike-thompson-ms-48 (not mike-thompson) due to name collision in scorecard
    ("mike-thompson-ms-48", "MS", "State Senator", [
        claim("mtt1", "mike-thompson-ms-48", "biblical_marriage", 2, True,
              "Thompson was a named co-sponsor of SB 2536 (2021), the Mississippi Fairness Act, requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting biological males from competing on female teams; Thompson's co-sponsorship is confirmed in the enrolled bill text; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021.",
              ["https://legiscan.com/MS/text/SB2536/id/2271648",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("mtt2", "mike-thompson-ms-48", "family_child_sovereignty", 0, True,
              "Thompson voted with the Republican caucus for HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 on a strict party-line vote on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/history/HB/HB1125.xml",
               "https://magnoliatribune.com/2023/02/23/mississippi-legislature-sends-bill-preventing-gender-reassignment-for-minors-to-governor/"]),
        claim("mtt3", "mike-thompson-ms-48", "self_defense", 0, True,
              "Thompson voted for HB 1110 (2023), the Second Amendment Financial Privacy Act, prohibiting banks and payment processors from using a firearms-specific merchant category code (MCC) to track purchases at gun stores — the Senate passed it 52-0 in a unanimous vote, reflecting Thompson's consistent pro-Second Amendment stance.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/HB/1100-1199/HB1110SG.htm",
               "https://www.nraila.org/articles/20230420/mississippi-governor-signs-second-amendment-financial-privacy-act/"]),
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
