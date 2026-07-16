#!/usr/bin/env python3
"""Enrichment batch 716: evidence-curated claims for 5 state officials.

Primary federal senator/representative pools (archetype_curated with 0 claims)
are fully exhausted. Batch continues evidence_state candidates with 0 claims,
bottom-of-alphabet reverse-sort (TX -> NM -> NJ -> NJ -> MD):

  Aicha Davis              (TX-D, Texas State Representative HD-109, since Jan 2025)
  Howie Morales            (NM-D, Lt. Governor, since Jan 2019; re-elected 2022)
  Jennifer Davenport       (NJ-D, Attorney General, confirmed Feb 2026)
  Dale Caldwell            (NJ-D, Lt. Governor / Secretary of State, since Nov 2025)
  Christopher Eric Bouchat (MD-R, State Delegate District 5, 2023-2026)

Claims sourced to texaspolicyresearch.com, texastribune.org, ballotpedia.org,
lgo.nm.gov, legiscan.com, adfmedia.org, njoag.gov, bearingarms.com,
en.wikipedia.org, mgaleg.maryland.gov, and foxbaltimore.com.
All reflect 2020-2026 public record.
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
    # --------------- Aicha Davis (TX-D, Texas State Representative HD-109) ---------------
    ("aicha-davis", "TX", "Representative", [
        claim("ad1", "aicha-davis", "sanctity_of_life", 0, False,
              "Voted NO on SB 33 (89th Legislature, 'Stop Taxpayer-Funded Abortion Travel Act,' "
              "passed 87-58 along party lines, May 22, 2025), which banned state and local government "
              "funding of abortion travel, lodging, meals, childcare, and logistical support for "
              "abortion seekers. Davis is a Planned Parenthood Legislative Champion with a stated "
              "100% pro-choice voting record who publicly supports 'restoring the right to abortion "
              "care, including mifepristone' -- rejecting any protection of unborn life.",
              ["https://www.texaspolicyresearch.com/bills/89th-legislature-sb-33/",
               "https://ballotpedia.org/Aicha_Davis"]),
        claim("ad2", "aicha-davis", "self_defense", 1, False,
              "Voted NO on SB 1362 (89th Legislature, 'Anti-Red Flag Act,' passed 86-53 on party "
              "lines, June 2025), which banned enforcement and recognition of Extreme Risk Protective "
              "Orders (red flag gun confiscation laws) in Texas and made enforcement of such orders a "
              "state jail felony -- opposing Texas's legislative defense of the Second Amendment against "
              "red-flag confiscation and aligning with Democrat caucus advocacy for ERPO authority.",
              ["https://www.texastribune.org/2025/05/27/texas-anti-red-flag-law-senate-bill-1362/",
               "https://www.texaspolicyresearch.com/texas-legislature-approves-sb-1362-to-preempt-red-flag-laws-what-you-need-to-know/"]),
        claim("ad3", "aicha-davis", "border_immigration", 1, False,
              "Voted NO on SB 8 (89th Legislature, 'Mandatory ICE 287g Cooperation Act,' passed "
              "89-52 on party lines, June 2025), which required all Texas sheriffs operating jails "
              "to enter into ICE 287(g) warrant-service model agreements mandating state-level "
              "enforcement partnerships with federal immigration authorities. The bill took effect "
              "January 1, 2026; Davis's opposition aligned with the Democrat caucus in blocking "
              "mandatory deportation cooperation.",
              ["https://www.texaspolicyresearch.com/bills/89th-legislature-sb-8/",
               "https://www.texastribune.org/2025/05/24/texas-legislature-sheriffs-ice-agreements/"]),
    ]),

    # --------------- Howie Morales (NM-D, Lt. Governor) ---------------
    ("howie-morales", "NM", "Governor", [
        claim("hm1", "howie-morales", "border_immigration", 0, False,
              "In an April 2020 official Lt. Governor press release, publicly declared 'There is no "
              "urgency whatsoever to construct Trump's Border Wall' and applauded the removal of a "
              "border wall construction worker housing camp from Columbus, NM -- directly opposing "
              "the God-First/America-First border security mandate and thanking Planned Parenthood "
              "of the Rocky Mountains among the civic groups credited with opposing the project.",
              ["https://www.lgo.nm.gov/2020/04/10/lt-gov-howie-morales-applauds-removal-of-border-wall-man-camp-thanks-residents-civic-group-for-voicing-their-opposition/",
               "https://www.heinrich.senate.gov/newsroom/in-the-news/officials-urge-halt-to-border-wall-construction-during-pandemic"]),
        claim("hm2", "howie-morales", "sanctity_of_life", 0, False,
              "As President of the NM Senate, presided over the March 10, 2023 passage of SB 13 "
              "('Reproductive Health Provider Protections Act'), which passed 26-16 on strict party "
              "lines and shielded abortion providers and patients from civil and criminal liability "
              "and from out-of-state extradition -- making New Mexico a legal sanctuary for elective "
              "abortion with no recognition of unborn personhood. Governor Lujan Grisham signed it "
              "April 5, 2023.",
              ["https://legiscan.com/NM/bill/SB13/2023",
               "https://www.governor.state.nm.us/2023/04/05/governor-signs-into-law-protections-for-reproductive-gender-affirming-health-care-providers-and-patients/"]),
        claim("hm3", "howie-morales", "biblical_marriage", 2, False,
              "Accepted an endorsement from Equality New Mexico (the state's leading LGBTQ advocacy "
              "organization) with explicit commitment to 'empower' the LGBTQ community through his "
              "office, and as presiding Senate officer championed the same SB 13 (2023) that also "
              "shielded gender-affirming care providers -- including those treating minors -- from "
              "out-of-state prosecution, actively advancing transgender ideology and gender-affirming "
              "care as official state policy.",
              ["https://www.eqnm.org/news/2018/4/30/equality-new-mexico-endorses-michelle-lujan-grisham-for-governor-and-howie-morales-for-lieutenant-governor-of-new-mexico",
               "https://www.kunm.org/local-news/2023-03-07/senate-passes-bill-to-prevent-obstruction-of-gender-and-reproductive-healthcare"]),
    ]),

    # --------------- Jennifer Davenport (NJ-D, Attorney General) ---------------
    ("jennifer-davenport", "NJ", "Attorney General", [
        claim("jd1", "jennifer-davenport", "sanctity_of_life", 0, False,
              "Visited a Cherry Hill abortion clinic and posted from the official AG account: 'Here "
              "in New Jersey, we will always protect your right to access critical reproductive "
              "healthcare.' Subsequently, the U.S. Supreme Court ruled 9-0 against her (First Choice "
              "Women's Resource Centers, Inc. v. Davenport, No. 24-781, April 29, 2026) that her "
              "office's subpoena against a pro-life pregnancy center's donor records violated the "
              "First Amendment; the day after the unanimous rebuke, she filed a letter demanding "
              "the state court 'proceed to resolve the enforceability' of the subpoena anyway -- "
              "persisting in targeting the pregnancy center.",
              ["https://x.com/NewJerseyOAG/status/1884043210546405489",
               "https://adfmedia.org/case/first-choice-womens-resource-centers-v-davenport/",
               "https://townhall.com/tipsheet/amy-curtis/2026/05/05/ag-davenport-still-targeting-pregnancy-center-despite-scouts-n2675561"]),
        claim("jd2", "jennifer-davenport", "self_defense", 1, False,
              "Condemned the Supreme Court's ruling in Wolford v. Lopez (2026) expanding concealed-"
              "carry rights as 'the latest dangerous blow to public safety,' and in May 2026 "
              "subpoenaed at least 15 federally licensed New Jersey firearms dealers demanding "
              "records of every Glock pistol sold to NJ customers over the prior ten years as "
              "part of a nuisance lawsuit against Glock Inc. -- described by gun-rights groups "
              "as building a de facto statewide gun owner registry.",
              ["https://newjerseyglobe.com/judiciary/davenport-condemns-supreme-court-decision-expanding-concealed-carry-rights/",
               "https://bearingarms.com/camedwards/2026/05/18/nj-attorney-general-demands-gun-stores-produce-customer-records-of-glock-sales-n1232559"]),
        claim("jd3", "jennifer-davenport", "border_immigration", 2, False,
              "In March 2026 filed suit to block ICE and DHS from establishing a 1,500-person "
              "immigration detention facility in Roxbury, NJ; under the Safe Communities Act "
              "(January 2026), published model policies directing schools, hospitals, shelters, "
              "and places of worship to limit cooperation with federal immigration enforcement -- "
              "creating statewide sanctuary protocols. The DHS publicly labeled NJ officials "
              "'sanctuary politicians' in a May 2026 press release.",
              ["https://www.njoag.gov/governor-sherrill-attorney-general-davenport-roxbury-township-sue-ice-dhs-over-plans-to-convert-warehouse-into-mass-detention-facility/",
               "https://www.insidernj.com/press-release/attorney-general-davenport-publishes-model-policies-to-protect-access-to-essential-services-as-federal-government-continues-to-target-new-jerseys-immigrant-communities/"]),
    ]),

    # --------------- Dale Caldwell (NJ-D, Lt. Governor / Secretary of State) ---------------
    ("dale-caldwell", "NJ", "Governor", [
        claim("dc1", "dale-caldwell", "sanctity_of_life", 0, False,
              "Ran as Governor Mikie Sherrill's chosen running mate on an explicit platform to "
              "enshrine abortion rights in the New Jersey Constitution, stockpile mifepristone, "
              "strengthen shield laws for abortion providers, and require expanded reproductive "
              "health coverage. After taking office (November 2025), the Sherrill-Caldwell "
              "administration publicly defended NJ's abortion insurance coverage when the Trump "
              "administration opened an investigation in March 2026, Governor Sherrill calling it "
              "'a fishing expedition' -- rejecting all legal protection for unborn life.",
              ["https://www.njspotlightnews.org/2025/10/nj-governors-race-sherrill-and-ciattarelli-on-abortion-gun-rights-vaccines/",
               "https://www.nj.gov/governor/news/2026/approved/20260319a.shtml"]),
        claim("dc2", "dale-caldwell", "biblical_marriage", 2, False,
              "Named by Garden State Equality in their victory statement as an 'LGBTQ+ ally' "
              "celebrating the 'resounding rejection of bigotry, inequality, and the erosion of "
              "civil rights.' The Sherrill-Caldwell administration maintains a state Transgender "
              "Information Hub (nj.gov/transgender), funds gender-affirming care by official "
              "policy, and issued a joint agency statement in December 2025 opposing HHS actions "
              "restricting gender-affirming care for youth -- promoting transgender ideology "
              "through official state channels.",
              ["https://www.insidernj.com/press-release/equality-wins-in-new-jersey-lgbtq-allies-mikie-sherrill-and-dale-caldwell-elected-in-resounding-victory/",
               "https://www.nj.gov/transgender/"]),
        claim("dc3", "dale-caldwell", "border_immigration", 2, False,
              "The Sherrill-Caldwell administration signed Executive Order No. 12 banning ICE "
              "agents from accessing nonpublic state property without a judicial warrant, and in "
              "June 2026 announced a $12 million increase in the Detention Deportation Defense "
              "Initiative (DDDI) -- bringing total funding to $20.2 million -- plus launched a "
              "Rapid Legal Response Initiative providing statewide legal defense for immigrants "
              "facing deportation. DHS publicly labeled NJ officials 'sanctuary politicians.'",
              ["https://www.nj.gov/governor/news/2026/20260211a.shtml",
               "https://www.nj.gov/governor/news/2026/20260604a.shtml"]),
    ]),

    # --------------- Christopher Eric Bouchat (MD-R, State Delegate District 5) ---------------
    ("christopher-eric-bouchat", "MD", "Delegate", [
        claim("cb1", "christopher-eric-bouchat", "sanctity_of_life", 0, True,
              "In March 2023, voted NAY on HB 705 / SB 798 -- the constitutional amendment "
              "enshrining a 'right to reproductive freedom' in Maryland -- which passed 99-37 with "
              "Republicans unanimously opposed and became 2024 Ballot Question 1 (approved by voters "
              "November 2024). Bouchat's consistent pro-life stance in a heavily Democratic state "
              "reflects sustained legislative defense of unborn life against the enshrinement of "
              "unrestricted abortion access in the state constitution.",
              ["https://ballotpedia.org/Maryland_Question_1,_Right_to_Reproductive_Freedom_Amendment_(2024)",
               "https://marylandmatters.org/2023/03/30/maryland-voters-to-see-reproductive-rights-on-2024-ballot/"]),
        claim("cb2", "christopher-eric-bouchat", "border_immigration", 2, True,
              "Voted NO on Maryland's 2026 bill banning local 287(g) ICE cooperation agreements, "
              "stating it placed 'an over-emphasis on anxieties and concerns of our illegal citizens "
              "over the concerns of public safety of Maryland citizens,' and co-sponsored HB 85 "
              "(2025), the Rachel Morin Act -- which would have repealed Maryland's sanctuary policy "
              "prohibitions and required localities to cooperate with ICE enforcement. Named for a "
              "Maryland woman murdered by an undocumented Salvadoran immigrant in Harford County.",
              ["https://en.wikipedia.org/wiki/Christopher_Eric_Bouchat",
               "https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/hb0085?ys=2025RS"]),
        claim("cb3", "christopher-eric-bouchat", "economic_stewardship", 2, True,
              "Voted NO on Maryland HB 352 (Budget Reconciliation and Financing Act of 2025), which "
              "raised the state's top income tax rate to 6.50% and imposed a 2% surcharge on capital "
              "gains for higher earners, and ran for Governor in 2026 on a platform to replace "
              "Maryland's entire tax system with a 3% flat tax across income, capital gains, and "
              "sales -- championing fiscal restraint and lower taxes as a principled economic stance "
              "against the state's relentless spending growth.",
              ["https://foxbaltimore.com/news/local/republican-chris-bouchat-plans-run-maryland-governor-2026",
               "https://legiscan.com/MD/bill/HB352/2025"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug cross-state collisions."""
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
        print(f"  + {m['name']:<36} ({state}) +{len(new_claims)} claims  "
              f"conf: {old_conf} -> evidence_curated")

    # Minified write -- keep scorecard.json under GitHub's 50 MB warning.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
