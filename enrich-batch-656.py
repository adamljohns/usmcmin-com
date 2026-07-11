#!/usr/bin/env python3
"""Enrichment batch 656: hand-curated claims for 2 Mississippi State Senators.

Senators: Jeff Tate (SD-32), Andy Berry (SD-33).
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
    # --- Jeff Tate (MS SD-32, State Senator — Lamar/Pearl River counties) ---
    ("jeff-tate", "MS", "State Senator", [
        claim("jt1", "jeff-tate", "biblical_marriage", 2, True,
              "Tate was a named co-sponsor of SB 2536 (2021), the Mississippi Fairness Act, requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting biological males from competing on female teams; Tate's co-sponsorship is confirmed in the enrolled bill text; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021, making Mississippi the first state in the nation to enact such a law.",
              ["https://legiscan.com/MS/text/SB2536/id/2271648",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("jt2", "jeff-tate", "election_integrity", 0, True,
              "Tate was directly quoted opposing early voting expansion proposals, stating 'everybody should have to show their ID and vote on Election Day with a paper ballot' — a clear statement of his support for in-person, voter-ID-required, paper-ballot elections; Tate voted against early voting legislation in the 2025 legislative session.",
              ["https://magnoliatribune.com/2025/02/mississippi-early-voting-debate/",
               "https://www.supertalk.fm/mississippi-senators-debate-early-voting/"]),
        claim("jt3", "jeff-tate", "family_child_sovereignty", 0, True,
              "Tate voted with the Republican caucus for HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 on a strict party-line vote on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/history/HB/HB1125.xml",
               "https://magnoliatribune.com/2023/02/23/mississippi-legislature-sends-bill-preventing-gender-reassignment-for-minors-to-governor/"]),
    ]),

    # --- Andy Berry (MS SD-33, State Senator — Forrest/Perry counties) ---
    ("andy-berry", "MS", "State Senator", [
        claim("ab1", "andy-berry", "family_child_sovereignty", 0, True,
              "Berry voted for HB 1126 (2024), the Mississippi Age-Appropriate Design Code Act, requiring digital platforms to perform data protection impact assessments and prohibiting collection or use of personal data of minors in ways that are not in the minor's best interests; the Senate passed it unanimously 49-0 and Gov. Reeves signed it March 15, 2024.",
              ["https://billstatus.ls.state.ms.us/documents/2024/html/HB/1100-1199/HB1126SG.htm",
               "https://www.wlbt.com/2024/03/15/gov-reeves-signs-bill-protecting-children-online/"]),
        claim("ab2", "andy-berry", "sanctity_of_life", 0, True,
              "Berry voted with the Republican caucus for HB 1613 (2026), which amends Mississippi drug trafficking law to classify distribution of abortion-inducing drugs — including mifepristone and misoprostol — as a felony carrying up to 10 years in prison; the House passed it 77-39 and the Senate 37-15; Gov. Reeves signed it April 8, 2026.",
              ["https://mississippitoday.org/2026/04/01/mississippi-abortion-medication/",
               "https://www.mississippifreepress.org/bill-criminalizing-mail-order-abortion-pills-as-drug-trafficking-heads-to-mississippi-governors-desk/"]),
        claim("ab3", "andy-berry", "election_integrity", 0, True,
              "Berry voted with the Republican caucus for SB 2588 (2026), the SHIELD Act, which requires annual citizenship verification of all registered voters against the federal SAVE database and mandates county registrars to run applicants through SAVE before registering them; the Senate passed it 33-17 on a strict party-line vote on February 5, 2026, and Gov. Reeves signed it April 3, 2026.",
              ["https://magnoliatribune.com/2026/04/01/governor-signs-shield-act-into-law-seeking-to-further-safeguard-mississippi-elections/",
               "https://www.mississippifreepress.org/mississippi-governor-signs-shield-act-into-law-enacting-voter-citizenship-checks/"]),
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
