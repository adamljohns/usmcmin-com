#!/usr/bin/env python3
"""Enrichment batch 650: hand-curated claims for 2 Mississippi State Senators.

Senators: Nicole Akins Boyd (SD-9), Neil Whaley (SD-10).
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
    # --- Nicole Akins Boyd (MS SD-9, State Senator — Lafayette/Panola County, in office since Jan 2020) ---
    ("nicole-akins-boyd", "MS", "State Senator", [
        claim("nab1", "nicole-akins-boyd", "family_child_sovereignty", 0, True,
              "Boyd authored and passed SB 2346 (2023), requiring any commercial website that distributes substantial pornographic content to implement age verification — digitized ID or commercial age-verification system — before granting access, and establishing civil liability for platforms that allow minors to access such content; the Mississippi Senate passed it 52-0 and Gov. Reeves signed it April 18, 2023, effective July 1, 2023.",
              ["https://www.thecentersquare.com/mississippi/article_51302e70-9d8f-11ed-8494-cf79ab1fdf30.html",
               "https://www.wlbt.com/2023/07/04/two-new-mississippi-laws-are-designed-protect-kids-easy-access-porn/"]),
    ]),

    # --- Neil Whaley (MS SD-10, State Senator — Marshall County/NW Mississippi, in office since Dec 2017) ---
    ("neil-whaley", "MS", "State Senator", [
        claim("nw1", "neil-whaley", "biblical_marriage", 2, True,
              "Whaley was a named co-author of SB 2536 (2021), the Mississippi Fairness Act, requiring all public schools and NCAA/NAIA/MHSAA-member institutions to designate athletic teams strictly by biological sex and prohibiting biological males from competing on female teams; the Senate passed it 34-9 on February 11, 2021, and Gov. Reeves signed it March 11, 2021, making Mississippi the first state in the nation to enact such a law.",
              ["https://magnoliatribune.com/2021/02/12/ms-senate-passes-fairness-act-aimed-at-protecting-female-athletes-see-how-your-senator-voted/",
               "https://www.wlbt.com/2021/03/12/gov-reeves-signs-bill-banning-trans-athletes-from-school-sports/"]),
        claim("nw2", "neil-whaley", "economic_stewardship", 0, True,
              "Whaley introduced SB 2272 (2026) to eliminate Mississippi's 1.5% sales tax on farm tractors, implements, logging and pulpwood equipment, and related parts, while fully exempting livestock fencing materials and agricultural lime — delivering direct tax relief to farmers and rural small businesses; the Senate passed the bill 50-1, demonstrating near-unanimous support, though it did not survive conference with the House.",
              ["https://www.supertalk.fm/bill-eliminating-sales-tax-on-ag-equipment-passes-in-mississippi-senate/",
               "https://msfb.org/capital-comments-mississippi-state-legislature-week-7-update/"]),
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
