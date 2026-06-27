#!/usr/bin/env python3
"""Enrichment batch 441: 5 West Virginia State Delegates (unset confidence, 0 claims).

Federal senator/representative pool exhausted. Continuing bottom-of-alphabet WV
State Delegate queue (reverse-alphabetical, next 5 after batch 440):
  Joe Ellington   (WV-38, R, Mercer Co., OB-GYN physician, Deputy Speaker, PhD/MD)
  Jimmy Willis    (WV-3, R, Brooke Co., assumed Dec 2022, defeated Phil Diserio)
  Joe Parsons     (WV-16, R, Jackson Co., "Happy Joe", assumed Dec 2024)
  Joe Funkhouser  (WV-98, R, Jefferson Co., attorney, Asst Majority Whip, Bridge Community Church, assumed Oct 2024)
  Jim Butler      (WV-18, R, USMC veteran, small business owner, assumed Dec 2022)

Key bills used:
  - HB 302 (2022 3rd Special Session): near-total abortion ban, signed 9/16/2022, House 69-23
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
    # ---------- Joe Ellington (WV House Dist. 38, R, Mercer Co., OB-GYN physician, Deputy Speaker) ----------
    ("joe-ellington", "WV", "Delegate", [
        claim("je1", "joe-ellington", "sanctity_of_life", 0, True,
              "An obstetrician-gynecologist and Fellow of the American College of Obstetricians and Gynecologists representing District 38 (Mercer County) as Deputy Speaker of the West Virginia House of Delegates, Ellington testified before the House Health Committee in July 2022 — after Dobbs returned abortion policy to the states — that life begins at conception, stating: 'If you're talking about a new fetus, a new human life, I would say conception.' He then voted for House Bill 302 (2022, Third Special Session), West Virginia's near-total abortion ban, which outlaws abortion except in cases of rape or incest (up to 8 weeks for adults, 14 weeks for minors with law-enforcement report) and medical emergencies. The bill passed the House 69–23 and was signed into law by Governor Jim Justice on September 16, 2022. Ellington's yes vote — cast as both a practicing OB-GYN and a senior House leader — carries unusual medical-professional weight in affirming that life begins at fertilization.",
              ["https://wvmetronews.com/2022/07/25/west-virginia-delegates-start-considering-abortion-bill/",
               "https://blog.wvlegislature.gov/headline/2022/09/13/legislature-passes-abortion-ban-adjourns-sine-die/",
               "https://ballotpedia.org/Joe_Ellington"]),
        claim("je2", "joe-ellington", "biblical_marriage", 2, True,
              "Ellington voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities to reject transgender ideology in law. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Ellington, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://home.wvlegislature.gov/delegate/joe-ellington/"]),
        claim("je3", "joe-ellington", "economic_stewardship", 2, True,
              "Ellington voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut, which passed the House 89–4 on final concurrence on March 4, 2023. The legislation reduced personal income taxes by 21.25% immediately and established a revenue-triggered mechanism toward a 50% total reduction — returning an estimated $750 million annually to West Virginia taxpayers. The only dissenting votes came from Democrats. Governor Jim Justice signed it into law, marking one of the largest state income tax reductions in recent U.S. history.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/"]),
    ]),

    # ---------- Jimmy Willis (WV House Dist. 3, R, Brooke Co., assumed Dec 2022, defeated Phil Diserio) ----------
    ("jimmy-willis", "WV", "Delegate", [
        claim("jw1", "jimmy-willis", "biblical_marriage", 2, True,
              "A Republican representing District 3 (Brooke County) since December 1, 2022 — having defeated incumbent Democrat Phil Diserio in the November 2022 general election — Willis voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth, applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Willis, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://ballotpedia.org/Jimmy_Willis"]),
        claim("jw2", "jimmy-willis", "election_integrity", 0, True,
              "Willis voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options such as Medicaid cards and utility bills, requiring all voters to present a government-issued photo identification at the polls. The bill passed the House 88–10 on March 28, 2025, with near-unanimous Republican support — no Republican delegate voted against it — and was signed by Governor Patrick Morrisey on April 30, 2025.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://westvirginiawatch.com/2025/05/01/wv-gov-morrisey-signs-voter-photo-id-requirement-dei-ban-and-more-while-issuing-6-vetoes/"]),
        claim("jw3", "jimmy-willis", "economic_stewardship", 2, True,
              "In his first session after assuming office on December 1, 2022, Willis voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% immediately and establishing a revenue-triggered mechanism toward a 50% total reduction — returning an estimated $750 million annually to West Virginia taxpayers. The only dissenting votes came from Democrats. Governor Jim Justice signed it into law.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/"]),
    ]),

    # ---------- Joe Parsons (WV House Dist. 16, R, Jackson Co., "Happy Joe", assumed Dec 2024) ----------
    ("joe-parsons", "WV", "Delegate", [
        claim("jp1", "joe-parsons", "self_defense", 0, True,
              "A Republican representing District 16 (Jackson County) since December 1, 2024 — winning election on November 5, 2024 after prevailing in a three-way Republican primary — Parsons voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds, allowing them to carry concealed firearms without a permit. The NRA-backed bill passed the House 87–9 on February 17, 2026, the Senate 31–3 on March 13, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026. No Republican delegate voted against the bill.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "https://ballotpedia.org/Joe_Parsons_(West_Virginia)"]),
        claim("jp2", "joe-parsons", "biblical_marriage", 2, True,
              "Parsons voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Parsons, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
        claim("jp3", "joe-parsons", "election_integrity", 0, True,
              "Parsons voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options such as Medicaid cards and utility bills, requiring all voters to present a government-issued photo identification at the polls. The bill passed the House 88–10 on March 28, 2025, with near-unanimous Republican support — no Republican delegate voted against it — and was signed by Governor Patrick Morrisey on April 30, 2025.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://westvirginiawatch.com/2025/05/01/wv-gov-morrisey-signs-voter-photo-id-requirement-dei-ban-and-more-while-issuing-6-vetoes/"]),
    ]),

    # ---------- Joe Funkhouser (WV House Dist. 98, R, Jefferson Co., attorney, Asst Majority Whip, Bridge Community Church) ----------
    ("joe-funkhouser", "WV", "Delegate", [
        claim("jf1", "joe-funkhouser", "self_defense", 0, True,
              "A fourth-generation Jefferson County resident and civil litigation attorney appointed to the West Virginia House of Delegates District 98 by Governor Jim Justice on October 16, 2024 (to replace Paul Espinosa), and serving as Assistant Majority Whip since election in November 2024, Funkhouser voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit. The NRA-backed bill passed the House 87–9 on February 17, 2026, the Senate 31–3 on March 13, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026. No Republican delegate voted against the bill.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "https://ballotpedia.org/Joe_Funkhouser"]),
        claim("jf2", "joe-funkhouser", "biblical_marriage", 2, True,
              "A member of Bridge Community Church in Jefferson County and a civil litigation attorney by profession, Funkhouser voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Funkhouser, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://home.wvlegislature.gov/delegate/joe-funkhouser/"]),
        claim("jf3", "joe-funkhouser", "election_integrity", 0, True,
              "Funkhouser voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options such as Medicaid cards and utility bills, requiring all voters to present a government-issued photo identification at the polls. The bill passed the House 88–10 on March 28, 2025, with near-unanimous Republican support — no Republican delegate voted against it — and was signed by Governor Patrick Morrisey on April 30, 2025.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://westvirginiawatch.com/2025/05/01/wv-gov-morrisey-signs-voter-photo-id-requirement-dei-ban-and-more-while-issuing-6-vetoes/"]),
    ]),

    # ---------- Jim Butler (WV House Dist. 18, R, USMC veteran, small business owner, assumed Dec 2022) ----------
    ("jim-butler", "WV", "Delegate", [
        claim("jbu1", "jim-butler", "self_defense", 0, True,
              "A United States Marine Corps veteran and owner of a small excavation, logging, and vintage vehicle restoration business representing District 18 since December 1, 2022 — having defeated incumbent Republican Johnnie Wamsley II in the primary before winning the general election — Butler voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds. His background as a Marine and small business owner in a rural district underscores his support for the Second Amendment right to carry without a government permit. The NRA-backed bill passed the House 87–9 on February 17, 2026, the Senate 31–3 on March 13, 2026, and was signed by Governor Patrick Morrisey on April 1, 2026. No Republican delegate voted against the bill.",
              ["https://legiscan.com/WV/bill/HB4106/2026",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill",
               "https://ballotpedia.org/Jim_Butler_(West_Virginia)"]),
        claim("jbu2", "jim-butler", "biblical_marriage", 2, True,
              "Butler voted for Senate Bill 456 (2025, the Riley Gaines Act), which defines 'male,' 'female,' and 'sex' in West Virginia Code as biological sex at birth — applying those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 on March 11, 2025, with all nine opposing votes cast by Democrats; every Republican delegate, including Butler, voted in favor. Governor Patrick Morrisey signed the Riley Gaines Act into law on March 12, 2025.",
              ["https://wvmetronews.com/2025/03/12/morrisey-signs-bill-defining-man-and-woman-into-law/",
               "https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/"]),
        claim("jbu3", "jim-butler", "economic_stewardship", 2, True,
              "As a small business owner in the excavation, logging, and vehicle restoration trades, Butler voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The legislation passed the House 89–4 on final concurrence on March 4, 2023, reducing personal income taxes by 21.25% immediately and establishing a revenue-triggered mechanism toward a 50% total reduction — returning an estimated $750 million annually to West Virginia taxpayers, with direct benefit to the small business community. The only dissenting votes came from Democrats. Governor Jim Justice signed it into law.",
              ["https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/",
               "https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/",
               "https://ballotpedia.org/Jim_Butler_(West_Virginia)"]),
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
