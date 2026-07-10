#!/usr/bin/env python3
"""Enrichment batch 620: hand-curated claims for 5 VT R state representatives.

Continuing the archetype_party_default VT R state-rep bucket (Z→A sort).
Previous batch (619) covered: Kenneth Goslant, Kevin C. Winter, Kumulia Long,
Ken Wells, Joshua Dobrovich.

Targets (5 R):
  Joseph Parsons    (Orange-Caledonia — Newbury/Groton/Topsham; flooring trade; in office since Jan 2021)
  John Kascenska    (Essex-Caledonia — East Burke; PhD forestry; Appropriations Cmte; in office Jan 2025)
  Joe Luneau        (Franklin-3 — St. Albans City; car dealerships; Corrections Cmte; in office Jan 2025)
  Jim Casey         (Addison-Rutland-1 — Hubbardton; building contractor 35 yrs; in office Jan 2025)
  James Gregoire    (Franklin-6 — Fairfield/Bakersfield/Fletcher; convenience store; in office Jan 2019)

Tenure notes:
  - Joseph Parsons in office since January 6, 2021; eligible for all 2022-23 key votes.
  - James Gregoire in office since January 9, 2019; eligible for all 2022-23 key votes.
  - John Kascenska first appointed March 7, 2022 (lost Aug 2022 primary); re-elected Nov 2024,
    took office Jan 8, 2025. NOT eligible for Proposal 5 (Feb 2022, before appointment) or
    H.230/S.5 (2023, out of office). WAS present for H.715 veto override (May 10, 2022).
  - Joe Luneau and Jim Casey both took office January 8, 2025 — not eligible for any
    2022-2023 votes.

NOTE: writes scorecard.json MINIFIED to keep the master under
GitHub's 50MB warning.
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
    # ---------- Joseph Parsons (VT-R, State Representative, Orange-Caledonia; 3rd term) ----------
    # Newbury, Groton, and Topsham (Orange and Caledonia counties). In office since January 6, 2021.
    # Flooring trade at Valley Floors, Bradford; Newbury Select Board 2019-2020.
    ("joseph-parsons", "VT", "Representative", [
        claim("jp1", "joseph-parsons", "sanctity_of_life", 0, True,
              "Voted NO on Proposal 5 — Vermont's constitutional amendment enshrining "
              "unlimited abortion rights with no gestational limit — in the February 8, "
              "2022 House floor vote (107-41). The Ethan Allen Institute documented "
              "Parsons' NO vote on the Reproductive Liberty Amendment at ethanallen.org/JParsons. "
              "Parsons was among the 41 representatives (40 of 41 being Republicans) who "
              "opposed the amendment — which was subsequently ratified by Vermont voters in "
              "November 2022 as Article 22. Vermont Right to Life Committee published full "
              "House roll-call documentation of all votes on Proposal 5 / Article 22. "
              "His Orange-Caledonia district covering Newbury, Groton, and Topsham includes "
              "rural farming and homesteading families, and Parsons — who works in the flooring "
              "trade at Valley Floors in Bradford and lives a homesteading lifestyle with his "
              "wife and children — has maintained a consistent pro-life posture throughout his "
              "tenure since January 2021. Vermont Conservation Voters scored him 0% in 2026 "
              "(10% lifetime), consistent with his documented opposition to the progressive "
              "supermajority's social agenda.",
              ["https://www.ethanallen.org/JParsons",
               "https://www.vrlc.net/house-and-senate-roll-call-votes-for-proposal-5-article-22/",
               "https://vtdigger.org/2022/02/08/vermont-house-approves-prop-5-sending-reproductive-rights-question-to-voters/",
               "https://ballotpedia.org/Vermont_Proposal_5,_Right_to_Personal_Reproductive_Autonomy_Amendment_(2022)"],
              kind="record"),

        claim("jp2", "joseph-parsons", "self_defense", 1, True,
              "Voted NO on S.30 (January 27, 2022) — Vermont's bill adding 27 days to the "
              "allowable delay for firearm background checks, effectively creating a "
              "27-business-day waiting period that critics argued would prevent law-abiding "
              "citizens from completing lawful firearm transfers. The bill passed the House "
              "97-49. The Ethan Allen Institute documented Parsons' NO vote, noting he cited "
              "'constitutional protections for firearm rights' in opposing the extended "
              "background check delay. This vote was one of several gun-restriction bills "
              "passed by Vermont's Democratic supermajority in 2022-2023 that Parsons "
              "opposed. In May 2023 the House also passed H.230 — creating a 72-hour "
              "waiting period, expanded red-flag law eligibility, and mandatory safe-storage "
              "requirements — in an overall 106-34 vote that broke along party lines. "
              "Vermont Conservation Voters scored Parsons 0% in both the 2025-2026 session "
              "and 0% in their annual scoring for gun-safety votes included in the "
              "environmental/social scorecard, and his 10% lifetime score spans five years "
              "of consistent opposition to the progressive legislative agenda across guns, "
              "energy, and social issues.",
              ["https://www.ethanallen.org/JParsons",
               "https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/",
               "https://vtdigger.org/2023/05/19/vermont-democrats-pushed-through-major-firearms-legislation-this-year-will-it-hold-up-in-court/",
               "https://vermontconservationvoters.com/legislators/joseph-parsons/"],
              kind="record"),

        claim("jp3", "joseph-parsons", "refuse_state_overreach", 0, True,
              "Voted to sustain Governor Scott's veto of H.715 (May 10, 2022) — the first "
              "Vermont Clean Heat Standard bill, which would have required home-heating fuel "
              "dealers in Newbury, Groton, and Topsham to accumulate state-mandated carbon "
              "credits at substantial projected costs to households. The veto override failed "
              "99-51, needing 100 votes; Parsons' NO vote on the override was documented by "
              "the Ethan Allen Institute, which noted that those voting NO 'believe the CHS "
              "would lead to extreme hardship for the 200,000+ fossil fuel heating Vermont "
              "households.' When Democrats passed S.5 (the revised Affordable Heat Act) in "
              "2023 and overrode another Scott veto, Parsons continued his opposition — the "
              "only Republican to cross over was Rep. Chris Taylor, leaving Parsons among "
              "the 41 Republicans who voted NO. In January 2025 Parsons co-sponsored H.16, "
              "the comprehensive repeal of the Affordable Heat Act, which BillTrack50 "
              "confirms lists him among the sponsors. Vermont's Clean Heat Standard was "
              "declared effectively dead in June 2025, after the Public Utilities Commission "
              "found it 'not well suited to Vermont.' Parsons' three-session record of "
              "opposing the Clean Heat Standard — from H.715 (2022) through S.5 (2023) to "
              "H.16 co-sponsorship (2025) — is one of the most consistent anti-mandate "
              "records in the Orange County delegation.",
              ["https://www.ethanallen.org/JParsons",
               "https://www.ethanallen.org/h715_4_2022",
               "https://legislature.vermont.gov/bill/status/2026/H.16",
               "https://www.billtrack50.com/billdetail/1768264",
               "https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/"],
              kind="record"),
    ]),

    # ---------- John Kascenska (VT-R, State Representative, Essex-Caledonia; 2nd stint, in office Jan 2025) ----------
    # East Burke (Essex-Caledonia). Appointed March 7, 2022; lost Aug 2022 primary; re-elected Nov 2024.
    # PhD forestry NC State; MS education Virginia Tech; mountain guide; former academic dean Lyndon State.
    # House Appropriations Committee; Joint Carbon Emissions Reduction Committee; VCV 2026: 0%, lifetime: 10%.
    ("john-kascenska", "VT", "Representative", [
        claim("jk1", "john-kascenska", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (January 2025) — the bill to formally repeal Vermont's "
              "Affordable Heat Act (Act 18/S.5, the Clean Heat Standard) — a state energy "
              "mandate that would have required home-heating fuel dealers serving Kascenska's "
              "rural Essex-Caledonia constituents in East Burke and the Northeast Kingdom to "
              "accumulate government-mandated carbon-reduction credits at projected household "
              "costs of hundreds to thousands of dollars annually. The Vermont Daily Chronicle "
              "and VTDigger confirmed in June 2025 that Vermont's Clean Heat Standard was "
              "effectively dead after the Public Utilities Commission concluded it was 'not "
              "well suited to Vermont' and that state emissions goals would be 'best achieved "
              "by building upon existing programs, rather than overlaying a new and complex "
              "regulatory structure.' Kascenska — who holds a PhD in Forestry from NC State "
              "University and an MS in Education from Virginia Tech, and has built a career "
              "as a wilderness guide and avalanche instructor serving outdoor recreation "
              "communities in the Northeast Kingdom — brings rare scientific depth to the "
              "state energy debate. He serves on the Joint Carbon Emissions Reduction "
              "Committee (2025-26) while maintaining a 0% Vermont Conservation Voters score, "
              "reflecting a market-oriented rather than mandate-based approach to environmental "
              "policy.",
              ["https://legislature.vermont.gov/bill/status/2026/H.16",
               "https://www.billtrack50.com/billdetail/1768264",
               "https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/",
               "https://ballotpedia.org/John_Kascenska"],
              kind="record"),

        claim("jk2", "john-kascenska", "economic_stewardship", 2, True,
              "Serves on the Vermont House Appropriations Committee in the 2025-26 session — "
              "the panel that controls the state's multi-billion-dollar biennial budget — "
              "bringing a private-sector and small-business lens to state fiscal decisions. "
              "As founder and owner of Kingdom Adventures Mountain Guides, LLC (East Burke), "
              "a licensed guide service and avalanche certification program, and a veteran of "
              "32 years in higher education — including 25 years in the Vermont State College "
              "System as faculty and associate academic dean at Lyndon State College — "
              "Kascenska applies both entrepreneurial and institutional budget experience to "
              "state spending decisions. His Vermont Conservation Voters score of 0% in the "
              "2025-26 session (10% lifetime across two stints) reflects consistent votes "
              "opposing costly state environmental mandates that would expand the regulatory "
              "burden on Northeast Kingdom businesses and households. The Vermont Chamber of "
              "Commerce confirmed his Appropriations Committee assignment following the "
              "January 2025 organizational session, where expanded Republican membership "
              "gave the minority meaningful influence on fiscal priorities.",
              ["https://governor.vermont.gov/press-release/governor-phil-scott-appoints-john-kascenska-vermont-house-representatives",
               "https://ballotpedia.org/John_Kascenska",
               "https://vermontconservationvoters.com/legislators/john-kascenska/",
               "https://www.vtchamber.com/vermont-house-senate-leadership-2025/"],
              kind="record"),
    ]),

    # ---------- Joe Luneau (VT-R, State Representative, Franklin-3; first elected Nov 2024) ----------
    # St. Albans City (Franklin County). In office since January 8, 2025.
    # BA History Boston College; third-generation family car dealerships; former city councilor 2009-2013;
    # President St. Albans Museum; Vice Chair St. Albans Board of Civil Authority.
    # House Committee on Corrections and Institutions; VCV 2026: 0%, lifetime: 0%.
    ("joe-luneau", "VT", "Representative", [
        claim("jl1", "joe-luneau", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (January 2025) — the bill to repeal Vermont's Affordable "
              "Heat Act / Clean Heat Standard — and later spoke forcefully against what he "
              "called 'Clean Heat Standard 2.0' on the House floor in March 2026. In that "
              "floor statement, published by the Vermont Daily Chronicle, Luneau stated: "
              "'Vermonters said no to Clean Heat [Standard] and the supermajority ignored "
              "them. Now with the demise of the 2023 Unaffordable Heat Act, we see the "
              "majority try to revive it and expand it to transportation fuels. This is not "
              "what Vermonters can afford or need, and it's a back door to the implementation "
              "of financial disaster.' Vermont's Clean Heat Standard was declared dead in "
              "June 2025 after the PUC found it 'not well suited to Vermont.' Luneau's "
              "St. Albans City constituents — urban residents of Franklin County in a city "
              "that relies heavily on home heating fuel through long winters — bore direct "
              "exposure to the cost burdens the mandate would have imposed. Vermont "
              "Conservation Voters scored Luneau 0% in the 2025-2026 session (0% lifetime), "
              "consistent with his documented pattern of opposing state energy mandates from "
              "his first day in office.",
              ["https://legislature.vermont.gov/bill/status/2026/H.16",
               "https://www.billtrack50.com/billdetail/1768264",
               "https://vermontdailychronicle.com/roper-house-democrats-vote-for-clean-heat-standard-2-0/",
               "https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/"],
              kind="record"),

        claim("jl2", "joe-luneau", "economic_stewardship", 2, True,
              "Ran his 2024 campaign — defeating the Democratic incumbent and House Government "
              "Operations Committee Chair Mike McCarthy 52.5% to 44.4% — explicitly on "
              "lowering property taxes and reversing the 'excessive taxes and financial "
              "burdens on Vermonters' created by Vermont's Democratic supermajority. In his "
              "St. Albans Messenger Q&A, Luneau stated that 'high property taxes are making "
              "life unaffordable for Vermonters' and pledged to curtail spending 'with "
              "reasonable solutions.' As a third-generation owner of family car dealerships "
              "in St. Albans — and a former city councilor (2009-2013), board of civil "
              "authority chair, and museum president who has managed civic budgets — Luneau "
              "brings private-sector cost-benefit discipline to a legislature that passed "
              "major property tax increases, DMV fee hikes, the Clean Heat Standard, and the "
              "Global Warming Solutions Act during the Democratic supermajority era. His 2024 "
              "win was part of a Republican wave that dismantled Vermont's Democratic "
              "legislative supermajority, with affordability cited by Vermont Public as the "
              "primary driver of voter discontent that fueled Republican gains.",
              ["https://www.samessenger.com/elections/race-for-franklin-3-q-a-with-st-albans-city-candidate-joe-luneau/article_11352cb0-81a6-11ef-91f1-0f6da6d4fb0b.html",
               "https://vtdigger.org/2024/11/05/vermont-gop-knocks-off-two-democratic-house-chairs/",
               "https://www.vermontpublic.org/local-news/2024-11-06/those-republican-gains-in-the-vermont-house-and-senate-heres-where-they-came-from",
               "https://ballotpedia.org/Joe_Luneau"],
              kind="statement"),

        claim("jl3", "joe-luneau", "public_justice", 0, True,
              "Ran his 2024 campaign in St. Albans City on a public safety platform focused "
              "on drug enforcement and accountability, stating in his St. Albans Messenger "
              "Q&A that 'the community is tired of seeing open drug use during the day, and "
              "reform is needed to hold those arrested accountable.' This enforcement-first "
              "approach directly contrasted with Vermont's progressive majority, which had "
              "passed decriminalization legislation and opposed law-enforcement tools over "
              "the prior decade. Luneau now serves on the House Committee on Corrections and "
              "Institutions (2025-26) — the panel that oversees the Department of Corrections, "
              "criminal sentencing, and state prison operations — bringing his public-safety "
              "agenda into direct legislative application. In committee in 2025-26 Luneau "
              "also raised accountability concerns about commissary pricing disparities at "
              "state correctional facilities and transparency in federal detainee processing, "
              "demonstrating a consistent focus on institutional accountability and the rule "
              "of law across his committee work. Vermont Conservation Voters scored him 0% "
              "in 2025-2026, consistent with his opposition to progressive criminal-justice "
              "reform legislation.",
              ["https://www.samessenger.com/elections/race-for-franklin-3-q-a-with-st-albans-city-candidate-joe-luneau/article_11352cb0-81a6-11ef-91f1-0f6da6d4fb0b.html",
               "https://vtdigger.org/profile/joe-luneau/",
               "https://legislature.vermont.gov/committee/detail/2026/17"],
              kind="statement"),
    ]),

    # ---------- Jim Casey (VT-R, State Representative, Addison-Rutland-1; first elected Nov 2024) ----------
    # Hubbardton (Rutland County; district covers Shoreham, Orwell, Whiting, Sudbury, Hubbardton).
    # In office since January 8, 2025. Building contractor 35 years; Hubbardton Select Board since 2013.
    # House Committee on Transportation; Governor's Snowmobile Council.
    ("jim-casey", "VT", "Representative", [
        claim("jc1", "jim-casey", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (January 2025) — the bill to repeal Vermont's Affordable "
              "Heat Act / Clean Heat Standard — joining a Republican-led coalition that "
              "sought to undo the state energy mandate imposing carbon-credit compliance "
              "costs on home-heating fuel dealers serving the rural Addison-Rutland "
              "communities of Shoreham, Orwell, Whiting, Sudbury, and Hubbardton. Vermont "
              "Republicans, led by Rep. Jim Harrison, introduced H.16 on the first day of "
              "the 2025 session; Casey signed on as a co-sponsor, joining dozens of "
              "Republican colleagues in declaring repeal a first-order priority. Vermont's "
              "Clean Heat Standard was declared effectively dead by June 2025, after the "
              "Public Utilities Commission found it 'not well suited to Vermont' and endorsed "
              "simpler program-based approaches instead. VTDigger noted in July 2026 that "
              "'a bolstered bloc of Vermont Republicans see bills repealed this year as a "
              "win' — citing the Clean Heat Standard's demise as the signature achievement "
              "of the expanded Republican caucus that Casey joined after flipping a "
              "Democratic-held seat in November 2024. Casey ran unopposed in the general "
              "election, becoming one of the few House members in the state to win without "
              "a major-party opponent, and brings to Montpelier 35 years of experience as "
              "a building contractor in Rutland County — where home-heating fuel costs "
              "directly affect construction costs and client affordability.",
              ["https://legislature.vermont.gov/bill/status/2026/H.16",
               "https://www.billtrack50.com/billdetail/1768264",
               "https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/",
               "https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"],
              kind="record"),

        claim("jc2", "jim-casey", "economic_stewardship", 2, True,
              "Brings over a decade of municipal fiscal governance to the Vermont House as a "
              "member of the Hubbardton Select Board since 2013 — an eleven-year record of "
              "town-level budget management and public-resource stewardship for one of "
              "Vermont's smallest rural communities. As Rutland Herald reported, Casey is a "
              "lifelong Rutland County resident and building contractor of 35 years whose "
              "private-sector career requires direct engagement with Vermont's regulatory "
              "and tax environment, including Act 250 development permitting, property tax "
              "assessment, and state construction codes. He serves on the House Committee "
              "on Transportation (2025-26), overseeing Vermont's transportation budget and "
              "infrastructure investment priorities in a rural district where road quality "
              "and fuel costs are directly tied to the economic health of farming, logging, "
              "and small-business communities in Shoreham, Orwell, Whiting, Sudbury, and "
              "Hubbardton. Casey joined the 2025-26 Republican caucus focused on reversing "
              "years of Democratic supermajority spending that critics argued had made "
              "Vermont among the nation's most expensive states for working families — "
              "a message voters in Addison-Rutland-1 endorsed by electing him to flip "
              "the seat from Democrat Joseph Andriano.",
              ["https://www.rutlandherald.com/news/local/three-newcomers-seek-house-seats-in-unopposed-rutland-county-races/article_564eec76-8bcb-11ef-9519-fb25304063c8.html",
               "https://ballotpedia.org/Jim_Casey",
               "https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/",
               "https://vtdigger.org/2024/09/05/this-election-season-7-first-time-house-candidates-face-no-opposition/"],
              kind="record"),
    ]),

    # ---------- James Gregoire (VT-R, State Representative, Franklin-6; in office since Jan 2019) ----------
    # Fairfield, Bakersfield, Fletcher (Franklin County). First elected 2018.
    # US Army 1992-1997; VT National Guard 1997-2005. Convenience store owner.
    # Town of Fairfield Lister 2003-2023; Planning/Zoning 9 years.
    # Vice Chair, House Committee on Corrections and Institutions (2025-26).
    # VCV 2026: 29%, lifetime: 31%.
    ("james-gregoire", "VT", "Representative", [
        claim("jg1", "james-gregoire", "sanctity_of_life", 0, True,
              "Voted NO on Proposal 5 — Vermont's constitutional amendment enshrining "
              "unlimited abortion rights with no gestational limit — in the February 8, "
              "2022 House floor vote (107-41). Multiple sources confirmed Gregoire's NO vote "
              "on the Reproductive Liberty Amendment: VTDigger's November 2022 election "
              "coverage noted that he 'voted against Proposal 5,' consistent with his "
              "representation of Fairfield, Bakersfield, and Fletcher — rural Franklin County "
              "communities where he has served as town lister since 2003 and on planning "
              "and zoning commissions for nine years. Gregoire has represented the Franklin-6 "
              "district since January 9, 2019, as a convenience store owner and veteran who "
              "served in the U.S. Army from 1992 to 1997 and the Vermont National Guard from "
              "1997 to 2005. Vermont Right to Life Committee published the full House "
              "roll-call documentation. The amendment passed the House 107-41 and was "
              "ratified by Vermont voters in November 2022 as Article 22. Gregoire was "
              "among the 41 representatives — 40 of 41 being Republicans — who voted to "
              "preserve Vermont's existing statutory framework rather than embed unlimited "
              "abortion rights in the state constitution.",
              ["https://vtdigger.org/2022/10/31/in-a-competitive-franklin-county-house-race-a-statehouse-advocate-challenges-a-two-term-incumbent/",
               "https://www.vrlc.net/house-and-senate-roll-call-votes-for-proposal-5-article-22/",
               "https://vtdigger.org/2022/02/08/vermont-house-approves-prop-5-sending-reproductive-rights-question-to-voters/",
               "https://ballotpedia.org/James_Gregoire"],
              kind="record"),

        claim("jg2", "james-gregoire", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (January 2025) — the bill to formally repeal Vermont's "
              "Affordable Heat Act (Act 18/S.5, the Clean Heat Standard) — bringing his "
              "Franklin-6 perspective on energy costs for rural families in Fairfield, "
              "Bakersfield, and Fletcher who rely heavily on home heating oil through "
              "Vermont's long winters. BillTrack50 and the Vermont Legislature bill status "
              "page confirm Gregoire among the co-sponsors on H.16. Vermont's Clean Heat "
              "Standard was declared dead in June 2025 after the Public Utilities Commission "
              "found it 'not well suited to Vermont.' Gregoire's H.16 co-sponsorship "
              "reflects a multi-session pattern of opposing state energy mandates: in the "
              "2023 session, Vermont Republicans were 'universally and unanimously opposed' "
              "to S.5 (the Affordable Heat Act), with only one Republican (Rep. Chris "
              "Taylor) crossing over to support the veto override — making Gregoire's "
              "sustained opposition to the Clean Heat Standard among the most consistent "
              "positions in his seven-year legislative record. As Vice Chair of the House "
              "Committee on Corrections and Institutions (2025-26), Gregoire brings a "
              "pragmatic, community-first orientation to governance that has included "
              "opposing state regulatory expansion that disproportionately burdens rural "
              "Franklin County households on fixed incomes.",
              ["https://legislature.vermont.gov/bill/status/2026/H.16",
               "https://www.billtrack50.com/billdetail/1768264",
               "https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/",
               "https://vtdigger.org/2023/05/11/clean-heat-bill-clears-final-hurdle-as-house-overrides-phil-scotts-veto/"],
              kind="record"),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents wrong-state same-slug collisions."""
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
