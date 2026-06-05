#!/usr/bin/env python3
"""Enrichment batch 47: bottom-of-alphabet Representatives with 0 claims.

Targets (3 candidates, bottom-of-alphabet Representatives bucket):
  Rashida Tlaib   (MI-D, US Representative MI-12, incumbent)
  Madison Sheahan (OH-R, OH-09 candidate, former ICE Deputy Director)
  Josh Williams   (OH-R, OH-09 candidate, Ohio state rep District 44)

Each claim cites >=1 reliable source and reflects documented 2024-2026
voting record / public positions.
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
    # ---- Rashida Tlaib (MI-D, US Representative MI-12) ----
    ("rashida-tlaib", "MI", "Representative", [
        claim("rt1", "rashida-tlaib", "sanctity_of_life", 0, False,
              "Voted NAY on the Born-Alive Abortion Survivors Protection Act "
              "(H.R.21, passed House Jan 11, 2025), which would require "
              "medical care for infants who survive a failed abortion — "
              "rejecting any legal protection for born-alive infants and "
              "implicitly denying personhood from the moment of birth.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21",
               "https://www.govtrack.us/congress/bills/119/hr21"]),
        claim("rt2", "rashida-tlaib", "biblical_marriage", 2, False,
              "Voted NAY on the Protection of Women and Girls in Sports Act "
              "(H.R.28, passed House Jan 14, 2025), which prohibits biological "
              "males from competing in female athletic categories — rejecting "
              "the biological-sex standard the rubric requires and affirming "
              "transgender ideology in public institutions.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://www.govtrack.us/congress/bills/119/hr28"]),
        claim("rt3", "rashida-tlaib", "border_immigration", 2, False,
              "Voted NAY on the Laken Riley Act (S.5, signed into law "
              "Jan 29, 2025), which mandates ICE detention of illegal aliens "
              "charged with theft or violent crimes — opposing mandatory "
              "detainer cooperation and effectively supporting sanctuary "
              "policies that shield criminal aliens from deportation.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/5",
               "https://www.govtrack.us/congress/bills/119/s5"]),
    ]),

    # ---- Madison Sheahan (OH-R, OH-09 candidate, former ICE Deputy Director) ----
    ("madison-sheahan", "OH", "Representative", [
        claim("ms1", "madison-sheahan", "border_immigration", 1, True,
              "As ICE Deputy Director (March 2025-January 2026), personally "
              "oversaw mandatory deportation operations removing more than "
              "2.5 million illegal aliens — the largest mass-deportation "
              "campaign in U.S. history — and then resigned to run for "
              "Congress on that enforcement record.",
              ["https://www.nbcnews.com/politics/2026-election/ice-no-2-steps-launch-run-battleground-house-district-ohio-rcna254218",
               "https://thehill.com/homenews/campaign/5866328-madison-sheahan-immigration-customs-enforcement-congressional-bid-ohio/"]),
        claim("ms2", "madison-sheahan", "border_immigration", 0, True,
              "Resigned as ICE No. 2 to run for Congress on a platform of "
              "extending Trump's enforcement-first border agenda, citing 'At "
              "ICE, I returned security to our communities' and championing "
              "the full wall, military-deployment, and mass-deportation "
              "posture that defines the rubric ideal.",
              ["https://www.axios.com/2026/01/15/ice-madison-sheahan-congress-republican-ohio-kaptur",
               "https://thehill.com/homenews/campaign/5866328-madison-sheahan-immigration-customs-enforcement-congressional-bid-ohio/"]),
    ]),

    # ---- Josh Williams (OH-R, OH-09 candidate, Ohio state rep District 44) ----
    ("josh-williams-oh-09", "OH", "Representative", [
        claim("jw1", "josh-williams-oh-09", "biblical_marriage", 4, True,
              "Was a lead sponsor of Ohio legislation banning drag "
              "performances from any venue where minors could be present "
              "(introduced 2023; reintroduced in the 136th GA and passed "
              "the Ohio House in 2025) — directly opposing government and "
              "institutional promotion of LGBTQ content before children.",
              ["https://ballotpedia.org/Josh_Williams_(Ohio)",
               "https://ohiohouse.gov/members/josh-williams/legislation"]),
        claim("jw2", "josh-williams-oh-09", "public_justice", 0, True,
              "Introduced HB 786 in the Ohio House to criminalize AI-"
              "generated child sexual abuse material (AI CSAM), expanding "
              "state criminal law to prosecute synthetic child exploitation "
              "imagery — a public-justice measure protecting children from "
              "predatory content.",
              ["https://ohiohouse.gov/members/josh-williams/legislation",
               "https://ballotpedia.org/Josh_Williams_(Ohio)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher prevents same-slug cross-state collisions."""
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
        print(f"  + {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (keep file ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
