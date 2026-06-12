#!/usr/bin/env python3
"""Enrichment batch 152: hand-curated claims for 4 federal candidates from
WI-07, VA-07, and WA-04 — taken from the bottom of the non-exhausted federal
bucket (WI, VA, WA states, reverse-alpha order).

Targets:
  Michael Alfonso  (WI-07, R) — Trump-endorsed America First candidate
  Ginger Murray    (WI-07, D) — Democratic primary candidate
  Douglas Ollivant (VA-07, R) — former NSC Director for Iraq
  John Duresky     (WA-04, D) — retired Air Force major

Each claim cites >=1 reliable source and reflects 2025-2026 public positions.

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
    # ---------------- Michael Alfonso (WI-07, R) ----------------
    ("michael-alfonso", "WI", "Representative", [
        claim("ma1", "michael-alfonso", "sanctity_of_life", 0, True,
              "Campaign materials state he 'believes every person has an inherent right to life—from conception to natural death' and he explicitly opposes Democrats' push to expand mail-in abortion pills — a life-at-conception / personhood posture fully aligned with the sanctity-of-life rubric.",
              ["https://www.tpaction.com/bio/michaelalfonso",
               "https://www.waow.com/news/president-trump-endorses-michael-alfonso-for-wisconsin-district-7/article_36828ff4-00fa-4329-95b7-8b0f2daaa974.html"]),
        claim("ma2", "michael-alfonso", "self_defense", 0, True,
              "Backs constitutional carry and the right to self-defense; President Trump's endorsement specifically praised his commitment to 'Protect our always under siege Second Amendment,' and his campaign platform lists 2A protection as a non-negotiable core issue.",
              ["https://www.tpaction.com/bio/michaelalfonso",
               "https://www.waow.com/news/president-trump-endorses-michael-alfonso-for-wisconsin-district-7/article_36828ff4-00fa-4329-95b7-8b0f2daaa974.html"]),
        claim("ma3", "michael-alfonso", "border_immigration", 0, True,
              "Campaigns to 'keep our border secure,' stop migrant crime, and advance Trump's America First border agenda; argues that mass-immigration programs harm American workers and depress wages — consistent with the wall-plus-military rubric posture.",
              ["https://www.waow.com/news/president-trump-endorses-michael-alfonso-for-wisconsin-district-7/article_36828ff4-00fa-4329-95b7-8b0f2daaa974.html",
               "https://ballotpedia.org/Michael_Alfonso"]),
    ]),

    # ---------------- Ginger Murray (WI-07, D) ----------------
    ("ginger-murray", "WI", "Representative", [
        claim("gm1", "ginger-murray", "border_immigration", 1, False,
              "At a March 2026 Rhinelander candidate forum, declared 'ICE agents are not peace officers' and criticized deportation enforcement as violating constitutional rights — directly opposing the rubric's mandatory-deportation and interior-enforcement standard.",
              ["https://www.wsaw.com/2026/03/04/democrats-make-their-case-7th-congressional-district-forum-rhinelander/",
               "https://www.apg-wi.com/ashland_daily_press/news/local/democratic-candidates-for-7th-congressional-district-hold-ashland-forum/article_a3463f27-2f34-4fda-88f7-e0929c0d762c.html"]),
        claim("gm2", "ginger-murray", "biblical_marriage", 2, False,
              "Declared publicly that 'The trans community is under attack. I'm always going to be an upstander, not a bystander' — affirming support for transgender ideology and rejecting the biological-sex-based categories the rubric requires candidates to protect.",
              ["https://www.wsaw.com/2026/03/04/democrats-make-their-case-7th-congressional-district-forum-rhinelander/",
               "https://www.apg-wi.com/ashland_daily_press/news/local/democratic-candidates-for-7th-congressional-district-hold-ashland-forum/article_a3463f27-2f34-4fda-88f7-e0929c0d762c.html"]),
    ]),

    # ---------------- Douglas Ollivant (VA-07, R) ----------------
    ("douglas-ollivant", "VA", "Representative", [
        claim("do1", "douglas-ollivant", "economic_stewardship", 2, True,
              "A central campaign plank is 'cutting government spending' and 'promoting a leaner, more efficient government that works for taxpayers' — directly aligned with the rubric's anti-deficit, balanced-budget standard.",
              ["https://ballotpedia.org/Douglas_Ollivant",
               "https://www.thecentersquare.com/virginia/article_6ec89afc-51c5-4a8b-9bc5-8893494fb646.html"]),
        claim("do2", "douglas-ollivant", "border_immigration", 0, True,
              "'Securing the border' is listed as a top campaign priority alongside strengthening the military — consistent with the wall-plus-military posture the rubric requires.",
              ["https://ballotpedia.org/Douglas_Ollivant",
               "https://www.potomaclocal.com/2025/09/16/doug-ollivant-just-jumped-into-the-va-7-race-against-tara-durant/"]),
    ]),

    # ---------------- John Duresky (WA-04, D) ----------------
    ("john-duresky", "WA", "Representative", [
        claim("jd1", "john-duresky", "border_immigration", 1, False,
              "Explicitly supports 'a legal pathway of some kind' for undocumented immigrants who have lived and worked in the community — directly opposing the rubric's mandatory-deportation and enforcement-first standard.",
              ["https://www.yakimaherald.com/news/local/government/elections/democrat-john-duresky-stresses-affordability-and-accountability-in-campaign-for-congress/article_9877b63c-762e-43f2-81a5-3b961af0e73b.html",
               "https://keprtv.com/news/local/democrat-john-duresky-enters-race-for-4th-congressional-seat"]),
        claim("jd2", "john-duresky", "economic_stewardship", 2, False,
              "Prioritizes 'restoring Medicaid access' and expanding Affordable Care Act subsidies as top campaign goals — government-spending expansion programs at odds with the rubric's anti-deficit, balanced-budget standard.",
              ["https://www.yakimaherald.com/news/local/government/elections/democrat-john-duresky-stresses-affordability-and-accountability-in-campaign-for-congress/article_9877b63c-762e-43f2-81a5-3b961af0e73b.html"]),
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
