#!/usr/bin/env python3
"""Enrichment batch 30: hand-curated claims for 4 federal House candidates.

Targets archetype_curated representatives that had 0 evidence claims, taken
from the bottom of the remaining alphabet bucket (TX → PA → OH).

Mix (4 R): Wesley Hunt (TX), Scott Perry (PA), Ryan Mackenzie (PA),
Warren Davidson (OH).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Wesley Hunt (TX, R, US Rep TX-38) ----------------
    ("wesley-hunt", "TX", "Representative", [
        claim("wh1", "wesley-hunt", "sanctity_of_life", 0, True,
              "Cosponsored H.R. 431, the Life at Conception Act (118th Congress, 2023), which would extend 14th Amendment equal-protection guarantees to unborn persons from the moment of fertilization — affirming life-begins-at-conception personhood.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/431/cosponsors",
               "https://www.govtrack.us/congress/bills/118/hr431/cosponsors"]),
        claim("wh2", "wesley-hunt", "self_defense", 1, True,
              "Introduced H.R. 6035, the Second Amendment Restoration Act (119th Congress, 2025), which repeals the Biden-era gun-control provisions inserted into the 2022 Bipartisan Safer Communities Act; the bill is endorsed by the NRA, Gun Owners of America, and National Association for Gun Rights.",
              ["https://hunt.house.gov/media/press-releases/congressman-wesley-hunt-introduced-second-amendment-restoration-act"]),
        claim("wh3", "wesley-hunt", "border_immigration", 0, True,
              "Publicly backs deploying U.S. military to the southern border and forcibly deporting illegal immigrants, and supports designating Mexican drug cartels as foreign terrorist organizations — a military-and-enforcement border posture.",
              ["https://hunt.house.gov/accomplishments-0"]),
    ]),

    # ---------------- Scott Perry (PA, R, US Rep PA-10) ----------------
    ("scott-perry", "PA", "Representative", [
        claim("sp1", "scott-perry", "sanctity_of_life", 0, True,
              "Cosponsored H.R. 431, the Life at Conception Act (118th Congress, 2023), asserting personhood and equal-protection rights for the unborn from the moment of fertilization.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/431/cosponsors"]),
        claim("sp2", "scott-perry", "economic_stewardship", 2, True,
              "His first bill as a congressman proposed a balanced budget amendment to the U.S. Constitution, and as House Freedom Caucus chairman (2021-2023) he consistently fought for spending cuts and against deficit-financed appropriations packages.",
              ["https://perry.house.gov/about-scott/default.aspx",
               "https://en.wikipedia.org/wiki/Scott_Perry_(politician)"]),
        claim("sp3", "scott-perry", "foreign_policy_restraint", 1, True,
              "Voted against Speaker Johnson's April 2024 supplemental foreign-aid packages — including the $61B Ukraine tranche and combined Taiwan/Israel/Ukraine bills — arguing against open-ended overseas military commitments and Congress's failure to exercise war-funding restraint.",
              ["https://en.wikipedia.org/wiki/Scott_Perry_(politician)",
               "https://ballotpedia.org/Scott_Perry"]),
    ]),

    # ---------------- Ryan Mackenzie (PA, R, US Rep PA-07) ----------------
    ("ryan-mackenzie", "PA", "Representative", [
        claim("rm1", "ryan-mackenzie", "sanctity_of_life", 0, True,
              "As a Pennsylvania state representative, voted for SB 106, a constitutional amendment establishing that there is no state right to taxpayer-funded abortion — a pro-life fiscal and legal position carried into his 2024 congressional campaign.",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/136465/ryan-mackenzie",
               "https://ballotpedia.org/Ryan_Mackenzie"]),
        claim("rm2", "ryan-mackenzie", "border_immigration", 2, True,
              "Sponsored H.Res. 1128 (119th Congress, March 2026) expressing the House's support for the Department of Homeland Security's border and interior enforcement operations, backing aggressive deportation and immigration enforcement.",
              ["https://www.congress.gov/bill/119th-congress/house-resolution/1128",
               "https://www.govtrack.us/congress/members/ryan_mackenzie/457017"]),
    ]),

    # ---------------- Warren Davidson (OH, R, US Rep OH-08) ----------------
    ("warren-davidson", "OH", "Representative", [
        claim("wd1", "warren-davidson", "sanctity_of_life", 0, True,
              "Consistently anti-abortion, opposing abortion in all cases except to save the mother's life — a life-from-conception position backed by a strong pro-life voting record throughout his congressional service since 2016.",
              ["https://en.wikipedia.org/wiki/Warren_Davidson",
               "https://ballotpedia.org/Warren_Davidson"]),
        claim("wd2", "warren-davidson", "border_immigration", 0, True,
              "Sponsored H.R. 8827 (119th Congress, 2025) to amend the Immigration and Nationality Act, replacing family-chain preferences with a national-interest standard, ending most family-sponsored categories, and tightening asylum procedures — a restrictionist enforcement-first approach.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/8827",
               "https://www.govtrack.us/congress/members/warren_davidson/412675"]),
        claim("wd3", "warren-davidson", "foreign_policy_restraint", 0, True,
              "Voted for a War Powers Resolution in March 2026 to restrain President Trump's military operations against Iran, asserting Congress's Article I authority over initiating hostilities — breaking with his party to defend constitutional limits on executive war-making.",
              ["https://en.wikipedia.org/wiki/Warren_Davidson",
               "https://www.govtrack.us/congress/members/warren_davidson/412675"]),
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
