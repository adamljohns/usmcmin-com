#!/usr/bin/env python3
"""
add-competitive-house-2026-pass4-batch4.py — Pass 4 batch 4 (final House).

Tier A round-out: LA-06, OH-13, WI-01, TN-09, IA-02, KS-03, MI-10 (open),
NY-18, PA-01, PA-04, NY-19, GA-12. ~14 records.
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
    'populist_right': {
        'sanctity_of_life':[T,T,T,T,T],'biblical_marriage':[T,T,T,T,T],
        'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,T],
        'economic_stewardship':[T,T,T,T,T],'election_integrity':[T,T,T,T,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
        'foreign_policy_restraint':[T,T,T,T,T],'industry_capture':[T,T,T,T,T],
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
    # ══ LA-06 (D incumbent Cleo Fields · R primary 11/3) ══
    rec('Garret Graves', 'garret-graves-2026', 'LA', 6,
        'U.S. Representative LA-06 (2026 R Candidate · former rep · gerrymandered out 2024)',
        'R', 'establishment_r', '2026-11-03',
        notes=('Former U.S. Representative LA-06 (2015-2025). Lost seat in 2024 redistricting '
               'when LA was forced to draw a second majority-Black district. Considering 2026 '
               'comeback bid.'),
        sources=['https://ballotpedia.org/Garret_Graves']),

    # ══ OH-13 (D incumbent Emilia Sykes · R primary 5/5 DONE) ══
    rec('Kevin Coughlin', 'kevin-coughlin', 'OH', 13,
        'U.S. Representative OH-13 (2026 R Candidate · 2024 nominee · former OH state senator)',
        'R', 'establishment_r', '2026-05-05',
        notes=('Former Ohio state senator. 2024 R nominee against Emilia Sykes (lost narrowly). '
               'Running again 2026 in Akron-area swing seat.'),
        sources=['https://ballotpedia.org/Kevin_Coughlin']),

    # ══ WI-01 (R incumbent Bryan Steil · D primary 8/11) ══
    rec('Peter Barca', 'peter-barca', 'WI', 1,
        'U.S. Representative WI-01 (2026 D Candidate · former U.S. Rep WI-01 · WI Dept of Revenue secretary)',
        'D', 'establishment_d', '2026-08-11',
        notes=('Former U.S. Representative WI-01 (1993-1995, before Paul Ryan). Secretary of '
               'WI Department of Revenue under Gov Evers. D candidate for WI-01 2026.'),
        sources=['https://ballotpedia.org/Peter_Barca']),

    # ══ TN-09 (D incumbent Steve Cohen · R primary 8/4) ══
    rec('Charlotte Bergmann', 'charlotte-bergmann', 'TN', 9,
        'U.S. Representative TN-09 (2026 R Candidate · perennial nominee in deep-blue Memphis seat)',
        'R', 'maga_conservative_r', '2026-08-04',
        notes=('Memphis-area conservative. Perennial R nominee against Steve Cohen in TN-09 '
               '(2010, 2012, 2018, 2020, 2022, 2024 — lost all). Likely 2026 candidate.'),
        sources=['https://ballotpedia.org/Charlotte_Bergmann']),

    # ══ IA-02 (R incumbent Ashley Hinson · D primary 6/2) ══
    rec('Sarah Corkery', 'sarah-corkery', 'IA', 2,
        'U.S. Representative IA-02 (2026 D Candidate · 2024 nominee · advocate)',
        'D', 'establishment_d', '2026-06-02',
        notes='Cedar Rapids-area D candidate. 2024 D nominee for IA-02 (lost to Hinson). 2026 candidate.',
        sources=['https://ballotpedia.org/Sarah_Corkery']),

    # ══ KS-03 (D incumbent Sharice Davids · R primary 8/4) ══
    rec('Prasanth Reddy', 'prasanth-reddy', 'KS', 3,
        'U.S. Representative KS-03 (2026 R Candidate · oncologist · 2024 R primary)',
        'R', 'establishment_r', '2026-08-04',
        notes=('Overland Park oncologist. 2024 R primary candidate KS-03. R candidate 2026 vs '
               'Sharice Davids in Johnson County swing district.'),
        sources=['https://ballotpedia.org/Prasanth_Reddy']),

    # ══ MI-10 (R incumbent John James RUNNING FOR GOV · open · D primary 8/4) ══
    rec('Carl Marlinga', 'carl-marlinga-2026', 'MI', 10,
        'U.S. Representative MI-10 (2026 D Candidate · 2022 + 2024 nominee · former Macomb Co prosecutor)',
        'D', 'establishment_d', '2026-08-04',
        notes=('Former Macomb County (MI) prosecutor + judge. 2022 + 2024 D nominee for MI-10 '
               '(lost narrowly both times). Running 2026 in newly-open Macomb seat (James '
               'running for MI Governor).'),
        sources=['https://ballotpedia.org/Carl_Marlinga']),

    # ══ NY-18 (D incumbent Pat Ryan · R primary 6/23) ══
    rec('Alison Esposito', 'alison-esposito-ny-18', 'NY', 18,
        'U.S. Representative NY-18 (2026 R Candidate · 2022 R Lt Gov nominee · former NYPD captain)',
        'R', 'establishment_r', '2026-06-23',
        notes=('Former NYPD captain. 2022 R Lt Governor nominee (with Zeldin, lost). Considering '
               'NY-18 House run 2026 vs Pat Ryan in Hudson Valley swing district.'),
        sources=['https://ballotpedia.org/Alison_Esposito']),

    # ══ PA-01 (R incumbent Brian Fitzpatrick · D primary 5/19 DONE) ══
    rec('Ashley Ehasz', 'ashley-ehasz', 'PA', 1,
        'U.S. Representative PA-01 (2026 D Candidate · 2022 + 2024 nominee · West Point grad)',
        'D', 'establishment_d', '2026-05-19',
        notes=('West Point graduate, Army helicopter pilot veteran. 2022 + 2024 D nominee against '
               'Brian Fitzpatrick (lost both). Running again 2026 in PA-01 swing district (Bucks County).'),
        sources=['https://ballotpedia.org/Ashley_Ehasz']),

    # ══ NJ-03 (D incumbent Herb Conaway · R primary 6/9) ══
    rec('Rajesh Mohan', 'rajesh-mohan-nj-03', 'NJ', 3,
        'U.S. Representative NJ-03 (2026 R Candidate · physician · first-time candidate)',
        'R', 'establishment_r', '2026-06-09',
        notes='Physician. R candidate for NJ-03 (Conaway) 2026.',
        sources=['https://ballotpedia.org/Rajesh_Mohan']),

    # ══ NY-19 (R incumbent Josh Riley · R primary 6/23) ══
    rec('Mike Roth', 'mike-roth-ny-19', 'NY', 19,
        'U.S. Representative NY-19 (2026 R Candidate · former county DA · Hudson Valley conservative)',
        'R', 'establishment_r', '2026-06-23',
        notes='Hudson Valley-area conservative attorney. R candidate for NY-19 2026.',
        sources=['https://ballotpedia.org/Mike_Roth']),

    # ══ MN-08 (R incumbent Pete Stauber · D primary 8/11) ══
    rec('Jen Schultz', 'jen-schultz', 'MN', 8,
        'U.S. Representative MN-08 (2026 D Candidate · 2022 nominee · former MN state rep · economist)',
        'D', 'establishment_d', '2026-08-11',
        notes=('Former Minnesota state representative (Duluth area). Economist. 2022 D nominee '
               'for MN-08 (lost to Stauber). D candidate 2026.'),
        sources=['https://ballotpedia.org/Jen_Schultz']),

    # ══ CA-45 (R incumbent Michelle Steel · top-2 6/2) ══
    rec('Derek Tran', 'derek-tran', 'CA', 45,
        'U.S. Representative CA-45 (D incumbent · 2024 winner · attorney · Vietnamese American)',
        'D', 'establishment_d', '2026-06-02',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent U.S. Representative CA-45 (sworn 2025). Attorney. First Vietnamese '
               'American Democrat in Congress. Defeated Michelle Steel in 2024. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Derek_Tran']),

    # ══ NV-04 (D incumbent Steven Horsford · R primary 6/9) ══
    rec('John Lee', 'john-lee-nv-04', 'NV', 4,
        'U.S. Representative NV-04 (2026 R Candidate · former mayor of North Las Vegas)',
        'R', 'establishment_r', '2026-06-09',
        notes=('Former mayor of North Las Vegas (2013-2022). Former Democrat, switched to GOP. '
               'R candidate for NV-04 (Horsford) 2026.'),
        sources=['https://ballotpedia.org/John_Lee']),
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
        dist_str = f'{r["district"]:02d}' if r['district'] else 'AL'
        print(f'  {action} {r["name"]:<28s} ({r["state"]}-{dist_str} {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
