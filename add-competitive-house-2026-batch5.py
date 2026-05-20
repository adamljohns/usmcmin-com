#!/usr/bin/env python3
"""
add-competitive-house-2026-batch5.py — Pass 3 (competitive district primaries).

Focuses on PA-07 + PA-10 D primary challengers to R incumbents Mackenzie + Perry.
PA primary was May 19 2026 (yesterday). Both Mackenzie + Perry ran unopposed.

Also adds a few D-side primary candidates for top-rated toss-up + lean-R districts
where the R incumbent runs unopposed:
  - PA-07 D primary (vs Mackenzie): Obando-Derstine, Brooks, McClure, Crosswell
  - PA-10 D primary (vs Perry): Douglas, Stelson
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None

ARCHETYPES_ESTABLISHMENT_D = {
    'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
    'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
    'economic_stewardship':[F,F,F,F,F],'election_integrity':[F,F,F,F,F],
    'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
    'foreign_policy_restraint':[F,F,F,F,F],'industry_capture':[F,F,F,F,F],
}

def empty_scores():
    return {cid: [None]*5 for cid in [
        'sanctity_of_life','biblical_marriage','family_child_sovereignty','christian_liberty',
        'economic_stewardship','election_integrity','border_immigration','self_defense',
        'foreign_policy_restraint','industry_capture',
    ]}

def rec(name, slug, state, district, office, party, archetype=None, primary_date='', notes='',
        sources=None, profile_extra=None, candidacy_status='primary_candidate'):
    scores = ({cid: list(row) for cid, row in ARCHETYPES_ESTABLISHMENT_D.items()}
              if archetype == 'establishment_d' else empty_scores())
    return {
        'name': name, 'slug': slug, 'state': state,
        'office': office, 'jurisdiction': 'United States House of Representatives',
        'party': party, 'level': 'federal', 'district': district,
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '', 'sources': sources or [f'https://ballotpedia.org/{state}_{district}_2026'],
        'notes': notes, 'footnotes': [], 'answer_footnotes': {},
        'scores': scores,
        'profile': {
            'next_election': 2026, 'next_election_type': 'primary',
            'seat_up_next': True, 'next_election_date': primary_date,
            'confidence': 'archetype_curated' if archetype else 'low_evidence',
            'confidence_note': (f'2026-05-20 — ingested for 2026 competitive district challenger ({state}-{district}). Archetype: {archetype}.' if archetype else '2026-05-20 — competitive-district placeholder.'),
            **(profile_extra or {}),
        },
    }


RECORDS = [
    # PA-07 (R incumbent Ryan Mackenzie · Cook toss-up · D primary 5/19 just held)
    rec('Carol Obando-Derstine', 'carol-obando-derstine', 'PA', 7,
        'U.S. Representative PA-07 (2026 D Candidate · challenger to Mackenzie · Cook toss-up)',
        'D', 'establishment_d', '2026-05-19',
        notes='D primary candidate challenging Rep. Ryan Mackenzie (R) in Cook-rated toss-up PA-07.',
        sources=['https://ballotpedia.org/Carol_Obando-Derstine',
                 "https://ballotpedia.org/Pennsylvania's_7th_Congressional_District_election,_2026_(May_19_Democratic_primary)"]),
    rec('Bob Brooks', 'bob-brooks-pa-07', 'PA', 7,
        'U.S. Representative PA-07 (2026 D Candidate · challenger to Mackenzie · Cook toss-up)',
        'D', 'establishment_d', '2026-05-19',
        notes='D primary candidate in PA-07 challenging Ryan Mackenzie.'),
    rec('Lamont McClure', 'lamont-mcclure', 'PA', 7,
        'U.S. Representative PA-07 (2026 D Candidate · Northampton Co Executive · challenger to Mackenzie)',
        'D', 'establishment_d', '2026-05-19',
        notes='Northampton County Executive. D primary candidate in PA-07 challenging Mackenzie.',
        sources=['https://ballotpedia.org/Lamont_McClure']),
    rec('Ryan Crosswell', 'ryan-crosswell', 'PA', 7,
        'U.S. Representative PA-07 (2026 D Candidate · challenger to Mackenzie · Cook toss-up)',
        'D', 'establishment_d', '2026-05-19',
        notes='D primary candidate in PA-07 challenging Mackenzie.'),

    # PA-10 (R incumbent Scott Perry · Cook toss-up · D primary 5/19 just held)
    rec('Janelle Stelson', 'janelle-stelson', 'PA', 10,
        'U.S. Representative PA-10 (2026 D Candidate · former TV news anchor · 2024 nominee · Cook toss-up)',
        'D', 'establishment_d', '2026-05-19',
        notes=('Former TV news anchor. 2024 D nominee against Scott Perry (lost 50.7-49.3). '
               'Running again in 2026 D primary for PA-10 — a top Cook-rated toss-up district.'),
        sources=['https://ballotpedia.org/Janelle_Stelson']),
    rec('Justin Douglas', 'justin-douglas-pa-10', 'PA', 10,
        'U.S. Representative PA-10 (2026 D Candidate · Dauphin County Commissioner · Cook toss-up)',
        'D', 'establishment_d', '2026-05-19',
        notes='Dauphin County Commissioner. D primary candidate in PA-10 challenging Scott Perry.',
        sources=['https://ballotpedia.org/Justin_Douglas']),
]


def upsert(cands, record):
    key = (record['state'], record['slug'])
    for i, c in enumerate(cands):
        if (c.get('state'), c.get('slug')) == key:
            cands[i] = record
            return 'REPLACED'
    cands.append(record)
    return 'INSERTED'


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']
    n_before = len(cands)
    for r in RECORDS:
        action = upsert(cands, r)
        print(f'  {action} {r["name"]:<30s} ({r["state"]}-{r["district"]:02d} {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
