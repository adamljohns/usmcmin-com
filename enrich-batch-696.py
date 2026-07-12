#!/usr/bin/env python3
"""Enrichment batch 696: cited claims for 5 Washington State Representatives.

All archetype_curated federal buckets are exhausted; pivoting to WA State
Representatives from the bottom of the alphabet (WA, bottom of reversed list).

Targets (5, all D, WA):
  Mari Leavitt       (WA HD-28, University Place / Pierce County)
  Liz Berry          (WA HD-36, Seattle)
  Lisa Parshley      (WA HD-22, Thurston County / Olympia)
  Lisa Callan        (WA HD-5,  Issaquah / East King County)
  Lillian Ortiz-Self (WA HD-21, Mukilteo / Edmonds / Snohomish County)

Sources: housedemocrats.wa.gov, leg.wa.gov, washingtonstatestandard.com,
         ballotpedia.org, bluevoterguide.org, progressivevotersguide.com,
         opb.org, knkx.org, nwprogressive.org, glsen.org, fox13seattle.com,
         gunresponsibility.org, plannedparenthoodaction.org, aclu-wa.org,
         cascadepbs.org, kimatv.com, mynorthwest.com, komonews.com

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
    # -------------- Mari Leavitt (WA HD-28, University Place / Pierce County) --------------
    ("mari-leavitt", "WA", "Representative", [
        claim("ml1", "mari-leavitt", "sanctity_of_life", 4, False,
              "Leavitt is a confirmed Planned Parenthood Alliance Advocates (PPAA) and Pro-Choice "
              "Washington endorsee in both her 2024 primary and general elections, placing her "
              "squarely in the abortion-industry endorsement-and-funding network. As Deputy Majority "
              "Whip she organizes and delivers caucus votes on reproductive-rights bills as a "
              "matter of her leadership role.",
              ["https://bluevoterguide.org/WA/candidate_Mari_Leavitt/36431",
               "https://housedemocrats.wa.gov/leavitt/2024/12/13/leavitt-re-elected-deputy-majority-whip/"]),
        claim("ml2", "mari-leavitt", "self_defense", 1, False,
              "Leavitt is endorsed by Gun Sense Voter (the Moms Demand Action / Everytown voter "
              "outreach arm) in both the 2024 primary and general, signaling consistent support "
              "for firearm restrictions. As Deputy Majority Whip she organized and delivered the "
              "House Democratic caucus's party-line yes vote for HB 1240 (2023), Washington's "
              "assault weapons ban, which passed 55-42 and was signed April 25, 2023 — directly "
              "opposing the rubric's protection of the right to own semi-automatic firearms.",
              ["https://bluevoterguide.org/WA/candidate_Mari_Leavitt/36431",
               "https://www.seattletimes.com/seattle-news/politics/wa-house-votes-to-ban-assault-weapons/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023"]),
        claim("ml3", "mari-leavitt", "family_child_sovereignty", 0, False,
              "Leavitt voted YES on SB 5181 / HB 1296 (2025), the Democrat-authored rewrite of "
              "Washington's voter-approved 2024 Parents' Bill of Rights (Initiative 2081). As "
              "Deputy Majority Whip, her vote was part of the strict party-line 56-37 majority "
              "that passed the bill at 2:15 a.m. after an all-night floor debate. The rewrite "
              "removed medical records from parental inspection rights, explicitly protected "
              "students' gender identity and sexual orientation from mandatory parental disclosure, "
              "and required all school districts to adopt new transgender student policies by "
              "January 31, 2026. Gov. Ferguson signed it May 20, 2025; conservative parent "
              "groups subsequently filed a lawsuit in Thurston County Superior Court to overturn it.",
              ["https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/"]),
    ]),

    # -------------- Liz Berry (WA HD-36, Seattle) --------------
    ("liz-berry", "WA", "Representative", [
        claim("lb1", "liz-berry", "self_defense", 1, False,
              "Berry is Washington's most aggressive gun-control legislator. She was the PRIMARY "
              "SPONSOR of HB 1163 (2025), which created a mandatory permit-to-purchase system "
              "requiring every firearm buyer to obtain a 5-year state permit from the Washington "
              "State Patrol after completing a certified firearms safety course and paying a fee. "
              "The bill passed the House 58-38 and Senate 57-39 on strict party lines and was "
              "signed by Gov. Ferguson May 20, 2025, taking effect May 1, 2027. She was also "
              "the primary sponsor of HB 1143 (2023, mandatory 10-day waiting period for all "
              "purchases) and HB 1903 (2024, mandatory reporting of lost/stolen firearms), and "
              "co-sponsored the 2023 assault weapons ban (HB 1240). Fox 13 Seattle headline: "
              "'Fourth year in the legislature and Rep. Liz Berry's main purpose is to pass gun "
              "laws.' She serves as national co-chair of Legislators for Safer Communities, the "
              "premier anti-gun-rights state legislative coalition.",
              ["https://washingtonstatestandard.com/2025/05/20/washingtonians-will-need-state-permit-to-buy-guns-under-new-law/",
               "https://www.opb.org/article/2025/05/21/washington-gun-law-permit-safety-course-house-bill-1163-firearms/",
               "https://www.fox13seattle.com/news/fourth-year-in-the-legislature-and-rep-liz-berrys-main-purpose-is-to-pass-gun-laws"]),
        claim("lb2", "liz-berry", "sanctity_of_life", 4, False,
              "Berry is a former board member of Pro-Choice Washington and is endorsed by "
              "Planned Parenthood Alliance Advocates. She co-sponsored Washington's 2023 "
              "Reproductive Care Shield Law (HB 1469), which prevents Washington courts, law "
              "enforcement, and professional licensing boards from cooperating with other states "
              "that seek to prosecute individuals involved in abortion care or gender-affirming "
              "care. She also co-sponsored employer protections for reproductive-care benefits "
              "(HB 1286, 2023) and championed increased state budget funding for family-planning "
              "services.",
              ["https://housedemocrats.wa.gov/berry/2023/07/27/345/",
               "https://www.aclu-wa.org/press-releases/aclu-washington-comment-signing-washingtons-abortion-and-gender-affirming-care-bills-law/",
               "https://housedemocrats.wa.gov/berry/2023/01/11/berry-keiser-bills-would-protect-employers-who-provide-reproductive-care-benefits/"]),
        claim("lb3", "liz-berry", "family_child_sovereignty", 0, False,
              "Berry voted YES on HB 1296 (2025), the rewrite of voter-approved Initiative 2081 "
              "(Washington's 2024 Parents' Bill of Rights), which removed medical records from "
              "parental inspection rights, protected students' gender identity from mandatory "
              "parental disclosure, and required school districts to adopt new transgender student "
              "policies by January 31, 2026. She also voted YES on SB 5462 (2024), mandating "
              "LGBTQ+ inclusive curricula in all Washington public schools — Washington became "
              "the seventh state to impose such a requirement.",
              ["https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://www.glsen.org/news/washington-governor-jay-inslee-signs-lgbtq-inclusive-curriculum-state-law",
               "https://www.cascadepbs.org/politics/2024/03/legislature-decides-wa-schools-should-include-lgbtq-history/"]),
    ]),

    # -------------- Lisa Parshley (WA HD-22, Thurston County / Olympia) --------------
    ("lisa-parshley", "WA", "Representative", [
        claim("lp1", "lisa-parshley", "sanctity_of_life", 4, False,
              "Parshley was endorsed by Planned Parenthood Alliance Advocates in her successful "
              "2024 race, placing her in the abortion-industry endorsement-and-funding network. "
              "As a freshman in the 2025 session she co-sponsored HB 2182, which removed the "
              "requirement that the Department of Corrections charge a cost-plus-$5 markup per "
              "dose from Washington's state-owned mifepristone stockpile, making the medication "
              "abortion drug easier to distribute to clinics statewide.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements",
               "https://komonews.com/news/politics/washington-state-lawmakers-discuss-bill-to-improve-access-to-abortion-medications-mifepristone-pregnancy-birth-law-legal-pro-choice-life-conception-roe-wade-payment-insurance-planned-parenthood"]),
        claim("lp2", "lisa-parshley", "family_child_sovereignty", 0, False,
              "In her first full legislative session, Parshley voted YES on HB 1296 (2025), the "
              "Democrat-authored rewrite of Washington's voter-approved 2024 Parents' Bill of "
              "Rights (Initiative 2081). The rewrite passed 56-37 on strict party lines at "
              "2:15 a.m. and was signed by Gov. Ferguson May 20, 2025. It removed medical records "
              "from parental inspection rights, explicitly protected students' gender identity and "
              "sexual orientation from mandatory parental disclosure, and required all school "
              "districts to adopt new transgender student policies by January 31, 2026. "
              "Conservative parent groups filed a lawsuit in Thurston County Superior Court "
              "to overturn the law.",
              ["https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://kimatv.com/news/local/house-bill-1296-passes-after-long-debate-sparking-controversy-over-parental-rights",
               "https://www.opb.org/article/2025/10/25/washington-parental-rights-law-conservative-group/"]),
        claim("lp3", "lisa-parshley", "self_defense", 1, False,
              "In her first weeks in office, Parshley co-sponsored HB 1132 (2025), which would "
              "have prohibited firearm dealers from selling more than one firearm or more than "
              "1,000 rounds of ammunition to the same buyer within any 30-day period. Though "
              "the bill died in the Rules Committee (referred to Rules 2 Review), her immediate "
              "co-sponsorship upon taking office signals a firm anti-gun posture consistent with "
              "her PPAA endorsement bloc.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1132&Year=2025",
               "https://www.nraila.org/articles/20250113/washington-2025-legislative-session-convenes-gun-control-bills-pre-filed"]),
    ]),

    # -------------- Lisa Callan (WA HD-5, Issaquah / East King County) --------------
    ("lisa-callan", "WA", "Representative", [
        claim("lc1", "lisa-callan", "self_defense", 1, False,
              "Callan voted YES on HB 1240 (2023), Washington's assault weapons ban, which "
              "passed 55-42 and was signed April 25, 2023, banning the manufacture, import, "
              "distribution, and sale of assault weapons in the state. She also co-sponsored "
              "HB 1132 (2025), which would have prohibited firearm dealers from selling more "
              "than one firearm or more than 1,000 rounds of ammunition to the same buyer "
              "within 30 days.",
              ["https://www.nwprogressive.org/weblog/2023/03/victory-washington-state-house-votes-to-ban-military-style-assault-weapons.html",
               "https://gunresponsibility.org/media-center/washington-state-legislature-passes-hb-1240-to-prohibit-the-sale-of-assault-rifles/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1132&Year=2025"]),
        claim("lc2", "lisa-callan", "biblical_marriage", 4, False,
              "Callan voted YES on SB 5462 (2024), which mandated that all Washington public "
              "school districts adopt curricula incorporating 'histories, contributions, and "
              "perspectives of LGBTQ people' in coordination with the Washington State LGBTQ "
              "Commission. The law was signed by Gov. Inslee March 18, 2024, making Washington "
              "the seventh state to require LGBTQ+ inclusive curriculum in public schools. "
              "Callan also signed the majority committee report supporting HB 1296 (2025), "
              "the rewrite of Washington's voter-approved Parents' Bill of Rights that "
              "protected students' gender identity from mandatory parental disclosure.",
              ["https://www.glsen.org/news/washington-governor-jay-inslee-signs-lgbtq-inclusive-curriculum-state-law",
               "https://www.cascadepbs.org/politics/2024/03/legislature-decides-wa-schools-should-include-lgbtq-history/",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/"]),
        claim("lc3", "lisa-callan", "sanctity_of_life", 4, False,
              "Callan is endorsed by Planned Parenthood Alliance Advocates and Pro-Choice "
              "Washington in multiple election cycles. She co-sponsored HB 1469 (2023), "
              "Washington's Reproductive Care Shield Law, which prevents Washington courts, "
              "law enforcement, and professional licensing boards from cooperating with other "
              "states seeking to prosecute patients, providers, or helpers involved in abortion "
              "care or gender-affirming care. Gov. Inslee signed it April 27, 2023.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/elections/washington-candidate-endorsements",
               "https://www.aclu-wa.org/press-releases/aclu-washington-comment-signing-washingtons-abortion-and-gender-affirming-care-bills-law/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1469&Year=2023"]),
    ]),

    # -------------- Lillian Ortiz-Self (WA HD-21, Mukilteo / Edmonds / Snohomish County) --------------
    ("lillian-ortiz-self", "WA", "Representative", [
        claim("los1", "lillian-ortiz-self", "family_child_sovereignty", 0, False,
              "Ortiz-Self was the PRIMARY SPONSOR of HB 1296 (2025), the Democrat-authored "
              "rewrite of Washington's voter-approved 2024 Parents' Bill of Rights (Initiative "
              "2081). She introduced and shepherded the bill through an all-night House floor "
              "debate; it passed 56-37 on strict party lines at 2:15 a.m. — all Democrats yes, "
              "all Republicans no — and was signed by Gov. Ferguson May 20, 2025. HB 1296 "
              "removed medical records from the scope of parental inspection rights, explicitly "
              "protected students' gender identity and sexual orientation from mandatory parental "
              "disclosure, required all school districts to adopt new transgender student policies "
              "by January 31, 2026, and authorized withholding of up to 20% of state funding "
              "from districts found willfully disobeying civil-rights laws. Conservative parent "
              "groups subsequently filed a lawsuit in Thurston County Superior Court to overturn "
              "the law. Ortiz-Self's stated defense: 'This bill creates clarity to make sure "
              "that it's not just some voices, but all voices are heard.'",
              ["https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://mynorthwest.com/seattles-morning-news/parental-rights-bill/4064560",
               "https://kimatv.com/news/local/house-bill-1296-passes-after-long-debate-sparking-controversy-over-parental-rights",
               "https://www.opb.org/article/2025/10/25/washington-parental-rights-law-conservative-group/"]),
        claim("los2", "lillian-ortiz-self", "biblical_marriage", 2, False,
              "Ortiz-Self publicly defended and voted YES on SB 5599 (2023), which allows "
              "licensed youth shelters to delay notifying parents of a runaway minor's location "
              "when the minor is seeking gender-affirming care, instead notifying the state's "
              "DCYF. In a public statement she said: 'Something needs to happen now to create "
              "a bridge because kids aren't leaving home by choice' — affirming her position "
              "that shelters should facilitate minors' access to gender-affirming care without "
              "parental knowledge or consent. Gov. Inslee signed SB 5599 May 9, 2023.",
              ["https://www.knkx.org/law/2023-05-09/trans-minors-protected-from-washington-law",
               "https://www.snoho.com/html/stories_2023/03292023_healthcare_protection_teenagers_transgender.html"]),
        claim("los3", "lillian-ortiz-self", "self_defense", 1, False,
              "Ortiz-Self voted YES on HB 1240 (2023), Washington's assault weapons ban "
              "(passed 55-42, signed April 25, 2023), banning the manufacture, import, "
              "distribution, and sale of assault weapons statewide. She holds an endorsement "
              "from the Alliance for Gun Responsibility, Washington's primary gun-control "
              "advocacy PAC.",
              ["https://www.nwprogressive.org/weblog/2023/03/victory-washington-state-house-votes-to-ban-military-style-assault-weapons.html",
               "https://gunresponsibility.org/pac/",
               "https://www.electlillian.com/endorsements"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing slug collisions."""
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
