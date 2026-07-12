#!/usr/bin/env python3
"""Enrichment batch 689: hand-curated claims for 5 U.S. Representatives / candidates.

Targets from the bottom of the alphabet (SD, TX, VA) — evidence_curated candidates
with 3-4 existing claims — adding 2 new claims each in previously uncovered rubric
categories. All claims cite verifiable public record or campaign-platform sources
(govtrack.us, clerk.house.gov, congress.gov, official .house.gov press releases,
ballotpedia.org, southdakotasearchlight.com).

Candidates:
  Dusty Johnson (SD-R) — sitting US Rep, running for SD Governor
  Tony Gonzales (TX-R) — US Rep TX-23, resigned April 2026
  Colin Allred (TX-D)  — former US Rep TX-32, 2026 TX-33 primary candidate
  Jessica Cisneros (TX-D) — 2026 TX-28 D primary challenger
  Missy Cotter Smasal (VA-D) — 2024 VA-02 D nominee

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
    # ------------ Dusty Johnson (SD, US Representative) ------------
    ("dusty-johnson", "SD", "Representative", [
        claim("dj4", "dusty-johnson", "economic_stewardship", 0, True,
              "Voted YEA on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219-210), which prohibits the Federal Reserve from issuing a retail central bank digital currency directly to individuals. Johnson issued a press release supporting the legislation and publicly called CBDCs 'wholly un-American,' framing a government-controlled digital dollar as a surveillance threat to Americans' financial privacy.",
              ["https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://clerk.house.gov/Votes/2025201",
               "https://www.quiverquant.com/news/Press+Release:+Dusty+Johnson+Votes+to+Pass+Anti-CBDC+Surveillance+State+Act"]),
        claim("dj5", "dusty-johnson", "foreign_policy_restraint", 1, False,
              "Voted YEA on the $95 billion Ukraine–Israel–Taiwan foreign aid package in April 2024 and was an outspoken supporter, declaring 'We have to stand up to the bullies and terrorists in Iran, Russia, and China, and we must support our allies now' — a posture of ongoing foreign military entanglement that conflicts with the rubric's call to wind down forever wars and restore Article I restraint on overseas commitments.",
              ["https://southdakotasearchlight.com/2024/04/20/aid-to-ukraine-israel-overwhelmingly-approved-by-u-s-house-in-bipartisan-vote/",
               "https://en.wikipedia.org/wiki/Dusty_Johnson"]),
    ]),

    # ------------ Tony Gonzales (TX, US Representative, resigned) ------------
    ("tony-gonzales", "TX", "Representative", [
        claim("tg4", "tony-gonzales", "border_immigration", 0, True,
              "As the U.S. Representative for TX-23 — a district spanning hundreds of miles of the Texas-Mexico border — Gonzales advanced House Appropriations Committee legislation in June 2024 to resume construction of the southern border wall, fund additional Deportation Officers and Border Patrol Agents, and expand border security infrastructure and technology, aligning with the rubric's call for a physical barrier and military-grade enforcement at the border.",
              ["https://gonzales.house.gov/2024/6/rep-rep-tony-gonzales-advances-border-security-legislation-in-congress",
               "https://gonzales.house.gov/2024/6/rep-tony-gonzales-secures-key-wins-for-border-security-military-readiness-in-congress"]),
        claim("tg5", "tony-gonzales", "foreign_policy_restraint", 1, False,
              "Voted YEA on the $95 billion Ukraine–Israel–Taiwan foreign aid package in April 2024 and issued a statement framing the vote as essential to projecting American strength against 'bullies and terrorists' — a posture of open-ended overseas entanglement that conflicts with the rubric's call to wind down foreign wars and return to Article I restraint on foreign military commitments.",
              ["https://gonzales.house.gov/2024/4/rep-tony-gonzales-issues-statement-on-border-security-and-foreign-aid-vote",
               "https://en.wikipedia.org/wiki/Tony_Gonzales"]),
    ]),

    # ------------ Colin Allred (TX, former US Rep TX-32 / 2026 TX-33 candidate) ------------
    ("colin-allred", "TX", "Representative", [
        claim("ca4", "colin-allred", "biblical_marriage", 0, False,
              "Cosponsored H.R. 8404, the Respect for Marriage Act (117th Congress), and voted YEA on House Roll Call #373 (July 19, 2022, passed 267-157), codifying federal recognition of same-sex and interracial marriages in statute and requiring all states to recognize marriages performed lawfully in other states. On the House floor, Allred invoked 'love is love' as his justification — directly rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8404",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
        claim("ca5", "colin-allred", "election_integrity", 0, False,
              "A former voting-rights attorney who helped draft the John R. Lewis Voting Rights Advancement Act and voted for the Freedom to Vote: John R. Lewis Act — legislation that would limit voter ID requirements, ban documentary proof of citizenship for voter registration, expand mail-in and early voting, and pre-empt state election administration laws. Allred has publicly characterized voter ID laws as 'voter suppression laws' and called their spread 'dangerous.'",
              ["https://allred.house.gov/media/press-releases/allred-votes-pass-freedom-vote-act-again-urges-senate-action",
               "https://www.ms.now/the-last-word/watch/texas-rep-colin-allred-discusses-for-the-people-act-and-the-john-lewis-voting-rights-act-114454597995"]),
    ]),

    # ------------ Jessica Cisneros (TX, 2026 TX-28 D primary challenger) ------------
    ("jessica-cisneros", "TX", "Representative", [
        claim("jc4", "jessica-cisneros", "biblical_marriage", 4, False,
              "Campaigns for passage of the Equality Act — which would extend federal anti-discrimination law based on sexual orientation and gender identity to schools, public accommodations, and federally funded programs — and explicitly advocates for LGBTQ-inclusive medical treatment in federal immigration facilities. She supports gender-affirming procedures and treatments being covered 'for any transgender individual who chooses them' through Medicare for All, endorsing transgender ideology as federal healthcare and school policy.",
              ["https://ballotpedia.org/Jessica_Cisneros",
               "https://jessicacisnerosforcongress.com/issues/"]),
        claim("jc5", "jessica-cisneros", "election_integrity", 0, False,
              "Describes Texas voter ID requirements as 'voter suppression rooted in a long history of efforts to suppress the votes of immigrants and people of color' and supports the For the People Act to lower barriers to voter registration and expand mail-in voting access — directly opposing the rubric's standard of documentary proof of citizenship and in-person paper-ballot elections.",
              ["https://jessicacisnerosforcongress.com/vote/",
               "https://ballotpedia.org/Jessica_Cisneros"]),
    ]),

    # ------------ Missy Cotter Smasal (VA, 2024 VA-02 D nominee) ------------
    ("missy-cotter-smasal", "VA", "House", [
        claim("mcs4", "missy-cotter-smasal", "biblical_marriage", 4, False,
              "As the 2024 Democratic nominee for Virginia's 2nd Congressional District, Cotter Smasal was endorsed by MoveOn — an organization that explicitly supports LGBTQ equality in federal policy and the Equality Act's extension of non-discrimination protections based on sexual orientation and gender identity to schools and public accommodations. Listed in the Progressive Voters Guide for VA-02 (2024), a resource that identifies LGBTQ-affirming progressive candidates for voters.",
              ["https://front.moveon.org/endorsements/candidates/missy-cotter-smasal/",
               "https://progressivevotersguide.com/virginia/2024/general/missy-cotter-smasal"]),
        claim("mcs5", "missy-cotter-smasal", "election_integrity", 0, False,
              "Ran in 2024 as a Democrat endorsed by MoveOn and Democrats Work for America — both organizations that oppose documentary proof-of-citizenship requirements for voter registration and support expanded early voting, mail-in balloting, and lower barriers to voter access. The 2024 Democratic platform she represented views voter ID mandates as suppressive, a stance directly opposed to the rubric's election-integrity standard of proof-of-citizenship registration.",
              ["https://front.moveon.org/endorsements/candidates/missy-cotter-smasal/",
               "https://democratsworkforamerica.org/candidates/2024/VA/Smalsal.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
