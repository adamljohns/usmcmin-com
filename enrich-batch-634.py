#!/usr/bin/env python3
"""Enrichment batch 634: hand-curated claims for 2 Oklahoma State Senators.

Senators: Bryan Logan (SD-8), Casey Murdock (SD-27).
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
    # --- Bryan Logan (OK SD-8, State Senator — sworn in May 2025, Pentecostal pastor) ---
    ("bryan-logan", "OK", "State Senator", [
        claim("bl1", "bryan-logan", "sanctity_of_life", 0, True,
              "Logan is a named Senate co-author of HB 3038 (2026), Oklahoma's Abolition of Abortion Act, which would extend 14th Amendment equal protection to unborn children and make intentionally killing an unborn child a homicide offense; the bill gained historic support with 25 legislative authors and co-authors — more than tripling any prior abolition measure in Oklahoma history.",
              ["https://oksenate.gov/press-releases/oklahoma-abolition-bill-gains-historic-support-after-capitol-rally",
               "https://legiscan.com/OK/bill/HB3038/2026"]),
        claim("bl2", "bryan-logan", "biblical_marriage", 2, True,
              "Logan voted YES on SB 904 (2026), prohibiting all Oklahoma public funds including SoonerCare/Medicaid from covering gender-transition procedures for any patient, and barring state property from being used for such procedures; the roll call confirms his yes vote and Gov. Stitt signed it May 14, 2026 with an emergency clause.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB904_VOTES.HTM",
               "https://legiscan.com/OK/bill/SB904/2026"]),
    ]),

    # --- Casey Murdock (OK SD-27, State Senator — Woodward/Panhandle, Majority Whip) ---
    ("casey-murdock", "OK", "State Senator", [
        claim("cm1", "casey-murdock", "sanctity_of_life", 0, True,
              "Murdock voted YEA on SB 612 (2022), authored by Sen. Nathan Dahm, making performing an abortion a felony punishable by up to 10 years in prison and a $100,000 fine with an exception only to save the mother's life; the Senate passed it 38-9 and Gov. Stitt signed it April 12, 2022.",
              ["http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/SB612_VOTES.HTM",
               "https://legiscan.com/OK/bill/SB612/2022"]),
        claim("cm2", "casey-murdock", "self_defense", 0, True,
              "Murdock was the prime sponsor of SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses that discriminate against firearm companies or trade associations; the Senate passed it 38-8, the House 73-16, and Gov. Stitt signed it effective November 1, 2025.",
              ["https://oksenate.gov/press-releases/murdock-bill-banning-state-contracts-anti-gun-companies-signed-governor",
               "https://www.nraila.org/articles/20250506/oklahoma-governor-stitt-signs-firearm-industry-non-discrimination-bill"]),
        claim("cm3", "casey-murdock", "border_immigration", 0, True,
              "Murdock was the principal Senate author of HB 4156 (2024), creating the state crime of 'impermissible occupation' for unauthorized immigrants who enter and remain in Oklahoma, requiring departure within 72 hours of conviction or release; Gov. Stitt signed it April 30, 2024, and it became fully enforceable in March 2025 after the federal DOJ dropped its lawsuit.",
              ["https://oksenate.gov/press-releases/sen-murdock-comments-passage-house-bill-4156",
               "https://www.kosu.org/politics/2025-03-19/doj-drops-federal-immigration-lawsuit-new-oklahoma-crime-impermissible-occupation-in-full-effect"]),
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
