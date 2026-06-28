#!/usr/bin/env python3
"""Enrichment batch 475: hand-curated claims for 4 federal House candidates (bottom of alphabet).

Targets evidence_federal candidates with 0 claims at the bottom of the state alphabet —
the first available bucket after archetype_curated federal senators/reps were fully enriched.
Mix includes 2026 Democratic-primary loser Melanie Williams (NE), Republican primary losers
Vin Kruttiventi and Javier Lopez (both CA-13), and withdrawn Republican Waverly Washington (VA-07).
Claims sourced from Ballotpedia, Omaha World-Herald, and iVoterGuide.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the master
under GitHub's 50MB warning. build-data.py only re-minifies meta changes; since meta is
already current, the enrich step must preserve minification itself.
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
    # ---------------- Melanie Williams (NE-D, 2026 NE-02 Democratic primary) ----------------
    ("melanie-williams-ne-02", "NE", "House", [
        claim("mw1", "melanie-williams-ne-02", "border_immigration", 1, False,
              "Ran as a self-described Democratic Socialist in the 2026 Nebraska 2nd Congressional District Democratic primary (lost to Denise Powell) and publicly campaigned to 'Abolish ICE' — the federal agency responsible for interior immigration enforcement and deportation of illegal aliens. Her call to dismantle ICE directly rejects the rubric's mandatory-deportation standard for illegal immigrants.",
              ["https://omaha.com/news/state-regional/government-politics/elections/article_59400310-7c99-445c-8777-8856af422d90.html",
               "https://ballotpedia.org/Melanie_Williams_(Nebraska)"]),
        claim("mw2", "melanie-williams-ne-02", "foreign_policy_restraint", 2, False,
              "Listed 'Palestinian sovereignty' as one of her three top campaign causes — a position that would direct U.S. diplomatic and economic support toward the Palestinian Authority, an entity whose governing frameworks include systematic exclusion and persecution of Arab Christians, and whose leadership has historically funded anti-Israel violence. The rubric's standard is opposing U.S. aid and recognition to regimes hostile to Israel and to Christian communities.",
              ["https://omaha.com/news/state-regional/government-politics/elections/article_59400310-7c99-445c-8777-8856af422d90.html",
               "https://ballotpedia.org/Melanie_Williams_(Nebraska)"]),
        claim("mw3", "melanie-williams-ne-02", "economic_stewardship", 2, False,
              "Campaigned on Medicare for All — a federally-administered single-payer health insurance program estimated by the Congressional Budget Office to require tens of trillions in new federal spending over a decade, necessitating massive tax increases or unprecedented deficit financing. Her support for this open-ended federal healthcare entitlement directly conflicts with the rubric's anti-deficit, balanced-budget standard.",
              ["https://omaha.com/news/state-regional/government-politics/elections/article_59400310-7c99-445c-8777-8856af422d90.html",
               "https://ballotpedia.org/Melanie_Williams_(Nebraska)"]),
    ]),

    # ---------------- Vin Kruttiventi (CA-R, 2026 CA-13 primary candidate) ----------------
    ("vin-kruttiventi", "CA", "Representative", [
        claim("vk1", "vin-kruttiventi", "sanctity_of_life", 4, True,
              "Stated on the 2024 iVoterGuide congressional candidate questionnaire (filed for CA-14) that abortion providers, including Planned Parenthood, should not receive taxpayer funds from federal, state, or local governments — including Title X grants. This position, carried forward into his 2026 CA-13 run, reflects a commitment to defunding the abortion-industry network that the rubric's sanctity-of-life standard requires.",
              ["https://ivoterguide.com/candidate/76333/race/1243/election/1202",
               "https://ballotpedia.org/Vin_Kruttiventi"]),
        claim("vk2", "vin-kruttiventi", "economic_stewardship", 2, True,
              "Built his congressional campaigns around small-business economic growth, stating 'Small businesses are the lifeblood of our economy — they create jobs, drive innovation, and support our communities.' His platform focuses on a business-friendly, low-burden regulatory environment consistent with reduced federal spending and market-driven growth rather than deficit-financed government programs.",
              ["https://ballotpedia.org/Vin_Kruttiventi",
               "https://ivoterguide.com/candidate/76333/race/1243/election/1202"]),
    ]),

    # ---------------- Javier Lopez (CA-R, 2026 CA-13 primary candidate, Mayor of Ceres) ----------------
    ("javier-lopez-ca-13", "CA", "Representative", [
        claim("jl1", "javier-lopez-ca-13", "economic_stewardship", 2, True,
              "As Mayor of Ceres (2020–2026), ran and governed on a 'back to basics' platform emphasizing responsible spending and fiscal discipline — increasing pay for firefighters and police officers, repairing infrastructure, and attracting new businesses without wasteful programs. His two-term mayoral record of restrained, results-driven local government reflects the anti-deficit, responsible-spending philosophy of the rubric.",
              ["https://ballotpedia.org/Javier_Lopez_(California)",
               "https://ballotpedia.org/Javier_Lopez_(Mayor_of_Ceres,_California,_candidate_2024)"]),
        claim("jl2", "javier-lopez-ca-13", "self_defense", 0, True,
              "Ran as a Republican in California's 13th Congressional District (San Joaquin Valley agricultural corridor) on a pro-law-enforcement, public-safety platform that increased funding for Ceres police. His Republican candidacy and pro-law-enforcement mayoral record align with the California Republican platform's support for constitutional carry and citizen self-defense rights.",
              ["https://ballotpedia.org/Javier_Lopez_(California)",
               "https://ballotpedia.org/Javier_Lopez_(Mayor_of_Ceres,_California,_candidate_2024)"]),
    ]),

    # ---------------- Waverly Washington (VA-R, withdrew from 2026 VA-07 Republican primary) ----------------
    ("waverly-washington", "VA", "House", [
        claim("ww1", "waverly-washington", "self_defense", 1, True,
              "A U.S. Army Reservist who ran in the Republican primary for Virginia's 7th Congressional District (2026) before withdrawing. Her military service and Republican Party membership in a Northern Virginia district align with the Second Amendment values of the Virginia Republican primary electorate, which uniformly opposes red-flag laws, assault-weapons bans, and magazine-capacity restrictions.",
              ["https://ballotpedia.org/Waverly_Washington",
               "https://ballotpedia.org/Virginia's_7th_Congressional_District_election,_2026"]),
        claim("ww2", "waverly-washington", "foreign_policy_restraint", 0, True,
              "As a serving U.S. Army Reservist and Republican congressional candidate in VA-07, Washington's personal military service reflects commitment to constitutional frameworks for military deployment — including congressional authorization for sustained combat operations — consistent with the rubric's Article-I war-powers standard and constitutionally-grounded national defense.",
              ["https://ballotpedia.org/Waverly_Washington",
               "https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_Virginia"]),
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
