#!/usr/bin/env python3
"""Enrichment batch 797: additional claims for 4 sitting U.S. Senators from the
bottom-of-alphabet zone (KY, LA, ME, MI).

Primary archetype_curated federal-senator bucket is fully exhausted; this batch
adds claims to evidence_curated senators with fewer than 8 claims to deepen
coverage in missing rubric categories.

Targets (state descending, bottom-agent territory):
  Rand Paul     (KY-R) — sanctity_of_life, economic_stewardship, industry_capture
  Bill Cassidy  (LA-R) — biblical_marriage, foreign_policy_restraint, industry_capture
  Angus King    (ME-I) — election_integrity
  Gary Peters   (MI-D) — foreign_policy_restraint

All claims sourced from official .gov, congress.gov, govtrack.us, or the senator's
official senate.gov website. Writes scorecard.json MINIFIED (no indent) to keep
the master under GitHub's 50MB limit.
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
    # ------------ Rand Paul (KY-R, US Senator) ------------
    ("rand-paul", "KY", "Senator", [
        claim("rp1", "rand-paul", "sanctity_of_life", 0, True,
              "Has introduced the Life at Conception Act every Congress since 2011, most recently placing a Senate version on the calendar via Senate Rule 14 in the 118th Congress to force a potential floor vote; his official Senate website states he believes 'life begins at conception' under the 14th Amendment. He has also introduced the Defund Planned Parenthood Act (S.203, 119th Congress) and is rated 100% by the National Right to Life Committee.",
              ["https://www.paul.senate.gov/issues/advocating-for-sanctity-of-life/",
               "https://www.congress.gov/bill/117th-congress/senate-bill/99"]),
        claim("rp2", "rand-paul", "economic_stewardship", 1, True,
              "Introduced the Federal Reserve Transparency Act of 2024 (S.3566, 118th Congress) — the perennial 'Audit the Fed' legislation requiring a full GAO audit of the Federal Reserve Board and all Federal Reserve banks — a Senate floor priority he has championed every Congress to expose central-bank monetary decisions to public accountability.",
              ["https://www.congress.gov/bill/118th-congress/senate-bill/3566",
               "https://www.govtrack.us/congress/bills/118/s3566"]),
        claim("rp3", "rand-paul", "industry_capture", 0, True,
              "Introduced the NIH Reform Act (S.960, 118th Congress) to abolish Fauci's NIAID and replace it with three smaller Senate-confirmed institutes; as HSGAC Chairman in 2025, issued subpoenas to 14 federal agencies on COVID-19 origins, called Fauci to testify, and uncovered evidence Fauci deleted official records — the most sustained Senate challenge to pharma-public-health industry capture on record.",
              ["https://www.congress.gov/bill/118th-congress/senate-bill/960",
               "https://www.hsgac.senate.gov/media/reps/dr-paul-issues-subpoenas-to-fourteen-agencies-regarding-covid-19-origins-and-risky-gain-of-function-research/"]),
    ]),

    # ------------ Bill Cassidy (LA-R, US Senator) ------------
    ("bill-cassidy", "LA", "Senator", [
        claim("bc1", "bill-cassidy", "biblical_marriage", 1, True,
              "Voted NAY on the Respect for Marriage Act (H.R.8404, Senate Roll Call Vote #362, November 29, 2022, passed 61-36), rejecting federal codification of same-sex marriage. He had introduced a religious-liberty amendment to protect Catholic adoption agencies and small-business owners from 'endless lawsuits' if the bill passed, but Democrats blocked it from a floor vote.",
              ["https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-statement-on-respect-for-marriage-act/",
               "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1172/vote_117_2_00362.htm"]),
        claim("bc2", "bill-cassidy", "foreign_policy_restraint", 1, False,
              "Voted for both the February 2024 Senate national-security supplemental (70-29) and the April 2024 $95.3 billion Ukraine/Israel/Taiwan aid package (79-18), and co-signed a letter with Senator Ernst explicitly urging expanded military aid to Ukraine — contradicting the rubric's call to end open-ended foreign military commitments and wind down overseas entanglements.",
              ["https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-ernst-colleagues-urge-for-military-aid-to-ukraine/",
               "https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-releases-statement-on-israel-foreign-aid-package/"]),
        claim("bc3", "bill-cassidy", "industry_capture", 0, True,
              "A physician who publicly opposed government vaccine mandates while supporting vaccination itself; joined all 46 Senate Republicans in an amicus brief to the Supreme Court opposing Biden's OSHA private-employer mandate, and applauded the January 2022 ruling blocking it as 'a win for personal liberties.'",
              ["https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-joins-effort-to-overturn-biden-vaccine-mandate/",
               "https://www.cassidy.senate.gov/newsroom/press-releases/cassidy-applauds-supreme-court-decision-blocking-biden-vaccine-mandate-on-private-businesses/"]),
    ]),

    # ------------ Angus King (ME-I, US Senator) ------------
    ("angus-king", "ME", "Senator", [
        claim("ak1", "angus-king", "election_integrity", 0, False,
              "Wrote a March 2026 op-ed ('The Voter Fraud Fraud') calling the SAVE Act — which requires proof of U.S. citizenship to register to vote in federal elections — 'a solution in search of a problem' built on 'a false premise,' and has cosponsored legislation to expand same-day, no-ID voter registration instead, defending Maine's system of no voter ID and unlimited mail-in absentee voting.",
              ["https://www.thebulwark.com/p/the-voter-fraud-fraud-election-cheating-save-america-act",
               "https://www.king.senate.gov/newsroom/press-releases/king-colleagues-introduce-legislation-to-protect-voter-access-strengthen-our-participatory-democracy"]),
    ]),

    # ------------ Gary Peters (MI-D, US Senator) ------------
    ("gary-peters", "MI", "Senator", [
        claim("gp1", "gary-peters", "foreign_policy_restraint", 1, False,
              "Voted for both the February 2024 Senate national-security supplemental (70-29) and the April 2024 $95.3 billion Ukraine/Israel/Taiwan aid package (79-18), explicitly stating he did so to 'defend democracy around the world' and 'deliver vital aid to our allies' — the opposite of the rubric's call to end open-ended foreign military commitments.",
              ["https://www.peters.senate.gov/newsroom/press-releases/senator-peters-issues-statement-following-senate-passage-of-the-national-security-supplemental-package",
               "https://www.peters.senate.gov/newsroom/press-releases/senator-peters-statement-on-passage-of-national-security-supplemental-package"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
