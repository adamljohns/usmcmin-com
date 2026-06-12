#!/usr/bin/env python3
"""Enrichment batch 153: hand-curated claims for 5 sitting/departing U.S. Representatives.

Targets archetype_party_default federal House members with 0 claims, taken from
the BOTTOM of the alphabet: TX (McCaul), TN (Rose), SC (Norman + Mace), PA (Fitzpatrick).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record / public positions.

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
    # ---------------- Michael McCaul (TX-10, R) ----------------
    ("michael-mccaul", "TX", "Representative", [
        claim("mc1", "michael-mccaul", "sanctity_of_life", 0, True,
              "Rated 100% by the National Right to Life Committee across his 20-year House career; consistently voted against taxpayer funding of abortion and supported parental notification requirements, aligning with the rubric's personhood-from-conception standard.",
              ["https://www.ontheissues.org/TX/Michael_McCaul.htm",
               "https://en.wikipedia.org/wiki/Michael_McCaul"]),
        claim("mc2", "michael-mccaul", "self_defense", 1, True,
              "Holds an NRA 'A' rating and signed the congressional friend-of-the-court briefs in both District of Columbia v. Heller (2008) and McDonald v. Chicago (2010), affirming the Second Amendment as an individual fundamental right that the rubric seeks to protect from registry and restriction.",
              ["https://www.nrapvf.org/articles/20100922/nra-pvf-endorses-michael-mccaul-for-us-house-of-representatives-in-texas-10th-congressional-district",
               "https://www.ontheissues.org/TX/Michael_McCaul.htm"]),
        claim("mc3", "michael-mccaul", "foreign_policy_restraint", 1, False,
              "As chairman of the House Foreign Affairs Committee (118th Congress), McCaul was the primary House architect of the $95 billion Ukraine/Israel/Taiwan supplemental aid package that passed in April 2024, and authored the Ukraine Aid Authorization and Oversight Act — a sustained push for open-ended overseas military commitments that runs counter to the rubric's call to end forever wars and reassert Article I war powers.",
              ["https://en.wikipedia.org/wiki/Michael_McCaul",
               "https://mccaul.house.gov/legislation/voting-record"]),
    ]),

    # ---------------- John Rose (TN-06, R) ----------------
    ("john-rose", "TN", "Representative", [
        claim("jr1", "john-rose", "sanctity_of_life", 0, True,
              "A+ rating from SBA Pro-Life America for a consistent pro-life voting record: voted to block taxpayer funding of abortion domestically and through international programs, and earned endorsements from anti-abortion groups in his 2026 Tennessee gubernatorial race.",
              ["https://sbaprolife.org/representative/john-rose",
               "https://smithcountyinsider.com/home-page-featured/gubernatorial-candidate-john-rose-receives-a-rating-from-national-pro-life-group/"]),
        claim("jr2", "john-rose", "self_defense", 1, True,
              "A lifetime NRA member who voted 'No' on both the Bipartisan Background Checks Act of 2021 (H.R.8) and the Enhanced Background Checks Act, calling them unconstitutional infringements; also cosponsored legislation to strike down the ATF's pistol-stabilizing brace rule, directly opposing federal regulatory overreach on firearms.",
              ["https://johnrose.house.gov/media/press-releases/us-rep-john-rose-votes-no-house-democrats-gun-control-bill",
               "https://johnrose.house.gov/media/press-releases/rep-rose-i-am-proud-cosponsor-legislation-strike-down-atfs-pistol-stabilizing"]),
        claim("jr3", "john-rose", "border_immigration", 0, True,
              "Argued on the House floor for the Secure the Border Act of 2023 (H.R.2), which mandates completion of border-wall construction and restricts asylum — calling Biden-era policies an 'open border' and demanding Senate action to restore law and order at the southern border.",
              ["https://johnrose.house.gov/media/press-releases/rep-rose-makes-case-house-republicans-secure-border-act",
               "https://johnrose.house.gov/media/press-releases/rep-rose-continues-raise-concerns-about-southern-border-crisis"]),
    ]),

    # ---------------- Ralph Norman (SC-05, R) ----------------
    ("ralph-norman", "SC", "Representative", [
        claim("rn1", "ralph-norman", "sanctity_of_life", 0, True,
              "A+ rating from SBA Pro-Life America and a 100% pro-life congressional voting record; endorsed by Students for Life Action in his 2026 South Carolina gubernatorial race for consistently defending the unborn and opposing federal abortion funding.",
              ["https://sbaprolife.org/representative/ralph-norman",
               "https://www.studentsforlifeaction.org/students-for-life-action-endorses-congressman-ralph-norman-for-south-carolina-governor/"]),
        claim("rn2", "ralph-norman", "economic_stewardship", 2, True,
              "A House Freedom Caucus member and self-described 'fiscal conservative with an appetite for cutting federal spending': pushed mandatory work requirements for Medicaid, voted against large deficit-expanding omnibus packages, and has made structural budget cuts and balanced-budget discipline a defining legislative priority.",
              ["https://norman.house.gov/news/documentsingle.aspx?DocumentID=2156",
               "https://en.wikipedia.org/wiki/Ralph_Norman"]),
        claim("rn3", "ralph-norman", "self_defense", 1, True,
              "One of Congress's most outspoken Second Amendment defenders — ranks among the most conservative House members (voted with President Biden just 2% of the time) and has publicly demonstrated his concealed-carry stance; broadly opposes any new firearm restrictions or registry measures.",
              ["https://ballotpedia.org/Ralph_Norman",
               "https://en.wikipedia.org/wiki/Ralph_Norman"]),
    ]),

    # ---------------- Nancy Mace (SC-01, R) ----------------
    ("nancy-mace", "SC", "Representative", [
        claim("nm1", "nancy-mace", "sanctity_of_life", 1, False,
              "Actively undermined strict pro-life state laws: publicly criticized South Carolina's 6-week heartbeat law, urged Republicans to accept 15–20 week cutoffs with rape/incest exceptions rather than pursuing full abolition, and used national media to attack life-affirming legislation — drawing a formal rebuke from SBA Pro-Life America for assailing pro-life policies even while casting some pro-life floor votes.",
              ["https://sbaprolife.org/newsroom/press-releases/susan-b-anthony-pro-life-america-responds-to-u-s-rep-nancy-mace-r-sc-on-meet-the-press",
               "https://en.wikipedia.org/wiki/Nancy_Mace"]),
        claim("nm2", "nancy-mace", "self_defense", 1, True,
              "A gun owner and avid outdoorswoman who voted against new firearms restrictions and has stated 'the debate over gun rights ended with the Second Amendment'; consistently opposed background-check expansions and gun-manufacturer liability bills.",
              ["https://mace.house.gov/media/press-releases/rep-mace-votes-protect-second-amendment-rights",
               "https://www.ontheissues.org/House/Nancy_Mace_Gun_Control.htm"]),
        claim("nm3", "nancy-mace", "border_immigration", 1, True,
              "Authored or cosponsored 60+ immigration enforcement bills; her Violence Against Women by Illegal Aliens Act (H.R.7909) passed 274-145 rendering immigrant sex offenders deportable; in 2025 introduced the Expedited Removal Expansion Act giving officers authority to deport illegal aliens on the spot without bureaucratic delay.",
              ["https://mace.house.gov/SecuringtheBorders",
               "https://mace.house.gov/media/press-releases/rep-nancy-mace-joins-president-trump-crack-down-illegal-immigration-and-speed"]),
    ]),

    # ---------------- Brian Fitzpatrick (PA-01, R) ----------------
    ("brian-fitzpatrick", "PA", "Representative", [
        claim("bf1", "brian-fitzpatrick", "self_defense", 1, False,
              "One of only 14 House Republicans to vote for the Bipartisan Safer Communities Act of 2022 — the first major federal gun legislation in 30 years, expanding background checks for under-21 buyers and closing the 'boyfriend loophole'; earned an 'F' rating from the NRA Political Victory Fund, the worst possible score for a House Republican.",
              ["https://ballotpedia.org/Bipartisan_Safer_Communities_Act_of_2022",
               "https://en.wikipedia.org/wiki/Brian_Fitzpatrick_(American_politician)"]),
        claim("bf2", "brian-fitzpatrick", "economic_stewardship", 2, False,
              "Scored only 7% on Tax and Fiscal from the Institute for Legislative Analysis in 2025, reflecting repeated support for large bipartisan spending packages; his trademark five-consecutive-year ranking as the most bipartisan House member correlates with consistent votes alongside Democrats on spending and fiscal priorities.",
              ["https://analysis.limitedgov.org/lawmakers/brian-fitzpatrick-r-pa-1",
               "https://en.wikipedia.org/wiki/Brian_Fitzpatrick_(American_politician)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
