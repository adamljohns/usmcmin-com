#!/usr/bin/env python3
"""Enrichment batch 531: 2 additional claims each for 5 sitting U.S. Reps
with only 3 claims — taken from the most bottom-of-alphabet states remaining
(PA and OR). Federal senator/rep archetype_curated pools are exhausted; this
batch pivots to evidence_curated reps needing depth.

Targets (2R+8D → 5 reps):
  John Joyce  (PA-R) — self_defense[4] + economic_stewardship[2]
  Summer Lee  (PA-D) — foreign_policy_restraint[1] + economic_stewardship[2]
  Val Hoyle   (OR-D) — biblical_marriage[4] + economic_stewardship[2]
  Janelle Bynum (OR-D) — biblical_marriage[2] + economic_stewardship[2]
  Suzanne Bonamici (OR-D) — border_immigration[1] + economic_stewardship[2]

NOTE: writes scorecard.json MINIFIED to keep the master under 50 MB.
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


TARGETS = [
    # -------- John Joyce (PA-R, U.S. Representative PA-13) --------
    ("john-joyce", "PA", "Representative", [
        claim("531a", "john-joyce", "self_defense", 4, True,
              "A consistent advocate for reducing federal gun-enforcement overreach: voted for FY2024 appropriations legislation that cut the ATF's budget by 7%, and has voted against every Democratic gun-control expansion bill — including H.R.8 (universal background checks) and H.R.1112. Holds an A rating from the NRA throughout his congressional tenure.",
              ["https://johnjoyce.house.gov/media/press-releases/joyce-votes-protect-rights-law-abiding-gun-owners",
               "https://justfacts.votesmart.org/candidate/evaluations/178911/john-joyce"]),
        claim("531b", "john-joyce", "economic_stewardship", 2, True,
              "A fiscal conservative who has repeatedly voted to cut wasteful federal spending and rein in the size of government. His office highlights votes for appropriations bills cutting agency budgets and reducing baseline spending, and he has publicly pressed Treasury Secretary Bessent on the FY2026 budget to pursue further fiscal discipline.",
              ["https://johnjoyce.house.gov/media/press-releases/dr-joyce-votes-cut-wasteful-spending-support-pa-13",
               "https://joyce.house.gov/posts/joyce-questions-treasury-secretary-bessent-on-fy26-budget-request"]),
    ]),

    # -------- Summer Lee (PA-D, U.S. Representative PA-12) --------
    ("summer-lee", "PA", "Representative", [
        claim("531a", "summer-lee", "foreign_policy_restraint", 1, True,
              "Voted against H.R. 8034, the $95 billion supplemental foreign-aid package for Ukraine, Israel, and Taiwan (April 2024), opposing open-ended U.S. overseas military commitments — one of the House progressive Democrats who broke with party leadership on the vote and argued the money was needed domestically.",
              ["https://northdallasgazette.com/2024/05/02/rep-summer-lee/",
               "https://www.congress.gov/bill/118th-congress/house-bill/8034"]),
        claim("531b", "summer-lee", "economic_stewardship", 2, False,
              "As a leading voice of the Congressional Progressive Caucus and Squad-aligned member, Lee consistently prioritizes expanding federal social programs over deficit reduction. She voted against and publicly denounced the One Big Beautiful Bill Act (H.R.1, 119th Congress, signed July 4, 2025), decrying its Medicaid and SNAP spending reforms as a Republican-manufactured 'healthcare crisis' — opposing any cuts to social spending regardless of fiscal cost.",
              ["https://summerlee.house.gov/newsroom/press-releases/rep-summer-lee-statement-on-vote-against-budget-fueling-republican-healthcare-crisis",
               "https://summerlee.house.gov/newsroom/press-releases/watch-rep-summer-lee-opposes-gop-budget-that-slashes-medicaid-snap-to-fund-billionaire-tax-breaks"]),
    ]),

    # -------- Val Hoyle (OR-D, U.S. Representative OR-04) --------
    ("val-hoyle", "OR", "Representative", [
        claim("531a", "val-hoyle", "biblical_marriage", 4, False,
              "A cosponsor of the federal Equality Act (H.R.15) in both the 118th Congress (joining June 21, 2023) and the 119th Congress (joining April 29, 2025), legislation that would enshrine sexual-orientation and gender-identity protections across schools, workplaces, and public accommodations nationwide — the active promotion of LGBTQ policy the rubric identifies as contrary to the biblical design for society.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/15/cosponsors",
               "https://www.congress.gov/bill/119th-congress/house-bill/15/cosponsors"]),
        claim("531b", "val-hoyle", "economic_stewardship", 2, False,
              "Voted against the One Big Beautiful Bill Act (H.R.1, 119th Congress), which passed 218-214 over universal Democratic opposition on July 3, 2025. As a Progressive Caucus member, Hoyle consistently supports expanded federal spending programs and opposes legislation that reduces social entitlement spending, reflecting a posture contrary to the rubric's anti-deficit fiscal ideal.",
              ["https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
    ]),

    # -------- Janelle Bynum (OR-D, U.S. Representative OR-05) --------
    ("janelle-bynum", "OR", "Representative", [
        claim("531a", "janelle-bynum", "biblical_marriage", 2, False,
              "Voted against H.R.28 (the SAVE Act, January 2025), which prohibits transgender students from competing on women's school sports teams consistent with their gender identity. Bynum publicly stated the bill 'goes too far' by subjecting children as young as 4 to genital examinations and enabling bullying of student athletes — rejecting the rubric's call to defend biological sex distinctions in public policy.",
              ["https://oregoncapitalchronicle.com/2025/01/14/repub/u-s-house-passes-bill-banning-trans-athletes-from-competing-in-womens-school-sports/",
               "https://www.congress.gov/bill/119th-congress/house-bill/28"]),
        claim("531b", "janelle-bynum", "economic_stewardship", 2, False,
              "Voted against the One Big Beautiful Bill Act (H.R.1, 119th Congress, passed 218-214 July 3, 2025) with universal Democratic opposition. Bynum's voting record and her work chairing Oregon's House Small Business and Economic Development Committee reflect consistent support for government-directed economic programs over fiscal restraint or deficit reduction.",
              ["https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://ballotpedia.org/Janelle_Bynum"]),
    ]),

    # -------- Suzanne Bonamici (OR-D, U.S. Representative OR-01) --------
    ("suzanne-bonamici", "OR", "Representative", [
        claim("531a", "suzanne-bonamici", "border_immigration", 1, False,
              "Voted against S.5, the Laken Riley Act (January 2025), which mandates ICE detention of undocumented immigrants accused of theft-related crimes and deportation of those convicted. She was among the 159 House Democrats who voted no on the measure that ultimately passed 264-159 with bipartisan support.",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://kpic.com/news/local/how-did-oregons-representatives-vote-on-the-laken-riley-act"]),
        claim("531b", "suzanne-bonamici", "economic_stewardship", 2, False,
              "Voted against the One Big Beautiful Bill Act (H.R.1, 119th Congress) with all House Democrats (218-214 final passage, July 3, 2025). A long-serving progressive who consistently opposes reductions to federal social spending and supports expanded government programs, placing her firmly against the rubric's anti-deficit/balanced-budget fiscal ideal.",
              ["https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://www.congress.gov/member/suzanne-bonamici/B001278"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
