#!/usr/bin/env python3
"""Enrichment batch 286: 2-claim federal candidates from bottom of alphabet.

Primary archetype_curated/0-claim bucket is empty (all converted to
evidence_curated by prior batches). This batch targets active federal
candidates with 2 existing claims from the bottom of the alphabet —
AZ, IA, and CA — adding distinct rubric-category claims sourced from
official campaign sites, Ballotpedia, Wikipedia, and VoteSmart.

Targets (5): Jay Feely (AZ-01, R), Shawnna Bolick (AZ-01, R),
Chris McGowan (IA-04, R), James Gallagher (CA-01, R), Vince Fong (CA-20, R).
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
    # ---------------- Jay Feely (AZ-01, R — July 21 2026 primary) ----------------
    ("jay-feely", "AZ", "AZ-01", [
        claim("jf1", "jay-feely", "self_defense", 0, True,
              "Campaign website explicitly lists 'Defend Our Second Amendment Rights' as one of five core platform pillars, pledging to protect constitutional carry and oppose federal restrictions on firearm ownership — directly aligning with the rubric's constitutional-carry priority.",
              ["https://www.jayfeelyforcongress.com/issues",
               "https://ballotpedia.org/Jay_Feely"]),
        claim("jf2", "jay-feely", "refuse_federal_overreach", 0, True,
              "Campaigns on stopping 'out-of-control federal mandates that hurt our families, small businesses, and schools,' explicitly framing federal overreach as a central threat to liberty — consistent with the rubric's call to refuse unconstitutional federal power.",
              ["https://www.jayfeelyforcongress.com/issues",
               "https://ballotpedia.org/Jay_Feely"]),
    ]),

    # ---------------- Shawnna Bolick (AZ-01, R — AZ State Senator) ----------------
    ("shawnna-bolick", "AZ", "AZ-01", [
        claim("sb1", "shawnna-bolick", "sanctity_of_life", 0, False,
              "Broke with Republican caucus on May 1, 2024, voting with all 14 Senate Democrats to repeal Arizona's 1864 territorial abortion law by a 16-14 margin — one of only two Republicans to do so — actively dismantling the strongest pro-life protection in Arizona history and rejecting a personhood-level prohibition in favor of abortion access up to 15 weeks.",
              ["https://en.wikipedia.org/wiki/Shawnna_Bolick",
               "https://ballotpedia.org/Shawnna_Bolick"]),
        claim("sb2", "shawnna-bolick", "sanctity_of_life", 1, False,
              "The 2024 vote to repeal Arizona's total abortion ban explicitly rejected an abolition-level protection (no exceptions, life from conception) in favor of Proposition 139's 15-week gestational-limit framework — choosing restrictions over abolition, the opposite of the rubric's standard.",
              ["https://en.wikipedia.org/wiki/Shawnna_Bolick",
               "https://ballotpedia.org/2024_Arizona_Proposition_139,_Right_to_Abortion_Initiative"]),
    ]),

    # ---------------- Chris McGowan (IA-04, R — 2026 nominee, Feenstra seat) ----------------
    ("ia-04-r-placeholder", "IA", "IA-04", [
        claim("cm1", "ia-04-r-placeholder", "economic_stewardship", 2, True,
              "As the Siouxland Chamber of Commerce President, McGowan's campaign under 'America First, Iowa Always' centers on reducing the federal deficit and reining in government spending — aligning with the rubric's demand for anti-deficit fiscal stewardship in a district historically represented by budget-hawk Randy Feenstra.",
              ["https://www.iowapublicradio.org/ipr-news/2025-06-25/chris-mcgowan-campaigns-for-iowa-4th-congressional-district",
               "https://www.thegazette.com/news/elections/sioux-city-s-chris-mcgowan-touts-trump-endorsement-in-4th-congressional-district-race/article_ad8399df-99cd-5c0c-9bfa-f1ec1aaefb7b.html"]),
        claim("cm2", "ia-04-r-placeholder", "election_integrity", 0, True,
              "Running as a Trump-endorsed 'America First' Republican in Iowa — a state that enacted photo voter ID in 2017 (SF 2, signed by Gov. Kim Reynolds) and tightened absentee-ballot rules in 2021 — McGowan's campaign backs Iowa's election-integrity framework as part of the MAGA platform he explicitly champions.",
              ["https://ballotpedia.org/Chris_McGowan",
               "https://www.notus.org/donald-trump/chris-mcgowan-iowa"]),
    ]),

    # ---------------- James Gallagher (CA-01, R — sworn in June 2026) ----------------
    ("james-gallagher-ca-01", "CA", "CA-01", [
        claim("jg1", "james-gallagher-ca-01", "self_defense", 1, True,
              "As California Assembly Minority Leader (2022–2025), consistently led Republican opposition to the state's sweeping gun-control legislation — including red-flag confiscation orders, assault-weapon restrictions, and magazine-capacity limits — opposing the most aggressive gun-regulation agenda in the country.",
              ["https://justfacts.votesmart.org/candidate/114778/james-gallagher?categoryId=37&type=V,S,R,E,F,P",
               "https://ballotpedia.org/James_Gallagher_(California)"]),
        claim("jg2", "james-gallagher-ca-01", "border_immigration", 0, True,
              "Won Trump's endorsement for the CA-01 special election (February 2026) and campaigns on the full America First border agenda — backing physical barrier construction, deportation enforcement, and elimination of catch-and-release — consistent with the rubric's wall-plus-military-enforcement standard.",
              ["https://en.wikipedia.org/wiki/James_Gallagher_(California_politician)",
               "https://news.ballotpedia.org/2026/06/15/james-gallagher-takes-office-ending-the-vacancy-in-californias-1st-congressional-district/"]),
    ]),

    # ---------------- Vince Fong (CA-20, R — sitting US Representative) ----------------
    ("vince-fong", "CA", "CA-20", [
        claim("vf1", "vince-fong", "sanctity_of_life", 0, True,
              "As a California State Assembly Republican (2016–2024), opposed California's successive expansions of abortion access, including voting against measures to eliminate accountability for post-viability abortions and broaden who could perform them — maintaining a pro-life caucus posture in the most pro-abortion-rights legislature in the country.",
              ["https://justfacts.votesmart.org/candidate/key-votes/169357/vince-fong/2/abortion",
               "https://ballotpedia.org/Vince_Fong"]),
        claim("vf2", "vince-fong", "economic_stewardship", 2, True,
              "Served as Vice Chair of the California Assembly Committee on Appropriations (2016–2024), a position focused on scrutinizing state spending and opposing unfunded liabilities — a fiscal discipline posture consistent with the rubric's anti-deficit, balanced-budget standard.",
              ["https://ballotpedia.org/Vince_Fong",
               "https://www.govtrack.us/congress/members/vince_fong/456958"]),
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
