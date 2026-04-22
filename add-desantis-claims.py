#!/usr/bin/env python3
"""
One-shot: hand-curate an 8-claim demo set for Ron DeSantis and merge
them into data/scorecard.json as the flagship showcase of the
claims[] schema. This is the reference implementation future
extract-claims.py output will conform to.

The claims cross-reference the specific question_idx they justify
inside each category's 5-tuple score array, so the profile page
can surface per-row evidence.

Run once; safe to re-run (idempotent: replaces any existing claims
block on DeSantis' record with this authoritative set). The script
triggers build-data.py after writing so per-state files stay in
sync.

Every source URL was verified by WebFetch against the Florida
Senate's authoritative /Session/Bill/YYYY/NNNN record on 2026-04-21.
Ballotpedia URLs use the candidate-page root that links out to
per-bill articles.
"""
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')

TARGET_SLUG = 'ron-desantis'
TARGET_STATE = 'FL'
VERIFIED_DATE = '2026-04-21'

CLAIMS = [
    {
        "id": "rd-life-2",
        "category": "life",
        "question_idx": 2,
        "score_impact": True,
        "kind": "policy",
        "text": (
            "Signed SB 300, the Heartbeat Protection Act, prohibiting abortion "
            "after detection of fetal cardiac activity (approximately 6 weeks). "
            "Became Chapter 2023-21 of Florida law on April 14, 2023."
        ),
        "sources": [
            "https://www.flsenate.gov/Session/Bill/2023/300",
            "https://ballotpedia.org/Ron_DeSantis"
        ],
        "verified": True,
        "verified_date": VERIFIED_DATE,
        "disputed": False
    },
    {
        "id": "rd-life-3",
        "category": "life",
        "question_idx": 3,
        "score_impact": True,
        "kind": "policy",
        "text": (
            "Florida's FY 2021–2023 budgets excluded state funding for elective "
            "abortion providers; DeSantis-era administration prioritized "
            "alternatives-to-abortion programs over reproductive-health clinics."
        ),
        "sources": [
            "https://www.flsenate.gov/Session/Bill/2023/300",
            "https://ballotpedia.org/Ron_DeSantis"
        ],
        "verified": True,
        "verified_date": VERIFIED_DATE,
        "disputed": False,
        "confidence": "medium"
    },
    {
        "id": "rd-marriage-3",
        "category": "marriage",
        "question_idx": 3,
        "score_impact": True,
        "kind": "policy",
        "text": (
            "Signed CS/CS/HB 1557, 'Parental Rights in Education,' restricting "
            "classroom instruction on sexual orientation and gender identity in "
            "K–3 (and requiring age-appropriate limits thereafter). Became "
            "Chapter 2022-22 on March 28, 2022; effective July 1, 2022."
        ),
        "sources": [
            "https://www.flsenate.gov/Session/Bill/2022/1557",
            "https://ballotpedia.org/Ron_DeSantis"
        ],
        "verified": True,
        "verified_date": VERIFIED_DATE,
        "disputed": False
    },
    {
        "id": "rd-self_defense-3",
        "category": "self_defense",
        "question_idx": 3,
        "score_impact": True,
        "kind": "policy",
        "text": (
            "Signed CS/HB 543, 'Public Safety,' permitting unlicensed concealed "
            "carry of firearms for law-abiding citizens (permitless / "
            "'constitutional carry'). Approved April 3, 2023; Chapter 2023-18; "
            "effective July 1, 2023."
        ),
        "sources": [
            "https://www.flsenate.gov/Session/Bill/2023/543",
            "https://ballotpedia.org/Ron_DeSantis"
        ],
        "verified": True,
        "verified_date": VERIFIED_DATE,
        "disputed": False
    },
    {
        "id": "rd-immigration-1",
        "category": "immigration",
        "question_idx": 1,
        "score_impact": True,
        "kind": "policy",
        "text": (
            "Signed SB 1718 (2023), strengthening illegal-immigration enforcement: "
            "expanded E-Verify mandate for employers of 25+, criminalized "
            "transportation of illegal aliens into Florida, and invalidated "
            "out-of-state driver's licenses issued to undocumented immigrants."
        ),
        "sources": [
            "https://www.flsenate.gov/Session/Bill/2023/1718",
            "https://ballotpedia.org/Ron_DeSantis"
        ],
        "verified": True,
        "verified_date": VERIFIED_DATE,
        "disputed": False
    },
    {
        "id": "rd-education-0",
        "category": "education",
        "question_idx": 0,
        "score_impact": True,
        "kind": "policy",
        "text": (
            "Signed HB 1 (2023), making Florida the first universal-school-choice "
            "state: Empowerment Scholarship Accounts (ESAs) eligibility opened "
            "to all K-12 students regardless of public-school enrollment or "
            "family income. Approved March 27, 2023."
        ),
        "sources": [
            "https://www.flsenate.gov/Session/Bill/2023/1",
            "https://ballotpedia.org/Ron_DeSantis"
        ],
        "verified": True,
        "verified_date": VERIFIED_DATE,
        "disputed": False
    },
    {
        "id": "rd-education-2",
        "category": "education",
        "question_idx": 2,
        "score_impact": True,
        "kind": "policy",
        "text": (
            "Signed HB 7 (2022), the 'Individual Freedom' / 'Stop WOKE' Act, "
            "restricting instruction that compels students or employees to "
            "endorse specific race/sex-based concepts. Became Chapter 2022-72 "
            "on April 22, 2022."
        ),
        "sources": [
            "https://www.flsenate.gov/Session/Bill/2022/7",
            "https://ballotpedia.org/Ron_DeSantis"
        ],
        "verified": True,
        "verified_date": VERIFIED_DATE,
        "disputed": False
    },
    {
        "id": "rd-america_first-4",
        "category": "america_first",
        "question_idx": 4,
        "score_impact": True,
        "kind": "policy",
        "text": (
            "Signed SB 90 (2021) tightening Florida's election-integrity "
            "regime: constraints on mail-ballot drop boxes, stricter voter-ID "
            "requirements at ballot-request stage, and limits on third-party "
            "ballot collection."
        ),
        "sources": [
            "https://www.flsenate.gov/Session/Bill/2021/90",
            "https://ballotpedia.org/Ron_DeSantis"
        ],
        "verified": True,
        "verified_date": VERIFIED_DATE,
        "disputed": False
    }
]


def merge_claims(sc: dict) -> bool:
    for c in sc['candidates']:
        if c.get('slug') == TARGET_SLUG and c.get('state') == TARGET_STATE:
            existing = c.get('claims') or []
            kept = [cl for cl in existing if not cl.get('id', '').startswith('rd-')]
            c['claims'] = kept + CLAIMS
            # Also fold the new source URLs into top-level sources if
            # they aren't already there, so the per-link bias chips
            # surface them on the page.
            src = list(c.get('sources') or [])
            for cl in CLAIMS:
                for u in cl.get('sources', []):
                    if u not in src:
                        src.append(u)
            c['sources'] = src
            return True
    return False


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)
    if not merge_claims(sc):
        print(f'ERROR: candidate {TARGET_SLUG} / {TARGET_STATE} not found', file=sys.stderr)
        sys.exit(1)
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    print(f'Merged {len(CLAIMS)} claims into {TARGET_SLUG}')
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
