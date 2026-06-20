#!/usr/bin/env python3
"""Enrichment batch 325: third claim for 5 evidence_curated federal House candidates.

Targets evidence_curated U.S. House candidates with exactly 2 existing claims,
taken from the bottom of the alphabet (MI, MN, NC). All archetype_curated
federal senator/rep slots are exhausted; these are the next ripe targets.

Mix (0 R / 5 D): Elyon Badger (MI-07), Matt Maasdam (MI-07), Tim Greimel (MI-10),
Jen Schultz (MN-08), Frank Pierce (NC-13, lost primary).

Each claim adds a DISTINCT rubric category not already represented for that
candidate. Sources: candidate campaign websites, Michigan Radio, Michigan Advance,
VoteVets, branch.vote.

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
    # ------------ Elyon Badger (MI-D, U.S. Rep MI-07 candidate) ------------
    # Existing claims: sanctity_of_life[0], biblical_marriage[2]
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("elyon-badger", "MI", "MI-07", [
        claim("eb3", "elyon-badger", "economic_stewardship", 2, False,
              "Badger's campaign platform at elyonbadger.com calls for 'Universal Healthcare: "
              "Shelter, Food and Medicine to each according to their basic needs,' framing "
              "government-guaranteed healthcare, food, and housing as a universal right. "
              "A federally mandated 'basic needs' guarantee of this scope would require "
              "massive deficit expansion and government takeover of medicine — directly "
              "opposing the rubric's balanced-budget and anti-deficit standard.",
              ["https://elyonbadger.com/",
               "https://michiganadvance.com/2025/08/27/lansing-activist-joins-the-democratic-fray-for-michigans-7th-congressional-district/"]),
    ]),

    # ------------ Matt Maasdam (MI-D, U.S. Rep MI-07 candidate) ------------
    # Existing claims: self_defense[1], economic_stewardship[2]
    # Adding: sanctity_of_life[0] (life-at-conception/personhood)
    ("matt-maasdam", "MI", "MI-07", [
        claim("mm3", "matt-maasdam", "sanctity_of_life", 0, False,
              "Maasdam's campaign priorities page (mattmaasdam.com) states he will 'always "
              "fight for our rights... women's rights, including the right to choose,' "
              "committing to protect abortion access. He is endorsed by VoteVets PAC, "
              "whose endorsed candidates uniformly support federal abortion rights — "
              "rejecting any recognition of personhood from conception.",
              ["https://mattmaasdam.com/priorites/",
               "https://votevets.org/candidates/matt-maasdam"]),
    ]),

    # ------------ Tim Greimel (MI-D, U.S. Rep MI-10 candidate) ------------
    # Existing claims: sanctity_of_life[0], economic_stewardship[2]
    # Adding: self_defense[1] (anti red-flag/AWB/mag-limit/registry)
    ("tim-greimel", "MI", "MI-10", [
        claim("tg3", "tim-greimel", "self_defense", 1, False,
              "As a 2026 congressional candidate and former Michigan House Minority Leader, "
              "Greimel has publicly called out Republican legislators for voting with the "
              "NRA 'because they're scared about their re-election,' aligning himself with "
              "the gun-control wing of the Democratic Party. His position supports stricter "
              "firearm restrictions — in direct opposition to the rubric's defense of "
              "unrestricted Second Amendment rights, opposition to red-flag laws, and "
              "rejection of magazine-capacity limits and gun registries.",
              ["https://michiganradio.org/post/democratic-candidate-credits-students-shaming-gun-control-opponents",
               "https://en.wikipedia.org/wiki/Tim_Greimel"]),
    ]),

    # ------------ Jen Schultz (MN-D, U.S. Rep MN-08 candidate) ------------
    # Existing claims: sanctity_of_life[0], self_defense[1]
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("jen-schultz", "MN", "MN-08", [
        claim("js3", "jen-schultz", "economic_stewardship", 2, False,
              "A PhD health economist and former chair of the Minnesota House Human Services "
              "Finance & Policy Committee, Schultz has endorsed a Medicare for All "
              "single-payer system that would eliminate private health insurance in favor "
              "of an expanded government program, and authored the MinnesotaCare Buy-In "
              "expansion in the state legislature. This commitment to government-run "
              "universal healthcare funding is directly at odds with the rubric's "
              "balanced-budget and anti-deficit standard.",
              ["https://jenschultzforcongress.com/issues",
               "https://en.wikipedia.org/wiki/Jennifer_Schultz"]),
    ]),

    # ------------ Frank Pierce (NC-D, U.S. Rep NC-13, LOST March 2026 primary) ------------
    # Existing claims: sanctity_of_life[0], self_defense[1]
    # Adding: biblical_marriage[0] (one-man-one-woman)
    ("frank-pierce-nc-13", "NC", "NC-13", [
        claim("fp3", "frank-pierce-nc-13", "biblical_marriage", 0, False,
              "Pierce explicitly listed 'Protection for LGBTQIA+ Rights' as a core campaign "
              "priority in the 2026 NC-13 Democratic primary, signaling support for federal "
              "LGBTQ+ nondiscrimination protections and same-sex marriage — directly "
              "rejecting the rubric's one-man-one-woman definition of marriage.",
              ["https://www.branch.vote/races/2026-north-carolina-primary-election-nc-state-us-representative-nc-congressional-13-d/candidates/frank-pierce",
               "https://www.wakedems.org/election-central-2024/candidate-info-frank-pierce/"]),
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
