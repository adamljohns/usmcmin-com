#!/usr/bin/env python3
"""
add-state-ags-sos-2026-batch2.py — 2026 state AG + SoS races (batch 2).

Targets NC, MD, MN, IL, NM, MA, MA SoS, OR, WA, KS, NE, WV, AR.
~15 records of declared/incumbent state AGs + SoS.
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
                 sources=None, profile_extra=None, candidacy_status='primary_candidate'):
    return {
        'name': name, 'slug': slug, 'state': state,
        'office': office, 'jurisdiction': JURISDICTION.get(state, f'State of {state}'),
        'party': party, 'level': 'state', 'district': None,
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '', 'sources': sources or [f'https://ballotpedia.org/State_executive_official_elections_in_{state}_2026'],
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
    # NORTH CAROLINA Attorney General (Jeff Jackson D incumbent · 3/3 DONE)
    # ════════════════════════════════════════════════════════════════
    state_office('Jeff Jackson', 'jeff-jackson-ag-2026', 'NC',
        'Attorney General of North Carolina (D incumbent · 2026 reelection · former U.S. Rep NC-14)',
        'D', 'establishment_d', '2026-03-03',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent NC Attorney General (since 2025). Former U.S. Representative NC-14 '
               '(2023-2025, gerrymandered out). Army National Guard JAG. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Jeff_Jackson']),

    # ════════════════════════════════════════════════════════════════
    # MARYLAND Attorney General (Anthony Brown D incumbent · 6/30 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Anthony Brown', 'anthony-brown-ag-2026', 'MD',
        'Attorney General of Maryland (D incumbent · 2026 reelection · former U.S. Rep MD-04)',
        'D', 'establishment_d', '2026-06-30',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent MD Attorney General (since 2023). Former U.S. Representative MD-04 '
               '(2017-2023). Former MD Lt Governor. Iraq War veteran. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Anthony_Brown_(Maryland_politician)']),

    # ════════════════════════════════════════════════════════════════
    # MINNESOTA Attorney General (Keith Ellison D incumbent · DFL primary 8/11)
    # ════════════════════════════════════════════════════════════════
    state_office('Keith Ellison', 'keith-ellison-ag-2026', 'MN',
        'Attorney General of Minnesota (D incumbent · 2026 reelection · former DNC vice chair)',
        'D', 'progressive_d', '2026-08-11',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent MN Attorney General (since 2019). Former U.S. Representative MN-05 '
               '(2007-2019). Former DNC vice chair. Lead prosecutor in Derek Chauvin / George '
               'Floyd murder trial. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Keith_Ellison']),

    # ════════════════════════════════════════════════════════════════
    # ILLINOIS Attorney General (Kwame Raoul D incumbent · 3/17 DONE)
    # ════════════════════════════════════════════════════════════════
    state_office('Kwame Raoul', 'kwame-raoul-ag-2026', 'IL',
        'Attorney General of Illinois (D incumbent · 2026 reelection · former IL state senator)',
        'D', 'establishment_d', '2026-03-17',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent IL Attorney General (since 2019). Former IL state senator. Succeeded '
               'Lisa Madigan. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Kwame_Raoul']),

    # ════════════════════════════════════════════════════════════════
    # NEW MEXICO Attorney General (Raúl Torrez D incumbent · 6/2 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Raul Torrez', 'raul-torrez-ag-2026', 'NM',
        'Attorney General of New Mexico (D incumbent · 2026 reelection · former Bernalillo Co DA)',
        'D', 'establishment_d', '2026-06-02',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent NM Attorney General (since 2023). Former Bernalillo County District '
               'Attorney. Stanford law alum. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Ra%C3%BAl_Torrez']),

    # ════════════════════════════════════════════════════════════════
    # WEST VIRGINIA Attorney General (JB McCuskey R · took over 2025)
    # ════════════════════════════════════════════════════════════════
    state_office('JB McCuskey', 'jb-mccuskey-ag-2026', 'WV',
        'Attorney General of West Virginia (R incumbent · sworn 2025 · former WV State Auditor)',
        'R', 'establishment_r', '2026-05-12',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent WV Attorney General (since 2025). Former WV State Auditor (2017-2025). '
               'Succeeded Patrick Morrisey (now WV Governor). Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/JB_McCuskey']),

    # ════════════════════════════════════════════════════════════════
    # ARKANSAS Attorney General (Tim Griffin R incumbent · 5/19 DONE)
    # ════════════════════════════════════════════════════════════════
    state_office('Tim Griffin', 'tim-griffin-ag-2026', 'AR',
        'Attorney General of Arkansas (R incumbent · 2026 reelection · former U.S. Rep AR-02)',
        'R', 'establishment_r', '2026-05-19',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent AR Attorney General (since 2023). Former U.S. Representative AR-02 '
               '(2011-2015). Former AR Lt Governor. Army Reserve JAG. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Tim_Griffin']),

    # ════════════════════════════════════════════════════════════════
    # MASSACHUSETTS Attorney General (Andrea Campbell D incumbent · 9/8 primary)
    # ════════════════════════════════════════════════════════════════
    state_office('Andrea Campbell', 'andrea-campbell-ag-2026', 'MA',
        'Attorney General of Massachusetts (D incumbent · 2026 reelection · former Boston city councilor)',
        'D', 'establishment_d', '2026-09-08',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent MA Attorney General (since 2023). Former Boston city councilor. '
               '2021 D primary candidate for Boston Mayor. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Andrea_Campbell']),

    # ════════════════════════════════════════════════════════════════
    # GEORGIA Attorney General (Chris Carr R RUNNING FOR GOVERNOR · open)
    # ════════════════════════════════════════════════════════════════
    state_office('Chris Carr', 'chris-carr-ag-running-higher', 'GA',
        'Attorney General of Georgia (R · running for GA Governor 2026 · seat open)',
        'R', 'establishment_r', '2026-05-19',
        candidacy_status='running_higher_office',
        notes=('R Attorney General of Georgia (2017-present). Announced 2026 R candidate for GA '
               'Governor. AG seat opens for 2026.'),
        sources=['https://ballotpedia.org/Chris_Carr_(Georgia)']),

    # ════════════════════════════════════════════════════════════════
    # FLORIDA Attorney General (James Uthmeier R appointed Feb 2025 · 8/18)
    # ════════════════════════════════════════════════════════════════
    state_office('James Uthmeier', 'james-uthmeier-ag', 'FL',
        'Attorney General of Florida (R incumbent · appointed Feb 2025 by DeSantis · 2026 elective)',
        'R', 'maga_conservative_r', '2026-08-18',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent FL Attorney General (since Feb 2025, DeSantis-appointed after Ashley '
               'Moody → U.S. Senate to succeed Rubio). Former DeSantis chief of staff. First '
               'elective bid for AG 2026.'),
        sources=['https://ballotpedia.org/James_Uthmeier']),

    # ════════════════════════════════════════════════════════════════
    # MICHIGAN Secretary of State (Jocelyn Benson RUNNING FOR GOV · open · 8/4)
    # ════════════════════════════════════════════════════════════════
    state_office('Jocelyn Benson', 'jocelyn-benson-running-higher', 'MI',
        'Secretary of State of Michigan (D · running for MI Governor 2026 · seat open)',
        'D', 'establishment_d', '2026-08-04',
        candidacy_status='running_higher_office',
        notes=('D Secretary of State of Michigan (2019-present). Announced 2026 D candidate for '
               'MI Governor. SoS seat opens for 2026.'),
        sources=['https://ballotpedia.org/Jocelyn_Benson']),

    # ════════════════════════════════════════════════════════════════
    # GEORGIA Secretary of State (Brad Raffensperger R RUNNING FOR GOV · open)
    # ════════════════════════════════════════════════════════════════
    state_office('Brad Raffensperger', 'brad-raffensperger-running-higher', 'GA',
        'Secretary of State of Georgia (R · running for GA Governor 2026 · seat open)',
        'R', 'establishment_r', '2026-05-19',
        candidacy_status='running_higher_office',
        notes=('R Secretary of State of Georgia (2019-present). Famously rejected Trump\'s 2020 '
               '"find 11,780 votes" call. Announced 2026 R candidate for GA Governor. SoS seat '
               'opens for 2026.'),
        sources=['https://ballotpedia.org/Brad_Raffensperger']),

    # ════════════════════════════════════════════════════════════════
    # WASHINGTON Secretary of State (Steve Hobbs D incumbent · top-2 8/4)
    # ════════════════════════════════════════════════════════════════
    state_office('Steve Hobbs', 'steve-hobbs-sos-2026', 'WA',
        'Secretary of State of Washington (D incumbent · 2026 reelection · former WA state senator)',
        'D', 'establishment_d', '2026-08-04',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent WA Secretary of State (since 2021, appointed by Inslee then elected '
               '2022). Former WA state senator. Army veteran. First D SoS in WA in over 50 years. '
               'Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Steve_Hobbs']),

    # ════════════════════════════════════════════════════════════════
    # MINNESOTA Secretary of State (Steve Simon D incumbent · DFL primary 8/11)
    # ════════════════════════════════════════════════════════════════
    state_office('Steve Simon', 'steve-simon-sos-2026', 'MN',
        'Secretary of State of Minnesota (D incumbent · 2026 reelection · long-serving SoS)',
        'D', 'establishment_d', '2026-08-11',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent MN Secretary of State (since 2015). Former MN state representative. '
               'Seeking 2026 reelection (his 4th term).'),
        sources=['https://ballotpedia.org/Steve_Simon']),

    # ════════════════════════════════════════════════════════════════
    # ILLINOIS Secretary of State (Alexi Giannoulias D incumbent · 3/17 DONE)
    # ════════════════════════════════════════════════════════════════
    state_office('Alexi Giannoulias', 'alexi-giannoulias-sos-2026', 'IL',
        'Secretary of State of Illinois (D incumbent · 2026 reelection · former IL state treasurer)',
        'D', 'establishment_d', '2026-03-17',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent IL Secretary of State (since 2023). Former IL State Treasurer '
               '(2007-2011). 2010 D U.S. Senate nominee (lost to Mark Kirk). Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Alexi_Giannoulias']),
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
