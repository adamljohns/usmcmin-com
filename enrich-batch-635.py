#!/usr/bin/env python3
"""Enrichment batch 635: hand-curated claims for 2 Oklahoma State Senators.

Senators: Christi Gillespie (SD-33), Chuck Hall (SD-20).
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
    # --- Christi Gillespie (OK SD-33, State Senator — Wagoner County, in office Nov 2024) ---
    ("christi-gillespie", "OK", "State Senator", [
        claim("cg1", "christi-gillespie", "sanctity_of_life", 0, True,
              "Gillespie voted YES on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them to cause an unlawful abortion; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking",
               "https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM"]),
        claim("cg2", "christi-gillespie", "self_defense", 0, True,
              "Gillespie was the prime Senate sponsor of SB 628 (2025), the Municipal Carry Act, modifying Oklahoma's firearm carry statutes to allow municipalities to authorize public officials and designated employees to carry concealed firearms inside government buildings where general carry had been restricted; the Senate passed it 39-8 and Gov. Stitt signed it May 2025.",
              ["https://oklahomavoice.com/briefs/senate-advances-gun-bill-that-could-expand-gun-rights-for-oklahoma-municipal-employees/",
               "https://www.okhouse.gov/posts/news-20250515_1"]),
        claim("cg3", "christi-gillespie", "economic_stewardship", 0, True,
              "Gillespie voted YES on HB 2764 (2025), cutting Oklahoma's top personal income tax rate from 4.75% to 4.5% starting in 2026, collapsing six brackets into three, and establishing a trigger mechanism for automatic future rate reductions toward full income tax elimination; the Senate passed it 34-11 on May 22, 2025, and Gov. Stitt signed it May 28, 2025.",
              ["https://oksenate.gov/press-releases/oklahoma-legislature-sends-comprehensive-tax-cuts-and-modernization-plan-governor",
               "https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB2764_VOTES.HTM"]),
    ]),

    # --- Chuck Hall (OK SD-20, State Senator — Perry/Noble County) ---
    ("chuck-hall", "OK", "State Senator", [
        claim("ch1", "chuck-hall", "sanctity_of_life", 0, True,
              "Hall voted YES on SB 918 (2021), Oklahoma's abortion trigger law reactivating the state's pre-Roe criminal abortion ban upon any SCOTUS ruling restoring state authority over abortion; the Senate passed it 38-9 on March 10, 2021, and Gov. Stitt signed it April 27, 2021. Hall is named in the confirmed YES roll call.",
              ["http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/SB918_VOTES.HTM",
               "https://legiscan.com/OK/bill/SB918/2021"]),
        claim("ch2", "chuck-hall", "biblical_marriage", 2, True,
              "Hall voted YES on SB 2 (2022), the Save Women's Sports Act, requiring all K-12 and collegiate athletic teams to be designated based on biological sex at birth and barring biological males from competing on female-designated teams at any Oklahoma public school or university; the Senate passed it 37-7 on March 24, 2022, and Gov. Stitt signed it March 30, 2022.",
              ["http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/SB2_VOTES.HTM",
               "https://legiscan.com/OK/bill/SB2/2022"]),
        claim("ch3", "chuck-hall", "family_child_sovereignty", 0, True,
              "Hall voted YES on SB 613 (2023), banning gender transition procedures for minors in Oklahoma — including puberty blockers, cross-sex hormone therapy, and surgical interventions — and authorizing civil lawsuits against providers and professional license revocations; the Senate passed it 37-8 on April 27, 2023, and Gov. Stitt signed it May 1, 2023.",
              ["http://webserver1.lsb.state.ok.us/cf/2023-24%20SUPPORT%20DOCUMENTS/votes/Senate/SB613_VOTES.HTM",
               "https://legiscan.com/OK/bill/SB613/2023"]),
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
