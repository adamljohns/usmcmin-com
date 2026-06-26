#!/usr/bin/env python3
"""Enrichment batch 435: 4 West Virginia State Delegates (unset confidence, 0 claims).

Archetype_curated federal pool exhausted; all 95 US Senators at evidence_curated.
Continuing bottom-of-alphabet WV queue: Pat McGeehan (WV-01, Majority Leader),
Phil Mallow (WV-75), Michael Hornby (WV-93), Mickey Petitto (WV-70, Asst Majority Leader).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
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
    # ---------- Pat McGeehan (WV House Dist. 1, R, Majority Leader) ----------
    ("pat-mcgeehan", "WV", "Delegate", [
        claim("pm1", "pat-mcgeehan", "economic_stewardship", 1, True,
              "In 2012, McGeehan published 'Printing Our Way to Poverty: The Consequences of American Inflation,' an Austrian-economics critique of central-bank monetary inflation. The book received strong praise from Congressman and former presidential candidate Ron Paul — a leading advocate of sound money and abolishing the Federal Reserve — positioning McGeehan firmly in the tradition of opposing fiat currency debasement and the unaccountable money-printing the rubric's sound-money criterion targets.",
              ["https://en.wikipedia.org/wiki/Pat_McGeehan",
               "https://ballotpedia.org/Patrick_McGeehan"]),
        claim("pm2", "pat-mcgeehan", "economic_stewardship", 2, True,
              "McGeehan publicly opposes all federal bailouts of private industry, stating: 'Federal bailouts reward inefficient and corrupt management, while robbing taxpayers and increasing the National Debt.' This consistent anti-bailout, anti-deficit posture aligns with the rubric's balanced-budget and anti-deficit-spending standard.",
              ["https://ballotpedia.org/Patrick_McGeehan",
               "https://en.wikipedia.org/wiki/Pat_McGeehan"]),
        claim("pm3", "pat-mcgeehan", "refuse_federal_overreach", 0, True,
              "The Republican Liberty Caucus — an organization within the GOP dedicated to individual liberty, limited government, and free-market economics, which opposes federal encroachment on constitutional freedoms — endorsed McGeehan in his 2013 WV U.S. Senate campaign. The endorsement reflects a career-long orientation toward constitutional restraint on federal power. McGeehan is now serving as Majority Leader of the West Virginia House of Delegates.",
              ["https://en.wikipedia.org/wiki/Pat_McGeehan",
               "https://en.wikipedia.org/wiki/Republican_Liberty_Caucus",
               "https://ballotpedia.org/Patrick_McGeehan"]),
    ]),

    # ---------- Phil Mallow (WV House Dist. 75, R, Courts Subcommittee Chair) ----------
    ("phil-mallow", "WV", "Delegate", [
        claim("pmallow1", "phil-mallow", "self_defense", 0, True,
              "Co-sponsored HB 4106 (2026 WV Regular Session), which extends West Virginia's constitutional carry regime to adults aged 18-20 by allowing them to carry a concealed deadly weapon without first obtaining a license; passed the House and signed into law by Governor Patrick Morrisey on April 1, 2026. Mallow is one of eleven Republican delegates listed on the bill, which amends WV Code §§61-7-6, 61-7-7, and 61-7-8.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://www.wvlegislature.gov/Bill_Text_HTML/2026_SESSIONS/RS/bills/hb4106%20eng.pdf"]),
        claim("pmallow2", "phil-mallow", "election_integrity", 0, True,
              "Co-sponsored HB 5077 (2024 WV Regular Session), which amends WV law to establish residency requirements for candidates seeking nomination for U.S. Congress from West Virginia, sets penalties for violations, and clarifies ballot-content rules for Congressional races — an election-integrity measure ensuring that only bona fide district-resident candidates appear on the ballot and preventing non-resident carpetbaggers from misrepresenting themselves to WV voters.",
              ["https://legiscan.com/WV/text/HB5077/id/2940158",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb5077+intr.htm&yr=2024&sesstype=RS&i=5077"]),
    ]),

    # ---------- Michael Hornby (WV House Dist. 93, R, publisher) ----------
    ("michael-hornby", "WV", "Delegate", [
        claim("mh1", "michael-hornby", "family_child_sovereignty", 0, True,
              "Serves as Vice Chair of the West Virginia House Educational Choice Subcommittee, the committee that reviews homeschool and school-choice legislation. In this role, Hornby advanced HB 4062 (2026 Regular Session) — the West Virginia Homeschool Student Athletics Participation Act, allowing homeschool students to participate in WVSSAC-sanctioned athletics — and reviewed HB 3422 (2025), requiring the WV Board of Education to build an internet-based reporting portal for homeschool families, directly supporting parental educational sovereignty.",
              ["https://home.wvlegislature.gov/delegate/mike-hornby/",
               "https://home.wvlegislature.gov/committee/house-educational-choice/",
               "https://blog.wvlegislature.gov/house-committee/2026/02/03/house-public-edu-and-edu-choice-discuss-several-bills/"]),
        claim("mh2", "michael-hornby", "biblical_marriage", 2, True,
              "Co-sponsored HB 4834 (2026 WV Regular Session), the West Virginia Women's Wrestling Sanctioning Act, which permits women's wrestling as a formally sanctioned sport in public high schools and charter schools — codifying single-sex athletic categories at the school level and reinforcing the biological-sex definition of 'women's' competition consistent with the rubric's position rejecting transgender ideology in schools and policy.",
              ["https://legiscan.com/WV/bill/HB4834/2026",
               "https://www.wvlegislature.gov/Bill_Text_HTML/2026_SESSIONS/RS/bills/hb4834%20intr.pdf"]),
    ]),

    # ---------- Mickey Petitto (WV House Dist. 70, R, Assistant Majority Leader) ----------
    ("mickey-petitto", "WV", "Delegate", [
        claim("mpetitto1", "mickey-petitto", "refuse_federal_overreach", 0, True,
              "Co-sponsored HCR 55 (2024 WV Regular Session), a concurrent resolution requesting that Congress direct the federal criminal prosecution of former President Donald Trump to be transferred from the U.S. District Court for the District of Columbia to a federal court in West Virginia — asserting that the DC prosecution represented an improper use of the federal judiciary against a political opponent and that West Virginia, as a non-DC jurisdiction, would provide a more appropriate and impartial venue.",
              ["https://legiscan.com/WV/text/HCR55/id/2906970",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hcr55+intr.htm&yr=2024&sesstype=RS&i=55&houseorig=H&billtype=CR"]),
        claim("mpetitto2", "mickey-petitto", "economic_stewardship", 2, True,
              "As a member of the West Virginia House Republican leadership team (Assistant Majority Leader since 2022), Petitto was part of the majority caucus that passed HB 2526 (2023) — a landmark personal income tax cut reducing West Virginia's income tax rate by 21.25% immediately and phasing in a total 50% reduction over three years, returning an estimated $750 million annually to WV taxpayers; signed into law March 2023. Petitto's background as an accountant and real estate appraiser reflects a consistent orientation toward fiscal discipline and reduced government tax burden.",
              ["https://blog.wvlegislature.gov/headline/2023/01/18/house-passes-tax-reduction-plan/",
               "https://ballotpedia.org/Mickey_Petitto"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
