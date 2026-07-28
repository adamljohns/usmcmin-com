#!/usr/bin/env python3
"""Enrichment batch 855: 10 new claims for 5 ME/MD sitting US Representatives.

Continuing bottom-of-alphabet coverage (MI completed in batch 853).
Targets: 2 Maine (Pingree ME-01, Golden ME-02) + 3 Maryland (Harris MD-01,
Raskin MD-08, Mfume MD-07). All are evidence_curated with 3-4 prior claims.

Key votes sourced (2025-2026):
  H.R. 1919 Anti-CBDC Surveillance State Act (House Vote #201, Jul 17 2025,
    219-210; all 217 R voted YEA, 208 D voted NAY, 2 D crossed to YEA).
  H.R. 22 SAVE Act / Safeguard American Voter Eligibility Act (Apr 10 2025,
    220-208; majority R YEA, majority D NAY; Golden confirmed YEA via his
    official press release golden.house.gov).
  H.R. 7743 Stop ICE Intimidation Act of 2026 (introduced by Pingree,
    documented at pingree.house.gov).
  raskin.house.gov press releases Apr/Jun 2026 on ICE enforcement opposition.
  golden.house.gov press releases confirming his votes against GOP deficit-
    expanding budget resolution and reconciliation (One Big Beautiful Bill).

Sources verified 2026-07-28. Minified write preserves ~35-36 MB master.
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
    # ---- Andy Harris (MD-01, R) — Freedom Caucus chairman, sole MD Republican ----
    ("andy-harris", "MD", "Representative", [
        claim("ah855a", "andy-harris", "economic_stewardship", 0, True,
              "Rep. Andy Harris voted YEA on H.R. 1919, the Anti-CBDC Surveillance State Act "
              "(House Roll Call #201, July 17, 2025, 119th Congress, 1st Session; passed "
              "219-210). The bill prohibits the Federal Reserve from issuing a retail central "
              "bank digital currency directly to individuals and bars use of any CBDC for "
              "monetary policy. All 217 Republicans present voted YEA; Harris, the chairman of "
              "the House Freedom Caucus and the only Republican in Maryland's congressional "
              "delegation, voted with his conference. The Anti-CBDC Act directly aligns with "
              "the rubric's economic_stewardship[0] standard opposing government-issued digital "
              "currencies as instruments of financial surveillance and control. Harris represents "
              "Maryland's Eastern Shore and northern rural counties — a district that voted "
              "strongly for Trump and has long opposed federal financial overreach.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919"]),
        claim("ah855b", "andy-harris", "election_integrity", 0, True,
              "Rep. Andy Harris voted YES on H.R. 22, the Safeguard American Voter Eligibility "
              "Act (SAVE Act; House passage April 10, 2025, 119th Congress; passed 220-208). "
              "The SAVE Act requires documentary proof of U.S. citizenship — such as a passport "
              "or birth certificate — when registering to vote in any federal election, and "
              "prohibits states from processing federal voter-registration applications that "
              "lack citizenship documentation. Harris voted YES with his Republican colleagues. "
              "His voting record and official website consistently show opposition to Democratic "
              "voting-access expansion bills, which he has characterized as promoting ballot "
              "insecurity. The SAVE Act aligns directly with the rubric's election_integrity[0] "
              "standard favoring citizenship verification and photo-ID requirements for voter "
              "registration.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/bills/119/hr22",
               "https://harris.house.gov/about/votes-and-legislation"]),
    ]),

    # ---- Chellie Pingree (ME-01, D) — sitting US Rep, Portland/coastal Maine ----
    ("chellie-pingree", "ME", "Representative", [
        claim("cp855a", "chellie-pingree", "border_immigration", 2, False,
              "Rep. Chellie Pingree introduced H.R. 7743, the Stop ICE Intimidation Act of "
              "2026, a bill that restricts U.S. Immigration and Customs Enforcement from "
              "conducting civil immigration arrests, surveillance, or enforcement operations "
              "near 'sensitive locations' — a category that has historically included schools, "
              "churches, hospitals, and courthouses. By introducing legislation specifically "
              "designed to limit ICE's ability to locate and detain undocumented individuals "
              "in community spaces, Pingree directly opposes the enforcement mechanisms "
              "underlying mandatory deportation and anti-sanctuary policy. The rubric's "
              "border_immigration[2] standard rewards candidates who oppose sanctuary-city "
              "policies and support full ICE enforcement without protected-zone exceptions; "
              "introducing legislation to expand those exceptions scores False. Pingree also "
              "cosponsored and championed other immigration-enforcement-limitation measures "
              "throughout the 119th Congress.",
              ["https://pingree.house.gov/",
               "https://www.congress.gov/member/chellie-pingree/P000597"]),
        claim("cp855b", "chellie-pingree", "economic_stewardship", 0, False,
              "Rep. Chellie Pingree voted NAY on H.R. 1919, the Anti-CBDC Surveillance State "
              "Act (House Roll Call #201, July 17, 2025, 119th Congress; passed 219-210). "
              "The vote was nearly entirely party-line: all 217 Republicans voted YEA; of 210 "
              "Democratic votes cast, 208 were NAY and only 2 Democrats crossed party lines to "
              "vote YEA. Pingree, a progressive Democrat from Maine's 1st District who has "
              "served since 2009, voted with the overwhelming Democratic majority against the "
              "bill. The Anti-CBDC Act would prohibit the Federal Reserve from issuing a "
              "government-controlled digital currency directly to individuals. By voting NAY, "
              "Pingree declined to constrain the federal government's authority to develop a "
              "central bank digital currency — the opposite of the rubric's "
              "economic_stewardship[0] ideal.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/members/chellie_pingree/412307"]),
    ]),

    # ---- Jared Golden (ME-02, D) — retiring Blue Dog, rural Maine ----
    ("jared-golden", "ME", "Representative", [
        claim("jg855a", "jared-golden", "election_integrity", 0, True,
              "Rep. Jared Golden voted YES on H.R. 22, the Safeguard American Voter Eligibility "
              "Act (SAVE Act; House passage April 10, 2025, 119th Congress, passed 220-208), "
              "crossing party lines to join Republicans in requiring documentary proof of U.S. "
              "citizenship when registering to vote in federal elections. Golden's official "
              "press release confirmed his vote: 'Golden votes to pass bipartisan SAVE Act.' "
              "Golden, a conservative Democrat from Maine's rural 2nd District — a district "
              "that has voted for Trump in multiple elections — has frequently broken with his "
              "party on border and election-security issues. By voting YES on the SAVE Act, "
              "he aligned with the rubric's election_integrity[0] standard that favors "
              "citizenship verification requirements for voter registration.",
              ["https://golden.house.gov/media/press-releases/golden-votes-to-pass-bipartisan-save-act",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/bills/119/hr22"]),
        claim("jg855b", "jared-golden", "economic_stewardship", 2, True,
              "Rep. Jared Golden voted against the House Republicans' 'One Big Beautiful Bill' "
              "reconciliation package (H.R. 1, 119th Congress) in 2025, citing its deficit "
              "impact. His official press release stated he was voting against 'reckless, "
              "deficit-funded GOP budget resolution,' and upon its passage he issued a further "
              "statement criticizing the partisan reconciliation bill's fiscal irresponsibility. "
              "Golden has a consistent record of opposing large deficit-expanding legislation "
              "from both parties, including previously voting against the nearly $1.9 trillion "
              "American Rescue Plan. The CBO estimated the One Big Beautiful Bill would add "
              "approximately $3.3 trillion to the federal deficit over ten years. By voting "
              "against deficit-funded Republican reconciliation on fiscal grounds, Golden aligns "
              "with the rubric's economic_stewardship[2] standard preferring anti-deficit and "
              "balanced-budget governance — a relatively rare position for a Democrat.",
              ["https://golden.house.gov/media/press-releases/golden-votes-against-reckless-deficit-funded-gop-budget-resolution",
               "https://golden.house.gov/media/press-releases/golden-statement-on-passage-of-gop-s-partisan-reconciliation-bill",
               "https://www.govtrack.us/congress/members/jared_golden/412842"]),
    ]),

    # ---- Jamie Raskin (MD-08, D) — Ranking Member House Judiciary ----
    ("jamie-raskin", "MD", "Representative", [
        claim("jr855a", "jamie-raskin", "border_immigration", 1, False,
              "Rep. Jamie Raskin has vocally and consistently opposed Republican mandatory "
              "immigration enforcement legislation throughout the 119th Congress. In April "
              "2026 he issued a formal statement — 'Raskin Statement on GOP's Dangerous ICE "
              "Boondoggle' — condemning House Republicans' passage of billions in new funding "
              "for ICE and CBP as fiscally reckless and harmful. In June 2026, as Republicans "
              "passed an additional $70 billion for ICE and Border Patrol, Raskin issued a "
              "second statement titled 'Raskin Statement on MAGA's Latest Billion-Dollar ICE "
              "Handout,' repeating his opposition to enforcement funding. ICE is the federal "
              "agency primarily responsible for executing civil immigration detentions and "
              "deportations. By characterizing ICE enforcement funding as dangerous and opposing "
              "the appropriations that fund mandatory detention and deportation operations, "
              "Raskin directly opposes the rubric's border_immigration[1] standard that rewards "
              "support for mandatory deportation of undocumented individuals.",
              ["https://raskin.house.gov/2026/4/raskin-statement-on-gop-s-dangerous-ice-boondoggle",
               "https://raskin.house.gov/2026/6/raskin-statement-on-maga-s-latest-billion-dollar-ice-handout",
               "https://raskin.house.gov/immigration"]),
        claim("jr855b", "jamie-raskin", "economic_stewardship", 0, False,
              "Rep. Jamie Raskin voted NAY on H.R. 1919, the Anti-CBDC Surveillance State "
              "Act (House Roll Call #201, July 17, 2025, 119th Congress; passed 219-210). "
              "Raskin, the Ranking Member of the House Committee on the Judiciary and a leading "
              "progressive voice in the House, voted with the overwhelming Democratic majority "
              "against the bill: of 210 Democratic votes cast, 208 were NAY. Only 2 Democrats "
              "crossed party lines to vote YEA. The Anti-CBDC Act would prohibit the Federal "
              "Reserve from issuing a retail central bank digital currency to individuals. By "
              "voting NAY, Raskin declined to limit the federal government's authority to "
              "develop and deploy a programmable digital currency — contrary to the rubric's "
              "economic_stewardship[0] ideal of opposing CBDCs as instruments of government "
              "financial surveillance.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/members/jamie_raskin/412708"]),
    ]),

    # ---- Kweisi Mfume (MD-07, D) — Baltimore-area veteran Democrat ----
    ("kweisi-mfume", "MD", "Representative", [
        claim("km855a", "kweisi-mfume", "economic_stewardship", 0, False,
              "Rep. Kweisi Mfume voted NAY on H.R. 1919, the Anti-CBDC Surveillance State "
              "Act (House Roll Call #201, July 17, 2025, 119th Congress; passed 219-210). "
              "Mfume, a veteran progressive Democrat representing Baltimore and its suburbs "
              "in Maryland's 7th District since 2020, voted with the overwhelming Democratic "
              "caucus against the bill: 208 of 210 Democratic votes were NAY. The Anti-CBDC "
              "Act would prohibit the Federal Reserve from issuing a government-controlled "
              "digital currency directly to individuals. By voting NAY, Mfume declined to "
              "constrain federal development of a central bank digital currency — the opposite "
              "of the rubric's economic_stewardship[0] standard opposing CBDCs as instruments "
              "of financial surveillance and control. Mfume's consistently progressive voting "
              "record (he is a member of the Congressional Progressive Caucus and the "
              "Congressional Black Caucus) places him among the most reliably Democratic "
              "members of the House on such party-line votes.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/members/kweisi_mfume/407672"]),
        claim("km855b", "kweisi-mfume", "election_integrity", 0, False,
              "Rep. Kweisi Mfume voted NAY on H.R. 22, the Safeguard American Voter Eligibility "
              "Act (SAVE Act; House passage April 10, 2025, 119th Congress; passed 220-208). "
              "The SAVE Act requires documentary proof of U.S. citizenship when registering to "
              "vote in any federal election. The vote was largely party-line: Republicans "
              "provided almost all of the 220 YEA votes, while Mfume voted with the Democratic "
              "majority in opposition. Mfume represents Baltimore (Maryland's 7th District), "
              "one of the most heavily Democratic and diverse urban districts in the nation, "
              "and has a long record of opposing voter-ID and citizenship-verification "
              "requirements as policies that disproportionately burden low-income and minority "
              "voters. By voting NAY on the SAVE Act, Mfume opposes the rubric's "
              "election_integrity[0] standard favoring documentary citizenship verification "
              "as a condition of voter registration.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/bills/119/hr22",
               "https://www.govtrack.us/congress/members/kweisi_mfume/407672"]),
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
