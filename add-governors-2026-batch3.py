#!/usr/bin/env python3
"""
add-governors-2026-batch3.py — 2026 gubernatorial expansion (batch 3).

Targets remaining states with 2026 governor races: NM, MN, MA, MD, ME, CT, RI,
HI, AK, NH, VT, PA, WI, NE, WY, OR, ID, NY.
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
    # NEW MEXICO Governor (Michelle Lujan Grisham term-limited · 6/2)
    # ════════════════════════════════════════════════════════════════
    gov('Deb Haaland', 'deb-haaland-gov', 'NM',
        'Governor of New Mexico (2026 D Candidate · former U.S. Sec of Interior · former Rep NM-01)',
        'D', 'progressive_d', '2026-06-02',
        notes=('Former U.S. Secretary of the Interior under Biden (2021-2025). Former U.S. Rep '
               'NM-01 (2019-2021). First Native American Cabinet secretary. D candidate for '
               'NM Governor 2026.'),
        sources=['https://ballotpedia.org/Deb_Haaland']),
    gov('Sam Bregman', 'sam-bregman-gov', 'NM',
        'Governor of New Mexico (2026 D Candidate · Bernalillo Co District Attorney)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Bernalillo County (Albuquerque) District Attorney since 2023. Former chair of '
               'NM Democratic Party. D candidate for NM Governor 2026.'),
        sources=['https://ballotpedia.org/Sam_Bregman']),
    gov('Mark Ronchetti', 'mark-ronchetti-gov-2026', 'NM',
        'Governor of New Mexico (2026 R Candidate · 2022 R nominee · former meteorologist)',
        'R', 'establishment_r', '2026-06-02',
        notes=('Former TV meteorologist (KRQE Albuquerque). 2020 R nominee for U.S. Senate, '
               '2022 R nominee for NM Governor (lost both). Likely 2026 R candidate.'),
        sources=['https://ballotpedia.org/Mark_Ronchetti']),

    # ════════════════════════════════════════════════════════════════
    # MINNESOTA Governor (Tim Walz seeking 3rd term? · DFL primary 8/11)
    # ════════════════════════════════════════════════════════════════
    gov('Tim Walz', 'tim-walz-gov-2026', 'MN',
        'Governor of Minnesota (D incumbent · 2024 VP nominee · 2026 reelection candidate)',
        'D', 'establishment_d', '2026-08-11',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Minnesota (since 2019). 2024 D vice-presidential nominee '
               '(lost with Harris). Former U.S. Rep MN-01. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Tim_Walz']),
    gov('Scott Jensen', 'scott-jensen-gov-2026', 'MN',
        'Governor of Minnesota (2026 R Candidate · 2022 R nominee · MD)',
        'R', 'establishment_r', '2026-08-11',
        notes=('Physician, former MN state senator. 2022 R nominee for MN Governor (lost to '
               'Walz). Reportedly considering 2026 rematch.'),
        sources=['https://ballotpedia.org/Scott_Jensen']),
    gov('Royce White', 'royce-white-gov', 'MN',
        'Governor of Minnesota (2026 R Candidate · 2024 U.S. Senate nominee · former NBA player)',
        'R', 'populist_right', '2026-08-11',
        notes=('Former NBA player, podcaster. 2024 R nominee for U.S. Senate (lost to Klobuchar). '
               'Considering 2026 R primary for MN Governor.'),
        sources=['https://ballotpedia.org/Royce_White']),

    # ════════════════════════════════════════════════════════════════
    # MASSACHUSETTS Governor (Maura Healey seeking 2nd term · D primary 9/8)
    # ════════════════════════════════════════════════════════════════
    gov('Maura Healey', 'maura-healey-gov-2026', 'MA',
        'Governor of Massachusetts (D incumbent · 2026 reelection · former AG)',
        'D', 'progressive_d', '2026-09-08',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Massachusetts (since 2023). Former MA Attorney General '
               '(2015-2023). First openly gay woman elected U.S. governor.'),
        sources=['https://ballotpedia.org/Maura_Healey']),
    gov('Brian Shortsleeve', 'brian-shortsleeve-gov', 'MA',
        'Governor of Massachusetts (2026 R Candidate · former MBTA acting general manager)',
        'R', 'establishment_r', '2026-09-08',
        notes=('Former acting general manager of MBTA under Gov Baker. Marine Corps veteran. '
               'R candidate for MA Governor 2026.'),
        sources=['https://ballotpedia.org/Brian_Shortsleeve']),

    # ════════════════════════════════════════════════════════════════
    # MARYLAND Governor (Wes Moore seeking 2nd term · D primary 6/30)
    # ════════════════════════════════════════════════════════════════
    gov('Wes Moore', 'wes-moore-gov-2026', 'MD',
        'Governor of Maryland (D incumbent · 2026 reelection · 2028 presidential talk)',
        'D', 'establishment_d', '2026-06-30',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Maryland (since 2023). Former Robin Hood Foundation CEO. '
               'Army veteran. Frequently mentioned for 2028 D presidential run.'),
        sources=['https://ballotpedia.org/Wes_Moore']),

    # ════════════════════════════════════════════════════════════════
    # MAINE Governor (Janet Mills term-limited · D primary 6/9)
    # ════════════════════════════════════════════════════════════════
    gov('Paul LePage', 'paul-lepage-gov-2026', 'ME',
        'Governor of Maine (2026 R Candidate · former Gov 2011-2019 · 2022 R nominee)',
        'R', 'maga_conservative_r', '2026-06-09',
        notes=('Former Governor of Maine (2011-2019). 2022 R nominee for Maine Governor (lost '
               'to Mills). Trump-aligned. R candidate 2026.'),
        sources=['https://ballotpedia.org/Paul_LePage']),
    gov('Hannah Pingree', 'hannah-pingree-gov', 'ME',
        'Governor of Maine (2026 D Candidate · former Speaker ME House · daughter of Rep Chellie Pingree)',
        'D', 'establishment_d', '2026-06-09',
        notes=('Former Speaker of the Maine House (2008-2010). Director of ME Office of Policy '
               'Innovation. Daughter of U.S. Rep Chellie Pingree (ME-01). D candidate 2026.'),
        sources=['https://ballotpedia.org/Hannah_Pingree']),
    gov('Troy Jackson', 'troy-jackson-gov', 'ME',
        'Governor of Maine (2026 D Candidate · former ME Senate President · logger)',
        'D', 'establishment_d', '2026-06-09',
        notes=('Former Maine Senate President (2018-2024). Logger from Aroostook County. '
               'D candidate for ME Governor 2026.'),
        sources=['https://ballotpedia.org/Troy_Jackson']),

    # ════════════════════════════════════════════════════════════════
    # CONNECTICUT Governor (Ned Lamont term-limited? seeking 3rd? · D primary 8/11)
    # ════════════════════════════════════════════════════════════════
    gov('Ned Lamont', 'ned-lamont-gov-2026', 'CT',
        'Governor of Connecticut (D incumbent · 2026 reelection · businessman)',
        'D', 'establishment_d', '2026-08-11',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Connecticut (since 2019). Businessman. Reportedly '
               'seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Ned_Lamont']),
    gov('Erin Stewart', 'erin-stewart-gov', 'CT',
        'Governor of Connecticut (2026 R Candidate · mayor of New Britain)',
        'R', 'establishment_r', '2026-08-11',
        notes='Mayor of New Britain, CT (since 2013). R candidate for CT Governor 2026.',
        sources=['https://ballotpedia.org/Erin_Stewart']),

    # ════════════════════════════════════════════════════════════════
    # NEW HAMPSHIRE Governor (Kelly Ayotte R incumbent · seeking 2nd term · 9/8)
    # ════════════════════════════════════════════════════════════════
    gov('Kelly Ayotte', 'kelly-ayotte-gov-2026', 'NH',
        'Governor of New Hampshire (R incumbent · 2026 reelection · former U.S. Senator)',
        'R', 'establishment_r', '2026-09-08',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent Governor of New Hampshire (since 2025). Former U.S. Senator from NH '
               '(2011-2017). Former NH Attorney General. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Kelly_Ayotte']),
    gov('Cinde Warmington', 'cinde-warmington-gov', 'NH',
        'Governor of New Hampshire (2026 D Candidate · NH Executive Councilor)',
        'D', 'establishment_d', '2026-09-08',
        notes=('Sitting NH Executive Councilor (District 2, since 2021). 2024 D primary candidate '
               'for NH Governor (lost to Joyce Craig). D candidate 2026.'),
        sources=['https://ballotpedia.org/Cinde_Warmington']),

    # ════════════════════════════════════════════════════════════════
    # VERMONT Governor (Phil Scott R incumbent — 2-year terms · D primary 8/11)
    # ════════════════════════════════════════════════════════════════
    gov('Phil Scott', 'phil-scott-gov-2026', 'VT',
        'Governor of Vermont (R incumbent · 2026 reelection · 2-year term)',
        'R', 'establishment_r', '2026-08-11',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent Governor of Vermont (since 2017). VT governor terms are 2 years. '
               'Most popular governor in U.S. (Morning Consult). Anti-Trump Republican.'),
        sources=['https://ballotpedia.org/Phil_Scott_(Vermont)']),

    # ════════════════════════════════════════════════════════════════
    # PENNSYLVANIA Governor (Josh Shapiro seeking 2nd term · D primary 5/19 DONE)
    # ════════════════════════════════════════════════════════════════
    gov('Josh Shapiro', 'josh-shapiro-gov-2026', 'PA',
        'Governor of Pennsylvania (D incumbent · 2026 reelection · 2028 presidential talk)',
        'D', 'establishment_d', '2026-05-19',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Pennsylvania (since 2023). Former PA Attorney General. '
               '2024 VP shortlist for Harris. Frequently mentioned for 2028 D presidential run.'),
        sources=['https://ballotpedia.org/Josh_Shapiro']),

    # ════════════════════════════════════════════════════════════════
    # WISCONSIN Governor (Tony Evers seeking 3rd term · D primary 8/11)
    # ════════════════════════════════════════════════════════════════
    gov('Tim Michels', 'tim-michels-gov-2026', 'WI',
        'Governor of Wisconsin (2026 R Candidate · 2022 R nominee · construction CEO)',
        'R', 'maga_conservative_r', '2026-08-11',
        notes=('Construction company CEO (Michels Corp). 2022 R nominee for WI Governor (lost '
               'to Evers). Considering 2026 rematch.'),
        sources=['https://ballotpedia.org/Tim_Michels']),

    # ════════════════════════════════════════════════════════════════
    # NEBRASKA Governor (Jim Pillen R incumbent · seeking 2nd · R primary 5/12)
    # ════════════════════════════════════════════════════════════════
    gov('Jim Pillen', 'jim-pillen-gov-2026', 'NE',
        'Governor of Nebraska (R incumbent · 2026 reelection · hog farmer)',
        'R', 'establishment_r', '2026-05-12',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent Governor of Nebraska (since 2023). Hog farmer, former NU Board of '
               'Regents. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Jim_Pillen']),

    # ════════════════════════════════════════════════════════════════
    # OREGON Governor (Tina Kotek seeking 2nd term · D primary 5/19 DONE)
    # ════════════════════════════════════════════════════════════════
    gov('Tina Kotek', 'tina-kotek-gov-2026', 'OR',
        'Governor of Oregon (D incumbent · 2026 reelection · former OR House Speaker)',
        'D', 'establishment_d', '2026-05-19',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Oregon (since 2023). Former Speaker of Oregon House '
               '(2013-2022). First openly lesbian U.S. governor. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Tina_Kotek']),
    gov('Christine Drazan', 'christine-drazan-gov-2026', 'OR',
        'Governor of Oregon (2026 R Candidate · 2022 R nominee · former OR House Minority Leader)',
        'R', 'establishment_r', '2026-05-19',
        notes=('Former Oregon House Republican Leader. 2022 R nominee for OR Governor (lost '
               'narrowly to Kotek in 3-way race). Likely 2026 R candidate.'),
        sources=['https://ballotpedia.org/Christine_Drazan']),
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
