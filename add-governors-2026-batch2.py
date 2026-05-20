#!/usr/bin/env python3
"""
add-governors-2026-batch2.py — 2026 gubernatorial expansion (batch 2).

Targets TX, OH, TN, IA, SD, NV, CO, KS, OK — incumbent-vs-challenger
or open-seat races. ~18 records.
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

JURISDICTION = {
    'AL':'State of Alabama','SC':'State of South Carolina','FL':'State of Florida',
    'AZ':'State of Arizona','GA':'State of Georgia','TX':'State of Texas',
    'MI':'State of Michigan','OH':'State of Ohio','TN':'State of Tennessee',
    'MN':'State of Minnesota','VA':'Commonwealth of Virginia','PA':'Commonwealth of Pennsylvania',
    'MA':'Commonwealth of Massachusetts','KY':'Commonwealth of Kentucky',
    'WI':'State of Wisconsin','NV':'State of Nevada','CO':'State of Colorado',
    'KS':'State of Kansas','OK':'State of Oklahoma','SD':'State of South Dakota',
    'IA':'State of Iowa','NM':'State of New Mexico','NH':'State of New Hampshire',
    'VT':'State of Vermont','MD':'State of Maryland','ME':'State of Maine',
    'CT':'State of Connecticut','RI':'State of Rhode Island','HI':'State of Hawaii',
    'AK':'State of Alaska','NY':'State of New York','NJ':'State of New Jersey',
    'IL':'State of Illinois','MO':'State of Missouri','WA':'State of Washington',
    'OR':'State of Oregon','UT':'State of Utah','ID':'State of Idaho',
    'NC':'State of North Carolina','LA':'State of Louisiana','MS':'State of Mississippi',
    'AR':'State of Arkansas','MT':'State of Montana','WY':'State of Wyoming',
    'ND':'State of North Dakota','NE':'State of Nebraska','DE':'State of Delaware',
    'WV':'State of West Virginia','IN':'State of Indiana','CA':'State of California',
}

def gov(name, slug, state, office, party, archetype=None, primary_date='', notes='',
        sources=None, profile_extra=None, candidacy_status='primary_candidate'):
    return {
        'name': name, 'slug': slug, 'state': state,
        'office': office, 'jurisdiction': JURISDICTION.get(state, f'State of {state}'),
        'party': party, 'level': 'state', 'district': None,
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '', 'sources': sources or [f'https://ballotpedia.org/Gubernatorial_election_in_{state}_2026'],
        'notes': notes, 'footnotes': [], 'answer_footnotes': {},
        'scores': scores_from(archetype) if archetype else empty_scores(),
        'profile': {
            'next_election': 2026, 'next_election_type': 'primary',
            'seat_up_next': True, 'next_election_date': primary_date,
            'confidence': 'archetype_curated' if archetype else 'low_evidence',
            'confidence_note': f'2026-05-20 — 2026 {state} Governor race. Archetype: {archetype}.' if archetype else f'2026-05-20 — 2026 {state} Governor candidate placeholder.',
            **(profile_extra or {}),
        },
    }

RECORDS = [
    # ════════════════════════════════════════════════════════════════
    # TEXAS Governor (Greg Abbott seeking 4th term · R primary 3/3 DONE)
    # ════════════════════════════════════════════════════════════════
    gov('Beto O\'Rourke', 'beto-orourke-gov-2026', 'TX',
        'Governor of Texas (2026 D Candidate · 2022 D nominee · former U.S. Rep TX-16)',
        'D', 'progressive_d', '2026-03-03',
        notes=('Former U.S. Representative TX-16 (2013-2019). 2022 D nominee for TX Governor '
               '(lost to Abbott). 2018 U.S. Senate candidate. 2020 D presidential candidate. '
               'Considering 2026 rematch with Abbott.'),
        sources=['https://ballotpedia.org/Beto_O\'Rourke']),
    gov('Colin Allred', 'colin-allred-gov-2026', 'TX',
        'Governor of Texas (2026 D Candidate · former U.S. Rep TX-32 · 2024 U.S. Senate nominee)',
        'D', 'establishment_d', '2026-03-03',
        notes=('Former U.S. Representative TX-32 (2019-2025). 2024 D nominee for U.S. Senate '
               '(lost to Ted Cruz). Civil rights attorney, former NFL linebacker. '
               'Considering 2026 D primary for Governor.'),
        sources=['https://ballotpedia.org/Colin_Allred']),

    # ════════════════════════════════════════════════════════════════
    # OHIO Governor (Mike DeWine term-limited · R primary 5/5 DONE)
    # ════════════════════════════════════════════════════════════════
    gov('Vivek Ramaswamy', 'vivek-ramaswamy-gov', 'OH',
        'Governor of Ohio (2026 R Candidate · biotech entrepreneur · 2024 R presidential candidate)',
        'R', 'maga_conservative_r', '2026-05-05',
        notes=('Biotech entrepreneur, Roivant Sciences founder. 2024 R presidential primary '
               'candidate (dropped out, endorsed Trump). Trump-endorsed for 2026 OH Governor. '
               'Frontrunner R primary.'),
        sources=['https://ballotpedia.org/Vivek_Ramaswamy']),
    gov('Heather Hill', 'heather-hill-gov', 'OH',
        'Governor of Ohio (2026 R Candidate · Morgan Co commissioner · rural advocate)',
        'R', 'establishment_r', '2026-05-05',
        notes='Morgan County (OH) Commissioner. R primary candidate for OH Governor 2026.',
        sources=['https://ballotpedia.org/Heather_Hill']),
    gov('Amy Acton', 'amy-acton-gov', 'OH',
        'Governor of Ohio (2026 D Candidate · former OH Dept of Health director · COVID lead)',
        'D', 'establishment_d', '2026-05-05',
        notes=('Former Ohio Department of Health director under Gov DeWine (resigned 2020). '
               'Led OH COVID-19 response 2020. First-time D candidate for OH Governor 2026.'),
        sources=['https://ballotpedia.org/Amy_Acton']),

    # ════════════════════════════════════════════════════════════════
    # TENNESSEE Governor (Bill Lee term-limited · R primary 8/4)
    # ════════════════════════════════════════════════════════════════
    gov('Bill Hagerty', 'bill-hagerty-gov', 'TN',
        'Governor of Tennessee (2026 R Candidate · sitting U.S. Senator · former Trump ambassador)',
        'R', 'establishment_r', '2026-08-04',
        notes=('Sitting U.S. Senator from TN (2021-present). Former U.S. Ambassador to Japan '
               'under Trump. Considering 2026 R primary for TN Governor; would also need to '
               'decide on Senate re-election (his seat next up 2026).'),
        sources=['https://ballotpedia.org/Bill_Hagerty']),
    gov('Marsha Blackburn', 'marsha-blackburn-gov', 'TN',
        'Governor of Tennessee (2026 R Candidate · sitting U.S. Senator · seat not up till 2030)',
        'R', 'establishment_r', '2026-08-04',
        notes=('Sitting U.S. Senator from TN (2019-present; re-elected 2024). Reportedly '
               'considering 2026 R primary for TN Governor. Senate seat not up until 2030 — '
               'gubernatorial run does NOT require giving up Senate seat.'),
        sources=['https://ballotpedia.org/Marsha_Blackburn']),
    gov('Carol Swain', 'carol-swain-gov', 'TN',
        'Governor of Tennessee (2026 R Candidate · former Vanderbilt prof · 2018 + 2023 Nashville mayor candidate)',
        'R', 'maga_conservative_r', '2026-08-04',
        notes=('Former Vanderbilt political science professor. 2018 + 2023 R candidate for '
               'Nashville mayor. R primary candidate for TN Governor 2026.'),
        sources=['https://ballotpedia.org/Carol_Swain']),
    gov('Gloria Johnson', 'gloria-johnson-gov-2026', 'TN',
        'Governor of Tennessee (2026 D Candidate · TN state rep · 2024 U.S. Senate nominee)',
        'D', 'progressive_d', '2026-08-04',
        notes=('Tennessee state representative (Knoxville). 2024 D nominee for U.S. Senate '
               '(lost to Blackburn). Tennessee Three member. D candidate for TN Governor 2026.'),
        sources=['https://ballotpedia.org/Gloria_Johnson']),

    # ════════════════════════════════════════════════════════════════
    # IOWA Governor (Kim Reynolds NOT seeking re-election · R primary 6/2)
    # ════════════════════════════════════════════════════════════════
    gov('Brad Zaun', 'brad-zaun-gov', 'IA',
        'Governor of Iowa (2026 R Candidate · IA state senator · former Urbandale mayor)',
        'R', 'establishment_r', '2026-06-02',
        notes='Iowa state senator (Urbandale). Former mayor of Urbandale. R primary candidate for IA Governor 2026.',
        sources=['https://ballotpedia.org/Brad_Zaun']),
    gov('Rob Sand', 'rob-sand-gov', 'IA',
        'Governor of Iowa (2026 D Candidate · sitting IA State Auditor · only D in IA statewide office)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Sitting Iowa State Auditor (since 2019). Only Democrat holding statewide office in '
               'Iowa. Announced D primary candidate for IA Governor 2026.'),
        sources=['https://ballotpedia.org/Rob_Sand']),

    # ════════════════════════════════════════════════════════════════
    # SOUTH DAKOTA Governor (Larry Rhoden incumbent — Noem to DHS · R primary 6/2)
    # ════════════════════════════════════════════════════════════════
    gov('Toby Doeden', 'toby-doeden-gov', 'SD',
        'Governor of South Dakota (2026 R Candidate · Aberdeen businessman · America First PAC)',
        'R', 'populist_right', '2026-06-02',
        notes=('Aberdeen businessman, founder of Dakota First Action PAC. R primary challenger '
               'to incumbent Gov Larry Rhoden 2026.'),
        sources=['https://ballotpedia.org/Toby_Doeden']),

    # ════════════════════════════════════════════════════════════════
    # NEVADA Governor (Joe Lombardo R incumbent · D primary 6/9)
    # ════════════════════════════════════════════════════════════════
    gov('Aaron Ford', 'aaron-ford-gov', 'NV',
        'Governor of Nevada (2026 D Candidate · sitting NV Attorney General)',
        'D', 'establishment_d', '2026-06-09',
        notes=('Sitting Nevada Attorney General (since 2019). Former NV state senate majority '
               'leader. D candidate for NV Governor 2026.'),
        sources=['https://ballotpedia.org/Aaron_Ford']),

    # ════════════════════════════════════════════════════════════════
    # COLORADO Governor (Jared Polis term-limited · D primary 6/30)
    # ════════════════════════════════════════════════════════════════
    gov('Phil Weiser', 'phil-weiser-gov', 'CO',
        'Governor of Colorado (2026 D Candidate · sitting CO Attorney General)',
        'D', 'establishment_d', '2026-06-30',
        notes=('Sitting Colorado Attorney General (since 2019). Former U.S. Deputy Assistant '
               'Attorney General under Obama. Announced D candidate for CO Governor 2026.'),
        sources=['https://ballotpedia.org/Phil_Weiser']),
    gov('Michael Bennet', 'michael-bennet-gov', 'CO',
        'Governor of Colorado (2026 D Candidate · sitting U.S. Senator)',
        'D', 'establishment_d', '2026-06-30',
        notes=('Sitting U.S. Senator from CO (2009-present). Reportedly considering 2026 D '
               'primary for CO Governor. 2020 D presidential candidate.'),
        sources=['https://ballotpedia.org/Michael_Bennet']),

    # ════════════════════════════════════════════════════════════════
    # KANSAS Governor (Laura Kelly term-limited · R primary 8/4)
    # ════════════════════════════════════════════════════════════════
    gov('Vicki Schmidt', 'vicki-schmidt-gov', 'KS',
        'Governor of Kansas (2026 R Candidate · sitting KS Insurance Commissioner)',
        'R', 'establishment_r', '2026-08-04',
        notes=('Sitting Kansas Insurance Commissioner (since 2019). R primary candidate for KS '
               'Governor 2026.'),
        sources=['https://ballotpedia.org/Vicki_Schmidt']),
    gov('Scott Schwab', 'scott-schwab-gov', 'KS',
        'Governor of Kansas (2026 R Candidate · sitting KS Secretary of State)',
        'R', 'establishment_r', '2026-08-04',
        notes=('Sitting Kansas Secretary of State (since 2019). Former KS state representative. '
               'R candidate for KS Governor 2026.'),
        sources=['https://ballotpedia.org/Scott_Schwab']),

    # ════════════════════════════════════════════════════════════════
    # OKLAHOMA Governor (Kevin Stitt term-limited · R primary 6/30)
    # ════════════════════════════════════════════════════════════════
    gov('Charles McCall', 'charles-mccall-gov', 'OK',
        'Governor of Oklahoma (2026 R Candidate · former Speaker of OK House)',
        'R', 'establishment_r', '2026-06-30',
        notes=('Former Speaker of the Oklahoma House of Representatives (2017-2024). R candidate '
               'for OK Governor 2026.'),
        sources=['https://ballotpedia.org/Charles_McCall']),
    gov('Mike Mazzei', 'mike-mazzei-gov', 'OK',
        'Governor of Oklahoma (2026 R Candidate · former OK state senator · businessman)',
        'R', 'establishment_r', '2026-06-30',
        notes='Former Oklahoma state senator. Tulsa-area businessman. R candidate for OK Governor 2026.',
        sources=['https://ballotpedia.org/Mike_Mazzei']),
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
        print(f'  {action} {r["name"]:<28s} ({r["state"]} Gov {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
