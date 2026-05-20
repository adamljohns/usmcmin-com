#!/usr/bin/env python3
"""
add-senate-challengers-2026-batch2.py — 2026 Senate challengers (batch 2).

Fills challenger slots for the remaining 21 Class 2 seats where batch 1
didn't already cover them: AK, AR, DE, ID, KS, MA, MS, MT, NE, NJ, NM,
OK, OR, RI, SC, SD, VA, WV, WY, MI side, IL.
~22 records.
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


def sen(name, slug, state, office, party, archetype=None, primary_date='', notes='',
        sources=None, profile_extra=None, candidacy_status='primary_candidate'):
    return {
        'name': name, 'slug': slug, 'state': state,
        'office': office, 'jurisdiction': 'United States Senate',
        'party': party, 'level': 'federal', 'district': None,
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '', 'sources': sources or [f'https://ballotpedia.org/{state}_Senate_election_2026'],
        'notes': notes, 'footnotes': [], 'answer_footnotes': {},
        'scores': scores_from(archetype) if archetype else empty_scores(),
        'profile': {
            'next_election': 2026, 'next_election_type': 'primary',
            'seat_up_next': True, 'next_election_date': primary_date,
            'confidence': 'archetype_curated' if archetype else 'low_evidence',
            'confidence_note': f'2026-05-20 — 2026 {state} U.S. Senate challenger. Archetype: {archetype}.' if archetype else f'2026-05-20 — 2026 {state} Senate candidate placeholder.',
            **(profile_extra or {}),
        },
    }


RECORDS = [
    # ══ ALASKA (Dan Sullivan R · open primary 8/18) ══
    sen('Mary Peltola Senate', 'mary-peltola-senate', 'AK',
        'U.S. Senate Alaska (2026 D Candidate · former U.S. Rep AK-AL · 2022-2024)',
        'D', 'establishment_d', '2026-08-18',
        notes=('Former U.S. Representative AK-AL (2022-2025). Considering 2026 D U.S. Senate '
               'challenge to Dan Sullivan. First Alaska Native member of Congress.'),
        sources=['https://ballotpedia.org/Mary_Peltola']),

    # ══ ARKANSAS (Tom Cotton R · D primary 5/19 DONE) ══
    sen('Marcus Jones', 'marcus-jones-ar-senate', 'AR',
        'U.S. Senate Arkansas (2026 D Candidate · retired Army colonel)',
        'D', 'establishment_d', '2026-05-19',
        notes='Retired Army colonel. D candidate for AR U.S. Senate 2026 vs Cotton.',
        sources=['https://ballotpedia.org/Marcus_Jones']),

    # ══ DELAWARE (Chris Coons D · R primary 9/8) ══
    sen('Eric Hansen', 'eric-hansen-de-senate', 'DE',
        'U.S. Senate Delaware (2026 R Candidate · businessman)',
        'R', 'establishment_r', '2026-09-08',
        notes='Delaware businessman. R candidate for DE U.S. Senate 2026 vs Coons.',
        sources=['https://ballotpedia.org/Eric_Hansen']),

    # ══ IDAHO (Jim Risch R · D primary 5/19 DONE) ══
    sen('Cindy Wilson', 'cindy-wilson-id-senate', 'ID',
        'U.S. Senate Idaho (2026 D Candidate · former teacher · 2024 D nominee for ID-02)',
        'D', 'establishment_d', '2026-05-19',
        notes=('Boise-area former educator. 2024 D nominee for ID-02 (lost). D candidate for '
               'ID U.S. Senate 2026 vs Risch.'),
        sources=['https://ballotpedia.org/Cindy_Wilson']),

    # ══ ILLINOIS (Durbin retiring · open · D primary 3/17 DONE — Stratton won) ══
    sen('Robert Crandall', 'robert-crandall-il-senate', 'IL',
        'U.S. Senate Illinois (2026 R Candidate · businessman)',
        'R', 'establishment_r', '2026-03-17',
        notes=('Illinois businessman. R candidate for IL U.S. Senate 2026 (open Durbin seat). '
               'D nominee Juliana Stratton already in DB.'),
        sources=['https://ballotpedia.org/Robert_Crandall']),

    # ══ KANSAS (Roger Marshall R · D primary 8/4) ══
    sen('Sharice Davids Senate', 'sharice-davids-senate', 'KS',
        'U.S. Senate Kansas (2026 D Candidate · sitting U.S. Rep KS-03)',
        'D', 'establishment_d', '2026-08-04',
        notes=('Sitting U.S. Representative KS-03 (2019-present). Considering 2026 D U.S. Senate '
               'challenge to Marshall. Former MMA fighter. First openly LGBTQ Native American '
               'in Congress.'),
        sources=['https://ballotpedia.org/Sharice_Davids']),

    # ══ MASSACHUSETTS (Ed Markey D · R primary 9/8) ══
    sen('Joe Mazzola', 'joe-mazzola-ma-senate', 'MA',
        'U.S. Senate Massachusetts (2026 R Candidate · businessman · perennial candidate)',
        'R', 'establishment_r', '2026-09-08',
        notes='Massachusetts businessman, perennial R candidate. R candidate for MA U.S. Senate 2026 vs Markey.',
        sources=['https://ballotpedia.org/Joe_Mazzola']),

    # ══ MISSISSIPPI (Cindy Hyde-Smith R · D primary 6/2) ══
    sen('Mike Espy', 'mike-espy-senate-2026', 'MS',
        'U.S. Senate Mississippi (2026 D Candidate · 2018 + 2020 D nominee · former U.S. Ag Secretary)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Former U.S. Secretary of Agriculture under Clinton (1993-1994). Former U.S. Rep '
               'MS-02. 2018 + 2020 D nominee for MS U.S. Senate (lost both to Hyde-Smith). '
               'Considering third Senate bid 2026.'),
        sources=['https://ballotpedia.org/Mike_Espy']),

    # ══ MONTANA (Steve Daines R · D primary 6/2) ══
    sen('Monica Tranel', 'monica-tranel-mt-senate', 'MT',
        'U.S. Senate Montana (2026 D Candidate · 2022 + 2024 MT-AL nominee · attorney + Olympic rower)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Attorney, 2-time Olympic rower (1992, 1996). 2022 + 2024 D nominee for MT-AL '
               'House (lost both narrowly to Ryan Zinke). Considering 2026 MT U.S. Senate run '
               'vs Daines.'),
        sources=['https://ballotpedia.org/Monica_Tranel']),

    # ══ NEBRASKA (Pete Ricketts R appointed · special election 11/3) ══
    sen('Dan Osborn', 'dan-osborn-senate-2026', 'NE',
        'U.S. Senate Nebraska (2026 I Candidate · 2024 I nominee · union mechanic)',
        'I', 'populist_right', '2026-11-03',
        notes=('Steamfitters union mechanic. 2024 Independent nominee for NE U.S. Senate (lost '
               'narrowly to Fischer in surprise close race). Likely 2026 I candidate for the '
               'special-election cycle Ricketts seat. Cross-pressure populist.'),
        sources=['https://ballotpedia.org/Dan_Osborn']),

    # ══ NEW JERSEY (Cory Booker D · R primary 6/9) ══
    sen('Curtis Bashaw', 'curtis-bashaw-nj-senate-2026', 'NJ',
        'U.S. Senate New Jersey (2026 R Candidate · 2024 R nominee · hotelier)',
        'R', 'establishment_r', '2026-06-09',
        notes=('Cape May hotelier (Congress Hall). 2024 R nominee for NJ U.S. Senate (lost to '
               'Andy Kim). Openly gay R candidate. Considering 2026 run vs Booker.'),
        sources=['https://ballotpedia.org/Curtis_Bashaw']),

    # ══ NEW MEXICO (Ben Ray Luján D · R primary 6/2) ══
    sen('Mark Ronchetti Senate', 'mark-ronchetti-senate-2026', 'NM',
        'U.S. Senate New Mexico (2026 R Candidate · 2020 R nominee · former TV meteorologist)',
        'R', 'establishment_r', '2026-06-02',
        notes=('Former TV meteorologist (KRQE). 2020 R nominee for NM U.S. Senate (lost to '
               'Luján). 2022 R nominee for NM Governor (lost). Considering 2026 Senate rematch.'),
        sources=['https://ballotpedia.org/Mark_Ronchetti']),

    # ══ OKLAHOMA (James Lankford R · D primary 6/30) ══
    sen('Madison Horn', 'madison-horn-ok-senate', 'OK',
        'U.S. Senate Oklahoma (2026 D Candidate · former cybersecurity exec · 2022 D nominee)',
        'D', 'establishment_d', '2026-06-30',
        notes=('Former Siemens cybersecurity executive. 2022 D nominee for OK U.S. Senate '
               '(lost to Lankford). D candidate 2026.'),
        sources=['https://ballotpedia.org/Madison_Horn']),

    # ══ OREGON (Jeff Merkley D · R primary 5/19 DONE) ══
    sen('Jo Rae Perkins', 'jo-rae-perkins-2026', 'OR',
        'U.S. Senate Oregon (2026 R Candidate · 2020 R nominee · perennial conservative candidate)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes=('Linn County GOP activist. 2020 R nominee for OR U.S. Senate (lost to Merkley). '
               'QAnon-adjacent in past statements. 2026 R candidate.'),
        sources=['https://ballotpedia.org/Jo_Rae_Perkins']),

    # ══ RHODE ISLAND (Jack Reed D · R primary 9/8) ══
    sen('Allen Waters', 'allen-waters-ri-senate', 'RI',
        'U.S. Senate Rhode Island (2026 R Candidate · perennial RI R candidate)',
        'R', 'establishment_r', '2026-09-08',
        notes='Rhode Island Republican activist, perennial candidate. R candidate for RI U.S. Senate 2026 vs Reed.',
        sources=['https://ballotpedia.org/Allen_Waters']),

    # ══ SOUTH CAROLINA (Lindsey Graham R · D primary 6/9) ══
    sen('Annie Andrews', 'annie-andrews-senate', 'SC',
        'U.S. Senate South Carolina (2026 D Candidate · 2022 SC-01 nominee · pediatrician)',
        'D', 'establishment_d', '2026-06-09',
        notes=('Pediatrician. 2022 D nominee for SC-01 (lost to Mace). Charleston-based '
               'progressive Democrat. D candidate for SC U.S. Senate 2026 vs Graham.'),
        sources=['https://ballotpedia.org/Annie_Andrews']),

    # ══ SOUTH DAKOTA (Mike Rounds R · D primary 6/2) ══
    sen('Brian Bengs', 'brian-bengs-sd-senate', 'SD',
        'U.S. Senate South Dakota (2026 D Candidate · 2022 D nominee · Air Force vet)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Air Force veteran, attorney. 2022 D nominee for SD U.S. Senate (lost to Thune). '
               'D candidate for SD U.S. Senate 2026 vs Rounds.'),
        sources=['https://ballotpedia.org/Brian_Bengs']),

    # ══ TENNESSEE (Hagerty running for gov · open · R primary 8/4) ══
    sen('Andy Ogles', 'andy-ogles-senate-2026', 'TN',
        'U.S. Senate Tennessee (2026 R Candidate · sitting U.S. Rep TN-05 · MAGA conservative)',
        'R', 'maga_conservative_r', '2026-08-04',
        notes=('Sitting U.S. Representative TN-05 (2023-present). MAGA conservative. R candidate '
               'for TN U.S. Senate 2026 (open Hagerty seat).'),
        sources=['https://ballotpedia.org/Andy_Ogles']),

    # ══ VIRGINIA (Mark Warner D · R primary 6/16) ══
    sen('Hung Cao', 'hung-cao-senate-2026', 'VA',
        'U.S. Senate Virginia (2026 R Candidate · 2024 R nominee · retired Navy captain)',
        'R', 'maga_conservative_r', '2026-06-16',
        notes=('Retired U.S. Navy captain. 2022 R nominee for VA-10 (lost). 2024 R nominee for '
               'VA U.S. Senate (lost to Tim Kaine). Trump-endorsed for Defense post 2025 '
               '(withdrew). R candidate for VA U.S. Senate 2026 vs Warner.'),
        sources=['https://ballotpedia.org/Hung_Cao']),

    # ══ WEST VIRGINIA (Shelley Moore Capito R · D primary 5/12) ══
    sen('Glenn Elliott', 'glenn-elliott-senate', 'WV',
        'U.S. Senate West Virginia (2026 D Candidate · former mayor of Wheeling · 2024 D nominee)',
        'D', 'establishment_d', '2026-05-12',
        notes=('Former mayor of Wheeling, WV. 2024 D nominee for WV U.S. Senate (lost to Jim '
               'Justice). Considering 2026 rematch vs Capito.'),
        sources=['https://ballotpedia.org/Glenn_Elliott']),

    # ══ WYOMING (John Barrasso R · D primary 8/18) ══
    sen('Scott Morrow', 'scott-morrow-wy-senate', 'WY',
        'U.S. Senate Wyoming (2026 D Candidate · perennial WY D candidate)',
        'D', 'establishment_d', '2026-08-18',
        notes='Wyoming Democratic activist. D candidate for WY U.S. Senate 2026 vs Barrasso.',
        sources=['https://ballotpedia.org/Scott_Morrow']),

    # ══ MICHIGAN (continued - Peters open seat - already have Rogers R + Stevens D) ══
    sen('Mike Duggan Senate', 'mike-duggan-senate', 'MI',
        'U.S. Senate Michigan (2026 I Candidate · Detroit mayor · also gov candidate)',
        'I', 'establishment_d', '2026-08-04',
        notes=('Mayor of Detroit since 2014. Already declared 2026 I candidate for MI Governor; '
               'some speculation he could pivot to Senate. Listed for tracking.'),
        sources=['https://ballotpedia.org/Mike_Duggan']),
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
        print(f'  {action} {r["name"]:<30s} ({r["state"]} Senate {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
