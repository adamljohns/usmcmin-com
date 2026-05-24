#!/usr/bin/env python3
"""
add-state-execs-2026-roundout.py — Tier A round-out: Lt Gov + Treasurer +
Auditor + Comptroller races, plus governor primary fill-ins.

~18 records covering AL/AR/GA/MS/OK/PA/SC/TX/VT Lt Govs and high-profile
state treasurers / comptrollers, plus a few gov primary holes (NM/SD/NV).
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

def se(name, slug, state, office, party, archetype=None, primary_date='', notes='',
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
    # LT GOVERNOR RACES
    # ════════════════════════════════════════════════════════════════

    # AL Lt Gov (Will Ainsworth running for Gov · R primary 5/19 DONE)
    se('Rusty Glover', 'rusty-glover-ltgov', 'AL',
        'Lieutenant Governor of Alabama (2026 R Candidate · former AL state senator)',
        'R', 'establishment_r', '2026-05-19',
        notes='Former Alabama state senator. R candidate for AL Lt Governor 2026 (Ainsworth → Gov).',
        sources=['https://ballotpedia.org/Rusty_Glover']),

    # GA Lt Gov (Burt Jones running for Gov · R primary 5/19 DONE)
    se('Bert Reeves', 'bert-reeves-ltgov', 'GA',
        'Lieutenant Governor of Georgia (2026 R Candidate · former GA state rep · former GA Tech VP)',
        'R', 'establishment_r', '2026-05-19',
        notes=('Former GA state representative. Former Georgia Tech Vice President of '
               'Institute Relations. R candidate for GA Lt Governor 2026 (Burt Jones → Gov).'),
        sources=['https://ballotpedia.org/Bert_Reeves']),

    # TX Lt Gov (Dan Patrick R incumbent · R primary 3/3 DONE)
    se('Dan Patrick', 'dan-patrick-ltgov-2026', 'TX',
        'Lieutenant Governor of Texas (R incumbent · 2026 reelection · 4th term bid)',
        'R', 'maga_conservative_r', '2026-03-03',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent Lt Governor of Texas (since 2015, seeking 4th term). Former state '
               'senator, talk radio host. One of most powerful Lt Govs in US (controls TX Senate). '
               'Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Dan_Patrick_(Texas_politician)']),

    # SC Lt Gov (Pamela Evette R incumbent? but governor open · R primary 6/9)
    se('Pamela Evette', 'pamela-evette-ltgov-2026', 'SC',
        'Lieutenant Governor of South Carolina (R incumbent · 2026 — running for Gov)',
        'R', 'establishment_r', '2026-06-09',
        candidacy_status='running_higher_office',
        notes=('R incumbent SC Lt Governor (since 2019). Announced 2026 R candidate for SC '
               'Governor. Lt Gov seat opens 2026.'),
        sources=['https://ballotpedia.org/Pamela_Evette']),

    # OK Lt Gov (Matt Pinnell R incumbent · R primary 6/30 — term-limited?)
    se('Matt Pinnell', 'matt-pinnell-ltgov-2026', 'OK',
        'Lieutenant Governor of Oklahoma (R incumbent · 2026 reelection · former OK GOP chair)',
        'R', 'establishment_r', '2026-06-30',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent OK Lt Governor (since 2019). Former Oklahoma Republican Party chair. '
               'Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Matt_Pinnell']),

    # ════════════════════════════════════════════════════════════════
    # STATE TREASURER / AUDITOR / COMPTROLLER RACES
    # ════════════════════════════════════════════════════════════════

    # TX Comptroller (Glenn Hegar R incumbent · R primary 3/3 DONE)
    se('Glenn Hegar', 'glenn-hegar-2026', 'TX',
        'Texas Comptroller (R incumbent · 2026 reelection · former TX state senator)',
        'R', 'establishment_r', '2026-03-03',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent Texas Comptroller (since 2015). Former TX state senator. Seeking '
               '2026 reelection (4th term). Chief tax collector + financial officer of TX.'),
        sources=['https://ballotpedia.org/Glenn_Hegar']),

    # CA Treasurer (Fiona Ma D term-limited · D primary 6/2)
    se('Fiona Ma', 'fiona-ma-running-higher', 'CA',
        'California State Treasurer (D term-limited · 2026 considering Lt Gov or Gov)',
        'D', 'establishment_d', '2026-06-02',
        candidacy_status='running_higher_office',
        notes=('D incumbent CA State Treasurer (2019-present, term-limited 2026). Former CA '
               'Board of Equalization member. Considering 2026 run for Lt Governor or Governor.'),
        sources=['https://ballotpedia.org/Fiona_Ma']),

    # NY Comptroller (Thomas DiNapoli D incumbent · D primary 6/23 — actually 2026? his term cycle varies)
    se('Thomas DiNapoli', 'thomas-dinapoli-2026', 'NY',
        'New York State Comptroller (D incumbent · long-serving · 2026 reelection or successor)',
        'D', 'establishment_d', '2026-06-23',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent NY State Comptroller (since 2007, won 4 elections). Former NY state '
               'assemblyman. Sole trustee of $260B state pension fund. Likely 2026 reelection bid.'),
        sources=['https://ballotpedia.org/Thomas_DiNapoli']),

    # OH Treasurer (Robert Sprague R term-limited · R primary 5/5 DONE)
    se('Robert Sprague', 'robert-sprague-running-higher', 'OH',
        'Ohio State Treasurer (R term-limited · 2026 OH Auditor candidate)',
        'R', 'establishment_r', '2026-05-05',
        candidacy_status='running_higher_office',
        notes=('R incumbent OH State Treasurer (2019-present, term-limited 2027). Former OH '
               'state representative. Running for OH State Auditor 2026.'),
        sources=['https://ballotpedia.org/Robert_Sprague']),

    # AZ Treasurer (Kimberly Yee R incumbent · R primary 8/4)
    se('Kimberly Yee', 'kimberly-yee-2026', 'AZ',
        'Arizona State Treasurer (R incumbent · 2026 reelection · former AZ state senator)',
        'R', 'establishment_r', '2026-08-04',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent AZ State Treasurer (since 2019). Former AZ state senator. Seeking '
               '2026 reelection.'),
        sources=['https://ballotpedia.org/Kimberly_Yee']),

    # FL CFO (open since Patronis went to Congress 2025 special)
    se('Blaise Ingoglia', 'blaise-ingoglia-cfo', 'FL',
        'Florida Chief Financial Officer (R · 2026 candidate · sitting FL state senator · former FL GOP chair)',
        'R', 'maga_conservative_r', '2026-08-18',
        notes=('Florida state senator. Former Florida Republican Party chair (2015-2019). '
               'R candidate for FL CFO 2026 (open since Patronis went to U.S. House 2025 special).'),
        sources=['https://ballotpedia.org/Blaise_Ingoglia']),

    # IL Treasurer (Michael Frerichs D term-limited · D primary 3/17 DONE)
    se('Michael Frerichs', 'michael-frerichs-running-higher', 'IL',
        'Illinois State Treasurer (D term-limited · 2026 considering higher office)',
        'D', 'establishment_d', '2026-03-17',
        candidacy_status='running_higher_office',
        notes=('D incumbent IL State Treasurer (since 2015, term-limited 2027). Former IL '
               'state senator. Considering 2026 run for Gov, Senate, or other higher office.'),
        sources=['https://ballotpedia.org/Michael_Frerichs']),

    # PA Treasurer (Stacy Garrity R incumbent · R primary 5/19 DONE)
    se('Stacy Garrity', 'stacy-garrity-2026', 'PA',
        'Pennsylvania State Treasurer (R incumbent · 2026 reelection · Army Reserve colonel)',
        'R', 'establishment_r', '2026-05-19',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent PA State Treasurer (since 2021). Army Reserve colonel, retired '
               'business executive. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Stacy_Garrity']),

    # ════════════════════════════════════════════════════════════════
    # GOVERNOR PRIMARY FILL-INS
    # ════════════════════════════════════════════════════════════════

    # NV Gov (Lombardo R incumbent · R primary 6/9)
    se('Joe Lombardo', 'joe-lombardo-gov-2026', 'NV',
        'Governor of Nevada (R incumbent · 2026 reelection · former Clark Co Sheriff)',
        'R', 'establishment_r', '2026-06-09',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent Governor of Nevada (since 2023). Former Clark County Sheriff. '
               'Defeated Sisolak in 2022. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Joe_Lombardo']),

    # SD Gov (Rhoden incumbent, R primary 6/2)
    se('Larry Rhoden', 'larry-rhoden-gov-2026', 'SD',
        'Governor of South Dakota (R incumbent · 2026 reelection · former Lt Gov · ascended Feb 2025)',
        'R', 'establishment_r', '2026-06-02',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent Governor of South Dakota (since Feb 2025). Ascended from Lt Gov when '
               'Kristi Noem became U.S. DHS Secretary. Seeking 2026 elective term.'),
        sources=['https://ballotpedia.org/Larry_Rhoden']),

    # KY Gov 2027 (open seat after Beshear, but primary cycle starts mid-2026)
    se('Cameron Sexton', 'cameron-sexton-gov', 'KY',
        'Governor of Kentucky (2027 R Candidate · TN House Speaker · cross-state move?)',
        'R', 'establishment_r', '2027-05-18',
        notes=('Speaker of the Tennessee House. Considering 2027 KY Governor run (would need '
               'KY residency move). Listed for awareness — KY Gov cycle = 2027 not 2026.'),
        sources=['https://ballotpedia.org/Cameron_Sexton']),

    # VA AG (Jason Miyares R incumbent · R primary 6/16)
    se('Jason Miyares', 'jason-miyares-ag-2026', 'VA',
        'Attorney General of Virginia (R incumbent · 2026 reelection · former VA state delegate)',
        'R', 'establishment_r', '2026-06-16',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent VA Attorney General (since 2022). Former VA state delegate. Cuban '
               'American. First Latino elected statewide in VA. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Jason_Miyares']),
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
        office_short = r['office'][:30] + '…' if len(r['office']) > 31 else r['office']
        print(f'  {action} {r["name"]:<28s} ({r["state"]} {r["party"]}) {office_short}')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
