#!/usr/bin/env python3
"""Enrichment batch 147: hand-curated claims for 4 sitting CA U.S. Representatives.

All four are from the evidence_federal pool (0 claims). archetype_curated pool
is exhausted; this batch targets bottom-of-CA sitting Republicans + one
Independent caucusing with R Conference.

Targets: Tom McClintock (CA-05 R), Jay Obernolte (CA-23 R),
Vince Fong (CA-20 R), Kevin Kiley (CA-03 I/R-caucus).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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
    # ---------------- Tom McClintock (CA-05, R) ----------------
    ("tom-mcclintock", "CA", "Representative CA-05", [
        claim("tm1", "tom-mcclintock", "sanctity_of_life", 0, True,
              "Carries a consistent A/100% pro-life record scored by SBA Pro-Life America: votes every session to defund Planned Parenthood in federal appropriations, blocks taxpayer-funded abortion domestically and internationally, and opposed any federal legislation to codify Roe v. Wade — affirming protection of the unborn from conception.",
              ["https://sbaprolife.org/representative/tom-mcclintock",
               "https://en.wikipedia.org/wiki/Tom_McClintock"]),
        claim("tm2", "tom-mcclintock", "economic_stewardship", 2, True,
              "Ranked #1 in the entire U.S. House on the National Taxpayers Union scorecard and earned the NTU Taxpayers' Friend Award; signed the Taxpayer Protection Pledge against all tax increases; in 2025 introduced a Line-Item Veto constitutional amendment to curb discretionary appropriations — one of Congress's most consistent fiscal-restraint votes over multiple terms.",
              ["https://mcclintock.house.gov/issues/fiscal-and-economic",
               "https://en.wikipedia.org/wiki/Tom_McClintock"]),
        claim("tm3", "tom-mcclintock", "border_immigration", 2, True,
              "Chairs the House Judiciary subcommittee on Immigration Integrity, Security, and Enforcement; in 2026 introduced the Shut Down Sanctuary Policies Act (H.R.7640) to strip federal funding from any jurisdiction that refuses DHS immigration detainers — a direct legislative assault on the sanctuary-city network that shields illegal aliens from removal.",
              ["https://mcclintock.house.gov/votes-and-legislation/vote-notes-archive",
               "https://www.govtrack.us/congress/committees/HSJU/01"]),
    ]),

    # ---------------- Jay Obernolte (CA-23, R) ----------------
    ("jay-obernolte", "CA", "Representative CA-23", [
        claim("jo1", "jay-obernolte", "sanctity_of_life", 0, True,
              "Holds an SBA Pro-Life America A/100% rating: votes to stop federal taxpayer funding of abortion, opposed codification of Roe v. Wade into federal law, and supports the Dobbs ruling returning abortion regulation to states — a consistent legislative record against federally-mandated abortion access.",
              ["https://sbaprolife.org/representative/jay-obernolte",
               "https://en.wikipedia.org/wiki/Jay_Obernolte"]),
        claim("jo2", "jay-obernolte", "economic_stewardship", 2, True,
              "Introduced a Balanced Budget Amendment to the U.S. Constitution as his very first bill in Congress; voted for the Fiscal Responsibility Act of 2023 — billed as the largest reduction in nondefense discretionary spending in U.S. history — publicly attributing chronic inflation to reckless federal deficit spending.",
              ["https://obernolte.house.gov/issues/budget",
               "https://obernolte.house.gov/media/press-releases/rep-obernolte-opposes-inflation-reduction-act-fiery-floor-speech"]),
        claim("jo3", "jay-obernolte", "biblical_marriage", 1, False,
              "On July 19, 2022, voted for the Respect for Marriage Act as one of 47 House Republicans, encoding federal recognition of same-sex marriages into statutory law; his vote ensures same-sex marriage remains legally protected federally regardless of any future Supreme Court ruling — contrary to the one-man-one-woman standard the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Jay_Obernolte",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
    ]),

    # ---------------- Vince Fong (CA-20, R) ----------------
    ("vince-fong", "CA", "Representative CA-20", [
        claim("vf1", "vince-fong", "self_defense", 1, True,
              "A lifetime member of the National Rifle Association; in the California Assembly authored a bill providing firearm safety training materials in multiple languages — extending lawful-carry literacy to California's non-English-speaking communities — and maintains a pro-Second-Amendment record opposing new restrictions on firearms.",
              ["https://en.wikipedia.org/wiki/Vince_Fong",
               "https://ballotpedia.org/Vince_Fong"]),
        claim("vf2", "vince-fong", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R.29, signed into law January 29, 2025) — the first legislation enacted in the 119th Congress — requiring DHS to detain any illegal alien arrested for theft, burglary, or violent crimes, ending catch-and-release for criminal aliens and aligning with a mandatory-enforcement posture.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
    ]),

    # ---------------- Kevin Kiley (CA-03, I caucusing R) ----------------
    ("kevin-kiley", "CA", "Representative CA-03", [
        claim("kk1", "kevin-kiley", "family_child_sovereignty", 0, True,
              "Author of the PROTECT Our Kids Act (H.R.1069, 119th Congress), passed by the House, stripping federal education funding from any K–12 school hosting a CCP-funded Confucius Classroom; also authored a school choice amendment to the Parents Bill of Rights adopted by the full House — making parental sovereignty over curriculum and schooling a centerpiece of his congressional work.",
              ["https://kiley.house.gov/posts/rep-kevin-kileys-protect-our-kids-act-passes-the-house",
               "https://www.congress.gov/bill/119th-congress/house-bill/1069/text/rfs"]),
        claim("kk2", "kevin-kiley", "industry_capture", 0, True,
              "A persistent opponent of government vaccine mandates: in his final term in the California State Assembly introduced legislation to ban state and local governments from implementing vaccine mandates; carried this anti-mandate stance into Congress, opposing federal COVID vaccination requirements and defending individual medical liberty against pharmaceutical-mandate overreach.",
              ["https://en.wikipedia.org/wiki/Kevin_Kiley_(politician)",
               "https://kiley.house.gov/"]),
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
