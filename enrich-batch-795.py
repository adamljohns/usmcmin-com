#!/usr/bin/env python3
"""Enrichment batch 795: 4 candidates from bottom-of-alphabet states (VA/TX).

Federal Senate/House archetype_curated bucket exhausted; targets drawn from
evidence_federal (VA-07 2026 R primary candidates) and evidence_local (TX
local officials). 4 targets / 11 claims.

Targets:
  Ricky (Rick) Smithers  — VA-07 2026 R primary candidate (pastor/veteran)
  Philip Harding         — VA-07 2026 R primary candidate (entrepreneur)
  Phil Sorrells          — Tarrant County Criminal District Attorney (TX-R)
  Mattie Parker          — Mayor of Fort Worth, TX (R)

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
    # ----------- Ricky (Rick) Smithers (VA-R, VA-07 2026 primary candidate) -----------
    ("ricky-smithers", "VA", "VA-07", [
        claim("rs1", "ricky-smithers", "self_defense", 0, True,
              "At the June 17, 2026 Fredericksburg GOP candidate forum, Smithers strongly championed Second Amendment rights and specifically endorsed national concealed carry reciprocity, framing lawful armed self-defense as a core constituency priority — consistent with the rubric's constitutional-carry ideal.",
              ["https://www.potomaclocal.com/2026/06/19/republican-candidates-outline-priorities-on-energy-data-centers-and-parental-rights-at-fredericksburg-forum/",
               "https://www.fredericksburgfreepress.com/2026/06/19/gop-hopefuls-in-virginias-7th-district-talk-data-centers-priorities-if-elected/"]),
        claim("rs2", "ricky-smithers", "election_integrity", 0, True,
              "Calls passing the SAVE Act (Safeguard American Voter Eligibility Act) — requiring documentary proof of U.S. citizenship at voter registration and photo ID at the polls — a non-negotiable legislative priority, telling VPM News it is 'too important' to trade away in any negotiation.",
              ["https://www.vpm.org/elections/2026-07-07/va-07-us-house-republican-primary-harding-ollivant-smithers-vindman",
               "https://virginiamercury.com/2026/07/06/affordability-jobs-election-integrity-take-center-stage-in-va-s-7th-congressional-district-race/"]),
        claim("rs3", "ricky-smithers", "family_child_sovereignty", 0, True,
              "At the June 2026 Fredericksburg forum, Smithers stated that parents should be the final decision-makers in their children's education and called for sharply limited federal involvement in schooling — aligning with the rubric's parental-rights and anti-federal-curriculum position.",
              ["https://www.potomaclocal.com/2026/06/19/republican-candidates-outline-priorities-on-energy-data-centers-and-parental-rights-at-fredericksburg-forum/"]),
    ]),

    # ----------- Philip Harding (VA-R, VA-07 2026 primary candidate) -----------
    ("philip-harding", "VA", "VA-07", [
        claim("ph1", "philip-harding", "economic_stewardship", 2, True,
              "Identifies the national debt as an existential threat and frames runaway deficit spending as intergenerational theft: 'Trillions of dollars in debt is not compassion, it's theft from future generations.' His campaign centers on lower taxes, cutting wasteful spending, auditing federal inefficiencies, and applying private-sector discipline to government — aligning with the rubric's anti-deficit/balanced-budget position.",
              ["https://www.vpm.org/elections/2026-07-07/va-07-us-house-republican-primary-harding-ollivant-smithers-vindman",
               "https://www.washingtonexaminer.com/news/campaigns/state/4533130/philip-harding-republican-entrepreneur-virginia-7th-district/"]),
        claim("ph2", "philip-harding", "election_integrity", 0, True,
              "Supports the SAVE Act to require proof of U.S. citizenship at voter registration, and favors treating in-person voting as the norm with narrow accommodations for military and disabled voters — consistent with the rubric's voter-ID and anti-mass-mail-in standard.",
              ["https://www.vpm.org/elections/2026-07-07/va-07-us-house-republican-primary-harding-ollivant-smithers-vindman"]),
        claim("ph3", "philip-harding", "family_child_sovereignty", 0, True,
              "Campaign platform explicitly prioritizes 'strengthening families' and parental authority: 'If we can address the family, get back to strengthening the families, that's going to solve most of the downstream issues in our society.' Backs parental rights as final decision-makers in education with limited federal government involvement.",
              ["https://www.washingtonexaminer.com/news/campaigns/state/4533130/philip-harding-republican-entrepreneur-virginia-7th-district/",
               "https://www.potomaclocal.com/2026/06/19/republican-candidates-outline-priorities-on-energy-data-centers-and-parental-rights-at-fredericksburg-forum/"]),
    ]),

    # ----------- Phil Sorrells (TX-R, Tarrant County Criminal District Attorney) -----------
    ("phil-sorrells", "TX", "Criminal District Attorney", [
        claim("ps1", "phil-sorrells", "election_integrity", 0, True,
              "In February 2023, co-launched the Tarrant County Election Integrity Task Force alongside the county sheriff and county judge, dedicating investigators and a prosecutor to receive and pursue voter fraud complaints — affirming a commitment to secure elections consistent with the rubric's voter-ID/election-integrity standard.",
              ["https://www.keranews.org/news/2023-02-08/tarrant-county-officials-announce-efforts-to-fight-voter-fraud-even-as-election-crimes-remain-rare",
               "https://communityimpact.com/dallas-fort-worth/grapevine-colleyville-southlake/government/2023/02/14/tarrant-countys-election-integrity-task-force-to-oversee-election-complaints-fraud/"]),
        claim("ps2", "phil-sorrells", "border_immigration", 2, True,
              "Actively supports Tarrant County's 287(g) ICE partnership (approved by commissioners under Texas SB 8 in 2025) and his campaign platform states he will 'aggressively prosecute criminal conduct by illegal aliens and make every effort to detain them until they are deported,' rejecting any sanctuary posture — consistent with the rubric's anti-sanctuary position.",
              ["https://www.philsorrells.com/issues/",
               "https://www.fox4news.com/news/tarrant-county-commissioners-approve-ice-partnership"]),
        claim("ps3", "phil-sorrells", "self_defense", 1, False,
              "Filed an amicus brief with the U.S. Supreme Court in United States v. Rahimi (2023-24) supporting a federal law that strips firearm rights from persons under domestic violence protective orders — a gun restriction the Fifth Circuit had struck down as unconstitutional. The Supreme Court upheld the ban 8-1 in June 2024 and Sorrells praised the outcome. His record here favors a targeted firearm restriction rather than the rubric's standard of protecting all lawful gun possession.",
              ["https://fortworthreport.org/2023/07/25/us-supreme-court-case-from-arlington-alarms-domestic-violence-victim-advocates-law-enforcement-in-tarrant-county/",
               "https://fortworthreport.org/2024/06/25/supreme-court-upholds-arlington-gun-case-tarrant-county-officials-advocates-react/"]),
    ]),

    # ----------- Mattie Parker (TX-R, Mayor of Fort Worth) -----------
    ("mattie-parker", "TX", "Mayor", [
        claim("mp1", "mattie-parker", "self_defense", 1, False,
              "After the 2022 Uvalde massacre, publicly supported raising the minimum purchase age for semi-automatic rifles from 18 to 21, breaking with Texas GOP orthodoxy. Renewed that support after the 2023 Allen mall shooting, backing HB 2744 to ban rifle sales in that caliber/magazine class to buyers under 21. Her position favors a specific age-based firearm restriction that the rubric's anti-AWB/anti-age-restriction standard does not support.",
              ["https://fortworthreport.org/2022/06/07/fort-worth-mayor-wants-gun-reform-but-some-elected-officials-dont-see-it-happening/",
               "https://www.nbcdfw.com/news/local/fort-worth-mayor-mattie-parker-supports-raising-the-age-to-21-to-purchase-semi-automatic-weapons/3254489/"]),
        claim("mp2", "mattie-parker", "economic_stewardship", 2, True,
              "Has driven consistent property tax rate reductions in Fort Worth, directing city management in August 2024 to hold the FY2025 rate flat at 67.25 cents per $100 valuation and then cutting it further to 67 cents in FY2026 — publicly stating commitment to 'lowering the property tax rate while maintaining superior city services,' reflecting a fiscal discipline posture consistent with the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.keranews.org/government/2024-08-26/fort-worth-mayor-council-members-unite-against-raising-citys-property-tax-rate-in-2025",
               "https://www.keranews.org/government/2025-09-17/fort-worth-council-cuts-tax-rate-increases-service-fees-for-homeowners-in-2026-budget"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
