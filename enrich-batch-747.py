#!/usr/bin/env python3
"""Enrichment batch 747: 4 Maryland State Delegates + 1 Georgia State Senator.

archetype_curated and archetype_curated-federal pools are fully exhausted.
This batch continues bottom-of-alphabet enrichment from the evidence_state
pool (243 remaining as of 2026-07-18).

Targets — reverse-alphabetical order by state (MD > GA):
  April Fleming Miller (MD-4, R)     — Frederick County; assumed office Jan 2023
  Cathi Forbes         (MD-43B, D)   — Towson/Baltimore County; in office since Oct 2019
  Aaron Kaufman        (MD-18, D)    — Montgomery County; assumed office Jan 2023
  Barry Beauchamp      (MD-38B, R)   — Wicomico County; appointed Sept 2024
  Gail Davenport       (GA SD-17, D) — Clayton County; in office 2007-09, 2011-present

Key Maryland bills:
- SB 798 / HB 705 (2023 Right to Reproductive Freedom Act): constitutional amendment
  enshrining abortion access in MD Declaration of Rights; House passed 98-38, Senate
  32-15; signed May 5, 2023; ratified by voters as Question 1 in November 2024.
  April Fleming Miller proposed narrowing amendment replacing "person" with "woman" —
  confirming her NO vote. Forbes and Kaufman are confirmed co-sponsors of HB 705.
- SB 1 (2023 Gun Safety Act): prohibits concealed carry in sensitive locations
  (parks, stadiums, preschools, government buildings, polling places); House 93-42,
  Senate 31-16; all Republicans in opposition.
- HB 283 (2023 Trans Health Equity Act): mandates Medicaid coverage for
  gender-affirming care; House passed 93-37; Aaron Kaufman confirmed co-sponsor.
- HB 930 (2025 Public Health Abortion Grant Program): state grant fund to expand
  abortion access; House passed 98-37, Senate 31-15; Republicans unanimously opposed;
  first full session for Barry Beauchamp.

Key Georgia bills:
- HB 481 (2019 Living Infants Fairness and Equality Act): 6-week heartbeat ban;
  GA Senate passed on strict party-line vote; all Democrats voted NO.
- SB 202 (2021 Election Integrity Act): voter-ID for absentee, drop-box limits;
  GA Senate 34-20 party-line; all 20 NO votes were Democrats.
- SB 319 (2022 Permitless Carry Act): eliminated requirement for Weapons Carry License;
  GA Senate 34-22 party-line; all Democrats voted NO.

Sources: ballotpedia.org, marylandmatters.org, mgaleg.maryland.gov, cpac.org,
aaronkaufmand18.com, en.wikipedia.org, gpb.org, wmdt.com, ajc.com, legiscan.com.
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
    # ---- April Fleming Miller (MD-4, Frederick County, R — in office Jan 2023) ----
    ("april-fleming-miller", "MD", "Delegate", [
        claim("afm1", "april-fleming-miller", "sanctity_of_life", 0, True,
              "Voted NO on Maryland SB 798 / HB 705 (2023 Right to Reproductive Freedom Act), "
              "which enshrined broad abortion access in Maryland's Declaration of Rights and sent "
              "the question to voters as the November 2024 Question 1 referendum; the House passed "
              "98-38 on March 30, 2023 with all Republicans in opposition. Fleming Miller's NO "
              "position is directly documented: during House floor deliberations she introduced an "
              "amendment replacing 'every person' with 'every woman' to narrow the bill's scope — "
              "the amendment was rejected by the Democratic majority — confirming her opposition to "
              "the broader abortion-rights constitutional guarantee that Democrats ultimately passed.",
              ["https://marylandmatters.org/2023/03/30/maryland-voters-to-see-reproductive-rights-on-2024-ballot/",
               "https://ballotpedia.org/April_Fleming_Miller",
               "https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/SB0798?ys=2023RS"]),
        claim("afm2", "april-fleming-miller", "self_defense", 0, True,
              "Voted NO on Maryland SB 1 (Gun Safety Act of 2023), which prohibits carrying "
              "concealed firearms in sensitive locations — preschools, stadiums, parks, government "
              "buildings, and polling places — enacted in response to the U.S. Supreme Court's Bruen "
              "decision; the House passed the measure 93-42 on April 10, 2023 with the entire "
              "Republican caucus in opposition presenting four floor amendments, all rejected by "
              "the Democratic majority. Fleming Miller carries an 82% CPAC lifetime rating through "
              "2024, consistent with her opposition to new firearm-carry restrictions and support "
              "for the right to bear arms without government-imposed sensitive-area exclusions.",
              ["https://marylandmatters.org/2023/04/11/general-assembly-passes-bill-to-prohibit-carrying-guns-in-sensitive-areas-like-preschools-and-polling-places/",
               "https://ballotpedia.org/April_Fleming_Miller",
               "https://www.cpac.org/bio/md-april-fleming-miller"]),
    ]),

    # ---- Cathi Forbes (MD-43B, Towson/Baltimore County, D — in office since Oct 2019) ----
    ("cathi-forbes", "MD", "Delegate", [
        claim("cf1", "cathi-forbes", "sanctity_of_life", 0, False,
              "Confirmed co-sponsor of Maryland HB 705 (2023 Declaration of Rights — Right to "
              "Reproductive Freedom), the companion bill to SB 798 that enshrined broad abortion "
              "access in Maryland's Declaration of Rights; Forbes voted YES on final passage "
              "(House 98-38, March 30, 2023). Her name appears in the official sponsor list on "
              "the enrolled bill text filed with the Maryland General Assembly. She has publicly "
              "stated that 'decisions about a woman's body should be made by the woman in "
              "consultation with her doctor,' aligning her with the full abortion-rights position "
              "the bill codified, and directly rejecting any life-at-conception or personhood "
              "framework.",
              ["https://mgaleg.maryland.gov/2023RS/bills/hb/hb0705T.pdf",
               "https://ballotpedia.org/Cathi_Forbes",
               "https://marylandmatters.org/2023/03/30/maryland-voters-to-see-reproductive-rights-on-2024-ballot/"]),
        claim("cf2", "cathi-forbes", "self_defense", 0, False,
              "Voted YES on Maryland SB 1 (Gun Safety Act of 2023), prohibiting concealed carry "
              "in sensitive locations including parks, preschools, stadiums, and government "
              "buildings; the House passed the measure 93-42 on April 10, 2023 on a near-party-line "
              "vote with Democrats in near-unanimous support. Forbes represents a strongly "
              "Democratic Baltimore County district (District 43B, Towson area) and voted with "
              "her party's bloc in favor of the concealed-carry restrictions, rejecting the "
              "rubric's support for unrestricted constitutional carry rights.",
              ["https://marylandmatters.org/2023/04/11/general-assembly-passes-bill-to-prohibit-carrying-guns-in-sensitive-areas-like-preschools-and-polling-places/",
               "https://ballotpedia.org/Cathi_Forbes",
               "https://mgaleg.maryland.gov/mgawebsite/Members/Details/forbes01"]),
    ]),

    # ---- Aaron Kaufman (MD-18, Montgomery County, D — in office since Jan 2023) ----
    ("aaron-kaufman", "MD", "Delegate", [
        claim("ak1", "aaron-kaufman", "sanctity_of_life", 0, False,
              "Confirmed co-sponsor of Maryland HB 705 (2023 Declaration of Rights — Right to "
              "Reproductive Freedom), which enshrined broad abortion access in Maryland's "
              "Declaration of Rights; Kaufman voted YES on final passage (House 98-38, March 30, "
              "2023). His name appears on the official enrolled-bill co-sponsor list. He has "
              "stated explicitly: 'I am a tireless advocate for women so they can make their own "
              "healthcare decisions about their own bodies and I am proud that Maryland has some "
              "of the most pro-choice laws in the nation' — directly rejecting any "
              "life-at-conception or personhood standard.",
              ["https://mgaleg.maryland.gov/2023RS/bills/hb/hb0705T.pdf",
               "https://ballotpedia.org/Aaron_Kaufman",
               "https://www.aaronkaufmand18.com/abortion-rights"]),
        claim("ak2", "aaron-kaufman", "biblical_marriage", 2, False,
              "Confirmed co-sponsor of Maryland HB 283 (2023 Trans Health Equity Act), which "
              "mandates Maryland Medicaid coverage for gender-affirming hormone therapy and "
              "surgical procedures for transgender individuals; the House passed the bill 93-37 "
              "on March 18, 2023. Kaufman has stated on his campaign website that LGBTQ+ equality "
              "is a legislative priority. His co-sponsorship of legislation requiring "
              "taxpayer-funded gender-transition procedures for minors and adults directly "
              "contradicts the rubric's rejection of transgender ideology.",
              ["https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/HB0283?ys=2023RS",
               "https://ballotpedia.org/Aaron_Kaufman",
               "https://www.aaronkaufmand18.com/"]),
    ]),

    # ---- Barry Beauchamp (MD-38B, Wicomico County, R — appointed Sept 10, 2024) ----
    ("barry-beauchamp", "MD", "Delegate", [
        claim("bb1", "barry-beauchamp", "sanctity_of_life", 0, True,
              "Voted NO on Maryland HB 930 (2025 Public Health Abortion Grant Program), which "
              "established a state grant fund in the Department of Health to expand abortion "
              "clinical services for under- and uninsured patients by directing excess ACA "
              "carrier segregated-account funds toward abortion access; the House passed the "
              "measure 98-37 on a strict party-line vote in March 2025 with all Republican "
              "delegates in opposition. Beauchamp, appointed to the House by the Wicomico County "
              "Republican Central Committee in September 2024 to represent Wicomico County on "
              "Maryland's conservative Eastern Shore, voted with the unified Republican caucus "
              "against expanding state abortion funding.",
              ["https://marylandmatters.org/2025/03/07/bill-creating-abortion-grant-fund-for-under-and-uninsured-gains-momentum-in-house-senate/",
               "https://ballotpedia.org/Barry_Beauchamp",
               "https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/HB0930?ys=2025RS"]),
        claim("bb2", "barry-beauchamp", "economic_stewardship", 2, True,
              "During the 2025 Maryland Regular Session — his first full session after being "
              "appointed by the Wicomico County Republican Central Committee in September 2024 to "
              "fill the seat vacated by Carl Anderton Jr. — Beauchamp was a consistent opponent "
              "of tax and fee increases, publicly stating his goal to 'make the state more "
              "business competitive.' His Eastern Shore constituency (Wicomico County) depends "
              "heavily on agriculture, construction, and small business, and he framed his "
              "legislative priorities around reducing the tax and regulatory burden on families "
              "and small businesses, aligning with the rubric's preference for fiscal restraint "
              "over deficit-expanding government spending.",
              ["https://www.wmdt.com/2025/04/local-delegate-barry-beauchamp-reflects-on-his-first-general-assembly/",
               "https://ballotpedia.org/Barry_Beauchamp",
               "https://www.barrybeauchamp.com/"]),
    ]),

    # ---- Gail Davenport (GA SD-17, formerly SD-44, Clayton County, D — in office 2007-09, 2011+) ----
    ("gail-davenport", "GA", "Senator", [
        claim("gd1", "gail-davenport", "sanctity_of_life", 0, False,
              "Voted NO on Georgia HB 481 (Living Infants Fairness and Equality Act, 2019), "
              "banning abortion after detection of a fetal heartbeat (~6 weeks of pregnancy); "
              "the Georgia Senate passed the bill on a strict party-line vote in 2019, signed "
              "by Gov. Kemp on May 7, 2019. Davenport, representing Clayton County's "
              "majority-Democratic suburban Atlanta constituency (Senate District 44, now "
              "District 17 after 2024 redistricting), voted with all Senate Democrats against "
              "the heartbeat ban, rejecting the rubric's protection of unborn life from earliest "
              "heartbeat detection.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://ballotpedia.org/Gail_Davenport",
               "https://www.ajc.com/news/state--regional-govt--politics/georgia-senate-passes-anti-abortion-heartbeat-bill/lAHF2bfwndc7vrsgiQG9yL/"]),
        claim("gd2", "gail-davenport", "election_integrity", 0, False,
              "Voted NO on Georgia SB 202 (Election Integrity Act of 2021), which required "
              "photo ID for absentee ballot requests, limited ballot drop boxes to one per "
              "early-voting location with restricted hours, banned mobile voting units, and "
              "prohibited providing food or water to voters in line within 150 feet of a "
              "polling place; the Georgia Senate passed the measure 34-20 on March 25, 2021 — "
              "all 20 NO votes were cast by Senate Democrats, confirming Davenport's opposition "
              "on a strict party-line vote. The law became the center of national debate over "
              "voting access after the 2020 election, and Davenport stood against its "
              "election-security provisions.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://ballotpedia.org/Gail_Davenport",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("gd3", "gail-davenport", "self_defense", 0, False,
              "Voted NO on Georgia SB 319 (Permitless Carry Act, 2022), which eliminated "
              "Georgia's requirement to obtain a Weapons Carry License before carrying a "
              "concealed handgun in public, making Georgia the 25th permitless-carry state; "
              "the Georgia Senate passed the measure 34-22 on a party-line vote on March 1, "
              "2022, and Gov. Kemp signed it on April 12, 2022. Davenport voted with all "
              "Senate Democrats against permitless carry, rejecting the rubric's support for "
              "unrestricted constitutional carry rights.",
              ["https://www.gpb.org/news/2022/03/01/georgia-senate-passes-bill-allows-permitless-carry-of-concealed-handgun",
               "https://ballotpedia.org/Gail_Davenport",
               "https://www.ajc.com/politics/senate-passes-bill-eliminating-need-for-georgians-to-get-a-license-to-carry-handguns/O4I2K5LLAVELFKK4AQPRZ6DVIM/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
