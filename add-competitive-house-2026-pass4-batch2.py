#!/usr/bin/env python3
"""
add-competitive-house-2026-pass4-batch2.py — Pass 4 batch 2.

More long-tail competitive challengers across FL, CA, NY, IL, TX, AK.
~14 records.
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
    # ══ FL-13 (R incumbent Anna Paulina Luna · D primary 8/18) ══
    rec('Whitney Fox', 'whitney-fox', 'FL', 13,
        'U.S. Representative FL-13 (2026 D Candidate · 2024 nominee · communications professional)',
        'D', 'establishment_d', '2026-08-18',
        notes=('Communications professional, former PR for Pinellas County. 2024 D nominee '
               'against Anna Paulina Luna (lost). Running again 2026.'),
        sources=['https://ballotpedia.org/Whitney_Fox']),

    # ══ FL-27 (R incumbent Maria Elvira Salazar · D primary 8/18) ══
    rec('Lucia Baez-Geller', 'lucia-baez-geller', 'FL', 27,
        'U.S. Representative FL-27 (2026 D Candidate · Miami-Dade school board · educator)',
        'D', 'establishment_d', '2026-08-18',
        notes=('Miami-Dade County School Board member. Educator and Cuban-American community '
               'leader. D candidate for FL-27 (Salazar) 2026.'),
        sources=['https://ballotpedia.org/Lucia_Baez-Geller']),

    # ══ CA-13 (D incumbent Adam Gray · top-2 6/2) ══
    rec('John Duarte', 'john-duarte', 'CA', 13,
        'U.S. Representative CA-13 (2026 R Candidate · former rep · 2022 winner / 2024 loser)',
        'R', 'establishment_r', '2026-06-02',
        notes=('Former U.S. Representative CA-13 (2023-2025). Lost narrowly to Adam Gray in '
               '2024. Pistachio/walnut farmer. Running again 2026 in CA-13 rematch.'),
        sources=['https://ballotpedia.org/John_Duarte']),

    # ══ CA-27 (D incumbent George Whitesides · top-2 6/2) ══
    rec('Mike Garcia', 'mike-garcia', 'CA', 27,
        'U.S. Representative CA-27 (2026 R Candidate · former rep · Navy fighter pilot)',
        'R', 'establishment_r', '2026-06-02',
        notes=('Former U.S. Representative CA-27 (2020-2025, won 2020 special). Lost to '
               'George Whitesides in 2024. Navy F/A-18 fighter pilot veteran. Running again 2026.'),
        sources=['https://ballotpedia.org/Mike_Garcia_(California_politician)']),

    # ══ TX-15 (R incumbent Monica De La Cruz · D primary 3/3 DONE) ══
    rec('Michelle Vallejo', 'michelle-vallejo', 'TX', 15,
        'U.S. Representative TX-15 (2026 D Candidate · 2022 + 2024 nominee · businesswoman)',
        'D', 'establishment_d', '2026-03-03',
        notes=('Pharr, TX businesswoman. 2022 + 2024 D nominee against Monica De La Cruz '
               '(lost both). Running 2026 in Rio Grande Valley swing district.'),
        sources=['https://ballotpedia.org/Michelle_Vallejo']),

    # ══ AK-AL (R incumbent Nick Begich · open primary 8/18) ══
    rec('Mary Peltola', 'mary-peltola', 'AK', None,
        'U.S. Representative AK-AL (2026 D Candidate · former rep · won 2022 special / lost 2024)',
        'D', 'establishment_d', '2026-08-18',
        notes=('Former U.S. Representative AK-AL (2022-2025, first Alaska Native rep). Won '
               '2022 special after Don Young death. Lost narrowly to Nick Begich in 2024. '
               'Considering 2026 rematch under RCV system.'),
        sources=['https://ballotpedia.org/Mary_Peltola']),

    # ══ IL-13 (D incumbent Nikki Budzinski · R primary 3/17 DONE) ══
    rec('Joshua Loyd', 'joshua-loyd', 'IL', 13,
        'U.S. Representative IL-13 (2026 R Candidate · 2024 nominee · businessman)',
        'R', 'establishment_r', '2026-03-17',
        notes='Springfield-area businessman. 2024 R nominee against Nikki Budzinski (lost). '
              '2026 R primary candidate.',
        sources=['https://ballotpedia.org/Joshua_Loyd']),

    # ══ MI-03 (D incumbent Hillary Scholten · R primary 8/4) ══
    rec('Paul Hudson', 'paul-hudson', 'MI', 3,
        'U.S. Representative MI-03 (2026 R Candidate · 2024 R primary · attorney)',
        'R', 'establishment_r', '2026-08-04',
        notes='Grand Rapids attorney. 2024 R primary candidate in MI-03. R candidate 2026 vs Scholten.',
        sources=['https://ballotpedia.org/Paul_Hudson']),

    # ══ PA-08 (R incumbent Rob Bresnahan · D primary 5/19 DONE — Cognetti already in DB) ══
    # (no record this batch — Cognetti added in earlier batch7)

    # ══ NJ-07 (R incumbent Tom Kean Jr. · D primary 6/9) ══
    rec('Rebecca Bennett', 'rebecca-bennett-nj-07', 'NJ', 7,
        'U.S. Representative NJ-07 (2026 D Candidate · attorney · first-time candidate)',
        'D', 'establishment_d', '2026-06-09',
        notes='New Jersey attorney. D primary candidate for NJ-07 (Kean Jr.) 2026.',
        sources=['https://ballotpedia.org/Rebecca_Bennett']),

    # ══ NY-17 (R incumbent Mike Lawler · D primary 6/23 — open per Lawler running for Gov?) ══
    rec('Mondaire Jones', 'mondaire-jones', 'NY', 17,
        'U.S. Representative NY-17 (2026 D Candidate · former rep · 2024 nominee)',
        'D', 'progressive_d', '2026-06-23',
        notes=('Former U.S. Representative NY-17 (2021-2023). 2024 D nominee against Mike Lawler '
               '(lost narrowly). Running again 2026.'),
        sources=['https://ballotpedia.org/Mondaire_Jones']),

    # ══ NY-22 (D incumbent John Mannion · R primary 6/23) ══
    rec('Brandon Williams', 'brandon-williams', 'NY', 22,
        'U.S. Representative NY-22 (2026 R Candidate · former rep · 2024 loser to Mannion)',
        'R', 'establishment_r', '2026-06-23',
        notes=('Former U.S. Representative NY-22 (2023-2025). Lost to John Mannion in 2024. '
               'Navy veteran. Considering 2026 rematch.'),
        sources=['https://ballotpedia.org/Brandon_Williams_(New_York)']),

    # ══ TX-28 (D incumbent Henry Cuellar · D primary 3/3 DONE) ══
    rec('Jessica Cisneros', 'jessica-cisneros', 'TX', 28,
        'U.S. Representative TX-28 (2026 D Primary Challenger · 2020 + 2022 + 2024 challenger to Cuellar)',
        'D', 'progressive_d', '2026-03-03',
        notes=('Immigration attorney. 2020 + 2022 + 2024 D primary challenger to Henry Cuellar '
               '(lost all three, narrowly in 2022). Progressive. May run again 2026.'),
        sources=['https://ballotpedia.org/Jessica_Cisneros']),

    # ══ PA-17 (D incumbent Chris Deluzio · R primary 5/19 DONE) ══
    rec('Rob Mercuri', 'rob-mercuri', 'PA', 17,
        'U.S. Representative PA-17 (2026 R Candidate · former PA state rep · West Point grad)',
        'R', 'establishment_r', '2026-05-19',
        notes=('Former Pennsylvania state representative (until 2024). West Point graduate, '
               'Army veteran. 2024 R nominee against Chris Deluzio (lost). May run again 2026.'),
        sources=['https://ballotpedia.org/Rob_Mercuri']),

    # ══ AZ-06 (R incumbent Juan Ciscomani · D primary 8/4) ══
    rec('Kirsten Engel', 'kirsten-engel', 'AZ', 6,
        'U.S. Representative AZ-06 (2026 D Candidate · former AZ state senator · 2022 + 2024 nominee)',
        'D', 'establishment_d', '2026-08-04',
        notes=('Former Arizona state senator. 2022 + 2024 D nominee against Juan Ciscomani '
               '(lost both, narrowly). Running 2026 in AZ-06 swing district.'),
        sources=['https://ballotpedia.org/Kirsten_Engel']),
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
