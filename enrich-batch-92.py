#!/usr/bin/env python3
"""Enrichment batch 92: hand-curated claims for 4 state-level R candidates.

Targets archetype_curated candidates from the bottom of the alphabet (MO, NM, MN)
that had 0 evidence claims. Uses the (slug + state + office_keyword) matcher.

Candidates: Jay Ashcroft (MO SoS), Denny Hoskins (MO SoS), Mark Ronchetti (NM Gov),
Scott Jensen (MN Gov). Each claim cites >=1 reliable source and reflects sourced
2024-2026 voting record / public positions.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # ---------------- Jay Ashcroft (MO, former Secretary of State) ----------------
    ("jay-ashcroft", "MO", "Missouri Secretary", [
        claim("ja1", "jay-ashcroft", "election_integrity", 0, True,
              "As Missouri Secretary of State (2017-2025), Ashcroft championed and enforced Missouri's strict photo-ID requirement for in-person voting — requiring a state- or federally issued, dated, photo ID at the polls — calling the law a success after its first use and defending it through legal challenges.",
              ["https://ballotpedia.org/Jay_Ashcroft",
               "https://en.wikipedia.org/wiki/Jay_Ashcroft"]),
        claim("ja2", "jay-ashcroft", "sanctity_of_life", 0, True,
              "Consistently opposed abortion access expansion: as SoS, Ashcroft drafted ballot summaries for Missouri abortion-rights initiatives in language a circuit court judge ruled overstated fetal harm and failed to fairly characterize the measures — revealing his personal pro-life posture in an official act.",
              ["https://missouriindependent.com/2024/09/05/judge-rules-ashcrofts-abortion-amendment-unfair-misleading/",
               "https://ballotpedia.org/Jay_Ashcroft"]),
        claim("ja3", "jay-ashcroft", "biblical_marriage", 1, True,
              "In November 2022 Ashcroft publicly criticised then-Sen. Roy Blunt for voting for the Respect for Marriage Act — the federal bill codifying same-sex marriage — signaling an unambiguous one-man-one-woman position that rejects federal recognition of same-sex unions.",
              ["https://missouriindependent.com/2022/11/29/ashcroft-criticizes-blunt-support-for-senate-bill-protecting-same-sex-marriage/",
               "https://en.wikipedia.org/wiki/Jay_Ashcroft"]),
    ]),

    # ---------------- Denny Hoskins (MO, current Secretary of State) ----------------
    ("denny-hoskins", "MO", "Missouri Secretary", [
        claim("dh1", "denny-hoskins", "election_integrity", 0, True,
              "Led implementation of Missouri Amendment 7 (passed November 2024 with 68.4% of the vote), which constitutionally requires proof of citizenship to vote and bans ranked-choice voting; praised President Trump's 'Make Elections Great Again' executive order on election integrity and champions citizenship-only voter rolls.",
              ["https://www.sos.mo.gov/default.aspx?PageId=10504",
               "https://www.dailysignal.com/2025/09/13/missouri-secretary-of-state-talks-election-integrity"]),
        claim("dh2", "denny-hoskins", "election_integrity", 1, True,
              "Proposed increasing Missouri's required hand-count audit of ballots from 5% to 10-15%, advocates for paper-only ballots and no internet-connected voting equipment, and is actively cleaning the state voter rolls — a paper-ballot, hand-count integrity posture matching the rubric standard.",
              ["https://www.kfvs12.com/2025/01/02/local-election-authorities-say-hoskins-plan-increase-hand-counting-ballots-would-cost-counties-time-resources/",
               "https://www.sos.mo.gov/default.aspx?PageId=10548"]),
    ]),

    # ---------------- Mark Ronchetti (NM, Governor 2026 R Candidate) ----------------
    ("mark-ronchetti-gov-2026", "NM", "Governor", [
        claim("mr1", "mark-ronchetti-gov-2026", "self_defense", 1, True,
              "Earned an NRA 'A' grade and describes himself as a gun owner who will 'oppose efforts by liberal gun-grabbers who seek to criminalize law-abiding gun owners.' Opposes gun bans and confiscation, and the NM Democratic Party highlighted his NRA-backed opposition to gun-control legislation as a line of attack.",
              ["https://ballotpedia.org/Mark_Ronchetti",
               "https://nmdemocrats.org/news/mark-ronchetti-and-the-gop-candidates-for-governor-stand-with-the-nra-in-opposing-commonsense-gun-safety-measures/"]),
        claim("mr2", "mark-ronchetti-gov-2026", "border_immigration", 2, True,
              "Pledges to eliminate sanctuary policies that shield illegal immigrants who commit crimes from federal immigration officials and to order the National Guard to the border — a direct anti-sanctuary-city posture consistent with the rubric's mandatory enforcement standard.",
              ["https://markronchetti.com/issues/border-security/",
               "https://ballotpedia.org/Mark_Ronchetti"]),
        claim("mr3", "mark-ronchetti-gov-2026", "border_immigration", 0, True,
              "Supports constructing physical border barriers, deploying drones and additional Border Patrol, closing the asylum loophole, and sending the National Guard to the New Mexico-Mexico border — a comprehensive secure-the-border posture aligning with the rubric's wall-and-military standard.",
              ["https://markronchetti.com/issues/border-security/",
               "https://www.ontheissues.org/Mark_Ronchetti_Immigration.htm"]),
    ]),

    # ---------------- Scott Jensen (MN, Governor 2026 R Candidate / MD) ----------------
    ("scott-jensen-gov-2026", "MN", "Governor", [
        claim("sj1", "scott-jensen-gov-2026", "industry_capture", 0, True,
              "As a practicing family physician, Jensen was one of the most prominent medical voices opposing COVID-19 vaccine and treatment mandates during the pandemic, criticizing the CDC's guidance on death-certificate coding and questioning mandates on his Senate record — a posture aligned with the rubric's anti-pharma-mandate standard.",
              ["https://en.wikipedia.org/wiki/Scott_Jensen_(Minnesota_politician)",
               "https://ballotpedia.org/Scott_Jensen_(Minnesota)"]),
        claim("sj2", "scott-jensen-gov-2026", "economic_stewardship", 2, True,
              "In his 2022 gubernatorial campaign, Jensen called for eliminating Minnesota's state personal income tax and dramatically reducing state expenditures — a hard anti-deficit, limited-government fiscal posture consistent with the rubric's balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Scott_Jensen_(Minnesota_politician)",
               "https://ballotpedia.org/Scott_Jensen_(Minnesota)"]),
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
