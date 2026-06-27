#!/usr/bin/env python3
"""Enrichment batch 436: 5 West Virginia State Delegates (unset confidence, 0 claims).

Federal senator/representative pool exhausted. Continuing bottom-of-alphabet WV
State Delegate queue:
  Shawn Fluharty    (WV-05, D, Minority Whip)
  Sean Hornbuckle   (WV-25, D, Minority Leader)
  Rick Garcia       (WV-76, D, freshman since Dec 2024)
  Patrick Lucas     (WV-24, R, former Asst. Majority Whip 2023-2025)
  Mike Pushkin      (WV-54, D, Chair of WV Democratic Party)

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
    # ---------- Shawn Fluharty (WV House Dist. 5, D, Minority Whip) ----------
    ("shawn-fluharty", "WV", "Delegate", [
        claim("sf1", "shawn-fluharty", "sanctity_of_life", 0, False,
              "A delegate since 2014 (Ohio County), Fluharty was a leading floor voice against WV's near-total abortion ban (HB 302, 2022 Third Extraordinary Session). During House debate he challenged colleagues: 'Do you want to side with child rape victims or child rapists?' — arguing the bill's lack of a rape or incest exception was indefensible. HB 302 passed 77–17 with near-unanimous Democratic opposition, outlawing nearly all abortions in West Virginia with only narrow medical exceptions.",
              ["https://www.cnn.com/2022/07/27/politics/west-virginia-abortion-bill-special-session/index.html",
               "https://www.cnn.com/2022/09/13/politics/west-virginia-state-legislature-abortion-ban/index.html"]),
        claim("sf2", "shawn-fluharty", "biblical_marriage", 2, False,
              "Voted against Senate Bill 456 (the Riley Gaines Act, signed March 12, 2025), which defines 'male' and 'female' in West Virginia Code as biological sex at birth and applies those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 with every Democrat in the chamber voting against it, including Fluharty as House Minority Whip.",
              ["https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://wvmetronews.com/2025/03/07/delegates-pass-bill-defining-man-and-woman/"]),
    ]),

    # ---------- Sean Hornbuckle (WV House Dist. 25, D, Minority Leader) ----------
    ("sean-hornbuckle", "WV", "Delegate", [
        claim("sh1", "sean-hornbuckle", "sanctity_of_life", 0, False,
              "West Virginia's first Black floor leader and Minority Leader since 2023, a delegate since 2014, Hornbuckle co-led House Democratic opposition to WV's near-total abortion ban (HB 302, 2022 Third Extraordinary Session). He was among the Democrats who voted for the rape-and-incest-exception amendment to HB 302 — which failed — and opposed the final bill, which passed 77–17. As Minority Leader he has since publicly called for restoring reproductive rights in the state.",
              ["https://www.cnn.com/2022/09/13/politics/west-virginia-state-legislature-abortion-ban/index.html",
               "https://mountainstatespotlight.org/2022/10/07/the-wv-races-where-abortion-is-on-the-ballot/"]),
        claim("sh2", "sean-hornbuckle", "biblical_marriage", 2, False,
              "Voted against Senate Bill 456 (the Riley Gaines Act, March 2025), which codifies 'male' and 'female' in West Virginia law as biological sex at birth. As Minority Leader, Hornbuckle led the Democratic bloc that unanimously opposed the bill; it passed the House 87–9, with every Democrat voting no.",
              ["https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://wvmetronews.com/2025/03/07/delegates-pass-bill-defining-man-and-woman/"]),
    ]),

    # ---------- Rick Garcia (WV House Dist. 76, D, freshman delegate) ----------
    ("rick-garcia", "WV", "Delegate", [
        claim("rg1", "rick-garcia", "sanctity_of_life", 0, False,
              "As a freshman delegate from Marion County (District 76, since December 2024), Garcia publicly opposed SB 173 (2026 Regular Session), a WV Senate bill prohibiting the prescription or mailing of abortifacients — including mifepristone — into West Virginia. Garcia stated: 'Not only are politicians trying to get into the medical offices and hospitals of the people in the state of West Virginia, but now we're trying to over reach into other states.' He argued existing healthcare access shortfalls in WV are worsened by such restrictions.",
              ["https://westvirginiawatch.com/2026/02/13/senate-passes-bill-prohibiting-abortifacients-being-prescribed-or-mailed-to-west-virginia/",
               "https://ballotpedia.org/Rick_Garcia_(West_Virginia)"]),
        claim("rg2", "rick-garcia", "biblical_marriage", 2, False,
              "Voted against Senate Bill 456 (the Riley Gaines Act, March 2025), which defines 'male' and 'female' in West Virginia Code as biological sex at birth. The bill passed the House 87–9 with every Democrat voting against it, including Garcia as a freshman member of the Democratic minority caucus in his first legislative session.",
              ["https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://wvmetronews.com/2025/03/07/delegates-pass-bill-defining-man-and-woman/"]),
    ]),

    # ---------- Patrick Lucas (WV House Dist. 24, R, former Asst. Majority Whip) ----------
    ("patrick-lucas", "WV", "Delegate", [
        claim("pl1", "patrick-lucas", "sanctity_of_life", 0, True,
              "Publicly supports West Virginia's near-total abortion ban, having stated he 'supports recent legislation banning most abortion procedures.' As a Republican member of the House since December 2022 and former Assistant Majority Whip (2023–2025), Lucas was part of the Republican supermajority that enacted and has defended WV's post-Dobbs abortion restrictions, among the most stringent in the nation.",
              ["https://www.herald-dispatch.com/elections/wv_candidates/candidate-profile-patrick-lucas-house-of-delegates-district-24/article_dd4a715e-90db-11ef-b416-ab7c8a62f7ea.html",
               "https://ballotpedia.org/Patrick_Lucas"]),
        claim("pl2", "patrick-lucas", "economic_stewardship", 2, True,
              "As part of the WV House Republican majority and a former Assistant Majority Whip (2023–2025), Lucas voted for HB 2526 (2023 Regular Session) — West Virginia's landmark personal income tax cut reducing rates by 21.25% immediately and phasing to a 50% total reduction over three years, returning an estimated $750 million annually to WV taxpayers and representing one of the largest state income tax reductions in recent U.S. history.",
              ["https://blog.wvlegislature.gov/headline/2023/01/18/house-passes-tax-reduction-plan/",
               "https://ballotpedia.org/Patrick_Lucas"]),
        claim("pl3", "patrick-lucas", "biblical_marriage", 2, True,
              "Voted for Senate Bill 456 (the Riley Gaines Act, signed March 12, 2025), which defines 'male' and 'female' in West Virginia Code as biological sex at birth and applies those definitions to schools, shelters, and correctional facilities. The bill passed the House 87–9 with near-unanimous Republican support, codifying a biological-sex-only framework that rejects transgender self-identification in those contexts.",
              ["https://westvirginiawatch.com/2025/03/07/bill-defining-men-and-women-passes-wv-house-sent-back-to-senate-for-final-approval/",
               "https://wvmetronews.com/2025/03/07/delegates-pass-bill-defining-man-and-woman/"]),
    ]),

    # ---------- Mike Pushkin (WV House Dist. 54, D, WV Democratic Party Chair) ----------
    ("mike-pushkin", "WV", "Delegate", [
        claim("mp1", "mike-pushkin", "biblical_marriage", 4, False,
              "Lead sponsor of HB 2763 (2025 WV Regular Session), which would add 'sexual orientation' and 'gender identity' as protected categories in West Virginia's Human Rights Act and Fair Housing Act — prohibiting discrimination in employment, housing, and public accommodations on those grounds. Pushkin stated he doesn't believe anyone should be fired or evicted 'simply because of who they are,' framing LGBTQ status as equivalent to race or religion under civil-rights law.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb2763+intr.htm&yr=2025&sesstype=RS&i=2763",
               "https://ballotpedia.org/Mike_Pushkin"]),
        claim("mp2", "mike-pushkin", "christian_liberty", 0, False,
              "Opposed West Virginia's Religious Freedom Restoration Act — legislation that would have allowed businesses to decline service in circumstances conflicting with their sincerely held religious beliefs. Pushkin and WV Democrats argued RFRA would function as a license to discriminate against LGBTQ individuals. His opposition subordinates the free exercise of religious conscience in commerce to LGBTQ anti-discrimination mandates.",
              ["https://mountainstatespotlight.org/2023/02/26/wv-lgbtq-legislature-religious-freedom/",
               "https://ballotpedia.org/Mike_Pushkin"]),
        claim("mp3", "mike-pushkin", "sanctity_of_life", 0, False,
              "Voted against West Virginia's near-total abortion ban (HB 302, 2022 Third Extraordinary Session), which passed 77–17. Pushkin was among Democrats who voted for the rape-and-incest-exception amendment to HB 302 during the July 2022 special session — an amendment that failed — and opposed the final bill. As Chair of the West Virginia Democratic Party, he has publicly called for repealing WV's abortion restrictions.",
              ["https://www.cnn.com/2022/09/13/politics/west-virginia-state-legislature-abortion-ban/index.html",
               "https://ballotpedia.org/Mike_Pushkin"]),
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
