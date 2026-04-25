#!/usr/bin/env python3
"""
add-brevard-cities.py — seed missing Brevard County, FL local officials.

Closes a HANDOFF-flagged gap: Melbourne / Palm Bay / Titusville /
Cocoa / Cape Canaveral all had near-zero scorecard coverage. This
script adds 22 city-government records sourced from Wikipedia and
verified 2026-04-25.

Coverage after this script:
  * Melbourne, FL:      Mayor + 6 council members (1/7 -> 7/7)
  * Palm Bay, FL:       Mayor + Deputy Mayor + 3 council (0/5 -> 5/5)
  * Titusville, FL:     Mayor only (0/5 -> 1/5; remaining 4 unnamed
                        in available sources)
  * Cocoa, FL:          Mayor + 4 council (0/5 -> 5/5)
  * Cape Canaveral, FL: Mayor + Mayor Pro Tem + 3 council (0/5 -> 5/5)

Every new record carries:
  * Awaiting-review banner (all-null scores)
  * Wikipedia + city-website sources
  * level=local, state=FL
  * jurisdiction matches the city name

Run once; idempotent.
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


def make(name, office, juris, sources, term=None, deputy=False, source_note=''):
    base_notes = (
        f"Brevard County local official, {juris}. Sourced from Wikipedia "
        f"and verified 2026-04-25. RESOLUTE Citizen scoring pass not yet "
        f"completed; record carries the Awaiting-review banner until "
        f"evidence is added."
    )
    if source_note:
        base_notes += ' ' + source_note
    return {
        'name': name,
        'slug': name.lower().replace(' ','-').replace('.','').replace("'",''),
        'office': office,
        'jurisdiction': juris,
        'level': 'local',
        'party': None,
        'district': None,
        'state': 'FL',
        'scores': empty_scores(),
        'notes': base_notes,
        'photo': None,
        'website': None,
        'sources': sources,
        'profile': {
            'religion': None,
            'background': None,
            'next_election_year': term,
            'seat_up_next': False,
        },
    }


WIKI_MELBOURNE = 'https://en.wikipedia.org/wiki/Melbourne,_Florida'
WIKI_PALM_BAY  = 'https://en.wikipedia.org/wiki/Palm_Bay,_Florida'
WIKI_TITUSVILLE = 'https://en.wikipedia.org/wiki/Titusville,_Florida'
WIKI_COCOA = 'https://en.wikipedia.org/wiki/Cocoa,_Florida'
WIKI_CC = 'https://en.wikipedia.org/wiki/Cape_Canaveral,_Florida'

CITY_SITES = {
    'Melbourne':      'https://www.melbourneflorida.org',
    'Palm Bay':       'https://www.palmbayflorida.org',
    'Titusville':     'https://www.titusville.com',
    'Cocoa':          'https://www.cocoafl.org',
    'Cape Canaveral': 'https://www.cityofcapecanaveral.org',
}

NEW = []

# --- Melbourne (Mayor Alfrey already in scorecard) ---
M_J = 'City of Melbourne, Florida'
M_S = [WIKI_MELBOURNE, CITY_SITES['Melbourne']]
NEW.append(make('Marcus Smith', 'City Council, District 1', M_J, M_S, term=2028))
NEW.append(make('Mark LaRusso', 'City Council, District 2', M_J, M_S, term=2026))
NEW.append(make('David Neuman', 'City Council, District 3', M_J, M_S, term=2028))
NEW.append(make('Rachael Bassett', 'City Council, District 4', M_J, M_S, term=2026))
NEW.append(make('Mimi Hanley', 'City Council, District 5', M_J, M_S, term=2028))
NEW.append(make('Julie Kennedy', 'City Council, District 6 (Vice Mayor)', M_J, M_S, term=2026))

# --- Palm Bay ---
PB_J = 'City of Palm Bay, Florida'
PB_S = [WIKI_PALM_BAY, CITY_SITES['Palm Bay']]
NEW.append(make('Rob Medina', 'Mayor', PB_J, PB_S))
NEW.append(make('Mike Jaffe', 'Deputy Mayor / City Council', PB_J, PB_S))
NEW.append(make('Kenny Johnson', 'City Council', PB_J, PB_S))
NEW.append(make('Chandler Langevin', 'City Council', PB_J, PB_S))
NEW.append(make('Mike Hammer', 'City Council', PB_J, PB_S))

# --- Titusville (only Mayor known from Wikipedia) ---
TT_J = 'City of Titusville, Florida'
TT_S = [WIKI_TITUSVILLE, CITY_SITES['Titusville']]
NEW.append(make('Andrew Connors', 'Mayor', TT_J, TT_S,
                source_note='Other 4 at-large council members not yet '
                            'extracted from primary sources; this record '
                            'documents only the mayor.'))

# --- Cocoa ---
CO_J = 'City of Cocoa, Florida'
CO_S = [WIKI_COCOA, CITY_SITES['Cocoa']]
NEW.append(make('Michael C. Blake', 'Mayor', CO_J, CO_S))
NEW.append(make('Alex Goins', 'City Council, District 1', CO_J, CO_S))
NEW.append(make('Lavander Hearn', 'City Council, District 2', CO_J, CO_S))
NEW.append(make('Matthew Barringer', 'City Council, District 3', CO_J, CO_S,
                source_note='Appointed following a previous councilmember resignation.'))
NEW.append(make('Lorraine Koss', 'City Council, District 4', CO_J, CO_S))

# --- Cape Canaveral ---
CC_J = 'City of Cape Canaveral, Florida'
CC_S = [WIKI_CC, CITY_SITES['Cape Canaveral']]
NEW.append(make('Wes Morrison', 'Mayor', CC_J, CC_S))
NEW.append(make('Mickie Kellum', 'Mayor Pro Tem / City Council', CC_J, CC_S))
NEW.append(make('Kim Davis', 'City Council', CC_J, CC_S))
NEW.append(make('Kay Jackson', 'City Council', CC_J, CC_S))
NEW.append(make('Don Willis', 'City Council', CC_J, CC_S))


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)

    next_id = max((c.get('id', 0) for c in sc['candidates']), default=0) + 1
    existing_keys = {(c.get('slug'), c.get('state')) for c in sc['candidates']}
    existing_name_juris = {
        (c.get('name','').lower(), (c.get('jurisdiction') or '').lower())
        for c in sc['candidates']
    }

    added = 0
    skipped = 0
    for rec in NEW:
        key = (rec['slug'], rec['state'])
        nj = (rec['name'].lower(), rec['jurisdiction'].lower())
        if key in existing_keys or nj in existing_name_juris:
            skipped += 1
            continue
        rec['id'] = next_id
        next_id += 1
        sc['candidates'].append(rec)
        existing_keys.add(key)
        existing_name_juris.add(nj)
        added += 1
        print(f'Added: {rec["name"]:25s}  {rec["office"]:35s}  ({rec["jurisdiction"]})')

    sc.setdefault('meta', {})
    sc['meta']['total_candidates'] = len(sc['candidates'])
    sc['meta']['last_updated'] = date.today().isoformat()
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    print(f'\nAdded {added} record(s); skipped {skipped} duplicates.')
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
