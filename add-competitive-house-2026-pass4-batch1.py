#!/usr/bin/env python3
"""
add-competitive-house-2026-pass4-batch1.py — Pass 4 expansion.

Long-tail competitive-district challengers: 2024 nominees running again
and known declared 2026 candidates in swing districts.
~12 records.
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
    # ══ WA-03 (D incumbent Marie Gluesenkamp Perez · R primary 8/4) ══
    rec('Joe Kent', 'joe-kent', 'WA', 3,
        'U.S. Representative WA-03 (2026 R Candidate · 2022/2024 nominee · Army Special Forces vet)',
        'R', 'maga_conservative_r', '2026-08-04',
        notes=('Former Army Special Forces. 2022 + 2024 R nominee against Marie Gluesenkamp Perez '
               '(narrow losses both cycles). Running again 2026. Trump-endorsed in past cycles.'),
        sources=['https://ballotpedia.org/Joe_Kent']),
    rec('Leslie Lewallen', 'leslie-lewallen', 'WA', 3,
        'U.S. Representative WA-03 (2026 R Candidate · Camas city council · 2024 R primary candidate)',
        'R', 'establishment_r', '2026-08-04',
        notes='Camas City Council member. 2024 R primary candidate vs Kent (lost). 2026 R primary candidate.',
        sources=['https://ballotpedia.org/Leslie_Lewallen']),

    # ══ NM-02 (D incumbent Gabe Vasquez · R primary 6/2) ══
    rec('Yvette Herrell', 'yvette-herrell', 'NM', 2,
        'U.S. Representative NM-02 (2026 R Candidate · former rep · 2020 winner / 2022 + 2024 nominee)',
        'R', 'maga_conservative_r', '2026-06-02',
        notes=('Former U.S. Representative NM-02 (2021-2023). 2024 R nominee against Vasquez '
               '(lost narrowly). NM-02 is a top R-target district that swings each cycle.'),
        sources=['https://ballotpedia.org/Yvette_Herrell']),

    # ══ NC-01 (D incumbent Don Davis · R primary 3/3 DONE) ══
    rec('Laurie Buckhout', 'laurie-buckhout', 'NC', 1,
        'U.S. Representative NC-01 (2026 R Candidate · 2024 nominee · retired Army colonel)',
        'R', 'maga_conservative_r', '2026-03-03',
        notes=('Retired U.S. Army colonel (electronic warfare). 2024 R nominee against Don Davis '
               '(lost narrowly). Running again 2026.'),
        sources=['https://ballotpedia.org/Laurie_Buckhout']),

    # ══ IL-17 (D incumbent Eric Sorensen · R primary 3/17 DONE) ══
    rec('Joe McGraw', 'joe-mcgraw', 'IL', 17,
        'U.S. Representative IL-17 (2026 R Candidate · 2024 nominee · retired Winnebago Co judge)',
        'R', 'establishment_r', '2026-03-17',
        notes=('Retired Winnebago County judge. 2024 R nominee against Sorensen (lost narrowly). '
               'Running again 2026.'),
        sources=['https://ballotpedia.org/Joe_McGraw']),

    # ══ MN-02 (D incumbent Angie Craig · MN primary 8/11) ══
    rec('Tyler Kistner', 'tyler-kistner', 'MN', 2,
        'U.S. Representative MN-02 (2026 R Candidate · Marine vet · 2020 + 2022 nominee)',
        'R', 'maga_conservative_r', '2026-08-11',
        notes=('Marine Corps veteran. 2020 and 2022 R nominee against Angie Craig (lost both, '
               'narrowly in 2020). Angie Craig now running for U.S. Senate (open 2026), making '
               'MN-02 an open R-target seat.'),
        sources=['https://ballotpedia.org/Tyler_Kistner']),

    # ══ IA-03 (R incumbent Zach Nunn · D primary 6/2) ══
    rec('Lanon Baccam', 'lanon-baccam', 'IA', 3,
        'U.S. Representative IA-03 (2026 D Candidate · 2024 nominee · USDA + Army National Guard vet)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Iowa Army National Guard vet, former USDA staff under Vilsack. 2024 D nominee '
               'against Zach Nunn (lost narrowly). Running again 2026 in top D-target seat.'),
        sources=['https://ballotpedia.org/Lanon_Baccam']),

    # ══ WI-03 (R incumbent Derrick Van Orden · D primary 8/11) ══
    rec('Rebecca Cooke', 'rebecca-cooke', 'WI', 3,
        'U.S. Representative WI-03 (2026 D Candidate · 2024 nominee · Eau Claire businesswoman)',
        'D', 'establishment_d', '2026-08-11',
        notes=('Eau Claire businesswoman, restaurant owner. 2024 D nominee against Van Orden '
               '(lost narrowly). Running again 2026.'),
        sources=['https://ballotpedia.org/Rebecca_Cooke']),

    # ══ MI-07 (R incumbent Tom Barrett · D primary 8/4) ══
    rec('Curtis Hertel', 'curtis-hertel', 'MI', 7,
        'U.S. Representative MI-07 (2026 D Candidate · 2024 nominee · former MI state senator)',
        'D', 'establishment_d', '2026-08-04',
        notes=('Former Michigan state senator, former Whitmer chief of staff. 2024 D nominee '
               'against Tom Barrett (lost narrowly). Running again 2026.'),
        sources=['https://ballotpedia.org/Curtis_Hertel_Jr.']),

    # ══ NY-19 (R incumbent Josh Riley DEFEATED 2024 - now D incumbent · R primary 6/23) ══
    rec('Marc Molinaro', 'marc-molinaro', 'NY', 19,
        'U.S. Representative NY-19 (2026 R Candidate · former rep · 2022 winner / 2024 loser)',
        'R', 'establishment_r', '2026-06-23',
        notes=('Former U.S. Representative NY-19 (2023-2025). Lost to Josh Riley in 2024 rematch. '
               'May run again 2026.'),
        sources=['https://ballotpedia.org/Marc_Molinaro']),

    # ══ CA-22 (R incumbent David Valadao · D primary 6/2) ══
    rec('Rudy Salas', 'rudy-salas', 'CA', 22,
        'U.S. Representative CA-22 (2026 D Candidate · former CA assembly · 2022 + 2024 nominee)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Former CA State Assembly member. 2022 + 2024 D nominee against David Valadao '
               '(lost both, narrowly). Running 2026 in top D-target seat (CA-22 is a Biden+13 '
               'district that elects an R).'),
        sources=['https://ballotpedia.org/Rudy_Salas']),

    # ══ PA-07 (D incumbent Susan Wild DEFEATED 2024 → R Mackenzie · D primary 5/19 DONE) ══
    rec('Ryan Mackenzie', 'ryan-mackenzie', 'PA', 7,
        'U.S. Representative PA-07 (2026 R incumbent · won 2024 vs Wild · former PA House)',
        'R', 'establishment_r', '2026-05-19',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent U.S. Representative PA-07. Defeated Susan Wild in 2024. Former PA '
               'state representative. PA-07 is a perennial swing district (Lehigh Valley).'),
        sources=['https://ballotpedia.org/Ryan_Mackenzie']),
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
