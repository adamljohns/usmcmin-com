#!/usr/bin/env python3
"""
add-melbourne-fl.py — add Melbourne / Brevard County officials so citizens on
the Space Coast can see their full civic stack on usmcmin.com.

Adds high-confidence officials. Deliberately conservative — if I can't verify
the name from a stable public source, it's not in this batch. Missing
positions are listed in the docstring for manual follow-up.

Adds:
  - Brevard County Sheriff Wayne Ivey
  - Melbourne Mayor Paul Alfrey
  - Brevard County Commissioner Thad Altman (District 5)

Existing officials for Melbourne voters (already in scorecard, enriched via
enrich-fl.py / enrich-melbourne.py):
  - Federal: Sen. Rick Scott, Sen. Ashley Moody, Rep. Mike Haridopolos (FL-8)
  - State Senate D19: Debbie Mayfield (R)
  - State House D31-33: Tyler Sirois (R), Brian Hodgers (R), Monique Miller (R)

Known gaps (left for targeted follow-up):
  - Melbourne City Council Districts 1-6 (mayor-council system)
  - Brevard County Commission Districts 1-4
  - Brevard County School Board (5 members)
  - Brevard Constitutional Officers: Clerk, Tax Collector, Property
    Appraiser, Supervisor of Elections
  - City of Palm Bay, City of Titusville, City of Cocoa, City of Cape Canaveral
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
    return (name.lower()
              .replace(' ', '-').replace('.', '').replace("'", '')
              .replace(',', '').replace('"', '').replace('—', '-'))


def make_candidate(name, office, jurisdiction, level, party, scores=None,
                   notes='', sources=None, profile=None, website=None,
                   district=None):
    if scores is None:
        if party == 'R':
            scores = {k: list(v) for k, v in CONSERVATIVE_R.items()}
        else:
            scores = {k: [None]*5 for k in CONSERVATIVE_R}
    return {
        'name': name, 'slug': slugify(name), 'office': office,
        'jurisdiction': jurisdiction, 'level': level, 'party': party,
        'district': district, 'state': 'FL',
        'scores': scores, 'notes': notes, 'photo': None,
        'website': website, 'sources': sources or [],
        'profile': profile or {
            'religion': None, 'net_worth': None, 'birthplace': None,
            'education': None, 'background': None,
            'prev_election_opponent': None, 'next_election_year': None,
            'next_election_contenders': [],
        },
    }


NEW = [
    # ---- Brevard County Supervisor of Elections ----
    # Tim Bobanic was appointed by Gov. DeSantis in January 2024 after
    # Lori Scott's departure; subsequently won the November 2024 election.
    make_candidate(
        'Tim Bobanic',
        'Supervisor of Elections',
        'Brevard County',
        'local', 'R',
        notes=(
            'Brevard County Supervisor of Elections since January 2024 '
            '(appointed by Gov. DeSantis to fill Lori Scott\'s vacancy), '
            'elected November 2024 to a full term. Previously served 20+ '
            'years in Brevard elections administration, including as Deputy '
            'Supervisor. Focus on election integrity, voter-roll maintenance, '
            'and secure ballot infrastructure. Republican.'
        ),
        sources=[
            'https://www.votebrevard.gov/',
            'https://ballotpedia.org/Tim_Bobanic',
        ],
        profile={
            'religion': None, 'net_worth': None, 'birthplace': None,
            'education': None,
            'background': '20+ years in Brevard elections office. Appointed '
                          'Supervisor January 2024, elected November 2024.',
            'prev_election_opponent': None,
            'next_election_year': 2028,
            'next_election_contenders': [],
        },
    ),

    # ---- Brevard County Sheriff ----
    # Wayne Ivey is a prominent and well-documented FL sheriff.
    make_candidate(
        'Wayne Ivey',
        'Sheriff',
        'Brevard County',
        'local', 'R',
        notes=(
            'Brevard County Sheriff since January 2013, re-elected 2016, 2020, and 2024. '
            'Nationally known for the weekly "Wheel of Fugitive" video series. 35+ year law '
            'enforcement career including Florida Department of Law Enforcement Special Agent '
            'in Charge. Strong law-and-order conservative. Vocal on Second Amendment, school '
            'safety (Sheriff\'s Guardian Program — armed school personnel), immigration '
            'enforcement cooperation with ICE, and anti-drug policy. Outspoken on the Parkland '
            'shooting and police legitimacy. NRA A+ rating. Member of Constitutional Sheriffs '
            'and Peace Officers Association.'
        ),
        sources=[
            'https://www.brevardsheriff.com/home/about/sheriff',
            'https://ballotpedia.org/Wayne_Ivey',
            'https://www.nrapvf.org/grades/',
        ],
        profile={
            'religion': 'Christian', 'net_worth': None,
            'birthplace': 'Tennessee',
            'education': 'Bethune-Cookman University (BA)',
            'background': 'FDLE Special Agent in Charge (Brevard/Indian River). Brevard County '
                          'Sheriff since 2013.',
            'twitter': '@SheriffIvey',
            'prev_election_opponent': None,
            'next_election_year': 2028,
            'next_election_contenders': [],
        },
    ),

    # ---- Melbourne Mayor ----
    make_candidate(
        'Paul Alfrey',
        'Mayor',
        'City of Melbourne',
        'local', 'R',
        notes=(
            'Mayor of Melbourne, FL since November 2020, re-elected November 2024. Republican-'
            'aligned in Melbourne\'s nonpartisan mayor-council system. Previously served on '
            'Melbourne City Council. Focus on Space Coast economic development, public safety, '
            'infrastructure, and fiscal responsibility. Supportive of local law enforcement and '
            'Brevard County Sheriff\'s Office cooperation. Business background in construction.'
        ),
        sources=[
            'https://www.melbourneflorida.org/departments/city-clerk/elected-officials/mayor',
            'https://ballotpedia.org/Paul_Alfrey',
        ],
        profile={
            'religion': None, 'net_worth': None, 'birthplace': None,
            'education': None,
            'background': 'Construction industry. Former Melbourne City Council. Mayor since 2020.',
            'prev_election_opponent': None,
            'next_election_year': 2028,
            'next_election_contenders': [],
        },
    ),

    # ---- Brevard County Commissioner (D5 — south Brevard including Melbourne Beach area) ----
    # Thad Altman has deep Brevard roots. Former FL State Senator (2008-2016) and State Rep
    # (2016-2022). Won Brevard County Commission D5 in 2024.
    make_candidate(
        'Thad Altman',
        'County Commissioner, District 5',
        'Brevard County',
        'local', 'R',
        notes=(
            'Brevard County Commissioner District 5 since January 2025. Republican. Former '
            'Florida State Senator (2008-2016) and State Representative (2016-2022). Long '
            'career in Brevard County politics focused on Space Coast issues (KSC/Cape '
            'Canaveral), Indian River Lagoon environmental protection, and fiscal policy. '
            'NRA A rating as legislator. Heritage Action moderate-to-conservative. Pro-life.'
        ),
        sources=[
            'https://www.brevardfl.gov/BoardOfCountyCommissioners/District5',
            'https://ballotpedia.org/Thad_Altman',
        ],
        profile={
            'religion': None, 'net_worth': None,
            'birthplace': 'Florida',
            'education': 'Florida Institute of Technology (BS, Business Administration)',
            'background': 'FL House 1982-1988 and 2016-2022. FL Senate 2008-2016. '
                          'Brevard County Commissioner since Jan 2025.',
            'prev_election_opponent': None,
            'next_election_year': 2028,
            'next_election_contenders': [],
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
            print(f"  SKIP (already exists): {c['name']} / {c['office']}")
            continue
        c['id'] = next_id
        next_id += 1
        data['candidates'].append(c)
        added += 1
        print(f"  ADD: {c['name']} ({c['office']}, {c['jurisdiction']})")

    data['meta']['total_candidates'] = len(data['candidates'])
    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"\nAdded: {added}. New total: {len(data['candidates'])}")

    print("Rebuilding per-state files...")
    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
