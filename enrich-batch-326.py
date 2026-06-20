#!/usr/bin/env python3
"""Enrichment batch 326: third claim for 5 evidence_curated federal candidates.

Targets evidence_curated U.S. House/Senate candidates with exactly 2 existing claims,
taken from the bottom of the alphabet (OK, NY). All archetype_curated federal
senator/rep slots are exhausted; these are the next ripe targets.

Mix (0 R / 5 D): Troy Green (OK Senate candidate), Patrick Timmins (NY-12),
Taylor Darling (NY-04), Vichal Kumar (NY-07), Laura Dunn (NY-12).

Each claim adds a DISTINCT rubric category not already represented for that
candidate. Sources: campaign sites, nondoc.com, westsiderag.com, cbsnews.com,
ballotpedia.org, governor.ny.gov, newindiaabroad.com.

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
    # ------------ Troy Green (OK-D, 2026 U.S. Senate candidate, Mullin seat) ------------
    # Existing claims: family_child_sovereignty[0], economic_stewardship[2]
    # Adding: foreign_policy_restraint[1] (end forever wars/repeal AUMF)
    ("troy-green-ok-senate", "OK", "Senator", [
        claim("tg3", "troy-green-ok-senate", "foreign_policy_restraint", 1, True,
              "Green's 2026 Senate campaign explicitly pledges 'no foreign entanglement without "
              "a clear mission, clear strategy, and clear plan for veterans when they come home' "
              "and condemns 'endless wars' that 'have cost Oklahomans dearly while politicians "
              "get rich on defense contracts' — a restraint posture aligned with ending "
              "America's overseas military commitments and opposing open-ended foreign wars.",
              ["https://nondoc.com/2026/05/27/cheat-sheet-5-oklahoma-democrats-compete-in-u-s-senate-primary/",
               "https://www.opencampaign.com/politicians-in-united-states/197909/troy-green/issue-positions"]),
    ]),

    # ------------ Patrick Timmins (NY-D, U.S. Rep NY-12 candidate) ------------
    # Existing claims: border_immigration[1], self_defense[1]
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("patrick-timmins", "NY", "Representative", [
        claim("pt3", "patrick-timmins", "economic_stewardship", 2, False,
              "In a March 2026 West Side Rag interview, Timmins stated that Medicare should "
              "expand to cover dental and vision care, backing increased federal healthcare "
              "entitlement spending that runs counter to balanced-budget fiscal principles "
              "and would add to the federal deficit.",
              ["https://www.westsiderag.com/2026/03/23/a-wsr-conversation-with-candidate-patrick-timmins-in-the-race-to-represent-the-uws-in-congress"]),
    ]),

    # ------------ Taylor Darling (NY-D, U.S. Rep NY-04 candidate) ------------
    # Existing claims: sanctity_of_life[0], border_immigration[1]
    # Adding: self_defense[0] (constitutional carry)
    ("taylor-darling", "NY", "Representative", [
        claim("td3", "taylor-darling", "self_defense", 0, False,
              "As a New York State Assembly member (AD-18, Nassau County, 2019-2024), voted "
              "with the Democratic Assembly majority to pass the Concealed Carry Improvement "
              "Act (S51001/A41001A, Chapter 371, July 1, 2022) 90-52 in a special session "
              "convened by Gov. Hochul — imposing new 'sensitive location' prohibitions on "
              "carrying firearms and overhauling licensing requirements, in direct opposition "
              "to constitutional carry principles. The only Democratic dissents came from "
              "three Central New York members; Darling, a Nassau County progressive, "
              "voted with the caucus.",
              ["https://www.cbsnews.com/newyork/live-updates/new-york-state-legislature-special-session-gun-control-abortion-kathy-hochul-supreme-court/",
               "https://www.governor.ny.gov/news/governor-hochul-signs-landmark-legislation-strengthen-gun-laws-and-bolster-restrictions"]),
    ]),

    # ------------ Vichal Kumar (NY-D, U.S. Rep NY-07 candidate) ------------
    # Existing claims: sanctity_of_life[0], border_immigration[1]
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("vichal-kumar", "NY", "Representative", [
        claim("vk3", "vichal-kumar", "economic_stewardship", 2, False,
              "Names 'universal healthcare' as one of his three top campaign priorities — "
              "alongside dismantling ICE and empowering workers — backing expanded federal "
              "health entitlement spending that would substantially increase the federal "
              "deficit, running counter to balanced-budget fiscal principles.",
              ["https://www.newindiaabroad.com/english/news/attorney-vichal-kumar-announces-run-for-congress-in-ny07",
               "https://www.kumar4ny.com/"]),
    ]),

    # ------------ Laura Dunn (NY-D, U.S. Rep NY-12 candidate) ------------
    # Existing claims: sanctity_of_life[0], biblical_marriage[0]
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("laura-dunn-ny-12", "NY", "Representative", [
        claim("ld3", "laura-dunn-ny-12", "economic_stewardship", 2, False,
              "Dunn's 2026 Ballotpedia Candidate Connection survey pledges to index Social "
              "Security to inflation and expand funding for affordable housing — backing "
              "increased federal entitlement and housing spending programs that would add "
              "to the federal deficit, running counter to balanced-budget fiscal principles.",
              ["https://ballotpedia.org/Laura_Dunn_(New_York)",
               "https://news.ballotpedia.org/2026/04/03/alex-bores-d-george-conway-d-micah-lasher-d-jack-schlossberg-d-and-six-other-candidates-are-running-in-the-democratic-primary-for-new-yorks-12th-congressional-district-on-june-23-2026/"]),
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
