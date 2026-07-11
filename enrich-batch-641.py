#!/usr/bin/env python3
"""Enrichment batch 641: hand-curated claims for 2 Oklahoma State Senators.

Senators: Jack Stewart (SD-18), Jerry Alvord (SD-14).
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
    # --- Jack Stewart (OK SD-18, State Senator — Yukon/Canadian County, in office since Nov 2022) ---
    ("jack-stewart", "OK", "State Senator", [
        claim("js1", "jack-stewart", "family_child_sovereignty", 0, True,
              "Stewart voted YES on SB 613 (2023), banning gender-transition procedures for minors in Oklahoma — including puberty blockers, cross-sex hormone therapy, and surgical interventions — with civil enforcement and professional license revocation provisions; Stewart's name was confirmed in the Yeas column of the official roll call; the Senate passed it 37-8 on April 27, 2023, and Gov. Stitt signed it May 1, 2023.",
              ["http://webserver1.lsb.state.ok.us/cf/2023-24%20SUPPORT%20DOCUMENTS/votes/Senate/SB613_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-approves-bill-prohibiting-gender-transition-procedures-minors"]),
        claim("js2", "jack-stewart", "self_defense", 0, True,
              "Stewart voted YES on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses that discriminate against firearm companies or trade associations; Stewart's name was confirmed in the 38-member Ayes list on the official roll call; the Senate passed it 38-8 on March 26, 2025, and Gov. Stitt signed it effective November 1, 2025.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM",
               "https://www.nraila.org/articles/20250328/oklahoma-firearm-non-discrimination-bill-passes-senate"]),
        claim("js3", "jack-stewart", "sanctity_of_life", 0, True,
              "Stewart voted YES on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; Stewart's name was confirmed in the 37-member Ayes list on the official roll call; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
    ]),

    # --- Jerry Alvord (OK SD-14, State Senator — Wilson/Carter County, in office since Nov 2022) ---
    ("jerry-alvord", "OK", "State Senator", [
        claim("ja1", "jerry-alvord", "family_child_sovereignty", 0, True,
              "Alvord was the prime author of SB 1959 (2024), requiring commercial adult-content websites to implement age verification to prevent minors from accessing explicit material, and establishing liability for platforms hosting child sexual abuse material; the Senate passed it 41-5 on March 5, 2024, the House passed it 79-13 on April 23, 2024, and Gov. Stitt signed it into law effective November 1, 2024. Co-authored with Senators Bullard and Jett.",
              ["https://oksenate.gov/press-releases/alvord-leads-way-protecting-kids-online-pornography",
               "https://oksenate.gov/press-releases/alvords-child-protection-bill-passes-house-heads-governors-desk"]),
        claim("ja2", "jerry-alvord", "self_defense", 0, True,
              "Alvord voted YES on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses that discriminate against firearm companies or trade associations; Alvord's name leads the alphabetical Ayes list on the official roll call, confirming his vote; the Senate passed it 38-8 on March 26, 2025, and Gov. Stitt signed it effective November 1, 2025.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM",
               "https://www.nraila.org/articles/20250328/oklahoma-firearm-non-discrimination-bill-passes-senate"]),
        claim("ja3", "jerry-alvord", "sanctity_of_life", 0, True,
              "Alvord voted YES on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; Alvord's name leads the alphabetical Ayes list on the official roll call, confirming his vote; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
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
