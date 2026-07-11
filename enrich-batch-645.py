#!/usr/bin/env python3
"""Enrichment batch 645: hand-curated claims for 2 Oklahoma State Senators.

Senators: Paul Rosino (SD-45), Spencer Kern (SD-31).
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
    # --- Paul Rosino (OK SD-45, State Senator — OKC metro, in office since Nov 2017) ---
    ("paul-rosino", "OK", "State Senator", [
        claim("pr1", "paul-rosino", "sanctity_of_life", 0, True,
              "Rosino voted AYE on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; Rosino's name is confirmed in the AYE list of the official Senate roll call; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
        claim("pr2", "paul-rosino", "election_integrity", 0, True,
              "Rosino voted YES on SJR 47 (2026), referring a constitutional voter identification amendment to Oklahoma voters as State Question 846 on the August 25, 2026 ballot; the Senate passed it 39-8 on a strict party-line vote with all 39 Republicans — including Rosino — in favor and all 8 Democrats opposed; the measure, authored by Senate Pro Tem Lonnie Paxton, would enshrine Oklahoma's photo-ID voting requirement in the state constitution.",
              ["https://oklahomavoice.com/briefs/oklahoma-lawmakers-send-voter-id-state-question-to-august-ballot/",
               "https://www.kgou.org/politics-and-government/2026-07-10/what-to-know-about-state-question-846-the-voter-identification-measure"]),
        claim("pr3", "paul-rosino", "self_defense", 0, True,
              "Rosino voted AYE on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses that discriminate against firearm companies or trade associations; Rosino's name is confirmed in the AYE list of the official Senate roll call; the Senate passed it 38-8 on March 26, 2025, and Gov. Stitt signed it effective November 1, 2025.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM",
               "https://www.nraila.org/articles/20250328/oklahoma-firearm-non-discrimination-bill-passes-senate"]),
    ]),

    # --- Spencer Kern (OK SD-31, State Senator — Duncan/SW Oklahoma, in office since Nov 2024) ---
    ("spencer-kern", "OK", "State Senator", [
        claim("sk1", "spencer-kern", "self_defense", 0, True,
              "Kern voted AYE on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses that discriminate against firearm companies or trade associations — one of his earliest major floor votes, taken roughly four months after taking office in November 2024; Kern's name is confirmed in the AYE list of the official Senate roll call; the Senate passed it 38-8 on March 26, 2025, and Gov. Stitt signed it effective November 1, 2025.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM",
               "https://www.nraila.org/articles/20250328/oklahoma-firearm-non-discrimination-bill-passes-senate"]),
        claim("sk2", "spencer-kern", "election_integrity", 0, True,
              "Kern voted YES on SJR 47 (2026), referring a constitutional voter identification amendment to Oklahoma voters as State Question 846 on the August 25, 2026 ballot; the Senate passed it 39-8 on a strict party-line vote with all 39 Republicans — including Kern — in favor and all 8 Democrats opposed; the measure would enshrine Oklahoma's photo-ID voting requirement in the state constitution.",
              ["https://oklahomavoice.com/briefs/oklahoma-lawmakers-send-voter-id-state-question-to-august-ballot/",
               "https://oklahomawatch.org/2026/07/10/what-to-know-about-state-question-846-the-voter-identification-measure"]),
        claim("sk3", "spencer-kern", "sanctity_of_life", 0, True,
              "Kern voted AYE on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; Kern's name is confirmed in the AYE list of the official Senate roll call; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
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
