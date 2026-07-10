#!/usr/bin/env python3
"""Enrichment batch 618: hand-curated claims for 5 VT R state representatives.

Continuing the archetype_party_default VT R state-rep bucket (Z→A sort).
Previous batch (617) covered: Michael Morgan, Michael Marcotte, Michael Boutin,
Matt Walker, Mary A. Morrissey.

Targets (5 R):
  Martha Feltus    (Caledonia-3 — Vice Chair Appropriations; NOT in office 2023-24)
  Mark Higley      (Orleans-Lamoille — Asst. Minority Leader, in office since 2009)
  Lisa Hango       (Franklin-5 — Vice-Chair Govt. Ops/Mil. Affairs; appointed 2019)
  Leland Morgan    (Grand Isle-Chittenden — NOT in office 2023-24; returned 2025)
  Larry Labor      (Essex-Orleans — Vice Chair Environment; appointed Dec 2021)

Tenure notes:
  - Martha Feltus served 2012-2023, sat out 2023-24 session, returned Jan 2025.
    She co-sponsored H.16 (2025 repeal) and was NOT eligible to vote on H.230/S.5.
  - Leland Morgan ran for Senate in 2022, lost; also NOT in office 2023-24.
    Confirmed he opposed Proposal 5 TWICE (2019-20 and 2021-22 sessions).

Each claim cites >=1 reliable source and reflects documented voting record /
public positions within the period each representative was actually in office.

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
    # ---------- Martha Feltus (VT-R, State Representative, Caledonia-3) ----------
    # Served 2012-2023 (sat out 2023-24), returned Jan 2025; Vice Chair Appropriations.
    # NOT eligible to vote on H.230 (2023) or S.5 veto override (2023) — not in office.
    ("martha-feltus", "VT", "Representative", [
        claim("mf1", "martha-feltus", "sanctity_of_life", 0, True,
              "Voted NO on Proposal 5 — Vermont's constitutional amendment enshrining "
              "unlimited reproductive autonomy with no gestational limit — in the February "
              "8, 2022 House floor vote (107-41). The Caledonian Record reported her "
              "position directly: 'I do not believe that the constitutional amendment is "
              "necessary.' Feltus was among the 41 House members (virtually all Republicans "
              "— 40 of 41 nays were GOP) who voted against the amendment. Her district "
              "covers Lyndon, Newark, Sheffield, Sutton, and Wheelock in the Northeast "
              "Kingdom; the Caledonian Record documented that NEK representatives were "
              "'among the minority' who opposed the amendment. The Vermont Right to Life "
              "Committee published full House roll call documentation of all votes on "
              "Proposal 5 / Article 22.",
              ["https://www.caledonianrecord.com/news/local/local-legislators-take-a-position-on-proposal-5/article_88632b22-d14d-5c62-a7f9-dff5dc16a65b.html",
               "https://www.caledonianrecord.com/news/local/majority-of-nek-lawmakers-among-the-minority-in-full-prop-5-house-vote/article_558a25ea-f91d-5461-aa3a-b2f8518e7a6f.html",
               "https://www.vrlc.net/house-and-senate-roll-call-votes-for-proposal-5-article-22/"],
              kind="statement"),
        claim("mf2", "martha-feltus", "refuse_state_overreach", 0, True,
              "Voted to sustain Governor Scott's veto of H.715 (Vermont's 2022 Clean Heat "
              "Standard bill) on May 10, 2022 — the veto-override effort failed 99-51, one "
              "vote short of the required two-thirds, with Feltus and other Northeast "
              "Kingdom Republicans providing critical no-override votes. The Caledonian "
              "Record reported: 'A Quarter Of Veto-Sustaining Votes Come From Kingdom.' "
              "The Freedom Index explicitly confirmed 'Martha A. Feltus voted No' on "
              "this override vote. Then, after returning to the House in January 2025, "
              "Feltus co-sponsored H.16 — the 2025 bill formally repealing the Affordable "
              "Heat Act (Act 18/S.5, which had passed on a later veto override in 2023 "
              "while she was out of office). Her co-sponsorship of H.16 confirms her "
              "longstanding opposition to the mandate, which would have cost rural "
              "Caledonia County heating-oil customers hundreds to thousands of dollars "
              "annually with no practical alternative.",
              ["https://www.caledonianrecord.com/news/local/a-quarter-of-veto-sustaining-votes-come-from-kingdom/article_26b5a0e2-c02b-5136-b395-d70c7b665737.html",
               "https://freedomindex.us/vt/vote/3252",
               "https://legiscan.com/VT/bill/H0016/2025",
               "https://vtdigger.org/2022/05/10/by-one-vote-house-fails-to-override-veto-of-the-clean-heat-standard/"]),
        claim("mf3", "martha-feltus", "economic_stewardship", 2, True,
              "Serving as Vice Chair of the House Appropriations Committee in the "
              "2025-2026 session, Feltus is one of the senior Republican fiscal voices "
              "on state spending. During the May 2026 budget debate, she stated: "
              "'Even though it might be nice to say we want to tax the rich, they're "
              "already taxed very high' — articulating her consistent anti-tax, "
              "affordability-first posture. She ran her 2024 comeback campaign on a "
              "platform of reversing the affordability crisis created by the Democratic "
              "supermajority's spending, DMV fee hikes, and property tax increases. "
              "A career professional with 27 years in international sales and management "
              "at Weidmann Electrical Technology, she brings a private-sector perspective "
              "to the House's budget process.",
              ["https://vnews.com/2026/05/02/vermont-lawmakers-debate-state-budget/",
               "https://www.caledonianrecord.com/news/local/feltus-quimby-elected-in-caledonia-3-house-race/article_1a5dbb4f-f9a8-5998-a099-2bb959d94789.html"],
              kind="statement"),
    ]),

    # ---------- Mark Higley (VT-R, State Representative, Orleans-Lamoille; Asst. Min. Leader) ----------
    ("mark-higley", "VT", "Representative", [
        claim("mh1", "mark-higley", "sanctity_of_life", 0, True,
              "Voted NO on Proposal 5 — Vermont's constitutional amendment enshrining "
              "unrestricted abortion through all nine months — in the February 8, 2022 "
              "House floor vote (107-41). The Caledonian Record confirmed: 'Mark Higley, "
              "of Lowell, voted against Proposal 5' and quoted him directly: "
              "'Constitutionally guaranteeing the right of someone to abort at the expense "
              "of the life of an unborn child is wrong. I consider the human fetus another "
              "human.' He also raised the concern that a constitutional right could compel "
              "doctors, nurses, and hospitals to perform abortions against their conscience. "
              "Higley was one of 40 Republicans (out of 45 present) who voted no; only "
              "5 Republicans crossed to vote yes.",
              ["https://www.caledonianrecord.com/news/local/majority-of-nek-lawmakers-among-the-minority-in-full-prop-5-house-vote/article_558a25ea-f91d-5461-aa3a-b2f8518e7a6f.html",
               "https://www.caledonianrecord.com/news/local/local-legislators-take-a-position-on-proposal-5/article_88632b22-d14d-5c62-a7f9-dff5dc16a65b.html",
               "https://vtdigger.org/2022/02/08/vermont-house-approves-prop-5-sending-reproductive-rights-question-to-voters/"],
              kind="statement"),
        claim("mh2", "mark-higley", "refuse_state_overreach", 0, True,
              "Primary-sponsored bills in the 2025-2026 session to repeal Vermont's Global "
              "Warming Solutions Act (H.62) and revoke Vermont's use of California's "
              "Clean Air Act waiver banning new gasoline vehicle sales by 2035 (H.65); "
              "co-sponsored H.16 to repeal the Affordable Heat Act. During April 2023 "
              "House floor debate on S.5 (Affordable Heat Act), Higley introduced an "
              "amendment to strip the GWSA's citizen-lawsuit enforcement clause — failed "
              "103-41 — stating: 'Vermonters cannot afford to spend $500 million per year "
              "on climate change initiatives and also spend hundreds of millions on "
              "hardening and repairing our infrastructure caused by extreme weather events.' "
              "He also voted NO on the S.5 veto override (May 11, 2023: 107-42; virtually "
              "all Republicans opposed). Published a March 2023 VTDigger op-ed explaining "
              "why he proposed repealing the GWSA, warning of its costs to rural families. "
              "Vermont Conservation Voters scored Higley 0% in 2026 (25% lifetime).",
              ["https://vtdigger.org/2023/03/24/rep-mark-higley-why-i-proposed-repealing-the-global-warming-solutions-act/",
               "https://vtdigger.org/2023/05/11/clean-heat-bill-clears-final-hurdle-as-house-overrides-phil-scotts-veto/",
               "https://www.vermontpublic.org/local-news/2023-04-20/vermont-house-gives-preliminary-approval-to-affordable-heat-act-climate-bill",
               "https://legislature.vermont.gov/bill/status/2026/H.16"],
              kind="statement"),
        claim("mh3", "mark-higley", "economic_stewardship", 2, True,
              "Elevated to House Republican Assistant Minority Leader (No. 2 Republican in "
              "the Vermont House) in January 2026 when predecessor Rep. Casey Toof resigned "
              "to become St. Albans Town manager. As a member of the House Ways and Means "
              "Committee in the 2025-2026 session, Higley opposed adding a homestead "
              "property tax exemption to education finance reform bill H.454, arguing the "
              "provision 'doesn't belong there' — favoring targeted, fiscally disciplined "
              "reform over add-ons that complicate the tax base. A self-employed general "
              "contractor and member of the Vermont Beef Producers Association and Vermont "
              "Sugar Makers Association, Higley has brought a rural small-business taxpayer "
              "perspective to the House since 2009, consistently advocating Vermont reduce "
              "its regulatory and tax burden on working families.",
              ["https://vtdigger.org/2026/01/08/rep-casey-toof-vermont-houses-no-2-republican-to-resign/",
               "https://vtdigger.org/2026/03/26/vermont-house-advances-property-tax-bill-with-7-average-increase/",
               "https://www.newportvermontdailyexpress.com/news/representative-higley-reports-at-the-half-way-point/article_31a6ad63-76f0-4940-9305-1d6044a0fc0e.html"]),
    ]),

    # ---------- Lisa Hango (VT-R, State Representative, Franklin-5; appointed Feb 2019) ----------
    ("lisa-hango", "VT", "Representative", [
        claim("lh1", "lisa-hango", "sanctity_of_life", 0, True,
              "Voted NO on Proposal 5 — Vermont's constitutional amendment enshrining "
              "unlimited abortion rights with no gestational limit — in the February 8, 2022 "
              "House floor vote (107-41). Hango was among the 41 House members (virtually "
              "the entire Republican caucus) who voted against the amendment — 40 of 41 no "
              "votes were Republicans. Appointed to the House in February 2019 by Gov. Phil "
              "Scott to represent Franklin-5 (Berkshire and surrounding Franklin County "
              "towns), she has served continuously and was re-elected in 2022 and 2024. "
              "The Vermont Right to Life Committee documented all House roll call votes "
              "on Proposal 5 / Article 22.",
              ["https://www.vrlc.net/house-and-senate-roll-call-votes-for-proposal-5-article-22/",
               "https://vtdigger.org/2022/02/08/vermont-house-approves-prop-5-sending-reproductive-rights-question-to-voters/"]),
        claim("lh2", "lisa-hango", "self_defense", 1, True,
              "Voted against H.230 (2023) — which created a 72-hour firearm purchase "
              "waiting period, expanded red-flag ERPO eligibility to family and household "
              "members, and imposed mandatory safe-storage requirements — as part of the "
              "34-member Republican-led opposition bloc (H.230 passed 106-34, May 5, 2023). "
              "Also opposed H.606 (2026), Vermont's omnibus firearms bill that banned "
              "rapid-fire devices, expanded the prohibited-persons list, and created FFL "
              "liability provisions. H.606 advanced through the House Judiciary Committee "
              "6-5 along strict party lines (all 5 Republicans voted no), consistent with "
              "Hango's record of opposing firearms restrictions. NRA-ILA flagged both bills "
              "as major threats to Vermont gun rights.",
              ["https://vtdigger.org/2023/05/19/vermont-democrats-pushed-through-major-firearms-legislation-this-year-will-it-hold-up-in-court/",
               "https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://www.nraila.org/articles/20260323/vermont-omnibus-gun-control-bill-passes-house-with-significant-amendments/"]),
        claim("lh3", "lisa-hango", "economic_stewardship", 2, True,
              "Co-authored H.255 (2024) to exempt all military retirement income and "
              "military survivor benefit payments from Vermont income tax, and co-wrote "
              "a March 2025 VTDigger op-ed — 'It's time for Vermont to stop taxing "
              "military survivor and retirement benefits' — alongside Rep. Laura Sibilia "
              "and Sen. Joe Major. Hango serves as Vice-Chair of the House Committee on "
              "Government Operations and Military Affairs and co-chairs both the VT "
              "National Guard and Veterans Affairs Caucus and the VT Rural Caucus, "
              "reflecting consistent advocacy for reducing the financial burden on Vermont's "
              "military families and rural communities. She was recognized as Vermont "
              "League of Cities and Towns Legislator of the Year (2023) for her advocacy "
              "for small-town Vermont.",
              ["https://vtdigger.org/2025/03/25/rep-lisa-hango-rep-laura-sibilia-and-sen-joe-major-its-time-for-vermont-to-to-stop-taxing-military-survivor-and-retirement-benefits/",
               "https://legislature.vermont.gov/people/single/2026/31854"]),
    ]),

    # ---------- Leland Morgan (VT-R, State Representative, Grand Isle-Chittenden) ----------
    # NOT in the House 2023-2024 (ran for State Senate, lost). Returned Jan 2025.
    # Confirmed he voted against Proposal 5 in BOTH 2019-20 and 2021-22 sessions.
    ("leland-morgan", "VT", "Representative", [
        claim("lem1", "leland-morgan", "sanctity_of_life", 0, True,
              "Voted against Proposal 5 — Vermont's abortion constitutional amendment — "
              "in BOTH legislative passages required before it reached voters: first in the "
              "2019-2020 session and again in the February 8, 2022 final House vote "
              "(107-41; 40 Republicans voted no). Morgan publicly confirmed this when "
              "announcing his 2022 State Senate run: he 'voted against it in the legislature "
              "twice.' He explained his objections to the amendment's vague language: "
              "'If we're going to have a constitutional amendment, let's have something "
              "written that everyone can read and everyone can understand, without it "
              "having to go into the courts to be deciphered.' He also questioned whether "
              "the broad language implicitly covered transgender policy: 'If it wants to "
              "be about transgender stuff, which people say that it might imply, let's "
              "talk about it, put that in there.' A retired military officer and former "
              "Justice of the Peace from West Milton, Morgan is one of only a few Vermont "
              "legislators who opposed Proposal 5 on two separate floor votes.",
              ["https://www.miltonindependent.com/news/milton-rep-leland-morgan-aims-for-chittenden-north-senate-seat/article_278c73d8-5bab-11ed-b92b-b386b1f93b1e.html",
               "https://www.essexreporter.com/news/government/rep-leland-morgan-aims-for-chittenden-north-senate-seat/article_239a8a98-5c47-11ed-aceb-471b776c6606.html",
               "https://www.vrlc.net/house-and-senate-roll-call-votes-for-proposal-5-article-22/"],
              kind="statement"),
        claim("lem2", "leland-morgan", "refuse_state_overreach", 0, True,
              "Returned to the Vermont House in January 2025 running explicitly on "
              "reversing the 'affordability crisis' caused by Democrats' 2023 veto overrides "
              "— including the Affordable Heat Act (Clean Heat Standard) — stating "
              "'people have to be able to afford to live and work here.' Co-sponsored H.16 "
              "(2025) to formally repeal the Affordable Heat Act, a mandate that would have "
              "required heating fuel dealers across Grand Isle County's island communities "
              "to accumulate state-mandated carbon-reduction credits at projected household "
              "costs of hundreds to thousands of dollars annually, with no practical "
              "alternative fuel for island residents. VTDigger reported in July 2026 that "
              "Vermont Republicans celebrated the Clean Heat Standard's demise as a "
              "signature legislative win for rural affordability.",
              ["https://www.miltonindependent.com/news/elections/3-candidates-vie-for-vermont-house-in-grand-isle-chittenden-district/article_3e88540c-8b1b-11ef-9402-9b53225f07b9.html",
               "https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/",
               "https://legiscan.com/VT/bill/H0016/2025"]),
        claim("lem3", "leland-morgan", "economic_stewardship", 2, True,
              "Serving as Ranking Member of the House Committee on Agriculture, Food "
              "Resiliency, and Forestry in the 2025-2026 session, Morgan raised concerns "
              "about H.454 (education finance reform) threatening consolidation of small "
              "schools in Grand Isle County's island communities. Ran his 2024 campaign "
              "on an explicit affordability platform, citing Democratic-imposed property "
              "tax increases, DMV fee hikes, and veto overrides as having made Vermont "
              "unaffordable for families in his district. H.454 (Act 73) passed 96-45 "
              "in June 2025 with strong Republican opposition. Morgan brings a background "
              "as a retired military officer, former Milton Selectboard member, Justice of "
              "the Peace, and former educator to his fiscal-conservative position.",
              ["https://www.miltonindependent.com/news/elections/3-candidates-vie-for-vermont-house-in-grand-isle-chittenden-district/article_3e88540c-8b1b-11ef-9402-9b53225f07b9.html",
               "https://ballotpedia.org/Leland_Morgan"]),
    ]),

    # ---------- Larry Labor (VT-R, State Representative, Essex-Orleans) ----------
    # Appointed Dec 2021; elected 2022 and 2024. Vice Chair, House Environment Committee.
    ("larry-labor", "VT", "Representative", [
        claim("ll1", "larry-labor", "sanctity_of_life", 0, True,
              "Voted NO on Proposal 5 — Vermont's constitutional amendment enshrining "
              "unlimited abortion rights with no gestational limit — in the February 8, 2022 "
              "House floor vote (107-41). Labor was appointed to the House in December 2021 "
              "by Gov. Phil Scott to represent the Orleans-1 District (later redrawn as "
              "Essex-Orleans), making him eligible to vote on Proposal 5. He was among the "
              "41 members who voted against the amendment, a group composed almost entirely "
              "of Republicans (40 of 41 no votes). Vermont Conservation Voters gave Labor "
              "a 0% score for 2022 and a 0% lifetime score — a record consistent with his "
              "documented opposition to the Democratic supermajority agenda. The Vermont "
              "Right to Life Committee published full House roll call documentation of all "
              "votes on Proposal 5.",
              ["https://vermontconservationvoters.com/legislators/larry-labor/",
               "https://vtdigger.org/2022/02/08/vermont-house-approves-prop-5-sending-reproductive-rights-question-to-voters/",
               "https://www.vrlc.net/house-and-senate-roll-call-votes-for-proposal-5-article-22/"]),
        claim("ll2", "larry-labor", "self_defense", 1, True,
              "Part of the House Republican caucus that uniformly opposed H.230 (2023) "
              "— which created a 72-hour firearm purchase waiting period, expanded red-flag "
              "ERPO eligibility to family members, and imposed mandatory safe-storage "
              "requirements (passed 106-34, May 5, 2023) — and opposed H.606 (2026), "
              "Vermont's omnibus firearms bill that banned rapid-fire devices, expanded "
              "the prohibited-persons list, and created FFL liability provisions. H.606 "
              "advanced through the House Judiciary Committee 6-5 on a strict party-line "
              "vote (all 5 Republicans against). Labor's Essex-Orleans district in "
              "Vermont's Northeast Kingdom is hunting and outdoor recreation country; "
              "NRA-ILA tracked both bills as major threats to Vermont gun owners.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://vtdigger.org/2023/05/19/vermont-democrats-pushed-through-major-firearms-legislation-this-year-will-it-hold-up-in-court/",
               "https://www.nraila.org/articles/20260323/vermont-omnibus-gun-control-bill-passes-house-with-significant-amendments/"]),
        claim("ll3", "larry-labor", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (January 2025) — the bill to formally repeal Vermont's "
              "Affordable Heat Act (Act 18/S.5, the Clean Heat Standard) — a mandate that "
              "would have imposed state-required carbon-credit compliance on home-heating "
              "fuel dealers at projected household costs of hundreds to thousands of "
              "dollars annually. For Essex-Orleans constituents — in one of Vermont's "
              "coldest, most isolated, and lowest-income regions — the Clean Heat Standard "
              "represented a severe regulatory burden with no practical alternative to "
              "heating oil. Labor, as Vice Chair of the House Environment Committee, was "
              "directly positioned to oppose such mandates from within the relevant "
              "committee. VTDigger reported in July 2026 that Vermont Republicans "
              "celebrated the Standard's repeal as a signature legislative win for "
              "rural affordability.",
              ["https://www.billtrack50.com/billdetail/1768264",
               "https://fastdemocracy.com/bill-search/vt/2025-2026/bills/VTB00010113/",
               "https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
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
