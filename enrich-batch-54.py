#!/usr/bin/env python3
"""Enrichment batch 54: hand-curated claims for 4 NY 2026 House candidates.

Bottom-of-alphabet selection: Taylor Darling (NY-04-D, former NY Assembly),
Julie Won (NY-07-D, NYC Council D26), Gian Jones (NY-04-D, businessman),
Claire Valdez (NY-07-D, DSA-endorsed, NY Assembly D37).
2-3 claims each spanning distinct rubric categories, sourced from campaign
websites, NYC Council press releases, state senate press releases, and
credible local news outlets.

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
    # ---------- Taylor Darling (NY-04 D, former NY Assembly District 18) ----------
    ("taylor-darling", "NY", "Representative", [
        claim("td1", "taylor-darling", "sanctity_of_life", 0, False,
              "As a NY Assembly member Darling joined a group of state and local officials to urge repeal of Long Island abortion restrictions, working directly with Planned Parenthood of Greater New York — rejecting any protection of the unborn from conception and actively campaigning to dismantle the remaining statutory limits in New York law.",
              ["https://www.nysenate.gov/newsroom/press-releases/2022/anna-m-kaplan/abortion-restrictions-long-island-uncovered-officials"]),
        claim("td2", "taylor-darling", "border_immigration", 1, False,
              "Darling launched her 2026 congressional primary campaign specifically to unseat Rep. Laura Gillen after Gillen's January 22, 2025 vote to increase DHS funding, which Darling condemned as endorsing the Trump administration's deportation operations — signaling explicit opposition to mandatory immigration enforcement and deportation.",
              ["https://www.cityandstateny.com/politics/2026/02/former-assembly-member-plans-primary-rep-laura-gillen-over-ice-funding-vote/411448/"]),
    ]),

    # ---------- Julie Won (NY-07 D, NYC Council District 26) ----------
    ("julie-won", "NY", "Representative", [
        claim("jw1", "julie-won", "border_immigration", 2, False,
              "Won's 2026 congressional platform explicitly pledges to 'fight attacks on our sanctuary City, create pathways to citizenship, protect immigrant workers from exploitation, end family separation — and abolish ICE,' directly opposing any enforcement-centered or anti-sanctuary immigration policy.",
              ["https://www.juliewon.com/"]),
        claim("jw2", "julie-won", "biblical_marriage", 4, False,
              "Responding to the LGBTQ Jim Owles Liberal Democratic Club's 2025 questionnaire, Won pledged she will 'gladly continue funding, supporting, and hosting Drag Story Hours in her district's libraries' — explicitly committing to promote LGBTQ content programming in public libraries and spaces.",
              ["https://jimowles.org/news/candidate-answers-to-joldc-julie-won-for-city-council-district-26-2025"]),
        claim("jw3", "julie-won", "sanctity_of_life", 0, False,
              "Won organized an abortion rights rally in Long Island City when the Supreme Court's Dobbs draft opinion leaked (May 2022) and in July 2022 voted as a NYC Council member for the historic NYC Abortion Rights Act — affirming unrestricted abortion access and rejecting any personhood-from-conception standard.",
              ["https://qns.com/2022/05/queens-abortion-rights-rally-long-island-city/",
               "https://council.nyc.gov/press/2022/07/14/2222/"]),
    ]),

    # ---------- Gian Jones (NY-04 D, businessman, moderate Democrat) ----------
    ("gian-jones", "NY", "Representative", [
        claim("gj1", "gian-jones", "border_immigration", 0, False,
              "Jones's platform calls for 'securing the border while strengthening legal immigration so the system is fair, orderly, and humane' — framing enforcement around managed migration and legal pathways rather than wall construction or military deployment, falling short of the rubric's hard-enforcement standard.",
              ["https://www.gianforcongress.com/"]),
        claim("gj2", "gian-jones", "economic_stewardship", 2, False,
              "Jones's signature economic priority is permanently restoring the full SALT (state and local tax) deduction — a revenue-reducing tax expenditure that widens the federal deficit by hundreds of billions over a decade — inconsistent with the rubric's anti-deficit and balanced-budget standard.",
              ["https://www.gianforcongress.com/"]),
    ]),

    # ---------- Claire Valdez (NY-07 D, DSA-endorsed, NY Assembly District 37) ----------
    ("claire-valdez", "NY", "Representative", [
        claim("cv1", "claire-valdez", "border_immigration", 1, False,
              "DSA-endorsed and Justice Democrats–backed, Valdez has pledged in her 2026 congressional campaign to 'dismantle and abolish ICE' and fight for 'real immigration reform that legalizes the status of millions of immigrant Americans' — a direct rejection of mandatory deportation and enforcement-first border policy.",
              ["https://clairevaldezforcongress.com/issues",
               "https://socialists.nyc/press-releases/nyc-dsa-endorses-claire-valdez-for-congress-in-ny-7-and-samantha-kattan-for-assembly-district-37/"]),
        claim("cv2", "claire-valdez", "sanctity_of_life", 0, False,
              "Valdez holds that 'New York must do more to protect and expand not only the right to abortion care but increase access to comprehensive reproductive and sexual health care overall,' rejecting any protection of unborn life from conception and calling for expanded public abortion funding and access.",
              ["https://clairevaldezforcongress.com/issues"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to avoid same-slug collisions across states."""
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
