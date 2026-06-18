#!/usr/bin/env python3
"""Enrichment batch 282: 5 active/recent 2026 federal candidates from the bottom of the alphabet.

Bottom-of-alphabet pull (NE, MT, NY, ME):
  Crystal Rhoades (NE-02, D, LOST May 12 primary),
  Russ Cleveland (MT-01, D, LOST June 2 primary),
  Stuart Amoriell (NY-21, D, active June 23 primary),
  Paige Loud (ME-02, D, June 9 primary),
  Vichal Kumar (NY-07, D, active June 23 primary).
Claims sourced from candidate websites, ballotpedia.org, mainepublic.org,
northcountrypublicradio.org, crystal4congress.com, russellcleveland.org,
nebraskavoterguide.com, ny1.com, qns.com (2025-2026).
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
    # ------------ Crystal Rhoades (NE-02, D, LOST May 12 primary) ------------
    ("crystal-rhoades", "NE", "Representative", [
        claim("cr1", "crystal-rhoades", "sanctity_of_life", 0, False,
              "Explicitly advocates for abortion access as a personal freedom, stating: 'Women must have the right to choose. Americans should have the freedom to make medical decisions for themselves. We have a right to demand privacy from the government.' Rejects any life-at-conception or personhood-from-fertilization standard.",
              ["https://crystal4congress.com/priorities/",
               "https://nebraskavoterguide.com/candidates/crystal-rhoades"]),
        claim("cr2", "crystal-rhoades", "border_immigration", 0, False,
              "Calls for 'comprehensive immigration reform that creates a path to citizenship in fields where workers are needed' and states that 'immigrants should not live in fear,' pushing back against Trump's immigration enforcement. Her approach prioritizes legalization pathways over border-wall construction, military deployment, or mandatory deportation.",
              ["https://crystal4congress.com/priorities/",
               "https://nebraskaexaminer.com/2025/07/21/douglas-county-district-court-clerk-jumps-into-nebraska-2nd-district-field/"]),
    ]),

    # ------------ Russ Cleveland (MT-01, D, LOST June 2 primary) ------------
    ("russ-cleveland", "MT", "Representative", [
        claim("rc1", "russ-cleveland", "sanctity_of_life", 0, False,
              "Supports passing the Women's Health Protection Act (WHPA) to establish and protect federal abortion access and abortion providers, stating that 'decisions about healthcare ought to stay between people, their families, and their doctors, not politicians.' Flatly rejects any life-at-conception or personhood standard.",
              ["https://russellcleveland.org/policy/",
               "https://ballotpedia.org/Russell_Cleveland"]),
        claim("rc2", "russ-cleveland", "economic_stewardship", 2, False,
              "Campaigns on deploying a 'Medicare for All + system that provides affordable, universal coverage' covering medical, mental health, rural transportation, eyes, ears, and teeth — a major government spending expansion with no stated commitment to reducing the federal deficit or achieving a balanced budget.",
              ["https://russellcleveland.org/platform",
               "https://projects.montanafreepress.org/election-guide-2026/candidates/russell-cleveland/"]),
    ]),

    # ------------ Stuart Amoriell (NY-21, D, active June 23 primary) ------------
    ("stuart-amoriell", "NY", "Representative", [
        claim("sa1", "stuart-amoriell", "sanctity_of_life", 0, False,
              "States that 'reproductive decisions should be made by individuals based on their own beliefs and convictions and that government should not replace those personal decisions' — explicitly rejecting any legislative life-at-conception or personhood standard as government overreach into private medical choices.",
              ["https://www.northcountrypublicradio.org/news/story/53534/20260609/amoriell-a-democrat-believes-his-progressive-platform-could-flip-ny-21",
               "https://www.wamc.org/news/2026-05-26/ny-21-candidate-questionnaire-democrats-gendebien-amoriell"]),
        claim("sa2", "stuart-amoriell", "economic_stewardship", 2, False,
              "Explicitly campaigns on Medicare for All, declaring 'It is well past time that we have universal, single-payer healthcare for every American.' His progressive platform also expands universal childcare, fully funded Medicare/Medicaid, and other safety-net programs — a major government spending commitment with no balanced-budget or deficit-reduction posture.",
              ["https://www.northcountrypublicradio.org/news/story/53534/20260609/amoriell-a-democrat-believes-his-progressive-platform-could-flip-ny-21",
               "https://www.waer.org/2026-06-09/ny-21-candidate-profile-democrat-stuart-amoriell"]),
    ]),

    # ------------ Paige Loud (ME-02, D, June 9 primary) ------------
    ("paige-loud", "ME", "Representative", [
        claim("pl1", "paige-loud", "border_immigration", 1, False,
              "Explicitly opposes mass deportation operations, indefinite detention, and family separations as policy tools, and supports a 'real pathway' to citizenship with more protections for immigrant workers. Further states she 'would vote to abolish ICE and vote against funding for the agency' — flatly rejecting the rubric's mandatory-deportation and border-enforcement standard.",
              ["https://www.mainepublic.org/politics/2026-04-19/your-vote-2026-profile-paige-loud-democrat-for-2nd-district",
               "https://mainemorningstar.com/voter-guides/contests/2026-democratic-primary-u-s-house-district-2/"]),
        claim("pl2", "paige-loud", "economic_stewardship", 2, False,
              "Campaigns on single-payer Medicare for All covering medical, dental, vision, mental health, and long-term care, plus major investment in affordable housing (the Homes for All Act, $800 billion for 8 million publicly owned homes) — a large-government spending orientation with no deficit-reduction or balanced-budget commitment.",
              ["https://www.mainepublic.org/politics/2026-04-19/your-vote-2026-profile-paige-loud-democrat-for-2nd-district",
               "https://ballotpedia.org/Paige_Loud"]),
    ]),

    # ------------ Vichal Kumar (NY-07, D, active June 23 primary) ------------
    ("vichal-kumar", "NY", "Representative", [
        claim("vk1", "vichal-kumar", "sanctity_of_life", 0, False,
              "States that 'reproductive care is a fundamental right that must be accessible, affordable, and protected' and that 'the basic protections once guaranteed by Roe v. Wade must be made law' — explicitly rejecting any life-at-conception or personhood standard in favor of federally codified abortion access.",
              ["https://ny1.com/nyc/all-boroughs/inside-city-hall/2026/06/17/vichal-kumar-on-why-he-wants-to-replace-rep--vel-zquez-in-congress",
               "https://www.bkreader.com/featured-news/meet-your-candidate-vichal-kumar-for-ny-7-12394337"]),
        claim("vk2", "vichal-kumar", "border_immigration", 1, False,
              "As a public defender of 20 years representing immigrants in detention, Kumar frames ICE enforcement as a community threat rather than a lawful deportation tool, noting community concerns about 'the presence of ICE in local neighborhoods.' His platform focuses on supporting immigrant entrepreneurs and workers rather than mandatory deportation or E-Verify requirements.",
              ["https://ny1.com/nyc/all-boroughs/inside-city-hall/2026/06/17/vichal-kumar-on-why-he-wants-to-replace-rep--vel-zquez-in-congress",
               "https://qns.com/2026/05/vichal-kumar-federal-small-business-plan/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
