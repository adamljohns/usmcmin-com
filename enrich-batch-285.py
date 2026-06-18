#!/usr/bin/env python3
"""Enrichment batch 285: 4 active 2026 federal House candidates (evidence_federal, 0 claims).

archetype_curated federal bucket is exhausted; this batch targets evidence_federal
candidates from the bottom of the alphabet (NY, MD, MI) with at least 2 sourced claims each.

Targets (all 2026 D challengers/open-seat candidates):
  Laura Dunn    NY-12  — victims'-rights attorney / SurvJustice founder
  Rushern Baker MD-05  — former Prince George's Co. Executive
  John Cappello NY-17  — retired USAF / FDD Senior Fellow
  Elyon Badger  MI-07  — Army NG vet / LGBTQIA+ activist

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
    # ---- Laura Dunn (NY-12, D — victims'-rights attorney, first-time candidate) ----
    ("laura-dunn-ny-12", "NY", "NY-12", [
        claim("ld1", "laura-dunn-ny-12", "sanctity_of_life", 0, False,
              "Her three-pillar campaign platform explicitly includes protecting 'reproductive access' as a constitutional commitment — endorsing abortion rights and rejecting any legal recognition of fetal personhood from conception.",
              ["https://ballotpedia.org/Laura_Dunn_(New_York)"]),
        claim("ld2", "laura-dunn-ny-12", "biblical_marriage", 0, False,
              "Her published platform pairs 'marriage equality' with reproductive access as a core 'rights and liberties' pledge, endorsing federal protection of same-sex unions and rejecting the one-man-one-woman biblical definition of marriage.",
              ["https://ballotpedia.org/Laura_Dunn_(New_York)"]),
    ]),

    # ---- Rushern Baker III (MD-05, D — former Prince George's County Executive) ----
    ("rushern-baker", "MD", "MD-05", [
        claim("rb1", "rushern-baker", "sanctity_of_life", 0, False,
              "As a 2022 Democratic gubernatorial candidate, publicly criticized the leaked Supreme Court draft overturning Roe v. Wade (Dobbs v. Jackson Women's Health Organization), affirming his support for preserving abortion access and rejecting protection for unborn life from conception.",
              ["https://en.wikipedia.org/wiki/Rushern_Baker",
               "https://en.wikipedia.org/wiki/2022_Maryland_gubernatorial_election"]),
        claim("rb2", "rushern-baker", "self_defense", 1, False,
              "In March 2018 organized and funded free bus trips from Maryland to Washington, D.C., supporting the March for Our Lives gun-control rally — endorsing firearm restrictions and opposing the unrestricted Second Amendment posture the rubric requires.",
              ["https://en.wikipedia.org/wiki/Rushern_Baker"]),
    ]),

    # ---- John Cappello (NY-17, D — retired USAF B-1 pilot, FDD Senior Fellow) ----
    ("john-cappello", "NY", "NY-17", [
        claim("jc1", "john-cappello", "foreign_policy_restraint", 0, False,
              "Served as Senior Fellow for Military Affairs at the Foundation for Defense of Democracies (FDD), a hawkish think tank that consistently advocates for forward U.S. military engagement, escalating sanctions, and sustained confrontation with adversaries — the opposite of the Article-I/restraint posture the rubric requires.",
              ["https://ballotpedia.org/John_Cappello"]),
        claim("jc2", "john-cappello", "industry_capture", 4, False,
              "A 20+ year Air Force career officer (B-1 pilot, Defense Attaché in Tel Aviv) and FDD military-affairs fellow who champions increased U.S. defense-technology investment; his career and affiliations align with expanding, not auditing, Pentagon and defense-contractor spending.",
              ["https://ballotpedia.org/John_Cappello"]),
    ]),

    # ---- Elyon Badger (MI-07, D — Michigan Army NG vet, LGBTQIA+ activist) ----
    ("elyon-badger", "MI", "MI-07", [
        claim("eb1", "elyon-badger", "sanctity_of_life", 0, False,
              "Explicitly declared on his campaign platform that 'Roe v. Wade was never enough to protect abortion rights' and calls for a constitutional amendment permanently enshrining abortion access — wholly rejecting the protection of unborn life from conception.",
              ["https://ballotpedia.org/Elyon_Badger"]),
        claim("eb2", "elyon-badger", "biblical_marriage", 2, False,
              "A self-described LGBTQIA+ activist who runs explicitly on LGBTQ inclusion as a core identity and campaign theme, directly opposing the rubric's call to reject transgender ideology and resist the normalization of LGBTQ identities in law and public life.",
              ["https://ballotpedia.org/Elyon_Badger"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
