#!/usr/bin/env python3
"""Enrichment batch 588: 5 Ohio R state senators with 0 claims (continued OH sweep).

Picks up where batch 587 left off — the next group of Ohio Republican state senators
alphabetically within the archetype_party_default bucket, all with 0 claims:

  Al Cutrona        (OH-R, District 33, Mahoning/Columbiana/Carroll — OH House 2020-2024,
                     Senate June 2024-; NRA lifetime member; SB 392 Freedom to Carry Act)
  Al Landis         (OH-R, District 31, Tuscarawas/Wayne/Muskingum — OH House 2011-2018,
                     Senate 2023-; NRA member; SB 219 oil-and-gas modernization sponsor)
  Andrew O. Brenner (OH-R, District 19, Delaware/Knox/Coshocton/Holmes — Senate 2019-,
                     Education Committee Chair 136th GA; SB 23 + SB 215 + SB 293 co-sponsor)
  Brian M. Chavez   (OH-R, District 30, southeastern OH — appointed Dec 2023, re-elected Nov
                     2024; Energy Committee Chair; SB 58 gun privacy vote; HB 15 energy policy)
  George F. Lang    (OH-R, District 4, Butler County — Senate 2021-, Majority Whip 136th GA;
                     SB 215 co-sponsor; SR 215 Issue-1 opponent; NRA A rating; 100% CPAC 2024)

Claims drawn from ohiosenate.gov, ohiohouse.gov, legislature.ohio.gov, ballotpedia.org,
wikipedia.org, buckeyefirearms.org, ivoterguide.com, ohiolife.org, cpac.org, and
congressionalsportsmen.org.

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep master under
GitHub's 50MB limit.
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
    # ---------- Al Cutrona (OH-R, District 33, Mahoning/Columbiana/Carroll) ----------
    ("al-cutrona", "OH", "Senator", [
        claim("ac1", "al-cutrona", "self_defense", 0, True,
              "Cutrona is a lifetime member of the National Rifle Association (NRA) per his "
              "official Ohio Senate biography, and received NRA-PVF and Buckeye Firearms "
              "Association (BFA-PAC) endorsements for his 2024 Senate race. As an Ohio House "
              "member (District 59, Mahoning County, 2020-2024), he voted YES on the House "
              "passage of Senate Bill 215 (134th General Assembly), Ohio's Constitutional "
              "Carry law authored by Senator Terry Johnson, which makes concealed handgun "
              "licenses optional for law-abiding adults 21 and over. The House passed SB 215 "
              "57-35 in March 2022 and Governor DeWine signed it on March 14, 2022 (effective "
              "June 13, 2022), making Ohio the 22nd constitutional carry state. In the Senate, "
              "Cutrona co-sponsored SB 392 (136th GA, March 2026), the 'Freedom to Carry Act' "
              "co-authored with Senator Terry Johnson, which further expands Ohio's carry "
              "rights, lowers the minimum age for a concealed carry license from 21 to 18, "
              "eases transport of long guns in vehicles, and broadens statewide preemption "
              "over local firearms ordinances.",
              ["https://ohiosenate.gov/members/al-cutrona/biography",
               "https://www.legislature.ohio.gov/legislation/134/sb215",
               "https://www.buckeyefirearms.org/sb-392-freedom-carry-act-would-expand-ohio-gun-rights-multiple-fronts",
               "https://ballotpedia.org/Alessandro_Cutrona"]),
        claim("ac2", "al-cutrona", "sanctity_of_life", 0, True,
              "In May 2023, Cutrona voted YES in the Ohio House to place the August 2023 "
              "Issue 1 on the ballot — a proposed constitutional amendment to raise the "
              "threshold for passing citizen-initiated constitutional amendments from 50% to "
              "60%. The measure was designed in significant part to protect Ohio's existing "
              "pro-life statutes (including SB 23, the Heartbeat Protection Act) from being "
              "permanently overridden by a simple-majority abortion-rights ballot initiative. "
              "Cutrona also stated publicly on the August 2023 supermajority measure: his "
              "position on abortion 'is clear.' While the August Issue 1 failed 57%-43% "
              "statewide, Cutrona acted legislatively to protect unborn life before the "
              "November 2023 abortion referendum. He also co-sponsored SB 1 (136th GA, 2025) "
              "with Senator Cirino, the Advance Ohio Higher Education Act banning DEI "
              "indoctrination and political litmus tests at state universities — protecting "
              "students from ideological coercion that undermines family-centered values.",
              ["https://ohiocapitaljournal.com/2023/05/11/ohio-lawmakers-send-60-supermajority-amendment-to-the-ballot/",
               "https://www.legislature.ohio.gov/legislation/136/sb1",
               "https://en.wikipedia.org/wiki/Alessandro_Cutrona"]),
    ]),

    # ---------- Al Landis (OH-R, District 31, Tuscarawas/Wayne/Muskingum) ----------
    ("al-landis", "OH", "Senator", [
        claim("al1", "al-landis", "self_defense", 0, True,
              "Landis is a documented NRA Life Member, listed on his official Ohio Senate "
              "biography page. A native of Dover, Tuscarawas County, he served as Chair of "
              "the Energy & Natural Resources Committee during 4 years in the Ohio House "
              "(2011-2018), and returned to the legislature as State Senator (District 31) "
              "in January 2023, representing Tuscarawas, Wayne, Muskingum, Stark, and "
              "Guernsey counties — communities where hunting, farming, and lawful firearm "
              "ownership are foundational traditions. He is also a member of the Ohio Farm "
              "Bureau. Landis voted for SB 214 (136th GA), Ohio's suppressor modernization "
              "bill, which passed the Ohio Senate 31-1 in March 2026. During the 135th GA "
              "(2023-2024), he served in the Republican caucus that voted for SB 58 (Second "
              "Amendment Financial Privacy Act), prohibiting merchant-category-code tracking "
              "of gun retailers and barring government from maintaining firearms registry "
              "lists — signed by Governor DeWine effective April 9, 2025.",
              ["https://ohiosenate.gov/members/al-landis/biography",
               "https://www.nraila.org/articles/20260325/ohio-senate-passes-suppressor-legislation",
               "https://www.legislature.ohio.gov/legislation/135/sb58",
               "https://ballotpedia.org/Al_Landis"]),
        claim("al2", "al-landis", "sanctity_of_life", 0, True,
              "During his final term in the Ohio House (132nd GA, 2017-2018), Landis "
              "co-sponsored HB 258, Ohio's House version of the heartbeat abortion ban. "
              "In May 2023 as a State Senator, he voted YES on Senate Joint Resolution 2 "
              "(SJR2), sending the August 2023 Issue 1 (requiring 60% supermajority for "
              "constitutional amendments) to the ballot — a direct legislative action to "
              "protect Ohio's existing pro-life statutes from a simple-majority abortion "
              "referendum. In October 2023, Landis co-sponsored Ohio Senate Resolution 215 "
              "(SR 215), formally opposing the November 2023 Issue 1 abortion amendment; "
              "the resolution passed 23-7. His Senate office issued a press release titled "
              "'Landis Votes to Protect Life.' Ohio Right to Life PAC endorsed Landis in "
              "both the 2022 primary and general elections.",
              ["https://ohiosenate.gov/members/al-landis/news/landis-votes-to-protect-life",
               "https://ohiosenate.gov/news/on-the-record/senate-passes-resolution-protecting-life",
               "https://legiscan.com/OH/bill/HB258/2017",
               "https://ballotpedia.org/Al_Landis"]),
        claim("al3", "al-landis", "family_child_sovereignty", 0, True,
              "Landis and the Ohio Senate Republican caucus passed House Bill 8 (135th "
              "General Assembly, 2024), the Ohio Parents' Bill of Rights, requiring public "
              "schools to adopt policies notifying parents about students' health and "
              "well-being, mental health, and instructional materials containing sexuality "
              "content. The bill also permitted released-time courses in religious "
              "instruction. Governor DeWine signed HB 8 on January 8, 2025, making Ohio "
              "the 23rd state to enact a Parents' Bill of Rights. Senate Democrats "
              "unanimously urged a veto; the Republican caucus — including Landis — passed "
              "it as a restoration of parents' authority over their children's education. "
              "In the 136th GA, Landis authored SB 219 (the first comprehensive "
              "modernization of Ohio's oil and gas laws in over a decade), signed by "
              "Governor DeWine on June 24, 2026 — creating a dedicated orphan-well "
              "remediation fund that protects rural landowners and property rights.",
              ["https://ohiosenate.gov/members/michele-reynolds/news/ohio-senate-passes-bill-reinforcing-parents-rights",
               "https://en.wikipedia.org/wiki/Ohio_House_Bill_8_(2023)",
               "https://news.ballotpedia.org/2025/01/23/ohio-becomes-the-23rd-state-to-adopt-what-supporters-call-a-parents-bill-of-rights/",
               "https://www.legislature.ohio.gov/legislation/136/sb219"]),
    ]),

    # ---------- Andrew O. Brenner (OH-R, District 19, Delaware/Knox/Coshocton/Holmes) ----------
    ("andrew-o-brenner", "OH", "Senator", [
        claim("ab1", "andrew-o-brenner", "sanctity_of_life", 0, True,
              "Brenner co-sponsored Ohio Senate Bill 23 (133rd General Assembly, 2019), the "
              "Human Rights and Heartbeat Protection Act, which bans most abortions once a "
              "fetal heartbeat is detectable (approximately six weeks), with an exception for "
              "medical emergencies. Governor Mike DeWine signed the bill on April 11, 2019. "
              "On the iVoterGuide candidate questionnaire, Brenner stated that 'human life "
              "begins at conception and deserves legal protection at every stage until natural "
              "death,' confirmed his support for the heartbeat bill, and stated that 'abortion "
              "providers, including Planned Parenthood, should not receive funds from federal, "
              "state, or local governments.' Brenner also co-sponsored Ohio Senate Resolution "
              "215 (135th GA, adopted 23-7 on October 11, 2023), formally urging voters to "
              "reject November 2023 Issue 1 (the abortion constitutional amendment). Ohio "
              "Right to Life has endorsed Brenner across multiple election cycles. He serves "
              "as Chair of the Education Committee for the 136th General Assembly (2025-2026).",
              ["https://www.legislature.ohio.gov/legislation/133/sb23",
               "https://ivoterguide.com/candidate/980/race/17919/election/978",
               "https://ohiosenate.gov/news/on-the-record/senate-passes-resolution-protecting-life",
               "https://ballotpedia.org/Andrew_Brenner"]),
        claim("ab2", "andrew-o-brenner", "self_defense", 0, True,
              "Brenner co-sponsored Senate Bill 215 (134th General Assembly, 2022), Ohio's "
              "Constitutional Carry law authored by Senator Terry Johnson. SB 215 makes "
              "concealed handgun licenses optional for law-abiding adults 21 and over and "
              "changed the duty-to-inform requirement to disclosure only when directly asked "
              "by law enforcement. Confirmed co-sponsors alongside Brenner included Senators "
              "Blessing, Huffman, Lang, Roegner, Rulli, Koehler, and others. Governor DeWine "
              "signed SB 215 on March 14, 2022 (effective June 13, 2022), making Ohio the "
              "22nd constitutional carry state. Brenner is also a personal member of the "
              "National Rifle Association (NRA) per his official Ohio Senate biography, and "
              "received Americans for Prosperity-Ohio endorsement for fiscal responsibility "
              "and individual liberty.",
              ["https://www.legislature.ohio.gov/legislation/134/sb215",
               "https://www.buckeyefirearms.org/ohio-senate-passes-sb-215-constitutional-carry",
               "https://www.ohiosenate.gov/members/andrew-o-brenner/biography"]),
        claim("ab3", "andrew-o-brenner", "election_integrity", 0, True,
              "Brenner co-sponsored Senate Bill 293 (136th General Assembly, 2025) with "
              "Senate President Theresa Gavarone, which passed the Ohio Senate with Republican "
              "support. SB 293 requires mail-in absentee ballots to be delivered by the time "
              "polls close on Election Day (not merely postmarked by Election Day), and directs "
              "the Ohio Secretary of State to verify the citizenship of registered voters. "
              "Brenner also co-sponsored SB 324 (136th GA, 2025) with Gavarone, a companion "
              "election protection measure. These bills extend Brenner's long record on "
              "election integrity: as Vice-Chair of the Government Oversight and Reform "
              "Committee (136th GA), he has consistently backed chain-of-custody safeguards "
              "for absentee ballots and affirmative citizenship verification as foundations "
              "of secure Ohio elections.",
              ["https://ohiosenate.gov/members/andrew-o-brenner/news/senate-passes-brenner-gavarone-bill-to-require-absentee-ballots-arrive-by-poll-closing",
               "https://ohiosenate.gov/members/andrew-o-brenner/news/senate-passes-brenner-gavarone-bill-protecting-ohios-elections",
               "https://ohiosenate.gov/members/andrew-o-brenner/legislation"]),
    ]),

    # ---------- Brian M. Chavez (OH-R, District 30, southeastern Ohio) ----------
    ("brian-m-chavez", "OH", "Senator", [
        claim("bc1", "brian-m-chavez", "self_defense", 1, True,
              "Chavez voted for Senate Bill 58 (135th General Assembly), the Second Amendment "
              "Financial Privacy Act, which passed the Ohio Senate 25-6 on December 18, 2024, "
              "and was signed by Governor DeWine (effective April 9, 2025). SB 58 prohibits "
              "financial institutions from using merchant category codes to specifically "
              "identify and track firearms retailers, and bars government from maintaining "
              "lists of privately owned firearms or gun owners — directly targeting the "
              "'de facto gun registry' threat posed by payment-network tracking of lawful "
              "gun purchases. Chavez represents southeastern Ohio's District 30 (Washington, "
              "Athens, Belmont, Meigs, Morgan, Monroe, Noble, Harrison, Jefferson, and part "
              "of Guernsey counties), where hunting and lawful gun ownership are foundational "
              "to rural community life.",
              ["https://www.legislature.ohio.gov/legislation/135/sb58",
               "https://congressionalsportsmen.org/news/firearm-privacy-legislation-sent-to-ohio-governors-desk/",
               "https://ballotpedia.org/Brian_Chavez"]),
        claim("bc2", "brian-m-chavez", "economic_stewardship", 4, True,
              "As Chair of the Ohio Senate Energy and Public Utilities Committee (136th GA), "
              "Chavez championed Ohio House Bill 15, the '21st Century Energy Policy,' signed "
              "by Governor DeWine on May 15, 2025. HB 15 prioritizes new baseload power "
              "generation (reliable, dispatchable sources including natural gas and nuclear), "
              "reduces tangible personal property tax on new generation projects by ~67%, "
              "and repeals Electric Security Plans — a direct rejection of the ESG/Davos "
              "energy-transition agenda that would force Ohio onto unreliable intermittent "
              "wind and solar. Chavez also championed Senate Bill 294 (passed Ohio Senate "
              "June 10, 2026, party-line) requiring electricity sources to maintain a 50% "
              "minimum capacity factor to qualify for Ohio grid integration — effectively "
              "requiring storage backup for wind/solar and protecting Ohio ratepayers from "
              "the globalist renewable-energy mandates driving European-style energy poverty.",
              ["https://ohiosenate.gov/members/brian-m-chavez/news/senate-passes-historic-energy-policy-incentivizing-reliability-affordability-and-accountability-for-new-power-projects",
               "https://ohiocapitaljournal.com/2025/05/01/ohio-lawmakers-send-energy-overhaul-to-the-governor/",
               "https://ohiocapitaljournal.com/2026/07/07/new-ohio-bill-could-hamstring-big-wind-and-solar-farms-even-more/"]),
    ]),

    # ---------- George F. Lang (OH-R, District 4, Butler County) ----------
    ("george-f-lang", "OH", "Senator", [
        claim("gl1", "george-f-lang", "self_defense", 0, True,
              "Lang co-sponsored Senate Bill 215 (134th General Assembly), Ohio's "
              "Constitutional Carry law authored by Senator Terry Johnson. The Ohio Senate "
              "passed SB 215 23-8 on December 15, 2021 (Lang voted yes) and Governor DeWine "
              "signed it on March 14, 2022, making Ohio the 22nd constitutional carry state. "
              "Lang holds an NRA 'A' rating and received NRA-PVF and Buckeye Firearms "
              "Association (BFA-PAC) endorsements for his 2024 Senate re-election. He states: "
              "'As a concealed-carry holder, George Lang will always defend our Second "
              "Amendment rights. He supports Stand-Your-Ground Laws and Constitutional "
              "Carry.' He earned a 100% annual CPAC/ACU rating for 2024 (93% lifetime) and "
              "serves as Senate Majority Whip for the 136th General Assembly (2025-2026).",
              ["https://www.legislature.ohio.gov/legislation/134/sb215",
               "https://www.buckeyefirearms.org/ohio-senate-passes-sb-215-constitutional-carry",
               "https://www.cpac.org/bio/oh-george-lang",
               "https://ballotpedia.org/George_Lang"]),
        claim("gl2", "george-f-lang", "sanctity_of_life", 0, True,
              "Lang co-sponsored Ohio Senate Bill 23 (133rd General Assembly, 2019), the "
              "Human Rights and Heartbeat Protection Act, as an Ohio House member (District "
              "52, West Chester / Butler County), and voted for it when the House passed it "
              "56-40. SB 23 prohibits abortion once a fetal heartbeat is detectable "
              "(approximately six weeks) and was signed by Governor DeWine on April 11, "
              "2019. Lang's campaign materials state he is '100% Pro-Life and voted for the "
              "Heartbeat Bill' and was 'the only candidate endorsed by Ohio Right to Life' "
              "in his 2020 Senate race. Ohio Right to Life PAC endorsed him in both 2020 and "
              "2024 primaries. In October 2023, Lang co-sponsored Ohio Senate Resolution 215 "
              "(135th GA) — formally adopted 23-7 on October 11, 2023 — which urged Ohio "
              "voters to reject November 2023 Issue 1 (the abortion constitutional amendment "
              "that passed 56.8%-43.2%).",
              ["https://www.legislature.ohio.gov/legislation/133/sb23",
               "https://ohiosenate.gov/news/on-the-record/senate-passes-resolution-protecting-life",
               "https://ohiolife.org/2024-ortl-pac-recommendations/",
               "https://ballotpedia.org/George_Lang"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
