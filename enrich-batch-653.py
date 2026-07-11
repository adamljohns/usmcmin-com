#!/usr/bin/env python3
"""Enrichment batch 653: hand-curated claims for 2 Mississippi State Senators.

Senators: Kevin Blackwell (SD-16), Josh Harkins (SD-20).
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
    # --- Kevin Blackwell (MS SD-16, State Senator — Rankin County) ---
    ("kevin-blackwell", "MS", "State Senator", [
        claim("kb1", "kevin-blackwell", "election_integrity", 0, True,
              "Blackwell was a named co-sponsor of SB 2358 (2023), the Mississippi ballot-harvesting ban making it a crime for anyone other than an election official, postal carrier, family or household member, or caregiver to collect and submit absentee ballots on behalf of another person — violations carry up to one year in jail and a $3,000 fine; Gov. Reeves signed it March 22, 2023, effective July 1, 2023.",
              ["https://billstatus.ls.state.ms.us/documents/2023/html/SB/2300-2399/SB2358IN.htm",
               "https://www.wlox.com/2023/03/22/ballot-harvesting-now-banned-mississippi/"]),
        claim("kb2", "kevin-blackwell", "family_child_sovereignty", 0, True,
              "Blackwell voted with the Republican caucus for HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 on a strict party-line vote on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/history/HB/HB1125.xml",
               "https://magnoliatribune.com/2023/02/23/mississippi-legislature-sends-bill-preventing-gender-reassignment-for-minors-to-governor/"]),
        claim("kb3", "kevin-blackwell", "election_integrity", 0, True,
              "Blackwell voted with the Republican caucus for SB 2588 (2026), the SHIELD Act, which requires annual citizenship verification of all registered voters against the federal SAVE database and mandates county registrars to run applicants through SAVE before registering them; the Senate passed it 33-17 on a strict party-line vote on February 5, 2026, and Gov. Reeves signed it April 3, 2026, effective July 1, 2026.",
              ["https://magnoliatribune.com/2026/04/01/governor-signs-shield-act-into-law-seeking-to-further-safeguard-mississippi-elections/",
               "https://www.mississippifreepress.org/mississippi-governor-signs-shield-act-into-law-enacting-voter-citizenship-checks/"]),
    ]),

    # --- Josh Harkins (MS SD-20, State Senator — Rankin/Scott counties, Finance Committee Chair) ---
    ("josh-harkins", "MS", "State Senator", [
        claim("jh1", "josh-harkins", "biblical_marriage", 2, True,
              "Harkins authored SB 2753 (2024), the Mississippi SAFER Act (Students and Athletes Free from Explicit Restrooms), prohibiting persons of one biological sex from using restrooms, changing rooms, or shower facilities designated for the opposite sex in public schools, public universities, and government buildings; the Senate passed it 35-15 and Gov. Reeves signed it April 15, 2024.",
              ["https://billstatus.ls.state.ms.us/documents/2024/html/SB/2700-2799/SB2753SG.htm",
               "https://www.wlbt.com/2024/04/15/gov-reeves-signs-safer-act-banning-biological-males-womens-restrooms-schools/"]),
        claim("jh2", "josh-harkins", "economic_stewardship", 0, True,
              "Harkins, serving as Senate Finance Committee Chairman, co-authored HB 1 (2025), the landmark Mississippi income tax elimination bill that phases out the state's 4% flat income tax entirely by 2030 — the largest tax cut in Mississippi history; Harkins shepherded the bill through the Finance Committee and the Senate, which passed it with overwhelming Republican support; Gov. Reeves signed it March 27, 2025.",
              ["https://billstatus.ls.state.ms.us/documents/2025/html/HB/0001-0099/HB0001SG.htm",
               "https://mississippitoday.org/2025/03/27/mississippi-eliminates-income-tax/"]),
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
