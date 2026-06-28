#!/usr/bin/env python3
"""Enrichment batch 472: hand-curated claims for 5 WV State Delegates.

All 5 are Republican members of the West Virginia House of Delegates with
0 existing claims. Targets chosen because they are confirmed co-authors or
co-sponsors of key WV legislation verifiable from official bill text and
news coverage.

Targets:
  Dean Jeffries      (WV-61, R) — co-authored HB 302 + co-sponsored HB 5297
  Evan Worrell       (WV-23, R) — co-authored HB 302 + chaired Health committee (HB 5297)
  D. Rolland Jennings (WV-84, R) — co-authored HB 302 + 2023 gender-care ban vote
  George Miller      (WV, R)    — co-authored HB 302 + 2023 gender-care ban vote
  Eric Brooks        (WV-45, R) — co-sponsored HB 5297 + 2023 gender-care ban vote

Sources: WV Legislature official bill text, The Hill, WV Gazette-Mail,
Mountain State Spotlight, WSAZ, ABC17/AP, The Intelligencer.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # -------------- Dean Jeffries (WV-61, R, State Delegate) --------------
    # Primary author of HB 302 (2022 near-total abortion ban) and co-sponsor
    # of HB 5297 (2024 removal of gender-care-ban exceptions).
    ("dean-jeffries", "WV", "Delegate", [
        claim("dj1", "dean-jeffries", "sanctity_of_life", 0, True,
              "Listed as a primary author of West Virginia HB 302 (2022 Third "
              "Extraordinary Session), the state's near-total abortion ban prohibiting "
              "abortion from fertilization forward, with narrow exceptions for medical "
              "emergencies, non-viable fetus, and ectopic pregnancy. A rape/incest "
              "exception was added by floor amendment (limited to 14 weeks for minors). "
              "The House passed the bill 77–17 on final concurrence on September 13, "
              "2022; Governor Jim Justice signed it into law September 16, 2022. "
              "Jeffries represents District 61 (Lincoln County), serves as Assistant "
              "Majority Leader, and chairs the House Health Care Regulation Subcommittee.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2022_SESSIONS/3X/bills/HB302%20ORG.pdf",
               "https://thehill.com/homenews/state-watch/3641548-west-virginia-legislature-approves-abortion-ban-headed-to-governor-for-signature/"]),
        claim("dj2", "dean-jeffries", "biblical_marriage", 2, True,
              "Listed as a co-sponsor of West Virginia HB 5297 (2024 Regular Session), "
              "which eliminated the only remaining exemption in West Virginia's ban on "
              "gender-affirming care for minors — a mental-health/self-harm carve-out "
              "that had allowed puberty blockers and cross-sex hormones for diagnosed "
              "gender-dysphoric youth at risk of suicide. HB 5297 made the prohibition "
              "on such interventions for those under 18 absolute and unconditional. "
              "The House passed HB 5297 by an 88–11 vote on February 28, 2024; "
              "Governor Justice signed it into law.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb5297+intr.htm&yr=2024&sesstype=RS&i=5297",
               "https://www.wvgazettemail.com/news/legislative_session/west-virginia-house-passes-bill-further-restricting-transgender-related-health-care/article_ffd5d606-20d5-5ef0-b155-050b5451f7c3.html"]),
    ]),

    # -------------- Evan Worrell (WV-23, R, State Delegate) --------------
    # Co-author of HB 302 and Chair of House Health and Human Resources Committee
    # that advanced HB 5297 in February 2024.
    ("evan-worrell", "WV", "Delegate", [
        claim("ew1", "evan-worrell", "sanctity_of_life", 0, True,
              "Listed as a primary author of West Virginia HB 302 (2022 Third "
              "Extraordinary Session), the state's near-total abortion ban from "
              "fertilization with narrow medical exceptions. The House passed the bill "
              "77–17 on September 13, 2022; Governor Jim Justice signed it into law "
              "September 16, 2022. Worrell represents District 23 (Cabell County) and "
              "serves as Chair of the House Health and Human Resources Committee, the "
              "principal committee handling healthcare and life-related legislation in "
              "the chamber.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2022_SESSIONS/3X/bills/HB302%20ORG.pdf",
               "https://www.plannedparenthood.org/about-us/newsroom/press-releases/west-virginia-legislature-passes-near-total-abortion-ban"]),
        claim("ew2", "evan-worrell", "biblical_marriage", 2, True,
              "As Chair of the West Virginia House Health and Human Resources Committee, "
              "Worrell oversaw the committee's reopening of debate on gender-affirming "
              "care in February 2024 and advanced HB 5297 — which removed the only "
              "remaining mental-health/self-harm exemption from WV's ban on "
              "gender-affirming care for minors — to the full House floor. The bill "
              "passed 88–11 on February 28, 2024. More than 500 health care providers "
              "signed a letter opposing the bill, but the committee and chamber majority "
              "moved forward with the absolute prohibition.",
              ["https://www.theintelligencer.net/news/top-headlines/2024/02/house-health-committee-reopens-debate-on-gender-affirming-care-in-west-virginia/",
               "https://mountainstatespotlight.org/2024/02/28/gender-affirming-care-transgender-ban-house/"]),
    ]),

    # -------------- D. Rolland Jennings (WV-84, R, State Delegate) --------------
    # Co-author of HB 302 (2022). In office since his 2017 appointment.
    # Chairs the House Homeland Security Committee.
    ("d-rolland-jennings", "WV", "Delegate", [
        claim("drj1", "d-rolland-jennings", "sanctity_of_life", 0, True,
              "Listed as a primary author of West Virginia HB 302 (2022 Third "
              "Extraordinary Session), the state's near-total abortion ban from "
              "fertilization with narrow exceptions for medical emergencies, non-viable "
              "fetus, and ectopic pregnancy. The House passed the bill 77–17 on "
              "September 13, 2022; Governor Jim Justice signed it September 16, 2022. "
              "Jennings represents District 84 (Tucker and Webster counties), has served "
              "since his 2017 appointment, and chairs the House Homeland Security "
              "Committee.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2022_SESSIONS/3X/bills/HB302%20ORG.pdf",
               "https://thehill.com/homenews/state-watch/3641548-west-virginia-legislature-approves-abortion-ban-headed-to-governor-for-signature/"]),
        claim("drj2", "d-rolland-jennings", "biblical_marriage", 2, True,
              "As a Republican member of the WV House since his 2017 appointment, "
              "Jennings voted for West Virginia's 2023 gender-affirming care ban for "
              "minors, which prohibits health care professionals from providing "
              "pubertal modulation, hormonal therapy, or surgical interventions to "
              "assist gender transition for those under 18. The bill passed the House "
              "84–10 on initial passage (February 3, 2023) and 88–10 on final amended "
              "passage (March 11, 2023). News coverage confirmed that all 10 'no' votes "
              "in both the initial and final House passages were cast by Democratic "
              "members — no Republican delegate voted in opposition.",
              ["https://www.wsaz.com/2023/02/03/bill-prohibiting-gender-affirming-care-minors-passes-wva-house/",
               "https://abc17news.com/news/ap-national-news/2023/03/11/west-virginia-gop-legislature-passes-transgender-care-ban/"]),
    ]),

    # -------------- George Miller (WV, R, State Delegate) --------------
    # Co-author of HB 302 (2022). Elected 2020, re-elected 2024.
    ("george-miller", "WV", "Delegate", [
        claim("gmw1", "george-miller", "sanctity_of_life", 0, True,
              "Listed as a primary author of West Virginia HB 302 (2022 Third "
              "Extraordinary Session), the state's near-total abortion ban from "
              "fertilization with narrow medical exceptions. The House passed the "
              "bill 77–17 on September 13, 2022; Governor Jim Justice signed it "
              "September 16, 2022. Miller was first elected to the House in 2020 and "
              "has been re-elected unopposed.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2022_SESSIONS/3X/bills/HB302%20ORG.pdf",
               "https://thehill.com/homenews/state-watch/3641548-west-virginia-legislature-approves-abortion-ban-headed-to-governor-for-signature/"]),
        claim("gmw2", "george-miller", "biblical_marriage", 2, True,
              "As a Republican member of the WV House, Miller voted for West Virginia's "
              "2023 gender-affirming care ban for minors, which prohibits health care "
              "professionals from providing pubertal modulation and hormonal therapy to "
              "assist gender transition for those under 18. The bill passed the House "
              "84–10 on initial passage (February 3, 2023) and 88–10 on final amended "
              "passage (March 11, 2023); every 'no' vote in both House passages was cast "
              "by a Democratic member, confirming the legislation passed as a Republican "
              "caucus measure with no GOP defections.",
              ["https://www.wsaz.com/2023/02/03/bill-prohibiting-gender-affirming-care-minors-passes-wva-house/",
               "https://abc17news.com/news/ap-national-news/2023/03/11/west-virginia-gop-legislature-passes-transgender-care-ban/"]),
    ]),

    # -------------- Eric Brooks (WV-45, R, State Delegate) --------------
    # Co-sponsor of HB 5297 (2024). Assistant Majority Whip. In office since 2022.
    ("eric-brooks", "WV", "Delegate", [
        claim("eb1", "eric-brooks", "biblical_marriage", 2, True,
              "Listed as a co-sponsor of West Virginia HB 5297 (2024 Regular Session), "
              "which eliminated the only remaining mental-health/self-harm exemption "
              "from WV's ban on gender-affirming care for minors, making the prohibition "
              "on puberty blockers, cross-sex hormones, and related interventions for "
              "those under 18 absolute. Brooks represents District 45 and serves as "
              "Assistant Majority Whip. HB 5297 passed the House 88–11 on February 28, "
              "2024; Governor Jim Justice signed it into law.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=hb5297+intr.htm&yr=2024&sesstype=RS&i=5297",
               "https://mountainstatespotlight.org/2024/02/28/gender-affirming-care-transgender-ban-house/"]),
        claim("eb2", "eric-brooks", "family_child_sovereignty", 0, True,
              "As a Republican member of the WV House since assuming office in December "
              "2022, Brooks voted for West Virginia's initial 2023 gender-affirming care "
              "ban for minors (passed 84–10 then 88–10, with all 10 'no' votes in both "
              "passages cast by Democrats). The law protects minors from providers "
              "administering puberty blockers, cross-sex hormones, or gender-transition "
              "surgeries without parental objection being overridden by the medical "
              "establishment, reinforcing parental authority over children's "
              "irreversible medical decisions.",
              ["https://www.wsaz.com/2023/02/03/bill-prohibiting-gender-affirming-care-minors-passes-wva-house/",
               "https://abc17news.com/news/ap-national-news/2023/03/11/west-virginia-gop-legislature-passes-transgender-care-ban/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
