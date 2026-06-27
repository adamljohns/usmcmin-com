#!/usr/bin/env python3
"""Enrichment batch 438: 5 West Virginia State Delegates (unset confidence, 0 claims).

Federal senator/representative pool exhausted. Continuing bottom-of-alphabet WV
State Delegate queue (reverse-alphabetical, next 5 after batch 437):
  Mark Zatezalo      (WV-02, R, Hancock/Brooke Co., hydrogeologist, Energy Cmte Vice Chair)
  Mark Dean          (WV-34, R, Mingo/McDowell Co., school principal, co-sponsor HB302 & HB4106)
  Margitta Mazzocchi (WV-31, R, Logan/Lincoln/Boone, small business, GOA-endorsed, naturalized citizen)
  Lori Dittman       (WV-63, R, Braxton Co., teacher, Higher Ed Subcommittee Chair)
  Lisa White         (WV-96, R, Berkeley Co., retired marketing director, Catholic, HB2712 lead sponsor)

Key bills used:
  - HB 302 (3rd Ext. Session 2022): near-total abortion ban, signed Sep 2022, 77-17
  - HCR 31 (2022 RS): Article V convention for fiscal restraint / term limits; passed 3/5/2022
  - HB 2526 (2023 RS): 21.25% income tax cut, signed Mar 2023, 89-4 concurrence
  - SB 456 (2025 RS, Riley Gaines Act): biological sex definition in WV Code, signed 3/12/2025, 87-9
  - HB 3016 (2025 RS): stricter voter photo ID, signed 4/30/2025, 88-10
  - HB 4106 (2026 RS): constitutional carry for 18-20 yr-olds, signed 4/1/2026, 87-9
  - HB 2712 (2025 RS): remove rape/incest exception from abortion ban (White lead sponsor)

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
    # ---------- Mark Zatezalo (WV House Dist. 02, R, Hancock/Brooke Co., hydrogeologist) ----------
    ("mark-zatezalo", "WV", "Delegate", [
        claim("mza1", "mark-zatezalo", "sanctity_of_life", 0, True,
              "A hydrogeologist from Weirton serving Hancock and Brooke counties in the Northern Panhandle, Zatezalo voted for House Bill 302 (2022 Third Extraordinary Session) — West Virginia's near-total abortion ban — and spoke on the House floor during debate in support of the bill. The ban, which prohibited all abortions beginning at fertilization with narrow medical exceptions, passed the House 77–17 on September 13, 2022, and was signed into law. Zatezalo's floor statement is confirmed in local press coverage of the vote.",
              ["https://www.weirtondailytimes.com/news/local-news/2022/07/w-va-house-passes-update-to-state-abortion-laws/",
               "https://blog.wvlegislature.gov/house-floor-session/2022/07/27/abortion-ban-moves-to-the-senate/"]),
        claim("mza2", "mark-zatezalo", "economic_stewardship", 2, True,
              "Zatezalo co-sponsored House Concurrent Resolution 31 (2022 Regular Session), applying to Congress to call an Article V constitutional convention to impose fiscal restraints on the federal government, limit federal power and jurisdiction, and limit the terms of office for federal officials and members of Congress. The resolution passed the House on March 5, 2022, with 36 Republican co-sponsors. Zatezalo has supported balanced-budget and fiscal-restraint convention efforts since at least 2016 (HCR 36), reflecting a consistent position on federal fiscal discipline.",
              ["https://openstates.org/wv/bills/2022/HCR31",
               "https://legiscan.com/WV/text/HCR31/id/2493409"]),
        claim("mza3", "mark-zatezalo", "self_defense", 0, True,
              "An NRA member who has publicly cited protecting gun-ownership rights as a legislative priority, Zatezalo voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit, consistent with the right already extended to those 21 and older. The NRA-backed bill passed the House 87–9 with near-unanimous Republican support and was signed by Governor Patrick Morrisey on April 1, 2026. No Republican delegate voted against the bill.",
              ["https://ballotpedia.org/Mark_Zatezalo",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
    ]),

    # ---------- Mark Dean (WV House Dist. 34, R, Mingo/McDowell Co., school principal) ----------
    ("mark-dean", "WV", "Delegate", [
        claim("mde1", "mark-dean", "sanctity_of_life", 0, True,
              "A school principal from Verner (Mingo County) serving District 34 since 2016 and Vice Chair of the Education Committee, Dean was a named co-sponsor of House Bill 302 (2022 Third Extraordinary Session) — West Virginia's near-total abortion ban, which prohibited all abortions beginning at fertilization with narrow medical exceptions. Official bill text confirms: 'Delegates Jeffries, Jennings, Dean, Honaker, G. Ward, Rowan, Worrell, Mallow, Forsht, and Miller.' The ban passed the House 77–17 and was signed into law September 2022.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2022_SESSIONS/3X/bills/HB302%20ORG.pdf",
               "https://www.weirtondailytimes.com/news/local-news/2022/07/w-va-house-passes-update-to-state-abortion-laws/"]),
        claim("mde2", "mark-dean", "self_defense", 0, True,
              "Dean was a named co-sponsor of House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit, consistent with the right already extended to those 21 and older. Official engrossed bill text confirms: 'Delegate Horst and co-sponsored by Delegates Brooks, Dean, Holstein, Kimble, Mallow, Martin, Masters, Phillips, Ridenour, and Ward.' The NRA-backed bill passed the House 87–9 and was signed by Governor Morrisey on April 1, 2026.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2026_SESSIONS/RS/bills/hb4106%20eng.pdf",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
        claim("mde3", "mark-dean", "economic_stewardship", 2, True,
              "As a senior Republican member serving since 2016 and Vice Chair of the Education Committee, Dean voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The compromise legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% immediately and establishing a revenue-triggered mechanism toward a 50% total reduction, returning an estimated $750 million annually to West Virginia taxpayers. The only dissenting votes came from Democrats.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/"]),
    ]),

    # ---------- Margitta Mazzocchi (WV House Dist. 31, R, Logan/Lincoln/Boone, GOA-endorsed) ----------
    ("margitta-mazzocchi", "WV", "Delegate", [
        claim("mma1", "margitta-mazzocchi", "sanctity_of_life", 0, True,
              "A naturalized U.S. citizen originally from Germany and small business owner from Chapmanville (Logan County) serving since 2020 and Vice Chair of the Finance and Health and Human Resources committees, Mazzocchi voted for House Bill 302 (2022 Third Extraordinary Session) — West Virginia's near-total abortion ban — and spoke on the House floor in favor: 'Life begins at conception, and I am glad that we are able to save so many babies.' The bill passed the House 77–17 on September 13, 2022, and was signed into law. She also co-sponsored HB 2461 (2025), imposing criminal penalties for performing chemical abortions using abortifacient drugs.",
              ["https://wvmetronews.com/2022/09/13/west-virginia-lawmakers-pass-bill-that-restricts-abortion-with-narrow-exceptions/",
               "https://www.billtrack50.com/billdetail/1834683"]),
        claim("mma2", "margitta-mazzocchi", "self_defense", 0, True,
              "Mazzocchi holds memberships in Gun Owners of America (GOA), the National Rifle Association (NRA), and the West Virginia Citizens Defense League. In September 2022, GOA endorsed her for 'relentless dedication to the Second Amendment,' noting that as a legal immigrant from Germany 'she understands the dangers of gun control' and 'has exceeded GOA's rigorous vetting process.' She voted YEA on House Bill 4106 (2026 Regular Session), expanding constitutional carry to 18- to 20-year-olds, per the official House roll call (Roll Call 00101, February 17, 2026). The bill passed 87–9 and was signed April 1, 2026.",
              ["https://www.gunowners.org/wv09072022a/",
               "https://www.wvlegislature.gov/legisdocs/2026/RS/votes/house/00101.pdf",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
        claim("mma3", "margitta-mazzocchi", "economic_stewardship", 2, True,
              "As Vice Chair of the Finance Committee, Mazzocchi voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The compromise legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% immediately and establishing a revenue-triggered mechanism toward a 50% total reduction — one of the largest state income tax reductions in recent U.S. history. The CPAC lifetime rating for Mazzocchi is 85%, with an 87% annual rating in 2023, reflecting consistent alignment with fiscal conservatism.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://www.cpac.org/bio/wv-margitta-mazzocchi"]),
    ]),

    # ---------- Lori Dittman (WV House Dist. 63, R, Braxton Co., teacher, Higher Ed Chair) ----------
    ("lori-dittman", "WV", "Delegate", [
        claim("ldi1", "lori-dittman", "self_defense", 0, True,
              "An 8th-grade teacher from Gassaway (Braxton County) serving District 63 since December 2022 and Chair of the Higher Education Subcommittee, Dittman voted YEA on House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit. She voted YEA on both roll calls: the initial passage (87–9, February 17, 2026) and the concurrence on the Senate-amended version (89–8, March 14, 2026). The NRA-backed bill was signed by Governor Patrick Morrisey on April 1, 2026.",
              ["https://legiscan.com/WV/rollcall/HB4106/id/1662298",
               "https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
        claim("ldi2", "lori-dittman", "biblical_marriage", 2, True,
              "Dittman voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities to reject transgender ideology in law. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Dittman, voted in favor. Governor Patrick Morrisey signed it into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-riley-gaines-act-law"]),
        claim("ldi3", "lori-dittman", "election_integrity", 0, True,
              "Dittman voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options (such as Medicaid cards and utility bills) and required all voters to present a government-issued photo identification at the polls. The bill passed the House 88–10 with strong Republican support and was signed by Governor Patrick Morrisey on April 30, 2025. No Republican delegate voted against the bill.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law"]),
    ]),

    # ---------- Lisa White (WV House Dist. 96, R, Berkeley Co., Catholic, HB2712 lead sponsor) ----------
    ("lisa-white", "WV", "Delegate", [
        claim("lw1", "lisa-white", "sanctity_of_life", 1, True,
              "A practicing Catholic from Inwood (Berkeley County) who took office December 1, 2024 after winning with 71% of the vote, White was the lead sponsor of House Bill 2712 (2025 Regular Session), which sought to eliminate the rape and incest exceptions from West Virginia's existing near-total abortion ban — leaving only three legal grounds (ectopic pregnancy, medical emergency, and nonviable fetus). She stated: 'I do believe that life begins at conception, and I cannot, in my mind, rationalize that their lives don't matter' and 'They are not responsible for the sins of their fathers... this baby was conceived under horrible, horrific circumstances, it's still a life to me.' The bill was reintroduced in the 2026 session. She also co-sponsored HB 2461 (2025), which would make performing a chemical abortion a felony.",
              ["https://westvirginiawatch.com/2025/02/21/gop-lawmakers-seek-to-remove-rape-incest-exemption-from-west-virginias-near-total-abortion-ban/",
               "https://www.wdtv.com/2025/02/24/they-are-not-responsible-sins-their-fathers-wv-delegate-supports-removing-rape-incest-abortion-exceptions/"]),
        claim("lw2", "lisa-white", "biblical_marriage", 2, True,
              "White voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities to reject transgender ideology in law. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including White, voted in favor. Governor Morrisey signed it March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
        claim("lw3", "lisa-white", "election_integrity", 0, True,
              "White voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options (such as Medicaid cards and utility bills) and required all voters to present a government-issued photo identification at the polls. She also co-sponsored HB 4684 (2026), which would eliminate state tax subsidies and credits for wind and solar energy projects. HB 3016 passed the House 88–10 and was signed by Governor Morrisey on April 30, 2025. No Republican delegate voted against it.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
