#!/usr/bin/env python3
"""Enrichment batch 281: 5 active 2026 federal candidates from the bottom of the alphabet.

Bottom-of-alphabet pull (UT, TN, SC, NH):
  Jonny Larsen (UT-04, D NOMINEE), Craig Ballin (TN-06, D),
  Mayra Rivera-Vázquez (SC-01, D), Max Diaz (SC-01, D),
  Jared Sullivan (NH Senate, D).
Claims sourced from candidate websites, Ballotpedia, citizenscount.org,
live5news.com, abcnews4.com, and state legislative records (2024-2026).
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
    # ------------ Jonny Larsen (UT-04, D NOMINEE) ------------
    ("jonny-larsen", "UT", "Representative", [
        claim("jl1", "jonny-larsen", "economic_stewardship", 2, False,
              "Campaigns on protecting Social Security and union-worker pensions — his grandmother's union pension and Social Security shaped his worldview — alongside expanding affordable healthcare and education access. His platform prioritizes government program defense over deficit reduction or balanced-budget commitments.",
              ["https://jonnyutah4congress.com/",
               "https://ballotpedia.org/Jonathan_Larsen"]),
        claim("jl2", "jonny-larsen", "border_immigration", 0, False,
              "Campaign platform is entirely focused on domestic economic issues — affordable healthcare, education, workers' rights, and government accountability — with no stated support for border wall construction, military deployment to the border, or mandatory deportation. Lacks any enforcement-first immigration posture.",
              ["https://jonnyutah4congress.com/",
               "https://ballotpedia.org/Jonathan_Larsen"]),
    ]),

    # ------------ Craig Ballin (TN-06, D Candidate) ------------
    ("craig-ballin", "TN", "Representative", [
        claim("cb1", "craig-ballin", "family_child_sovereignty", 0, False,
              "Explicitly opposes school voucher programs, stating that 'public school funding should go to public schools rather than wealthy families' and calling for 'killing vouchers.' His position rejects the parental-choice school-funding model that allows families to direct education dollars to private, charter, or home-based options.",
              ["https://ballinforcongress.com/the-issues/",
               "https://ballotpedia.org/Craig_Ballin"]),
        claim("cb2", "craig-ballin", "border_immigration", 0, False,
              "Frames illegal immigration as a bureaucratic-pathway problem rather than a border-security crisis, arguing that 'many come illegally because it's actually easier than obtaining legal citizenship.' His approach calls for reforming the legal-immigration process rather than border-wall construction, military deployment, or mandatory deportation.",
              ["https://ballotpedia.org/Craig_Ballin",
               "https://ballotpedia.org/Tennessee's_6th_Congressional_District_election,_2026"]),
    ]),

    # ------------ Mayra Rivera-Vázquez (SC-01, D Candidate) ------------
    ("mayra-rivera-vazquez", "SC", "Representative", [
        claim("mrv1", "mayra-rivera-vazquez", "sanctity_of_life", 0, False,
              "Explicitly advocates for 'protecting reproductive freedom and access to abortion,' supports federal statutory protections for abortion rights, and criticizes government interference in 'personal medical decisions' — rejecting any life-at-conception or personhood-from-fertilization standard.",
              ["https://abcnews4.com/news/lowcountry-and-state-politics/mayra-rivera-vazquez-pushes-for-stronger-hispanic-representation-in-congressional-run",
               "https://www.mayra4congress.com/meet-mayra"]),
        claim("mrv2", "mayra-rivera-vazquez", "border_immigration", 0, False,
              "Criticizes ICE enforcement as overreach, stating that '70-80 percent of those detained by ICE have no criminal record and are simply trying to get through the immigration system.' Champions immigration reform focused on easing legal pathways rather than mandatory deportation, E-Verify, or border-wall construction.",
              ["https://www.live5news.com/2026/05/20/we-palmetto-meet-candidate-mayra-rivera-vzquez-for-sc-01/",
               "https://ballotpedia.org/Mayra_Rivera-Vazquez"]),
    ]),

    # ------------ Max Diaz (SC-01, D Candidate) ------------
    ("max-diaz-sc-01", "SC", "Representative", [
        claim("md1", "max-diaz-sc-01", "economic_stewardship", 2, False,
              "Campaigns on federal investment in next-generation nuclear energy, multi-story indoor farming, renewable energy manufacturing, and aerospace innovation, plus universal healthcare and housing affordability — a government-growth spending orientation with no stated commitment to reducing the deficit or achieving a balanced budget.",
              ["https://www.live5news.com/2026/05/02/we-palmetto-meet-candidate-max-diaz-sc-01/",
               "https://ballotpedia.org/Max_Diaz"]),
        claim("md2", "max-diaz-sc-01", "sanctity_of_life", 0, False,
              "Received a co-endorsement from Progressive Victory, a left-progressive PAC that endorses candidates who support reproductive freedom and pushes the Democratic Party left. His campaign platform contains no stated pro-life position or support for life-at-conception protections.",
              ["https://www.progressivevictory.win/endorsements",
               "https://ballotpedia.org/Max_Diaz"]),
    ]),

    # ------------ Jared Sullivan (NH, 2026 D Senate Candidate) ------------
    ("jared-sullivan-nh-senate", "NH", "Senator", [
        claim("js1", "jared-sullivan-nh-senate", "sanctity_of_life", 0, False,
              "As a NH state representative, voted for a constitutional right to abortion before 24 weeks (CACR 23) and voted to repeal NH's Fetal Life Protection Act (HB 271) that restricted abortions after 24 weeks — flatly rejecting any life-at-conception or fetal-personhood standard.",
              ["https://www.citizenscount.org/candidate/jared-sullivan/serving",
               "https://en.wikipedia.org/wiki/Jared_Sullivan"]),
        claim("js2", "jared-sullivan-nh-senate", "self_defense", 1, False,
              "As a NH state representative, voted to establish extreme-risk protection (red-flag) orders (HB 106), expand background checks for firearms (HB 59, HB 56), and impose a 3-day waiting period on firearm purchases (HB 76) — directly opposing the rubric's anti-red-flag/AWB/registry standard for Second Amendment protection.",
              ["https://www.citizenscount.org/candidate/jared-sullivan/serving",
               "https://fastdemocracy.com/bill-search/nh/legislators/NHL001612/"]),
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
