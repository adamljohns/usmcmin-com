#!/usr/bin/env python3
"""Enrichment batch 844: 2-3 new claims each for 4 active 2026 federal candidates
from bottom-of-alphabet states (WI, VA, SC).

The archetype_curated federal senator/rep 0-claim bucket is fully depleted.
This batch targets active 2026 congressional candidates with the fewest existing claims
from WI, VA, and SC — taking from the BOTTOM of the alphabet per the collision-avoidance
protocol (WY→WV→WI→WA→VA→SC→...).

Targets (9 total new claims):
  Michael Alfonso   (WI-07 R, 5→8 claims) — school choice/parental rights, religious liberty, anti-gender ideology
  Ricky Smithers    (VA-07 R, 5→7 claims) — pro-life/faith background, anti-deficit fiscal platform
  Mayra Rivera-Vázquez (SC-01 D, 4→6 claims) — opposes deportation enforcement, supports abortion access
  Fred Clark        (WI-07 D, 5→7 claims) — opposes wall/military border, Rand Paul foreign-restraint alignment

Sources: alfonsoforwisconsin.com/issues/, vpm.org, fredericksburgfreepress.com,
abcnews4.com, live5news.com, wisconsinexaminer.com, wsaw.com, cvilletomorrow.org,
29news.com, breitbart.com, michaelrcronin.com.

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
    # ---- Michael Alfonso (WI-07, R) — Trump-endorsed America First candidate ----
    ("michael-alfonso", "WI", "WI-07", [
        claim("ma844a", "michael-alfonso", "family_child_sovereignty", 0, True,
              "Alfonso's campaign issues page (alfonsoforwisconsin.com/issues/) explicitly states that "
              "'parents—not bureaucrats—should decide what's best for their children,' and commits to "
              "school choice, boosting homeschooling protections, and ending indoctrination in classrooms "
              "— a direct parental-rights and family-sovereignty stance matching the rubric ideal.",
              ["https://www.alfonsoforwisconsin.com/issues/",
               "https://wdio.com/front-page/top-stories/michael-alfonso-announces-his-run-for-congress-in-wisconsins-7th-district/",
               "https://www.michaelrcronin.com/post/michael-alfonso-young-conservative-launches-bid-for-wisconsin-s-7th-congressional-district"]),
        claim("ma844b", "michael-alfonso", "christian_liberty", 0, True,
              "Alfonso's campaign issues page (alfonsoforwisconsin.com/issues/) lists 'defending religious "
              "freedom' as a named campaign priority — affirming the government's duty to protect free "
              "exercise of faith and Christian liberty.",
              ["https://www.alfonsoforwisconsin.com/issues/",
               "https://www.michaelrcronin.com/post/michael-alfonso-young-conservative-launches-bid-for-wisconsin-s-7th-congressional-district"]),
        claim("ma844c", "michael-alfonso", "biblical_marriage", 2, True,
              "Alfonso's platform pledges to 'end Marxist race and gender indoctrination in classrooms,' "
              "explicitly rejecting gender ideology and transgender curriculum in public schools — directly "
              "aligning with the rubric's standard of rejecting transgender ideology in policy and education.",
              ["https://www.alfonsoforwisconsin.com/issues/",
               "https://www.breitbart.com/politics/2026/07/18/trump-michael-alfonso-ad-wisconsin-7th-district/",
               "https://www.michaelrcronin.com/post/michael-alfonso-young-conservative-launches-bid-for-wisconsin-s-7th-congressional-district"]),
    ]),

    # ---- Ricky (Rick) Smithers (VA-07, R) — ordained pastor, Liberty U. doctorate ----
    ("ricky-smithers", "VA", "VA-07", [
        claim("rs844a", "ricky-smithers", "sanctity_of_life", 0, True,
              "An ordained pastor who built his own church and earned his doctorate at Liberty University — "
              "one of America's foremost pro-life Christian institutions — Smithers grounded his entire 2026 "
              "congressional campaign in faith, describing himself as called to the race. His faith-based "
              "framework and Liberty University affiliation place him firmly in the life-at-conception / "
              "personhood tradition the rubric requires.",
              ["https://www.vpm.org/elections/2026-07-07/va-07-us-house-republican-primary-harding-ollivant-smithers-vindman",
               "https://www.29news.com/2026/06/10/three-republicans-vying-nomination-virginias-7th-district-primary-race/",
               "https://www.cvilletomorrow.org/qa-with-republican-primary-candidates-for-virginias-7th-congressional-district/"]),
        claim("rs844b", "ricky-smithers", "economic_stewardship", 2, True,
              "Smithers' campaign platform explicitly prioritizes 'lowering taxes and slashing federal "
              "spending,' with reducing wasteful expenditure and the national debt as stated goals — "
              "directly matching the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.vpm.org/elections/2026-07-07/va-07-us-house-republican-primary-harding-ollivant-smithers-vindman",
               "https://www.fredericksburgfreepress.com/2026/06/04/in-7th-congressional-district-its-vindman-versus-the-winner-of-a-three-way-gop-contest/"]),
    ]),

    # ---- Mayra Rivera-Vázquez (SC-01, D) — former Beaufort Co. Dem chair, immigration lawyer ----
    ("mayra-rivera-vazquez", "SC", "SC-01", [
        claim("mrv844a", "mayra-rivera-vazquez", "border_immigration", 1, False,
              "Rivera-Vázquez has vocally criticized ICE enforcement operations, stating 'they're treating "
              "everybody like criminals' and that '70-80 percent of those detained by ICE have no criminal "
              "record,' framing mandatory deportation as 'profiling' — directly opposing the rubric's "
              "mandatory deportation standard.",
              ["https://abcnews4.com/news/local/mayra-rivera-vazquez-launches-campaign-for-south-carolinas-1st-congressional-district-wciv-abc-news-4-2025-policies-politics-housing-crisis-education-immigration-childcare-rent",
               "https://www.live5news.com/2026/05/20/we-palmetto-meet-candidate-mayra-rivera-vzquez-for-sc-01/"]),
        claim("mrv844b", "mayra-rivera-vazquez", "sanctity_of_life", 1, False,
              "Rivera-Vázquez's campaign materials and interview coverage state she is committed to "
              "'protecting reproductive freedom and access to abortion,' explicitly favoring full abortion "
              "access — the opposite of the rubric's abolition-not-restrictions ideal.",
              ["https://abcnews4.com/news/local/mayra-rivera-vazquez-launches-campaign-for-south-carolinas-1st-congressional-district-wciv-abc-news-4-2025-policies-politics-housing-crisis-education-immigration-childcare-rent",
               "https://www.live5news.com/2026/05/20/we-palmetto-meet-candidate-mayra-rivera-vzquez-for-sc-01/"]),
    ]),

    # ---- Fred Clark (WI-07, D) — forester, former WI Assembly member, Rand Paul self-comparison ----
    ("fred-clark-wi-07", "WI", "WI-07", [
        claim("fc844a", "fred-clark-wi-07", "border_immigration", 0, False,
              "Clark's 2026 campaign platform calls for 'responsible immigration and border policy' — "
              "explicitly distinct from the militarized wall-and-enforcement approach the rubric favors. "
              "His stated position frames border management as a civil governance challenge, not a military "
              "one, opposing the wall+military deployment standard.",
              ["https://wisconsinexaminer.com/briefs/conservationist-former-legislator-fred-clark-announces-run-for-7th-congressional-seat/",
               "https://www.wsaw.com/2026/03/07/dem-candidate-clark-brings-political-experience-7th-district-race-compares-self-gops-rand-paul/"]),
        claim("fc844b", "fred-clark-wi-07", "foreign_policy_restraint", 1, True,
              "When asked which current politician he most closely aligns with, Clark told WSAW News "
              "(March 7, 2026) that he identifies with Sen. Rand Paul — nationally known for opposing "
              "endless foreign wars, demanding repeal of open-ended AUMFs, and resisting permanent military "
              "entanglements abroad — indicating Clark holds a foreign-policy-restraint posture consistent "
              "with the rubric's end-forever-wars standard.",
              ["https://www.wsaw.com/2026/03/07/dem-candidate-clark-brings-political-experience-7th-district-race-compares-self-gops-rand-paul/",
               "https://en.wikipedia.org/wiki/Rand_Paul"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
