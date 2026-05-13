#!/usr/bin/env python3
"""Add the 5 Soros-funded prosecutor records flagged in
data/soros_adjustments.json so the apply-soros-adjustments.py
pass can find them.

Each is recorded with party_default(D) baseline scoring and the
Soros penalty layered on top.
"""
import json, os, subprocess
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')

D_BASE = {
    'america_first':      [False] * 5,
    'life':               [False] * 5,
    'immigration':        [False] * 5,
    'marriage':           [False] * 5,
    'self_defense':       [False] * 5,
    'education':          [False] * 5,
    'christian_heritage': [None] * 5,
}
RATIONALE = (
    "Party-default scoring (D) for a Soros-funded prosecutor. "
    "These records can be promoted to evidence-reviewed via the "
    "claim pipeline as specific charging-policy decisions and "
    "case-disposition records are documented."
)

NEW = [
    {'name':'Alvin Bragg', 'slug':'alvin-bragg', 'state':'NY',
     'office':'Manhattan District Attorney', 'jurisdiction':'New York County, NY'},
    {'name':'George Gascón', 'slug':'george-gascon', 'state':'CA',
     'office':'Los Angeles County District Attorney (former)', 'jurisdiction':'Los Angeles County, CA',
     'note_extra': 'Lost re-election November 2024.'},
    {'name':'Kim Foxx', 'slug':'kim-foxx', 'state':'IL',
     'office':"Cook County State's Attorney (former)", 'jurisdiction':'Cook County, IL',
     'note_extra': 'Term ended December 2024; succeeded by Eileen O\'Neill Burke.'},
    {'name':'Larry Krasner', 'slug':'larry-krasner', 'state':'PA',
     'office':'Philadelphia District Attorney', 'jurisdiction':'Philadelphia, PA'},
    {'name':'Kim Gardner', 'slug':'kim-gardner', 'state':'MO',
     'office':'St. Louis Circuit Attorney (former)', 'jurisdiction':'St. Louis, MO',
     'note_extra': 'Resigned May 2023 amid Missouri AG suit.'},
]


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)
    next_id = max((c.get('id', 0) for c in sc['candidates']), default=0) + 1
    existing = {(c.get('slug'), c.get('state')) for c in sc['candidates']}
    today = date.today().isoformat()

    added = 0
    for rec in NEW:
        if (rec['slug'], rec['state']) in existing:
            print(f'Skip (exists): {rec["slug"]}')
            continue
        cand = {
            'name': rec['name'],
            'slug': rec['slug'],
            'office': rec['office'],
            'jurisdiction': rec['jurisdiction'],
            'level': 'local',
            'party': 'D',
            'district': None,
            'state': rec['state'],
            'id': next_id,
            'scores': {k: list(v) for k,v in D_BASE.items()},
            'notes': (
                f"Soros-funded prosecutor (see data/soros_adjustments.json for "
                f"the documented contribution total). Party-default(D) "
                f"scoring applied as a baseline; the Soros adjustment "
                f"layer adds the specific score penalty. "
                + (rec.get('note_extra') or '')
            ).strip(),
            'photo': None,
            'website': None,
            'sources': [
                'https://www.opensecrets.org/political-action-committees-pacs/look-up/Soros',
            ],
            'profile': {
                'confidence': 'party_default',
                'scoring_rationale': RATIONALE,
                'seeded_on': today,
                'seat_up_next': False,
            },
        }
        sc['candidates'].append(cand)
        next_id += 1
        added += 1
        print(f'Added: {rec["name"]} ({rec["state"]}) — {rec["office"]}')

    sc['meta']['total_candidates'] = len(sc['candidates'])
    sc['meta']['last_updated'] = today
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    print(f'\nAdded {added} record(s).')
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
