#!/usr/bin/env python3
"""Enrichment batch 277: evidence-curated R federal candidates with 2 claims,
reverse-alphabetical by state (WI → SC → MN → MO).

Targets:
  Ann Wagner      (MO-02,  R, 2 claims → +2)
  Brad Finstad    (MN-01,  R, 2 claims → +2)
  Wes Climer      (SC-05,  R, 2 claims → +1)

All claims cite >=1 reliable source; 2024-2026 positions/records only.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ---------------- Ann Wagner (MO-02, R) ----------------
    ("ann-wagner", "MO", "House", [
        claim("aw3", "ann-wagner", "sanctity_of_life", 3, True,
              "Primary sponsor of H.R. 21, the Born-Alive Abortion Survivors Protection Act, in the 119th Congress (introduced January 3, 2025; passed the House January 23, 2025, 213-210). The bill requires healthcare providers to give life-saving medical care to any infant born alive after a failed abortion attempt, criminalizing abandonment of living infants — a direct legislative defense against infanticide-by-omission.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21",
               "https://www.govtrack.us/congress/bills/119/hr21"]),
        claim("aw4", "ann-wagner", "self_defense", 0, True,
              "Original cosponsor of H.R. 38, the Constitutional Concealed Carry Reciprocity Act of 2025, in the 119th Congress — legislation that would allow any law-abiding citizen with a valid concealed-carry permit (or who legally carries in a permitless-carry state) to carry concealed in any other state, a direct federal recognition of constitutional carry as a nationwide right.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/cosponsors",
               "https://www.govtrack.us/congress/bills/119/hr38"]),
    ]),

    # ---------------- Brad Finstad (MN-01, R) ----------------
    ("brad-finstad", "MN", "House", [
        claim("bf3", "brad-finstad", "sanctity_of_life", 3, True,
              "Cosponsor of H.R. 21, the Born-Alive Abortion Survivors Protection Act, in the 119th Congress (joined January 6, 2025) — legislation requiring healthcare providers to give life-saving care to infants born alive after failed abortion attempts; Finstad also holds a 100% pro-life voting record per SBA Pro-Life America, which ranks him among the most consistent defenders of life-at-every-stage in the Minnesota delegation.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21/cosponsors",
               "https://sbaprolife.org/representative/brad-finstad"]),
        claim("bf4", "brad-finstad", "self_defense", 0, True,
              "Cosponsor of H.R. 38, the Constitutional Concealed Carry Reciprocity Act of 2025, in the 119th Congress — legislation allowing law-abiding citizens with valid permits (or residents of permitless-carry states) to carry concealed firearms nationwide, extending constitutional carry recognition across state lines. Finstad also cosponsored the identical legislation in the 118th Congress (H.R. 38, January 9, 2023).",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/cosponsors",
               "https://www.congress.gov/bill/118th-congress/house-bill/38/cosponsors"]),
    ]),

    # ---------------- Wes Climer (SC-05, R) ----------------
    ("sc-05-r-placeholder", "SC", "SC-05", [
        claim("wc3", "sc-05-r-placeholder", "sanctity_of_life", 1, True,
              "On his 2026 iVoterGuide candidate profile (running for U.S. House SC-05), Climer stated that 'abortion should only be permitted to preserve the life of the mother' — an essentially abolitionist position that allows no gestational exceptions, no rape/incest carve-outs, and no viability windows beyond the narrowest life-of-mother threshold, aligning with the rubric's call for abolition rather than merely incremental restriction.",
              ["https://ivoterguide.com/candidate/49310/race/21236/election/1229",
               "https://ballotpedia.org/Wes_Climer"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
    """
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
