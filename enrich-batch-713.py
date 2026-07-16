#!/usr/bin/env python3
"""Enrichment batch 713: depth pass for 5 New York U.S. Representatives.

All archetype_curated federal buckets are exhausted; this batch continues
depth enrichment of evidence_curated sitting House members with 3 existing
claims. Targets taken from the bottom of the state alphabet (NY), adding 2
new claims each in distinct rubric categories not yet scored.

NY-02 Andrew Garbarino (R): +2  sanctity_of_life[0], biblical_marriage[1]
NY-03 Tom Suozzi (D):        +2  border_immigration[1], biblical_marriage[2]
NY-15 Ritchie Torres (D):    +2  economic_stewardship[2], foreign_policy_restraint[3]
NY-18 Pat Ryan (D):          +2  foreign_policy_restraint[0], sanctity_of_life[0]
NY-16 George Latimer (D):    +2  border_immigration[2], foreign_policy_restraint[3]

Sources: en.wikipedia.org, govtrack.us, congress.gov, ballotpedia.org.
NOTE: writes scorecard.json MINIFIED to keep master under GitHub 50MB limit.
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
    # ------------- Andrew Garbarino (NY-02, R, US Representative) -------------
    ("andrew-garbarino", "NY", "Representative", [
        claim("ag1", "andrew-garbarino", "sanctity_of_life", 0, True,
              "Carries a consistent 100% pro-life voting record and A+ rating from SBA Pro-Life America; "
              "has voted against federal abortion funding and in favor of born-alive protections "
              "throughout his House tenure, affirming protection of the unborn.",
              ["https://sbaprolife.org/representative/andrew-garbarino",
               "https://en.wikipedia.org/wiki/Andrew_Garbarino"]),
        claim("ag2", "andrew-garbarino", "biblical_marriage", 1, False,
              "Was one of 46 House Republicans to vote YES on the Respect for Marriage Act "
              "(H.R. 8404, House Vote #373, July 19, 2022), which codified federal recognition "
              "of same-sex marriage and repealed the Defense of Marriage Act — directly contradicting "
              "the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://en.wikipedia.org/wiki/Andrew_Garbarino"]),
    ]),

    # ------------- Tom Suozzi (NY-03, D, US Representative) ------------------
    ("tom-suozzi", "NY", "Representative", [
        claim("ts1", "tom-suozzi", "border_immigration", 1, True,
              "Was one of 46 House Democrats to cross party lines and vote for the Laken Riley Act "
              "(House Vote #23, January 22, 2025), which requires mandatory detention without bond "
              "of non-citizens arrested for crimes including theft, burglary, and assault on law "
              "enforcement — a significant immigration-enforcement vote rare among House Democrats.",
              ["https://www.govtrack.us/congress/bills/119/s5",
               "https://en.wikipedia.org/wiki/Tom_Suozzi"]),
        claim("ts2", "tom-suozzi", "biblical_marriage", 2, True,
              "Following Kamala Harris's 2024 presidential defeat, Suozzi publicly criticized the "
              "Democratic Party's stance on transgender athletes competing in girls' sports, calling it "
              "part of a 'general attack on traditional values' — a rare crossover position for a House "
              "Democrat that partially aligns with the rubric's standard of rejecting transgender ideology.",
              ["https://en.wikipedia.org/wiki/Tom_Suozzi"]),
    ]),

    # ------------- Ritchie Torres (NY-15, D, US Representative) --------------
    ("ritchie-torres", "NY", "Representative", [
        claim("rt1", "ritchie-torres", "economic_stewardship", 2, False,
              "Cosponsored the Medicare for All Act of 2025 (H.R. 3069, 119th Congress), a government "
              "health program projected to cost $30–40 trillion over ten years and funded through new "
              "federal taxes and deficit spending — the opposite of the rubric's anti-deficit, "
              "balanced-budget standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3069/cosponsors",
               "https://en.wikipedia.org/wiki/Ritchie_Torres"]),
        claim("rt2", "ritchie-torres", "foreign_policy_restraint", 3, False,
              "Received approximately $1.6 million in contributions from pro-Israel lobby groups — "
              "including AIPAC — as of December 2025, making him one of the largest recipients of "
              "pro-Israel PAC money in Congress. The rubric flags acceptance of AIPAC and "
              "foreign-linked PAC funding as disqualifying under this category.",
              ["https://en.wikipedia.org/wiki/Ritchie_Torres"]),
    ]),

    # ------------- Pat Ryan (NY-18, D, US Representative) --------------------
    ("pat-ryan", "NY", "Representative", [
        claim("pr1", "pat-ryan", "foreign_policy_restraint", 0, True,
              "Supported a House War Powers resolution in March 2026 requiring President Trump to "
              "obtain congressional authorization before continuing U.S. military operations in Iran, "
              "and separately introduced the No Funds for Iran War Act — asserting Congress's "
              "Article I authority over the decision to wage war.",
              ["https://en.wikipedia.org/wiki/Pat_Ryan_(politician)",
               "https://www.congress.gov/member/patrick-ryan/R000579"]),
        claim("pr2", "pat-ryan", "sanctity_of_life", 0, False,
              "Sponsored H.R. 8734 (2026) to express the Sense of Congress on the safety of "
              "medication abortion and to establish federal preemption of state restrictions on "
              "dispensing it — directly opposing any recognition of life beginning at conception "
              "and asserting a federal right to abortion access.",
              ["https://www.congress.gov/member/patrick-ryan/R000579",
               "https://en.wikipedia.org/wiki/Pat_Ryan_(politician)"]),
    ]),

    # ------------- George Latimer (NY-16, D, US Representative) --------------
    ("george-latimer", "NY", "Representative", [
        claim("gl1", "george-latimer", "border_immigration", 2, False,
              "As Westchester County Executive, signed the Immigration Protection Act, which limits "
              "county cooperation with federal investigations of undocumented workers — a sanctuary-"
              "policy measure that directly contravenes the rubric's anti-sanctuary standard.",
              ["https://en.wikipedia.org/wiki/George_Latimer_(New_York_politician)",
               "https://ballotpedia.org/George_Latimer_(New_York)"]),
        claim("gl2", "george-latimer", "foreign_policy_restraint", 3, False,
              "AIPAC and aligned pro-Israel groups spent heavily to support Latimer in the 2024 "
              "Democratic primary against Jamaal Bowman — widely reported as the most expensive "
              "congressional primary in U.S. history — making Latimer's election the direct product "
              "of foreign-linked PAC influence, which the rubric identifies as disqualifying.",
              ["https://en.wikipedia.org/wiki/George_Latimer_(New_York_politician)",
               "https://ballotpedia.org/George_Latimer_(New_York)"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
