#!/usr/bin/env python3
"""Enrichment batch 773: hand-curated claims for 5 sitting U.S. Representatives.

All archetype_curated federal senator/representative buckets are exhausted;
targets pulled from evidence_curated sitting federal representatives with <5 claims,
taken from the bottom of the state alphabet (KY, GA).

Targets: James Comer (KY-R), Andrew Clyde (GA-R), Rick Allen (GA-R),
         Austin Scott (GA-R), Brian Jack (GA-R).

Each claim cites >=1 reliable source and reflects 2024-2026 voting record /
public positions. Claims cover DISTINCT rubric categories not already filed per
candidate (no category/question_idx already occupied is re-used here).

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB limit.
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
    # ---------- James Comer (KY-R, U.S. Representative KY-01) ----------
    ("james-comer", "KY", "U.S. Representative", [
        claim("jc1", "james-comer", "self_defense", 1, True,
              "Holds an NRA 'A' rating and was endorsed by the NRA Political Victory Fund before his first House election; is a member of the Congressional Second Amendment Caucus; has cosponsored the Concealed Carry Reciprocity Act and other legislation expanding lawful carry rights, consistently opposing any new federal firearm restrictions.",
              ["https://www.nrapvf.org/articles/20160411/nra-pvf-endorses-james-comer-in-kentucky-s-primary-for-the-1st-congressional-district",
               "https://comer.house.gov/press-release?ID=DD2DC8A5-35B5-468C-B3AD-DA1B6B0E86B1",
               "https://www.nssf.org/articles/nssf-profile-q-and-a-rep-james-comer-r-ky/"]),
        claim("jc2", "james-comer", "economic_stewardship", 2, True,
              "Called for a Balanced Budget Amendment to the U.S. Constitution in a January 2026 op-ed published by the Lexington Herald-Leader, warning that Washington's chronic budget dysfunction is fueling a 'growing debt crisis' and that Congress will not act without a constitutional constraint. As chairman of the House Committee on Oversight and Accountability he has aggressively investigated government waste, fraud, and abuse.",
              ["https://comer.house.gov/2026/1/comer-in-herald-leader-it-s-time-to-finally-balance-america-s-budget",
               "https://comer.house.gov/about"]),
    ]),

    # ---------- Andrew Clyde (GA-R, U.S. Representative GA-09) ----------
    ("andrew-clyde", "GA", "U.S. Representative", [
        claim("ac1", "andrew-clyde", "foreign_policy_restraint", 1, True,
              "Voted NO on the $95.3 billion Ukraine/Israel/Taiwan foreign aid package (House Vote, April 20, 2024), publicly condemning it as an 'America Last' bill that prioritizes foreign governments over Americans; wrote an op-ed on his official site arguing aid packages undermine U.S. interests and told Newsmax the legislation puts foreign nationals ahead of American citizens.",
              ["https://clyde.house.gov/news/documentsingle.aspx?DocumentID=167",
               "https://www.newsmax.com/newsmax-tv/andrew-clyde-mike-johnson-ukraine/2024/04/18/id/1161559/"]),
        claim("ac2", "andrew-clyde", "economic_stewardship", 2, True,
              "Voted NO in the House Budget Committee (May 16, 2025) on the initial reconciliation bill as insufficient on spending cuts, joining other Freedom Caucus conservatives in demanding deeper reductions; holds Heritage Action scorecard scores of 96% (117th), 98% (118th), and 100% (119th) Congress — consistently placing him among the most fiscally conservative members of the House.",
              ["https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://heritageaction.com/scorecard/members/c001116",
               "https://heritageaction.com/scorecard/members/C001116/117"]),
    ]),

    # ---------- Rick Allen (GA-R, U.S. Representative GA-12) ----------
    ("rick-allen", "GA", "U.S. Representative", [
        claim("ra1", "rick-allen", "election_integrity", 0, True,
              "Voted YES on the Safeguard American Voter Eligibility (SAVE) Act (H.R. 22, House Roll Call #102, April 10, 2025; passed 220-208), which requires documentary proof of U.S. citizenship when registering to vote in federal elections. Allen, who had previously voted to object to Arizona's and Pennsylvania's 2020 electoral votes, issued a press release praising the SAVE Act as ensuring 'only American citizens are deciding American elections.'",
              ["https://allen.house.gov/news/documentsingle.aspx?DocumentID=7098",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("ra2", "rick-allen", "economic_stewardship", 2, True,
              "Cosponsored H.J.Res. 3 (117th Congress), proposing a Balanced Budget Amendment to the U.S. Constitution, and has consistently championed fiscal restraint: 'Washington does not have a revenue problem; it has a spending problem. The spending-addicted politicians in Washington are doing nothing to solve it.' He has also chaired the House HELP Subcommittee effort to ban ESG considerations from retirement fund investment decisions.",
              ["https://allen.house.gov/news/documentsingle.aspx?DocumentID=1203",
               "https://www.congress.gov/bill/117th-congress/house-joint-resolution/3/text",
               "https://congressionaldigest.com/issue/esg-and-retirement-investment-funds/honorable-rick-allen/"]),
    ]),

    # ---------- Austin Scott (GA-R, U.S. Representative GA-08) ----------
    ("austin-scott", "GA", "U.S. Representative", [
        claim("as1", "austin-scott", "election_integrity", 0, True,
              "Supported the SAVE Act (H.R. 22, April 2025) and the SAVE America Act (2026), and participated in the House Rules Committee debate on the latter: 'House Republicans passed the SAVE America Act to further protect the integrity of the country's federal elections… 83% of Americans support requiring all voters to show government-issued photo ID.' Also cosponsored the American Confidence in Elections (ACE) Act (H.R. 4563, 118th Congress) to tighten federal election safeguards.",
              ["https://www.laniercountynewsonline.com/2026/02/16/an-update-from-congressman-austin-scott-70/",
               "https://austinscott.house.gov/votes-and-legislation",
               "https://www.congress.gov/bill/118th-congress/house-bill/4563"]),
        claim("as2", "austin-scott", "economic_stewardship", 2, True,
              "Voted YES on the Limit, Save, Grow Act (H.R. 2811, House Vote #199, April 26, 2023), which imposed discretionary spending caps through FY2033 and rescinded unobligated COVID-era funds as a condition of raising the debt ceiling. Also voted NO on the Inflation Reduction Act (August 2022), calling it a 'tax and spending spree that would dramatically exacerbate inflation' and NO on the Infrastructure Investment and Jobs Act as similar overreach.",
              ["https://www.govtrack.us/congress/bills/118/hr2811",
               "https://www.govtrack.us/congress/votes/117-2022/h420",
               "https://ballotpedia.org/Austin_Scott"]),
    ]),

    # ---------- Brian Jack (GA-R, U.S. Representative GA-03) ----------
    ("brian-jack", "GA", "U.S. Representative", [
        claim("bj1", "brian-jack", "self_defense", 2, True,
              "Voted YES on H.R. 1 (One Big Beautiful Bill Act, signed July 4, 2025; passed 218-214), which included a provision eliminating the $200 federal NFA excise tax on suppressors and short-barreled rifles — the first reduction in NFA transfer taxes since the National Firearms Act's passage in 1934 and described by Second Amendment advocates as one of the most significant legislative wins for gun owners in nearly a century.",
              ["https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://www.congress.gov/bill/119th-congress/house-bill/1",
               "https://clyde.house.gov/news/documentsingle.aspx?DocumentID=3267"]),
        claim("bj2", "brian-jack", "election_integrity", 0, True,
              "Voted YES on the Safeguard American Voter Eligibility (SAVE) Act (H.R. 22, House Roll Call #102, April 10, 2025; passed 220-208), requiring documentary proof of U.S. citizenship when registering to vote in federal elections. Jack, a 100% attendance Trump-aligned freshman (0 missed votes from Jan 2025 through Apr 2026), supported this long-sought Republican election integrity measure.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.govtrack.us/congress/members/brian_jack/456987"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
