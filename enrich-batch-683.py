#!/usr/bin/env python3
"""Enrichment batch 683: hand-curated claims for 3 PA state senators + 2 OR state senators.

Continuing archetype_party_default state senators from bottom of alphabet (remaining PA
Democrats + first OR Democrats). Claims span sanctity_of_life, biblical_marriage, and
self_defense categories.

Sources verified against palegis.us, legiscan.com, olis.oregonlegislature.gov,
choicetracker.org, pasenate.com, opb.org, oregoncapitalchronicle.com, witf.org,
ballotpedia.org, en.wikipedia.org.

Targets (from top of reverse-alpha 0-claim archetype_party_default state senator list):
  Art Haywood               (PA SD4, Philadelphia   — D; gun-control advocacy, NO on SB106)
  Anthony H. Williams       (PA SD8, SW Philly/DE   — D; PA LGBT Equality Caucus Whip)
  Amanda M. Cappelletti     (PA SD17, Montgomery/DE — D; former PP Director, abortion pkg)
  Lew Frederick             (OR SD22, Portland      — D; HB 2002, HB 4088, SB 243)
  Khanh Pham                (OR SD23, Portland      — D; HB 2002, HB 4088, HB 4127)
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
    # ---- Art Haywood (PA SD4, Philadelphia area — D, since 2012) ----
    ("art-haywood", "PA", "State Senator", [
        claim("ah1", "art-haywood", "sanctity_of_life", 0, False,
              "Voted NO on SB 106 (July 8, 2022), the Pennsylvania constitutional amendment package "
              "declaring the state constitution confers no right to abortion. The Senate passed 28–22; "
              "Sen. Lisa Boscola was the only Democrat to vote YES. All other Democratic senators, "
              "including Haywood, voted NO, blocking voters from deciding the question.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?sYear=2021&sInd=0&body=S&type=B&bn=106",
               "https://legiscan.com/PA/rollcall/SB106/id/1221943",
               "https://www.inquirer.com/politics/pennsylvania/pa-senate-constitutional-amendments-abortion-elections-voting-20220708.html"]),
        claim("ah2", "art-haywood", "self_defense", 1, False,
              "Sponsored SB 701 to limit handgun purchases to one per month and sponsored fingerprint "
              "licensing legislation, and publicly led press conferences urging Republican colleagues "
              "to move red flag (ERPO) legislation — directly opposing the rubric's defense of "
              "unrestricted Second Amendment rights and opposing red-flag law resistance.",
              ["https://www.senatorhaywood.com/gunviolenceprevention",
               "https://whyy.org/articles/pa-lawmakers-red-flag-laws-gun-control/",
               "https://www.witf.org/2022/06/27/with-new-federal-gun-laws-in-place-pa-lawmakers-push-for-state-red-flag-laws/"]),
        claim("ah3", "art-haywood", "biblical_marriage", 2, False,
              "Co-sponsored SB 150 (the Pennsylvania Fairness Act), which amends the Pennsylvania "
              "Human Relations Act to prohibit discrimination in employment, housing, and public "
              "accommodations based on sexual orientation and gender identity or expression — "
              "embedding transgender ideology into state civil-rights law.",
              ["https://pasenate.com/fairness/",
               "https://www.pahouse.com/LGBTQ/pafairnessact",
               "https://www.palegis.us/legislation/bills/2025/sb150"]),
    ]),

    # ---- Anthony H. Williams (PA SD8, SW Philadelphia/Delaware Co — D, since 1998) ----
    ("anthony-h-williams", "PA", "State Senator", [
        claim("ahw1", "anthony-h-williams", "sanctity_of_life", 0, False,
              "Voted NO on SB 106 (July 8, 2022), the omnibus PA constitutional amendment declaring "
              "no state right to abortion. As one of 20 Democratic senators voting against, he "
              "described the Republicans' procedural maneuver as 'dangerous' to the democratic "
              "process, opposing any constitutional protection for pre-born life.",
              ["https://legiscan.com/PA/rollcall/SB106/id/1221943",
               "https://penncapital-star.com/government-politics/senate-approves-constitutional-amendment-package-as-reproductive-rights-advocates-protest/",
               "https://choicetracker.org/legislator/s8williams"]),
        claim("ahw2", "anthony-h-williams", "sanctity_of_life", 1, False,
              "Voted against legislation banning dilation and evacuation (D&E) abortions and against "
              "a bill prohibiting abortions due to a prenatal Down syndrome diagnosis; recorded as "
              "Pro-Choice across his Senate tenure by Choice Tracker, opposing any gestational or "
              "diagnostic restriction on abortion.",
              ["https://choicetracker.org/legislator/s8williams"]),
        claim("ahw3", "anthony-h-williams", "biblical_marriage", 2, False,
              "Serves as Whip of the Pennsylvania LGBT Equality Caucus and is a co-sponsor of SB 150 "
              "(the Fairness Act), which would bar discrimination based on sexual orientation and "
              "gender identity in employment, housing, and public accommodations statewide.",
              ["https://en.wikipedia.org/wiki/Pennsylvania_LGBT_Equality_Caucus",
               "https://pasenate.com/fairness/",
               "https://pasenate.com/pride/"]),
    ]),

    # ---- Amanda M. Cappelletti (PA SD17, Montgomery/Delaware Co — D, since 2020) ----
    ("amanda-m-cappelletti", "PA", "State Senator", [
        claim("amc1", "amanda-m-cappelletti", "sanctity_of_life", 4, False,
              "Before entering the Pennsylvania Senate, Cappelletti served as Director of Policy for "
              "Planned Parenthood Pennsylvania Advocates, entering her legislative seat directly from "
              "the organization — representing the deepest form of PP institutional alignment the "
              "rubric's qidx-4 flag captures.",
              ["https://ballotpedia.org/Amanda_Cappelletti",
               "https://en.wikipedia.org/wiki/Amanda_Cappelletti",
               "https://pasenatorcappelletti.com/about/"]),
        claim("amc2", "amanda-m-cappelletti", "sanctity_of_life", 0, False,
              "Co-introduced the Abortion Protections Package (SB 837, July 2023) with Sen. Judith "
              "Schwank — a six-bill package repealing all Pennsylvania abortion restrictions including "
              "gestational limits, informed consent waiting periods, parental consent requirements, "
              "spousal notice, and facility licensing rules, while establishing a state right to "
              "reproductive healthcare; received public praise from Planned Parenthood leadership.",
              ["https://pasenate.com/senators-cappelletti-and-schwank-to-introduce-abortion-protections-package-in-pennsylvania/",
               "https://senatorschwank.com/senators-cappelletti-and-schwank-to-introduce-abortion-protections-package-in-pennsylvania/"]),
        claim("amc3", "amanda-m-cappelletti", "self_defense", 1, False,
              "Sponsored SB 637, which would establish a mandatory 72-hour waiting period on all "
              "firearm purchases and transfers in Pennsylvania — a gun-control measure that directly "
              "conflicts with the rubric's opposition to firearm purchase restrictions and "
              "infringement on the right to keep and bear arms.",
              ["https://www.wtaj.com/news/regional-news/gun-control-legislation-to-be-reintroduced-in-pennsylvania/"]),
    ]),

    # ---- Lew Frederick (OR SD22, Northeast Portland — D, since 2014) ----
    ("lew-frederick", "OR", "State Senator", [
        claim("lf1", "lew-frederick", "sanctity_of_life", 0, False,
              "Voted YES on HB 2002 (Oregon Senate, June 2023, 26–20). The bill allows minors of any "
              "age to obtain abortions without parental notification, requires Medicaid and private "
              "insurers to cover gender-affirming procedures, and creates mobile clinics for "
              "reproductive and gender-affirming care in rural areas. Signed by Gov. Kotek "
              "July 13, 2023.",
              ["https://legiscan.com/OR/rollcall/HB2002/id/1291955",
               "https://www.opb.org/article/2023/06/21/oregon-legislature-republican-senate-walkout-reproductive-rights-bill-governor-tina-kotek-desk/",
               "https://oregoncapitalchronicle.com/2023/05/22/heres-what-oregons-controversial-abortion-gender-affirming-care-bill-would-do/"]),
        claim("lf2", "lew-frederick", "biblical_marriage", 2, False,
              "Voted YES on HB 4088 (Oregon Senate, March 5, 2026, 18–12, all 18 Democrats yes). "
              "Bill strengthens legal shield protections for abortion and gender-affirming care "
              "providers and patients, prohibits state employees from assisting federal agencies "
              "in investigating such care, and makes sex/name-change court petitions confidential — "
              "embedding transgender ideology into state law.",
              ["https://www.opb.org/article/2026/03/05/oregon-gender-affirming-care-transgender-abortion/",
               "https://www.ortl.org/shield-law-extending-legal-protections-for-abortion-providers-those-who-assist-in-abortions-passes-oregon-legislature/"]),
        claim("lf3", "lew-frederick", "self_defense", 1, False,
              "Publicly advocated for SB 348 (2023, permit-to-purchase and 10-round magazine ban), "
              "stating 'Anything we can do to cut down on the number of guns...is something that "
              "will be helping.' Also voted YES on SB 243 (June 2025), the Community Safety Firearms "
              "Act banning rapid-fire activators (bump stocks, binary triggers) statewide; Senate "
              "passed 17–12 on party lines.",
              ["https://www.kgw.com/article/news/politics/oregon-senate-bill-348-gun-control/283-05e02bac-1047-4eb0-ae6d-604869a09448",
               "https://oregoncapitalchronicle.com/2025/06/26/oregon-lawmakers-pass-gun-bill-to-ban-rapid-fire-devices-allow-new-concealed-carry-rules/",
               "https://olis.oregonlegislature.gov/liz/2025R1/Measures/Overview/SB243"]),
    ]),

    # ---- Khanh Pham (OR SD23, Outer SE/NE Portland — D, since Jan 2025; prev. HD46) ----
    ("khanh-pham", "OR", "State Senator", [
        claim("kp1", "khanh-pham", "sanctity_of_life", 0, False,
              "Voted YES on HB 2002 (Oregon House, May 2023, all 36 House Democrats in favor) as "
              "Oregon House member for HD 46. Bill allows minors of any age to access abortion "
              "without parental consent, mandates insurance coverage for gender-affirming care, and "
              "protects out-of-state patients receiving care in Oregon. Signed into law July 13, 2023.",
              ["https://www.opb.org/article/2023/05/02/abortion-gender-affirming-health-care-oregon-bill-2002/",
               "https://oregoncapitalchronicle.com/2023/05/01/oregon-house-passes-sweeping-bill-to-guarantee-access-to-abortion-gender-affirming-care/"]),
        claim("kp2", "khanh-pham", "biblical_marriage", 2, False,
              "Voted YES on HB 4088 (Oregon Senate, March 2026, all 18 Senate Democrats yes) as OR "
              "Senator SD 23. Bill extends abortion and gender-affirming care shield protections, adds "
              "privacy rights for transgender individuals seeking legal sex/name changes, and bars "
              "extradition for receiving legal-in-Oregon care — enshrining transgender ideology "
              "into state law.",
              ["https://www.opb.org/article/2026/03/05/oregon-gender-affirming-care-transgender-abortion/",
               "https://www.ortl.org/oregon-legislature-passes-bill-creating-permanent-state-taxpayer-funding-for-oregon-planned-parenthood/"]),
        claim("kp3", "khanh-pham", "sanctity_of_life", 4, False,
              "Voted YES on HB 4127 (Oregon Senate, March 2026, party-line) as OR Senator SD 23. "
              "Bill creates permanent state taxpayer funding for Oregon's Planned Parenthood health "
              "centers to replace lost federal Medicaid reimbursements, signed by Gov. Kotek May 2026 "
              "— representing direct legislative sponsorship of PP's operating budget with public funds.",
              ["https://nrlc.org/nrlnewstoday/2026/03/new-oregon-law-will-create-permanent-state-taxpayer-funding-for-oregons-planned-parenthoods/",
               "https://oregoncapitalchronicle.com/2026/05/13/oregon-governor-signs-laws-to-backfill-planned-parenthood-funding-strengthen-shield-law/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
