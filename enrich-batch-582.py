#!/usr/bin/env python3
"""Enrichment batch 582: 5 state senators with 0 claims (UT / SD / SC).

Bottom-of-alphabet bucket (archetype_party_default, 0 claims, state senators).
The archetype_curated pool is fully exhausted; these continue the reverse-alpha
sweep of archetype_party_default state senators.

Senators: Emily Buss (UT-Forward), Liz Larson (SD-D, Minority Leader),
Red Dawn Foster (SD-D, Minority Whip), Tameika Isaac Devine (SC-D),
Stephen L. Goldfinch Jr. (SC-R).

Each claim cites >=1 reliable source and reflects documented 2021-2026 positions,
votes, and public statements.
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
    # --- Emily Buss (UT, Forward Party, State Senate District 11, appt. Dec 2025) ---
    ("emily-buss", "UT", "Senator", [
        claim("eb1", "emily-buss", "election_integrity", 0, False,
              "Buss, Utah's only Forward Party state senator (appointed December 2025), "
              "stated publicly: 'I want Utah to welcome innovation in how we vote so people "
              "can choose the candidate they actually believe in. I would work to expand "
              "voting methods that give voters more choice and reduce fear around participating "
              "instead of forcing voters to choose the lesser of two evils.' The Forward Party "
              "selected her via approval voting and she champions open primaries — both aimed "
              "at expanding participation rather than the voter-ID/paper-ballot/anti-mass-"
              "mail-in election integrity framework the rubric calls for.",
              ["https://votesearch.utah.gov/cb/625988096.pdf",
               "https://eaglemountain.gov/following-forward-party-vote-state-sen-buss-outlines-priorities/",
               "https://www.kuer.org/politics-government/2025-12-16/the-forward-party-of-utah-has-a-new-senator-can-they-hold-on-in-2026"]),
        claim("eb2", "emily-buss", "family_child_sovereignty", 0, False,
              "Buss's primary stated education policy is increasing per-pupil public school "
              "funding — Utah ranks second-lowest nationally in per-pupil spending — and "
              "raising teacher pay. She has proposed a grant program for high-growth school "
              "districts and sponsored a bill expanding school-based mental health services. "
              "No documented support for parental rights frameworks, school choice, charter "
              "or homeschool access, or parental notification requirements appears in her "
              "record. The Forward Party has no school-choice or parental-sovereignty plank. "
              "Her approach centers on government investment in public schools rather than "
              "parental direction of educational alternatives.",
              ["https://utahnewsdispatch.com/2026/01/20/meet-new-utah-lawmakers-2026-legislature/",
               "https://eaglemountain.gov/following-forward-party-vote-state-sen-buss-outlines-priorities/",
               "https://senate.utah.gov/sen/BUSSEM/"]),
    ]),

    # --- Liz Larson (SD-D, District 10, Senate Minority Leader since Jan 2025) ---
    ("liz-larson", "SD", "Senator", [
        claim("ll1", "liz-larson", "sanctity_of_life", 0, False,
              "Larson was the sole dissenting vote in the South Dakota Senate State Affairs "
              "Committee against HB 1274 (2026), which made it a Class 6 felony to dispense, "
              "distribute, sell, or advertise abortion pills. She stated: 'I feel like our "
              "medical community has spoken. I feel like this just adds uncertainty into very "
              "difficult scenarios,' and publicly said mifepristone 'is used in a variety of "
              "medical situations, including miscarriage and abortion, that are really necessary "
              "for women.' The bill was signed into law March 20, 2026. As SD Senate Minority "
              "Leader — the first woman to lead a Democratic caucus in the SD Legislature — "
              "she has consistently opposed the state's near-total abortion ban, directly "
              "contradicting the rubric's life-at-conception standard.",
              ["https://southdakotasearchlight.com/2026/02/20/ban-on-advertising-and-dispensing-abortion-pills-advances-in-south-dakota-legislature/",
               "https://www.keloland.com/keloland-com-original/senate-panel-advances-abortion-pill-crackdown/",
               "https://southdakotasearchlight.com/2026/03/20/new-anti-abortion-laws-clarify-definition-criminalize-pills-require-prenatal-videos-in-schools/"]),
        claim("ll2", "liz-larson", "self_defense", 0, False,
              "Larson was one of only two senators to vote against SB 100 (2025), allowing "
              "enhanced concealed-carry permit holders to carry on public university and "
              "technical college campuses. She voted No in both the State Affairs Committee "
              "(7-2) and on the Senate floor (33-2). The bill was signed by Governor Rhoden "
              "March 31, 2025. She also voted No on HB 1259 (2025), the transgender bathroom "
              "bill (27-6), and explicitly opposed the bill on the floor. Her consistent No "
              "votes on Second Amendment expansion legislation — including campus carry — "
              "place her in opposition to the rubric's constitutional-carry standard.",
              ["https://southdakotasearchlight.com/2025/02/12/bill-to-allow-concealed-pistols-on-college-campuses-clears-state-senate/",
               "https://www.nraila.org/articles/20250324/south-dakota-governor-rhoden-signs-pro-gun-bills-into-law",
               "https://legiscan.com/SD/bill/SB100/2025"]),
        claim("ll3", "liz-larson", "election_integrity", 0, False,
              "Larson was the only member of the South Dakota Senate State Affairs Committee "
              "to vote against SB 30 (2026), which allows any registered voter to challenge "
              "another voter's citizenship status. She stated: 'To have those issues of people "
              "challenging citizenship for other people, it comes with so much baggage and "
              "especially now with a lot of the violence that\'s going on in Minnesota. I "
              "think this is too far.' She questioned what evidence suffices to challenge "
              "a vote and whether the state should give 'everyday citizens that authority.' "
              "The law was signed by Governor Rhoden and took effect July 1, 2026. Her lone "
              "election-integrity-adjacent sponsored bill (SB 164, 2025) focused on AI "
              "deepfake labeling — not voter-ID or ballot security.",
              ["https://southdakotasearchlight.com/2026/03/08/new-south-dakota-law-allows-voters-to-challenge-other-voters-citizenship/",
               "https://southdakotasearchlight.com/2026/01/28/legislation-headed-to-sd-senate-would-authorize-challenges-to-voters-citizenship/",
               "https://www.kotatv.com/2026/03/10/new-south-dakota-law-allows-voters-challenge-other-voters-citizenship/"]),
    ]),

    # --- Red Dawn Foster (SD-D, District 27, Pine Ridge/Oglala Lakota, Minority Whip) ---
    ("red-dawn-foster", "SD", "Senator", [
        claim("rdf1", "red-dawn-foster", "biblical_marriage", 2, False,
              "Foster sponsored SB 166 (2021), the first bill in any U.S. state legislature "
              "to propose protections specifically for Native American Two-Spirit individuals, "
              "adding LGBTQ and gender-identity protections to South Dakota's hate crime law. "
              "She stated South Dakota's hate crime law is 'woefully deficient.' The Senate "
              "Judiciary Committee passed it unanimously, but the full Senate rejected it "
              "27-8. She also voted NO on HB 1080 (2023), South Dakota's 'Help Not Harm' "
              "Act banning puberty blockers, hormones, and gender-transition surgery for "
              "minors (passed 30-4); she is confirmed in the named roll call as one of the "
              "four No votes. Both actions directly oppose the rubric's standard of "
              "rejecting transgender ideology.",
              ["https://nativenewsonline.net/currents/bill-protecting-native-american-two-spirit-individuals-fails-in-south-dakota-state-senate",
               "https://www.dakotanewsnow.com/2023/02/09/live-1-south-dakota-senate-discuss-bill-medical-parameters-trans-youth/",
               "https://www.metroweekly.com/2023/02/south-dakota-gop-bans-gender-affirming-care-for-trans-youth/"]),
        claim("rdf2", "red-dawn-foster", "christian_liberty", 0, True,
              "Foster co-sponsored SB 113 (2026), a bill increasing criminal penalties for "
              "any person who prevents or attempts to prevent another from practicing their "
              "religion. The bill passed the South Dakota Senate 30-4 and the House 48-18 "
              "and was signed by Governor Rhoden on March 10, 2026. Co-sponsoring bipartisan "
              "legislation to criminalize interference with religious practice is directly "
              "aligned with the rubric's religious free exercise standard.",
              ["https://sdlegislature.gov/Legislators/Profile/4359/Detail",
               "https://ballotpedia.org/Red_Dawn_Foster",
               "https://southdakotasearchlight.com/2026/01/29/lawmakers-ask-south-dakotans-to-seek-the-lord-most-high/"]),
    ]),

    # --- Tameika Isaac Devine (SC-D, District 19, Richland County/Columbia, since Jan 2024) ---
    ("tameika-isaac-devine", "SC", "Senator", [
        claim("tid1", "tameika-isaac-devine", "self_defense", 0, False,
              "Devine voted against H.3594, South Carolina's Constitutional Carry/Second "
              "Amendment Preservation Act, which passed the Senate 28-15 on February 1, 2024 "
              "(she took office January 8, 2024). During floor debate she stated: 'We\'re "
              "going to have untrained individuals including 18-year-olds walking around our "
              "streets with guns and the law enforcement really has no ability to determine "
              "who is lawfully carrying and who is not.' She holds the Moms Demand Action "
              "'Gun Sense Candidate' designation, was endorsed by Everytown for Gun Safety "
              "(July 2024), and sponsored S.141 (2025-2026) requiring firearm owners to carry "
              "liability insurance — directly opposing the rubric's constitutional-carry "
              "standard.",
              ["https://www.postandcourier.com/politics/south-carolina-senate-permitless-constitutional-carry/article_e5d09e26-c141-11ee-865e-43b91e5e3d2c.html",
               "https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/",
               "https://www.everytown.org/press/everytown-for-gun-safety-endorses-latest-round-of-moms-demand-action-volunteers-running-for-office-3/"]),
        claim("tid2", "tameika-isaac-devine", "election_integrity", 0, False,
              "Devine was one of only three senators to vote No on SJR 1126 (April 3, 2024), "
              "a South Carolina constitutional amendment stating only U.S. citizens may vote "
              "(passed 40-3). SC Daily Gazette confirmed she was among the three No votes: "
              "'Matthews, Mia McLeod, I-Columbia; and Tameika Issac Devine, D-Columbia.' "
              "On her iVoterGuide questionnaire she stated: 'People should be able to vote "
              "without photo identification.' She also actively opposed the 2026 Trump-backed "
              "congressional redistricting gerrymander, hosting a town hall and offering "
              "hundreds of delaying amendments — a voter-access expansion orientation directly "
              "opposing the rubric's voter-ID/election-integrity framework.",
              ["https://scdailygazette.com/2024/04/03/republicans-call-for-1-word-voting-change-to-sc-constitution-democrats-says-theres-zero-need/",
               "https://ivoterguide.com/candidate/77578/race/19294/election/1074",
               "https://ballotpedia.org/South_Carolina_Citizenship_Requirement_for_Voting_Amendment_(2024)"]),
        claim("tid3", "tameika-isaac-devine", "christian_liberty", 0, False,
              "Devine stated on her official iVoterGuide candidate questionnaire (2024 SC "
              "Senate race): 'Individuals and businesses should be required to provide "
              "services even if it would violate their moral and/or religious beliefs.' This "
              "is a direct rejection of religious-conscience exemptions from public- "
              "accommodations requirements — the core of the rubric's religious free-exercise "
              "standard. She reinforced this orientation when she publicly opposed the state "
              "legislature's coercive repeal of Columbia's conversion therapy ban in June "
              "2025: 'I urge you to please stand strong and not cave to the games being "
              "played by those who do not live in Columbia.'",
              ["https://ivoterguide.com/candidate/77578/race/19294/election/1074",
               "https://scdailygazette.com/2025/06/17/facing-loss-of-millions-in-state-aid-columbia-council-votes-to-repeal-conversion-therapy-ban/",
               "https://www.southcarolinapublicradio.org/sc-news/2025-06-24/columbia-city-council-repeals-only-conversion-therapy-ban-in-sc"]),
    ]),

    # --- Stephen L. Goldfinch Jr. (SC-R, District 34, Georgetown/Horry counties) ---
    ("stephen-l-goldfinch", "SC", "Senator", [
        claim("slg1", "stephen-l-goldfinch", "sanctity_of_life", 0, True,
              "Goldfinch voted for S.474, South Carolina's Fetal Heartbeat and Protection "
              "from Abortion Act (2023), banning abortion after a fetal heartbeat is detected "
              "(~6 weeks) with exceptions for rape, incest, fatal fetal anomaly, and the "
              "mother's life. The bill passed 27-19 on May 23, 2023 and was signed as Act "
              "No. 70. His iVoterGuide questionnaire (2026) confirmed: 'Human life deserves "
              "legal protection from conception until natural death.' He has stated publicly: "
              "'I am unapologetically pro-life. I\'ve been proudly pro-life my entire public "
              "career' and committed to 'fight to protect pro-life laws in court' as "
              "Attorney General — fully aligned with the rubric's life-at-conception standard.",
              ["https://legiscan.com/SC/rollcall/S0474/id/1247216",
               "https://www.cnn.com/2023/05/23/politics/south-carolina-senate-abortion-ban-bill/index.html",
               "https://ivoterguide.com/candidate/25095/race/27679/election/1421"]),
        claim("slg2", "stephen-l-goldfinch", "family_child_sovereignty", 0, True,
              "Goldfinch co-sponsored S.39 (2023-2024), South Carolina's Education Scholarship "
              "Trust Fund Act (Act 8 of 2023), establishing ESAs providing up to $6,000 per "
              "year for parents to use at private schools; the bill passed the Senate 28-15 "
              "on January 31, 2023 and was signed by Gov. McMaster May 5, 2023. The Institute "
              "for Legislative Analysis awarded him 100% in the Education category. He has "
              "stated: 'Government should recognize and support the fundamental right and "
              "essential duty of parents to direct their child\'s health and educational "
              "well-being' and supports an 'all of the above approach to school choice' — "
              "fully aligned with the rubric's family and child sovereignty standard.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/39.htm",
               "https://palmettopromise.org/details-of-south-carolinas-new-education-scholarship-account-program-act-8-of-2023/",
               "https://analysis.limitedgov.org/lawmakers/stephen-goldfinch-r-sc-sen-34"]),
        claim("slg3", "stephen-l-goldfinch", "election_integrity", 0, True,
              "Goldfinch co-sponsored SJR 1126 (2024), a South Carolina constitutional "
              "amendment explicitly stating only U.S. citizens may vote in state elections. "
              "The amendment passed the Senate 40-3, the House 105-0, and was ratified by "
              "SC voters in November 2024. He also co-sponsored S305 (2025-2026), adding "
              "party affiliation to voter registration and closing SC's open primary system. "
              "Both measures align with the rubric's election integrity standard.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/1126.htm",
               "https://ballotpedia.org/South_Carolina_Citizenship_Requirement_for_Voting_Amendment_(2024)",
               "https://www.scpolicycouncil.org/looking_ahead_constitutional_amendment_heads_to_november_ballot"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug collisions across states."""
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
