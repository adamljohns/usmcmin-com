#!/usr/bin/env python3
"""Enrichment batch 440: 5 West Virginia State Delegates (unset confidence, 0 claims).

Federal senator/representative pool exhausted. Continuing bottom-of-alphabet WV
State Delegate queue (reverse-alphabetical, next 5 after batch 439):
  Jordan Maynor     (WV-41, R, Mercer/Raleigh/Summers, Vice Chair Judiciary, assumed Dec 2022)
  Jordan Bridges    (WV-33, R, Logan area, Asst Majority Whip, Arch Coal, Beth Haven grad, assumed Dec 2022)
  Jonathan Pinson   (WV-17, R, Jackson Co., Asst Majority Whip, pastor & police officer, assumed Dec 2020)
  Jonathan Kyle     (WV-66, R, Elkins, real estate investor/CPA, assumed Dec 2024)
  John Paul Hott II (WV-85, R, Petersburg/Grant Co., first elected 2018, insurance/disposal svc, not running 2026)

Key bills used:
  - HB 4106 (2026 RS): constitutional carry for 18-20 yr-olds, signed 4/1/2026, 87-9
  - HB 3016 (2025 RS): stricter voter photo ID, signed 4/30/2025, 88-10
  - SB 456 (2025 RS, Riley Gaines Act): biological sex definition in WV Code, signed 3/12/2025, 87-9
  - HB 2526 (2023 RS): 21.25% income tax cut, signed Mar 2023, 89-4 concurrence

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
    # ---------- Jordan Maynor (WV House Dist. 41, R, Mercer/Raleigh/Summers, Vice Chair Judiciary) ----------
    ("jordan-maynor", "WV", "Delegate", [
        claim("jm1", "jordan-maynor", "biblical_marriage", 2, True,
              "A Republican representing District 41 (Mercer, Raleigh, and Summers counties) since December 1, 2022, and serving as Vice Chairman of the Standing Judiciary Committee in the 87th Legislature, Maynor voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities to reject transgender ideology in law. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Maynor, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://ballotpedia.org/Jordan_Maynor"]),
        claim("jm2", "jordan-maynor", "election_integrity", 0, True,
              "Maynor voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options such as Medicaid cards and utility bills, requiring all voters to present a government-issued photo identification at the polls. The bill passed the House 88–10 on March 28, 2025, with near-unanimous Republican support — no Republican delegate voted against it — and was signed by Governor Patrick Morrisey on April 30, 2025.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://westvirginiawatch.com/2025/05/01/wv-gov-morrisey-signs-voter-photo-id-requirement-dei-ban-and-more-while-issuing-6-vetoes/"]),
        claim("jm3", "jordan-maynor", "economic_stewardship", 2, True,
              "Maynor voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The compromise legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% immediately and establishing a revenue-triggered mechanism toward a 50% total reduction — returning an estimated $750 million annually to West Virginia taxpayers. The only dissenting votes came from Democrats. Governor Jim Justice signed it into law, marking one of the largest state income tax reductions in recent U.S. history.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/"]),
    ]),

    # ---------- Jordan Bridges (WV House Dist. 33, R, Logan area, Asst Majority Whip, Arch Coal, Beth Haven Christian School) ----------
    ("jordan-bridges", "WV", "Delegate", [
        claim("jb1", "jordan-bridges", "self_defense", 0, True,
              "A born-and-raised Logan, West Virginia Republican who graduated from Beth Haven Christian School (2006) and worked as a heavy equipment operator for Arch Coal before entering public service, Bridges serves as an Assistant Majority Whip in the West Virginia House and voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit, consistent with the right already extended to those 21 and older. The NRA-backed bill passed the House 87–9 on February 17, 2026, the Senate 31–3 on March 13, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026. No Republican delegate voted against the bill.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "https://ballotpedia.org/Jordan_Bridges_(West_Virginia)"]),
        claim("jb2", "jordan-bridges", "biblical_marriage", 2, True,
              "Bridges voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Bridges, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
        claim("jb3", "jordan-bridges", "economic_stewardship", 2, True,
              "Bridges voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% and establishing a revenue-triggered mechanism toward a 50% total reduction — one of the largest state income tax cuts in recent U.S. history, returning an estimated $750 million annually to West Virginia taxpayers. The only dissenting votes came from Democrats.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/"]),
    ]),

    # ---------- Jonathan Pinson (WV House Dist. 17, R, Jackson Co., Asst Majority Whip, pastor & Jackson Co. Sheriff's Dept. officer) ----------
    ("jonathan-pinson", "WV", "Delegate", [
        claim("jp1", "jonathan-pinson", "biblical_marriage", 2, True,
              "A Republican pastor and active-duty police officer with the Jackson County Sheriff's Department serving District 17 since December 2020, and currently an Assistant Majority Whip, Pinson voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Pinson, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://ballotpedia.org/Jonathan_Pinson"]),
        claim("jp2", "jonathan-pinson", "self_defense", 0, True,
              "A serving law-enforcement officer (Jackson County Sheriff's Department) and ordained pastor, Pinson voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit. His support as a sitting officer reflects the pro-Second-Amendment posture the bill's backers — including the NRA — sought to demonstrate: that constitutional carry is compatible with law-and-order governance. The bill passed the House 87–9 on February 17, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "https://home.wvlegislature.gov/delegate/jonathan-pinson/"]),
        claim("jp3", "jonathan-pinson", "election_integrity", 0, True,
              "Pinson voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options such as Medicaid cards and utility bills, requiring all voters to present a government-issued photo identification at the polls. The bill passed the House 88–10 on March 28, 2025, with near-unanimous Republican support — no Republican delegate voted against it — and was signed by Governor Patrick Morrisey on April 30, 2025.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://westvirginiawatch.com/2025/05/01/wv-gov-morrisey-signs-voter-photo-id-requirement-dei-ban-and-more-while-issuing-6-vetoes/"]),
    ]),

    # ---------- Jonathan Kyle (WV House Dist. 66, R, Elkins, accounting/Marshall Univ., real estate investor, assumed Dec 2024) ----------
    ("jonathan-kyle", "WV", "Delegate", [
        claim("jky1", "jonathan-kyle", "biblical_marriage", 2, True,
              "A Republican real estate investor and accounting graduate of Marshall University from Elkins, West Virginia, representing District 66 since December 1, 2024, Kyle voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Kyle, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://ballotpedia.org/Jonathan_Kyle"]),
        claim("jky2", "jonathan-kyle", "self_defense", 0, True,
              "Kyle voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit, consistent with the right already extended to those 21 and older. The NRA-backed bill passed the House 87–9 on February 17, 2026, the Senate 31–3 on March 13, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026. No Republican delegate voted against the bill.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
        claim("jky3", "jonathan-kyle", "election_integrity", 0, True,
              "Kyle voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options such as Medicaid cards and utility bills, requiring all voters to present a government-issued photo identification at the polls. The bill passed the House 88–10 on March 28, 2025, with near-unanimous Republican support — no Republican delegate voted against it — and was signed by Governor Patrick Morrisey on April 30, 2025.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://westvirginiawatch.com/2025/05/01/wv-gov-morrisey-signs-voter-photo-id-requirement-dei-ban-and-more-while-issuing-6-vetoes/"]),
    ]),

    # ---------- John Paul Hott II (WV House Dist. 85, R, Petersburg/Grant Co., first elected 2018, not running 2026) ----------
    ("john-paul-hott", "WV", "Delegate", [
        claim("jph1", "john-paul-hott", "biblical_marriage", 2, True,
              "A Petersburg native (born September 23, 1969) representing Grant County (District 85) since his first election in 2018 and currently serving through December 2026, Hott voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Hott, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://ballotpedia.org/John_Paul_Hott_II"]),
        claim("jph2", "john-paul-hott", "self_defense", 0, True,
              "Hott voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit, consistent with the right already extended to those 21 and older. The NRA-backed bill passed the House 87–9 on February 17, 2026, the Senate 31–3 on March 13, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026. No Republican delegate voted against the bill.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
        claim("jph3", "john-paul-hott", "economic_stewardship", 2, True,
              "First elected to the West Virginia House in 2018 and a longtime fixture in Grant County public life (including service on the Petersburg City Council), Hott voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% immediately and establishing a revenue-triggered mechanism toward a 50% total reduction — returning an estimated $750 million annually to West Virginia taxpayers. The only dissenting votes came from Democrats. Governor Jim Justice signed it into law.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/",
               "https://ballotpedia.org/John_Paul_Hott_II"]),
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
