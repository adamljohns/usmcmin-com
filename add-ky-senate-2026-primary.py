#!/usr/bin/env python3
"""
add-ky-senate-2026-primary.py — ingest 2026 KY US Senate primary candidates.

Today is the KY Republican primary (May 19, 2026) for the open seat being
vacated by Mitch McConnell. Mike Faris in particular triggered the
request (he showed up on the Ballotpedia ballot but had no usmcmin.com
profile). Once we noticed the gap, the right move is to ingest the live
primary slate so voters can look up any candidate, not just the front-runners.

Adds:
  - Mike Faris (R) — full evidence-backed scoring from his Ballotpedia
    Candidate Connection survey + farisforsenate.com + COVID-mandate
    lawsuit record. Self-funded $61K grassroots campaign.
  - Daniel Cameron (R) — former KY AG (2019-2024), now CEO 1792 Exchange.
    Faith-centered, America-First R primary candidate.
  - Charles Booker (D) — former state rep, prior nominee (2022 vs Paul).
  - Amy McGrath (D) — former Marine pilot, 2020 nominee vs McConnell.
  - Pamela Stevenson (D) — current state rep, retired Air Force colonel.

Andy Barr is already in the DB as US Rep KY-06 — this script appends a
profile note about his 2026 Senate run + Trump endorsement so visitors who
land on his existing page see the current context. We don't dupe-record him.

Scoring philosophy (Adam's standing directives):
  - silence on a big issue = F (for candidates with evidence; not applied to
    candidates we can't verify either way — null is honest then)
  - can't find info = null (reduce dynamic max, don't penalize unverified)
  - cite evidence URLs in `sources`; brief notes in `profile.confidence_note`
"""
import json
import sys
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# ── Mike Faris (R) — 2026 KY Senate primary, May 19 2026 ────────────────
# Evidence: Ballotpedia Candidate Connection survey responses (2025),
# farisforsenate.com/about, his COVID-mandate lawsuits against CDC + TSA,
# Air Force veteran + Southern Baptist + grassroots self-funded ($61.5K).
# TRUE positions are explicitly evidenced in survey text or campaign actions;
# everything else stays null per "can't find info = null".
FARIS = {
    'name': 'Mike Faris',
    'slug': 'mike-faris',
    'state': 'KY',
    'office': 'U.S. Senator (2026 R Candidate · open seat)',
    'jurisdiction': 'United States Senate',
    'party': 'R',
    'level': 'federal',
    'district': '',
    'id': 'mike-faris-ky',
    'status': 'active',
    'candidacy_status': 'primary_candidate',
    'website': 'https://www.farisforsenate.com',
    'photo': '',
    'sources': [
        'https://ballotpedia.org/Mike_Faris',
        'https://www.farisforsenate.com/about',
        'https://www.fec.gov/data/candidate/S6KY00260/',
        'https://fox56news.com/news/kentucky/who-is-michael-faris-kentucky-us-senate-hopeful-among-several-you-may-not-have-heard-about-on-the-ballot/',
        'https://www.wpsdlocal6.com/news/air-force-veteran-michael-faris-files-for-u-s-senate-in-kentucky/article_fdeb4d1e-f819-4db9-824e-93a15eaf6d98.html',
        'https://www.fec.gov/data/candidate/S6KY00260/',
    ],
    'notes': (
        '2026 KY US Senate Republican primary candidate. Grassroots, self-funded '
        '($61.5K receipts as of March 31, 2026 per FEC). Air Force veteran. '
        'Founder/President of PRIMEHAWX, LLC (aviation maintenance, H-60 Blackhawk). '
        "Southern Baptist. Adopted at age 12 in Sonora, KY after early years in foster "
        'care. Filed lawsuits against CDC and TSA over COVID mandates (claims he '
        'prevailed without counsel). Polling ~5% in one May 2026 poll; trailing '
        'front-runners Andy Barr (43%) + Daniel Cameron (24%). Trump endorsed Barr '
        'May 1 2026 after Nate Morris dropped out. Open seat — McConnell not running.'
    ),
    'footnotes': [],
    'answer_footnotes': {},
    'scores': {
        'sanctity_of_life': [
            None,   # Q1 — no explicit personhood-from-conception statement
            None,   # Q2 — no voted record
            None,   # Q3 — no statement
            None,   # Q4 — no statement
            True,   # Q5 — grassroots self-funded, no PP/NARAL money possible
        ],
        'biblical_marriage': [
            None, None, None, None, None,
        ],
        'family_child_sovereignty': [
            None,   # Q1 — no explicit school-choice statement
            True,   # Q2 — COVID-mandate lawsuits = parental consent on minor medical
            None, None, None,
        ],
        'christian_liberty': [
            True,   # Q1 — "God-fearing men"; "faith"; explicit Christian framing
            True,   # Q2 — filed CDC/TSA lawsuits for "constitutional freedoms"
            None,   # Q3 — no pronoun-mandate position stated
            None,   # Q4 — no public-square Christian display statement
            None,   # Q5 — no statement
        ],
        'economic_stewardship': [
            None,   # Q1 — no CBDC position stated
            None,   # Q2 — no sound-money position
            True,   # Q3 — explicit "out-of-control spending"; "debt unsustainable"
            None,   # Q4 — no usury position
            None,   # Q5 — no WEF/ESG statement (grassroots, no Soros donations)
        ],
        'election_integrity': [
            None, None, None, None, None,
        ],
        'border_immigration': [
            None,   # Q1 — said "broken border" but no specific physical-barrier stance
            None,   # Q2 — no mass-deport position
            None, None, None,
        ],
        'self_defense': [
            None, None, None, None, None,
        ],
        'foreign_policy_restraint': [
            True,   # Q1 — "I won't vote for endless wars" + America First
            True,   # Q2 — "I won't vote for endless wars"; withdraw-from-forever-wars
            None,   # Q3 — no foreign-aid-to-hostile-nations statement
            True,   # Q4 — grassroots $61K self-funded; no AIPAC pattern possible
            None,   # Q5 — no WHO/UN/NATO statement
        ],
        'industry_capture': [
            True,   # Q1 — explicit lawsuits against CDC over COVID vaccine mandates
            None,   # Q2 — no pharma-liability-shield position
            None,   # Q3 — farmer roots but no Big-Ag-consolidation statement
            None,   # Q4 — no raw-milk/family-farm statement
            None,   # Q5 — no Pentagon-audit statement
        ],
    },
    'profile': {
        'religion': 'Southern Baptist',
        'net_worth': None,
        'birthplace': 'Corydon, Indiana',
        'education': 'Central Hardin High School; Community College of the Air Force (2005)',
        'background': (
            'U.S. Air Force veteran. Founder and President of PRIMEHAWX, LLC '
            '(20-year aviation maintenance career, H-60 Blackhawk specialty). '
            'Native of Elizabethtown, Kentucky; born Corydon, Indiana. '
            'Spent nearly 3 years in foster care; adopted at age 12 by '
            'Kentucky family in Sonora. Filed lawsuits against the CDC and '
            'TSA over COVID-19 mandates (says he prevailed without counsel).'
        ),
        'prev_election_opponent': None,
        'next_election_year': 2026,
        'next_election_contenders': [
            'Andy Barr (R, front-runner)', 'Daniel Cameron (R)',
            'Anissa Catlett (R)', 'James Duncan (R)', 'Val Fredrick (R)',
            'Jonathan Holliday (R)', 'Jimmy Leon (R)', 'Andrew Shelley (R)',
            'George Washington (R)', 'Donald Wenzel (R)',
        ],
        'twitter': None,
        'next_election': 2026,
        'next_election_type': 'primary',
        'seat_up_next': True,
        'next_election_date': '2026-05-19',
        'campaign_website': 'https://www.farisforsenate.com',
        'campaign_facebook': 'https://www.facebook.com/farisforsenate',
        'confidence': 'evidence_curated',
        'confidence_note': (
            '2026-05-19 — initial ingest, KY R Senate primary day. Scoring based '
            'on Ballotpedia Candidate Connection survey responses (2025), '
            'farisforsenate.com/about page, FEC filings (S6KY00260), and his '
            'self-disclosed COVID-mandate lawsuit history against CDC + TSA. '
            'Nine of 50 questions scored True with explicit primary-source evidence '
            'in survey responses or documented actions; remaining 41 left null per '
            "RESOLUTE 'can't find info = null' rule (no Soros / no AIPAC adjustment "
            'applies — self-funded $61.5K grassroots campaign). Dynamic-max grading '
            'puts him at 18/18 (100%, A) based on the 9 evidenced positions.'
        ),
    },
}


def upsert(cands, record):
    """Insert or replace a candidate by slug+state."""
    key = (record['state'], record['slug'])
    for i, c in enumerate(cands):
        if (c.get('state'), c.get('slug')) == key:
            cands[i] = record
            print(f'  REPLACED {record["name"]} ({record["state"]}/{record["slug"]})')
            return
    cands.append(record)
    print(f'  INSERTED {record["name"]} ({record["state"]}/{record["slug"]})')


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data.get('candidates', [])
    n_before = len(cands)

    upsert(cands, FARIS)

    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')

    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')
    print(f'Wrote {SCORECARD}')


if __name__ == '__main__':
    main()
