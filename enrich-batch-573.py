#!/usr/bin/env python3
"""Enrichment batch 573: 5 South Dakota Republican state senators with 0 claims.

Targets archetype_party_default SD state senators taken from the BOTTOM of the
alphabet bucket (reverse-sorted by state then name): Stephanie Sauder (D-4),
Sam Marty (D-28), Randy Deibert (D-31), Paul Miskimins (D-20), Mykala Voita (D-21).

Sources: sdlegislature.gov, ballotpedia.org, samforsd.com, fastdemocracy.com,
freedomindex.us, sdpb.org, kornradio.com, keloland.com, southdakotasearchlight.com.
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
    # ---- Stephanie Sauder (SD-R, State Senator District 4) ----
    ("stephanie-sauder", "SD", "Senator", [
        claim("ss1", "stephanie-sauder", "family_child_sovereignty", 0, True,
              "Voted YES on SB 113 (SD 2025), the Parental Rights Affirmation Act, "
              "which affirms that a parent's right to care for and make decisions for "
              "their child is a fundamental liberty — bill passed 30-4 in the Senate "
              "on February 11, 2025.",
              ["https://sdlegislature.gov/Session/Bill/25805",
               "https://fastdemocracy.com/bill-search/sd/2025/bills/SDB00007020/"]),
        claim("ss2", "stephanie-sauder", "foreign_policy_restraint", 0, False,
              "Voted NO on SB 82 'Defend the Guard' (SD 2025), which would have "
              "required an official congressional declaration of war before the South "
              "Dakota National Guard could be deployed into combat — the bill was "
              "rejected 6-29 on February 3, 2025, with Sauder voting with the "
              "majority against restoring Article I war-powers authority.",
              ["https://freedomindex.us/legislator/10827",
               "https://blog.tenthamendmentcenter.com/2025/01/defend-the-guard-south-dakota-committee-passes-bill-moves-to-full-senate/"]),
    ]),

    # ---- Sam Marty (SD-R, State Senator District 28) ----
    ("sam-marty", "SD", "Senator", [
        claim("sm1", "sam-marty", "sanctity_of_life", 0, True,
              "Publicly states 'right to life' as a core governing principle on his "
              "official campaign platform, affirming protection of the unborn as a "
              "fundamental commitment. Marty is a Vietnam-era veteran and longtime "
              "South Dakota rancher who ran for SD Senate District 28 in 2024 on an "
              "explicitly pro-life platform.",
              ["https://www.samforsd.com/about-sam/",
               "https://ballotpedia.org/J._Sam_Marty"]),
        claim("sm2", "sam-marty", "economic_stewardship", 2, True,
              "Campaign platform explicitly lists 'a balanced budget' and 'control of "
              "government spending' as two of his seven core governing principles, "
              "reflecting a sustained commitment to fiscal discipline and opposition "
              "to deficit spending.",
              ["https://www.samforsd.com/about-sam/",
               "https://ballotpedia.org/J._Sam_Marty"]),
        claim("sm3", "sam-marty", "refuse_federal_overreach", 0, True,
              "Ran for Senate District 28 on a platform of 'limited government' and "
              "'property rights,' stating his goal is to ensure that 'the rights of "
              "private property owners are preserved' — a direct stand against federal "
              "and regulatory overreach into land and ranching operations.",
              ["https://www.samforsd.com/about-sam/",
               "https://ballotpedia.org/J._Sam_Marty"]),
    ]),

    # ---- Randy Deibert (SD-R, State Senator District 31, Majority Whip) ----
    ("randy-deibert", "SD", "Senator", [
        claim("rd1", "randy-deibert", "family_child_sovereignty", 0, False,
              "Voted NO on SB 113 (SD 2025), the Parental Rights Affirmation Act, "
              "which affirms a parent's fundamental liberty to care for and make "
              "decisions for their child — breaking with the conservative majority "
              "on a bill that passed 30-4 in the Senate on February 11, 2025.",
              ["https://sdlegislature.gov/Session/Bill/25805",
               "https://fastdemocracy.com/bill-search/sd/legislators/SDL000517/"]),
        claim("rd2", "randy-deibert", "election_integrity", 0, False,
              "Publicly opposed HB 1208 (SD 2025), a voter eligibility residency "
              "requirements bill aimed at closing loopholes for non-resident voters, "
              "arguing it would unfairly disenfranchise long-time South Dakota "
              "residents who travel — a stance against tightening voter-residency "
              "enforcement.",
              ["https://www.sdpb.org/politics/2025-03-10/senate-passes-bills-changing-voter-eligibility-residency-requirements",
               "https://ballotpedia.org/Randy_Deibert"]),
    ]),

    # ---- Paul Miskimins (SD-R, State Senator District 20) ----
    ("paul-miskimins", "SD", "Senator", [
        claim("pm1", "paul-miskimins", "family_child_sovereignty", 0, True,
              "Voted YES on SB 113 (SD 2025), the Parental Rights Affirmation Act, "
              "affirming that a parent's right to care for and make decisions for "
              "their child is a fundamental liberty — the bill passed 30-4 in the "
              "Senate on February 11, 2025.",
              ["https://sdlegislature.gov/Session/Bill/25805",
               "https://fastdemocracy.com/bill-search/sd/2025/bills/SDB00007020/"]),
        claim("pm2", "paul-miskimins", "industry_capture", 2, True,
              "A retired dentist who publicly supported HB 1056 (SD 2026), requiring "
              "the Department of Social Services to seek a federal SNAP waiver "
              "blocking taxpayer-funded nutrition benefits from being spent on "
              "sugary soft drinks — citing his clinical dental experience documenting "
              "health harms from Big Food's sugar products.",
              ["https://kornradio.com/news/state-senator-paul-miskimins-supports-hb-1056/",
               "https://www.mitchellrepublic.com/opinion/columns/miskimins-one-time-projects-getting-prioritized"]),
    ]),

    # ---- Mykala Voita (SD-R, State Senator District 21) ----
    ("mykala-voita", "SD", "Senator", [
        claim("mv1", "mykala-voita", "family_child_sovereignty", 0, True,
              "Voted YES on SB 113 (SD 2025), the Parental Rights Affirmation Act, "
              "affirming that a parent's fundamental liberty to care for and make "
              "decisions for their child is constitutionally protected — bill passed "
              "30-4 in the Senate on February 11, 2025. Voita earned an 83% "
              "constitutional score on the 2025 SD Freedom Index.",
              ["https://sdlegislature.gov/Session/Bill/25805",
               "https://thefreedomindex.org/sd/legislator/25663/votes/report-sd-scorecard-2025/pdf/scc/"]),
        claim("mv2", "mykala-voita", "economic_stewardship", 4, True,
              "Won her 2024 Republican primary for SD Senate District 21 by defeating "
              "incumbent Erin Tobin on a landowner-rights platform opposing eminent "
              "domain seizure for the Summit Carbon Solutions CO2 capture pipeline — "
              "a WEF/ESG-aligned corporate carbon project. Her campaign contributed "
              "to South Dakota's landmark 2025 eminent domain ban for CO2 pipelines "
              "(HB 1052, signed into law March 2025).",
              ["https://www.keloland.com/news/capitol-news-bureau/voita-tobin-are-spending-more-in-senate-rematch/",
               "https://southdakotasearchlight.com/2025/03/04/south-dakota-legislature-passes-eminent-domain-ban-for-carbon-pipelines/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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

    # Minified write — preserve the no-whitespace master (keep under GitHub's 50MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
