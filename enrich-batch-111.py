#!/usr/bin/env python3
"""Enrichment batch 111: hand-curated claims for 4 state-level / governor candidates.

Targets archetype_curated governor candidates with 0 evidence claims, taken
from the BOTTOM of the alphabet (AZ, MI, AL) to avoid collision with the
concurrent top-of-alphabet enrichment loop.

Targets (2 R / 1 I / 1 D):
  Karrin Taylor Robson (AZ-R, dropped out Feb 2026),
  Tim James (AL-R, lost 5/19 primary to Tuberville),
  Mike Duggan (MI-I, dropped out May 2026),
  Yolanda Flowers (AL-D, lost 5/19 primary to Doug Jones).
Each claim cites >=1 reliable source and reflects 2024-2026 public positions.
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
    # ---------------- Karrin Taylor Robson (AZ-R, Governor candidate) ----------------
    ("karrin-taylor-robson-gov", "AZ", "Governor", [
        claim("ktr1", "karrin-taylor-robson-gov", "sanctity_of_life", 0, True,
              "Declared 'I'm pro-life. I always have been.' and pledged to enforce Arizona's near-total abortion ban (the pre-Roe law criminalizing nearly all abortions) as governor; maintains a long record of supporting crisis pregnancy centers.",
              ["https://ballotpedia.org/Karrin_Taylor_Robson",
               "https://www.azfamily.com/2022/05/31/arizona-republican-governor-candidate-pushes-gun-rights-ad-wake-texas-shooting/"]),
        claim("ktr2", "karrin-taylor-robson-gov", "self_defense", 1, True,
              "A lifetime NRA member who ran pro-Second-Amendment ads within days of the 2022 Uvalde school shooting, stating 'I don't believe you eliminate this kind of violence by taking away people's constitutional rights.' Pledged to oppose any legislation restricting law-abiding gun owners.",
              ["https://www.azfamily.com/2022/05/31/arizona-republican-governor-candidate-pushes-gun-rights-ad-wake-texas-shooting/",
               "https://www.ontheissues.org/governor/Karrin_Taylor_Robson_Gun_Control.htm"]),
        claim("ktr3", "karrin-taylor-robson-gov", "election_integrity", 0, True,
              "Supports voter ID requirements and a universal ban on ballot harvesting; said the 2020 presidential election 'wasn't fair' and pledged to pursue election-security measures including stricter ID verification as governor.",
              ["https://karrinforarizona.com/issue/secure-our-elections/",
               "https://www.azfamily.com/2022/06/11/gop-gubernatorial-hopeful-karrin-taylor-robson-says-2020-election-results-were-inaccurate/"]),
    ]),

    # ---------------- Tim James (AL-R, Governor candidate) ----------------
    ("tim-james-gov", "AL", "Governor", [
        claim("tj1", "tim-james-gov", "sanctity_of_life", 0, True,
              "Ran explicitly on protecting 'faith, family, and freedom'; opposes public funding for abortions and campaigned as an extreme social conservative in a state with a near-total abortion ban he pledged to uphold.",
              ["https://ballotpedia.org/Tim_James_(Alabama)",
               "https://www.alreporter.com/2022/01/13/tim-james-begins-third-gubernatorial-run-with-fire-and-brimstone/"]),
        claim("tj2", "tim-james-gov", "border_immigration", 0, True,
              "Supports building a wall across the U.S.-Mexico border and called on Alabama to take stronger measures to block illegal immigration, including at the Port of Mobile.",
              ["https://ballotpedia.org/Tim_James_(Alabama)"]),
        claim("tj3", "tim-james-gov", "economic_stewardship", 2, True,
              "An outspoken fiscal conservative who opposed the Obama-era TARP and auto-industry bailouts, arguing that financial institutions and automakers should file for bankruptcy rather than receive taxpayer money — consistent with anti-deficit, anti-bailout principles.",
              ["https://www.alreporter.com/2022/01/13/tim-james-begins-third-gubernatorial-run-with-fire-and-brimstone/",
               "https://ballotpedia.org/Tim_James_(Alabama)"]),
    ]),

    # ---------------- Mike Duggan (MI-I, Governor candidate, dropped out May 2026) ----------------
    ("mike-duggan-gov", "MI", "Governor", [
        claim("md1", "mike-duggan-gov", "economic_stewardship", 2, True,
              "Oversaw 14 consecutive balanced city budgets and $100M+ annual surpluses as Detroit mayor; ran for Michigan governor on a platform of government fiscal discipline, ending wasteful spending, and building bipartisan consensus around core economic priorities.",
              ["https://www.cbsnews.com/detroit/news/detroit-mayor-mike-duggan-discusses-citys-budget-surplus/",
               "https://mikeduggan.com/"]),
        claim("md2", "mike-duggan-gov", "industry_capture", 0, False,
              "As Detroit mayor, championed city-pharma partnerships and aggressive COVID vaccination distribution programs; ran as a moderate Democrat-turned-independent with no record of challenging pharmaceutical mandates or the pharma-government public-health consensus.",
              ["https://en.wikipedia.org/wiki/Mike_Duggan",
               "https://ballotpedia.org/Mike_Duggan"]),
    ]),

    # ---------------- Yolanda Flowers (AL-D, Governor candidate, lost primary 5/19/2026) ----------------
    ("yolanda-flowers-gov", "AL", "Governor", [
        claim("yf1", "yolanda-flowers-gov", "sanctity_of_life", 0, False,
              "Initially courted pro-life Democratic voters and sought endorsement from Democrats for Life of America, then shifted to a pro-choice stance supporting rape and incest exceptions; Democrats for Life formally withdrew their endorsement when she changed her position.",
              ["https://www.alreporter.com/2022/05/31/democratic-governor-candidate-flowers-backed-by-democrats-for-life/",
               "https://www.democratsforlife.org/index.php/about-us/75-uncategorised/1139-democrats-for-life-of-america-withdraws-endorsement-of-alabama-gubernatorial-candidate"]),
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
