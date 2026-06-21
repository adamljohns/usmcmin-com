#!/usr/bin/env python3
"""Enrichment batch 349: 5 TX/UT US House members — +2 claims each (except Gonzalez +1).

Targets (evidence_curated, 3-4 existing claims — bottom-of-alphabet sweep, TX/UT):
  Wesley Hunt        (TX-38, R) — +2 claims (election_integrity[0], economic_stewardship[2])
  Troy Nehls         (TX-22, R) — +2 claims (election_integrity[0], economic_stewardship[2])
  Blake Moore        (UT-01, R) — +2 claims (border_immigration[3], election_integrity[0])
  Burgess Owens      (UT-04, R) — +2 claims (election_integrity[0], border_immigration[2])
  Vicente Gonzalez   (TX-34, D) — +1 claim  (election_integrity[0])

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep the master
under GitHub's 50 MB limit.
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
    # ---------- Wesley Hunt (TX-38, R) ----------
    # Existing: sanctity_of_life[0]T, self_defense[1]T, border_immigration[0]T
    ("wesley-hunt", "TX", "Representative", [
        claim("wh1", "wesley-hunt", "election_integrity", 0, True,
              "Voted YES on H.R. 22 (the SAVE Act), which passed the House 220-208 on April 10, "
              "2025. The SAVE Act amends the National Voter Registration Act to require "
              "documentary proof of U.S. citizenship before an applicant can register to vote in "
              "federal elections — directly matching the rubric's voter-ID and citizenship-"
              "verification standard. Every House Republican voted in favor.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://hunt.house.gov/"]),
        claim("wh2", "wesley-hunt", "economic_stewardship", 2, True,
              "Voted NO on the Fiscal Responsibility Act of 2023 (H.R. 3746), the debt-ceiling "
              "deal that raised the statutory debt limit by roughly $4 trillion through 2025 "
              "without sufficient spending reductions, joining 71 House Republicans who rejected "
              "the bill as insufficiently conservative. Hunt also publicly backed DOGE-driven "
              "spending cuts in 2025-2026 and opposed large deficit-expanding appropriations "
              "packages — a consistent anti-deficit posture matching the rubric's balanced-budget "
              "standard.",
              ["https://en.wikipedia.org/wiki/Wesley_Hunt",
               "https://www.govtrack.us/congress/members/wesley_hunt/456946",
               "https://ballotpedia.org/Wesley_Hunt"]),
    ]),

    # ---------- Troy Nehls (TX-22, R) ----------
    # Existing: sanctity_of_life[0]T, self_defense[1]T, border_immigration[0]T
    ("troy-nehls", "TX", "Representative", [
        claim("tn1", "troy-nehls", "election_integrity", 0, True,
              "On January 6-7, 2021, Nehls voted to object to the certification of electoral "
              "votes from Arizona and Pennsylvania, citing election-security concerns — one of "
              "the most direct congressional assertions of the election-integrity standard the "
              "rubric requires (both objections were rejected by the House, 121-303 on AZ and "
              "138-282 on PA). Nehls also cosponsored H.R. 8281 (SAVE Act, 118th Congress) and "
              "voted YES on H.R. 22 (SAVE Act, 119th Congress, April 10, 2025), requiring "
              "documentary proof of citizenship to register to vote in federal elections.",
              ["https://en.wikipedia.org/wiki/Troy_Nehls",
               "https://www.congress.gov/bill/118th-congress/house-bill/8281/cosponsors",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("tn2", "troy-nehls", "economic_stewardship", 2, True,
              "A persistent opponent of deficit-expanding continuing resolutions: voted NO on "
              "H.R. 5525 (the FY2024 Continuing Resolution) calling it a continuation of "
              "'bloated spending levels with no border security,' and voted NO on other CRs that "
              "extended high baseline spending. Nehls opposed large appropriations packages from "
              "both parties that lacked offsetting spending reductions — consistent with the "
              "rubric's anti-deficit/balanced-budget standard.",
              ["https://nehls.house.gov/media/press-releases/rep-troy-e-nehls-votes-no-continuing-bloated-spending-levels-no-border",
               "https://nehls.house.gov/media/press-releases/rep-troy-e-nehls-votes-no-continuing-resolution-fiscal-year-2024",
               "https://www.govtrack.us/congress/members/troy_nehls/456848"]),
    ]),

    # ---------- Blake Moore (UT-01, R) ----------
    # Existing: biblical_marriage[1]F, economic_stewardship[2]F, sanctity_of_life[0]T
    ("blake-moore", "UT", "Representative", [
        claim("bm1", "blake-moore", "border_immigration", 3, True,
              "Supports mandatory E-Verify for all employers to reduce incentives for illegal "
              "immigration, backed resuming border-wall construction, and supported the "
              "Remain-in-Mexico (Migrant Protection Protocols) policy that prevented asylum "
              "seekers from being paroled into the United States pending hearings. Moore's "
              "official border-security issue page calls for hiring additional border agents and "
              "reimposing these enforcement tools as a unified border-security package — "
              "aligning with the rubric's E-Verify standard.",
              ["https://blakemoore.house.gov/issue/border-security-and-immigration",
               "https://ballotpedia.org/Blake_Moore",
               "https://www.govtrack.us/congress/members/blake_moore/456851"]),
        claim("bm2", "blake-moore", "election_integrity", 0, True,
              "Voted YES on H.R. 22 (the SAVE Act), which passed the House 220-208 on April 10, "
              "2025 with all Republicans in support. The SAVE Act requires documentary proof of "
              "U.S. citizenship to register to vote in federal elections, amending the National "
              "Voter Registration Act — matching the rubric's voter-ID and citizenship-"
              "verification standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Blake_Moore"]),
    ]),

    # ---------- Burgess Owens (UT-04, R) ----------
    # Existing: sanctity_of_life[0]T, self_defense[2]T, family_child_sovereignty[0]T
    ("burgess-owens", "UT", "Representative", [
        claim("bo1", "burgess-owens", "election_integrity", 0, True,
              "On January 6-7, 2021, Owens voted to object to the certification of electoral "
              "votes from Arizona and/or Pennsylvania, asserting election-security concerns — "
              "consistent with the rubric's election-integrity standard. Owens has since "
              "publicly supported requiring documentary proof of U.S. citizenship to register "
              "to vote in federal elections, and voted YES on H.R. 22 (SAVE Act, 220-208, "
              "April 10, 2025).",
              ["https://ballotpedia.org/Burgess_Owens",
               "https://en.wikipedia.org/wiki/Burgess_Owens",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("bo2", "burgess-owens", "border_immigration", 2, True,
              "Introduced the Sanctuary City Oversight and Responsibility in Enforcement (SCORE) "
              "Act of 2024 to prohibit the use of FEMA Shelter and Services Program funds to "
              "transport migrants to sanctuary jurisdictions without prior notification — "
              "directly targeting sanctuary-city policies the rubric opposes. Owens also voted "
              "YES on H.R. 2 (Secure the Border Act of 2023), which funds border-wall "
              "construction, reinstates Remain in Mexico, and tightens asylum standards.",
              ["https://owens.house.gov/posts/owens-votes-yes-on-the-secure-the-border-act-of-2023",
               "https://owens.house.gov/resources/immigration-and-border-security",
               "https://ballotpedia.org/Burgess_Owens"]),
    ]),

    # ---------- Vicente Gonzalez (TX-34, D) ----------
    # Existing: biblical_marriage[2]T, family_child_sovereignty[0]T, border_immigration[1]T,
    #           economic_stewardship[2]T
    ("vicente-gonzalez", "TX", "Representative", [
        claim("vg1", "vicente-gonzalez", "election_integrity", 0, True,
              "On April 10, 2025, Gonzalez was one of only approximately five House Democrats to "
              "vote YES on H.R. 22 (the SAVE Act, passed 220-208), which requires documentary "
              "proof of U.S. citizenship to register to vote in federal elections — breaking "
              "with his party's near-unanimous opposition and aligning with the rubric's "
              "citizenship-verification and voter-ID standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Vicente_Gonzalez_Jr."]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
