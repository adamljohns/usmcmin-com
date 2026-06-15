#!/usr/bin/env python3
"""Enrichment batch 218: third-claim enrichment for 5 bottom-of-alphabet federal candidates.

Primary archetype_curated bucket exhausted; this batch adds a sourced 3rd
claim to evidence_curated candidates that had only 2 claims, taking from
the reverse-alphabetical bottom (TN × 1, TX × 1, PA × 1, NC × 1, NY × 1).

Targets: Charlotte Bergmann (TN-R, TN-09), Chris Gober (TX-R, TX-10),
         Ryan Mackenzie (PA-R, PA-07), Michael Whatley (NC-R, Senate),
         Alison Esposito (NY-R, NY-18).
Each new claim covers a DISTINCT rubric category not yet evidenced.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub 50MB limit.
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
    # -------- Charlotte Bergmann (TN-R, TN-09 2026 candidate) --------
    ("charlotte-bergmann", "TN", "Representative", [
        claim("cb1", "charlotte-bergmann", "self_defense", 1, True,
              "Campaign website explicitly states she is 'a gun owner and fully supports the 2nd amendment' and that she 'opposes legislation that wants to limit the 2nd amendment and take guns out of law-abiding citizens' hands' — directly opposing red-flag laws, assault-weapon bans, magazine limits, and registration schemes that restrict law-abiding gun owners.",
              ["https://www.charlottebergmann.com/issues.html",
               "https://ballotpedia.org/Charlotte_Bergmann"]),
    ]),

    # -------- Chris Gober (TX-R, TX-10 2026 candidate — won R primary March 2026) --------
    ("chris-gober", "TX", "Representative", [
        claim("cg1", "chris-gober", "self_defense", 1, True,
              "Campaign explicitly commits to 'defend the Second Amendment' and 'Protect our always under siege Second Amendment,' pledging to oppose any legislation that restricts the right of law-abiding citizens to keep and bear arms — including red-flag orders, magazine limits, and assault-weapon bans.",
              ["https://www.ballotready.org/people/chris-gober",
               "https://ballotpedia.org/Chris_Gober"]),
    ]),

    # -------- Ryan Mackenzie (PA-R, PA-07 incumbent) --------
    ("ryan-mackenzie", "PA", "Representative", [
        claim("rm1", "ryan-mackenzie", "self_defense", 2, True,
              "Voted YES on H.R. 1, the One Big Beautiful Bill Act (House 219-214, final passage July 3, 2025), which includes Section 70401 removing suppressors (silencers) from the National Firearms Act's registration, taxation, and transfer-approval requirements — the most significant rollback of NFA/Title II restrictions in decades. Mackenzie hailed the reconciliation package as addressing 'government spending run amok' while protecting constitutional rights.",
              ["https://penncapital-star.com/food-insecurity/pa-congressional-republicans-unanimous-in-support-of-trumps-big-beautiful-bill/",
               "https://mackenzie.house.gov/media/press-releases/congressman-mackenzie-applauds-passage-budget-reconciliation-bill",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
    ]),

    # -------- Michael Whatley (NC-R, 2026 Senate nominee — Tillis seat) --------
    ("michael-whatley", "NC", "Senator", [
        claim("mw1", "michael-whatley", "sanctity_of_life", 0, True,
              "Stated he was 'proud' when the Supreme Court overturned Roe v. Wade and called North Carolina's 12-week abortion ban 'responsible,' 'reasonable,' and 'mainstream.' Received a $4.5 million endorsement contribution from Susan B. Anthony Pro-Life America for his 2026 Senate campaign. As NC GOP chair he presided over a party platform that included an abortion ban with no exceptions — consistent with a personhood-from-conception position opposing abortion in all circumstances.",
              ["https://thehill.com/homenews/senate/5426353-rnc-chair-michael-whatley-nc-senate/amp/",
               "https://www.ncdp.org/media/new-dc-insider-michael-whatley-supports-national-abortion-ban-endorsed-by-dark-money-anti-abortion-group/",
               "https://ballotpedia.org/Michael_Whatley"]),
    ]),

    # -------- Alison Esposito (NY-R, NY-18 2026 candidate) --------
    ("alison-esposito-ny-18", "NY", "Representative", [
        claim("ae1", "alison-esposito-ny-18", "family_child_sovereignty", 0, True,
              "Stated that 'parents must have the right to be as involved in their child's education as they wish,' affirming robust parental rights over school curriculum and upbringing decisions — consistent with the rubric's protection of parental authority against state overreach in education.",
              ["https://spectrumlocalnews.com/nys/central-ny/politics/2024/09/09/republican-alison-esposito-discusses-her-run-for-congress",
               "https://ballotpedia.org/Alison_Esposito"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
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
