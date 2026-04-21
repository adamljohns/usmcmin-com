#!/usr/bin/env python3
"""
add-brevard-const-officers.py — add Brevard County's three remaining
directly-elected constitutional officers (other than Sheriff + Supervisor
of Elections, already in place):

  - Clerk of the Courts: Rachel Sadoff (verified via brevardclerk.us —
    page title "Brevard County, Florida - Clerk of the Court" with
    "Clerk Sadoff" in the welcome copy)
  - Tax Collector: Lisa Cullen, CFC (verified via brevardtaxcollector.com —
    page title "Brevard County Tax Collector - Lisa Cullen, CFC")
  - Property Appraiser: Dana Blickley (verified — has a dedicated
    Wikipedia article at en.wikipedia.org/wiki/Dana_Blickley)

All three are Republicans. Brevard constitutional officer elections run
on 4-year cycles, usually midterm (so up in 2024, next 2028).

Brevard Constitutional Officers (for future reference, now complete):
  Sheriff            Wayne Ivey       (already added)
  Supervisor of Elections Tim Bobanic (already added)
  Clerk of Courts    Rachel Sadoff    (THIS commit)
  Tax Collector      Lisa Cullen      (THIS commit)
  Property Appraiser Dana Blickley    (THIS commit)
"""
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'

CONSERVATIVE_R = {
    "america_first": [True, True, True, None, True],
    "life": [True, True, True, True, True],
    "immigration": [True, True, None, None, None],
    "marriage": [True, True, True, True, False],
    "christian_heritage": [False, False, False, False, False],
    "self_defense": [True, True, True, True, True],
    "education": [True, True, True, None, True]
}


def slugify(name):
    return (name.lower().replace(' ', '-').replace('.', '').replace("'", '')
              .replace(',', '').replace('"', '').replace('—', '-'))


def make(name, office, party, notes, sources, profile_extra=None):
    scores = {k: list(v) for k, v in CONSERVATIVE_R.items()} if party == 'R' \
             else {k: [None]*5 for k in CONSERVATIVE_R}
    profile = {
        'religion': None, 'net_worth': None, 'birthplace': None,
        'education': None, 'background': None,
        'prev_election_opponent': None,
        'next_election_year': 2028,
        'next_election_contenders': [],
        'next_election_date': '2028-11-07',
        'next_election_type': 'general',
        'seat_up_next': False,  # Elected 2024, not up 2026
    }
    if profile_extra:
        profile.update(profile_extra)
    return {
        'name': name,
        'slug': slugify(name),
        'office': office,
        'jurisdiction': 'Brevard County',
        'level': 'local',
        'party': party,
        'district': None,
        'state': 'FL',
        'scores': scores,
        'notes': notes,
        'photo': None,
        'website': None,
        'sources': sources,
        'profile': profile,
    }


NEW = [
    make(
        'Rachel Sadoff',
        'Clerk of the Courts',
        'R',
        notes=(
            'Brevard County Clerk of the Courts. Directly elected constitutional '
            'officer responsible for court records, official county records, '
            'real estate recordings, county finances, and minutes of the Board '
            'of County Commissioners. Longtime Brevard clerk office career.'
        ),
        sources=[
            'https://www.brevardclerk.us/',
            'https://ballotpedia.org/Rachel_Sadoff',
        ],
        profile_extra={'background': 'Brevard County Clerk of the Courts.'},
    ),
    make(
        'Lisa Cullen',
        'Tax Collector',
        'R',
        notes=(
            'Brevard County Tax Collector, CFC (Certified Florida Collector). '
            'Directly elected constitutional officer; the tax collector '
            'administers property tax collection, driver license and tag '
            'services, business tax receipts, and hunting/fishing licenses '
            'for the county.'
        ),
        sources=[
            'https://www.brevardtaxcollector.com/',
            'https://ballotpedia.org/Lisa_Cullen',
        ],
        profile_extra={'background': 'Brevard County Tax Collector (CFC).'},
    ),
    make(
        'Dana Blickley',
        'Property Appraiser',
        'R',
        notes=(
            'Brevard County Property Appraiser, CFA (Certified Florida '
            'Appraiser). Directly elected constitutional officer responsible '
            'for determining the just value of all real and tangible personal '
            'property in the county, administering homestead and other '
            'property tax exemptions, and maintaining property ownership '
            'records. In office since 2013.'
        ),
        sources=[
            'https://www.bcpao.us/',
            'https://en.wikipedia.org/wiki/Dana_Blickley',
            'https://ballotpedia.org/Dana_Blickley',
        ],
        profile_extra={
            'background': 'Brevard County Property Appraiser since 2013.',
        },
    ),
]


def main():
    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    max_id = max(c.get('id', 0) for c in data['candidates'])
    next_id = max_id + 1
    existing = {(c['name'], c.get('state'), c.get('office')) for c in data['candidates']}

    added = 0
    for c in NEW:
        key = (c['name'], c.get('state'), c.get('office'))
        if key in existing:
            print(f"  SKIP (exists): {c['name']} / {c['office']}")
            continue
        c['id'] = next_id
        next_id += 1
        data['candidates'].append(c)
        added += 1
        print(f"  ADD: {c['name']} ({c['office']})")

    data['meta']['total_candidates'] = len(data['candidates'])
    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"\nAdded: {added}. New total: {len(data['candidates'])}")

    print('Rebuilding per-state files...')
    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
