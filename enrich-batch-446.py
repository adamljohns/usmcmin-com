#!/usr/bin/env python3
"""Enrichment batch 446: 5 Washington state House Republicans (archetype_party_default, 0 claims).

Federal and archetype_curated pools exhausted; continuing bottom-of-alphabet WA State
Representatives (reverse-alphabetical within remaining 34 WA R zero-claim pool).

Targets (all R):
  Stephanie McClintock  (WA HD-18, Clark County, since Jan 2023)
  Stephanie Barnard     (WA HD-08, Benton/Franklin Counties, since Jan 2023)
  Skyler Rude           (WA HD-16, Walla Walla County, since 2019)
  Sam Low               (WA HD-39, Snohomish/Skagit Counties, since Jan 2023)
  Rob Chase             (WA HD-04, Spokane Valley, 1st term 2021-23; returned Jan 2025)

Key bills / measures used:
  - HB 1240 (2023 RS): WA assault-weapons ban; final passage 56-42 (all Rs NAY, Mar 2023)
    Roll call confirmed: Barnard, Low, McClintock, and Rude all appear in the NAY list.
  - ESSB 5599 (2023 RS): Allowed shelters to house runaway minors for gender-affirming care
    without parental notification; 57-39 party-line (all Rs NAY, Apr 2023)
    Rude floor quote confirmed by KUOW; Barnard floor speech confirmed by YouTube.
  - HB 1296 / ESSB 5181 (2025): Democrat rollback of voter-passed Initiative 2081
  - IL26-638 (2026): Girls-sports protection initiative (445k+ signatures, Nov 2026 ballot)
  NOTE: Rob Chase was NOT in the Legislature during the 2023 session (lost Nov 2022 re-election;
        returned Jan 2025). His claims use 2025-2026 documented positions only.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
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
    # ------ Stephanie McClintock (WA-18, Clark County, R, State Rep since Jan 2023) ------
    ("stephanie-mcclintock", "WA", "state representative", [
        claim("sm1", "stephanie-mcclintock", "self_defense", 1, True,
              "Voted NAY on HB 1240 (final passage 56-42, March 2023), Washington's assault-weapons ban "
              "prohibiting the manufacture, import, distribution, and sale of semi-automatic rifles. "
              "Issued a statement on the 2023 gun bill package declaring: 'Majority Democrats continue "
              "to push legislation that makes it harder for law-abiding citizens to own firearms. House "
              "Republicans will continue to fight for your Second Amendment rights.' McClintock "
              "represents Clark County's 18th District (Battle Ground, Ridgefield, Camas, Washougal) "
              "and has consistently opposed new gun-control mandates since taking office in January 2023.",
              ["https://legiscan.com/WA/votes/HB1240/2023",
               "https://www.nwprogressive.org/weblog/2023/03/victory-washington-state-house-votes-to-ban-military-style-assault-weapons.html"]),
        claim("sm2", "stephanie-mcclintock", "family_child_sovereignty", 0, True,
              "Actively opposed ESSB 5599 (57-39 party-line, April 2023), which authorized licensed "
              "youth shelters to house runaway minors seeking gender-affirming care indefinitely without "
              "notifying their parents. McClintock offered an amendment during House floor debate "
              "(AMH MCCL WICM 617) requiring parental notification — rejected by Democrats. In February "
              "2025, published a legislative update titled 'Ruling party stripping parental rights and "
              "limiting open debate,' opposing Democrat HB 1296's rollback of voter-passed Initiative "
              "2081 (Parents' Bill of Rights). She proposed an amendment requiring immediate parental "
              "notification when a child is a victim of misconduct by a school employee — voted down "
              "by the Democrat majority.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023",
               "https://stephaniemcclintock.houserepublicans.wa.gov/2025/02/07/ruling-party-stripping-parental-rights-and-limiting-open-debate-legislative-update-from-rep-stephanie-mcclintock/"]),
    ]),

    # ------- Stephanie Barnard (WA-08, Benton/Franklin Tri-Cities, R, since Jan 2023) ----
    ("stephanie-barnard", "WA", "state representative", [
        claim("sb1", "stephanie-barnard", "self_defense", 1, True,
              "Voted NAY on HB 1240 (56-42, March 2023), Washington's assault-weapons ban. Spoke "
              "during House floor debate in favor of a Republican amendment protecting gun rights, "
              "declaring: 'if we don't protect that right, then what's to hold us back from infringing "
              "upon the others?' Barnard represents the 8th District Tri-Cities region (Benton and "
              "Franklin Counties: Kennewick, Pasco, Richland, West Richland) and has opposed all "
              "gun-control expansions since taking office in January 2023.",
              ["https://legiscan.com/WA/votes/HB1240/2023",
               "https://stephaniebarnard.houserepublicans.wa.gov/2023/03/10/rep-stephanie-barnard-speaks-against-bill-that-restricts-constitutionally-protected-gun-rights/"]),
        claim("sb2", "stephanie-barnard", "family_child_sovereignty", 0, True,
              "Voted NAY on ESSB 5599 (57-39 party-line, April 2023) and spoke against it on the "
              "House floor (documented in 'Rep. Stephanie Barnard speaks against bill that denies "
              "parental rights,' YouTube). In 2025, opposed ESSB 5181/HB 1296 — Democrat bills "
              "rolling back voter-approved Initiative 2081 (Parents' Bill of Rights) — stating on "
              "the House floor: 'This bill is creating a wedge, putting a wedge between parents and "
              "their children' and 'I feel like the schools should not operate under the premise that "
              "the parents are bad or dangerous.' Offered Amendment 1162 to ESSB 5181 to block "
              "removal of parents' access to children's school medical records; Democrats rejected it.",
              ["https://www.youtube.com/watch?v=ZvByJEG-N10",
               "https://washingtonstatestandard.com/2025/04/14/democrats-approve-changes-to-parents-rights-initiative/"]),
        claim("sb3", "stephanie-barnard", "biblical_marriage", 2, True,
              "Voted NAY on ESSB 5181/HB 1296 (passed 56-39, April 2025), the Democrat bill that "
              "dismantled voter-approved Initiative 2081's parental oversight provisions and codified "
              "state school-shelter access to gender-transition services for minors. Barnard explicitly "
              "framed Democrats' removal of parental access to school medical records as enabling "
              "institutions to act as if 'parents are bad or dangerous' — opposing the legislature's "
              "effort to embed transgender-ideology medical care for minors into school policy outside "
              "parental authority. She is a mother of six and founded the ANGELS Network nonprofit "
              "providing resources to parents of newborns.",
              ["https://washingtonstatestandard.com/2025/04/14/democrats-approve-changes-to-parents-rights-initiative/",
               "https://app.leg.wa.gov/billsummary?BillNumber=5181&Year=2025"]),
    ]),

    # ----------- Skyler Rude (WA-16, Walla Walla County, R, State Rep since 2019) ---------
    ("skyler-rude", "WA", "state representative", [
        claim("sr1", "skyler-rude", "family_child_sovereignty", 0, True,
              "Voted NAY on ESSB 5599 (57-39 party-line, April 2023), which allowed licensed youth "
              "shelters to house runaway minors seeking gender-affirming care without parental "
              "notification. Rude spoke on the House floor: 'There are a lot of loving parents out "
              "there that may support their child in some of these choices down the road but might "
              "feel that it's not an appropriate time at 13 or 14 or 15 years old' — voting NAY "
              "because the bill removed parents from the decision entirely. In March 2025, published "
              "'Advocating for student safety and parental involvement in education — Opposition to "
              "House Bill 1296,' opposing the Democrat rollback of Initiative 2081 and arguing HB "
              "1296 'strips away key parental rights.' Co-moved January 2026 for committee hearings "
              "on IL26-001 (parental-rights restoration initiative, 418,666 signatures) — rejected "
              "by Democrats on a party-line floor vote.",
              ["https://www.kuow.org/stories/washington-s-regular-legislative-session-is-over-here-are-some-of-the-highlights",
               "http://skylerrude.houserepublicans.wa.gov/2025/03/13/rep-skyler-rude-advocating-for-student-safety-and-parental-involvement-in-education-opposition-to-house-bill-1296/",
               "http://skylerrude.houserepublicans.wa.gov/2026/01/28/lawmakers-refuse-to-hear-2026-initiatives-to-the-legislature/"]),
        claim("sr2", "skyler-rude", "self_defense", 1, True,
              "Voted NAY on HB 1240 (final passage 56-42, March 2023), Washington's ban on the "
              "manufacture, import, distribution, and sale of semi-automatic rifles. Rude represents "
              "the 16th District (Walla Walla County, plus parts of Benton and Franklin Counties) "
              "and voted with the full House Republican caucus against the ban, which passed on a "
              "near-party-line 56-42 vote with only two Democrats crossing to NAY. He serves as "
              "Ranking Member on the House Education and Appropriations Committees.",
              ["https://legiscan.com/WA/votes/HB1240/2023",
               "https://www.nwprogressive.org/weblog/2023/03/victory-washington-state-house-votes-to-ban-military-style-assault-weapons.html"]),
    ]),

    # ----------- Sam Low (WA-39, Snohomish/Skagit Counties, R, State Rep since Jan 2023) --
    ("sam-low", "WA", "state representative", [
        claim("sl1", "sam-low", "self_defense", 1, True,
              "Voted NAY on HB 1240 (56-42, March 2023), Washington's assault-weapons ban prohibiting "
              "the manufacture, import, distribution, and sale of semi-automatic rifles. Low represents "
              "the 39th District (rural Snohomish and Skagit Counties — Lake Stevens, Monroe, Sultan, "
              "Gold Bar, Arlington, Cascade foothills) and voted with the full House Republican caucus "
              "against the ban. He took office in January 2023 after serving on the Snohomish County "
              "Council (2016-2022) and holds an M.A. in Organizational Leadership from Maranatha "
              "Baptist University.",
              ["https://legiscan.com/WA/votes/HB1240/2023",
               "https://ballotpedia.org/Sam_Low"]),
        claim("sl2", "sam-low", "family_child_sovereignty", 0, True,
              "Voted NAY on ESSB 5599 (57-39 party-line, April 2023), which allowed licensed youth "
              "shelters to house runaway minors seeking gender-affirming care indefinitely without "
              "notifying parents. In March 2025, opposed HB 1296 — the Democrat rollback of "
              "voter-approved Initiative 2081 (Parents' Bill of Rights) — with a floor speech stating: "
              "'We are accountable to the voters, and that's why we're all here tonight. They signed "
              "400,000+ times. Over and over and over to send it [Initiative 2081] to us to make "
              "that decision.' Published a press release titled 'Rep. Sam Low says voters deserve to "
              "have the final say in Democrats' changes to Parents' Rights law.'",
              ["https://samlow.houserepublicans.wa.gov/2025/03/18/rep-sam-low-says-voters-deserve-to-have-the-final-say-in-democrats-changes-to-parents-rights-law/",
               "https://legiscan.com/WA/rollcall/SB5599/id/1266180"]),
        claim("sl3", "sam-low", "biblical_marriage", 2, True,
              "Delivered the official Washington House Republican caucus floor speech in support of "
              "IL26-638 (2026 citizen initiative certified with 445,187 signatures), which would "
              "require health-provider verification of biological sex for K-12 students competing in "
              "female-only sports in Washington state. Low was designated one of two caucus floor "
              "speakers on the initiative (alongside Rep. Joshua Penner); the speech was aired on "
              "TVW and posted by the WA House Republican caucus. IL26-638 directly counters Democrat "
              "legislation authorizing transgender participation in girls' sports and heads to the "
              "November 2026 ballot after Democrats declined to act on it in session.",
              ["https://houserepublicans.wa.gov/current/initiative-il26-638/",
               "https://ballotpedia.org/Washington_Limit_Participation_in_Female_Sports_to_Students_Verified_as_Biologically_Female_Initiative_(2026)"]),
    ]),

    # ------ Rob Chase (WA-04, Spokane Valley, R; 1st term 2021-23; returned Jan 2025) -----
    ("rob-chase", "WA", "state representative", [
        claim("rc1", "rob-chase", "election_integrity", 0, True,
              "In March 2026, led a letter co-signed by 30 House Republicans to Governor Bob Ferguson "
              "and Secretary of State Steve Hobbs urging cooperation with federal election integrity "
              "efforts under President Trump's March 25, 2025 Executive Order, including sharing voter "
              "registration data with federal partners to verify rolls. Published the letter with the "
              "statement: 'Election integrity is fundamental to a healthy democratic republic' and "
              "'Protecting voter privacy and protecting election integrity are not mutually exclusive "
              "goals.' Note: Chase was not in the Legislature during the 2023 session (lost his "
              "Nov 2022 re-election bid; returned after winning Nov 2024) and therefore did not vote "
              "on 2023 gun-control or gender-care bills.",
              ["https://robchase.houserepublicans.wa.gov/2026/03/10/rep-rob-chase-and-house-republicans-call-for-collaboration-with-federal-partners-to-strengthen-election-integrity/",
               "https://ballotpedia.org/Rob_Chase"]),
        claim("rc2", "rob-chase", "self_defense", 1, True,
              "In January 2025, immediately upon returning to the Legislature, issued a constituent "
              "alert titled 'Legislative note and upcoming gun bills' explicitly committing to vote "
              "against any legislation infringing on Second Amendment rights. Chase's political career "
              "reflects a consistent constitutional-liberty stance on firearms — he coordinated Ron "
              "Paul's 2008 and 2012 presidential campaigns in Eastern Washington, a role centered on "
              "constitutional limited government. During his first House term (2021-2023) he opposed "
              "Washington's escalating gun-control agenda; upon returning to office he immediately "
              "reaffirmed that position publicly.",
              ["https://robchase.houserepublicans.wa.gov/2025/01/16/legislative-note-and-upcoming-gun-bills-rep-rob-chase/",
               "https://ballotpedia.org/Rob_Chase"]),
        claim("rc3", "rob-chase", "economic_stewardship", 2, True,
              "Consistently opposes deficit spending and government budget expansion. During his first "
              "House term, opposed the record $65 billion 2021-23 supplemental state operating budget, "
              "stating: 'According to the census our state's population has increased about 13% in the "
              "last ten years, but our state budget has doubled in the same amount of time. This level "
              "of spending is unsustainable and irresponsible.' Introduced HB 2628 (2026) to require "
              "Washington's official budget outlook to be regularly updated with current revenue "
              "forecasts, enabling earlier identification of fiscal shortfalls. Has argued Washington "
              "'does not have a revenue problem — it has a spending problem,' opposing Governor "
              "Ferguson's 2025-2026 budget and its accompanying tax increases.",
              ["https://robchase.houserepublicans.wa.gov/2022/03/11/rep-chase-issues-statement-on-supplemental-state-operating-budget/",
               "https://robchase.houserepublicans.wa.gov/2026/01/22/2026-session-underway-more-tax-proposals-on-the-table-take-my-win-win-act-survey-improving-budget-transparency-and-accuracy-rep-rob-chase/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
    """
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
