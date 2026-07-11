#!/usr/bin/env python3
"""Enrichment batch 659: hand-curated claims for 2 Mississippi State Senators.

Senators: Don Hartness (SD-42), Dennis DeBar (SD-43).
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
    # --- Don Hartness (MS SD-42, State Senator — Jones County, in office since Jan 2026) ---
    ("don-hartness", "MS", "State Senator", [
        claim("dh1", "don-hartness", "family_child_sovereignty", 0, True,
              "Hartness voted for HB 1662 (2026), the 50/50 Joint Custody Act, establishing a rebuttable presumption in favor of equal (50/50) custody arrangements in Mississippi divorce and child custody proceedings — a landmark parental rights bill; news coverage confirmed the Senate passed it and Gov. Reeves signed it in 2026, with Hartness voting yes in his first legislative session.",
              ["https://magnoliatribune.com/2026/03/mississippi-joint-custody-act/",
               "https://www.wlbt.com/2026/mississippi-50-50-custody-law/"]),
        claim("dh2", "don-hartness", "election_integrity", 0, True,
              "Hartness voted with the Republican caucus for SB 2588 (2026), the SHIELD Act, which requires annual citizenship verification of all registered voters against the federal SAVE database and mandates county registrars to run applicants through SAVE before registering them; the Senate passed it 33-17 on a strict party-line vote on February 5, 2026, and Gov. Reeves signed it April 3, 2026, effective July 1, 2026.",
              ["https://magnoliatribune.com/2026/04/01/governor-signs-shield-act-into-law-seeking-to-further-safeguard-mississippi-elections/",
               "https://www.mississippifreepress.org/mississippi-governor-signs-shield-act-into-law-enacting-voter-citizenship-checks/"]),
        claim("dh3", "don-hartness", "sanctity_of_life", 0, True,
              "Hartness voted with the Republican caucus for HB 1613 (2026), which amends Mississippi drug trafficking law to classify distribution of abortion-inducing drugs — including mifepristone and misoprostol — as a felony carrying up to 10 years in prison; the House passed it 77-39 and the Senate 37-15; Gov. Reeves signed it April 8, 2026 — Hartness's first session in office.",
              ["https://mississippitoday.org/2026/04/01/mississippi-abortion-medication/",
               "https://www.mississippifreepress.org/bill-criminalizing-mail-order-abortion-pills-as-drug-trafficking-heads-to-mississippi-governors-desk/"]),
    ]),

    # --- Dennis DeBar (MS SD-43, State Senator — Marion/Lamar/Pearl River counties, in office since Jan 2016) ---
    ("dennis-debar", "MS", "State Senator", [
        claim("dd1", "dennis-debar", "family_child_sovereignty", 0, True,
              "DeBar voted with the Republican caucus for HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 on a strict party-line vote on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/history/HB/HB1125.xml",
               "https://magnoliatribune.com/2023/02/23/mississippi-legislature-sends-bill-preventing-gender-reassignment-for-minors-to-governor/"]),
        claim("dd2", "dennis-debar", "biblical_marriage", 2, True,
              "DeBar voted with the Republican caucus for SB 2536 (2021), the Mississippi Fairness Act, requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting biological males from competing on female teams; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021.",
              ["https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/",
               "https://billstatus.ls.state.ms.us/documents/2021/html/SB/2500-2599/SB2536SG.htm"]),
        claim("dd3", "dennis-debar", "election_integrity", 0, True,
              "DeBar was a named co-sponsor of SB 2358 (2023), the Mississippi ballot-harvesting ban making it a crime for anyone other than an election official, postal carrier, family or household member, or caregiver to collect and submit absentee ballots on behalf of another person — violations carry up to one year in jail and a $3,000 fine; Gov. Reeves signed it March 22, 2023, effective July 1, 2023.",
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
