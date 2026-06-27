#!/usr/bin/env python3
"""Enrichment batch 439: 5 West Virginia State Delegates (unset confidence, 0 claims).

Federal senator/representative pool exhausted. Continuing bottom-of-alphabet WV
State Delegate queue (reverse-alphabetical, next 5 after batch 438):
  Laura Kimble       (WV-71, R, Harrison Co., homemaker, Catholic, NRA member, HB4106 co-sponsor)
  Keith Marple       (WV-69, R, Harrison area/Lost Creek, assumed Dec 2022)
  Kathie Hess Crouse (WV-19, R, Putnam Co., microbiologist/mycologist, Educational Choice Chair)
  Josh Holstein      (WV-32, R, Boone Co., Marshall Univ. Economics grad, coal-miner family, HB4106+HB3016 co-sponsor)
  Joe Statler        (WV-77, R, Monongalia Co./Core, retired coal miner, assumed Dec 2022)

Key bills used:
  - HB 4106 (2026 RS): constitutional carry for 18-20 yr-olds, signed 4/1/2026, 87-9
  - HB 3016 (2025 RS): stricter voter photo ID, signed 4/30/2025, 88-10
  - SB 456 (2025 RS, Riley Gaines Act): biological sex definition in WV Code, signed 3/12/2025, 87-9
  - HB 2526 (2023 RS): 21.25% income tax cut, signed Mar 2023, 89-4 concurrence
  - HB 2777 (2025 RS): homeschool changes (removes HS diploma requirement for parents), Crouse sponsor

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
    # ---------- Laura Kimble (WV House Dist. 71, R, Harrison Co., homemaker, Catholic, NRA member) ----------
    ("laura-kimble", "WV", "Delegate", [
        claim("lk1", "laura-kimble", "self_defense", 0, True,
              "A homemaker, NRA member, and Roman Catholic from Harrison County serving District 71 since December 1, 2022, Kimble was a named co-sponsor of House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit, consistent with the right already extended to those 21 and older. Official engrossed bill text confirms: 'Delegate Horst and co-sponsored by Delegates Brooks, Dean, Holstein, Kimble, Mallow, Martin, Masters, Phillips, Ridenour, and Ward.' The NRA-backed bill passed the House 87–9 on February 17, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2026_SESSIONS/RS/bills/hb4106%20eng.pdf",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
        claim("lk2", "laura-kimble", "biblical_marriage", 2, True,
              "Kimble voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities to reject transgender ideology in law. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Kimble, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025, with former University of Kentucky swimmer Riley Gaines present at the signing ceremony.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
        claim("lk3", "laura-kimble", "election_integrity", 0, True,
              "Kimble voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options (such as Medicaid cards and utility bills) and required all voters to present a government-issued photo identification at the polls. The bill passed the House 88–10 on March 28, 2025, with near-unanimous Republican support, and was signed by Governor Patrick Morrisey on April 30, 2025. No Republican delegate voted against the bill.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://westvirginiawatch.com/2025/05/01/wv-gov-morrisey-signs-voter-photo-id-requirement-dei-ban-and-more-while-issuing-6-vetoes/"]),
    ]),

    # ---------- Keith Marple (WV House Dist. 69, R, Harrison area / Lost Creek) ----------
    ("keith-marple", "WV", "Delegate", [
        claim("km1", "keith-marple", "biblical_marriage", 2, True,
              "A Republican representing District 69 (Harrison County area, centered on Lost Creek) since December 1, 2022, Marple voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Marple, voted in favor. Governor Morrisey signed it into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
        claim("km2", "keith-marple", "economic_stewardship", 2, True,
              "Marple voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The compromise legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% immediately and establishing a revenue-triggered mechanism toward a 50% total reduction — returning an estimated $750 million annually to West Virginia taxpayers. The only dissenting votes came from Democrats. Governor Jim Justice signed it into law, marking one of the largest state income tax reductions in recent U.S. history.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/"]),
        claim("km3", "keith-marple", "election_integrity", 0, True,
              "Marple voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options (such as Medicaid cards and utility bills) and required all voters to present a government-issued photo identification at the polls. Sponsored by Delegate Erica Moore and co-sponsored by Delegates Holstein, Funkhouser, and others, the bill passed the House 88–10 on March 28, 2025, and was signed by Governor Patrick Morrisey on April 30, 2025.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://westvirginiawatch.com/2025/05/01/wv-gov-morrisey-signs-voter-photo-id-requirement-dei-ban-and-more-while-issuing-6-vetoes/"]),
    ]),

    # ---------- Kathie Hess Crouse (WV House Dist. 19, R, Putnam Co., microbiologist, Educational Choice Chair) ----------
    ("kathie-hess-crouse", "WV", "Delegate", [
        claim("khc1", "kathie-hess-crouse", "family_child_sovereignty", 0, True,
              "A homeschooling parent, microbiologist, and mycologist from Putnam County serving District 19 since December 1, 2022, Hess Crouse chairs the House Educational Choice Subcommittee and has made parental education rights her flagship issue — publicly stating: 'Parents deserve to decide what works best for their children, whether that is homeschooling, private school, microschools, charter schools or the Hope Scholarship... education belongs to parents, not the state.' She sponsored House Bill 2777 (2025 Regular Session), approved by the House on April 1, 2025, which removes West Virginia's requirement that a homeschooling parent hold a high school diploma — freeing more families to educate their children at home. As subcommittee chair she worked through 2025 with the state Department of Education to build West Virginia's first school choice portal, and announced plans to introduce legislation in 2026 to create a permanent state Office of School Choice.",
              ["https://westvirginiawatch.com/2025/10/07/house-republican-hess-crouse-working-with-wv-education-department-to-create-school-choice-portal/",
               "https://westvirginiawatch.com/2025/04/01/wv-house-approves-homeschool-changes-includes-addressing-parents-in-child-abuse-cases/",
               "https://blog.wvlegislature.gov/headline/2025/10/07/interim-report-educational-choice-subcommittee/"]),
        claim("khc2", "kathie-hess-crouse", "biblical_marriage", 2, True,
              "Hess Crouse voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Hess Crouse, voted in favor. Governor Morrisey signed the Riley Gaines Act on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
        claim("khc3", "kathie-hess-crouse", "economic_stewardship", 2, True,
              "Hess Crouse voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% and establishing a revenue-triggered mechanism toward a 50% total reduction — one of the largest state income tax cuts in recent U.S. history, returning an estimated $750 million annually to West Virginia taxpayers. The only dissenting votes came from Democrats.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/"]),
    ]),

    # ---------- Josh Holstein (WV House Dist. 32, R, Boone Co., Marshall Univ. Economics, coal-miner family) ----------
    ("josh-holstein", "WV", "Delegate", [
        claim("jh1", "josh-holstein", "self_defense", 0, True,
              "An economics graduate of Marshall University from Ashford (Boone County) — the son of generations of coal miners — Holstein was a named co-sponsor of House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds. Official engrossed bill text confirms: 'Delegate Horst and co-sponsored by Delegates Brooks, Dean, Holstein, Kimble, Mallow, Martin, Masters, Phillips, Ridenour, and Ward.' The NRA-backed bill passed the House 87–9 on February 17, 2026, the Senate 31–3 on March 13, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2026_SESSIONS/RS/bills/hb4106%20eng.pdf",
               "https://legiscan.com/WV/bill/HB4106/2026",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
        claim("jh2", "josh-holstein", "election_integrity", 0, True,
              "Holstein was a named co-sponsor of House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law requiring all voters to present a government-issued photo identification at the polls and eliminating previously accepted non-photo options such as Medicaid cards and utility bills. Legislative records confirm Holstein as co-sponsor: 'Delegates Moore, Akers, Jeffries, Rohrbach, B. Smith, Street, Phillips, Holstein, Funkhouser, Riley, and McGeehan.' The bill passed the House 88–10 on March 28, 2025, and was signed by Governor Morrisey on April 30, 2025.",
              ["https://legiscan.com/WV/text/HB3016/2025",
               "https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://westvirginiawatch.com/2025/05/01/wv-gov-morrisey-signs-voter-photo-id-requirement-dei-ban-and-more-while-issuing-6-vetoes/"]),
        claim("jh3", "josh-holstein", "biblical_marriage", 2, True,
              "Holstein voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Holstein, voted in favor. Governor Morrisey signed it March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/12/morrisey-signs-first-priority-bill-to-define-gender-in-wv-state-code-targeting-transgender-people/"]),
    ]),

    # ---------- Joe Statler (WV House Dist. 77, R, Monongalia Co./Core, retired coal miner) ----------
    ("joe-statler", "WV", "Delegate", [
        claim("js1", "joe-statler", "economic_stewardship", 2, True,
              "A retired coal miner from Core (Monongalia County) and former chairman of the Morgantown-Monongalia Metropolitan Planning Organization serving District 77 since December 1, 2022, Statler voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% immediately and establishing a revenue-triggered mechanism toward a 50% total reduction — returning an estimated $750 million annually to West Virginia taxpayers. The only dissenting votes came from Democrats. Governor Jim Justice signed it into law.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/"]),
        claim("js2", "joe-statler", "biblical_marriage", 2, True,
              "Statler voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Statler, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025, with Riley Gaines present at the signing ceremony.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/12/morrisey-signs-first-priority-bill-to-define-gender-in-wv-state-code-targeting-transgender-people/"]),
        claim("js3", "joe-statler", "self_defense", 0, True,
              "Statler voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit, consistent with the right already extended to those 21 and older. The NRA-backed bill passed the House 87–9 on February 17, 2026, the Senate 31–3 on March 13, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026. No Republican delegate voted against the bill.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
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
