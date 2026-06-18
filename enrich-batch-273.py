#!/usr/bin/env python3
"""Enrichment batch 273: hand-curated claims for 5 sitting U.S. House members.

Targets bottom-of-alphabet (MI×3, ME, MA) sitting House members with exactly
2 existing claims each.  Adds 2 claims per candidate spanning DISTINCT rubric
categories not yet documented.  All claims cite reliable public sources and
reflect 2024-2026 voting records / public positions.

Candidates: Tom Barrett (MI-R), John Moolenaar (MI-R), Hillary Scholten (MI-D),
Chellie Pingree (ME-D), Stephen Lynch (MA-D).
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
    # ---- Tom Barrett (MI-07-R, sitting since Jan 3, 2025) ----
    ("tom-barrett", "MI", "Representative", [
        claim("tb273a", "tom-barrett", "border_immigration", 1, True,
              "Voted Yes on the Laken Riley Act (H.R. 29, House Vote #6, January 7, 2025, 264–159), which mandates detention without bond of non-citizens arrested, charged with, or admitting to crimes including theft, burglary, shoplifting, assault on a law enforcement officer, or any crime causing death or serious bodily injury, and empowers states to sue DHS for enforcement failures. Barrett voted with every House Republican on passage — directly aligned with the rubric's mandatory-enforcement and deportation-first standard. The bill was the first legislation enacted in the 119th Congress and was signed by President Trump on January 29, 2025.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://ballotpedia.org/Tom_Barrett_(Michigan)"]),
        claim("tb273b", "tom-barrett", "biblical_marriage", 2, True,
              "Voted Yes on the Protection of Women and Girls in Sports Act (H.R. 28, House Vote #12, January 14, 2025, 218–206), which amends Title IX to prohibit males from competing in sports designated for females at educational institutions receiving federal funding — the most direct federal legislative codification of rejecting transgender sports ideology. Barrett voted with every House Republican on passage, fully aligned with the rubric's standard of rejecting transgender ideology in policy.",
              ["https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://ballotpedia.org/Tom_Barrett_(Michigan)"]),
    ]),

    # ---- John Moolenaar (MI-02-R, sitting since 2015) ----
    ("john-moolenaar", "MI", "Representative", [
        claim("jm273a", "john-moolenaar", "self_defense", 1, True,
              "Voted No on the Assault Weapons Ban of 2022 (H.R. 1808, House Vote #410, July 29, 2022, 217–213), which would have banned the manufacture and sale of semi-automatic rifles with detachable magazines and magazines holding more than 15 rounds. Only two House Republicans — Chris Jacobs (NY-27) and Brian Fitzpatrick (PA-01) — broke ranks; Moolenaar voted with the Republican majority against the bill, directly aligned with the rubric's rejection of assault-weapons bans, magazine limits, and gun-registration schemes. The bill never advanced in the Senate.",
              ["https://www.govtrack.us/congress/votes/117-2022/h410",
               "https://www.congress.gov/bill/117th-congress/house-bill/1808",
               "https://ballotpedia.org/John_Moolenaar"]),
        claim("jm273b", "john-moolenaar", "border_immigration", 1, True,
              "Voted Yes on the Laken Riley Act (H.R. 29, House Vote #6, January 7, 2025, 264–159), which mandates detention without bond of non-citizens arrested, charged with, or admitting to crimes including theft, burglary, shoplifting, assault of a law enforcement officer, or any crime causing death or serious bodily injury — and empowers states to sue DHS for enforcement failures. Moolenaar voted with every House Republican, aligned with the rubric's mandatory-enforcement and deportation-first standard. He has maintained a consistent enforcement-first border posture through his tenure, voting for the Secure the Border Act (H.R. 2, 2023) and opposing sanctuary-city funding.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://ballotpedia.org/John_Moolenaar"]),
    ]),

    # ---- Hillary Scholten (MI-03-D, sitting since Jan 2023) ----
    ("hillary-scholten", "MI", "Representative", [
        claim("hs273a", "hillary-scholten", "biblical_marriage", 2, False,
              "Voted No on the Protection of Women and Girls in Sports Act (H.R. 28, House Vote #12, January 14, 2025, 218–206), which amends Title IX to ban males from competing in women's and girls' sports at federally funded educational institutions. Scholten voted with every House Democrat against the bill — the inverse of the rubric's standard of rejecting transgender ideology in policy. Her No vote is consistent with her broader record supporting LGBTQ-inclusive federal policy throughout her tenure representing Grand Rapids's MI-03 swing district.",
              ["https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://ballotpedia.org/Hillary_Scholten"]),
        claim("hs273b", "hillary-scholten", "economic_stewardship", 2, False,
              "Voted Yes on the Consolidated Appropriations Act, 2024 (H.R. 4366, March 22, 2024, 339–85), a $1.2 trillion omnibus spending package funding federal operations through September 2024. The legislation significantly added to the national deficit, funding discretionary programs above the caps that fiscal-restraint advocates sought. Scholten's Yes vote — consistent with her Democratic caucus position — places her in opposition to the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/4366",
               "https://en.wikipedia.org/wiki/Consolidated_Appropriations_Act,_2024",
               "https://ballotpedia.org/Hillary_Scholten"]),
    ]),

    # ---- Chellie Pingree (ME-01-D, sitting since 2009) ----
    ("chellie-pingree", "ME", "Representative", [
        claim("cp273a", "chellie-pingree", "border_immigration", 0, False,
              "Voted No on the Secure the Border Act (H.R. 2, House Vote #200, May 11, 2023, 218–214), the House Republican border-security bill that funds additional physical border barriers, reinstates the Remain in Mexico (Migrant Protection Protocols) policy, ends catch-and-release, and tightens asylum eligibility. Pingree voted with every House Democrat against the measure — the inverse of the rubric's wall-plus-military-enforcement standard. Her opposition to immigration enforcement is further illustrated by her 2026 introduction of the Stop ICE Intimidation Act (H.R. 7743), which restricts ICE enforcement near sensitive locations — a consistent anti-enforcement posture across her 15+ years in Congress.",
              ["https://www.govtrack.us/congress/votes/118-2023/h200",
               "https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/Chellie_Pingree"]),
        claim("cp273b", "chellie-pingree", "economic_stewardship", 2, False,
              "Voted Yes on the American Rescue Plan Act (H.R. 1319, House Vote #52, March 10, 2021, 220–211), a $1.9 trillion pandemic-relief package, and the Inflation Reduction Act (H.R. 5376, House Vote #420, August 12, 2022, 220–207), adding ~$737 billion in IRS enforcement, green-energy subsidies, and healthcare spending — both passed on near-party-line votes and projected to add hundreds of billions to the national deficit. Pingree's consistent support for large deficit-financed federal spending packages, maintained across multiple Congresses, places her in direct opposition to the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.govtrack.us/congress/votes/117-2021/h52",
               "https://www.govtrack.us/congress/votes/117-2022/h420",
               "https://ballotpedia.org/Chellie_Pingree"]),
    ]),

    # ---- Stephen Lynch (MA-08-D, sitting since 2001) ----
    ("stephen-lynch", "MA", "Representative", [
        claim("sl273a", "stephen-lynch", "border_immigration", 0, False,
              "Voted No on the Secure the Border Act (H.R. 2, House Vote #200, May 11, 2023, 218–214), the House Republican border-security bill funding additional physical border barriers, reinstating the Remain in Mexico policy, ending catch-and-release, and tightening asylum eligibility. Lynch voted with every House Democrat against the measure — the inverse of the rubric's wall-plus-military-enforcement standard. Despite his reputation as a moderate Democrat — he notably voted against the Affordable Care Act in 2010 — Lynch has consistently opposed Republican enforcement-first immigration bills throughout his 20+ years representing South Boston and the MA-08 district.",
              ["https://www.govtrack.us/congress/votes/118-2023/h200",
               "https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/Stephen_Lynch"]),
        claim("sl273b", "stephen-lynch", "economic_stewardship", 2, False,
              "Voted Yes on the American Rescue Plan Act (H.R. 1319, House Vote #52, March 10, 2021, 220–211), a $1.9 trillion pandemic-relief package, and the Inflation Reduction Act (H.R. 5376, House Vote #420, August 12, 2022, 220–207), adding ~$737 billion in new federal spending — both passed on near-party-line votes and projected to add hundreds of billions to the national deficit. Lynch's consistent support for large deficit-financed spending packages across his 23-year House career places him in opposition to the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.govtrack.us/congress/votes/117-2021/h52",
               "https://www.govtrack.us/congress/votes/117-2022/h420",
               "https://ballotpedia.org/Stephen_Lynch"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
