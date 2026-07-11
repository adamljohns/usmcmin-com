#!/usr/bin/env python3
"""Enrichment batch 640: hand-curated claims for 2 Oklahoma State Senators.

Senators: Dana Prieto (SD-34), Darcy Jech (SD-26).
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
    # --- Dana Prieto (OK SD-34, State Senator — Tulsa County, in office since Nov 2022) ---
    ("dana-prieto", "OK", "State Senator", [
        claim("dp1", "dana-prieto", "sanctity_of_life", 0, True,
              "Prieto voted YEA on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
        claim("dp2", "dana-prieto", "self_defense", 0, True,
              "Prieto voted YEA on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses that discriminate against firearm companies or trade associations; the Senate passed it 38-8 and Gov. Stitt signed it effective November 1, 2025.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM",
               "https://www.nraila.org/articles/20250328/oklahoma-firearm-non-discrimination-bill-passes-senate"]),
        claim("dp3", "dana-prieto", "election_integrity", 0, True,
              "Prieto voted YEA on SJR 47 (2026), referring a constitutional voter identification amendment to Oklahoma voters; the Senate passed it 39-8 on March 26, 2026, with all 39 Republicans voting in favor; it was placed on the August 25, 2026 ballot as State Question 846.",
              ["https://oklahomavoice.com/briefs/oklahoma-lawmakers-send-voter-id-state-question-to-august-ballot/",
               "https://legiscan.com/OK/bill/SJR47/2026"]),
    ]),

    # --- Darcy Jech (OK SD-26, State Senator — Kingfisher area, in office since Nov 2014) ---
    ("darcy-jech", "OK", "State Senator", [
        claim("dj1", "darcy-jech", "sanctity_of_life", 0, True,
              "Jech voted YES on SB 918 (2021), Oklahoma's abortion trigger law designed to restore the state's authority to prohibit abortion upon any Supreme Court ruling overturning Roe v. Wade; the Senate passed it 38-9 on March 10, 2021, and Gov. Stitt signed it April 27, 2021.",
              ["http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/SB918_VOTES.HTM",
               "https://legiscan.com/OK/bill/SB918/2021"]),
        claim("dj2", "darcy-jech", "sanctity_of_life", 1, False,
              "Jech voted NAY on HB 1168 (2026), the Stop Chemical Abortion Trafficking Act making delivery of abortion-inducing drugs a felony; the Senate passed it 37-10 on April 30, 2026, with Jech joining all 8 Senate Democrats and one other Republican in opposition — a notable departure from his caucus on anti-abortion legislation.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
        claim("dj3", "darcy-jech", "border_immigration", 0, True,
              "Jech voted YEA on HB 4156 (2024), making unlawful entry or re-entry into Oklahoma after federal deportation a state crime of 'impermissible occupation'; the Senate passed it 37-8 on April 23, 2024, and Gov. Stitt signed it April 30, 2024.",
              ["http://webserver1.lsb.state.ok.us/cf/2023-24%20SUPPORT%20DOCUMENTS/votes/Senate/HB4156_VOTES.HTM",
               "https://legiscan.com/OK/votes/HB4156/2024"]),
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
