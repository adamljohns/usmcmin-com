#!/usr/bin/env python3
"""
add-fishback.py — adds James Fishback (R) to the FL Governor 2026 race.

He was on my "minor candidates deferred" list in the original compare
commit, but Adam flagged that he should be included. Public positions
are well-documented enough to score with claim-level evidence on
several cells, then party-default for the rest.

Key documented positions (Wikipedia, verified 2026-04-29):
  * Supports a complete abortion ban with NO exceptions (including
    rape and incest)  -> life q[1] = True (claim-evidenced)
  * Opposes same-sex marriage                                ->
    marriage q[0] = True (claim-evidenced)
  * Pledges to fire all H-1B visa workers in state government ->
    america_first q[1] = True (claim-evidenced)
  * Supports divestment from Israel Bonds                    ->
    america_first q[3] = True (claim-evidenced; this is the
    foreign-lobby-money question, and his stance is OPPOSITE of
    most R candidates who take AIPAC money — significant signal)
  * Eliminate property tax on homesteads, raise teacher pay 25%,
    oppose AI data centers in FL — not directly mapped to RESOLUTE
    Citizen criteria.

Background:
  * Born January 1, 1995
  * Attended Georgetown for international economics, dropped out
    after sophomore year
  * Founded Azoria Capital; left in January 2026 (says so under
    sworn testimony April 2026)
  * Declared 2026 FL gubernatorial candidacy on November 24, 2025

Sources verified 2026-04-29:
  * https://en.wikipedia.org/wiki/James_Fishback
  * https://en.wikipedia.org/wiki/2026_Florida_gubernatorial_election

Run once; idempotent.
"""
import json
import os
import subprocess
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
RACES = os.path.join(REPO, 'data', 'races.json')

RACE_ID = 'fl-governor-2026'
PRIMARY_DATE = '2026-08-18'
GENERAL_DATE = '2026-11-03'
TODAY = date.today().isoformat()

# R party-default baseline
R_BASE = {
    'america_first':      [True,  True,  None,  None,  True],
    'life':               [True,  True,  None,  True,  None],
    'immigration':        [True,  True,  None,  None,  None],
    'marriage':           [True,  None,  True,  None,  None],
    'self_defense':       [True,  True,  True,  None,  True],
    'education':          [True,  True,  True,  None,  None],
    'christian_heritage': [None]*5,
}

# Override cells with claim-evidenced positions.
# (cat, qidx) -> True/False — applied on top of R_BASE.
OVERRIDES = {
    ('life', 1): True,           # Total abolition, no exceptions (he explicitly supports)
    ('marriage', 0): True,       # One-man-one-woman, he opposes same-sex marriage
    ('america_first', 1): True,  # Pledges to fire H-1B visa workers — opposite of foreign-influence
    ('america_first', 3): True,  # Divests from Israel Bonds — opposite of AIPAC alignment
}

# Apply overrides
SCORES = {cat: list(vals) for cat, vals in R_BASE.items()}
for (cat, q), v in OVERRIDES.items():
    SCORES[cat][q] = v


CLAIMS = [
    {
        'id': 'jf-life-1',
        'category': 'life',
        'question_idx': 1,
        'score_impact': True,
        'kind': 'statement',
        'text': (
            "Publicly supports a complete abortion ban with NO exceptions, "
            "including for rape and incest. Position documented in his "
            "campaign positions as covered in the Wikipedia profile."
        ),
        'sources': [
            'https://en.wikipedia.org/wiki/James_Fishback',
        ],
        'verified': True,
        'verified_date': TODAY,
        'disputed': False,
        'confidence': 'high',
    },
    {
        'id': 'jf-marriage-0',
        'category': 'marriage',
        'question_idx': 0,
        'score_impact': True,
        'kind': 'statement',
        'text': (
            "Publicly opposes same-sex marriage. Position documented in "
            "his campaign positions as covered in the Wikipedia profile."
        ),
        'sources': [
            'https://en.wikipedia.org/wiki/James_Fishback',
        ],
        'verified': True,
        'verified_date': TODAY,
        'disputed': False,
        'confidence': 'high',
    },
    {
        'id': 'jf-america_first-1',
        'category': 'america_first',
        'question_idx': 1,
        'score_impact': True,
        'kind': 'statement',
        'text': (
            "Pledges to fire all H-1B visa workers from Florida state "
            "government if elected. A direct America-First labor-policy "
            "stance favoring U.S.-citizen workers over foreign visa holders."
        ),
        'sources': [
            'https://en.wikipedia.org/wiki/James_Fishback',
        ],
        'verified': True,
        'verified_date': TODAY,
        'disputed': False,
        'confidence': 'high',
    },
    {
        'id': 'jf-america_first-3',
        'category': 'america_first',
        'question_idx': 3,
        'score_impact': True,
        'kind': 'policy',
        'text': (
            "Supports state divestment from Israel Bonds. Notable because "
            "it positions him opposite of most major-party candidates who "
            "accept AIPAC-aligned campaign support; on the RESOLUTE Citizen "
            "scoring criterion (no donations from foreign-backed lobbies) "
            "this counts as alignment with the True direction."
        ),
        'sources': [
            'https://en.wikipedia.org/wiki/James_Fishback',
        ],
        'verified': True,
        'verified_date': TODAY,
        'disputed': False,
        'confidence': 'high',
    },
]


