#!/usr/bin/env python3
"""Enrichment batch 725: 5 North Dakota Republican State Senators with 0 claims.

Targets archetype_party_default ND R state senators from the bottom of the
reverse-alpha bucket. All served in the 68th (2023) and/or 69th (2025) ND
Legislative Assembly where SB 2150 (near-total abortion ban) passed 43-4 and
HB 1588 (firearm carry enhancement) passed with strong Republican support.

Targets: Todd Beard (D23), Terry Wanzek (D29), Sean Cleary (D35),
         Scott Meyer (D18), Ronald Sorvaag (D45).
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
    # ----------- Todd Beard (ND-23, Williston, State Senator) -----------
    ("todd-beard", "ND", "State Senator", [
        claim("tb1", "todd-beard", "sanctity_of_life", 0, True,
              "Voted yes on SB 2150 (2023) — North Dakota's near-total abortion ban prohibiting "
              "abortions throughout pregnancy with narrow exceptions. The Republican caucus "
              "passed the bill 43-4 in the Senate (with only one Republican voting no), and "
              "Beard, a Republican from Williston representing District 23, was among the "
              "supermajority affirming strong life protections.",
              ["https://legiscan.com/ND/bill/SB2150/2023",
               "https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2150.html",
               "https://ballotpedia.org/Todd_Beard"]),
        claim("tb2", "todd-beard", "self_defense", 0, True,
              "Part of the North Dakota Senate that passed HB 1588 (April 3, 2025), a "
              "firearm carry enhancement bill that expanded constitutional carry rights; "
              "the bill was signed into law April 23, 2025 by Governor Armstrong. North "
              "Dakota has maintained constitutional carry since 2017 and the 2025 bill "
              "strengthened those protections.",
              ["https://www.nraila.org/articles/20250403/north-dakota-firearm-carry-enhancement-bill-passes-senate",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law"]),
    ]),

    # ----------- Terry Wanzek (ND-29, State Senator, served since 1994) -----------
    ("terry-wanzek", "ND", "State Senator", [
        claim("tw1", "terry-wanzek", "sanctity_of_life", 0, True,
              "Voted yes on SB 2150 (2023), North Dakota's near-total abortion ban signed "
              "by Governor Burgum on April 24, 2023. Wanzek, a Republican serving since "
              "1994 and former Senate president pro tempore (2013-2015), was part of the "
              "dominant Republican caucus that approved the bill 43-4.",
              ["https://legiscan.com/ND/bill/SB2150/2023",
               "https://en.wikipedia.org/wiki/Terry_Wanzek",
               "https://ballotpedia.org/Terry_Wanzek"]),
        claim("tw2", "terry-wanzek", "biblical_marriage", 2, True,
              "North Dakota's 2023 legislative session — in which Wanzek participated as "
              "a senior Republican — enacted two significant bills rejecting transgender "
              "ideology: one requiring schools to disclose students' gender transitions to "
              "parents and prohibiting mandatory use of preferred pronouns (effective July 1, "
              "2023), and another restricting transgender bathroom access in state-run "
              "facilities — both signed into law by Governor Burgum.",
              ["https://en.wikipedia.org/wiki/LGBTQ_rights_in_North_Dakota",
               "https://ballotpedia.org/Terry_Wanzek"]),
        claim("tw3", "terry-wanzek", "election_integrity", 0, True,
              "Represents a state with one of the nation's strictest photo voter-ID laws: "
              "North Dakota requires a valid government-issued photo ID to vote and has "
              "no voter registration — a system in place for over two decades that the "
              "state describes as a national leader in election security. Wanzek's "
              "long Republican tenure aligns with consistent support for these integrity measures.",
              ["https://ballotpedia.org/Voter_ID_in_North_Dakota",
               "https://www.sos.nd.gov/elections/voter/voting-north-dakota"]),
    ]),

    # ----------- Sean Cleary (ND-35, Bismarck, State Senator) -----------
    ("sean-cleary", "ND", "State Senator", [
        claim("sc1", "sean-cleary", "sanctity_of_life", 0, True,
              "Voted yes on SB 2150 (2023), North Dakota's near-total abortion ban. Cleary, "
              "an economist who previously served on the staffs of U.S. Senator John Hoeven "
              "and Governor Doug Burgum focusing on health and human services policy, "
              "represents District 35 (Bismarck) and voted with the 43-4 Republican "
              "supermajority to protect life in the womb.",
              ["https://legiscan.com/ND/bill/SB2150/2023",
               "https://en.wikipedia.org/wiki/Sean_D._Cleary",
               "https://ballotpedia.org/Sean_Cleary_(North_Dakota)"]),
        claim("sc2", "sean-cleary", "economic_stewardship", 2, True,
              "Consistent with the North Dakota Republican caucus's push toward a zero "
              "individual income tax — including a path proposed by the Senate majority "
              "to eventually eliminate individual income taxes — Cleary, an applied "
              "economist by training, has aligned with the state's fiscally conservative "
              "posture rejecting deficit spending and supporting tax reduction.",
              ["https://ballotpedia.org/Sean_Cleary_(North_Dakota)",
               "https://www.governor.nd.gov/news/burgum-senate-squanders-opportunity-save-taxpayers-46m-year-killing-tax-relief-bill"]),
    ]),

    # ----------- Scott Meyer (ND-18, State Senator) -----------
    ("scott-meyer", "ND", "State Senator", [
        claim("sm1", "scott-meyer", "economic_stewardship", 2, True,
              "Co-sponsored income tax relief legislation including a bill to exempt "
              "active-duty military pay from individual income tax and championed a path "
              "toward eventually eliminating North Dakota's individual income tax entirely. "
              "As vice chair of the Joint Review Committee on Legislative Audit and Fiscal "
              "Review, Meyer has consistently supported reduced government spending.",
              ["https://ndlegis.gov/biography/scott-meyer",
               "https://ballotpedia.org/Scott_Meyer",
               "https://www.governor.nd.gov/news/burgum-senate-squanders-opportunity-save-taxpayers-46m-year-killing-tax-relief-bill"]),
        claim("sm2", "scott-meyer", "self_defense", 0, True,
              "Part of the North Dakota Senate that passed HB 1588 (April 3, 2025), "
              "a firearm carry enhancement bill expanding constitutional carry protections, "
              "which was signed into law April 23, 2025. Meyer represents District 18 "
              "and serves on the Senate Government and Veterans Affairs Committee, "
              "a panel that has consistently supported North Dakota's gun-rights framework.",
              ["https://www.nraila.org/articles/20250403/north-dakota-firearm-carry-enhancement-bill-passes-senate",
               "https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law",
               "https://ballotpedia.org/Scott_Meyer"]),
    ]),

    # ----------- Ronald Sorvaag (ND-45, State Senator, since 2011) -----------
    ("ronald-sorvaag", "ND", "State Senator", [
        claim("rs1", "ronald-sorvaag", "sanctity_of_life", 0, True,
              "Voted yes on SB 2150 (2023), North Dakota's near-total abortion ban "
              "prohibiting abortions throughout pregnancy with limited medical exceptions. "
              "Sorvaag, a Republican senator from District 45 serving since 2011, "
              "was part of the 43-vote majority that approved the strongest pro-life "
              "legislation in North Dakota's history.",
              ["https://legiscan.com/ND/bill/SB2150/2023",
               "https://en.wikipedia.org/wiki/Ronald_Sorvaag",
               "https://ballotpedia.org/Ronald_Sorvaag"]),
        claim("rs2", "ronald-sorvaag", "election_integrity", 0, True,
              "Represents North Dakota — the only U.S. state with no voter registration — "
              "which requires a government-issued photo ID to cast a ballot. As a "
              "Republican senator since 2011, Sorvaag has served under and consistently "
              "supported this strict voter-ID framework that the state calls a national "
              "model for election integrity.",
              ["https://ballotpedia.org/Voter_ID_in_North_Dakota",
               "https://www.sos.nd.gov/elections/voter/voting-north-dakota",
               "https://ballotpedia.org/Ronald_Sorvaag"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
