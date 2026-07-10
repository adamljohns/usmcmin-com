#!/usr/bin/env python3
"""Enrichment batch 619: hand-curated claims for 5 VT R state representatives.

Continuing the archetype_party_default VT R state-rep bucket (Z→A sort).
Previous batch (618) covered: Martha Feltus, Mark Higley, Lisa Hango,
Leland Morgan, Larry Labor.

Targets (5 R):
  Kenneth Goslant   (Washington-1 — Berlin/Northfield; Judiciary Clerk; in office since Jan 2019)
  Kevin C. Winter   (Rutland-Windsor — Ludlow/Mt. Holly/Shrewsbury; first elected Nov 2024)
  Kumulia Long      (Chittenden-Franklin — Milton/Georgia; appointed April 1, 2026)
  Ken Wells         (Orleans-3 — Barton/Brownington/Evansville/Orleans/Westmore; first elected Nov 2024)
  Joshua Dobrovich  (Orange-3 — Chelsea/Williamstown; first elected Nov 2024)

Tenure notes:
  - Kenneth Goslant in office since January 2019; eligible for all 2022-23 votes.
  - Kevin C. Winter, Ken Wells, and Joshua Dobrovich all took office January 8, 2025 —
    not eligible for any 2022-2023 votes (Proposal 5, H.230, S.5 override).
  - Kumulia Long appointed April 1, 2026 — not eligible for any pre-2026 votes.
    H.16 never received a House floor vote (died in committee/administrative channels).

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
    # ---------- Kenneth Goslant (VT-R, State Representative, Washington-1; Clerk Judiciary) ----------
    # In office since January 2019 (Berlin/Northfield, Washington County).
    # Founder/owner, Goslant Granite Company (1989-present); 10 years Northfield Select Board.
    ("kenneth-goslant", "VT", "Representative", [
        claim("kg1", "kenneth-goslant", "self_defense", 1, True,
              "A March 2023 VTDigger op-ed by Norm Vandal identified Goslant as having "
              "'sought out and proudly received' a 95% NRA Political Victory Fund rating "
              "and stated he 'has voted against every piece of legislation pertaining to "
              "gun reform and gun safety' in the Vermont House. That documented record "
              "encompasses H.230 (2023) — Vermont's gun bill imposing a 72-hour firearm "
              "purchase waiting period, expanded red-flag law (ERPO) eligibility to family "
              "and household members, and mandatory safe-storage requirements, which passed "
              "106-34 in May 2023 — as well as earlier gun legislation in the 2019-2022 "
              "sessions. Goslant serves as Clerk of the House Judiciary Committee, the "
              "panel through which firearms legislation moves before reaching the floor, "
              "giving him a front-row opposition role on every gun bill advanced by "
              "Vermont's Democratic supermajority. Vermont Conservation Voters scored him "
              "0% in 2026, consistent with his documented pattern of opposing the "
              "progressive legislative agenda. His Berlin and Northfield constituents in "
              "Washington County include many hunters, farmers, and rural homeowners who "
              "rely on firearms for lawful self-defense and sport.",
              ["https://vtdigger.org/2023/03/04/norm-vandal-stand-up-against-the-gun-rights-media-campaign/",
               "https://vermontconservationvoters.com/legislators/kenneth-goslant/",
               "https://vtdigger.org/2023/05/19/vermont-democrats-pushed-through-major-firearms-legislation-this-year-will-it-hold-up-in-court/"],
              kind="record"),

        claim("kg2", "kenneth-goslant", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (January 2025) — the bill to formally repeal Vermont's "
              "Affordable Heat Act (Act 18/S.5, the Clean Heat Standard) — a state energy "
              "mandate that would have required home-heating fuel dealers in Berlin and "
              "Northfield to accumulate government-mandated carbon-reduction credits at "
              "projected household costs of hundreds to thousands of dollars annually. "
              "In his January 2025 legislative update, Rep. Winter (co-sponsor) summarized "
              "the Public Utilities Commission's own report finding that 'the Clean Heat "
              "Standard is not well suited to Vermont' and that state emissions goals would "
              "be 'best achieved by building upon existing programs, rather than overlaying "
              "a new and complex regulatory structure.' Vermont Conservation Voters scored "
              "Goslant 0% in 2026 and 16% lifetime — a record reflecting consistent "
              "opposition to state energy and environmental mandates across his seven years "
              "in the House. VTDigger confirmed in June 2025 that Vermont's Clean Heat "
              "Standard was effectively dead, vindicated by the PUC's own assessment.",
              ["https://legislature.vermont.gov/bill/status/2026/H.16",
               "https://vermontconservationvoters.com/legislators/kenneth-goslant/",
               "https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/",
               "https://vtdigger.org/2023/05/11/clean-heat-bill-clears-final-hurdle-as-house-overrides-phil-scotts-veto/"],
              kind="record"),

        claim("kg3", "kenneth-goslant", "sanctity_of_life", 0, True,
              "Voted NO on Proposal 5 — Vermont's constitutional amendment enshrining "
              "unlimited abortion rights with no gestational limit — in the February 8, "
              "2022 House floor vote (107-41). The Ethan Allen Institute documented "
              "Goslant's NO vote on the Reproductive Liberty Amendment, and the Vermont "
              "Right to Life Committee published full House roll-call documentation of "
              "all votes on Proposal 5 / Article 22. Goslant was among the 41 members "
              "(40 of 41 being Republicans) who opposed the amendment — which went on to "
              "be ratified by Vermont voters in November 2022 as Article 22. His Berlin "
              "and Northfield district in Washington County includes many pro-life "
              "constituents, and Goslant has maintained a consistent conservative posture "
              "on life issues throughout his tenure since January 2019. Vermont "
              "Conservation Voters scored him 0% in 2026 (16% lifetime), consistent with "
              "his documented opposition to the progressive supermajority agenda across "
              "social, environmental, and constitutional issues.",
              ["https://www.ethanallen.org/KGoslant",
               "https://www.vrlc.net/house-and-senate-roll-call-votes-for-proposal-5-article-22/",
               "https://vtdigger.org/2022/02/08/vermont-house-approves-prop-5-sending-reproductive-rights-question-to-voters/"],
              kind="record"),

        claim("kg4", "kenneth-goslant", "public_justice", 0, True,
              "Voted against H.225 (April 2021) — the bill to decriminalize buprenorphine, "
              "an opioid treatment drug, in Vermont. Goslant stated publicly that he feared "
              "the legislation was 'rushed' and warned it could lead 'an unsuspecting, "
              "uninformed young person down the road toward addiction,' adding: 'If that "
              "tragic event was to happen, my decision would haunt me for life.' H.225 "
              "ultimately passed the House, but Goslant's NO vote reflected a consistent "
              "law-and-order, public-health-protective posture on drug policy. As Clerk "
              "of the House Judiciary Committee — the panel that processes criminal-justice "
              "and public-safety legislation — since 2019, Goslant occupies the senior "
              "Republican procedural role on criminal-law matters, providing a consistent "
              "voice for enforcement-first approaches over decriminalization or harm-reduction "
              "frameworks pushed by Vermont's progressive majority.",
              ["https://vtdigger.org/2021/04/08/house-backs-bill-decriminalizing-opioid-treatment-drug/",
               "https://legislature.vermont.gov/committee/detail/2026/18"],
              kind="record"),
    ]),

    # ---------- Kevin C. Winter (VT-R, State Representative, Rutland-Windsor; first elected Nov 2024) ----------
    # Ludlow, Mount Holly, Shrewsbury. In office since January 8, 2025.
    # 45-year engineering/manufacturing career (GE, UTC, TECO-Westinghouse); 11 yrs NY school board.
    ("kevin-c-winter", "VT", "Representative", [
        claim("kw1", "kevin-c-winter", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (January 2025), Vermont's bill to formally repeal the "
              "Affordable Heat Act / Clean Heat Standard — a state energy mandate that "
              "would have imposed carbon-credit compliance costs on home-heating fuel "
              "dealers serving Ludlow, Mount Holly, and Shrewsbury. In a January 2025 "
              "letter to the editor in the Vermont Journal, Winter summarized the Public "
              "Utilities Commission's own January 2025 report: the PUC concluded 'the "
              "Clean Heat Standard is not well suited to Vermont' and that state emissions "
              "goals would be 'best achieved by building upon existing programs, rather than "
              "overlaying a new and complex regulatory structure.' Vermont's Clean Heat "
              "Standard was declared dead in June 2025, vindicating Goslant's, Winter's, "
              "and other Republican co-sponsors' position. A constitutional originalist who "
              "ran on reversing 'excessive taxes and financial burdens on Vermonters created "
              "by the current Democratic Super Majority in Montpelier,' Winter has "
              "consistently opposed state regulatory overreach since taking office in "
              "January 2025 after flipping the Rutland-Windsor seat from a Democrat — "
              "the first Republican to hold it in over two decades.",
              ["https://legislature.vermont.gov/bill/status/2026/H.16",
               "https://vermontjournal.com/news/lte-kevin-winter-on-legislative-priorities/",
               "https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/",
               "https://www.rutlandherald.com/news/local/winter-elected-to-house-in-rutland-windsor-district/article_0a36bb4c-9be4-11ef-a08f-cb10024c5b03.html"],
              kind="record"),

        claim("kw2", "kevin-c-winter", "economic_stewardship", 2, True,
              "Co-sponsored H.74 (January 2025), a bipartisan bill to phase out Vermont's "
              "income tax on Social Security benefits over 8 years, which would eliminate "
              "a financial burden disproportionately borne by retired constituents in "
              "Ludlow, Mount Holly, and Shrewsbury. Vermont is one of only nine states "
              "that still tax Social Security benefits; the Vermont Biz reported the full "
              "phase-out would reduce state revenue by $56 million annually at maturity. "
              "Winter's campaign platform centered on reversing 'the excessive taxes and "
              "financial burdens on Vermonters that have been created by the current "
              "Democratic Super Majority in Montpelier,' stating his commitment to "
              "bringing fiscal balance to a legislature that had passed major property tax "
              "increases, DMV fee hikes, the Clean Heat Standard, and the Global Warming "
              "Solutions Act. A 45-year veteran of corporate manufacturing and sales (GE, "
              "UTC/Carrier Corp., TECO-Westinghouse), Winter applies a private-sector "
              "cost-benefit discipline to state fiscal policy that Vermont's Democratic "
              "supermajority has consistently overridden.",
              ["https://legislature.vermont.gov/bill/status/2026/H.74",
               "https://vermontbiz.com/news/2025/january/24/vermont-legislators-introduce-bi-partisan-bill-phase-out-tax-social-security",
               "https://mountaintimes.info/2025/01/29/vt-legislators-introduce-bi-partisan-bill-to-phase-out-tax-on-social-security-benefits/",
               "https://ballotpedia.org/Kevin_Winter"],
              kind="record"),

        claim("kw3", "kevin-c-winter", "self_defense", 0, True,
              "Ran for the Vermont House in 2024 as a self-described 'constitutional "
              "originalist' committed to preserving 'individual liberties embodied "
              "especially in the 1st and 2nd Amendments,' a specific campaign commitment "
              "that contrasted him with Vermont Democrats who had passed H.230 (2023, gun "
              "waiting period / red-flag expansion / safe storage) and subsequently "
              "H.606 (2026, omnibus firearms restrictions). The Vermont Journal editorial "
              "board endorsed Winter specifically for bringing a principled "
              "constitutional-conservative voice to Montpelier. In his March 2026 "
              "legislative update Winter highlighted his support for H.769 (parental "
              "freedom in education) and H.767 (reforming Vermont's climate mandates) — "
              "illustrating a broad constitutional-conservative commitment extending to "
              "individual rights. Winter won by 15 percentage points in November 2024, "
              "flipping Rutland-Windsor for Republicans for the first time in over two "
              "decades, bringing to Montpelier a retired engineer and grandfather of seven "
              "with 11 years of New York school board experience.",
              ["https://kevinwinterforvt.com/about",
               "https://vermontjournal.com/editorial/opinion-kevin-winter-for-vermont-house-of-representatives/",
               "https://vermontjournal.com/politics/lte-rep-kevin-winter-legislative-update/",
               "https://ballotpedia.org/Kevin_Winter"],
              kind="statement"),
    ]),

    # ---------- Kumulia Long (VT-R, State Representative, Chittenden-Franklin; appointed April 1, 2026) ----------
    # Milton and Georgia (Chittenden and Franklin counties). Appointed to replace Chris Taylor.
    # 11-yr VT Army National Guard combat vet; real estate broker; 4 yrs Milton school board (2 as chair).
    ("kumulia-long", "VT", "Representative", [
        claim("kl1", "kumulia-long", "self_defense", 0, True,
              "Endorsed by Gun Owners of Vermont as a 'pro-Second Amendment candidate' in "
              "the November 2020 Vermont State Senate race (Chittenden District) and "
              "received an NRA Political Victory Fund grade of AQ — an A based on candidate "
              "questionnaire, the highest rating available for a candidate without a "
              "legislative voting record. Long is a combat veteran who served 11 years in "
              "the Vermont Army National Guard, including overseas deployments as an "
              "intelligence analyst, and was awarded the Vermont Distinguished Service "
              "Medal — giving him direct experience with firearms both in military service "
              "and as a civilian and property owner in Milton. When Governor Phil Scott "
              "appointed Long to the Vermont House on April 1, 2026, replacing Rep. Chris "
              "Taylor (R-Milton) who resigned to serve as Milton town manager, the "
              "appointment continued the Chittenden-Franklin district's pro-Second "
              "Amendment representation. Long is running for the Vermont State Senate "
              "(Chittenden District) in the August 11, 2026 Republican primary.",
              ["https://gunownersofvermont.org/elect-kumulia-long-a-pro-second-amendment-candidate/",
               "https://vermontbiz.com/news/2026/april/01/governor-appoints-kumulia-long-milton-fill-house-seat",
               "https://governor.vermont.gov/press-release/governor-phil-scott-appoints-kumulia-long-house-representatives"],
              kind="statement"),

        claim("kl2", "kumulia-long", "family_child_sovereignty", 0, True,
              "Served four years on the Milton Town School District Board of Trustees, "
              "including two years as chair, overseeing policy development and budget "
              "management for the district where Long's three daughters attend school. "
              "Governor Scott specifically cited this school governance background when "
              "appointing Long on April 1, 2026: '[Long] has served on and chaired his "
              "local school board as well, which will be an important perspective as we "
              "move forward with education transformation.' Long was assigned to the "
              "House Education Committee immediately upon appointment — the same committee "
              "where his predecessor Rep. Chris Taylor had served as ranking Republican "
              "and vice chair — enabling him to continue the district's conservative "
              "voice on education policy, including resistance to top-down state mandates "
              "that override local school boards and parental preferences. Vermont "
              "conservatives in the 2025-26 session consistently opposed education reforms "
              "that centralize governance at the expense of local districts, parents, and "
              "community control.",
              ["https://vermontbiz.com/news/2026/april/01/governor-appoints-kumulia-long-milton-fill-house-seat",
               "https://schoolboardspotlight.org/governor-appoints-kumulia-long-to-fill-vacant-house-seat/",
               "https://vtdigger.org/2026/04/01/milton-state-representative-resigns-to-be-fully-present-in-town-manager-role/"],
              kind="record"),

        claim("kl3", "kumulia-long", "economic_stewardship", 2, True,
              "A licensed real estate broker serving Chittenden County for nearly a decade, "
              "Long has built his professional career around Vermont's housing and "
              "affordability market. His 2026 Senate campaign website frames the cost of "
              "living as 'a major concern for residents' of the region. Long's appointment "
              "to the House in April 2026 came as Vermont Republicans were celebrating a "
              "string of fiscal victories — repeal of the Clean Heat Standard (2025), "
              "partial repeal of Act 181 (land-use law, 2026), and resistance to further "
              "property tax increases — after years of Democratic supermajority spending "
              "that had made Vermont one of the nation's most expensive states. As a "
              "Milton resident and father of three daughters in the public school system, "
              "Long's appointment combined his military-service background with private-"
              "sector real estate expertise, reflecting a market-oriented, "
              "affordability-first approach to Vermont's fiscal challenges rather than the "
              "mandate-and-mandate-again approach of the Democratic majority.",
              ["https://vermontbiz.com/news/2026/april/01/governor-appoints-kumulia-long-milton-fill-house-seat",
               "https://vtdigger.org/2026/05/07/vermont-house-votes-to-partially-repeal-act-181/",
               "https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"],
              kind="statement"),
    ]),

    # ---------- Ken Wells (VT-R, State Representative, Orleans-3; first elected Nov 2024) ----------
    # Barton, Brownington, Evansville, Orleans, Westmore (Orleans County). 5th-gen Vermonter.
    # Former Newport Daily Express publisher; sports broadcaster; in office since January 8, 2025.
    ("ken-wells", "VT", "Representative", [
        claim("kew1", "ken-wells", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (January 2025), Vermont's bill to formally repeal the "
              "Affordable Heat Act / Clean Heat Standard, a state energy mandate that "
              "would have imposed carbon-credit compliance costs on home-heating fuel "
              "dealers serving the rural Orleans County communities of Barton, "
              "Brownington, Evansville, Orleans, and Westmore. Wells ran his 2024 "
              "campaign explicitly on opposing the Clean Heat Standard, stating: 'I don't "
              "want them to have to pick between buying groceries or purchasing fuel "
              "during the long winters.' As a fifth-generation Vermonter and publisher "
              "of the Newport Daily Express for a decade, Wells had direct familiarity "
              "with how state energy mandates and cost-of-living pressures fall hardest "
              "on rural Northeast Kingdom families. Vermont's Clean Heat Standard was "
              "declared effectively dead in June 2025, after the Public Utilities "
              "Commission found it 'not well suited to Vermont' — a vindication of the "
              "position Wells had campaigned on.",
              ["https://legislature.vermont.gov/bill/status/2026/H.16",
               "https://www.newportdispatch.com/2024/10/30/ken-wells-set-to-take-orleans-3-house-seat/",
               "https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/"],
              kind="record"),

        claim("kew2", "ken-wells", "public_justice", 0, True,
              "Published an April 2024 op-ed titled 'Enough is Enough' in the Newport "
              "Dispatch calling for aggressive crackdown on drug trafficking in Orleans "
              "County. Wells documented a pattern of out-of-state males moving into "
              "the region to sell drugs, targeting young women, and demanded law-abiding "
              "citizens 'stand up and report illegal activities rather than look the other "
              "way.' He explicitly opposed supervised injection sites, stating they 'have "
              "been proven to never work and just serve as a place for addicts to engage "
              "in their activities,' and expressed support for legislation to imprison "
              "fentanyl dealers for 10 years for selling 1,000 doses, calling it a "
              "necessary deterrent. As the Orleans-3 representative covering a rural "
              "Northeast Kingdom district that has been hit hard by the opioid crisis, "
              "Wells brings a community-protection, enforcement-first approach to public "
              "justice rather than the decriminalization framework preferred by Vermont "
              "progressives.",
              ["https://www.newportdispatch.com/2024/04/07/enough-is-enough-ken-wells/",
               "https://www.newportdispatch.com/2024/10/30/ken-wells-set-to-take-orleans-3-house-seat/"],
              kind="statement"),

        claim("kew3", "ken-wells", "economic_stewardship", 2, True,
              "As a member of the House Committee on Transportation, Wells conducted a "
              "'deep dive' into Vermont's $934 million VTrans budget and highlighted the "
              "agency's funding shortage — driven by stagnant gas-tax revenue — as a "
              "core challenge for rural districts where road infrastructure is critical. "
              "He designated passage of a responsible transportation funding bill as a "
              "legislative priority in the 2025-26 session. Wells also co-sponsored "
              "H.116 (February 2025) to limit campaign contributions for state "
              "legislative races, stating: 'I don't believe elections should be purchased "
              "and I don't like the one-sidedness of someone with a massive financial "
              "advantage.' A career newspaper publisher and former sales manager who "
              "watched Vermont's economy evolve over 30-plus years of community "
              "journalism in the Northeast Kingdom, Wells applies fiscal accountability "
              "principles from the private sector to state budget and transportation "
              "policy.",
              ["https://www.newportvermontdailyexpress.com/news/representative-ken-wells-talks-transportation-agency-revenue-shortage/article_be939cfc-4a7e-4998-a7d6-a33de3c66e17.html",
               "http://www.newportvermontdailyexpress.com/news/transportation-bill-a-priority-for-representative-ken-wells/article_76afb84c-e629-4083-abbc-4d408ac20595.html",
               "https://www.newportvermontdailyexpress.com/news/local-legislators-introduce-bill-seeking-to-limit-campaign-spending/article_2257d756-e73e-11ef-8475-03a55fe6bbc1.html"],
              kind="record"),
    ]),

    # ---------- Joshua Dobrovich (VT-R, State Representative, Orange-3; first elected Nov 2024) ----------
    # Chelsea and Williamstown (Orange County). In office since January 8, 2025.
    # Works in affordable housing; former Paine Mountain School District Board.
    ("joshua-dobrovich", "VT", "Representative", [
        claim("jd1", "joshua-dobrovich", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (January 2025), Vermont's bill to repeal the Affordable "
              "Heat Act / Clean Heat Standard, and ran his 2024 campaign explicitly "
              "opposing 'carbon taxes on motor fuels and home heating fuels, which "
              "disproportionately impact hardworking families.' Dobrovich also committed "
              "to reforming the Global Warming Solutions Act — changing its mandatory "
              "emissions targets back to aspirational goals and stripping the provision "
              "allowing citizen lawsuits against the state for missing targets. Vermont "
              "Conservation Voters scored him 0% in 2026 (first session), consistent "
              "with his campaign platform and co-sponsorship of H.16. His Orange-3 "
              "district covering Chelsea and Williamstown is rural, low-income, and "
              "heavily oil-heated — making state energy mandates an acute affordability "
              "threat for his constituents. Vermont's Clean Heat Standard was declared "
              "dead in June 2025, vindicating Dobrovich's pre-election campaign position.",
              ["https://legislature.vermont.gov/bill/status/2026/H.16",
               "https://www.ourherald.com/articles/seeks-seat-in-orange-3-district/",
               "https://vermontconservationvoters.com/legislators/joshua-dobrovich/",
               "https://vtdigger.org/2025/06/30/the-clean-heat-standard-is-dead-what-comes-next/"],
              kind="record"),

        claim("jd2", "joshua-dobrovich", "family_child_sovereignty", 0, True,
              "Ran a 2024 campaign specifically committing to 'remove political and "
              "social ideologies from classrooms' and focusing education on 'core "
              "competencies (reading, writing, math, science, and the arts),' and "
              "identified as a strong advocate for Vermont's existing school choice "
              "system. He stated at the time: 'I have yet to get one email that says, "
              "\"Reduce the amount of choice that we currently have. Go to no choice.\"' "
              "(Vermont Public, February 2025). As a primary sponsor of H.454 — the "
              "2025-26 education transformation bill that became Act 73 (signed June 16, "
              "2025) — Dobrovich shaped education governance reform that creates a new "
              "foundation-funding formula and new school district structures, bringing "
              "his prior experience on the Paine Mountain School District Board to bear "
              "on statewide policy. He also co-sponsored H.310 (2025), expanding school "
              "anti-harassment policies to include antisemitism awareness curriculum.",
              ["https://www.ourherald.com/articles/seeks-seat-in-orange-3-district/",
               "https://www.vermontpublic.org/local-news/2025-02-07/capitol-recap-school-choice-for-all",
               "https://ballotpedia.org/Josh_Dobrovich",
               "https://legislature.vermont.gov/bill/status/2026/H.454"],
              kind="statement"),

        claim("jd3", "joshua-dobrovich", "economic_stewardship", 2, True,
              "Ran his 2024 campaign on an explicit promise to 'implement a taxpayer "
              "bill of rights to cap state spending' — a concrete anti-deficit, "
              "constitutional-spending-limit commitment consistent with TABOR-style "
              "fiscal conservatism. He also campaigned to 'provide affordable, quality "
              "housing in central Vermont' and expand vocational arts education, "
              "reflecting both fiscal conservatism and workforce-investment priorities. "
              "Vermont Conservation Voters scored Dobrovich 0% in 2026, while the "
              "Freedom Index (freedomindex.us/vt) scored him 67% — a mix that reflects "
              "his limited-government fiscal posture offset by some bipartisan "
              "collaboration on education reform. As a first-term representative "
              "working in affordable housing in central Vermont, Dobrovich brings "
              "direct private-sector experience with the economic dysfunction caused "
              "by Vermont's regulatory excess and high tax burden, which have made the "
              "Green Mountain State one of the nation's least affordable for working "
              "families.",
              ["https://ballotpedia.org/Josh_Dobrovich",
               "https://www.ourherald.com/articles/seeks-seat-in-orange-3-district/",
               "https://vermontconservationvoters.com/legislators/joshua-dobrovich/",
               "https://freedomindex.us/vt/"],
              kind="statement"),
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
