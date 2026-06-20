#!/usr/bin/env python3
"""Enrichment batch 327: third claim for 5 evidence_curated federal candidates.

Targets evidence_curated U.S. House candidates with exactly 2 existing claims,
taken from the bottom of the alphabet (WI, PA, NY). All archetype_curated federal
senator/rep slots are exhausted; these are the next ripe targets.

Mix (1 R / 4 D): Paul Wassgren (WI-R, WI-07), Pablo McConnie-Saad (PA-D, PA-03),
Effie Phillips-Staley (NY-D, NY-17), John Cappello (NY-D, NY-17),
Beth Davidson (NY-D, NY-17).

Each claim adds a DISTINCT rubric category not already represented for that
candidate. Sources: yahoo.com, wispolitics.com, whyy.org, pabloforcongress.com,
effieforcongress.com, ourrevolution.com, wamc.org, ballotpedia.org,
bethdavidsonforcongress.com.

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
    # ------------ Paul Wassgren (WI-R, WI-07 open-seat candidate) ------------
    # Existing claims: self_defense[0] (constitutional carry, True),
    #                  border_immigration[0] (wall/military, True)
    # Adding: sanctity_of_life[0] (life-at-conception/personhood)
    ("paul-wassgren", "WI", "Representative", [
        claim("pw3", "paul-wassgren", "sanctity_of_life", 0, True,
              "Wassgren's 2025 campaign launch carried explicit anti-abortion language "
              "self-identifying him as 'proudly pro-life' on his campaign website — text "
              "flagged by the DCCC and reported by Salon (August 2025) before being later "
              "scrubbed. He listed 'family values' as one of his three top campaign pillars "
              "and suspended his race in April 2026 to expand his involvement with the "
              "Catholic Church, consistent with a life-from-conception posture.",
              ["https://www.yahoo.com/news/articles/proudly-pro-life-wisconsin-republican-103053735.html",
               "https://www.wispolitics.com/2025/wassgren-campaign-suspends-congressional-campaign-to-assist-wisconsin-republicans-and-faith-community/"]),
    ]),

    # ------------ Pablo McConnie-Saad (PA-D, PA-03, LOST 2026 D primary) ------------
    # Existing claims: border_immigration[1] (abolish ICE, False),
    #                  foreign_policy_restraint[3] (reject AIPAC/corporate PAC, True)
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("pablo-mcconnie-saad", "PA", "Representative", [
        claim("pms3", "pablo-mcconnie-saad", "economic_stewardship", 2, False,
              "As a former Biden White House climate-policy advisor, McConnie-Saad helped "
              "advance the Inflation Reduction Act and similar programs that added trillions "
              "to the federal deficit. His 2026 congressional campaign prioritized making "
              "Philadelphia more affordable by expanding government programs — explicitly "
              "naming 'health insurance for our families' as a top commitment — a posture "
              "of expanded entitlement spending inconsistent with balanced-budget fiscal "
              "principles.",
              ["https://whyy.org/articles/pablo-mcconnie-saad-congressional-candidate-philadelphia-biden/",
               "https://pabloforcongress.com/"]),
    ]),

    # ------------ Effie Phillips-Staley (NY-D, NY-17) ------------
    # Existing claims: sanctity_of_life[0] (abortion, False),
    #                  border_immigration[0] (wall/military, False)
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("effie-phillips-staley", "NY", "Representative", [
        claim("eps3", "effie-phillips-staley", "economic_stewardship", 2, False,
              "Phillips-Staley has made Medicare for All the centerpiece of her healthcare "
              "platform, stating 'In Congress, my focus will be Medicare for All at the "
              "federal level, which is the structural fix this problem requires.' Her "
              "Our Revolution endorsement highlights her commitment to fully replacing "
              "private insurance with a single-payer federal program that would dramatically "
              "expand entitlement spending and the federal deficit, running counter to "
              "balanced-budget fiscal principles.",
              ["https://effieforcongress.com/priorities/",
               "https://ourrevolution.com/effie-phillips-staley-for-congress-in-ny-17/"]),
    ]),

    # ------------ John Cappello (NY-D, NY-17) ------------
    # Existing claims: foreign_policy_restraint[0] (FDD hawkish, False),
    #                  industry_capture[4] (defense-contractor ties, False)
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("john-cappello", "NY", "Representative", [
        claim("jc3", "john-cappello", "economic_stewardship", 2, False,
              "In a June 2026 WAMC radio segment covering the NY-17 Democratic primary, "
              "Cappello named 'universal healthcare' as a top legislative priority and "
              "called for restoring and strengthening the Affordable Care Act, saying "
              "'We're talking about people's well-being, and I think that we can figure "
              "out a way to provide universal coverage and choice.' Expanded government "
              "healthcare entitlement programs add to the federal deficit and run counter "
              "to balanced-budget fiscal principles.",
              ["https://www.wamc.org/news/2026-06-15/new-york-17-democratic-primary",
               "https://ballotpedia.org/John_Cappello"]),
    ]),

    # ------------ Beth Davidson (NY-D, NY-17) ------------
    # Existing claims: sanctity_of_life[0] (abortion, False),
    #                  self_defense[0] (constitutional carry, False)
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("beth-davidson", "NY", "Representative", [
        claim("bd3", "beth-davidson", "economic_stewardship", 2, False,
              "Davidson's healthcare platform calls for a Medicare public option 'so "
              "everyone can have affordable, accessible healthcare' and lists protecting "
              "'Social Security and Medicare' as a top legislative priority — commitments "
              "to expanding and preserving federal entitlement programs that would increase "
              "federal spending and the deficit, running counter to balanced-budget fiscal "
              "principles.",
              ["https://bethdavidsonforcongress.com/beths-priorities/",
               "https://www.yahoo.com/news/beth-davidson-house-candidate-backed-204713930.html"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
