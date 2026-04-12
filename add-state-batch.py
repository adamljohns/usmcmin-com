#!/usr/bin/env python3
"""
Add a batch of states from a research JSON file into scorecard.json.
Usage: python3 add-state-batch.py <input_file.json>

The input file should have structure:
{
  "ST": {
    "statewide": [...],
    "us_senators": [...],
    "us_house": [...],
    "state_senate": [...],
    "state_house": [...]
  },
  ...
}
"""
import json
import sys
import os

# State name mappings
STATE_NAMES = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
    'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
    'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
    'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
    'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
    'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'District of Columbia'
}

# Senate names by state
SENATE_NAMES = {
    'SC': 'South Carolina State Senate', 'GA': 'Georgia State Senate',
    'TN': 'Tennessee State Senate', 'KY': 'Kentucky State Senate',
    'PA': 'Pennsylvania State Senate', 'OH': 'Ohio State Senate',
    'FL': 'Florida State Senate', 'AL': 'Alabama State Senate',
    'MS': 'Mississippi State Senate', 'LA': 'Louisiana State Senate',
    'NC': 'North Carolina State Senate', 'MD': 'Maryland State Senate',
    'WV': 'West Virginia State Senate',
}

HOUSE_NAMES = {
    'SC': 'South Carolina House of Representatives', 'GA': 'Georgia House of Representatives',
    'TN': 'Tennessee House of Representatives', 'KY': 'Kentucky House of Representatives',
    'PA': 'Pennsylvania House of Representatives', 'OH': 'Ohio House of Representatives',
    'FL': 'Florida House of Representatives', 'AL': 'Alabama House of Representatives',
    'MS': 'Mississippi House of Representatives', 'LA': 'Louisiana House of Representatives',
    'NC': 'North Carolina House of Representatives', 'MD': 'Maryland House of Delegates',
    'WV': 'West Virginia House of Delegates',
}

CONSERVATIVE_R = {
    "america_first": [True, True, True, None, True],
    "life": [True, True, True, True, True],
    "immigration": [True, True, None, None, None],
    "marriage": [True, True, True, True, False],
    "christian_heritage": [False, False, False, False, False],
    "self_defense": [True, True, True, True, True],
    "education": [True, True, True, None, True]
}
DEMOCRAT = {
    "america_first": [False, False, True, None, False],
    "life": [False, False, False, False, False],
    "immigration": [False, False, False, False, False],
    "marriage": [False, False, False, False, False],
    "christian_heritage": [False, False, False, False, False],
    "self_defense": [False, False, False, False, False],
    "education": [False, False, False, False, False]
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 add-state-batch.py <input_file.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scorecard_path = os.path.join(base_dir, 'data', 'scorecard.json')

    with open(scorecard_path, 'r') as f:
        data = json.load(f)

    with open(input_file, 'r') as f:
        batch = json.load(f)

    max_id = max(c['id'] for c in data['candidates'])
    next_id = max_id + 1
    total_added = 0

    for state_code, state_data in batch.items():
        if state_code in ('metadata', 'summary'):
            continue

        state_name = STATE_NAMES.get(state_code, state_code)
        senate_name = SENATE_NAMES.get(state_code, f'{state_name} State Senate')
        house_name = HOUSE_NAMES.get(state_code, f'{state_name} House of Representatives')

        section_map = {
            'statewide': (f'State of {state_name}', 'state'),
            'us_senators': ('United States Senate', 'federal'),
            'us_house': ('United States House of Representatives', 'federal'),
            'state_senate': (senate_name, 'state'),
            'state_house': (house_name, 'state'),
        }

        count = 0
        for section, (jurisdiction, level) in section_map.items():
            items = state_data.get(section, [])
            if not isinstance(items, list):
                continue

            for raw in items:
                name = raw.get('name', '')
                if not name or name.lower() in ('vacant', 'tbd', ''):
                    continue

                slug = name.lower().replace(' ', '-').replace('.', '').replace("'", '').replace(',', '').replace('"', '')
                party = raw.get('party', 'Unknown')

                office = raw.get('office', '')
                if not office:
                    district = raw.get('district')
                    if section == 'us_house' and district:
                        office = f"U.S. House — District {district}"
                    elif section == 'state_senate' and district:
                        office = f"State Senate — District {district}"
                    elif section == 'state_house' and district:
                        office = f"State House — District {district}"

                if party == 'R':
                    scores = {k: list(v) for k, v in CONSERVATIVE_R.items()}
                elif party == 'D':
                    scores = {k: list(v) for k, v in DEMOCRAT.items()}
                else:
                    scores = {k: [None]*5 for k in CONSERVATIVE_R}

                c = {
                    "name": name, "slug": slug, "office": office,
                    "jurisdiction": jurisdiction, "level": level,
                    "party": party, "district": raw.get('district'),
                    "state": state_code, "id": next_id,
                    "scores": scores, "notes": "",
                    "photo": None, "website": None, "sources": [],
                    "profile": {
                        "religion": None, "net_worth": None, "birthplace": None,
                        "education": None, "background": None,
                        "prev_election_opponent": None, "next_election_year": None,
                        "next_election_contenders": []
                    }
                }
                data['candidates'].append(c)
                next_id += 1
                count += 1

        if state_code not in data['meta']['states']:
            data['meta']['states'].append(state_code)
        total_added += count
        print(f'  {state_code} ({state_name}): {count} candidates')

    data['meta']['total_candidates'] = len(data['candidates'])

    with open(scorecard_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f'\nTotal added: {total_added}')
    print(f'Grand total: {len(data["candidates"])} candidates across {len(data["meta"]["states"])} states')

if __name__ == '__main__':
    main()
