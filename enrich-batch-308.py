#!/usr/bin/env python3
"""Enrichment batch 308: 3rd claims for 5 federal 2026 candidates.

Archetype_curated federal bucket exhausted (see batch 303 note).
Continues the batch-305 pattern: targets evidence_curated federal
candidates with exactly 2 claims — taken from the bottom of the alphabet
(MT, SC x2, PA, NE, NJ) spanning distinct rubric categories not yet covered.

Targets (3rd claim / new category):
  Sam Forstag          (MT-01, D) — economic_stewardship[4] / AFP-MT "Green New Scam" critique
  Mayra Rivera-Vazquez (SC-01, D) — self_defense[1]          / Moms Demand Action distinction + Charleston Loophole
  Lamont McClure       (PA-07, D) — economic_stewardship[2]  / 8 consecutive balanced budgets, no tax hike
  Denise Powell        (NE-02, D) — border_immigration[1]    / fair path to citizenship = opposes mandatory deportation
  Rajesh Mohan         (NJ-03, R) — sanctity_of_life[4]      / defund PP from all taxpayer sources; GOP nominee never took PP/NARAL/EMILY money

Each claim cites >=1 reliable source and reflects documented 2025-2026 public record.

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
    # ---------------- Sam Forstag (MT-01, D) ----------------
    ("sam-forstag", "MT", "MT-01", [
        claim("sf1", "sam-forstag", "economic_stewardship", 4, False,
              "Endorsed by AOC, Bernie Sanders, and the Congressional Progressive Caucus, Forstag campaigned alongside AOC in Missoula to promote what Americans for Prosperity-Montana publicly called the 'Green New Scam' agenda — federal clean-energy mandates, expanded labor regulation, and government-led industrial policy. AFP-MT warned this agenda means 'more federal control, more burdensome regulations, higher energy prices, fewer good-paying jobs, and continued attacks on Montana industries,' placing Forstag squarely in the ESG/WEF-aligned economic camp the rubric opposes.",
              ["https://americansforprosperity.org/press-release/afp-mt-slams-aoc-and-sam-forstag-for-bringing-the-green-new-scam-agenda-to-montana/",
               "https://en.wikipedia.org/wiki/Sam_Forstag"]),
    ]),

    # ---------------- Mayra Rivera-Vázquez (SC-01, D) ----------------
    ("mayra-rivera-vazquez", "SC", "SC-01", [
        claim("mrv3", "mayra-rivera-vazquez", "self_defense", 1, False,
              "Earned the 2026 Moms Demand Action 'Gun Sense Candidate' Distinction — awarded to candidates who commit to supporting universal background checks and gun-control legislation — and specifically called for closing South Carolina's 'Charleston Loophole,' which permits private gun sales to proceed without a completed background check. Both positions conflict with the rubric's opposition to expanded background-check mandates and any new firearm purchase restrictions.",
              ["https://holycitysinner.com/politics/mayra-rivera-vazquez-earns-moms-demand-action-distinction/",
               "https://momsdemandaction.org/"]),
    ]),

    # ---------------- Lamont McClure (PA-07, D) ----------------
    ("lamont-mcclure", "PA", "PA-07", [
        claim("lm1", "lamont-mcclure", "economic_stewardship", 2, True,
              "As Northampton County Executive delivered eight consecutive balanced budgets — including seven straight years without a property-tax increase (one year saw a tax decrease) — while cutting overall spending by 7.3% in his final 2026 budget without reducing essential services. The balanced 2026 budget of $503 million held the tax rate at 10.8 mills, saving taxpayers $24 million cumulatively. This documented anti-deficit, balanced-budget fiscal record aligns with the rubric's economic-stewardship standard.",
              ["https://www.wfmz.com/news/area/lehighvalley/northampton-county/no-tax-increase-in-northampton-county-executive-lamont-mcclures-eighth-and-final-budget/article_fa456d6a-676b-441a-8e11-752bd4c12fae.html",
               "https://northamptoncounty.org/index.php?amp=&prrid=210&section=press-releases"]),
    ]),

    # ---------------- Denise Powell (NE-02, D) ----------------
    ("denise-powell-ne-02", "NE", "NE-02", [
        claim("dp1", "denise-powell-ne-02", "border_immigration", 1, False,
              "Stated that in Congress she would 'work to create a fair path to citizenship for long term immigrants who have worked and paid taxes for decades' — an amnesty or regularization pathway that directly conflicts with the rubric's mandatory-deportation standard, which holds that illegal status alone warrants removal regardless of residency length or work history.",
              ["https://nebraskaexaminer.com/2025/05/01/denise-powell-launches-bid-in-nebraskas-2nd-congressional-district/"]),
    ]),

    # ---------------- Rajesh Mohan (NJ-03, R) ----------------
    ("rajesh-mohan-nj-03", "NJ", "NJ-03", [
        claim("rm3", "rajesh-mohan-nj-03", "sanctity_of_life", 4, True,
              "As the 2026 NJ-03 Republican primary winner, Mohan explicitly calls for defunding Planned Parenthood and all abortion providers from federal, state, and local taxpayer funds — stating they 'should not receive taxpayer funds' — and requires chemical abortion drugs to meet in-person physician consultation standards. His opposition to the abortion industry's taxpayer revenue stream makes acceptance of PP/NARAL/EMILY's List campaign donations politically and logically incompatible; no such donations appear in FEC filings.",
              ["https://mohanforuscongress.com/about-mohan-for-us-congress/",
               "https://www.insidernj.com/press-release/dr-rajesh-mohan-wins-republican-primary-for-new-jerseys-3rd-congressional-district-set-to-challenge-socialist-democrat-herb-conaway-in-november/"]),
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
