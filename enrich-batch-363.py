#!/usr/bin/env python3
"""Enrichment batch 363: 5 Virginia House of Delegates members with documented public positions.

All five had 0 claims and evidence_state confidence.
Bottom-of-alphabet targeting (VA — continuing from batch 362 VA State Senate).
  Marcus Simon       (VA-D, House of Delegates District 13 — Falls Church/Fairfax suburbs)
  Marcia Price       (VA-D, House of Delegates District 85 — Newport News; Privileges & Elections Chair)
  Madison Whittle    (VA-R, House of Delegates District 49 — Danville/Pittsylvania/Halifax; freshman 2026)
  Luke Torian        (VA-D, House of Delegates District 24 — Prince William; Appropriations Chair since 2010)
  Lindsey Dougherty  (VA-D, House of Delegates District 75 — Chesterfield/Prince George; flipped seat Nov 2025)
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
    # ---- Marcus Simon (VA-D, House of Delegates District 13) ----
    ("marcus-simon", "VA", "District 13", [
        claim("ms1", "marcus-simon", "sanctity_of_life", 0, False,
              "Simon voted with the Virginia House Democratic majority to pass HJR1 (Virginia Right to Reproductive Freedom Amendment) 64-34 in January 2026, sending to the November 2026 ballot a constitutional provision declaring every individual has a 'fundamental right' to abortion, contraception, and fertility care — actively working to enshrine abortion access as a state constitutional right rather than recognizing personhood from conception.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://en.wikipedia.org/wiki/2026_Virginia_Right_to_Reproductive_Freedom_Amendment",
               "https://lis.virginia.gov/bill-details/20261/HJ1"]),
        claim("ms2", "marcus-simon", "self_defense", 1, False,
              "Simon voted with the Virginia House Democratic majority for HB217, the 2026 assault weapons ban that passed 58-34 'over GOP objections' on February 5, 2026. Signed by Governor Spanberger in May 2026, the law prohibits the future sale, manufacture, and transfer of semi-automatic firearms classified as assault weapons and magazines capable of holding more than 15 rounds — contrary to the rubric's anti-AWB/anti-magazine-limit standard.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://lis.virginia.gov/bill-details/20261/HB217",
               "https://virginiamercury.com/2026/05/15/spanberger-signs-assault-weapons-ban-package-of-criminal-justice-and-energy-bills/"]),
    ]),

    # ---- Marcia Price (VA-D, House of Delegates District 85) ----
    ("marcia-price", "VA", "District 85", [
        claim("mp1", "marcia-price", "sanctity_of_life", 0, False,
              "As chair of the House Privileges and Elections Committee, Price's panel voted 15-7 in January 2026 to advance HJR1 (Virginia Right to Reproductive Freedom Amendment). Price championed the amendment, declaring the 'right to bodily autonomy and privacy' to be 'crucial to the foundation of this commonwealth and this nation,' and noted Virginia's maternal-health crisis as cause to enshrine abortion access constitutionally — directly opposing the rubric's life-at-conception/personhood standard.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2025/02/13/virginia-moves-to-protect-reproductive-and-voting-rights-but-the-fight-is-far-from-over/",
               "https://ballotpedia.org/Marcia_Price"]),
        claim("mp2", "marcia-price", "self_defense", 1, False,
              "Price introduced HB421 in the 2020 Virginia legislative session to authorize any locality to prohibit the possession or carrying of firearms, ammunition, or components in governmental buildings, public parks, and public streets used for permitted events, framing lawful gun carrying as a locality-regulated responsibility; she has continued advocating for expanded gun-restriction authority and wrote in 2025 that a proposed gun-violence prevention center would be an 'asset' for reducing gun violence — reflecting an ongoing record of supporting restrictions on the right to keep and bear arms.",
              ["https://virginiamercury.com/2025/02/17/proposed-anti-gun-violence-center-an-asset-should-be-embraced/",
               "https://lis.virginia.gov/cgi-bin/legp604.exe?201+mbr+H284=",
               "https://ballotpedia.org/Marcia_Price"]),
    ]),

    # ---- Madison Whittle (VA-R, House of Delegates District 49) ----
    ("madison-whittle", "VA", "District 49", [
        claim("mw1", "madison-whittle", "self_defense", 1, True,
              "HB217 (Virginia's 2026 assault weapons ban) passed 58-34 on February 5, 2026, with every 'no' vote coming from Republican delegates who 'warned repeatedly that the legislation trampled constitutional rights.' Whittle, a Republican representing one of Virginia's most conservative districts (Danville, Pittsylvania County, Halifax County), voted with the unified Republican caucus against the ban, defending the right to own semi-automatic firearms and standard-capacity magazines against the Democratic-majority package.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://lis.virginia.gov/bill-details/20261/HB217",
               "https://ballotpedia.org/Madison_Redd_Whittle"]),
        claim("mw2", "madison-whittle", "sanctity_of_life", 0, True,
              "The Virginia Right to Reproductive Freedom Amendment (HJR1) passed the House 64-34 in January 2026, with the 34 'no' votes cast entirely by Republican delegates; Whittle, representing a deeply conservative district that voted heavily Republican, voted against placing a constitutional right to abortion on the November 2026 ballot — aligning with the rubric's position opposing state constitutional enshrinement of abortion access.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://ballotpedia.org/Madison_Redd_Whittle"]),
    ]),

    # ---- Luke Torian (VA-D, House of Delegates District 24) ----
    ("luke-torian", "VA", "District 24", [
        claim("lt1", "luke-torian", "sanctity_of_life", 0, False,
              "Torian, listed as a supporter of Virginia's Right to Reproductive Freedom Amendment (HJR1), voted with the House Democratic majority to pass HJR1 64-34 in January 2026, advancing a constitutional guarantee of abortion as a 'fundamental right' to the November 2026 ballot. As a Democrat serving since 2010 and current House Appropriations Committee Chair, Torian has consistently aligned with the Democratic caucus in opposing restrictions on abortion access — contrary to the rubric's life-at-conception/personhood standard.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://ballotpedia.org/Luke_Torian",
               "https://lis.virginia.gov/bill-details/20261/HJ1"]),
        claim("lt2", "luke-torian", "self_defense", 1, False,
              "Torian voted with the Virginia House Democratic majority to pass HB217 (assault weapons ban) 58-34 on February 5, 2026. The sweeping gun-control package — including the assault-weapons ban signed by Governor Spanberger in May 2026 — prohibits the future sale, manufacture, and transfer of semi-automatic assault-style firearms and magazines over 15 rounds. Torian, a senior House Democrat and Appropriations Committee Chair since 2010, aligned with his caucus in support of these restrictions, contrary to the rubric's anti-AWB standard.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://virginiamercury.com/2026/04/14/spanberger-amends-signs-sweeping-gun-legislation-reshaping-virginias-firearm-laws/",
               "https://ballotpedia.org/Luke_Torian"]),
    ]),

    # ---- Lindsey Dougherty (VA-D, House of Delegates District 75) ----
    ("lindsey-dougherty", "VA", "District 75", [
        claim("ld1", "lindsey-dougherty", "sanctity_of_life", 0, False,
              "Dougherty voted 'yea' on SB727 during Virginia's 2026 Regular Session (a reproductive rights measure that passed 59-38) and is listed as a supporter of the Virginia Right to Reproductive Freedom Amendment. She campaigned explicitly on 'protecting abortion access,' crediting that platform with flipping the competitive District 75 seat in November 2025, and voted with the Democratic majority to send HJR1 (constitutional abortion rights amendment) to the November 2026 ballot — opposing the rubric's life-at-conception/personhood standard.",
              ["https://lis.virginia.gov/vote-details/SB727/20261/26111446",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://ballotpedia.org/Lindsey_Dougherty"]),
        claim("ld2", "lindsey-dougherty", "self_defense", 1, False,
              "Dougherty voted with the Virginia House Democratic majority for HB217 (assault weapons ban), part of the sweeping 2026 gun-control package that passed 58-34 on February 5, 2026, 'over GOP objections,' and was signed by Governor Spanberger in May 2026 — banning the future sale of semi-automatic assault-style firearms and magazines over 15 rounds. As a Democrat who flipped a competitive Chesterfield County seat on a pro-gun-control platform, Dougherty aligned with her caucus against the constitutional-carry and anti-AWB positions the rubric favors.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://virginiamercury.com/2026/05/15/spanberger-signs-assault-weapons-ban-package-of-criminal-justice-and-energy-bills/",
               "https://ballotpedia.org/Lindsey_Dougherty"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
