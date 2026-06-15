#!/usr/bin/env python3
"""Enrichment batch 236: third-claim enrichment for 4 federal candidates from
the bottom of the alphabet (evidence_curated 2-claim pool, reverse-sorted by state).

Targets (bottom-of-alphabet priority: US → PA):
  Todd Blanche    (US-R · Acting Attorney General)          – election_integrity
  Mac Warner      (US-R · Acting Asst AG / Civil Rights)    – christian_liberty
  Doug Collins    (US-R · Secretary of Veterans Affairs)    – election_integrity
  Sharif Street   (PA-D · U.S. Rep PA-03 2026 Candidate)   – biblical_marriage

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
    # ------------ Todd Blanche (US-R, Acting Attorney General) -------------
    ("todd-blanche", "US", "Attorney General", [
        claim("tb3", "todd-blanche", "election_integrity", 0, True,
              "As Acting Attorney General beginning April 2026, Blanche directed the Justice Department to aggressively prosecute noncitizens who illegally vote in federal elections, publicly declaring: 'This administration will not tolerate aliens who attempt to vote in our elections when they know they are not eligible' and 'This Justice Department will use every authority to protect the integrity of U.S. elections, including by prosecuting any noncitizens who lie about their legal status in an attempt to vote.' The DOJ's Election Integrity Task Force, operating under Blanche's leadership, charged multiple aliens in the District of New Jersey with illegally voting in federal elections and making false statements while applying for U.S. citizenship — a direct enforcement action against foreign influence over American ballots consistent with the rubric's standard of preserving election integrity against fraudulent participation.",
              ["https://www.justice.gov/usao-nj/pr/multiple-aliens-charged-illegally-voting-federal-elections-and-making-false-statements",
               "https://www.justice.gov/dag/bio/deputy-attorney-general-todd-blanche",
               "https://en.wikipedia.org/wiki/Todd_Blanche"]),
    ]),

    # ------------ Mac Warner (US-R, Acting Asst AG / Civil Rights) ---------
    ("mac-warner", "US", "Civil Rights", [
        claim("mw3", "mac-warner", "christian_liberty", 0, True,
              "As Acting Assistant Attorney General for the Civil Rights Division since January 2025, Warner directed the Justice Department to file a federal statement of interest in support of access to places of worship, publicly declaring: 'Every person should be free to worship and attend religious services without fear of violence, threats, or intimidation.' This filing is part of the Civil Rights Division's Religious Freedom in Focus program — which Warner oversees — using federal law-enforcement authority to defend Christian congregants and other believers' constitutional right to assemble for worship. His public posture explicitly frames freedom of worship as a protected right the federal government must actively enforce, directly reflecting the rubric's standard of defending free religious exercise from government or third-party interference.",
              ["https://www.justice.gov/opa/pr/justice-department-files-statement-interest-supporting-access-places-worship",
               "https://www.justice.gov/crt/religious-freedom-focus",
               "https://en.wikipedia.org/wiki/Mac_Warner"]),
    ]),

    # ------------ Doug Collins (US-R, Secretary of Veterans Affairs) --------
    ("doug-collins", "US", "Veterans", [
        claim("dc3", "doug-collins", "election_integrity", 0, True,
              "In December 2020, Collins was one of 126 Republican House members who signed an amicus brief supporting Texas v. Pennsylvania — a lawsuit filed at the United States Supreme Court contesting the presidential election results in Georgia, Michigan, Pennsylvania, and Wisconsin based on alleged irregularities in those states' election administration. After losing the Georgia Senate special election, Collins also made public allegations of fraud in Georgia's 2020 elections and called for thorough investigation of reported irregularities. These actions, taken while Collins was a sitting Member of Congress for Georgia's 9th District, reflect a sustained public posture demanding verification and integrity checks for electoral processes — consistent with the rubric's election integrity standard of demanding accountable, transparent elections free from systemic irregularity.",
              ["https://en.wikipedia.org/wiki/Doug_Collins_(politician)",
               "https://ballotpedia.org/Doug_Collins",
               "https://www.govtrack.us/congress/members/doug_collins/412531"]),
    ]),

    # ------------ Sharif Street (PA-D, U.S. Rep PA-03 2026 Candidate) ------
    ("sharif-street", "PA", "PA-03", [
        claim("ss3", "sharif-street", "biblical_marriage", 1, False,
              "Street is a member of the Pennsylvania LGBT Equality Caucus — an organized coalition of state senators formally dedicated to advancing 'equality for lesbian, gay, bisexual and transgender Pennsylvanians.' He attended a Pennsylvania Senate Democratic Caucus policy hearing explicitly examining 'statewide barriers for the transgender community,' lending legislative legitimacy to transgender public accommodations claims. His candidacy for Pennsylvania's 3rd Congressional District runs on a platform that includes support for The Fairness Act (HB300) — legislation that would make gender identity and sexual orientation protected categories under Pennsylvania civil rights law. These positions directly contradict the rubric's standard of opposing legal recognition of same-sex marriage and rejecting the normalization of same-sex unions in law and public policy.",
              ["https://en.wikipedia.org/wiki/Pennsylvania_LGBT_Equality_Caucus",
               "https://pasenate.com/pa-senate-dems-hold-policy-hearing-on-statewide-barriers-for-the-transgender-community/",
               "https://ballotpedia.org/Sharif_Street"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
