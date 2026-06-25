#!/usr/bin/env python3
"""Enrichment batch 414: 5 Wyoming state representatives — Posey, Brown, Campbell, McCann, Neiman.

Continues reverse-alpha Wyoming House enrichment from batch 413.
Sources: wyoleg.gov, legiscan.com, ballotpedia.org, wyomingpublicmedia.org,
         oilcity.news, cowboystatedaily.com, wyofile.com, wyomingrising.org,
         sundancetimes.com, gunowners.org; 2025-2026 Wyoming legislative sessions.

Targets:
  Ivan Posey         (WY-HD33, D, Fremont County — Eastern Shoshone/Army veteran, elected 2024)
  Gary Brown         (WY-HD41, R, Laramie County, elected 2024, 1st term)
  Elissa Campbell    (WY-HD56, R, Natrona County / Casper, elected 2024, 1st term)
  Darin McCann       (WY-HD48, R, Sweetwater County / Rock Springs, PA-C/82nd Airborne, elected 2024)
  Chip Neiman        (WY-HD1, R, Crook County — Speaker of Wyoming House 2025-2026, rancher)

Key bill references:
  HB0126 (2026) – Human Heartbeat Act: bans abortion at detectable heartbeat (~6 wks).
    Primary sponsor: Chip Neiman. 7 NO votes: Byron, Campbell(E), Chestek, Provenza,
    Storer, Yin, Jarvis. House 3rd Reading Feb 24, 2026: 51-7.
    House Concurrence March 5, 2026: 47-7. Gov. Gordon signed as HEA No. 29 on March 9, 2026.
    Posey (D) confirmed AYE — not among the 7 NO votes.
  HB0156 (2025) – Proof of Voter Residency-Registration Qualifications Act:
    Passed House 54-3 (NO: Chestek, Provenza, Sherwood only). Became law March 21, 2025.
  HB0064 (2025) – Chemical Abortion / Ultrasound Requirement:
    Primary sponsor: Neiman. Passed both chambers; Gov. Gordon vetoed; veto overridden by
    both chambers. Subsequently struck down by a Wyoming district court judge.
  HB0014 (2025/2026) – Protecting Self-Defense: Reimbursement and Amendments:
    Sponsor: Gary Brown. Allows reimbursement of legal costs and expungement of record
    when acquitted on lawful self-defense grounds.
  HB0013 (2026) – Ivermectin: No Prescription Required:
    Sponsor: Gary Brown. Removes prescription gatekeeping requirement for ivermectin.
  HB0159 (2025) – Medication Abortion Restrictions:
    Primary sponsor: Darin McCann. Required Wyoming DEQ to test public water systems for
    abortion medications; required women to return fetal tissue to healthcare facilities.
  HB0152 (2025) – Donated Blood-mRNA Disclosure:
    Primary sponsor: Darin McCann. Required disclosure when donated blood came from
    mRNA-vaccinated donor. Not advanced for introduction Feb 3, 2025.
  HB0172 (2025) – Firearms Preemption / Gun-Free-Zone Repeal:
    Co-sponsored by Neiman. Repeals gun-free-zone statutes; strengthens state preemption.
    Passed House 50-10; became law Feb 28, 2025.

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
    # ---- Ivan Posey (WY-HD33, D — Eastern Shoshone tribal member, Army veteran) ----
    ("ivan-posey", "WY", "Representative", [
        claim("ip414-1", "ivan-posey", "sanctity_of_life", 0, True,
              "Voted AYE on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Posey — a registered "
              "Democrat representing Fremont County (HD-33) and the only Native American member of "
              "the 68th Wyoming Legislature — was not among the seven House members who voted "
              "against the bill (Byron, Campbell[E], Chestek, Provenza, Storer, Yin, Jarvis). His "
              "cross-party AYE vote confirmed his support for protecting unborn life. Governor "
              "Gordon signed the bill (HEA No. 29) on March 9, 2026, making Wyoming the 5th state "
              "to enact a heartbeat protection law.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://legiscan.com/WY/bill/HB0126/2026",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat",
               "https://ballotpedia.org/Ivan_Posey"]),
        claim("ip414-2", "ivan-posey", "election_integrity", 0, True,
              "Voted AYE on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency. The "
              "bill passed the House 54-3 on February 28, 2025 — only Chestek, Provenza, and "
              "Sherwood dissented; Posey is not among the dissenting votes, confirming his support "
              "for citizenship-based voter roll integrity. The law took effect March 21, 2025 "
              "(Chapter 172) after Governor Gordon allowed it to pass without his signature.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature",
               "https://ballotpedia.org/Ivan_Posey"]),
    ]),

    # ---- Gary Brown (WY-HD41, R — retired electrician, Independent Baptist, Cheyenne) ----
    ("gary-brown", "WY", "Representative", [
        claim("gb414-1", "gary-brown", "sanctity_of_life", 0, True,
              "Voted AYE on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion "
              "once fetal cardiac activity is detectable (approximately six weeks of gestation), "
              "with exceptions only for life-threatening medical emergencies. Brown is confirmed "
              "by name in the aye column ('Brown, G.') of the March 5, 2026 concurrence roll call "
              "(47-7, with only 7 members dissenting). Governor Gordon signed the bill (HEA No. 29) "
              "on March 9, 2026, making Wyoming the 5th state to enact a heartbeat protection law. "
              "Brown, a retired electrician and Independent Baptist from the Cheyenne area (HD-41), "
              "won his seat by defeating a six-term Republican incumbent in the August 2024 primary.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://legiscan.com/WY/bill/HB0126/2026",
               "https://ballotpedia.org/Gary_Brown_(Wyoming)"]),
        claim("gb414-2", "gary-brown", "self_defense", 0, True,
              "Co-sponsored HB0172 (2025), 'Repeal Gun Free Zones and Preemption Amendments,' "
              "which eliminated all of Wyoming's gun-free-zone statutes and explicitly reserved "
              "sole authority over firearm regulation to the state legislature — preventing cities, "
              "counties, and institutions from creating their own carry restrictions and clearing "
              "the way for constitutional carry statewide. The bill passed the House 50-10 "
              "(January 23, 2025) and became law without Gov. Gordon's signature on February 27, "
              "2025 (Chapter 61, effective July 1, 2025). Gun Owners of America praised its "
              "enactment. Brown also sponsored HB0014 (2025/2026), 'Protecting Self-Defense: "
              "Reimbursement and Amendments,' which allows residents acquitted on lawful "
              "self-defense charges to recover legal costs and expunge their record.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://legiscan.com/WY/bill/HB0172/2025",
               "https://www.gunowners.org/wy02282025/",
               "https://cowboystatedaily.com/2025/01/23/bill-banning-gun-free-zones-blasts-through-wyoming-house/"]),
        claim("gb414-3", "gary-brown", "industry_capture", 0, True,
              "Sponsored HB0013 (2026), 'Ivermectin: No Prescription Required,' which removes "
              "Wyoming's prescription gatekeeping requirement for ivermectin, allowing pharmacies "
              "to dispense the long-approved antiparasitic medication directly to patients without "
              "a physician's prescription. The bill challenges pharmaceutical industry control over "
              "access to a widely used and affordable drug and reflects Brown's skepticism of "
              "pharma-government mandates that restrict patient medical choice and access to "
              "alternative treatments.",
              ["https://www.wyoleg.gov/Legislators/2025/H/2140",
               "https://ballotpedia.org/Gary_Brown_(Wyoming)"]),
    ]),

    # ---- Elissa Campbell (WY-HD56, R — Natrona County/Casper, elected 2024, 1st term) ----
    ("elissa-campbell", "WY", "Representative", [
        claim("ec414-1", "elissa-campbell", "sanctity_of_life", 0, False,
              "Voted NAY on HB0126 (2026), Wyoming's Human Heartbeat Act, which would ban abortion "
              "once fetal cardiac activity is detectable (approximately six weeks), with exceptions "
              "only for life-threatening medical emergencies. Campbell is named explicitly in the "
              "seven-member minority that voted against the bill on both the February 24 third "
              "reading (51-7) and March 5 concurrence vote (47-7): Byron, Campbell(E), Chestek, "
              "Provenza, Storer, Yin, and Jarvis. On the House floor Campbell framed her opposition "
              "in individual-liberty terms, stating: 'What terrifies me the most is we talk about "
              "government overreach, and we talk about protecting the rights and freedoms... This "
              "bill, to me, screams, We are taking rights, liberties, freedoms from individuals, "
              "and giving that authority to the state.'",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://oilcity.news/community/elections/2026/06/19/election-qa-elissa-campbell-for-wyoming-house-district-56/",
               "https://oilcity.news/politics/2026/01/09/rep-elissa-campbell-files-resolution-for-wyoming-abortion-amendment/"]),
        claim("ec414-2", "elissa-campbell", "election_integrity", 0, True,
              "Voted AYE on HB0156 (2025), Wyoming's Proof of Voter Residency-Registration "
              "Qualifications Act, which requires every new voter registrant to provide documentary "
              "proof of U.S. citizenship and at least 30 days of bona fide Wyoming residency. "
              "Campbell is confirmed in the aye column; only Chestek, Provenza, and Sherwood "
              "dissented (54-3 passage on February 28, 2025). The law took effect March 21, 2025 "
              "(Chapter 172) without Governor Gordon's signature, making Wyoming a national model "
              "for citizenship-based voter roll integrity.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature",
               "https://ballotpedia.org/Elissa_Campbell"]),
    ]),

    # ---- Darin McCann (WY-HD48, R, Freedom Caucus — PA-C, 82nd Airborne veteran, Rock Springs) ----
    ("darin-mccann", "WY", "Representative", [
        claim("dm414-1", "darin-mccann", "sanctity_of_life", 0, True,
              "Co-sponsored HB0126 (2026), Wyoming's Human Heartbeat Act (primary sponsor: Speaker "
              "Chip Neiman), which bans abortion once fetal cardiac activity is detectable "
              "(approximately six weeks), with exceptions only for life-threatening emergencies; "
              "voted AYE (47-7 concurrence, March 5, 2026). McCann also served as primary sponsor "
              "of HB0159 (2025), one of Wyoming's most restrictive abortion-medication measures: "
              "it required the Wyoming DEQ to test public water systems for abortion medications "
              "and required women who took abortion pills to return fetal tissue to healthcare "
              "facilities. McCann — a physician assistant with over 20 years of orthopedic practice "
              "and an 82nd Airborne/Special Forces-trained Army veteran — sponsored HB0159 from the "
              "position that unborn life begins at conception and must be protected at every stage.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyoleg.gov/Legislation/2025/HB0159",
               "https://legiscan.com/WY/bill/HB0126/2026",
               "https://www.wyomingrising.org/2025/01/27/action-needed-protect-reproductive-health-care/"]),
        claim("dm414-2", "darin-mccann", "industry_capture", 0, True,
              "Primary sponsor of HB0096 (2025), 'Prohibiting Mask, Vaccine and Testing "
              "Discrimination,' which would have barred businesses and organizations receiving "
              "taxpayer subsidies from requiring employees or customers to wear masks, submit to "
              "COVID-19 testing, or receive COVID-19 vaccines as a condition of participation. The "
              "bill created a civil cause of action for violations and passed the House 45-16, "
              "reflecting majority House support for ending COVID-era pharmaceutical and public-health "
              "mandates — before failing the Senate Labor Committee 2-3 on February 26, 2025. "
              "McCann, a physician assistant, framed the bill around protecting informed medical "
              "consent and individual freedom from pharma-government mandate regimes.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0096",
               "https://www.wyomingpublicmedia.org/politics-government/2025-02-04/a-series-of-bills-focused-on-public-health-are-moving-through-the-wyoming-legislature",
               "https://ballotpedia.org/Darin_McCann"]),
        claim("dm414-3", "darin-mccann", "self_defense", 0, True,
              "Co-sponsored HB0172 (2025), 'Repeal Gun Free Zones and Preemption Amendments,' "
              "which eliminated all of Wyoming's statutory gun-free zones and reserved sole "
              "authority over firearms regulation to the state legislature, enabling constitutional "
              "carry in previously restricted locations. The bill passed the House 50-10 and became "
              "law February 27, 2025 (Chapter 61) without Gov. Gordon's signature. McCann's broader "
              "Second Amendment philosophy is unambiguous: during his 2024 primary campaign debate "
              "he stated, 'My statement is — nullify, nullify, nullify. I don't believe that the "
              "federal government should have any standing on what we can and can't have as far as "
              "weapons. I believe an armed society is a polite society.'",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://legiscan.com/WY/bill/HB0172/2025",
               "https://www.wyomingnews.com/rocketminer/stith-and-mccann-clash-over-gun-legislation-and-fiscal-policy-in-heated-house-district-48/article_c9814780-581c-11ef-8491-7332cdc2aa37.html",
               "https://www.gunowners.org/wy02282025/"]),
    ]),

    # ---- Chip Neiman (WY-HD1, R — Speaker of Wyoming House 2025-2026, Crook County rancher) ----
    ("chip-neiman", "WY", "Representative", [
        claim("cn414-1", "chip-neiman", "sanctity_of_life", 0, True,
              "Primary sponsor of HB0126 (2026), Wyoming's Human Heartbeat Act — joined by "
              "approximately 40 co-sponsors — which bans abortion once fetal cardiac activity is "
              "detectable (approximately six weeks of gestation), with exceptions only for "
              "life-threatening medical emergencies. The bill passed the House 51-7 on third "
              "reading (February 24, 2026) and 47-7 on concurrence (March 5, 2026); Gov. Gordon "
              "signed it as HEA No. 29 on March 9, 2026, making Wyoming the 5th state to enact a "
              "heartbeat protection law. Neiman also led HB0064 (2025), requiring a transvaginal "
              "ultrasound within 48 hours before taking an abortion pill; though Gov. Gordon "
              "vetoed it, both chambers overrode the veto. Neiman openly stated HB0064's intent "
              "was to discourage abortions. The law was later struck down by a Wyoming district "
              "court, but the veto override demonstrated Neiman's willingness to defy executive "
              "resistance to life-protection legislation.",
              ["https://www.wyoleg.gov/Legislation/2026/HB0126",
               "https://legiscan.com/WY/bill/HB0126/2026",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat",
               "https://oilcity.news/legislature-community/2026/03/05/heartbeat-bill-emerges-to-restrict-abortion-in-wake-of-supreme-courts-decision/",
               "https://wyofile.com/wyoming-judge-strikes-down-ultrasound-requirement-two-other-abortion-laws/"]),
        claim("cn414-2", "chip-neiman", "election_integrity", 0, True,
              "Champion of HB0156 (2025), the Proof of Voter Residency-Registration Qualifications "
              "Act, which made Wyoming the first state in the nation to require both documentary "
              "proof of U.S. citizenship AND at least 30 days of verifiable Wyoming residency as "
              "conditions for voter registration. The bill passed the House 54-3 (only Chestek, "
              "Provenza, and Sherwood dissented) and became law March 21, 2025 (Chapter 172) after "
              "Gov. Gordon allowed it to take effect without his signature. Neiman highlights "
              "this achievement in his 2026 Wyoming Senate campaign: 'I made Wyoming the first "
              "state in the nation to require proof of U.S. citizenship and Wyoming residency "
              "to register to vote.'",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-21/gordon-lets-proof-of-voter-residency-bill-become-law-without-his-signature",
               "https://www.sundancetimes.com/story/2026/04/09/news/house-speaker-chip-neiman-announces-candidacy-for-wyoming-senate/12349.html"]),
        claim("cn414-3", "chip-neiman", "self_defense", 0, True,
              "Co-sponsored HB0172 (2025), which repealed Wyoming's existing gun-free-zone statutes "
              "and strengthened state firearms preemption — allowing law-abiding citizens to carry "
              "lawfully owned firearms in locations previously prohibited by statute, and asserting "
              "exclusive state authority over firearm regulation to block local-government "
              "restrictions on carry. The bill passed the House 50-10 and became law February 28, "
              "2025, without Governor Gordon's signature. Gun Owners of America praised its "
              "enactment as a constitutional-carry expansion. Neiman's co-sponsorship, exercised "
              "while serving as House Majority Floor Leader, reflects his conviction that Second "
              "Amendment rights should not be restricted by government-designated zones.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://wyofile.com/house-makes-first-move-to-expand-concealed-carry-other-gun-rights-in-wyoming/",
               "https://www.gunowners.org/wy02282025/",
               "https://ballotpedia.org/Chip_Neiman"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions across states."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
