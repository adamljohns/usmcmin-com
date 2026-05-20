#!/usr/bin/env python3
"""
add-fl-retiring-house-successors-2026.py — FL-02, FL-11, FL-16 successor candidates.

Neal Dunn (FL-2), Daniel Webster (FL-11), and Vern Buchanan (FL-16) are
retiring 2026. This adds named R primary + D candidates for those open seats.
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
            'confidence_note': f'2026-05-20 — open-seat successor placeholder ({state}-{district}). Archetype: {archetype}.' if archetype else '2026-05-20 — open-seat successor placeholder.',
            **(profile_extra or {}),
        },
    }

RECORDS = [
    # ══ FL-02 (R Neal Dunn retiring · safe R · 8/18 primary) ══
    rec('Jay Trumbull', 'jay-trumbull', 'FL', 2,
        'U.S. Representative FL-02 (2026 R Candidate · FL state senator · Dunn-seat open)',
        'R', 'maga_conservative_r', '2026-08-18',
        notes=('Florida state senator (Panama City area, since 2022). Former FL House. R primary '
               'candidate for FL-02 open seat (Neal Dunn retiring).'),
        sources=['https://ballotpedia.org/Jay_Trumbull']),
    rec('Drew Wilson', 'drew-wilson-fl-02', 'FL', 2,
        'U.S. Representative FL-02 (2026 R Candidate · businessman · Dunn-seat open)',
        'R', 'establishment_r', '2026-08-18',
        notes='Panama City-area businessman. R primary candidate for FL-02 open seat 2026.',
        sources=['https://ballotpedia.org/Drew_Wilson']),

    # ══ FL-11 (R Daniel Webster retiring · safe R Villages district · 8/18) ══
    rec('Randy Fine', 'randy-fine-fl-11', 'FL', 11,
        'U.S. Representative FL-11 (2026 R Candidate · former FL state senator · vocal MAGA voice)',
        'R', 'maga_conservative_r', '2026-08-18',
        notes=('Former FL state senator. Already won 2025 FL-06 special election after Mike Waltz '
               'resignation (replacing Cory Mills). May run for Webster\'s safe FL-11 in 2026 '
               '(or stay in FL-06). Trump-endorsed populist.'),
        sources=['https://ballotpedia.org/Randy_Fine']),
    rec('Anthony Sabatini', 'anthony-sabatini-fl-11', 'FL', 11,
        'U.S. Representative FL-11 (2026 R Candidate · former FL state rep · MAGA conservative)',
        'R', 'maga_conservative_r', '2026-08-18',
        notes=('Former Florida state representative. 2022 R candidate for FL-07 (lost primary). '
               'Lake County-area MAGA conservative. R candidate for FL-11 open seat 2026.'),
        sources=['https://ballotpedia.org/Anthony_Sabatini']),

    # ══ FL-16 (R Vern Buchanan retiring · safe R Sarasota district · 8/18) ══
    rec('Joe Gruters', 'joe-gruters-fl-16', 'FL', 16,
        'U.S. Representative FL-16 (2026 R Candidate · FL state senator · former FL GOP chair)',
        'R', 'maga_conservative_r', '2026-08-18',
        notes=('Florida state senator (Sarasota). Former chair of Florida Republican Party '
               '(2019-2023). Trump campaign co-chair in FL. R candidate for FL-16 open seat 2026 '
               '(Buchanan retiring).'),
        sources=['https://ballotpedia.org/Joe_Gruters']),
    rec('Fiona McFarland', 'fiona-mcfarland-fl-16', 'FL', 16,
        'U.S. Representative FL-16 (2026 R Candidate · FL state rep · Navy vet)',
        'R', 'establishment_r', '2026-08-18',
        notes=('Florida state representative (Sarasota). Navy veteran. Daughter of pollster '
               'Whit Ayres. R candidate for FL-16 open seat 2026.'),
        sources=['https://ballotpedia.org/Fiona_McFarland']),
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
        print(f'  {action} {r["name"]:<28s} ({r["state"]}-{r["district"]:02d} {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
