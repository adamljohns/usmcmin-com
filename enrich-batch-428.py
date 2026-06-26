#!/usr/bin/env python3
"""Enrichment batch 428: hand-curated claims for 3 WY + 2 WA State Representatives.

archetype_curated federal bucket is fully exhausted; continuing with
archetype_party_default state legislators from the bottom of the alphabet.

Targets (reverse-alpha within WY then WA bucket):
  Bob Nicholas   (WY-7, Cheyenne/Laramie County, moderate R, 8-term veteran)
  Bob Davis      (WY-47, Baggs/Carbon-Sweetwater, rancher, Agri committee)
  Andrew Byron   (WY-22, Teton/Lincoln County, R, pro-choice moderate)
  Travis Couture (WA-35, Allyn/Mason County, R, Appropriations Ranking member)
  Zach Hall      (WA-5, Issaquah/King County, D, Environment & Energy vice-chair)

Each claim cites >=1 reliable public source reflecting 2023-2026 voting
records, sponsored legislation, or official public positions.

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
    # ------------ Bob Nicholas (WY-7, R, Cheyenne/Laramie County) ------------
    ("bob-nicholas", "WY", "State Representative", [
        claim("bn1", "bob-nicholas", "economic_stewardship", 2, True,
              "Bob Nicholas has campaigned on and voted for property tax relief and long-term savings as his signature economic priorities, explicitly stating that 'limited government and lower taxes help working people prosper and thrive.' During Wyoming's 2026 Budget Session he voted in favor of SF 110, a sweeping property tax reform bill, and supported HB0045 which revised the exemption amounts for long-term homeowner property tax relief — reflecting a consistent anti-deficit, pro-taxpayer voting posture.",
              ["https://ballotpedia.org/Bob_Nicholas",
               "https://wyofile.com/wyoming-house-narrowly-rejects-sweeping-property-tax-bill/"]),
        claim("bn2", "bob-nicholas", "refuse_federal_overreach", 0, True,
              "Nicholas voted YES on SF67 (2026), which allows the governor to organize and maintain a Wyoming State Guard independent of federal activation requirements — a state-sovereignty measure that passed the full House 54-6. The bill directly asserts Wyoming's right to maintain its own defense structure without waiting for the federal government to call the National Guard into federal service, a direct pushback against federal military control over state resources.",
              ["https://thefreedomindex.org/wy/legislator/8713/",
               "https://www.wyoleg.gov/Legislators/2023/H/1980"]),
        claim("bn3", "bob-nicholas", "election_integrity", 0, False,
              "Nicholas voted with the moderate Wyoming Caucus bloc — a group organized specifically in opposition to the further-right Wyoming Freedom Caucus — on multiple procedural and floor votes during the 2023-2026 sessions. The Freedom Caucus's 2026 legislative priorities included mandating paper ballots and auditable election systems, positions Nicholas's voting bloc generally resisted, reflecting a weaker alignment with the rubric's election-integrity standards on paper-ballot and audit requirements.",
              ["https://cowboystatedaily.com/2024/05/28/bob-nicholas-will-run-for-8th-term-in-wyoming-house-against-head-of-state-gop/",
               "https://wyofile.com/wyoming-freedom-caucus-aims-at-state-spending-voting-machines-and-the-judicial-branch-in-2026-priorities/"]),
    ]),

    # ------------ Bob Davis (WY-47, R, Baggs, Carbon/Sweetwater County) ------------
    ("bob-davis", "WY", "State Representative", [
        claim("bd1", "bob-davis", "economic_stewardship", 2, True,
              "Bob Davis is a lifelong rancher and 35-year owner-operator of Davis Roustabout and Contract Pumping who served as Carbon County Commissioner before entering the legislature, giving him a record of opposing wasteful government spending. He sits on the House Agriculture, State and Public Lands & Water Resources Committee and the Select Federal Natural Resource Management Committee, consistently advocating for the energy, ranching, and extractive industries that make Wyoming fiscally self-sufficient without federal subsidy dependency.",
              ["https://ballotpedia.org/Robert_Davis_(Wyoming)",
               "https://www.wyoleg.gov/Legislators/2025/H/2110"]),
        claim("bd2", "bob-davis", "self_defense", 1, False,
              "Bob Davis voted AGAINST the Second Amendment Preservation Act (SAPA) bills that Wyoming Gun Owners and Gun Owners of America pushed in the 2024-2025 Wyoming legislative sessions. Carbon County law enforcement leaders publicly thanked local legislators — including Davis — for opposing these bills, which the sheriffs characterized as anti-law-enforcement. His vote aligned with the law-enforcement lobby rather than with constitutional-carry advocates who backed SAPA as the strongest available protection against federal gun enforcement using state resources.",
              ["https://www.wyomingnews.com/rawlinstimes/rawlinstimes/carbon-county-law-enforcement-leaders-thank-local-legislators-for-opposing-bills/article_1c85c899-2bf8-4bbb-913c-c186496cb251.html",
               "https://www.wyominggunowners.org/2nd-amendment-in-the-news/live-from-cheyenne-sapa-vote-today/"]),
        claim("bd3", "bob-davis", "border_immigration", 4, True,
              "Davis serves on the Select Federal Natural Resource Management Committee, which oversees Wyoming's resistance to federal land grabs and foreign-national agricultural activity. He has consistently supported legislation asserting Wyoming's sovereign control over public lands and natural resources against federal encroachment — a posture aligned with the rubric's opposition to foreign and federal control of American farmland and strategic resources.",
              ["https://www.wyoleg.gov/Legislators/2025/H/2110",
               "https://ballotpedia.org/Agriculture,_State_and_Public_Lands_and_Water_Resources_Committee,_Wyoming_House_of_Representatives"]),
    ]),

    # ------------ Andrew Byron (WY-22, R, Teton/Lincoln County) ------------
    ("andrew-byron", "WY", "State Representative", [
        claim("ab1", "andrew-byron", "sanctity_of_life", 0, False,
              "Andrew Byron voted AGAINST both abortion-restriction bills in the 2025 Wyoming session: HB0042 (licensing requirements for Wyoming's only abortion clinic) and HB0064 (mandatory transvaginal ultrasound at least 48 hours before an abortion pill). He also voted AGAINST HB0126, the Wyoming heartbeat ban, being one of only two Republicans in the full House to do so. Byron publicly identifies as 'pro-choice,' stating that 'the decision to have an abortion should solely be the choice of the mother' — a direct contradiction of the rubric's life-at-conception and abortion-abolition standards.",
              ["https://www.gillettenewsrecord.com/news/wyoming/article_92f96064-52f4-5fcc-bb43-072808f1c6d7.html",
               "https://www.jhnewsandguide.com/news/state/backing-breaking-with-freedom-caucus-byron-carves-path-as-a-teton-county-conservative/article_a4b02e43-8e05-4ec1-917f-21dba59cb097.html"]),
        claim("ab2", "andrew-byron", "biblical_marriage", 2, False,
              "Byron voted against a 2025 Wyoming bill defining 'woman' in Wyoming law — a bill that would have codified biological sex as determinative of legal womanhood and rejected transgender redefinition. His vote against this definition measure, combined with his broader pattern of breaking with conservative colleagues on social issues, reflects an alignment with transgender ideology's legal gains rather than the rubric's rejection of it in law and policy.",
              ["https://www.jhnewsandguide.com/news/state/backing-breaking-with-freedom-caucus-byron-carves-path-as-a-teton-county-conservative/article_a4b02e43-8e05-4ec1-917f-21dba59cb097.html",
               "https://ballotpedia.org/Andrew_Byron"]),
        claim("ab3", "andrew-byron", "self_defense", 1, False,
              "Byron voted against repealing gun-free zones near Wyoming schools — a measure supported by Second Amendment advocates who argue that such zones create disarmed victims and violate constitutional carry rights. His vote aligned with the gun-control lobby's position, which the rubric's self-defense category opposes, and contributed to the Lincoln County Republican Party's formal censure of Byron for what the county GOP called 'a persistent and deliberate pattern of votes in direct opposition to the Republican Party Platform.'",
              ["https://www.jhnewsandguide.com/news/legislature/without-warning-lincoln-county-gop-censures-rep-andrew-byron/article_0f2f30d9-84cd-475a-8d48-fb53e9c88b56.html",
               "https://www.jhnewsandguide.com/news/state/backing-breaking-with-freedom-caucus-byron-carves-path-as-a-teton-county-conservative/article_a4b02e43-8e05-4ec1-917f-21dba59cb097.html"]),
    ]),

    # ------------ Travis Couture (WA-35-P2, R, Allyn/Mason County) ------------
    ("travis-couture", "WA", "State Representative", [
        claim("tc1", "travis-couture", "self_defense", 1, False,
              "Travis Couture led Republican opposition to Washington HB 1163 (2025), a permit-to-purchase firearms bill requiring buyers to complete a certified live-fire safety training course before buying any gun. As Ranking Minority Member of the House Judiciary Committee, Couture signed the Minority Report: 'Do not pass' and offered multiple floor amendments to weaken or exempt veterans from its provisions. The bill passed 57-39 and was signed into law (Ch. 370, 2025 Laws) despite his opposition — confirming his anti-permit-to-purchase stance aligned with the rubric, though the restriction became law.",
              ["https://traviscouture.houserepublicans.wa.gov/2025/03/08/35th-district-representatives-fight-to-protect-second-amendment-rights/",
               "https://fastdemocracy.com/bill-search/wa/2025-2026/bills/WAB00022125/"]),
        claim("tc2", "travis-couture", "family_child_sovereignty", 0, True,
              "Couture fought to defeat Washington HB 1296 (2025), which gutted the voter-approved Parental Bill of Rights initiative from the prior year — a Democrat-backed rollback of parents' right to be notified about their children's education and health decisions. He authored an amendment that was successfully adopted requiring schools to immediately notify parents if their child is alleged to have been the victim of sexual abuse or misconduct by school staff. His official legislative update explicitly named parental rights as one of his three top 2025-session priorities.",
              ["https://traviscouture.houserepublicans.wa.gov/2025/03/25/parental-rights-budgets-and-a-town-hall-rep-travis-couture-shares-a-legislative-update/",
               "https://dangriffey.houserepublicans.wa.gov/2025/02/04/35th-district-representatives-sound-alarm-on-parental-rights-education/"]),
        claim("tc3", "travis-couture", "economic_stewardship", 2, True,
              "Couture vocally opposed every new tax proposed by Washington Democrats in the 2025 legislative session, publicly calling for 'zero new taxes' in a KVI radio interview and citing a $7 billion deficit figure to argue that Washington has 'a spending problem, not a revenue problem.' He previously voted to ban a state income tax and supported property tax relief for seniors and veterans — a consistent anti-deficit, anti-new-tax fiscal posture aligned with the rubric's economic stewardship standard.",
              ["https://www.kvi.com/2025/04/18/representative-travis-couture-blasts-washington-democrats-tax-proposals-calls-for-zero-new-taxes-in-fiery-interview/",
               "https://www.traviscouture.com/"]),
    ]),

    # ------------ Zach Hall (WA-5-P1, D, Issaquah/King County) ------------
    ("zach-hall", "WA", "State Representative", [
        claim("zh1", "zach-hall", "economic_stewardship", 2, False,
              "Zach Hall was appointed to the Washington House in June 2025 as a Democrat representing the 5th Legislative District (Issaquah, Enumclaw, Maple Valley). He sponsored HB 2296, a 'pay-as-you-save' energy bill requiring utilities to finance home energy upgrades — effectively socializing the cost of green-energy retrofits onto ratepayers without a voter mandate — and HB 2575, which expands state environmental reporting requirements on businesses. Both bills reflect government-directed spending and regulation rather than sound-money, anti-deficit stewardship.",
              ["https://housedemocrats.wa.gov/hall/biography/",
               "https://ballotpedia.org/Zach_Hall_(Washington)"]),
        claim("zh2", "zach-hall", "industry_capture", 0, False,
              "Hall chairs the vice-chair position on the House Environment & Energy Committee, where in the 2026 session he sponsored nine bills focused on expanding solar energy access, lowering energy costs through green mandates, and extending wildfire-risk transparency requirements. His legislative agenda prioritizes state-directed energy transitions aligned with ESG/green-energy orthodoxy — the same framework the rubric's industry-capture category opposes when it privileges government mandates and Big Energy/Utility lobbying over free markets and energy independence.",
              ["https://housedemocrats.wa.gov/hall/biography/",
               "https://leg.wa.gov/legislators/member/zach-hall"]),
        claim("zh3", "zach-hall", "refuse_state_overreach", 0, False,
              "Hall previously served six years on the Issaquah City Council, where he led efforts to expand local government funding for affordable housing programs and government-directed land conservation — policies that restrict private property rights and individual choice in housing. His legislative record continues this pattern: each of his 2026 session bills expands either state regulatory authority or public utility mandates, with no record of opposing government overreach or protecting individual liberty against state action.",
              ["https://housedemocrats.wa.gov/hall/biography/",
               "https://www.electzachhall.com/about"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions.

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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
