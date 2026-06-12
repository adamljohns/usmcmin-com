#!/usr/bin/env python3
"""Enrichment batch 146: hand-curated claims for 5 sitting U.S. Representatives.

All 5 are from Texas — taken from the bottom of the 0-claim bucket
(reverse-alphabetical collision-avoidance; top-of-alphabet agent handles
AK/AL/AR). archetype_curated federal senators/reps are exhausted; these are
archetype_party_default sitting TX House members.

Mix (5R): Lance Gooden (TX-05-R), Keith Self (TX-03-R),
Nathaniel Moran (TX-01-R), Craig Goldman (TX-12-R), Brandon Gill (TX-26-R).
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
    # ---------------- Lance Gooden (TX-05-R, US Representative) ----------------
    ("lance-gooden", "TX", "Representative", [
        claim("lg1", "lance-gooden", "sanctity_of_life", 0, True,
              "Proudly pro-life; at the 2020 March for Life stated '63 million unborn babies have lost their lives since Roe v. Wade' and pledged to 'stand with every pro-life American marching for those who cannot march for themselves' — affirming the value of unborn life from conception.",
              ["https://en.wikipedia.org/wiki/Lance_Gooden",
               "https://www.govtrack.us/congress/members/lance_gooden/412822"]),
        claim("lg2", "lance-gooden", "border_immigration", 2, True,
              "Introduced the End Sanctuary Cities Act of 2026 (H.R.7612, February 2026) to defund jurisdictions that harbor illegal aliens from federal enforcement; also reintroduced the No Tax Dollars for the UN's Immigration Invasion Act barring U.S. funding of UNRWA and UN migration agencies — a consistent anti-sanctuary legislative record.",
              ["https://www.congress.gov/member/lance-gooden/G000589",
               "https://www.govtrack.us/congress/members/lance_gooden/412822"]),
        claim("lg3", "lance-gooden", "election_integrity", 0, True,
              "Cosponsor of the SAVE Act in the 118th Congress (H.R.2584, joined May 2023), requiring documentary proof of U.S. citizenship to register to vote in federal elections — sustaining a consistent election-integrity position on voter eligibility verification.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2584/cosponsors",
               "https://ballotpedia.org/Lance_Gooden"]),
    ]),

    # ---------------- Keith Self (TX-03-R, US Representative) ----------------
    ("keith-self", "TX", "Representative", [
        claim("ks1", "keith-self", "sanctity_of_life", 0, True,
              "Rated 100% by the National Right to Life Committee; publicly declared 'The sonogram is the greatest tool in our fight against the barbarism and child sacrifice of the abortion industry' — an unequivocal pro-life, personhood-from-conception position.",
              ["https://en.wikipedia.org/wiki/Keith_Self",
               "https://ballotpedia.org/Keith_Self"]),
        claim("ks2", "keith-self", "self_defense", 0, True,
              "NRA life member who opposes gun-control mandates; advocates arming school staff and argues that prayer and mental-health investment — not firearm restrictions — address violent crime; a consistent constitutional-carry and Second Amendment defender.",
              ["https://en.wikipedia.org/wiki/Keith_Self",
               "https://www.govtrack.us/congress/members/keith_self/456941"]),
        claim("ks3", "keith-self", "border_immigration", 0, True,
              "Voted YES on H.R.1, the One Big Beautiful Bill Act (House Vote #190, July 3, 2025), which appropriated $46.5 billion for border-wall construction and authorized National Guard and military deployment to the southern border — backing wall-and-military border enforcement.",
              ["https://www.govtrack.us/congress/votes/119-2025/h190",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act"]),
    ]),

    # ---------------- Nathaniel Moran (TX-01-R, US Representative) ----------------
    ("nathaniel-moran", "TX", "Representative", [
        claim("nm1", "nathaniel-moran", "sanctity_of_life", 0, True,
              "SBA Pro-Life America gives Moran a perfect scorecard; he has voted consistently to protect unborn lives and block forced taxpayer funding of abortion throughout his congressional tenure, confirmed by the national pro-life tracking organization.",
              ["https://sbaprolife.org/representative/nathaniel-moran",
               "https://en.wikipedia.org/wiki/Nathaniel_Moran"]),
        claim("nm2", "nathaniel-moran", "family_child_sovereignty", 0, True,
              "Sponsored the Orderly Liquidation of the Department of Education Act (March 27, 2025) to abolish the federal Department of Education entirely and return education authority to states — restoring parental and local sovereignty over schooling, a core family-child-sovereignty position.",
              ["https://www.govtrack.us/congress/members/nathaniel_moran/456940",
               "https://en.wikipedia.org/wiki/Nathaniel_Moran"]),
    ]),

    # ---------------- Craig Goldman (TX-12-R, US Representative) ----------------
    ("craig-goldman", "TX", "Representative", [
        claim("cg1", "craig-goldman", "sanctity_of_life", 0, True,
              "Endorsed by SBA Pro-Life America in his 2024 congressional campaign; maintains a consistent pro-life legislative posture protecting unborn life from conception, consistent with the organization's strict pro-life screening criteria.",
              ["https://en.wikipedia.org/wiki/Craig_Goldman",
               "https://ballotpedia.org/Craig_Goldman"]),
        claim("cg2", "craig-goldman", "self_defense", 0, True,
              "Self-reported constitutional-carry voter: stated 'I voted to make Constitutional Carry the law in Texas, ensuring that you have the right to ensure your personal safety without government interference' as a Texas state representative; pledges to 'fiercely protect' Second Amendment rights in Congress.",
              ["https://ballotpedia.org/Craig_Goldman",
               "https://www.govtrack.us/congress/members/craig_goldman/457021"]),
        claim("cg3", "craig-goldman", "border_immigration", 1, True,
              "Publicly declared that illegal immigration 'makes a mockery of those who come here legally and respect our processes and our laws' and called 'rampant, unchecked illegal immigration an unsustainable burden to American taxpayers' — affirming a mandatory-enforcement, deportation-first immigration posture.",
              ["https://ballotpedia.org/Craig_Goldman",
               "https://en.wikipedia.org/wiki/Craig_Goldman"]),
    ]),

    # ---------------- Brandon Gill (TX-26-R, US Representative) ----------------
    ("brandon-gill", "TX", "Representative", [
        claim("bg1", "brandon-gill", "sanctity_of_life", 0, True,
              "Cosponsor of the Born-Alive Abortion Survivors Protection Act (H.R.21), cosponsored January 21, 2025 — two days before it passed the House 217-204 on January 23 — requiring medical care for infants born alive after failed abortions; affirms the sanctity of life at every stage.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/21/cosponsors",
               "https://en.wikipedia.org/wiki/Born-Alive_Abortion_Survivors_Protection_Act"]),
        claim("bg2", "brandon-gill", "border_immigration", 1, True,
              "Publicly supports mandatory mass deportations as a primary policy objective; introduced the Somalia Immigration Moratorium Act to pause immigration from Somalia and the Student Visa Integrity Act of 2026 to tighten student-visa oversight — a consistent deportation-and-enforcement-first immigration record.",
              ["https://en.wikipedia.org/wiki/Brandon_Gill",
               "https://www.congress.gov/member/brandon-gill/G000603"]),
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
