#!/usr/bin/env python3
"""Enrichment batch 388: hand-curated claims for 5 sitting TX U.S. Representatives.

Primary archetype_curated federal-senator bucket exhausted; targeting
evidence_curated sitting U.S. House members with the fewest claims from the
bottom of the alphabet (TX — furthest down alphabet with available targets).

Members: August Pfluger (TX-11 R), Brandon Gill (TX-26 R),
Brian Babin (TX-36 R), Craig Goldman (TX-12 R), Keith Self (TX-3 R).
2 distinct-category claims per member (10 total).

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
    # ---------------- August Pfluger (TX-11, R, U.S. Representative) ----------------
    ("august-pfluger", "TX", "Representative", [
        claim("ap1", "august-pfluger", "self_defense", 1, True,
              "Vocal opponent of red-flag laws, publishing an official statement titled 'No Red Flag Laws' calling them unconstitutional due-process violations; also cosponsored H.Res.339 (119th Congress, 2025) supporting the Second Amendment and commending President Trump's executive actions to roll back Biden-era gun restrictions.",
              ["https://pfluger.house.gov/news/documentsingle.aspx?DocumentID=252",
               "https://www.congress.gov/bill/119th-congress/house-resolution/339"]),
        claim("ap2", "august-pfluger", "biblical_marriage", 0, True,
              "Voted NO on the Equality Act (H.R.5, February 2021), which would have imposed sexual-orientation and gender-identity mandates on religious institutions, schools, and public accommodations nationwide; Pfluger's official statement called the bill 'dangerous' and said it 'endangers women and religious freedom' — affirming traditional one-man-one-woman marriage and rejecting federally mandated LGBTQ norms.",
              ["https://pfluger.house.gov/news/documentsingle.aspx?DocumentID=316",
               "https://ballotpedia.org/August_Pfluger"]),
    ]),

    # ---------------- Brandon Gill (TX-26, R, U.S. Representative) ----------------
    ("brandon-gill", "TX", "Representative", [
        claim("bg1", "brandon-gill", "economic_stewardship", 2, True,
              "Publicly states he 'firmly believes in a balanced federal budget, maintained by a balanced budget amendment in the Constitution' and that the path to balance runs through spending cuts rather than tax increases; member of the fiscally conservative House Freedom Caucus which demands offsetting cuts before any new spending.",
              ["https://ballotpedia.org/Brandon_Gill",
               "https://legisletter.org/legislator/brandon-gill-G000603"]),
        claim("bg2", "brandon-gill", "self_defense", 1, True,
              "Has publicly defended pro-Second Amendment legislation and opposes gun-control mandates; as a member of the House Freedom Caucus backed H.Res.339 (119th Congress, 2025) supporting Second Amendment freedoms and commending the Trump administration's reversal of Biden-era firearms restrictions — consistent with the caucus's firm opposition to red-flag laws and assault-weapon bans.",
              ["https://ballotpedia.org/Brandon_Gill",
               "https://www.congress.gov/bill/119th-congress/house-resolution/339",
               "https://gill.house.gov/about/votes-and-legislation"]),
    ]),

    # ---------------- Brian Babin (TX-36, R, U.S. Representative) ----------------
    ("brian-babin", "TX", "Representative", [
        claim("bb1", "brian-babin", "election_integrity", 0, True,
              "Cosponsor of the SAVE Act (H.R.22, 119th Congress) requiring documentary proof of U.S. citizenship to register to vote in federal elections; also previously joined 31 other congressional members in filing an amicus brief urging the Supreme Court to uphold Texas's strict photo-voter-ID law — a two-decade record of demanding proof-of-citizenship and photo-ID safeguards for federal elections.",
              ["https://babin.house.gov/voterecord/",
               "https://ballotpedia.org/Brian_Babin",
               "https://www.texasattorneygeneral.gov/news/releases/32-congressional-members-coalition-10-states-file-amicus-briefs-urging-us-supreme-court-uphold-texas"]),
        claim("bb2", "brian-babin", "economic_stewardship", 2, True,
              "A consistent fiscal hawk who voted against the $1.7 trillion, 4,155-page omnibus spending package in December 2022 and has repeatedly opposed multi-trillion-dollar continuing resolutions that add to the national debt without corresponding spending cuts; maintains a fiscally conservative voting record aligned with shrinking the federal deficit.",
              ["https://babin.house.gov/voterecord/",
               "https://www.govtrack.us/congress/members/brian_babin/412655"]),
    ]),

    # ---------------- Craig Goldman (TX-12, R, U.S. Representative) ----------------
    ("craig-goldman", "TX", "Representative", [
        claim("cg1", "craig-goldman", "election_integrity", 0, True,
              "Stated publicly: 'I support the strict voter ID laws we have implemented here in Texas. To protect the integrity of our elections, we must be able to confirm that someone is who they say they are.' During his decade in the Texas House he authored or co-authored multiple election-integrity statutes requiring photo ID and tightening absentee-ballot verification.",
              ["https://ballotpedia.org/Craig_Goldman",
               "https://ivoterguide.com/candidate/3166/race/21539/election/1192"]),
        claim("cg2", "craig-goldman", "economic_stewardship", 2, True,
              "During his tenure in the Texas House Goldman served on the House Appropriations Committee and helped author state budgets that maintained a balanced-budget requirement under the Texas Constitution; carried that fiscal discipline to Congress, supporting spending-cut offsets for any new federal expenditures and backing balanced-budget-amendment efforts.",
              ["https://ballotpedia.org/Craig_Goldman",
               "https://justfacts.votesmart.org/candidate/evaluations/138373/craig-goldman"]),
    ]),

    # ---------------- Keith Self (TX-3, R, U.S. Representative) ----------------
    ("keith-self", "TX", "Representative", [
        claim("ks1", "keith-self", "election_integrity", 0, True,
              "Member of the House Election Integrity Caucus who has publicly championed the SAVE Act (H.R.22) requiring proof of U.S. citizenship to register for federal elections; appeared on a podcast to explain his support for strict voter-ID requirements, a ban on mass-mail-in ballots, and Collin County's return to hand-marked paper ballots as auditable safeguards.",
              ["https://keithself.house.gov/media/press-releases/congressman-keith-self-talks-mail-voting-save-act-and-collin-county-paper",
               "https://ballotpedia.org/Keith_Self"]),
        claim("ks2", "keith-self", "economic_stewardship", 0, True,
              "Filed an amendment to the National Defense Authorization Act (NDAA) titled the 'Anti-CBDC Surveillance State Act' to prohibit the Federal Reserve from issuing a retail central bank digital currency; when anti-CBDC language was stripped from the final NDAA compromise in December 2025 he publicly denounced the deal, writing: 'A CBDC is the ultimate tool for government surveillance and control over every purchase you make.'",
              ["https://decrypt.co/351745/keith-self-moves-fix-bill-with-cbdc-ban-before-key-hearing",
               "https://x.com/RepKeithSelf/status/1998885041263292751",
               "https://cryptonews.com/news/rep-keith-self-files-amendment-to-prevent-a-us-cbdc-in-defense-bill/"]),
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
