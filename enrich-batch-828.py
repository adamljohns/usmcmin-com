#!/usr/bin/env python3
"""Enrichment batch 828: 5 Wisconsin State Assembly Democrats.

Targets archetype_party_default Assembly members with 0 claims from the
bottom of the alphabet (WI). All five co-authored Wisconsin AB 355 (abortion
rights, 2025) and AB 324 (handgun waiting period, 2025), directly opposing
the RESOLUTE Citizen rubric on sanctity of life and self-defense. Joers and
Stroud additionally co-authored AB 1077 (firearms dealer regulations, 2026)
and AB 314 (gender-neutral marriage and parentage, 2025).

Targets: Angelina Cruz (WI-62), Angela Stroud (WI-73), Andrew Hysell (WI-48),
Amaad Rivera-Wagner (WI-90), Alex Joers (WI-81).
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
    # ------------- Angelina Cruz (WI-62, D) -------------
    ("angelina-cruz-wi-62", "WI", "Assembly", [
        claim("ac1", "angelina-cruz-wi-62", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), which declares abortion a fundamental "
              "right of bodily autonomy at any stage of pregnancy as long as a provider "
              "deems it necessary — with no recognition of the unborn child's personhood "
              "from conception, directly opposing the rubric's life-at-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("ac2", "angelina-cruz-wi-62", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), imposing a mandatory waiting period "
              "for the purchase of handguns — a government-imposed delay on the individual "
              "right to lawful firearm acquisition, in direct conflict with the rubric's "
              "opposition to firearm purchase restrictions.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324"]),
    ]),

    # ------------- Angela Stroud (WI-73, D) -------------
    ("angela-stroud-wi-73", "WI", "Assembly", [
        claim("as1", "angela-stroud-wi-73", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), declaring abortion a fundamental right "
              "of bodily autonomy at every stage of pregnancy with no life-at-conception "
              "exception — directly rejecting the rubric's personhood-from-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("as2", "angela-stroud-wi-73", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), mandating a waiting period for handgun "
              "purchases, and co-authored AB 1077 (2026), imposing permit and surveillance "
              "requirements on firearms dealers — both opposing the rubric's commitment to "
              "unrestricted constitutional carry and anti-restriction standards.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB1077.pdf"]),
        claim("as3", "angela-stroud-wi-73", "biblical_marriage", 1, False,
              "Co-authored Wisconsin AB 314 (2025), which amends state statutes to adopt "
              "gender-neutral marriage and parentage terminology, aligning Wisconsin law "
              "with Obergefell v. Hodges same-sex marriage recognition and extending "
              "presumptions of parentage to same-sex couples — directly opposing the rubric's "
              "one-man-one-woman and anti-same-sex-marriage standards.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab314",
               "https://legiscan.com/WI/bill/AB314/2025"]),
    ]),

    # ------------- Andrew Hysell (WI-48, D) -------------
    ("andrew-hysell-wi-48", "WI", "Assembly", [
        claim("ah1", "andrew-hysell-wi-48", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), which would establish abortion as a "
              "fundamental right of bodily autonomy throughout pregnancy, with no "
              "personhood-from-conception standard — directly opposing the rubric's "
              "life-at-conception protection.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("ah2", "andrew-hysell-wi-48", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), requiring a mandatory waiting period "
              "before the purchase of a handgun — in direct conflict with the rubric's "
              "opposition to government-imposed delays and restrictions on the lawful "
              "exercise of Second Amendment rights.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324"]),
    ]),

    # ------------- Amaad Rivera-Wagner (WI-90, D) -------------
    ("amaad-rivera-wagner-wi-90", "WI", "Assembly", [
        claim("arw1", "amaad-rivera-wagner-wi-90", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), establishing abortion as a fundamental "
              "right of bodily autonomy at any stage of pregnancy based solely on a "
              "provider's professional judgment, with no recognition of unborn personhood — "
              "directly rejecting the rubric's life-at-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("arw2", "amaad-rivera-wagner-wi-90", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), imposing a mandatory waiting period "
              "for handgun purchases — a restriction the rubric opposes as a "
              "government-imposed delay on the individual right to lawful firearm acquisition "
              "under the Second Amendment.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324"]),
    ]),

    # ------------- Alex Joers (WI-81, D) -------------
    ("alex-joers-wi-81", "WI", "Assembly", [
        claim("aj1", "alex-joers-wi-81", "sanctity_of_life", 0, False,
              "Co-authored Wisconsin AB 355 (2025), which declares abortion a fundamental "
              "right of bodily autonomy throughout pregnancy with no life-at-conception "
              "exception — directly opposing the rubric's personhood-from-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf"]),
        claim("aj2", "alex-joers-wi-81", "self_defense", 1, False,
              "Co-authored Wisconsin AB 324 (2025), a mandatory handgun waiting period, "
              "and AB 1077 (2026), a comprehensive firearms-dealer permit and surveillance "
              "package — both opposing the rubric's constitutional-carry and "
              "anti-restriction standards.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab324",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB1077.pdf"]),
        claim("aj3", "alex-joers-wi-81", "biblical_marriage", 1, False,
              "Co-authored Wisconsin AB 314 (2025), adopting gender-neutral marriage and "
              "parentage terminology to align state law with Obergefell v. Hodges same-sex "
              "marriage rights, and voted against Republican anti-transgender bills in "
              "March 2025, stating he was 'devastated' by legislative efforts to 'deny the "
              "existence and lived experiences of LGBTQ+ Wisconsinites' — directly opposing "
              "the rubric's one-man-one-woman and anti-same-sex-marriage standards.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab314",
               "https://www.wispolitics.com/2025/rep-joers-votes-no-on-anti-trans-bills/"]),
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
