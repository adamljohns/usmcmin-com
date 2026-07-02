#!/usr/bin/env python3
"""Enrichment batch 524: 5 claims across 4 candidates (bottom-of-alphabet states).

archetype_curated + 0-claim buckets fully exhausted. Targets evidence_curated
candidates from WA, WI, and WV with 3 existing claims, adding 1-2 distinct-
category claims each to fill uncovered rubric dimensions.

Targets (bottom-of-alphabet states WA/WI/WV):
  Carmen Goers   (WA-08 R 2024 nominee)  — biblical_marriage, family_child_sovereignty
  Paul Wassgren  (WI-07 R suspended)     — economic_stewardship
  Jack Woodrum   (WV state senator R)    — election_integrity
  Bill Hamilton  (WV state senator R)    — economic_stewardship

Sources: ivoterguide.com, paulwassgren.com, ballotpedia.org, wvmetronews.com,
         wtrf.com, wvdn.com, blog.wvlegislature.gov.

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
    # ---------------- Carmen Goers (WA-08 R, 2024 nominee) ----------------
    ("carmen-goers", "WA", "Representative", [
        claim("cg4", "carmen-goers", "biblical_marriage", 0, True,
              "Goers states on her 2024 iVoterGuide candidate profile: 'Marriage is a God-ordained, "
              "sacred and legal union of one man and one woman. No government has the authority to "
              "alter this definition.' This directly affirms the one-man-one-woman marriage standard "
              "at the core of the rubric's biblical marriage criterion.",
              ["https://ivoterguide.com/candidate/68720/race/2695/election/1247",
               "https://ballotpedia.org/Carmen_Goers"]),
        claim("cg5", "carmen-goers", "family_child_sovereignty", 0, True,
              "Goers states children 'must be protected from abuse, including gender ideology, "
              "grooming, and bodily mutilation.' She endorses broad school choice — vouchers, tax "
              "credits, charter, private, and home schools — and advocates eliminating the U.S. "
              "Department of Education to return education control to states and local communities. "
              "These positions align with the rubric's parental rights and anti-government-overreach-"
              "into-child-rearing standard.",
              ["https://ivoterguide.com/candidate/68720/race/2695/election/1247"]),
    ]),

    # ---------------- Paul Wassgren (WI-07 R, campaign suspended April 2026) ----------------
    ("paul-wassgren", "WI", "Representative", [
        claim("pw4", "paul-wassgren", "economic_stewardship", 2, True,
              "During Trump's first term, Wassgren was described as 'one of the country's leading "
              "advocates for Opportunity Zones' — the 2017 Tax Cuts and Jobs Act program that "
              "channels private capital into economically distressed communities as a market-based "
              "alternative to deficit-funded government spending programs. His promotion of this "
              "model in his 2026 congressional run reflects a fiscal philosophy consistent with "
              "the rubric's anti-deficit, private-sector-first economic stewardship standard.",
              ["https://paulwassgren.com/meet-paul/",
               "https://ballotpedia.org/Paul_Wassgren"]),
    ]),

    # ---------------- Jack Woodrum (WV State Senator, R-Summers/District 10) ----------------
    ("jack-woodrum", "WV", "Senator", [
        claim("jw3", "jack-woodrum", "election_integrity", 0, True,
              "Sponsored West Virginia SB 490 (2025), which permanently prohibits ranked-choice "
              "voting and instant-runoff voting in all state, county, and local elections — "
              "protecting single-vote transparent election processes from algorithmic manipulation. "
              "The bill passed the full Senate 31-2 and was signed into law by Governor Morrisey "
              "on March 18, 2025.",
              ["https://wvmetronews.com/2025/03/04/ranked-choice-voting-would-be-banned-under-bill-passed-by-west-virginia-senate/",
               "https://www.wtrf.com/west-virginia/west-virginia-governor-signs-bill-into-law-to-ban-ranked-choice-voting/"]),
    ]),

    # ---------------- Bill Hamilton (WV State Senator, R-District 11) ----------------
    ("bill-hamilton", "WV", "Senator", [
        claim("bh3", "bill-hamilton", "economic_stewardship", 2, True,
              "Senator Hamilton, serving in the WV legislature continuously since 2003, campaigns "
              "in 2026 on his record of passing 'the largest tax cut in state history' — WV's "
              "landmark income tax reductions: a 21.25% cut signed in March 2023, a further 2% "
              "cut in October 2024, and an additional 5% cut in 2026, collectively returning more "
              "than $626 million to West Virginia taxpayers. This sustained fiscal conservatism "
              "directly aligns with the rubric's anti-deficit/balanced-budget standard.",
              ["https://wvdn.com/172344/",
               "https://blog.wvlegislature.gov/headline/2023/02/08/senate-passes-income-tax-cut-plan"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
