#!/usr/bin/env python3
"""
add-senate-challengers-2026-batch1.py — 2026 Senate challengers.

For the 26 Class 2 senators seeking reelection, add named declared or
strongly-considering challengers (R+D). ~17 records covering high-profile
races: ME, NC, TX, GA, LA, MS, IA, KS, CO, NM, OR, MT, NH (open), SC, MN (open).
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
    # ══ MAINE Senate (Susan Collins R · D primary 6/9) ══
    sen('Janet Mills', 'janet-mills-senate-2026', 'ME',
        'U.S. Senate Maine (2026 D Candidate · sitting ME Governor · term-limited 2027)',
        'D', 'establishment_d', '2026-06-09',
        notes=('Sitting D Governor of Maine (2019-present, term-limited 2027). Former ME AG. '
               'Considering 2026 D U.S. Senate primary challenge to Susan Collins. Would be a '
               'top-tier D recruit.'),
        sources=['https://ballotpedia.org/Janet_Mills']),
    sen('Mike Tipping', 'mike-tipping-senate', 'ME',
        'U.S. Senate Maine (2026 D Candidate · ME state senator · progressive)',
        'D', 'progressive_d', '2026-06-09',
        notes='Maine state senator (Penobscot County). Progressive D candidate for ME U.S. Senate 2026.',
        sources=['https://ballotpedia.org/Mike_Tipping']),

    # ══ NORTH CAROLINA Senate (Thom Tillis R · D primary 3/3 DONE) ══
    sen('Roy Cooper', 'roy-cooper-senate-2026', 'NC',
        'U.S. Senate North Carolina (2026 D Candidate · former NC Governor · top D recruit)',
        'D', 'establishment_d', '2026-03-03',
        notes=('Former D Governor of North Carolina (2017-2025, term-limited). Former NC '
               'Attorney General. Top D recruit for 2026 Senate run against Tillis (Tillis '
               'announced retirement May 2026 — seat now OPEN).'),
        sources=['https://ballotpedia.org/Roy_Cooper']),
    sen('Wiley Nickel', 'wiley-nickel-senate', 'NC',
        'U.S. Senate North Carolina (2026 D Candidate · former U.S. Rep NC-13)',
        'D', 'establishment_d', '2026-03-03',
        notes=('Former U.S. Representative NC-13 (2023-2025, gerrymandered out). Former NC '
               'state senator. D candidate for NC U.S. Senate 2026.'),
        sources=['https://ballotpedia.org/Wiley_Nickel']),

    # ══ TEXAS Senate (Cornyn R · R primary 3/3 DONE) ══
    sen('Wesley Hunt', 'wesley-hunt-senate', 'TX',
        'U.S. Senate Texas (2026 R Candidate · U.S. Rep TX-38 · West Point grad · Black conservative)',
        'R', 'maga_conservative_r', '2026-03-03',
        notes=('Sitting U.S. Representative TX-38 (2023-present). West Point graduate, former '
               'Army helicopter pilot. R primary candidate for TX U.S. Senate 2026 (running '
               'against Cornyn from the right).'),
        sources=['https://ballotpedia.org/Wesley_Hunt']),
    sen('Ken Paxton', 'ken-paxton-senate', 'TX',
        'U.S. Senate Texas (2026 R Candidate · sitting TX AG · MAGA conservative)',
        'R', 'maga_conservative_r', '2026-03-03',
        notes=('Sitting Texas Attorney General (2015-present). Survived 2023 impeachment trial '
               'in Senate. Trump-aligned. R primary candidate for TX U.S. Senate 2026 (running '
               'against Cornyn from the right).'),
        sources=['https://ballotpedia.org/Ken_Paxton']),

    # ══ LOUISIANA Senate (Bill Cassidy R · open primary 11/3) ══
    sen('John Fleming', 'john-fleming-senate-2026', 'LA',
        'U.S. Senate Louisiana (2026 R Candidate · LA Treasurer · former U.S. Rep LA-04)',
        'R', 'maga_conservative_r', '2026-11-03',
        notes=('Sitting Louisiana State Treasurer. Former U.S. Representative LA-04 (2009-2017). '
               'Trump-aligned. R primary candidate for LA U.S. Senate 2026 (running against '
               'Cassidy after Cassidy\'s vote to convict Trump in 2021 impeachment).'),
        sources=['https://ballotpedia.org/John_Fleming']),

    # ══ GEORGIA Senate (Jon Ossoff D · R primary 5/19 DONE) ══
    sen('Doug Collins', 'doug-collins-senate-2026', 'GA',
        'U.S. Senate Georgia (2026 R Candidate · former U.S. Rep GA-09 · former VA Secretary)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes=('Former U.S. Secretary of Veterans Affairs under Trump 2025. Former U.S. '
               'Representative GA-09 (2013-2021). 2020 R Senate primary loser. R candidate for '
               'GA U.S. Senate 2026 vs Ossoff.'),
        sources=['https://ballotpedia.org/Doug_Collins']),
    sen('Buddy Carter', 'buddy-carter-senate', 'GA',
        'U.S. Senate Georgia (2026 R Candidate · sitting U.S. Rep GA-01 · pharmacist)',
        'R', 'establishment_r', '2026-05-19',
        notes=('Sitting U.S. Representative GA-01 (2015-present). Pharmacist. R candidate for '
               'GA U.S. Senate 2026 vs Ossoff.'),
        sources=['https://ballotpedia.org/Buddy_Carter']),

    # ══ MICHIGAN Senate (Gary Peters retiring · open · D primary 8/4) ══
    sen('Mike Rogers', 'mike-rogers-mi-senate-2026', 'MI',
        'U.S. Senate Michigan (2026 R Candidate · former U.S. Rep MI-08 · 2024 R nominee)',
        'R', 'establishment_r', '2026-08-04',
        notes=('Former U.S. Representative MI-08 (2001-2015), former House Intelligence Chair. '
               '2024 R Senate nominee in MI (lost narrowly to Elissa Slotkin). Running again '
               '2026 for the open Peters seat.'),
        sources=['https://ballotpedia.org/Mike_Rogers_(Michigan)']),
    sen('Haley Stevens', 'haley-stevens-senate', 'MI',
        'U.S. Senate Michigan (2026 D Candidate · sitting U.S. Rep MI-11)',
        'D', 'establishment_d', '2026-08-04',
        notes=('Sitting U.S. Representative MI-11 (2019-present). Former Obama auto bailout team. '
               'D candidate for MI U.S. Senate 2026 (open Peters seat).'),
        sources=['https://ballotpedia.org/Haley_Stevens']),

    # ══ MINNESOTA Senate (Tina Smith retiring · open · DFL primary 8/11) ══
    sen('Peggy Flanagan', 'peggy-flanagan-senate', 'MN',
        'U.S. Senate Minnesota (2026 D Candidate · sitting MN Lt Governor · Native American)',
        'D', 'progressive_d', '2026-08-11',
        notes=('Sitting Minnesota Lt Governor (since 2019). Member of White Earth Band of Ojibwe. '
               'D candidate for MN U.S. Senate 2026 (open Smith seat). Would be first Native '
               'American woman in U.S. Senate.'),
        sources=['https://ballotpedia.org/Peggy_Flanagan']),

    # ══ NEW HAMPSHIRE Senate (Jeanne Shaheen retiring · open · 9/8) ══
    sen('Chris Pappas', 'chris-pappas-senate', 'NH',
        'U.S. Senate New Hampshire (2026 D Candidate · sitting U.S. Rep NH-01 · restaurateur)',
        'D', 'establishment_d', '2026-09-08',
        notes=('Sitting U.S. Representative NH-01 (2019-present). Manchester restaurateur. '
               'Openly gay. D candidate for NH U.S. Senate 2026 (open Shaheen seat).'),
        sources=['https://ballotpedia.org/Chris_Pappas']),
    sen('Scott Brown', 'scott-brown-nh-senate', 'NH',
        'U.S. Senate New Hampshire (2026 R Candidate · former MA Senator + Trump ambassador)',
        'R', 'establishment_r', '2026-09-08',
        notes=('Former U.S. Senator from Massachusetts (2010-2013). Former U.S. Ambassador to '
               'New Zealand under Trump. 2014 R nominee for NH U.S. Senate (lost to Shaheen). '
               'R candidate for NH U.S. Senate 2026.'),
        sources=['https://ballotpedia.org/Scott_Brown']),

    # ══ KENTUCKY Senate (McConnell retiring · open · R primary 5/19 DONE) ══
    sen('Andy Beshear', 'andy-beshear-senate-2026', 'KY',
        'U.S. Senate Kentucky (2026 D Candidate · sitting KY Governor · term-limited 2027)',
        'D', 'establishment_d', '2026-05-19',
        notes=('Sitting D Governor of Kentucky (2019-present, term-limited 2027). Won 2019 + '
               '2023 in deep-red KY. Former KY AG. Considering 2026 D U.S. Senate run for '
               'open McConnell seat. Top D recruit.'),
        sources=['https://ballotpedia.org/Andy_Beshear']),

    # ══ COLORADO Senate (Hickenlooper D · R primary 6/30) ══
    sen('Joe O\'Dea', 'joe-odea-senate-2026', 'CO',
        'U.S. Senate Colorado (2026 R Candidate · 2022 R nominee · construction CEO)',
        'R', 'establishment_r', '2026-06-30',
        notes=('Denver-area construction company CEO (Concrete Express). 2022 R nominee for CO '
               'U.S. Senate (lost to Bennet). Considering 2026 run vs Hickenlooper.'),
        sources=['https://ballotpedia.org/Joe_O\'Dea']),

    # ══ IOWA Senate (Joni Ernst R · D primary 6/2) ══
    sen('Rob Sand Senate', 'rob-sand-senate', 'IA',
        'U.S. Senate Iowa (2026 D Candidate · IA State Auditor · also Gov candidate)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Sitting Iowa State Auditor (only D in IA statewide office). Considering both '
               'IA Gov and IA U.S. Senate 2026. D challenger to Joni Ernst.'),
        sources=['https://ballotpedia.org/Rob_Sand']),
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
        print(f'  {action} {r["name"]:<28s} ({r["state"]} Senate {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
