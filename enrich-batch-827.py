#!/usr/bin/env python3
"""Enrichment batch 827: 5 Wisconsin State Assembly Democrats.

Targets archetype_party_default Assembly members with 0 claims from the
bottom of the alphabet (WI). All five co-authored 2025 bills that directly
conflict with the RESOLUTE Citizen rubric's sanctity-of-life and
self-defense standards.

Targets: Christian Phelps (WI-93), Brienne Brown (WI-43),
Ben DeSmidt (WI-65), Ann Roe (WI-44), Angelito Tenorio (WI-14).
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
    # ------------- Christian Phelps (WI-93, D) -------------
    ("christian-phelps-wi-93", "WI", "Assembly", [
        claim("cp1", "christian-phelps-wi-93", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), which declares abortion a fundamental "
              "right of bodily autonomy and prohibits the state from restricting abortion "
              "at any stage of pregnancy as long as a provider deems it necessary — "
              "directly rejecting life-at-conception protection.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("cp2", "christian-phelps-wi-93", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), imposing a mandatory waiting period "
              "for the purchase of handguns — a restriction the rubric opposes as a "
              "government-imposed delay on the individual right to lawful firearm acquisition.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324"]),
    ]),

    # ------------- Brienne Brown (WI-43, D) -------------
    ("brienne-brown-wi-43", "WI", "Assembly", [
        claim("bb1", "brienne-brown-wi-43", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), declaring abortion a fundamental right "
              "of bodily autonomy at any stage of pregnancy, with no recognition of the "
              "unborn child's personhood — directly opposing the rubric's life-from-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("bb2", "brienne-brown-wi-43", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), mandating a waiting period for handgun "
              "purchases, and co-authored AB 1077 (2025), a comprehensive firearms-safety "
              "package expanding firearm regulations — both directly opposing the rubric's "
              "commitment to unrestricted constitutional carry and anti-restriction standards.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab1077"]),
    ]),

    # ------------- Ben DeSmidt (WI-65, D) -------------
    ("ben-desmidt-wi-65", "WI", "Assembly", [
        claim("bd1", "ben-desmidt-wi-65", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), which would enshrine abortion access "
              "as a fundamental right of bodily autonomy at every stage of pregnancy "
              "with no life-at-conception exception — opposing the rubric's standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("bd2", "ben-desmidt-wi-65", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), imposing a mandatory waiting period "
              "for handgun purchases — in conflict with the rubric's opposition to "
              "government-imposed delays and restrictions on lawful firearm acquisition.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324"]),
    ]),

    # ------------- Ann Roe (WI-44, D) -------------
    ("ann-roe-wi-44", "WI", "Assembly", [
        claim("ar1", "ann-roe-wi-44", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), declaring abortion a fundamental right "
              "at any point in pregnancy based solely on the medical provider's judgment, "
              "with no recognition of personhood from conception — rejecting the rubric's "
              "life-at-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("ar2", "ann-roe-wi-44", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), mandating a waiting period for handgun "
              "purchases, and co-authored AB 1077 (2025), a comprehensive firearms-regulation "
              "package — both directly opposing the rubric's defense of unrestricted Second "
              "Amendment rights against government-imposed delays and new restrictions.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab1077"]),
    ]),

    # ------------- Angelito Tenorio (WI-14, D) -------------
    ("angelito-tenorio-wi-14", "WI", "Assembly", [
        claim("at1", "angelito-tenorio-wi-14", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), establishing abortion as a fundamental "
              "right of bodily autonomy throughout pregnancy with no personhood-from-conception "
              "standard — directly rejecting the rubric's sanctity-of-life position.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("at2", "angelito-tenorio-wi-14", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), a mandatory handgun waiting period, "
              "and AB 1077 (2025), a comprehensive firearms-safety package — both opposing "
              "the rubric's constitutional-carry and anti-restriction standards.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab1077"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher: returns the candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record."""
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master to keep scorecard.json ~35-36MB.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
