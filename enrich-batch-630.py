#!/usr/bin/env python3
"""Enrichment batch 630: hand-curated claims for 3 Pennsylvania State Senators.

Senators: Joe Picozzi (SD-5), Greg Rothman (SD-34), Chris Gebhard (SD-48).
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
    # --- Joe Picozzi (PA SD-5, State Senator — Northeast Philadelphia) ---
    ("joe-picozzi", "PA", "State Senator", [
        claim("jp1", "joe-picozzi", "election_integrity", 0, False,
              "Picozzi co-sponsored SB 400 (2025-2026), which amends the Pennsylvania Election Code to allow unenrolled independent voters to cast ballots in party primaries — an open-primary expansion that loosens rather than strengthens election-integrity requirements such as voter identification and ballot security.",
              ["https://www.palegis.us/legislation/bills/2025/sb400",
               "https://ballotpedia.org/Joe_Picozzi"]),
    ]),

    # --- Greg Rothman (PA SD-34, State Senator) ---
    ("greg-rothman", "PA", "State Senator", [
        claim("gr1", "greg-rothman", "election_integrity", 0, True,
              "Rothman co-sponsored SB 1 (2023-2024), a joint resolution proposing a constitutional amendment to require all qualified Pennsylvania electors to present valid photo identification at every election; the Senate passed it 28-20 on January 11, 2023.",
              ["https://www.palegis.us/legislation/bills/2023/sb1",
               "https://legiscan.com/PA/bill/SB1/2023"]),
        claim("gr2", "greg-rothman", "sanctity_of_life", 0, True,
              "Rothman co-sponsored SB 1 (2023-2024), a joint resolution that also proposed a constitutional amendment explicitly declaring the Pennsylvania Constitution confers no right to abortion and no right to taxpayer-funded abortion, effectively removing any state constitutional basis for abortion access.",
              ["https://www.palegis.us/legislation/bills/2023/sb1",
               "https://www.pasenategop.com"]),
        claim("gr3", "greg-rothman", "self_defense", 0, True,
              "Rothman co-sponsored SB 357 (2025-2026), Pennsylvania's constitutional carry bill allowing law-abiding adults to carry concealed firearms without a government-issued permit while preserving an optional License to Carry for interstate reciprocity.",
              ["https://www.palegis.us/legislation/bills/2025/sb357",
               "https://www.pasenategop.com/news/baker-judiciary-committee-advances-constitutional-carry-as-senate-sends-preemption-expansion-to-the-house/"]),
    ]),

    # --- Chris Gebhard (PA SD-48, State Senator) ---
    ("chris-gebhard", "PA", "State Senator", [
        claim("cg1", "chris-gebhard", "biblical_marriage", 2, True,
              "Gebhard is the prime sponsor of SB 1321 (2025-2026), which prohibits Pennsylvania Medicaid and CHIP reimbursements for any gender-transition procedure performed on a minor; the bill advanced through the Senate Banking and Insurance Committee in May 2026.",
              ["https://www.palegis.us/legislation/bills/2025/sb1321",
               "https://www.pasenategop.com/news/measure-to-end-state-funding-for-gender-transition-of-minors-passes-committee/"]),
        claim("cg2", "chris-gebhard", "election_integrity", 0, True,
              "Gebhard co-sponsored SB 1 (2023-2024), a joint resolution proposing a constitutional amendment requiring qualified Pennsylvania electors to present valid identification at every election; the Senate passed it 28-20 on January 11, 2023.",
              ["https://www.palegis.us/legislation/bills/2023/sb1",
               "https://legiscan.com/PA/bill/SB1/2023"]),
        claim("cg3", "chris-gebhard", "self_defense", 0, True,
              "Gebhard co-sponsored SB 357 (2025-2026), Pennsylvania's constitutional carry bill establishing that law-abiding adults may carry concealed firearms without a government-issued permit, while retaining an optional License to Carry for reciprocity purposes.",
              ["https://www.palegis.us/legislation/bills/2025/sb357",
               "https://www.pasenategop.com/news/baker-judiciary-committee-advances-constitutional-carry-as-senate-sends-preemption-expansion-to-the-house/"]),
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
