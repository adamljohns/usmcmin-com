#!/usr/bin/env python3
"""
add-governors-2026-batch4-final.py — Final 2026 governor batch.

Covers AK, AR, CA, HI, ID, IL, NY, RI, WY — the 9 remaining states with
2026 gubernatorial elections not yet ingested with multi-candidate slates.
~18 records.
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
    # ALASKA Governor (Mike Dunleavy term-limited · R primary 8/18)
    # ════════════════════════════════════════════════════════════════
    gov('Nancy Dahlstrom', 'nancy-dahlstrom-gov-2026', 'AK',
        'Governor of Alaska (2026 R Candidate · sitting AK Lt Governor · former state rep)',
        'R', 'establishment_r', '2026-08-18',
        candidacy_status='running_higher_office',
        notes=('Sitting AK Lt Governor (since 2022). Former AK state representative. R '
               'candidate for AK Governor 2026 (Dunleavy term-limited).'),
        sources=['https://ballotpedia.org/Nancy_Dahlstrom']),
    gov('Bill Walker', 'bill-walker-gov-2026', 'AK',
        'Governor of Alaska (2026 I Candidate · former Gov 2014-2018 · independent)',
        'I', 'establishment_r', '2026-08-18',
        notes=('Former AK Governor (2014-2018, Independent). 2022 I gubernatorial nominee '
               '(lost). Considering 2026 comeback bid.'),
        sources=['https://ballotpedia.org/Bill_Walker_(Alaska_politician)']),

    # ════════════════════════════════════════════════════════════════
    # ARKANSAS Governor (Sarah Huckabee Sanders R · seeking 2nd · 5/19 DONE)
    # ════════════════════════════════════════════════════════════════
    gov('Sarah Huckabee Sanders', 'sarah-huckabee-sanders-gov-2026', 'AR',
        'Governor of Arkansas (R incumbent · 2026 reelection · former Trump press sec)',
        'R', 'maga_conservative_r', '2026-05-19',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent Governor of Arkansas (since 2023). Former Trump White House Press '
               'Secretary (2017-2019). Daughter of former Gov Mike Huckabee. Seeking 2026 '
               'reelection.'),
        sources=['https://ballotpedia.org/Sarah_Huckabee_Sanders']),
    gov('Chris Jones AR', 'chris-jones-ar-gov-2026', 'AR',
        'Governor of Arkansas (2026 D Candidate · 2022 D nominee · physicist + minister)',
        'D', 'establishment_d', '2026-05-19',
        notes=('PhD physicist (MIT), ordained minister. 2022 D nominee for AR Governor (lost '
               'to Sanders). Considering 2026 rematch.'),
        sources=['https://ballotpedia.org/Chris_Jones_(Arkansas_politician)']),

    # ════════════════════════════════════════════════════════════════
    # CALIFORNIA Governor (Gavin Newsom term-limited · top-2 6/2)
    # ════════════════════════════════════════════════════════════════
    gov('Kamala Harris', 'kamala-harris-gov', 'CA',
        'Governor of California (2026 D Candidate · former VP + presidential nominee 2024)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Former U.S. Vice President (2021-2025). 2024 D presidential nominee (lost to '
               'Trump). Former U.S. Senator from CA (2017-2021). Former CA Attorney General. '
               'Considering 2026 CA gubernatorial bid.'),
        sources=['https://ballotpedia.org/Kamala_Harris']),
    gov('Katie Porter', 'katie-porter-gov', 'CA',
        'Governor of California (2026 D Candidate · former U.S. Rep CA-47 · law professor)',
        'D', 'progressive_d', '2026-06-02',
        notes=('Former U.S. Representative CA-47 (2019-2025). UC Irvine law professor. 2024 D '
               'primary candidate for U.S. Senate (lost to Schiff). Announced 2026 D candidate '
               'for CA Governor.'),
        sources=['https://ballotpedia.org/Katie_Porter']),
    gov('Steve Hilton', 'steve-hilton-gov', 'CA',
        'Governor of California (2026 R Candidate · former Fox News host · British-American)',
        'R', 'maga_conservative_r', '2026-06-02',
        notes=('British-American political commentator. Former host of Fox News\' "The Next '
               'Revolution" (2017-2023). Former senior adviser to UK PM David Cameron. R '
               'candidate for CA Governor 2026.'),
        sources=['https://ballotpedia.org/Steve_Hilton']),
    gov('Chad Bianco', 'chad-bianco-gov', 'CA',
        'Governor of California (2026 R Candidate · Riverside Co Sheriff · MAGA conservative)',
        'R', 'maga_conservative_r', '2026-06-02',
        notes=('Riverside County Sheriff. Conservative, anti-mandate during COVID. R candidate '
               'for CA Governor 2026.'),
        sources=['https://ballotpedia.org/Chad_Bianco']),

    # ════════════════════════════════════════════════════════════════
    # HAWAII Governor (Josh Green seeking 2nd · D primary 8/8)
    # ════════════════════════════════════════════════════════════════
    gov('Josh Green', 'josh-green-gov-2026', 'HI',
        'Governor of Hawaii (D incumbent · 2026 reelection · ER physician)',
        'D', 'establishment_d', '2026-08-08',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Hawaii (since 2022). ER physician. Former HI Lt '
               'Governor. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Josh_Green_(Hawaii_politician)']),
    gov('James Aiona', 'james-aiona-gov-2026', 'HI',
        'Governor of Hawaii (2026 R Candidate · former HI Lt Gov · perennial R nominee)',
        'R', 'establishment_r', '2026-08-08',
        notes=('Former HI Lt Governor (2002-2010). 2010 + 2022 R nominee for HI Governor (lost '
               'both). Considering 2026 R candidacy.'),
        sources=['https://ballotpedia.org/James_Aiona']),

    # ════════════════════════════════════════════════════════════════
    # IDAHO Governor (Brad Little seeking 3rd? · R primary 5/19 DONE)
    # ════════════════════════════════════════════════════════════════
    gov('Brad Little', 'brad-little-gov-2026', 'ID',
        'Governor of Idaho (R incumbent · 2026 reelection · 3rd term bid · rancher)',
        'R', 'establishment_r', '2026-05-19',
        candidacy_status='incumbent_seeking_reelection',
        notes=('R incumbent Governor of Idaho (since 2019). Sheep + cattle rancher. Seeking '
               '2026 reelection (3rd term).'),
        sources=['https://ballotpedia.org/Brad_Little']),
    gov('Janice McGeachin', 'janice-mcgeachin-gov-2026', 'ID',
        'Governor of Idaho (2026 R Candidate · former ID Lt Gov · 2022 R primary challenger)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes=('Former ID Lt Governor (2019-2023). 2022 R primary challenger to Brad Little '
               '(lost). Trump-aligned populist. May run again 2026.'),
        sources=['https://ballotpedia.org/Janice_McGeachin']),

    # ════════════════════════════════════════════════════════════════
    # ILLINOIS Governor (JB Pritzker term-limited? seeking 3rd? · D primary 3/17 DONE)
    # ════════════════════════════════════════════════════════════════
    gov('JB Pritzker', 'jb-pritzker-gov-2026', 'IL',
        'Governor of Illinois (D incumbent · 2026 reelection · 3rd term bid · billionaire)',
        'D', 'establishment_d', '2026-03-17',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Illinois (since 2019). Hyatt Hotels heir, billionaire. '
               'Frequently mentioned for 2028 D presidential run. Seeking 2026 reelection (3rd term).'),
        sources=['https://ballotpedia.org/J._B._Pritzker']),
    gov('Darren Bailey', 'darren-bailey-gov-2026', 'IL',
        'Governor of Illinois (2026 R Candidate · 2022 R nominee · farmer + state senator)',
        'R', 'maga_conservative_r', '2026-03-17',
        notes=('Farmer, former IL state senator. 2022 R nominee for IL Governor (lost decisively '
               'to Pritzker). 2024 R primary candidate for IL-12 (lost). May run again 2026.'),
        sources=['https://ballotpedia.org/Darren_Bailey']),

    # ════════════════════════════════════════════════════════════════
    # NEW YORK Governor (Kathy Hochul seeking 2nd full term · D primary 6/23)
    # ════════════════════════════════════════════════════════════════
    gov('Kathy Hochul', 'kathy-hochul-gov-2026', 'NY',
        'Governor of New York (D incumbent · 2026 reelection · former Lt Gov)',
        'D', 'establishment_d', '2026-06-23',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of New York (since 2021, won 2022). Former NY Lt Governor. '
               'Former U.S. Rep NY-26. First woman to serve as NY Governor. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Kathy_Hochul']),
    gov('Mike Lawler', 'mike-lawler-gov', 'NY',
        'Governor of New York (2026 R Candidate · sitting U.S. Rep NY-17 · former NY state assemblyman)',
        'R', 'establishment_r', '2026-06-23',
        candidacy_status='running_higher_office',
        notes=('Sitting U.S. Representative NY-17 (2023-present). Former NY state assemblyman. '
               'Considering 2026 R candidacy for NY Governor.'),
        sources=['https://ballotpedia.org/Mike_Lawler']),
    gov('Elise Stefanik', 'elise-stefanik-gov', 'NY',
        'Governor of New York (2026 R Candidate · sitting U.S. Rep NY-21 · former House Conf Chair)',
        'R', 'maga_conservative_r', '2026-06-23',
        candidacy_status='running_higher_office',
        notes=('Sitting U.S. Representative NY-21 (2015-present). Former House Republican '
               'Conference Chair. 2024 Trump UN Ambassador nominee (withdrew). Considering '
               '2026 R candidacy for NY Governor.'),
        sources=['https://ballotpedia.org/Elise_Stefanik']),

    # ════════════════════════════════════════════════════════════════
    # RHODE ISLAND Governor (Daniel McKee seeking 2nd full · D primary 9/8)
    # ════════════════════════════════════════════════════════════════
    gov('Daniel McKee', 'daniel-mckee-gov-2026', 'RI',
        'Governor of Rhode Island (D incumbent · 2026 reelection · former Lt Gov)',
        'D', 'establishment_d', '2026-09-08',
        candidacy_status='incumbent_seeking_reelection',
        notes=('D incumbent Governor of Rhode Island (since 2021, won 2022). Former RI Lt '
               'Governor. Former mayor of Cumberland. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Daniel_McKee']),
    gov('Helena Foulkes', 'helena-foulkes-gov', 'RI',
        'Governor of Rhode Island (2026 D Candidate · former CVS exec · 2022 D primary candidate)',
        'D', 'establishment_d', '2026-09-08',
        notes=('Former CVS Health President of Pharmacy. Former Hudson\'s Bay Company CEO. '
               '2022 D primary candidate for RI Governor (lost to McKee). D candidate 2026.'),
        sources=['https://ballotpedia.org/Helena_Foulkes']),

    # ════════════════════════════════════════════════════════════════
    # WYOMING Governor (Mark Gordon term-limited · R primary 8/18)
    # ════════════════════════════════════════════════════════════════
    gov('Harriet Hageman', 'harriet-hageman-gov', 'WY',
        'Governor of Wyoming (2026 R Candidate · sitting U.S. Rep WY-AL · ousted Liz Cheney 2022)',
        'R', 'maga_conservative_r', '2026-08-18',
        candidacy_status='running_higher_office',
        notes=('Sitting U.S. Representative WY-AL (2023-present). Defeated Liz Cheney in 2022 '
               'R primary. Trump-endorsed. Considering 2026 R candidacy for WY Governor '
               '(Gordon term-limited).'),
        sources=['https://ballotpedia.org/Harriet_Hageman']),
    gov('Chuck Gray', 'chuck-gray-gov', 'WY',
        'Governor of Wyoming (2026 R Candidate · sitting WY Secretary of State · election integrity activist)',
        'R', 'maga_conservative_r', '2026-08-18',
        notes=('Sitting WY Secretary of State (since 2023). Election integrity activist. '
               'Former WY state representative. R candidate for WY Governor 2026.'),
        sources=['https://ballotpedia.org/Chuck_Gray']),
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
        print(f'  {action} {r["name"]:<30s} ({r["state"]} Gov {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
