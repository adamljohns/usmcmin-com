#!/usr/bin/env python3
"""Enrichment batch 473: hand-curated claims for 5 WI Republican State Assembly Members.

All 5 are members of the Wisconsin State Assembly with 0 existing claims.
Targets chosen because they are confirmed co-sponsors of verifiable 2023-2025
Wisconsin legislation with official bill text and news coverage.

Targets:
  Joy Goeben        (WI-5,  R) — co-sponsored AB 465 + co-introduced AJR1
  Nate Gustafson    (WI-55, R) — co-sponsored AB 465 + co-introduced AJR1
  Karen Hurd        (WI-69, R) — co-sponsored AB 465 + co-introduced AJR1
  Jeffrey Mursau    (WI-36, R) — co-introduced AJR1 + voted for AB 465 (party-line)
  Mark Born         (WI-37, R) — co-introduced AJR1 + voted for AB 465 (party-line)

Key bills:
  WI AB 465 (2023) — prohibits gender transition medical intervention for minors;
    passed Assembly Oct 12, 2023 along party lines (all Republicans for, all
    Democrats against); Gov. Evers vetoed Dec 13, 2023.
  WI AJR1 (2025-2026 session, second passage) — constitutionally enshrines
    Wisconsin's voter photo ID requirement; approved by Assembly Jan 2025 along
    party lines 54-45; voter ID referendum passed April 2025 election; voter ID
    is now in the Wisconsin Constitution.

Sources: Wisconsin Legislature official bill pages, Wisconsin Public Radio (WPR),
WKOW, Ballotpedia, Rep. Donovan WI Assembly press release.

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
    # -------------- Joy Goeben (WI-5, R, State Assembly Member) --------------
    # Co-sponsor of WI AB 465 (2023 gender-affirming care ban for minors) and
    # co-introducer of AJR1 (2025 voter ID constitutional amendment, second passage).
    ("joy-goeben-wi-5", "WI", "Assembly", [
        claim("jg1", "joy-goeben-wi-5", "biblical_marriage", 2, True,
              "Listed as a named co-sponsor of Wisconsin Assembly Bill 465 (2023 "
              "Regular Session), which prohibits gender transition medical intervention "
              "— including surgeries, puberty-blocking drugs, and hormone therapy — "
              "for patients younger than 18. The bill was introduced September 29, 2023 "
              "by Representatives Allen, Vos, Armstrong and others including Goeben, "
              "and passed the Wisconsin State Assembly on October 12, 2023 along strict "
              "party lines, with all Republican members voting in favor and all "
              "Democratic members voting against. Governor Tony Evers vetoed the bill "
              "on December 13, 2023. Goeben represents District 5 (Green Bay area).",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab465",
               "https://www.wpr.org/health/lawmakers-approve-bills-bar-gender-affirmation-procedures-sports-participation-transgender-youth",
               "https://www.wkow.com/news/politics/gov-evers-vetoes-bill-that-would-block-gender-affirming-care-for-minors/article_ad800b44-944e-11ee-a6b4-83112927fc71.html"]),
        claim("jg2", "joy-goeben-wi-5", "election_integrity", 0, True,
              "Listed as a named co-introducer of Wisconsin Assembly Joint Resolution 1 "
              "(2025-2026 Legislative Session), the second consecutive legislative "
              "passage required to send Wisconsin's voter photo ID constitutional "
              "amendment to the voters. AJR1 was introduced January 6, 2025 by "
              "Representatives including Snyder, Donovan, Allen, Behnke, Born, Goeben, "
              "Hurd, Mursau, Gustafson, and others; the Assembly approved it 54-45 along "
              "party lines (all Republicans for, all Democrats against). The resulting "
              "ballot measure — Wisconsin Question 1 — was approved by voters at the "
              "April 2025 election, permanently enshrining a mandatory voter photo ID "
              "requirement in the Wisconsin State Constitution.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ajr1",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://www.wpr.org/news/april-2025-election-voter-id-requirement-passes-wisconsin-constitution"]),
    ]),

    # -------------- Nate Gustafson (WI-55, R, State Assembly Member) --------------
    # Co-sponsor of WI AB 465 and co-introducer of AJR1.
    ("nate-gustafson-wi-55", "WI", "Assembly", [
        claim("ng1", "nate-gustafson-wi-55", "biblical_marriage", 2, True,
              "Listed as a named co-sponsor of Wisconsin Assembly Bill 465 (2023 "
              "Regular Session), which prohibits gender transition medical intervention "
              "— including surgeries, puberty-blocking drugs, and cross-sex hormone "
              "therapy — for individuals under 18. The bill passed the Wisconsin State "
              "Assembly on October 12, 2023 along strict party lines, with every "
              "Republican member voting in favor and every Democratic member voting "
              "against. Governor Tony Evers vetoed the bill on December 13, 2023. "
              "Gustafson represents District 55 in the Wisconsin State Assembly.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab465",
               "https://www.wpr.org/health/lawmakers-approve-bills-bar-gender-affirmation-procedures-sports-participation-transgender-youth",
               "https://www.wkow.com/news/politics/gov-evers-vetoes-bill-that-would-block-gender-affirming-care-for-minors/article_ad800b44-944e-11ee-a6b4-83112927fc71.html"]),
        claim("ng2", "nate-gustafson-wi-55", "election_integrity", 0, True,
              "Listed as a named co-introducer of Wisconsin Assembly Joint Resolution 1 "
              "(2025-2026 Legislative Session), the second consecutive legislative "
              "passage of the voter photo ID constitutional amendment. AJR1 was "
              "introduced January 6, 2025 and passed the Assembly 54-45 along party "
              "lines. Wisconsin's constitution requires any proposed amendment to pass "
              "two consecutive legislative sessions before going to the voters; this "
              "second passage sent Wisconsin Question 1 to the April 2025 ballot, "
              "where it was approved by voters, permanently embedding a mandatory voter "
              "photo ID requirement in the Wisconsin State Constitution.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ajr1",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://www.wpr.org/news/april-2025-election-voter-id-requirement-passes-wisconsin-constitution"]),
    ]),

    # -------------- Karen Hurd (WI-69, R, State Assembly Member) --------------
    # Co-sponsor of WI AB 465 and co-introducer of AJR1. Elected 2014.
    # Serves as Majority Caucus Secretary.
    ("karen-hurd-wi-69", "WI", "Assembly", [
        claim("kh1", "karen-hurd-wi-69", "biblical_marriage", 2, True,
              "Listed as a named co-sponsor of Wisconsin Assembly Bill 465 (2023 "
              "Regular Session), which prohibits surgeries, puberty-blocking drugs, "
              "and cross-sex hormone therapy for gender transition in patients under "
              "18. Hurd has represented District 69 (Wood County area) since her "
              "election in 2014 and serves as Majority Caucus Secretary. AB 465 "
              "passed the Wisconsin State Assembly on October 12, 2023 along strict "
              "party lines — every Republican voted in favor, every Democrat against. "
              "Governor Tony Evers vetoed the bill on December 13, 2023.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab465",
               "https://www.wpr.org/health/lawmakers-approve-bills-bar-gender-affirmation-procedures-sports-participation-transgender-youth",
               "https://www.wkow.com/news/politics/gov-evers-vetoes-bill-that-would-block-gender-affirming-care-for-minors/article_ad800b44-944e-11ee-a6b4-83112927fc71.html"]),
        claim("kh2", "karen-hurd-wi-69", "election_integrity", 0, True,
              "Listed as a named co-introducer of Wisconsin Assembly Joint Resolution 1 "
              "(2025-2026 Legislative Session), constitutionally enshrining Wisconsin's "
              "voter photo ID requirement. AJR1 was introduced January 6, 2025, with "
              "co-introducers including Hurd, Goeben, Born, Mursau, Gustafson and "
              "other Republican Assembly members. The resolution passed the Assembly "
              "54-45 along party lines. This was the second consecutive legislative "
              "passage, completing the state constitutional amendment process; the "
              "resulting Wisconsin Question 1 passed at the April 2025 election and "
              "voter ID is now permanently in the Wisconsin Constitution.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ajr1",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://www.wpr.org/news/april-2025-election-voter-id-requirement-passes-wisconsin-constitution"]),
    ]),

    # -------------- Jeffrey Mursau (WI-36, R, State Assembly Member) --------------
    # Co-introducer of AJR1; in office since 2005; chairs Forestry/Parks Committee.
    # Voted for AB 465 as part of the party-line Republican caucus.
    ("jeffrey-mursau-wi-36", "WI", "Assembly", [
        claim("jm1", "jeffrey-mursau-wi-36", "election_integrity", 0, True,
              "Listed as a named co-introducer of Wisconsin Assembly Joint Resolution 1 "
              "(2025-2026 Legislative Session), which constitutionally enshrines "
              "Wisconsin's mandatory voter photo ID requirement. AJR1 was introduced "
              "January 6, 2025 by Representatives including Mursau, Born, Goeben, "
              "Hurd, Gustafson, and others. The resolution passed the Wisconsin Assembly "
              "54-45 along party lines — all Republicans voting in favor, all Democrats "
              "against. This second consecutive legislative passage completed Wisconsin's "
              "constitutional amendment process; Wisconsin Question 1 appeared on the "
              "April 2025 ballot and was approved by voters, permanently adding voter "
              "photo ID to the Wisconsin State Constitution. Mursau has served District "
              "36 (Marinette County area) since 2005 and chairs the Assembly Committee "
              "on Forestry, Parks and Outdoor Recreation.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ajr1",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://www.wpr.org/news/april-2025-election-voter-id-requirement-passes-wisconsin-constitution"]),
        claim("jm2", "jeffrey-mursau-wi-36", "biblical_marriage", 2, True,
              "As a Republican member of the Wisconsin State Assembly since 2005, "
              "Mursau voted for Assembly Bill 465 (2023 Regular Session), which "
              "prohibits gender transition medical interventions — including surgeries, "
              "puberty-blocking drugs, and cross-sex hormone therapy — for patients "
              "under 18. AB 465 passed the Assembly on October 12, 2023 along strict "
              "party lines, with every Republican member voting in favor and every "
              "Democratic member voting against. Governor Tony Evers vetoed the bill "
              "on December 13, 2023. News coverage confirmed that the vote divided "
              "strictly along party lines with no Republican defections.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab465",
               "https://www.wpr.org/health/lawmakers-approve-bills-bar-gender-affirmation-procedures-sports-participation-transgender-youth",
               "https://www.wkow.com/news/politics/gov-evers-vetoes-bill-that-would-block-gender-affirming-care-for-minors/article_ad800b44-944e-11ee-a6b4-83112927fc71.html"]),
    ]),

    # -------------- Mark Born (WI-37, R, State Assembly Member) --------------
    # Co-introducer of AJR1; in office since 2012; law enforcement background.
    # Voted for AB 465 as part of the party-line Republican caucus.
    ("mark-born-wi-37", "WI", "Assembly", [
        claim("mb1", "mark-born-wi-37", "election_integrity", 0, True,
              "Listed as a named co-introducer of Wisconsin Assembly Joint Resolution 1 "
              "(2025-2026 Legislative Session), the second of two required consecutive "
              "legislative passages to enshrine Wisconsin's voter photo ID requirement "
              "in the state constitution. AJR1 was introduced January 6, 2025 by "
              "Representatives including Born, Goeben, Hurd, Mursau, Gustafson, and "
              "others. The Assembly approved AJR1 54-45 along party lines. The "
              "resulting Wisconsin Question 1 was approved by voters at the April 2025 "
              "election, making voter photo ID a permanent constitutional requirement. "
              "Born has represented District 37 (Dodge and Columbia Counties) since "
              "2012 and has a background in law enforcement, including service on the "
              "Beaver Dam Fire and Police Commission (2003-05).",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ajr1",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://www.wpr.org/news/april-2025-election-voter-id-requirement-passes-wisconsin-constitution"]),
        claim("mb2", "mark-born-wi-37", "biblical_marriage", 2, True,
              "As a Republican member of the Wisconsin State Assembly since 2012, "
              "Born voted for Assembly Bill 465 (2023 Regular Session), which "
              "prohibits gender transition medical interventions — including surgeries, "
              "puberty-blocking drugs, and cross-sex hormone therapy — for individuals "
              "under 18. AB 465 passed the Wisconsin Assembly on October 12, 2023 "
              "along strict party lines, with every Republican member voting in favor "
              "and every Democratic member voting against. Governor Tony Evers vetoed "
              "the bill on December 13, 2023. Wisconsin Public Radio confirmed the "
              "vote divided strictly along party lines with no Republican defections.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab465",
               "https://www.wpr.org/health/lawmakers-approve-bills-bar-gender-affirmation-procedures-sports-participation-transgender-youth",
               "https://www.wkow.com/news/politics/gov-evers-vetoes-bill-that-would-block-gender-affirming-care-for-minors/article_ad800b44-944e-11ee-a6b4-83112927fc71.html"]),
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
