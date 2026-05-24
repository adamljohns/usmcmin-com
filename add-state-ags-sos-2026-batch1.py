#!/usr/bin/env python3
"""
add-state-ags-sos-2026-batch1.py — 2026 state AG + SoS races (batch 1).

Targets high-profile state Attorney General + Secretary of State races
across AZ, MI, OH, WI, IA, GA, TX, AL, NV, CO, NM.
~16 records.
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

def state_office(name, slug, state, office, party, archetype=None, primary_date='', notes='',
                 sources=None, profile_extra=None, candidacy_status='primary_candidate',
                 source_url_label='State_executive_official_elections'):
    """Generic state executive (AG, SoS, Treasurer, etc.) record builder."""
    return {
        'name': name, 'slug': slug, 'state': state,
        'office': office, 'jurisdiction': JURISDICTION.get(state, f'State of {state}'),
        'party': party, 'level': 'state', 'district': None,
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '', 'sources': sources or [f'https://ballotpedia.org/{source_url_label}_in_{state}_2026'],
        'notes': notes, 'footnotes': [], 'answer_footnotes': {},
        'scores': scores_from(archetype) if archetype else empty_scores(),
        'profile': {
            'next_election': 2026, 'next_election_type': 'primary',
            'seat_up_next': True, 'next_election_date': primary_date,
            'confidence': 'archetype_curated' if archetype else 'low_evidence',
            'confidence_note': f'2026-05-20 — 2026 {state} state executive race. Archetype: {archetype}.' if archetype else f'2026-05-20 — 2026 {state} state executive placeholder.',
            **(profile_extra or {}),
        },
    }

RECORDS = [
    # ════════════════════════════════════════════════════════════════
    # ARIZONA Attorney General (Kris Mayes D incumbent · 8/4 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Kris Mayes', 'kris-mayes-ag', 'AZ',
        'Attorney General of Arizona (D incumbent · 2026 reelection · won 2022 by 280 votes)',
        'D', 'establishment_d', '2026-08-04',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent AZ Attorney General (since 2023). Won 2022 by margin of 280 votes '
               'over Abe Hamadeh. Former AZ state senator. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Kris_Mayes']),
    state_office('Rodney Glassman', 'rodney-glassman-ag', 'AZ',
        'Attorney General of Arizona (2026 R Candidate · attorney · 2010 D Senate nominee, now R)',
        'R', 'maga_conservative_r', '2026-08-04',
        notes=('Phoenix attorney. Former Democrat (2010 D U.S. Senate nominee vs McCain). '
               'Switched to GOP. R primary candidate for AZ AG 2026.'),
        sources=['https://ballotpedia.org/Rodney_Glassman']),

    # ════════════════════════════════════════════════════════════════
    # MICHIGAN Attorney General (Dana Nessel D term-limited · 8/4 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Mark Totten', 'mark-totten-ag', 'MI',
        'Attorney General of Michigan (2026 D Candidate · U.S. Attorney Western District MI)',
        'D', 'establishment_d', '2026-08-04',
        notes=('U.S. Attorney for the Western District of Michigan (Biden appointee). Former MI '
               'state senator. 2014 D nominee for MI AG. D candidate for MI AG 2026.'),
        sources=['https://ballotpedia.org/Mark_Totten']),
    state_office('Matthew DePerno', 'matthew-deperno-ag', 'MI',
        'Attorney General of Michigan (2026 R Candidate · 2022 R nominee · election integrity attorney)',
        'R', 'maga_conservative_r', '2026-08-04',
        notes=('Kalamazoo attorney. 2022 R nominee for MI AG (lost to Nessel). Election integrity '
               'activist. Indicted 2023 over voting machine access; case dismissed 2024. May run again 2026.'),
        sources=['https://ballotpedia.org/Matthew_DePerno']),

    # ════════════════════════════════════════════════════════════════
    # OHIO Attorney General (Dave Yost R term-limited · 5/5 primary DONE)
    # ════════════════════════════════════════════════════════════════
    state_office('Mathura Sridharan', 'mathura-sridharan-ag', 'OH',
        'Attorney General of Ohio (2026 R Candidate · OH deputy SG)',
        'R', 'establishment_r', '2026-05-05',
        notes='Ohio Deputy Solicitor General. R primary candidate for OH AG 2026.',
        sources=['https://ballotpedia.org/Mathura_Sridharan']),
    state_office('Elliot Forhan', 'elliot-forhan-ag', 'OH',
        'Attorney General of Ohio (2026 D Candidate · former OH state rep · attorney)',
        'D', 'establishment_d', '2026-05-05',
        notes='Former Ohio state representative (Cleveland-area). Attorney. D candidate for OH AG 2026.',
        sources=['https://ballotpedia.org/Elliot_Forhan']),

    # ════════════════════════════════════════════════════════════════
    # WISCONSIN Attorney General (Josh Kaul D incumbent · 8/11 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Josh Kaul', 'josh-kaul-ag-2026', 'WI',
        'Attorney General of Wisconsin (D incumbent · 2026 reelection · former federal prosecutor)',
        'D', 'establishment_d', '2026-08-11',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent WI Attorney General (since 2019). Former federal prosecutor. '
               'Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Josh_Kaul']),
    state_office('Eric Toney', 'eric-toney-ag', 'WI',
        'Attorney General of Wisconsin (2026 R Candidate · Fond du Lac Co DA · 2022 R nominee)',
        'R', 'establishment_r', '2026-08-11',
        notes=('Fond du Lac County District Attorney. 2022 R nominee for WI AG (lost narrowly '
               'to Kaul). May run again 2026.'),
        sources=['https://ballotpedia.org/Eric_Toney']),

    # ════════════════════════════════════════════════════════════════
    # IOWA Attorney General (Brenna Bird R incumbent · 6/2 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Brenna Bird', 'brenna-bird-ag-2026', 'IA',
        'Attorney General of Iowa (R incumbent · 2026 reelection · ousted Tom Miller 2022)',
        'R', 'establishment_r', '2026-06-02',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent IA Attorney General (since 2023). Defeated long-serving D AG Tom Miller '
               'in 2022. Trump-aligned conservative. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Brenna_Bird']),

    # ════════════════════════════════════════════════════════════════
    # TEXAS Attorney General (Open · Paxton to U.S. Senate · 3/3 DONE)
    # ════════════════════════════════════════════════════════════════
    state_office('Aaron Reitz', 'aaron-reitz-ag', 'TX',
        'Attorney General of Texas (2026 R Candidate · former DOJ official · Trump appointee)',
        'R', 'maga_conservative_r', '2026-03-03',
        notes=('Trump DOJ official (Assistant Attorney General for Legal Policy). Former chief '
               'of staff to Sen Ted Cruz. R candidate for TX AG 2026 (Paxton open seat).'),
        sources=['https://ballotpedia.org/Aaron_Reitz']),
    state_office('John Bash', 'john-bash-ag', 'TX',
        'Attorney General of Texas (2026 R Candidate · former U.S. Attorney WD-TX · Trump-era prosecutor)',
        'R', 'establishment_r', '2026-03-03',
        notes=('Former U.S. Attorney for Western District of Texas (Trump appointee). Former '
               'White House associate counsel. R candidate for TX AG 2026.'),
        sources=['https://ballotpedia.org/John_Bash']),

    # ════════════════════════════════════════════════════════════════
    # ARIZONA Secretary of State (Adrian Fontes D incumbent · 8/4 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Adrian Fontes', 'adrian-fontes-sos-2026', 'AZ',
        'Secretary of State of Arizona (D incumbent · 2026 reelection · former Maricopa Co recorder)',
        'D', 'establishment_d', '2026-08-04',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent AZ Secretary of State (since 2023). Former Maricopa County Recorder. '
               'Defeated election-denier Mark Finchem in 2022. Marine Corps veteran. '
               'Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Adrian_Fontes']),

    # ════════════════════════════════════════════════════════════════
    # OHIO Secretary of State (Frank LaRose R · running for U.S. Senate 2024 lost)
    # ════════════════════════════════════════════════════════════════
    state_office('Frank LaRose', 'frank-larose-sos-2026', 'OH',
        'Secretary of State of Ohio (R incumbent · 2026 reelection · former state senator)',
        'R', 'establishment_r', '2026-05-05',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent OH Secretary of State (since 2019). Former OH state senator. '
               '2024 R U.S. Senate primary candidate (lost). May seek 2026 reelection or '
               'another office.'),
        sources=['https://ballotpedia.org/Frank_LaRose']),

    # ════════════════════════════════════════════════════════════════
    # COLORADO Secretary of State (Jena Griswold D term-limited · 6/30 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Jena Griswold', 'jena-griswold-sos-2026', 'CO',
        'Secretary of State of Colorado (D term-limited · 2026 considering AG or governor)',
        'D', 'progressive_d', '2026-06-30',
        candidacy_status='running_higher_office',
        notes=('D Secretary of State of Colorado (since 2019). Term-limited 2026. Vocal critic '
               'of Trump-era election challenges. May run for CO AG or governor 2026.'),
        sources=['https://ballotpedia.org/Jena_Griswold']),

    # ════════════════════════════════════════════════════════════════
    # NEW MEXICO Secretary of State (Maggie Toulouse Oliver D term-limited · 6/2)
    # ════════════════════════════════════════════════════════════════
    state_office('Bernadette Sanchez', 'bernadette-sanchez-sos', 'NM',
        'Secretary of State of New Mexico (2026 D Candidate · former NM state senator)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Former NM state senator. D candidate for NM Secretary of State 2026.'),
        sources=['https://ballotpedia.org/Bernadette_Sanchez']),

    # ════════════════════════════════════════════════════════════════
    # NEVADA Secretary of State (Cisco Aguilar D incumbent · 6/9 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Cisco Aguilar', 'cisco-aguilar-sos-2026', 'NV',
        'Secretary of State of Nevada (D incumbent · 2026 reelection · attorney)',
        'D', 'establishment_d', '2026-06-09',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent NV Secretary of State (since 2023). Attorney, former Andre Agassi '
               'Charitable Foundation board chair. Defeated election denier Jim Marchant in 2022. '
               'Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Cisco_Aguilar']),
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
        office_short = r['office'][:24] + '…' if len(r['office']) > 25 else r['office']
        print(f'  {action} {r["name"]:<28s} ({r["state"]} {r["party"]}) {office_short}')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
