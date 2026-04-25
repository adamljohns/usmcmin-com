#!/usr/bin/env python3
"""
update-fredericksburg-council.py — sync the Fredericksburg, VA city
council roster in scorecard.json against the current verified roster
from the city's own page (https://www.fredericksburgva.gov/263/Council-Members,
fetched 2026-04-24).

Roster turnover detected:
  Ward 1: Jason Graham (already marked Former) -> Matt D. Rowe (sworn 2025)
  Ward 2: Jonathan Gerlach -> Joy Y. Crump (sworn 2025)

Existing records kept:
  Kerry P. Devine (Mayor, At-Large), Charlie Frye Jr. (Vice Mayor, W4),
  Jannan Holmes (At-Large), Will Mackintosh (At-Large), Susanna Finn (W3)

Approach:
  * Mark Jonathan Gerlach's office as "Former — City Council, Ward 2"
    so the audit trail stays intact (his profile carries his recent
    record). Set seat_up_next False.
  * Add Joy Y. Crump as a new Ward 2 council member with all-null
    scores + an "Awaiting review" tag (her record will pick up the
    awaiting-review banner automatically via generate-profiles.py).
  * Add Matt D. Rowe as Ward 1 council member with all-null scores
    + awaiting-review.

All facts cited at the bottom against the city government primary source.
Idempotent: re-running is a no-op.
"""
import json
import os
import subprocess

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')

NEW_MEMBERS = [
    {
        'name': 'Matt D. Rowe',
        'slug': 'matt-rowe-fxbg',
        'office': 'City Council, Ward 1',
        'jurisdiction': 'City of Fredericksburg',
        'level': 'local',
        'party': None,
        'district': 1,
        'state': 'VA',
        'scores': {cat: [None]*5 for cat in [
            'america_first','life','immigration','marriage',
            'self_defense','education','christian_heritage'
        ]},
        'notes': (
            "Elected to Fredericksburg City Council representing Ward 1; "
            "term ends 2029. RESOLUTE Citizen scoring pass not yet "
            "completed — record is scaffolding awaiting review."
        ),
        'photo': None,
        'website': None,
        'sources': [
            'https://www.fredericksburgva.gov/263/Council-Members',
            'https://en.wikipedia.org/wiki/Fredericksburg,_Virginia',
        ],
        'profile': {
            'religion': None,
            'background': None,
            'next_election_year': 2029,
            'next_election_date': '2029-11-06',
            'next_election_type': 'general',
            'seat_up_next': False,
        },
    },
    {
        'name': 'Joy Y. Crump',
        'slug': 'joy-crump-fxbg',
        'office': 'City Council, Ward 2',
        'jurisdiction': 'City of Fredericksburg',
        'level': 'local',
        'party': None,
        'district': 2,
        'state': 'VA',
        'scores': {cat: [None]*5 for cat in [
            'america_first','life','immigration','marriage',
            'self_defense','education','christian_heritage'
        ]},
        'notes': (
            "Elected to Fredericksburg City Council representing Ward 2; "
            "term ends 2029. RESOLUTE Citizen scoring pass not yet "
            "completed — record is scaffolding awaiting review."
        ),
        'photo': None,
        'website': None,
        'sources': [
            'https://www.fredericksburgva.gov/263/Council-Members',
            'https://en.wikipedia.org/wiki/Fredericksburg,_Virginia',
        ],
        'profile': {
            'religion': None,
            'background': None,
            'next_election_year': 2029,
            'next_election_date': '2029-11-06',
            'next_election_type': 'general',
            'seat_up_next': False,
        },
    },
]


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)

    # Step 1: Mark Jonathan Gerlach as Former
    for c in sc['candidates']:
        if c.get('slug') == 'jonathan-gerlach' and c.get('state') == 'VA':
            if 'Former' not in (c.get('office') or ''):
                c['office'] = 'Former — City Council, Ward 2'
            existing_notes = c.get('notes') or ''
            tag = 'Resigned/replaced 2025; seat now held by Joy Y. Crump.'
            if tag not in existing_notes:
                c['notes'] = (existing_notes + ' ' + tag).strip()
            (c.setdefault('profile', {}))['seat_up_next'] = False
            break

    # Verify Jason Graham is already marked Former
    for c in sc['candidates']:
        if c.get('slug') == 'jason-graham' and c.get('state') == 'VA':
            if 'Former' not in (c.get('office') or ''):
                c['office'] = 'Former — City Council, Ward 1'
            (c.setdefault('profile', {}))['seat_up_next'] = False
            break

    # Step 2: Add new members. Mint fresh ids; skip if a record by the
    # same slug+state already exists.
    existing_keys = {(c.get('slug'), c.get('state')) for c in sc['candidates']}
    next_id = max((c.get('id', 0) for c in sc['candidates']), default=0) + 1
    added = 0
    for rec in NEW_MEMBERS:
        if (rec['slug'], rec['state']) in existing_keys:
            print(f'Skip (exists): {rec["slug"]}')
            continue
        rec['id'] = next_id
        next_id += 1
        sc['candidates'].append(rec)
        added += 1
        print(f'Added: {rec["name"]} ({rec["office"]})')

    # Refresh meta
    sc.setdefault('meta', {})
    sc['meta']['total_candidates'] = len(sc['candidates'])
    sc['meta']['last_updated'] = '2026-04-24'

    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)

    print(f'\nAdded {added} new council member(s).')
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
