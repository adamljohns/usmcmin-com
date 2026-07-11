#!/usr/bin/env python3
"""Enrichment batch 639: hand-curated claims for 2 Oklahoma State Senators.

Senators: David Rader (SD-39), Dusty Deevers (SD-32).
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
    # --- David Rader (OK SD-39, State Senator — Verdigris/Tulsa area) ---
    ("david-rader", "OK", "State Senator", [
        claim("dr1", "david-rader", "sanctity_of_life", 0, True,
              "Rader voted YES on SB 918 (2021), Oklahoma's abortion trigger law designed to restore the state's authority to ban abortion upon any Supreme Court ruling overturning Roe v. Wade; the Senate passed it 38-9 on March 10, 2021, and Gov. Stitt signed it April 27, 2021.",
              ["http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/SB918_VOTES.HTM",
               "https://legiscan.com/OK/bill/SB918/2021"]),
        claim("dr2", "david-rader", "family_child_sovereignty", 0, True,
              "Rader voted YES on SB 613 (2023), banning gender-transition procedures for minors in Oklahoma — including puberty blockers, cross-sex hormone therapy, and surgical interventions — with civil enforcement and professional license revocation provisions; the Senate passed it 37-8 on April 27, 2023, and Gov. Stitt signed it May 1, 2023.",
              ["http://webserver1.lsb.state.ok.us/cf/2023-24%20SUPPORT%20DOCUMENTS/votes/Senate/SB613_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-approves-bill-prohibiting-gender-transition-procedures-minors"]),
        claim("dr3", "david-rader", "sanctity_of_life", 0, True,
              "Rader voted YES on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to someone intending an unlawful abortion; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking"]),
    ]),

    # --- Dusty Deevers (OK SD-32, State Senator — pastor, joined via Dec 2023 special election) ---
    ("dusty-deevers", "OK", "State Senator", [
        claim("dd1", "dusty-deevers", "sanctity_of_life", 0, True,
              "Deevers was the prime author of SB 456 (2025), the Abolition of Abortion Act, which would have extended homicide and equal-protection statutes to all preborn children at every stage and closed the self-managed/pill-order abortion loophole; the bill reflected the most comprehensive anti-abortion authorship in recent Oklahoma Senate history before failing in the Senate Judiciary Committee 6-2 on February 19, 2025.",
              ["https://legiscan.com/OK/bill/SB456/2025",
               "https://www.kosu.org/politics/2025-02-20/abolition-of-abortion-act-fails-in-oklahoma-senate-judiciary-committee"]),
        claim("dd2", "dusty-deevers", "sanctity_of_life", 1, True,
              "Deevers was a named Senate co-author of HB 3038 (2026), the 2026 Abolition of Abortion Act, which would extend 14th Amendment equal protection to all unborn children and make intentionally killing an unborn child a homicide offense; the bill surged to 25 total authors and co-authors after an Abolition Day rally — more than tripling support for any prior abolition measure in Oklahoma history.",
              ["https://legiscan.com/OK/bill/HB3038/2026",
               "https://oksenate.gov/press-releases/oklahoma-abolition-bill-gains-historic-support-after-capitol-rally"]),
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
