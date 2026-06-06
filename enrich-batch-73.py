#!/usr/bin/env python3
"""Enrichment batch 73: hand-curated claims for 5 bottom-of-alphabet archetype_curated candidates.

Targets (bottom-of-alpha + US federal officials): Todd Blanche (US-R, Acting AG),
Sean Duffy (US-R, Sec of Transportation), Scott Bessent (US-R, Sec of Treasury),
Scott Turner (US-R, Sec of HUD), Greg Abbott (TX-R, Governor).
Each claim cites >=1 reliable source and reflects 2024-2026 public positions.

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
    # ---------------- Todd Blanche (US-R, Acting Attorney General) ----------------
    ("todd-blanche", "US", "Attorney", [
        claim("tb1", "todd-blanche", "border_immigration", 2, True,
              "Signed the 'Operation Take Back America' memorandum as Deputy AG, directing all U.S. Attorneys and DOJ components to prosecute officials who obstruct federal immigration enforcement in sanctuary jurisdictions. The DOJ filed 14+ lawsuits against sanctuary cities (New York, Minnesota, Los Angeles, Boston, New Jersey, and others), making Blanche a leading federal enforcer against sanctuary obstruction.",
              ["https://www.justice.gov/dag/media/1393746/dl?inline=",
               "https://en.wikipedia.org/wiki/Todd_Blanche",
               "https://www.justice.gov/opa/pr/justice-department-files-lawsuit-against-washtenaw-county-michigan-interfering-federal-0"]),
        claim("tb2", "todd-blanche", "border_immigration", 1, True,
              "Within hours of being sworn in as Deputy Attorney General in January 2025, Blanche issued a memorandum shifting DOJ hiring to the Mexico-U.S. border to bolster Trump's mass-deportation campaign. He directed the reorganization of Organized Crime Drug Enforcement Task Forces and Project Safe Neighborhoods to prioritize immigration enforcement and removal of undocumented immigrants — a mandatory-deportation posture matching the rubric's standard.",
              ["https://en.wikipedia.org/wiki/Todd_Blanche",
               "https://www.justice.gov/usao-mdpa/operation-take-back-america"]),
    ]),

    # ---------------- Sean Duffy (US-R, Secretary of Transportation) ----------------
    ("sean-duffy", "US", "Transportation", [
        claim("sd1", "sean-duffy", "sanctity_of_life", 0, True,
              "As a Wisconsin congressman, Duffy introduced the Equal Right to Life Act (116th Congress) affirming the right to life from fertilization. He is a devout Catholic and father of nine children, with a consistent pro-life voting record in Congress (2011-2019) endorsed by National Right to Life; the NRA also endorsed him for his Second Amendment record.",
              ["https://en.wikipedia.org/wiki/Sean_Duffy",
               "https://ballotpedia.org/Sean_Duffy",
               "https://www.nrapvf.org/emails/2016/wisconsin/nra-pvf-endorses-sean-duffy-for-wi-07"]),
        claim("sd2", "sean-duffy", "biblical_marriage", 2, True,
              "As Secretary of Transportation, Duffy signed the 'Woke Rescission' Memorandum eliminating all Biden-era DEI, gender-identity, and environmental-justice directives from DOT programs and grant conditions; issued a mandatory Operations Specification requiring all commercial airlines to certify merit-based pilot hiring and end DEI practices; and launched an FAA investigation into prior DEI hiring — directly rejecting transgender and gender-identity ideology in a major federal agency.",
              ["https://www.transportation.gov/briefing-room/us-transportation-secretary-sean-duffy-takes-action-rescind-woke-dei-policies-and",
               "https://www.transportation.gov/briefing-room/trumps-us-transportation-secretary-sean-p-duffy-doubles-down-purging-dei-our-skies",
               "https://www.transportation.gov/briefing-room/icymi-transportation-secretary-sean-p-duffy-launches-investigation-dei-hiring-allegations"]),
    ]),

    # ---------------- Scott Bessent (US-R, Secretary of the Treasury) ----------------
    ("scott-bessent", "US", "Treasury", [
        claim("sb1", "scott-bessent", "economic_stewardship", 2, True,
              "Outlined a '3-3-3' economic framework committing to reduce the federal deficit to 3% of GDP within three years. At his Senate confirmation hearing Bessent stated the prior administration 'ran up the largest peacetime deficit in our nation's history' and that reducing the deficit was a primary motivation for entering public service; Treasury has since reported progress toward deficit reduction targets.",
              ["https://en.wikipedia.org/wiki/Scott_Bessent",
               "https://home.treasury.gov/news/press-releases/sb0466",
               "https://home.treasury.gov/news/press-releases/sb0521"]),
        claim("sb2", "scott-bessent", "economic_stewardship", 4, True,
              "Under Bessent's Treasury leadership, federal banking regulators ended the use of 'politicized reputation risk' — the ESG-driven practice of banks de-risking clients based on political or reputational criteria — and proposed to rescind the Biden-era Community Reinvestment Act rule that directed lending toward ESG-aligned outcomes. These actions push back against the WEF/ESG/Davos-style stakeholder-capitalism framework that the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Scott_Bessent",
               "https://home.treasury.gov/news/press-releases/sb0202"]),
    ]),

    # ---------------- Scott Turner (US-R, Secretary of Housing and Urban Development) ----------------
    ("scott-turner", "US", "Housing", [
        claim("st1", "scott-turner", "biblical_marriage", 2, True,
              "Signed the 'Restore Biological Truth and Sanity to HUD's Policies' directive removing gender-identity definitions and replacing them with biological sex across nearly 50 HUD regulations — the most comprehensive departmental rollback of gender-identity ideology in a domestic-policy agency, directly aligning with the rubric's rejection of transgender ideology.",
              ["https://www.hud.gov/news/hud-no-26-027",
               "https://en.wikipedia.org/wiki/Scott_Turner_(politician)"]),
        claim("st2", "scott-turner", "christian_liberty", 0, True,
              "Directed that faith-based housing providers will no longer be penalized for being faith-based organizations, reversing Biden-era HUD policies that had conditioned grants on compliance with LGBTQ non-discrimination mandates that conflicted with providers' religious convictions. Turner, an associate pastor at Prestonwood Baptist Church, has made protecting religious freedom in HUD programs a stated policy priority.",
              ["https://www.hud.gov/aboutus/leadership/scott-turner",
               "https://en.wikipedia.org/wiki/Scott_Turner_(politician)"]),
    ]),

    # ---------------- Greg Abbott (TX-R, Governor of Texas) ----------------
    ("greg-abbott", "TX", "Governor", [
        claim("ga1", "greg-abbott", "sanctity_of_life", 0, True,
              "Signed Texas Senate Bill 8 (the heartbeat bill, May 2021) protecting unborn children from abortion once a heartbeat is detected, and House Bill 1280 (the trigger-ban law) which took effect after Dobbs and prohibits nearly all abortions in Texas. Abbott has been a featured speaker at the Texas Rally for Life, affirming protection of human life from conception.",
              ["https://en.wikipedia.org/wiki/Greg_Abbott",
               "https://gov.texas.gov/news/post/governor-abbott-champions-protecting-unborn-at-texas-rally-for-life"]),
        claim("ga2", "greg-abbott", "border_immigration", 0, True,
              "Launched Operation Lone Star in 2021, deploying the Texas National Guard and Texas Department of Public Safety to the southern border. Signed legislation allocating $1.54 billion for construction of border barriers. In 2023-2024 initiated busing of migrants to Democratic-led cities and deployed razor-wire barriers along the Rio Grande, becoming the national leader in state-level military border enforcement.",
              ["https://en.wikipedia.org/wiki/Greg_Abbott",
               "https://gov.texas.gov/operationlonestar",
               "https://en.wikipedia.org/wiki/Operation_Lone_Star"]),
        claim("ga3", "greg-abbott", "self_defense", 0, True,
              "Signed House Bill 1927 (September 2021), making Texas a permitless-carry state allowing Texans to carry a handgun without a license or training — one of the largest Second Amendment expansions in Texas history. Abbott has also signed legislation strengthening castle-doctrine protections and consistently vetoed gun-control measures reaching his desk.",
              ["https://en.wikipedia.org/wiki/Greg_Abbott",
               "https://gov.texas.gov/news/post/governor-abbott-signs-second-amendment-legislation-into-law-2021"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
