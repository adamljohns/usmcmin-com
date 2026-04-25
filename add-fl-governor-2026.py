#!/usr/bin/env python3
"""
add-fl-governor-2026.py — seed the FL Governor 2026 race.

Three new candidates for scorecard.json (Paul Renner, David Jolly,
Jason Pizzo). The other two leading candidates (Byron Donalds, Jay
Collins) already exist in the scorecard.

All five candidates get a `candidacy` block on their `profile`
identifying them as candidates for the 2026 FL Governor race. Plus
data/races.json gets a new race entry that the new /compare.html
view consumes.

Sources verified 2026-04-25 against Wikipedia.

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

# Three new records (Renner, Jolly, Pizzo).
NEW_CANDIDATES = [
    {
        'name': 'Paul Renner',
        'slug': 'paul-renner',
        'office': 'Candidate for Governor of Florida',
        'jurisdiction': 'State of Florida',
        'level': 'state',
        'party': 'R',
        'district': None,
        'state': 'FL',
        'scores': {cat: [None]*5 for cat in [
            'america_first','life','immigration','marriage',
            'self_defense','education','christian_heritage'
        ]},
        'notes': (
            "Declared 2026 Florida gubernatorial candidate (announced "
            "September 3, 2025). 103rd Speaker of the Florida House of "
            "Representatives (2022-2024); state representative for "
            "House District 19 (2015-2024). RESOLUTE Citizen scoring "
            "pass not yet completed; record carries the Awaiting-review "
            "banner until evidence is added."
        ),
        'photo': None,
        'website': 'https://www.paulrenner.com',
        'sources': [
            'https://en.wikipedia.org/wiki/Paul_Renner_(politician)',
            'https://en.wikipedia.org/wiki/2026_Florida_gubernatorial_election',
            'https://ballotpedia.org/Paul_Renner',
        ],
        'profile': {
            'religion': None,
            'birthplace': 'Atlanta, Georgia',
            'education': 'Davidson College (BA History, 1989); University of Florida Levin College of Law (JD, 1994)',
            'background': (
                'Florida State House Speaker (2022-2024), state representative '
                '(2015-2024). Former U.S. Navy JAG officer.'
            ),
            'next_election_year': 2026,
            'next_election_date': PRIMARY_DATE,
            'next_election_type': 'primary',
            'seat_up_next': True,
            'candidacy': {
                'race_id': RACE_ID,
                'office': 'Governor of Florida',
                'primary_date': PRIMARY_DATE,
                'general_date': GENERAL_DATE,
                'is_incumbent': False,
                'declared_date': '2025-09-03',
            },
        },
    },
    {
        'name': 'David Jolly',
        'slug': 'david-jolly',
        'office': 'Candidate for Governor of Florida',
        'jurisdiction': 'State of Florida',
        'level': 'state',
        'party': 'D',
        'district': None,
        'state': 'FL',
        'scores': {cat: [None]*5 for cat in [
            'america_first','life','immigration','marriage',
            'self_defense','education','christian_heritage'
        ]},
        'notes': (
            "Declared 2026 Florida gubernatorial candidate (announced "
            "June 2025). Former U.S. Representative for Florida's 13th "
            "congressional district (2014-2017). Registered Republican "
            "1985-2018, Independent 2018-2022, Forward Party 2022-2025, "
            "Democratic Party since April 2025. Stated public-position "
            "shifts: now pro-choice (codifying Roe v. Wade); now "
            "supports licensing/registration/insurance for firearms "
            "and an assault-weapons ban. RESOLUTE scoring pass pending; "
            "Awaiting-review banner active until evidence is added."
        ),
        'photo': None,
        'website': 'https://www.davidjollyforflorida.com',
        'sources': [
            'https://en.wikipedia.org/wiki/David_Jolly',
            'https://en.wikipedia.org/wiki/2026_Florida_gubernatorial_election',
            'https://ballotpedia.org/David_Jolly',
        ],
        'profile': {
            'religion': None,
            'birthplace': 'Dunedin, Florida',
            'education': 'Emory University (BA, 1994); George Mason University School of Law (JD, 2001)',
            'background': (
                'U.S. Representative FL-13 (2014-2017). Lobbyist and political '
                'analyst between congressional service and gubernatorial run. '
                'Party history: Republican (1985-2018), Independent (2018-2022), '
                'Forward Party (2022-2025), Democrat (April 2025-present).'
            ),
            'next_election_year': 2026,
            'next_election_date': PRIMARY_DATE,
            'next_election_type': 'primary',
            'seat_up_next': True,
            'candidacy': {
                'race_id': RACE_ID,
                'office': 'Governor of Florida',
                'primary_date': PRIMARY_DATE,
                'general_date': GENERAL_DATE,
                'is_incumbent': False,
                'declared_date': '2025-06-15',
            },
        },
    },
    {
        'name': 'Jason Pizzo',
        'slug': 'jason-pizzo',
        'office': 'Candidate for Governor of Florida',
        'jurisdiction': 'State of Florida',
        'level': 'state',
        'party': 'I',
        'district': None,
        'state': 'FL',
        'scores': {cat: [None]*5 for cat in [
            'america_first','life','immigration','marriage',
            'self_defense','education','christian_heritage'
        ]},
        'notes': (
            "Declared 2026 Florida gubernatorial candidate as an "
            "Independent (announced May 9, 2025). Florida State Senator "
            "for District 37 since 2018; served as Senate Minority Leader "
            "2024-2025. Switched from Democratic to Independent on April "
            "24, 2025. Formerly an assistant state attorney for the "
            "Miami-Dade State Attorney's Office. RESOLUTE scoring pass "
            "pending."
        ),
        'photo': None,
        'website': 'https://www.jasonpizzo.com',
        'sources': [
            'https://en.wikipedia.org/wiki/Jason_Pizzo',
            'https://en.wikipedia.org/wiki/2026_Florida_gubernatorial_election',
            'https://ballotpedia.org/Jason_Pizzo',
        ],
        'profile': {
            'religion': None,
            'birthplace': 'Somerville, New Jersey',
            'education': 'New York University (BA); Columbia University (MA); University of Miami (JD)',
            'background': (
                'Florida State Senator District 37 (2018-present). Senate '
                'Minority Leader 2024-2025 (D). Former Miami-Dade assistant '
                'state attorney.'
            ),
            'next_election_year': 2026,
            'next_election_date': PRIMARY_DATE,
            'next_election_type': 'primary',
            'seat_up_next': True,
            'candidacy': {
                'race_id': RACE_ID,
                'office': 'Governor of Florida',
                'primary_date': PRIMARY_DATE,
                'general_date': GENERAL_DATE,
                'is_incumbent': False,
                'declared_date': '2025-05-09',
                'party_switch_date': '2025-04-24',
            },
        },
    },
]

# Existing candidates we just need to tag with `candidacy`. Keys = slug.
EXISTING_CANDIDACY_TAGS = {
    'byron-donalds': {
        'race_id': RACE_ID,
        'office': 'Governor of Florida',
        'primary_date': PRIMARY_DATE,
        'general_date': GENERAL_DATE,
        'is_incumbent': False,
        'declared_date': '2025-02-25',
        'note': 'Endorsed by President Donald Trump.',
    },
    'jay-collins': {
        'race_id': RACE_ID,
        'office': 'Governor of Florida',
        'primary_date': PRIMARY_DATE,
        'general_date': GENERAL_DATE,
        'is_incumbent': False,
        'declared_date': '2025-08-15',
        'note': 'Currently the 21st Lieutenant Governor of Florida.',
    },
}


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)

    next_id = max((c.get('id', 0) for c in sc['candidates']), default=0) + 1
    existing_keys = {(c.get('slug'), c.get('state')) for c in sc['candidates']}

    added = 0
    for rec in NEW_CANDIDATES:
        if (rec['slug'], rec['state']) in existing_keys:
            print(f'Skip (exists): {rec["slug"]}')
            continue
        rec['id'] = next_id
        next_id += 1
        sc['candidates'].append(rec)
        added += 1
        print(f'Added: {rec["name"]} ({rec["party"]}) — {rec["office"]}')

    tagged = 0
    for c in sc['candidates']:
        slug = c.get('slug')
        if slug in EXISTING_CANDIDACY_TAGS:
            prof = c.setdefault('profile', {})
            prof['candidacy'] = EXISTING_CANDIDACY_TAGS[slug]
            tagged += 1
            print(f'Tagged candidacy: {c.get("name")} ({c.get("state")})')

    sc.setdefault('meta', {})
    sc['meta']['total_candidates'] = len(sc['candidates'])
    sc['meta']['last_updated'] = date.today().isoformat()
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    print(f'\nAdded {added} candidate(s); tagged {tagged} existing.')

    # Now write data/races.json with the FL Gov 2026 race definition.
    race_doc = {
        '_meta': {
            'description': (
                'Race manifest for /compare.html. Each race entry lists the '
                'office, election dates, incumbent (if any), and the slugs '
                'of declared candidates grouped by party. Only the leading '
                'candidates per primary are listed by default; minor '
                'candidates can be added by hand or via a future updater.'
            ),
            'updated': date.today().isoformat(),
        },
        'races': {
            RACE_ID: {
                'race_id': RACE_ID,
                'office': 'Governor of Florida',
                'state': 'FL',
                'primary_date': PRIMARY_DATE,
                'general_date': GENERAL_DATE,
                'incumbent': None,   # Term-limited DeSantis cannot run
                'incumbent_note': 'Ron DeSantis (R) is term-limited.',
                'candidates_by_party': {
                    'R': ['byron-donalds', 'jay-collins', 'paul-renner'],
                    'D': ['david-jolly'],
                    'I': ['jason-pizzo'],
                },
                'sources': [
                    'https://en.wikipedia.org/wiki/2026_Florida_gubernatorial_election',
                    'https://ballotpedia.org/Gubernatorial_election_in_Florida,_2026',
                ],
            },
        },
    }
    if os.path.exists(RACES):
        with open(RACES, 'r', encoding='utf-8') as f:
            existing = json.load(f)
        existing.setdefault('races', {})[RACE_ID] = race_doc['races'][RACE_ID]
        existing.setdefault('_meta', {}).update(race_doc['_meta'])
        race_doc = existing
    with open(RACES, 'w', encoding='utf-8') as f:
        json.dump(race_doc, f, indent=2, ensure_ascii=False)
    print(f'Wrote {RACES}')

    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
