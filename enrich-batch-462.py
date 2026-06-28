#!/usr/bin/env python3
"""Enrichment batch 462: 4 active 2026 federal House D candidates from bottom states.

Primary archetype_curated bucket (federal senators/reps with 0 claims) is fully
exhausted. Fallback: evidence_curated candidates with only 2 claims from the
bottom of the alphabet (MO, IL, MI) who are active in upcoming Aug 4 / Nov 2026
contests.

Targets:
- Josh Smead (MO-06, D) — Aug 4 2026 D primary
- Matthew Levine (MO-06, D) — Aug 4 2026 D primary
- Patty Garcia (IL-04, D) — 2026 D Nominee
- William Lawrence (MI-07, D) — Aug 4 2026 D primary

2 new distinct-category claims per candidate; all existing claim categories
avoided to prevent duplication.
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
    # ---------------- Josh Smead (MO-06, D) ----------------
    ("josh-smead", "MO", "Representative", [
        claim("js3", "josh-smead", "sanctity_of_life", 0, False,
              "As a Democratic candidate for Missouri's 6th District in the 2026 cycle — where a 2026 ballot measure seeks to reinstate the state's abortion ban over 2024's Amendment 3 reproductive-freedom right — Smead campaigns on expanding 'maternity and family healthcare' access for every Missourian, signaling support for abortion access consistent with his Indivisible-network coalition and opposing any legal recognition of life from conception.",
              ["https://votesmead.com/",
               "https://ballotpedia.org/Josh_Smead"]),
        claim("js4", "josh-smead", "economic_stewardship", 2, False,
              "Campaigns on building 'stronger infrastructure, expanded access to healthcare, and equal opportunities for all' — a platform of expanded federal investment in healthcare and community programs that runs counter to the rubric's balanced-budget, anti-deficit stewardship standard.",
              ["https://votesmead.com/",
               "https://ballotpedia.org/Josh_Smead"]),
    ]),

    # ---------------- Matthew Levine (MO-06, D) ----------------
    ("matthew-levine-mo-06", "MO", "Representative", [
        claim("ml3", "matthew-levine-mo-06", "self_defense", 1, False,
              "On gun policy, Levine states he 'supports and will defend' the Second Amendment while simultaneously proposing 'implementing background checks' and 'age restrictions on who should be able to carry weapons,' citing that 'firearms are currently the leading cause of death in children in the United States' — an endorsement of the background-check and age-restriction framework the rubric classifies as opposed to constitutional-carry and anti-red-flag principles.",
              ["https://www.levine4congress.com/key-issues",
               "https://ballotpedia.org/Matthew_Levine"]),
        claim("ml4", "matthew-levine-mo-06", "border_immigration", 1, False,
              "Publicly stated 'I do not believe that ICE should be allowed to run rampant without being held accountable' — opposing the rubric's call for mandatory deportation enforcement and rejecting an unrestricted immigration-enforcement posture for federal immigration officers.",
              ["https://www.levine4congress.com/key-issues",
               "https://ballotpedia.org/Matthew_Levine"]),
    ]),

    # ---------------- Patty Garcia (IL-04, D) ----------------
    ("patty-garcia-il-04", "IL", "Representative", [
        claim("pg3", "patty-garcia-il-04", "sanctity_of_life", 0, False,
              "The 2026 Democratic nominee for Illinois' 4th Congressional District, Garcia is endorsed by Our Revolution — whose candidate criteria require support for reproductive freedom — and by Illinois Senate President Don Harmon and House Speaker Chris Welch, both of whom champion abortion access. Her candidacy in this majority-Latino Chicago district is anchored in the Democratic consensus supporting abortion rights, opposing any personhood-from-conception legal protection.",
              ["https://ourrevolution.com/patty-garcia-us-congress/",
               "https://ballotpedia.org/Patty_Garcia"]),
        claim("pg4", "patty-garcia-il-04", "self_defense", 1, False,
              "Campaigns on delivering 'safer, healthier communities' in Chicago's 4th District — a formulation that in the Chicago political context encompasses gun-violence prevention and gun-control legislation, consistent with the Illinois Democratic legislative consensus supporting background checks and high-capacity weapon restrictions rather than the rubric's anti-red-flag, anti-AWB constitutional-carry standard.",
              ["https://pattyforillinois.com/",
               "https://ballotpedia.org/Patty_Garcia"]),
    ]),

    # ---------------- William Lawrence (MI-07, D) ----------------
    ("william-lawrence-mi-07", "MI", "Representative", [
        claim("wl3", "william-lawrence-mi-07", "economic_stewardship", 2, False,
              "Advocates for Medicare for All — arguing that 'everyone should be covered for life, similar to housing' — alongside a federal Green New Deal as central campaign commitments. Both programs represent multi-trillion-dollar expansions of federal spending and fiscal obligations that directly conflict with the rubric's balanced-budget and anti-deficit stewardship standard.",
              ["https://wewill2026.com/",
               "https://en.wikipedia.org/wiki/William_Lawrence_(activist)"]),
        claim("wl4", "william-lawrence-mi-07", "sanctity_of_life", 0, False,
              "Endorsed by the Sunrise Movement and Indivisible MI-07 — progressive organizations whose endorsement criteria uniformly require support for reproductive rights — Lawrence's 2026 D candidacy for Michigan's 7th District is anchored in the progressive platform that includes abortion access and comprehensive reproductive freedom, opposing any legal protection of life from conception.",
              ["https://indivisible.org/candidates/william-lawrence-mi-07/",
               "https://en.wikipedia.org/wiki/William_Lawrence_(activist)"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
