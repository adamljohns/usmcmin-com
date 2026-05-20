#!/usr/bin/env python3
"""
add-competitive-house-2026-batch7.py — Pass 3 final expansion batch.

More competitive swing-district challengers across NJ/NY/PA/OH.
~15 records, focused on candidates with concrete public profiles.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None

ARCHETYPES = {
    'maga_conservative_r': {
        'sanctity_of_life':[T,T,T,T,T],'biblical_marriage':[T,T,T,T,T],
        'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,N],
        'economic_stewardship':[T,N,T,N,T],'election_integrity':[N,T,N,T,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
        'foreign_policy_restraint':[N,N,N,F,N],'industry_capture':[N,N,N,T,N],
    },
    'establishment_r': {
        'sanctity_of_life':[T,F,T,T,T],'biblical_marriage':[N,F,T,N,N],
        'family_child_sovereignty':[N,N,T,N,N],'christian_liberty':[T,N,N,N,N],
        'economic_stewardship':[N,F,N,N,F],'election_integrity':[F,T,F,F,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,F,F,T,T],
        'foreign_policy_restraint':[F,F,F,F,F],'industry_capture':[F,F,F,N,F],
    },
    'establishment_d': {
        'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
        'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
        'economic_stewardship':[F,F,F,F,F],'election_integrity':[F,F,F,F,F],
        'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
        'foreign_policy_restraint':[F,F,F,F,F],'industry_capture':[F,F,F,F,F],
    },
    'progressive_d': {
        'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
        'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
        'economic_stewardship':[F,F,F,N,T],'election_integrity':[F,F,F,F,F],
        'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
        'foreign_policy_restraint':[N,T,N,N,N],'industry_capture':[N,F,T,N,T],
    },
}

def scores_from(a): return {cid: list(row) for cid, row in ARCHETYPES[a].items()}
def empty_scores():
    return {cid: [None]*5 for cid in [
        'sanctity_of_life','biblical_marriage','family_child_sovereignty','christian_liberty',
        'economic_stewardship','election_integrity','border_immigration','self_defense',
        'foreign_policy_restraint','industry_capture',
    ]}

def rec(name, slug, state, district, office, party, archetype=None, primary_date='', notes='',
        sources=None, profile_extra=None, candidacy_status='primary_candidate'):
    return {
        'name': name, 'slug': slug, 'state': state,
        'office': office, 'jurisdiction': 'United States House of Representatives',
        'party': party, 'level': 'federal', 'district': district,
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '', 'sources': sources or [f'https://ballotpedia.org/{state}_{district}_2026'],
        'notes': notes, 'footnotes': [], 'answer_footnotes': {},
        'scores': scores_from(archetype) if archetype else empty_scores(),
        'profile': {
            'next_election': 2026, 'next_election_type': 'primary',
            'seat_up_next': True, 'next_election_date': primary_date,
            'confidence': 'archetype_curated' if archetype else 'low_evidence',
            'confidence_note': f'2026-05-20 — competitive district challenger ({state}-{district}). Archetype: {archetype}.' if archetype else '2026-05-20 — competitive district placeholder.',
            **(profile_extra or {}),
        },
    }

RECORDS = [
    # ══ NY-04 (D incumbent Gillen · D primary 6/23) ══
    rec('Taylor Darling', 'taylor-darling', 'NY', 4,
        'U.S. Representative NY-04 (2026 D Candidate · challenger to Gillen · former NY Assembly)',
        'D', 'establishment_d', '2026-06-23',
        notes='Former NY State Assembly member (District 18, 2019-2024). D primary challenger to incumbent Rep. Laura Gillen.',
        sources=['https://ballotpedia.org/Taylor_Darling']),
    rec('Gian Jones', 'gian-jones', 'NY', 4,
        'U.S. Representative NY-04 (2026 D Candidate · challenger to Gillen · businessman)',
        'D', 'establishment_d', '2026-06-23',
        notes='Businessman. D primary challenger to incumbent Rep. Laura Gillen.',
        sources=['https://ballotpedia.org/Gian_Jones']),

    # ══ PA-08 (R incumbent Bresnahan · D primary 5/19 DONE) ══
    rec('Paige Cognetti', 'paige-cognetti', 'PA', 8,
        'U.S. Representative PA-08 (2026 D Nominee · Scranton Mayor · unopposed D primary)',
        'D', 'establishment_d', '2026-05-19',
        candidacy_status='general_candidate',
        notes=('Mayor of Scranton, PA. Unopposed in 2026 D primary; now nominee against '
               'incumbent R Rep. Rob Bresnahan in November. PA-08 is a top D target.'),
        sources=['https://ballotpedia.org/Paige_Cognetti'],
        profile_extra={'background': 'Mayor of Scranton, PA. D nominee for PA-08 vs Bresnahan.',
                       'next_election_type': 'general', 'next_election_date': '2026-11-03'}),

    # ══ OH-09 (D incumbent Kaptur · R primary 5/5 DONE per OH primary calendar) ══
    rec('Derek Merrin', 'derek-merrin', 'OH', 9,
        'U.S. Representative OH-09 (2026 R Candidate · challenger to Kaptur · 2024 nominee + former state rep)',
        'R', 'maga_conservative_r', '2026-05-05',
        notes=('Former Ohio state representative. 2024 R nominee against Marcy Kaptur (lost '
               'narrowly). Running again in 2026 to challenge Kaptur in OH-09 — one of the '
               'most competitive D-held R-target districts.'),
        sources=['https://ballotpedia.org/Derek_Merrin']),
    rec('Josh Williams', 'josh-williams-oh-09', 'OH', 9,
        'U.S. Representative OH-09 (2026 R Candidate · OH state rep · challenger to Kaptur)',
        'R', 'maga_conservative_r', '2026-05-05',
        notes='Ohio state representative. R primary candidate in OH-09 vs Marcy Kaptur.',
        sources=['https://ballotpedia.org/Josh_Williams_(Ohio)']),
    rec('Madison Sheahan', 'madison-sheahan', 'OH', 9,
        'U.S. Representative OH-09 (2026 R Candidate · former ICE Deputy Director)',
        'R', 'maga_conservative_r', '2026-05-05',
        notes='Former Immigration and Customs Enforcement Deputy Director. R primary candidate in OH-09.',
        sources=['https://ballotpedia.org/Madison_Sheahan']),
    rec('Alea Nadeem', 'alea-nadeem', 'OH', 9,
        'U.S. Representative OH-09 (2026 R Candidate · Air Force veteran)',
        'R', 'maga_conservative_r', '2026-05-05',
        notes='Air Force veteran. R primary candidate in OH-09 challenging Kaptur.',
        sources=['https://ballotpedia.org/Alea_Nadeem']),
    rec('Anthony Campbell', 'anthony-campbell-oh-09', 'OH', 9,
        'U.S. Representative OH-09 (2026 R Candidate · healthcare data exec)',
        'R', 'establishment_r', '2026-05-05',
        notes='Healthcare data science executive. R primary candidate in OH-09.',
        sources=['https://ballotpedia.org/Anthony_Campbell_(Ohio)']),
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
    inserts = replacements = 0
    for r in RECORDS:
        action = upsert(cands, r)
        if action == 'INSERTED':
            inserts += 1
        else:
            replacements += 1
        print(f'  {action} {r["name"]:<30s} ({r["state"]}-{r["district"]:02d} {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
