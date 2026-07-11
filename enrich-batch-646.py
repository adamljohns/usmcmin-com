#!/usr/bin/env python3
"""Enrichment batch 646: hand-curated claims for 2 Oklahoma State Senators.

Senators: Kelly E. Hines (SD-47), Kendal Sacchieri (SD-43).
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
    # --- Kelly E. Hines (OK SD-47, State Senator — Norman/Moore, in office since Nov 2024) ---
    ("kelly-e-hines", "OK", "State Senator", [
        claim("kh1", "kelly-e-hines", "sanctity_of_life", 0, True,
              "Hines voted AYE on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; Hines' name appears in the AYE column of the official Senate roll call; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
        claim("kh2", "kelly-e-hines", "election_integrity", 0, True,
              "Hines voted AYE on SJR 47 (2026), referring a constitutional voter identification amendment to Oklahoma voters as State Question 846 on the August 25, 2026 ballot; the Senate passed it 39-8 on a strict party-line vote — all 39 Republicans in favor, all 8 Democrats opposed — definitively placing Hines in the AYE column; the measure would enshrine Oklahoma's existing photo-ID voting requirement in the state constitution.",
              ["https://news.ballotpedia.org/2026/04/17/oklahoma-voters-to-decide-ballot-measure-to-add-voter-id-requirement-to-the-state-constitution-on-aug-25-2026/",
               "https://www.kgou.org/politics-and-government/2026-07-10/what-to-know-about-state-question-846-the-voter-identification-measure"]),
        claim("kh3", "kelly-e-hines", "family_child_sovereignty", 0, True,
              "Hines voted AYE on HB 3586 (2026), the Right to Raise Act, ensuring that prospective adoptive or foster parents cannot be denied placement solely because they decline to use a child's preferred pronouns or support a gender transition, and clarifying that raising a child consistent with biological sex does not constitute abuse or neglect; Hines' name appears in the AYE column of the official roll call; the Senate passed it 39-7 on April 29, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB3586_VOTES.HTM",
               "https://www.okhouse.gov/posts/news-20260507_5"]),
    ]),

    # --- Kendal Sacchieri (OK SD-43, State Senator — Blanchard/Grady-McClain County, in office since Nov 2024) ---
    ("kendal-sacchieri", "OK", "State Senator", [
        claim("ks1", "kendal-sacchieri", "border_immigration", 0, True,
              "Sacchieri was the prime Senate author of SB 20 (2025), the Secure Roads and Safe Trucking Act, requiring commercial vehicle operators in Oklahoma to present proof of citizenship or valid work authorization and demonstrate English proficiency; the law bars B-1/B-2 visitor visa holders from operating commercial vehicles and imposes a $3,000 fine and up to 90 days in jail for violations; the Senate passed it 36-10 on its fourth reading and Gov. Stitt signed it May 27, 2025.",
              ["https://oksenate.gov/press-releases/senator-sacchieri-applauds-passage-sb20-secure-roads-and-safe-trucking-act-2025",
               "https://cdllife.com/2025/oklahoma-bill-pushes-for-english-proficiency-for-cdl-drivers-restricts-b-1-b-2-visa-holders-from-operating-commercial-vehicles/"]),
        claim("ks2", "kendal-sacchieri", "sanctity_of_life", 0, True,
              "Sacchieri voted AYE on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; Sacchieri's name appears in the AYE column of the official Senate roll call; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://www.lifenews.com/2026/04/30/oklahoma-senate-passes-bill-to-stop-mail-order-abortions/"]),
        claim("ks3", "kendal-sacchieri", "election_integrity", 0, True,
              "Sacchieri voted AYE on SJR 47 (2026), referring a constitutional voter identification amendment to Oklahoma voters as State Question 846 on the August 25, 2026 ballot; the Senate passed it 39-8 on a strict party-line vote — all 39 Republicans in favor, all 8 Democrats opposed — definitively placing Sacchieri in the AYE column; the measure would enshrine Oklahoma's existing photo-ID voting requirement in the state constitution.",
              ["https://news.ballotpedia.org/2026/04/17/oklahoma-voters-to-decide-ballot-measure-to-add-voter-id-requirement-to-the-state-constitution-on-aug-25-2026/",
               "https://www.kgou.org/politics-and-government/2026-07-10/what-to-know-about-state-question-846-the-voter-identification-measure"]),
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
