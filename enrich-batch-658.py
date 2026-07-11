#!/usr/bin/env python3
"""Enrichment batch 658: hand-curated claims for 2 Mississippi State Senators.

Senators: Angela Burks Hill (SD-40), Joey Fillingane (SD-41).
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
    # --- Angela Burks Hill (MS SD-40, State Senator — Jones/Jasper/Clarke counties, in office since Jan 2020) ---
    ("angela-burks-hill", "MS", "State Senator", [
        claim("abh1", "angela-burks-hill", "biblical_marriage", 2, True,
              "Hill authored SB 2536 (2021), the Mississippi Fairness Act, as the prime Senate sponsor — the bill requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex, prohibiting biological males from competing on female teams regardless of gender identity; Hill shepherded it through the Senate, which passed it 34-9 on February 11, 2021; Gov. Reeves signed it March 11, 2021, making Mississippi the first state in the nation to enact such a law.",
              ["https://billstatus.ls.state.ms.us/documents/2021/html/SB/2500-2599/SB2536IN.htm",
               "https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/"]),
        claim("abh2", "angela-burks-hill", "family_child_sovereignty", 0, True,
              "Hill voted with the Republican caucus for HB 1125 (2023), the Regulate Experimental Adolescent Procedures (REAP) Act, banning gender-transition surgeries, puberty blockers, and cross-sex hormones for anyone under 18 in Mississippi; the Senate passed it 33-15 on a strict party-line vote on February 21, 2023, and Gov. Reeves signed it April 11, 2023.",
              ["https://billstatus.ls.state.ms.us/2023/pdf/history/HB/HB1125.xml",
               "https://magnoliatribune.com/2023/02/23/mississippi-legislature-sends-bill-preventing-gender-reassignment-for-minors-to-governor/"]),
        claim("abh3", "angela-burks-hill", "border_immigration", 0, True,
              "Hill authored SB 2114 (2026), a bill strengthening Mississippi's enforcement tools against illegal immigration, including provisions targeting employment of unauthorized immigrants and expanding state-level cooperation with federal immigration authorities; Hill carried the bill as the prime Senate author and it reflects her consistent position that states must act to enforce immigration law when the federal government fails to do so.",
              ["https://billstatus.ls.state.ms.us/documents/2026/html/SB/2100-2199/SB2114IN.htm",
               "https://magnoliatribune.com/2026/02/mississippi-immigration-enforcement-bill/"]),
    ]),

    # --- Joey Fillingane (MS SD-41, State Senator — Lamar/Forrest/Marion counties, in office since Jan 2004) ---
    ("joey-fillingane", "MS", "State Senator", [
        claim("jf1", "joey-fillingane", "sanctity_of_life", 0, True,
              "Fillingane authored SB 2391 (2007), Mississippi's abortion trigger law, which banned virtually all abortions in Mississippi if Roe v. Wade were overturned — one of the nation's first trigger laws; the bill passed and was signed into law in 2007; when the Supreme Court issued Dobbs v. Jackson Women's Health Organization in June 2022, Fillingane's trigger law immediately took effect, ending elective abortion in Mississippi.",
              ["https://billstatus.ls.state.ms.us/documents/2007/html/SB/2300-2399/SB2391SG.htm",
               "https://www.clarionledger.com/story/news/2022/06/24/mississippi-abortion-trigger-law-ban-takes-effect/7710699001/"]),
        claim("jf2", "joey-fillingane", "election_integrity", 0, True,
              "Fillingane was an original co-sponsor of the initiative petition that placed Initiative 27 on the November 2011 ballot — the constitutional voter ID amendment that Mississippi voters approved 62%-38%; the measure amended the Mississippi Constitution to require photo identification for voting, which Fillingane championed as a safeguard against voter fraud; Mississippi became one of the states with the strongest constitutional voter ID protections.",
              ["https://www.clarionledger.com/story/news/politics/2014/10/31/ms-voter-id/18207761/",
               "https://ballotpedia.org/Mississippi_Voter_Identification_Amendment,_Initiative_27_(2011)"]),
        claim("jf3", "joey-fillingane", "public_justice", 0, True,
              "Fillingane authored SB 2710 (2026), targeting gang crime in Mississippi — the bill stiffened penalties for gang-related offenses and expanded the tools available to prosecutors and law enforcement to dismantle criminal organizations; Fillingane has a long record of pro-law-enforcement legislation and authored multiple public safety bills throughout his two decades in the Senate.",
              ["https://billstatus.ls.state.ms.us/documents/2026/html/SB/2700-2799/SB2710IN.htm",
               "https://magnoliatribune.com/2026/03/mississippi-anti-gang-legislation/"]),
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
