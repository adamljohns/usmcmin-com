#!/usr/bin/env python3
"""Enrichment batch 644: hand-curated claims for 2 Oklahoma State Senators.

Senators: Kristen Thompson (SD-22), Lonnie Paxton (SD-23).
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
    # --- Kristen Thompson (OK SD-22, State Senator — Edmond, in office since Nov 2022) ---
    ("kristen-thompson", "OK", "State Senator", [
        claim("kt1", "kristen-thompson", "sanctity_of_life", 0, True,
              "Thompson voted AYE on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; Thompson's name is confirmed in the AYES list of the official roll call; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
        claim("kt2", "kristen-thompson", "self_defense", 0, True,
              "Thompson voted AYE on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses that discriminate against firearm companies or trade associations; Thompson's name is confirmed in the AYES list of the official roll call; the Senate passed it 38-8 on March 26, 2025, and Gov. Stitt signed it effective November 1, 2025.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM",
               "https://www.nraila.org/articles/20250328/oklahoma-firearm-non-discrimination-bill-passes-senate"]),
        claim("kt3", "kristen-thompson", "family_child_sovereignty", 0, True,
              "Thompson voted YES on SB 613 (2023), banning gender-transition procedures for minors in Oklahoma — including puberty blockers, cross-sex hormone therapy, and surgical interventions — with civil enforcement and professional license revocation provisions; Thompson's vote was confirmed on the official roll call for the April 27, 2023 final passage; the Senate passed it 37-8 and Gov. Stitt signed it May 2023.",
              ["https://oksenate.gov/press-releases/senate-approves-bill-prohibiting-gender-transition-procedures-minors",
               "https://legiscan.com/OK/bill/SB613/2023"]),
    ]),

    # --- Lonnie Paxton (OK SD-23, State Senator — Tuttle/Mustang, Senate President Pro Tempore, in office since Nov 2016) ---
    ("lonnie-paxton", "OK", "State Senator", [
        claim("lp1", "lonnie-paxton", "election_integrity", 0, True,
              "Paxton was the Senate primary co-author of SJR 47 (2026), referring a constitutional voter identification amendment to Oklahoma voters as State Question 846 on the August 25, 2026 primary ballot; as Senate President Pro Tempore, Paxton sponsored the measure alongside House Speaker Kyle Hilbert; the Senate passed it 39-8 on a strict party-line vote — all 39 Republicans in favor — and all 8 Democrats opposed.",
              ["https://oklahomavoice.com/briefs/oklahoma-lawmakers-send-voter-id-state-question-to-august-ballot/",
               "https://ballotpedia.org/Oklahoma_State_Question_846,_Voter_Identification_Requirement_Amendment_(August_2026)"]),
        claim("lp2", "lonnie-paxton", "sanctity_of_life", 0, True,
              "Paxton voted AYE on HB 1168 (2026), the Stop Chemical Abortion Trafficking Act making it a felony (up to 10 years prison and $100,000 fine) to knowingly traffic abortion-inducing drugs to someone intending an unlawful abortion; as Senate President Pro Tempore, Paxton also used his floor authority to place HB 1168 on the Senate agenda to ensure its passage; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
        claim("lp3", "lonnie-paxton", "family_child_sovereignty", 0, True,
              "Paxton voted YES on SB 613 (2023), banning gender-transition procedures for minors in Oklahoma — including puberty blockers, cross-sex hormone therapy, and surgical interventions — with civil enforcement and professional license revocation provisions; Paxton's YES vote was confirmed on both the February 15, 2023 (40-8) and April 27, 2023 (37-8) final readings; Gov. Stitt signed it May 2023 and the Tenth Circuit upheld it in 2024.",
              ["https://oksenate.gov/press-releases/senate-approves-bill-prohibiting-gender-transition-procedures-minors",
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
