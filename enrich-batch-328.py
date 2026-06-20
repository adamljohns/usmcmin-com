#!/usr/bin/env python3
"""Enrichment batch 328: third claim for 5 evidence_curated federal candidates.

Targets evidence_curated federal candidates with exactly 2 existing claims,
taken from the bottom of the alphabet (MT, NJ, MS). All archetype_curated
federal senator/rep slots are exhausted; these are next-ripe targets.

Mix (0 R / 5 D): Monica Tranel (MT-D, MT Senate), Matt Rains (MT-D, MT-01),
Rob Menendez (NJ-D, NJ House), Shanel Robinson (NJ-D, NJ-12),
Mike Espy (MS-D, MS Senate).

Each claim adds a DISTINCT rubric category not already represented for that
candidate. Sources: ballotpedia.org, bozemandailychronicle.com,
montanafreepress.org, robmenendez.com, insidernj.com, mississippitoday.org.

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
    # ------------ Monica Tranel (MT-D, 2026 MT Senate / 2022+2024 MT-AL) ------------
    # Existing claims: sanctity_of_life[0] (abortion, False),
    #                  economic_stewardship[2] (deficit spending, False)
    # Adding: self_defense[1] (anti red-flag/AWB/mag-limit/registry)
    ("monica-tranel-mt-senate", "MT", "Senate", [
        claim("mt-sd1", "monica-tranel-mt-senate", "self_defense", 1, False,
              "In her 2022 and 2024 Montana At-Large congressional campaigns, Tranel "
              "explicitly stated she would support legislation making it harder for "
              "'dangerous people to buy a gun,' including universal criminal background "
              "checks and red flag laws. A Bozeman Daily Chronicle candidate forum on "
              "firearms policy quoted her endorsing red flag / Extreme Risk Protection "
              "Order laws, arguing they would not impact 'the majority of Montana's gun "
              "owners.' These positions — active support for red-flag ERPOs and expanded "
              "background-check mandates — are contrary to the anti-red-flag/AWB/registry "
              "standard.",
              ["https://ballotpedia.org/Monica_Tranel",
               "https://www.bozemandailychronicle.com/news/elections/candidates-in-western-house-race-discuss-firearms-policy/article_5a0a5da4-cb94-53e0-bc42-303745548c1e.html"]),
    ]),

    # ------------ Matt Rains (MT-D, MT-01 open-seat candidate, LOST 2026 D primary) ------------
    # Existing claims: sanctity_of_life[0] (abortion, False),
    #                  refuse_federal_overreach[0] (Medicaid cuts, False)
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("matt-rains-mt-01", "MT", "Representative", [
        claim("mr-es2", "matt-rains-mt-01", "economic_stewardship", 2, False,
              "Rains made preserving federal healthcare entitlements a signature campaign "
              "theme, stating 'we are spending over a billion dollars a day on this war, "
              "all while President Trump cuts Medicaid, forces rural hospitals to close "
              "and strips Montanans of their health care.' His top affordability priorities "
              "included affordable housing programs and opposing federal Medicaid budget "
              "cuts — an agenda of maintaining or expanding federal entitlement spending "
              "that runs counter to balanced-budget and debt-reduction fiscal principles.",
              ["https://montanafreepress.org/2026/04/27/four-brands-of-democrat-make-their-case-in-montanas-western-congressional-primary/",
               "https://projects.montanafreepress.org/election-guide-2026/candidates/matt-rains/"]),
    ]),

    # ------------ Rob Menendez (NJ-D, US House NJ-08) ------------
    # Existing claims: sanctity_of_life[0] (abortion, False),
    #                  sanctity_of_life[4] (NARAL/RF4A funding, False)
    # Adding: self_defense[1] (anti red-flag/AWB/mag-limit/registry)
    ("rob-menendez", "NJ", "House", [
        claim("rm-sd1", "rob-menendez", "self_defense", 1, False,
              "Since taking office in January 2023, Rep. Menendez has cosponsored more "
              "than twenty gun violence prevention bills, including the Assault Weapons "
              "Ban, the Federal Extreme Risk Protection Order Act (a red flag law), and "
              "the Bipartisan Background Checks Act. His campaign website's gun-control "
              "page lists these as top legislative priorities. These positions — active "
              "support for an assault weapons ban, red-flag ERPOs, and expanded background "
              "check legislation — are directly contrary to the anti-AWB/anti-red-flag "
              "standard.",
              ["https://www.robmenendez.com/issues/gun-control/",
               "https://ballotpedia.org/Rob_Menendez"]),
    ]),

    # ------------ Shanel Robinson (NJ-D, NJ-12 2026 D candidate) ------------
    # Existing claims: self_defense[1] (assault weapons restrictions, False),
    #                  biblical_marriage[4] (LGBTQ promotion, False)
    # Adding: sanctity_of_life[0] (life-at-conception/personhood)
    ("shanel-robinson", "NJ", "Representative", [
        claim("sr-sol0", "shanel-robinson", "sanctity_of_life", 0, False,
              "As Somerset County Commissioner Director, Robinson co-signed an official "
              "board press release on the second anniversary of Dobbs v. Jackson Women's "
              "Health Organization condemning the Supreme Court's ruling and warning of "
              "'threats to reproductive freedoms.' The statement explicitly noted that "
              "'access to abortion reduces maternal mortality and teen pregnancy.' "
              "She runs for Congress as a pro-choice candidate who supports protecting "
              "abortion access — a position directly contrary to a life-at-conception "
              "or personhood standard.",
              ["https://www.insidernj.com/press-release/the-female-majority-of-the-somerset-county-commissioner-board-commissioner-director-shanel-robinson-commissioner-deputy-sector-sara-sooy-and-commissioner-melonie-marano-released-the-following-st/",
               "https://ballotpedia.org/Shanel_Robinson"]),
    ]),

    # ------------ Mike Espy (MS-D, 2026 MS Senate candidate) ------------
    # Existing claims: sanctity_of_life[0] (abortion self-described, False-ish),
    #                  border_immigration[0] (wall, False)
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget)
    ("mike-espy-senate-2026", "MS", "Senate", [
        claim("me-es2", "mike-espy-senate-2026", "economic_stewardship", 2, False,
              "Espy's 2020 Mississippi Senate campaign called for expanding Medicaid "
              "and strengthening the Affordable Care Act, with Mississippi Today's "
              "issues guide documenting him as 'working to expand Medicaid, to increase "
              "the minimum wage, and to ensure people with pre-existing conditions have "
              "access to health insurance.' These are proposals to grow federal entitlement "
              "obligations and spending — running counter to balanced-budget and "
              "national-debt-reduction fiscal principles despite his rhetorical "
              "self-description as a 'deficit and debt hawk.'",
              ["https://mississippitoday.org/2020/09/09/heres-where-cindy-hyde-smith-and-mike-espy-stand-on-healthcare-ahead-of-senate-race/",
               "https://mississippitoday.org/2020/09/24/mike-espy-bio/"]),
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
