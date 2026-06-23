#!/usr/bin/env python3
"""Enrichment batch 388: 4 sitting U.S. House members with 2 existing claims each.

Targets evidence_curated House members needing additional rubric coverage.
All four are Democrats; claims document positions that score False on the
God-First/America-First rubric (negative scores are wanted for accuracy).

Mix: Jared Moskowitz (FL-23/25), Darren Soto (FL-09),
     Norma Torres (CA-35), Debbie Wasserman Schultz (FL).
2 new claims per candidate, spanning distinct rubric categories from
their existing claims. Total: +8 claims.

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
    # ------------ Jared Moskowitz (FL-23/25, D, US Representative) ------------
    ("jared-moskowitz", "FL", "Representative", [
        claim("jm1", "jared-moskowitz", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act of 2023 (H.R. 12, 118th Congress) on March 30, 2023, which would enshrine abortion as a federal statutory right and bar states from restricting abortion services at any stage — rejecting any personhood or life-at-conception protection. His office states: 'It's time for Congress to codify Roe v. Wade into federal law.'",
              ["https://www.congress.gov/bill/118th-congress/house-bill/12/cosponsors",
               "https://moskowitz.house.gov/resources"]),
        claim("jm2", "jared-moskowitz", "border_immigration", 1, False,
              "Cosponsored the American Dream and Promise Act of 2025 (H.R. 1589) on October 24, 2025, which provides a pathway to lawful permanent residence and citizenship for DACA recipients and Temporary Protected Status holders — directly opposing mandatory deportation of those present illegally.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1589/cosponsors",
               "https://ballotpedia.org/Jared_Moskowitz"]),
    ]),

    # ------------ Darren Soto (FL-09, D, US Representative) ------------
    ("darren-soto", "FL", "Representative", [
        claim("ds2", "darren-soto", "self_defense", 1, False,
              "Holds an NRA F rating from the NRA Political Victory Fund and has been a consistent vote for gun control legislation since entering Congress in 2017, after evolving from an NRA A-rating (2010) to a D in the Florida Senate following Sandy Hook. Wikipedia documents him as 'a reliable vote for gun law reform' since 2017 — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Darren_Soto",
               "https://justfacts.votesmart.org/candidate/evaluations/67618/darren-soto"]),
        claim("ds3", "darren-soto", "sanctity_of_life", 0, False,
              "Has publicly declared 'Women have a right to control their own bodies. Reproductive health care decisions should be between a woman and her doctor — and nobody else,' and condemned the Supreme Court's overturning of Roe v. Wade as setting 'women back 50 years' — rejecting any personhood-from-conception standard.",
              ["https://justfacts.votesmart.org/candidate/key-votes/67618/darren-soto/2/abortion",
               "https://ballotpedia.org/Darren_Soto"]),
    ]),

    # ------------ Norma Torres (CA-35, D, US Representative) ------------
    ("norma-torres", "CA", "Representative", [
        claim("nt3", "norma-torres", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (H.R. 8404, December 8, 2022), which codified federal recognition of same-sex marriages, celebrating the vote: 'Love is love, and with today's vote, Congress has taken the long overdue step to protect marriage equality for millions of Americans' — rejecting the one-man-one-woman definition of marriage.",
              ["https://torres.house.gov/media-center/press-releases/congresswoman-torres-applauds-house-vote-send-respect-marriage-act",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
        claim("nt4", "norma-torres", "self_defense", 1, False,
              "Author of the Multiple Firearm Sales Reporting Modernization Act to help law enforcement track gun trafficking; lead co-sponsor of legislation to track untraceable 'ghost guns'; consistent voter for expanded background checks; and public advocate for 'common sense gun control,' citing her 17 years as a 9-1-1 dispatcher — opposing the rubric's defense of unrestricted firearms rights.",
              ["https://torres.house.gov/media-center/press-releases/rep-torres-calls-common-sense-gun-control-policies",
               "https://ballotpedia.org/Norma_Torres"]),
    ]),

    # ------------ Debbie Wasserman Schultz (FL, D, US Representative) ------------
    ("debbie-wasserman-schultz", "FL", "Representative", [
        claim("dws2", "debbie-wasserman-schultz", "sanctity_of_life", 0, False,
              "Coined the phrase 'war on women' in Congress (2011) to describe pro-life legislation, maintains an active role with Planned Parenthood, and has consistently championed unrestricted abortion access throughout her congressional career — rejecting any recognition of fetal personhood from conception.",
              ["https://en.wikipedia.org/wiki/Debbie_Wasserman_Schultz",
               "https://ballotpedia.org/Debbie_Wasserman_Schultz"]),
        claim("dws3", "debbie-wasserman-schultz", "biblical_marriage", 0, False,
              "A longstanding congressional advocate for same-sex marriage and LGBT rights who voted for the Respect for Marriage Act (December 2022), codifying federal recognition of same-sex unions in law — rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Debbie_Wasserman_Schultz",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
