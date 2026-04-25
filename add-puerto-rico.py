#!/usr/bin/env python3
"""
add-puerto-rico.py — seed an initial Puerto Rico scorecard.

Adds 4 high-profile PR elected officials with awaiting-review status:

  * Jenniffer González Colón (PNP) — Governor of Puerto Rico
  * Pablo José Hernández Rivera (PPD/D) — Resident Commissioner
    (PR's at-large non-voting member of the U.S. House)
  * Thomas Rivera Schatz (PNP) — President of the Senate of PR
  * Carlos Johnny Méndez (PNP) — Speaker of the House of PR

PR uses a different party landscape than the mainland; we record
the actual PR party label in `party` and note US-Congress caucus
alignment in `notes` where relevant.

Sources verified 2026-04-25:
  https://en.wikipedia.org/wiki/Government_of_Puerto_Rico
  https://en.wikipedia.org/wiki/Resident_Commissioner_of_Puerto_Rico

Run once; idempotent (skips by slug+state).
"""
import json
import os
import subprocess
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')


def empty_scores():
    return {cat: [None]*5 for cat in [
        'america_first','life','immigration','marriage',
        'self_defense','education','christian_heritage'
    ]}


SOURCES_GOVT = [
    'https://en.wikipedia.org/wiki/Government_of_Puerto_Rico',
]
SOURCES_RC = [
    'https://en.wikipedia.org/wiki/Resident_Commissioner_of_Puerto_Rico',
]

NEW = [
    {
        'name': 'Jenniffer González Colón',
        'slug': 'jenniffer-gonzalez-colon',
        'office': 'Governor',
        'jurisdiction': 'Commonwealth of Puerto Rico',
        'level': 'state',
        'party': 'PNP',
        'state': 'PR',
        'scores': empty_scores(),
        'notes': (
            "Governor of Puerto Rico. Member of the New Progressive Party "
            "(PNP), which is generally aligned with the U.S. Republican "
            "Party and supports Puerto Rican statehood. Previously served "
            "as Resident Commissioner of Puerto Rico (PR's at-large non-"
            "voting member of the U.S. House) and caucused with House "
            "Republicans. RESOLUTE Citizen scoring pass not yet completed."
        ),
        'sources': SOURCES_GOVT + ['https://en.wikipedia.org/wiki/Jenniffer_Gonz%C3%A1lez'],
        'profile': {
            'background': 'Former Resident Commissioner (2017–2025); now serving as Governor of Puerto Rico after the November 2024 election.',
            'next_election_year': 2028,
            'seat_up_next': False,
        },
    },
    {
        'name': 'Pablo José Hernández Rivera',
        'slug': 'pablo-jose-hernandez-rivera',
        'office': 'Resident Commissioner of Puerto Rico (U.S. House, non-voting)',
        'jurisdiction': 'Commonwealth of Puerto Rico',
        'level': 'federal',
        'party': 'PPD',
        'district': 'At-Large',
        'state': 'PR',
        'scores': empty_scores(),
        'notes': (
            "Resident Commissioner of Puerto Rico, sworn in January 3, "
            "2025. Member of the Popular Democratic Party (PPD), the "
            "youngest person ever to hold the post. Caucuses with House "
            "Democrats. PR's Resident Commissioner is the only non-"
            "voting U.S. House member who can sit on committees and vote "
            "in committee but not on the House floor."
        ),
        'sources': SOURCES_RC + ['https://en.wikipedia.org/wiki/Pablo_Jos%C3%A9_Hern%C3%A1ndez_Rivera'],
        'profile': {
            'background': 'Sworn in January 3, 2025 as the at-large non-voting Resident Commissioner. Caucuses with House Democrats.',
            'next_election_year': 2028,
            'seat_up_next': False,
            'sworn_in_date': '2025-01-03',
        },
    },
    {
        'name': 'Thomas Rivera Schatz',
        'slug': 'thomas-rivera-schatz',
        'office': 'President of the Senate',
        'jurisdiction': 'Senate of Puerto Rico',
        'level': 'state',
        'party': 'PNP',
        'state': 'PR',
        'scores': empty_scores(),
        'notes': (
            "President of the Senate of Puerto Rico. PNP (New Progressive "
            "Party); generally aligned with U.S. Republican policy "
            "preferences and pro-statehood."
        ),
        'sources': SOURCES_GOVT + ['https://en.wikipedia.org/wiki/Thomas_Rivera_Schatz'],
        'profile': {'seat_up_next': False},
    },
    {
        'name': 'Carlos Johnny Méndez',
        'slug': 'carlos-johnny-mendez',
        'office': 'Speaker of the House',
        'jurisdiction': 'House of Representatives of Puerto Rico',
        'level': 'state',
        'party': 'PNP',
        'state': 'PR',
        'scores': empty_scores(),
        'notes': (
            "Speaker of the Puerto Rico House of Representatives. PNP "
            "(New Progressive Party)."
        ),
        'sources': SOURCES_GOVT,
        'profile': {'seat_up_next': False},
    },
]


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)

    existing_keys = {(c.get('slug'), c.get('state')) for c in sc['candidates']}
    next_id = max((c.get('id', 0) for c in sc['candidates']), default=0) + 1
    added = 0
    for rec in NEW:
        rec.setdefault('district', None)
        rec.setdefault('photo', None)
        rec.setdefault('website', None)
        if (rec['slug'], rec['state']) in existing_keys:
            print(f'Skip (exists): {rec["slug"]}')
            continue
        rec['id'] = next_id
        next_id += 1
        sc['candidates'].append(rec)
        added += 1
        print(f'Added: {rec["name"]} ({rec["party"]}) — {rec["office"]}')

    # Add PR to meta.states if it isn't there
    states_list = sc['meta'].setdefault('states', [])
    if 'PR' not in states_list:
        states_list.append('PR')
        states_list.sort()
        print('Added PR to meta.states')

    sc['meta']['total_candidates'] = len(sc['candidates'])
    sc['meta']['last_updated'] = date.today().isoformat()
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    print(f'\nAdded {added} record(s); meta.states now has {len(states_list)} entries.')
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
