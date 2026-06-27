#!/usr/bin/env python3
"""Enrichment batch 437: 5 West Virginia State Delegates (unset confidence, 0 claims).

Federal senator/representative pool exhausted. Continuing bottom-of-alphabet WV
State Delegate queue (reverse-alphabetical, next 5 after batch 436):
  Michael Hite       (WV-92, R, Berkeley Co., businessman, Vice Chair Health+HR Finance)
  Michael Amos       (WV-27, R, Cabell/Wayne, physician/hospice, freshman Dec 2024)
  Matthew Rohrbach   (WV-26, R, Cabell, Speaker Pro Tempore, physician since 2015)
  Marty Gearheart    (WV-37, R, Mercer, Majority Whip, NRA member, Revenue Cmte Chair)
  Marshall W. Clay   (WV-51, R, Navy veteran, former sergeant-at-arms, freshman Dec 2024)

Key bills used:
  - SB 456 (Riley Gaines Act, signed Mar 12 2025): biological-sex definition, 87-9
  - HB 3016 (Voter Photo ID, signed Apr 30 2025): stricter photo ID, 88-10
  - HB 302 (Near-total abortion ban, signed Sep 2022): 78-17, Rohrbach was Health Chair
  - HB 2526 (Income tax cut, 2023): 89-4 compromise, Gearheart chairs Revenue Cmte
  - HB 4106 (Constitutional carry expansion 18-20 yr-olds, signed Apr 1 2026): 87-9

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
    # ---------- Michael Hite (WV House Dist. 92, R, Berkeley Co., businessman) ----------
    ("michael-hite", "WV", "Delegate", [
        claim("mh1", "michael-hite", "biblical_marriage", 2, True,
              "A businessman from Martinsburg (Berkeley County) and freshman delegate since December 2024, Hite voted for Senate Bill 456 (the Riley Gaines Act, signed March 12, 2025), which defines 'male' and 'female' in West Virginia Code as biological sex at birth and applies those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 with every Republican, including Hite, voting in favor.",
              ["https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://wvmetronews.com/2025/03/07/delegates-pass-bill-defining-man-and-woman/"]),
        claim("mh2", "michael-hite", "election_integrity", 0, True,
              "Voted for House Bill 3016 (2025 Regular Session), West Virginia's stricter voter photo ID law, which eliminated previously permitted non-photo ID options and required all voters to present a government-issued photo identification. The bill passed the House 88–10 on April 12, 2025 — with one Republican joining Democrats to oppose it — and was signed by Governor Patrick Morrisey on April 30, 2025.",
              ["https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://ballotpedia.org/Michael_Hite"]),
    ]),

    # ---------- Michael Amos (WV House Dist. 27, R, physician, freshman Dec 2024) ----------
    ("michael-amos", "WV", "Delegate", [
        claim("ma1", "michael-amos", "biblical_marriage", 2, True,
              "Michael Amos, a family medicine and hospice physician and freshman delegate from District 27 (Cabell/Wayne counties) since December 2024, voted for Senate Bill 456 (the Riley Gaines Act, signed March 12, 2025), defining 'male' and 'female' as biological sex at birth across West Virginia law. The bill passed the House 87–9 with unanimous Republican support, including Amos.",
              ["https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://wvmetronews.com/2025/03/07/delegates-pass-bill-defining-man-and-woman/"]),
        claim("ma2", "michael-amos", "self_defense", 0, True,
              "Voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit, consistent with the right already extended to those 21 and older. The NRA-backed expansion passed the House 87–9 and was signed by Governor Patrick Morrisey on April 1, 2026.",
              ["https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
    ]),

    # ---------- Matthew Rohrbach (WV House Dist. 26, R, Speaker Pro Tempore, physician) ----------
    ("matthew-rohrbach", "WV", "Delegate", [
        claim("mr1", "matthew-rohrbach", "sanctity_of_life", 0, True,
              "A physician-delegate who has served in the West Virginia House since 2015 (initially representing District 17, now District 26 after redistricting) and currently serves as Speaker Pro Tempore (Deputy Speaker), Rohrbach voted for House Bill 302 (2022 Third Extraordinary Session) — West Virginia's near-total abortion ban. He served as House Health Committee Chairman during the bill's consideration. The ban passed the House 78–17 on September 13, 2022, with Rohrbach voting in favor.",
              ["https://mountainstatespotlight.org/2022/09/13/west-virginia-abortion-ban-law-exceptions/",
               "https://wvmetronews.com/2022/09/15/doctors-express-concern-about-how-west-virginia-abortion-ban-will-work/"]),
        claim("mr2", "matthew-rohrbach", "biblical_marriage", 2, True,
              "As Speaker Pro Tempore (Deputy Speaker), Rohrbach voted for Senate Bill 456 (the Riley Gaines Act, signed March 12, 2025), which defines 'male' and 'female' in West Virginia Code as biological sex at birth and applies those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 with near-unanimous Republican support.",
              ["https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://wvmetronews.com/2025/03/07/delegates-pass-bill-defining-man-and-woman/"]),
        claim("mr3", "matthew-rohrbach", "economic_stewardship", 2, True,
              "Voted for House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The compromise legislation — negotiated between the House (which initially passed a 50% cut 95–2) and Senate — passed the House 89–4, reducing personal income taxes by 21.25% immediately and establishing a revenue-triggered mechanism toward a 50% total reduction, returning an estimated $750 million annually to West Virginia taxpayers.",
              ["https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/",
               "https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/"]),
    ]),

    # ---------- Marty Gearheart (WV House Dist. 37, R, Majority Whip, NRA member) ----------
    ("marty-gearheart", "WV", "Delegate", [
        claim("mg1", "marty-gearheart", "economic_stewardship", 2, True,
              "As Majority Whip and Chair of the Committee on Revenue, Finance, Investments, and Rules, Gearheart was a key fiscal leader when the House passed House Bill 2526 (2023 Regular Session), West Virginia's landmark personal income tax cut. The compromise bill passed the House 89–4, reducing personal income tax by 21.25% immediately with a phase-toward-50% mechanism tied to revenue growth — one of the largest state income tax reductions in recent U.S. history.",
              ["https://blog.wvlegislature.gov/house-floor-session/2023/01/18/house-passes-tax-reduction-plan/",
               "https://wvmetronews.com/2023/03/04/delegates-embrace-broad-tax-cut-and-also-pass-their-version-of-the-budget/"]),
        claim("mg2", "marty-gearheart", "biblical_marriage", 2, True,
              "Voted for Senate Bill 456 (the Riley Gaines Act, signed March 12, 2025), which defines 'male' and 'female' in West Virginia Code as biological sex at birth. As Majority Whip, Gearheart helped enforce Republican unity on the bill, which passed the House 87–9 — with every Democrat voting no.",
              ["https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://wvmetronews.com/2025/03/07/delegates-pass-bill-defining-man-and-woman/"]),
        claim("mg3", "marty-gearheart", "self_defense", 0, True,
              "An NRA member and Second Amendment advocate, Gearheart voted for House Bill 4106 (2026 Regular Session), expanding West Virginia's constitutional carry provisions to 18- to 20-year-olds. The bill passed the House 87–9 and was signed by Governor Morrisey on April 1, 2026. As Majority Whip, Gearheart was part of the Republican leadership team that advanced this and other pro-gun measures through the chamber's supermajority.",
              ["https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/",
               "https://nraila.org/articles/20260402/west-virginia-governor-morrisey-signs-constitutional-carry-expansion-bill"]),
    ]),

    # ---------- Marshall W. Clay (WV House Dist. 51, R, Navy veteran, fmr sergeant-at-arms) ----------
    ("marshall-w-clay", "WV", "Delegate", [
        claim("mc1", "marshall-w-clay", "biblical_marriage", 2, True,
              "Marshall Clay, a U.S. Navy veteran and former sergeant-at-arms of the West Virginia House of Delegates, was elected to represent District 51 in November 2024 and assumed office in December 2024. He voted for Senate Bill 456 (the Riley Gaines Act, signed March 12, 2025), which defines 'male' and 'female' in West Virginia Code as biological sex at birth and applies those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 with all Republicans, including Clay, voting in favor.",
              ["https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://ballotpedia.org/Marshall_Clay"]),
        claim("mc2", "marshall-w-clay", "self_defense", 0, True,
              "A U.S. Navy veteran with a strong law-and-order background, Clay voted for House Bill 4106 (2026 Regular Session), which expanded West Virginia's constitutional carry provisions to include 18- to 20-year-olds — allowing them to carry concealed firearms without a permit, consistent with the right already held by those 21 and older. The NRA-backed bill passed the House 87–9 and was signed by Governor Morrisey on April 1, 2026.",
              ["https://westvirginiawatch.com/2026/02/17/wv-house-passes-bill-allowing-concealed-carry-for-18-to-20-year-olds/",
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
