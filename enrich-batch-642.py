#!/usr/bin/env python3
"""Enrichment batch 642: hand-curated claims for 2 Oklahoma State Senators.

Senators: John Haste (SD-36), Jonathan Wingard (SD-13).
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
    # --- John Haste (OK SD-36, State Senator — Broken Arrow, in office since Nov 2018) ---
    ("john-haste", "OK", "State Senator", [
        claim("jh1", "john-haste", "sanctity_of_life", 0, True,
              "Haste voted YES on SB 612 (2022), Oklahoma's felony abortion ban prohibiting all abortions except to save the mother's life in a medical emergency — with penalties of up to 10 years in prison and a $100,000 fine for providers; Haste's name appears as a Yea vote in the official Senate roll call; the Senate passed it 38-9 and Gov. Stitt signed it April 12, 2022.",
              ["http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/SB612_VOTES.HTM",
               "https://www.oklegislature.gov/BillInfo.aspx?Bill=sb612&Session=2200"]),
        claim("jh2", "john-haste", "election_integrity", 0, True,
              "Haste was the Senate prime author of HB 3364 (2022), requiring online absentee ballot requests to include voter identification — driver's license number, state ID number, or last four digits of SSN — with a second provision effective January 1, 2023 requiring address confirmation before submission; Muskogee Politico names 'Sen. John Haste, R-Broken Arrow' as prime author; Gov. Stitt signed it into law May 2022.",
              ["https://www.muskogeepolitico.com/2022/05/two-bills-to-make-absentee-ballots-and.html",
               "https://oksenate.gov/senator-press-releases/john-haste"]),
        claim("jh3", "john-haste", "self_defense", 0, True,
              "Haste voted YES on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses that discriminate against firearm companies or trade associations; Haste's name was confirmed in the AYE list on the official roll call; the Senate passed it 38-8 on March 26, 2025, and Gov. Stitt signed it effective November 1, 2025.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM",
               "https://www.nraila.org/articles/20250328/oklahoma-firearm-non-discrimination-bill-passes-senate"]),
    ]),

    # --- Jonathan Wingard (OK SD-13, State Senator — Ada area, in office since Nov 2024) ---
    ("jonathan-wingard", "OK", "State Senator", [
        claim("jw1", "jonathan-wingard", "self_defense", 0, True,
              "Wingard voted YES on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses that discriminate against firearm companies or trade associations; Wingard's name was confirmed in the official roll call Ayes list; the Senate passed it 38-8 on March 26, 2025, and Gov. Stitt signed it effective November 1, 2025. Wingard scored 93% on the 2025 Oklahoma Conservative Index.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM",
               "https://www.nraila.org/articles/20250328/oklahoma-firearm-non-discrimination-bill-passes-senate"]),
        claim("jw2", "jonathan-wingard", "sanctity_of_life", 0, True,
              "Wingard voted YES on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; the bill exempts contraceptives, IVF, miscarriage care, and lawful pharmaceutical distribution; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
        claim("jw3", "jonathan-wingard", "election_integrity", 0, True,
              "Wingard voted YES on SJR 47 (2026), referring a constitutional voter identification amendment to Oklahoma voters as State Question 846 on the August 25, 2026 primary ballot; the Senate passed it 39-8 on March 26, 2026, on a strict party-line vote with all 39 Republicans — including Wingard — in favor and all 8 Democrats opposed.",
              ["https://news.ballotpedia.org/2026/04/17/oklahoma-voters-to-decide-ballot-measure-to-add-voter-id-requirement-to-the-state-constitution-on-aug-25-2026/",
               "https://oklahomavoice.com/briefs/oklahoma-lawmakers-send-voter-id-state-question-to-august-ballot/"]),
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
