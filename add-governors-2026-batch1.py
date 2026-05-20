#!/usr/bin/env python3
"""
add-governors-2026-batch1.py — 2026 gubernatorial race expansion (batch 1).

Targets 4 high-profile open/competitive governor races: AL, SC, FL, AZ.
~16 records of declared/likely candidates.
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

# State name → "State of X" / "Commonwealth of X"
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
    """Build a governor candidate record."""
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
    # ALABAMA Governor (Kay Ivey term-limited · R primary 5/19 DONE)
    # ════════════════════════════════════════════════════════════════
    gov('Tim James', 'tim-james-gov', 'AL',
        'Governor of Alabama (2026 R Candidate · businessman · son of Gov Fob James)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes=('Businessman, son of former Alabama Governor Fob James (1979-83, 1995-99). '
               'Has run for AL Gov previously (2010 primary). R primary candidate 2026.'),
        sources=['https://ballotpedia.org/Tim_James']),
    gov('Lew Burdette', 'lew-burdette-gov', 'AL',
        'Governor of Alabama (2026 R Candidate · businessman + ministry executive)',
        'R', 'establishment_r', '2026-05-19',
        notes='Businessman and Christian ministry executive. R primary candidate for AL Governor.',
        sources=['https://ballotpedia.org/Lew_Burdette']),
    gov('Yolanda Flowers', 'yolanda-flowers-gov', 'AL',
        'Governor of Alabama (2026 D Candidate · 2022 D nominee · former educator)',
        'D', 'establishment_d', '2026-05-19',
        notes='2022 D nominee for AL Governor (lost to Ivey). Former educator. Considering 2026 rematch.',
        sources=['https://ballotpedia.org/Yolanda_Flowers']),

    # ════════════════════════════════════════════════════════════════
    # SOUTH CAROLINA Governor (Henry McMaster term-limited · R primary 6/9)
    # ════════════════════════════════════════════════════════════════
    gov('Joe Cunningham', 'joe-cunningham-gov', 'SC',
        'Governor of South Carolina (2026 D Candidate · former rep SC-01 · 2022 D nominee)',
        'D', 'establishment_d', '2026-06-09',
        notes=('Former U.S. Representative SC-01 (2019-2021), 2022 D nominee for SC Governor '
               '(lost to McMaster). Charleston attorney. Likely 2026 D candidate.'),
        sources=['https://ballotpedia.org/Joe_Cunningham']),
    gov('Mia McLeod', 'mia-mcleod-gov', 'SC',
        'Governor of South Carolina (2026 D Candidate · former SC state senator)',
        'D', 'establishment_d', '2026-06-09',
        notes=('Former SC state senator. Ran in 2022 D primary for governor (lost to Cunningham). '
               'D candidate 2026.'),
        sources=['https://ballotpedia.org/Mia_McLeod']),

    # ════════════════════════════════════════════════════════════════
    # FLORIDA Governor (Ron DeSantis term-limited · R primary 8/25)
    # ════════════════════════════════════════════════════════════════
    gov('Casey DeSantis', 'casey-desantis-gov', 'FL',
        'Governor of Florida (2026 R Candidate · current First Lady of Florida)',
        'R', 'maga_conservative_r', '2026-08-25',
        notes=('Current First Lady of Florida (wife of term-limited Gov Ron DeSantis). '
               'Reportedly considering R primary run for governor. Former TV news anchor.'),
        sources=['https://ballotpedia.org/Casey_DeSantis']),
    gov('Wilton Simpson', 'wilton-simpson-gov', 'FL',
        'Governor of Florida (2026 R Candidate · FL Agriculture Commissioner · former Senate Pres)',
        'R', 'establishment_r', '2026-08-25',
        notes=('Florida Commissioner of Agriculture and Consumer Services (since 2023). '
               'Former Florida Senate President (2020-2022). R candidate for Governor 2026.'),
        sources=['https://ballotpedia.org/Wilton_Simpson']),
    gov('Jared Moskowitz', 'jared-moskowitz-gov', 'FL',
        'Governor of Florida (2026 D Candidate · U.S. Rep FL-23 · former FL emergency mgmt director)',
        'D', 'establishment_d', '2026-08-25',
        notes=('U.S. Representative FL-23 (2023-present). Former FL Division of Emergency '
               'Management director under DeSantis. Reportedly considering 2026 D gubernatorial run.'),
        sources=['https://ballotpedia.org/Jared_Moskowitz']),
    gov('Anna Eskamani', 'anna-eskamani-gov', 'FL',
        'Governor of Florida (2026 D Candidate · FL state rep · progressive)',
        'D', 'progressive_d', '2026-08-25',
        notes='Florida state representative (Orlando). Progressive D candidate for FL Governor 2026.',
        sources=['https://ballotpedia.org/Anna_Eskamani']),

    # ════════════════════════════════════════════════════════════════
    # ARIZONA Governor (Katie Hobbs D incumbent · R primary 8/4)
    # ════════════════════════════════════════════════════════════════
    gov('Karrin Taylor Robson', 'karrin-taylor-robson-gov', 'AZ',
        'Governor of Arizona (2026 R Candidate · businesswoman · 2022 R primary candidate)',
        'R', 'establishment_r', '2026-08-04',
        notes=('Phoenix businesswoman, former AZ Board of Regents. 2022 R primary candidate '
               '(lost to Kari Lake). Running again 2026. Trump-endorsed in some past cycles.'),
        sources=['https://ballotpedia.org/Karrin_Taylor_Robson']),
    gov('Mark Lamb', 'mark-lamb-gov', 'AZ',
        'Governor of Arizona (2026 R Candidate · Pinal County Sheriff · 2024 U.S. Senate primary)',
        'R', 'maga_conservative_r', '2026-08-04',
        notes=('Pinal County Sheriff. 2024 R primary candidate for U.S. Senate (lost to Lake). '
               'Pivoted to gubernatorial primary 2026.'),
        sources=['https://ballotpedia.org/Mark_Lamb']),
    gov('Katie Hobbs', 'katie-hobbs-gov-2026', 'AZ',
        'Governor of Arizona (D incumbent · 2026 reelection candidate · won 2022 vs Lake)',
        'D', 'establishment_d', '2026-08-04',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Arizona (sworn 2023). Former AZ Secretary of State. '
               'Defeated Kari Lake in narrow 2022 race. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Katie_Hobbs']),

    # ════════════════════════════════════════════════════════════════
    # GEORGIA Governor (Brian Kemp term-limited · R primary 5/19 DONE)
    # ════════════════════════════════════════════════════════════════
    gov('Stacey Abrams', 'stacey-abrams-gov-2026', 'GA',
        'Governor of Georgia (2026 D Candidate · 2018 + 2022 D nominee · voter rights activist)',
        'D', 'progressive_d', '2026-05-19',
        notes=('2018 and 2022 D nominee for GA Governor (lost both to Kemp). Founder Fair Fight '
               'Action. Considering third gubernatorial bid 2026.'),
        sources=['https://ballotpedia.org/Stacey_Abrams']),
    gov('Marc Morial', 'marc-morial-gov', 'GA',
        'Governor of Georgia (2026 D Candidate · former New Orleans mayor · National Urban League pres)',
        'D', 'establishment_d', '2026-05-19',
        notes=('National Urban League president (since 2003). Former mayor of New Orleans (1994-2002). '
               'Reportedly considering GA gubernatorial run 2026.'),
        sources=['https://ballotpedia.org/Marc_Morial']),
    gov('Geoff Duncan', 'geoff-duncan-gov', 'GA',
        'Governor of Georgia (2026 Candidate · former GA Lt Gov · anti-Trump Republican)',
        'R', 'establishment_r', '2026-05-19',
        notes=('Former GA Lt Governor (2019-2023). Vocal anti-Trump Republican. Endorsed Harris '
               'in 2024. Considering 2026 gubernatorial bid (party affiliation TBD - may run as D).'),
        sources=['https://ballotpedia.org/Geoff_Duncan']),

    # ════════════════════════════════════════════════════════════════
    # MICHIGAN Governor (Gretchen Whitmer term-limited · R primary 8/4)
    # ════════════════════════════════════════════════════════════════
    gov('Mike Duggan', 'mike-duggan-gov', 'MI',
        'Governor of Michigan (2026 I Candidate · Detroit mayor · former Democrat running Independent)',
        'I', 'establishment_d', '2026-08-04',
        notes=('Mayor of Detroit (since 2014). Lifelong Democrat, announced 2026 gubernatorial bid '
               'as Independent. Considered moderate / business-friendly.'),
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
        print(f'  {action} {r["name"]:<28s} ({r["state"]} Gov {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
