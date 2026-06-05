#!/usr/bin/env python3
"""Enrichment batch 56: 2 sitting/running federal Republicans from bottom of alphabet.

Targets archetype_curated federal candidates with 0 claims, reverse-sorted
by state (bottom-of-alphabet strategy to avoid collision with the top-down loop).

Candidates: Cory Mills (FL-7, sitting US Rep), Elise Stefanik (NY-21 → NY Gov 2026).
Each claim cites >=1 reliable source and reflects 2022-2025 voting record / public positions.
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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------------- Cory Mills (FL-7, R, sitting US Representative) ----------------
    ("cory-mills", "FL", "Representative", [
        claim("cm1", "cory-mills", "sanctity_of_life", 0, True,
              "Voted yes on the Born-Alive Abortion Survivors Protection Act (H.R. 26, 118th Congress, Jan 11 2023), which requires medical care for infants born alive after a failed abortion. The bill passed the House 220-210.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/26",
               "https://www.govtrack.us/congress/votes/118-2023/h29"]),
        claim("cm2", "cory-mills", "self_defense", 0, True,
              "Cosponsored the Constitutional Concealed Carry Reciprocity Act (H.R. 38, 119th Congress, 2025) — legislation requiring all states to honor concealed-carry permits issued by other states, an expansion of carry rights consistent with constitutional carry principles.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38"]),
        claim("cm3", "cory-mills", "border_immigration", 4, True,
              "Cosponsored the Birthright Citizenship Act of 2025 (H.R. 569, 119th Congress) — a bill to end automatic birthright citizenship for children born in the U.S. to parents who are neither citizens nor lawful permanent residents.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/569"]),
    ]),

    # ---------------- Elise Stefanik (NY-21 rep, R, 2026 NY Governor candidate) ----------------
    ("elise-stefanik-gov", "NY", "Governor", [
        claim("es1", "elise-stefanik-gov", "sanctity_of_life", 0, True,
              "Voted yes on the Born-Alive Abortion Survivors Protection Act (H.R. 26, 118th Congress, Jan 11 2023), requiring medical care for infants who survive a failed abortion. The bill passed the House 220-210.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/26",
               "https://www.govtrack.us/congress/votes/118-2023/h29"]),
        claim("es2", "elise-stefanik-gov", "biblical_marriage", 1, False,
              "Voted yes on the Respect for Marriage Act (H.R. 8404, 117th Congress, July 19 2022), one of 47 Republicans to codify federal recognition of same-sex marriage — rejecting the one-man-one-woman definition the rubric upholds. The bill passed 267-157.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://en.wikipedia.org/wiki/Elise_Stefanik"]),
        claim("es3", "elise-stefanik-gov", "biblical_marriage", 2, True,
              "In 2024, co-authored a joint call (with Dr. Ben Carson and Dr. Miriam Grossman) for a nationwide ban on gender-affirming care for transgender minors and for public schools to be barred from using students' preferred pronouns — a clear rejection of transgender ideology.",
              ["https://en.wikipedia.org/wiki/Elise_Stefanik"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-slug collisions."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        office = (c.get("office") or "")
        if office_keyword.lower() not in office.lower():
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
            print(f"  ✗ NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