FISHBACK = {
    'name': 'James Fishback',
    'slug': 'james-fishback',
    'office': 'Candidate for Governor of Florida',
    'jurisdiction': 'State of Florida',
    'level': 'state',
    'party': 'R',
    'district': None,
    'state': 'FL',
    'scores': SCORES,
    'notes': (
        "Declared 2026 Florida gubernatorial Republican primary "
        "candidate (announced November 24, 2025). Born January 1, 1995. "
        "Founder and former CEO of Azoria Capital (left January 2026). "
        "Attended Georgetown University for international economics, "
        "dropped out after sophomore year. Public positions: complete "
        "abortion ban with no exceptions, opposition to same-sex "
        "marriage, pledge to fire H-1B visa workers from FL state "
        "government, elimination of property tax on homesteads, raising "
        "teacher pay by 25%, opposition to AI data centers in Florida, "
        "and state divestment from Israel Bonds. Initial scoring: "
        "Republican party-default baseline with explicit overrides for "
        "the four positions above where direct public-statement evidence "
        "supports the score; christian_heritage left null."
    ),
    'photo': None,
    'website': 'https://fishback2026.com',
    'sources': [
        'https://en.wikipedia.org/wiki/James_Fishback',
        'https://en.wikipedia.org/wiki/2026_Florida_gubernatorial_election',
        'https://ballotpedia.org/James_Fishback',
    ],
    'profile': {
        'religion': None,
        'birthplace': None,
        'education': 'Georgetown University (international economics, undergraduate, did not complete degree)',
        'background': (
            'Founder and former CEO of Azoria Capital (left January 2026). '
            'Public-policy commentator and Republican primary candidate.'
        ),
        'next_election_year': 2026,
        'next_election_date': PRIMARY_DATE,
        'next_election_type': 'primary',
        'seat_up_next': True,
        'confidence': 'evidence',  # has claim evidence, not party_default
        'candidacy': {
            'race_id': RACE_ID,
            'office': 'Governor of Florida',
            'primary_date': PRIMARY_DATE,
            'general_date': GENERAL_DATE,
            'is_incumbent': False,
            'declared_date': '2025-11-24',
        },
    },
    'claims': CLAIMS,
}


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)
    next_id = max((c.get('id', 0) for c in sc['candidates']), default=0) + 1
    existing_keys = {(c.get('slug'), c.get('state')) for c in sc['candidates']}

    if (FISHBACK['slug'], FISHBACK['state']) in existing_keys:
        # Replace by slug+state
        for i, c in enumerate(sc['candidates']):
            if c.get('slug') == FISHBACK['slug'] and c.get('state') == FISHBACK['state']:
                FISHBACK['id'] = c.get('id')
                sc['candidates'][i] = FISHBACK
                print(f'Replaced: {FISHBACK["name"]}')
                break
    else:
        FISHBACK['id'] = next_id
        sc['candidates'].append(FISHBACK)
        print(f'Added: {FISHBACK["name"]} ({FISHBACK["party"]}) — {FISHBACK["office"]}')

    sc['meta']['total_candidates'] = len(sc['candidates'])
    sc['meta']['last_updated'] = TODAY
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)

    # Update races.json — add fishback to R list
    if os.path.exists(RACES):
        with open(RACES, 'r', encoding='utf-8') as f:
            races = json.load(f)
        race = races.get('races', {}).get(RACE_ID)
        if race:
            r_list = race.setdefault('candidates_by_party', {}).setdefault('R', [])
            if 'james-fishback' not in r_list:
                # Insert after Renner so the order is donalds, collins, renner, fishback
                r_list.append('james-fishback')
                with open(RACES, 'w', encoding='utf-8') as f:
                    json.dump(races, f, indent=2, ensure_ascii=False)
                print('Added james-fishback to fl-governor-2026 R list in data/races.json')

    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
