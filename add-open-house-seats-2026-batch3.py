#!/usr/bin/env python3
"""
add-open-house-seats-2026-batch3.py — Pass 2 House primary work, batch 3.

Covers ~17 more open House seats across FL, GA, IL, MD, MO, NV, NY, PA, TN,
UT, WA, CA-01/CA-14/CA-26 (special elections + Brownley retirement).

~70 candidate records added, mix of evidence-curated and placeholders.
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
    'progressive_d': {
        'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
        'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
        'economic_stewardship':[F,F,F,N,T],'election_integrity':[F,F,F,F,F],
        'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
        'foreign_policy_restraint':[N,T,N,N,N],'industry_capture':[N,F,T,N,T],
    },
    'establishment_d': {
        'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
        'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
        'economic_stewardship':[F,F,F,F,F],'election_integrity':[F,F,F,F,F],
        'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
        'foreign_policy_restraint':[F,F,F,F,F],'industry_capture':[F,F,F,F,F],
    },
    'populist_right': {
        'sanctity_of_life':[T,T,T,T,T],'biblical_marriage':[T,T,T,T,T],
        'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,N],
        'economic_stewardship':[T,N,F,N,T],'election_integrity':[N,T,T,T,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
        'foreign_policy_restraint':[T,T,T,F,T],'industry_capture':[T,T,T,N,T],
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
        sources=None, profile_extra=None, candidacy_status='primary_candidate', cn=''):
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
            'confidence_note': cn or (f'2026-05-20 — ingested for 2026 open House seat ({state}-{district}). Archetype: {archetype}.' if archetype else '2026-05-20 — placeholder.'),
            **(profile_extra or {}),
        },
    }

def ph(name, slug, state, district, party, primary_date, ctx=''):
    label = {'R':'R','D':'D','I':'I','NPP':'No Party Pref'}[party]
    office = f'U.S. Representative {state}-{district:02d} (2026 {label} Candidate · open seat{(" · "+ctx) if ctx else ""})'
    return rec(name, slug, state, district, office, party, None, primary_date,
               f'{name} — on the 2026 {state}-{district:02d} primary ballot. Placeholder.')


RECORDS = [
    # ════ FL-20 (Cherfilus-McCormick resigned 4/21/26) ════
    ph('Mark Douglas', 'mark-douglas-fl-20', 'FL', 20, 'D', '2026-08-18', 'Cherfilus-McCormick vacancy'),
    ph('Dale Holness', 'dale-holness', 'FL', 20, 'D', '2026-08-18', 'Cherfilus-McCormick vacancy'),
    ph('Elijah Manley', 'elijah-manley', 'FL', 20, 'D', '2026-08-18', 'Cherfilus-McCormick vacancy'),

    # ════ GA-01 (Buddy Carter → Senate); GA primary 5/19/26 ════
    rec('Patrick Farrell', 'patrick-farrell', 'GA', 1,
        'U.S. Representative GA-01 (2026 R Candidate · Carter-seat open · Chatham County Commissioner)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes='Chatham County (Savannah) commissioner. R primary candidate for GA-01 to succeed Buddy Carter.',
        sources=['https://ballotpedia.org/Georgia%27s_1st_Congressional_District_election,_2026']),
    rec('Jim Kingston', 'jim-kingston', 'GA', 1,
        'U.S. Representative GA-01 (2026 R Candidate · Carter-seat open · insurance / Kingston-family)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes='Insurance salesman. Son of former U.S. Rep. Jack Kingston (GA-01 1993-2015). R primary candidate.',
        sources=['https://ballotpedia.org/Georgia%27s_1st_Congressional_District_election,_2026']),
    rec('Kandiss Taylor', 'kandiss-taylor', 'GA', 1,
        'U.S. Representative GA-01 (2026 R Candidate · Carter-seat open · GA GOP district chair)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes='Georgia Republican Party District 1 chair. 2022 R primary candidate for Governor (lost). R primary candidate for GA-01.',
        sources=['https://ballotpedia.org/Kandiss_Taylor']),
    rec('Vernon Jones', 'vernon-jones', 'GA', 1,
        'U.S. Representative GA-01 (2026 R Candidate · Carter-seat open · former DeKalb CEO)',
        'R', 'populist_right', '2026-05-19',
        notes=('Former DeKalb County CEO. Switched from D to R in 2022. 2022 R primary candidate '
               'for GA Governor (lost). Populist Trump-aligned candidate.'),
        sources=['https://ballotpedia.org/Vernon_Jones']),
    ph('Brian Montgomery', 'brian-montgomery-ga-01', 'GA', 1, 'R', '2026-05-19', 'Carter seat (ret. LtCol)'),
    ph('Eugene Yu', 'eugene-yu', 'GA', 1, 'R', '2026-05-19', 'Carter seat'),
    ph('James Burchett', 'james-burchett', 'GA', 1, 'R', '2026-05-19', 'Carter seat (state rep)'),
    ph('Jesse Petrea', 'jesse-petrea', 'GA', 1, 'R', '2026-05-19', 'Carter seat (state rep)'),

    # ════ GA-10 (Mike Collins → Senate); GA 5/19 ════
    rec('Houston Gaines', 'houston-gaines', 'GA', 10,
        'U.S. Representative GA-10 (2026 R Candidate · Collins-seat open · GA state rep)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes='GA state representative. Top R seeking to succeed Mike Collins in GA-10.',
        sources=['https://ballotpedia.org/Houston_Gaines']),

    # ════ GA-11 (Loudermilk retiring); GA 5/19 ════
    rec('Rob Adkerson', 'rob-adkerson', 'GA', 11,
        'U.S. Representative GA-11 (2026 R Candidate · Loudermilk-seat open · Loudermilk-endorsed staffer)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes='Loudermilk-endorsed staffer. R primary candidate for GA-11.',
        sources=['https://ballotpedia.org/Rob_Adkerson']),
    rec('John Cowan', 'john-cowan-ga-11', 'GA', 11,
        'U.S. Representative GA-11 (2026 R Candidate · Loudermilk-seat open · neurologist)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes='Neurologist. Prior R primary candidate. R primary candidate for GA-11.',
        sources=['https://ballotpedia.org/John_Cowan_(Georgia)']),
    rec('Tricia Pridemore', 'tricia-pridemore', 'GA', 11,
        'U.S. Representative GA-11 (2026 R Candidate · Loudermilk-seat open · GA PSC member)',
        'R', 'maga_conservative_r', '2026-05-19',
        notes='Georgia Public Service Commissioner. R primary candidate for GA-11.',
        sources=['https://ballotpedia.org/Tricia_Pridemore']),

    # ════ GA-13 (David Scott died 4/22/26); GA 5/19 ════
    rec('Jasmine Clark', 'jasmine-clark-ga-13', 'GA', 13,
        'U.S. Representative GA-13 (2026 D Candidate · Scott-seat vacant · GA state rep)',
        'D', 'progressive_d', '2026-05-19',
        notes=('GA state representative. Top D fundraiser to succeed the late David Scott (D, '
               'died Apr 22 2026). Majority-Black district in southern + eastern Atlanta suburbs.'),
        sources=['https://ballotpedia.org/Jasmine_Clark']),
    rec('Everton Blair', 'everton-blair', 'GA', 13,
        'U.S. Representative GA-13 (2026 D Candidate · Scott-seat vacant · Gwinnett school board chair)',
        'D', 'progressive_d', '2026-05-19',
        notes='Gwinnett County school board chair. D primary candidate for the GA-13 vacancy.',
        sources=['https://ballotpedia.org/Everton_Blair']),

    # ════ IL-04 (Jesus Garcia retiring); primary 3/17 DONE ════
    rec('Patty Garcia', 'patty-garcia-il-04', 'IL', 4,
        'U.S. Representative IL-04 (2026 D Nominee · Garcia-seat open · former Chief of Staff to Garcia)',
        'D', 'progressive_d', '2026-03-17',
        candidacy_status='general_candidate',
        notes=('Chief of Staff to retiring Rep. Chuy Garcia. No relation to Chuy. Won 2026 D '
               'primary essentially unopposed after Chuy withdrew post-deadline. Heavily D district.'),
        sources=['https://ballotpedia.org/Patty_Garcia'],
        profile_extra={'next_election_type': 'general', 'next_election_date': '2026-11-03'}),

    # ════ IL-07 (Danny Davis retiring); primary 3/17 DONE ════
    rec('La Shawn Ford', 'la-shawn-ford', 'IL', 7,
        'U.S. Representative IL-07 (2026 D Nominee · Davis-seat open · IL state rep · Davis-endorsed)',
        'D', 'progressive_d', '2026-03-17',
        candidacy_status='general_candidate',
        notes=('IL state representative. Won 2026 D primary with 26.8% in 13-candidate field. '
               'Endorsed by retiring Rep. Danny Davis. Chicago West Side district.'),
        sources=['https://ballotpedia.org/La_Shawn_Ford'],
        profile_extra={'next_election_type': 'general', 'next_election_date': '2026-11-03'}),

    # ════ IL-09 (Schakowsky retiring); primary 3/17 DONE ════
    rec('Daniel Biss', 'daniel-biss', 'IL', 9,
        'U.S. Representative IL-09 (2026 D Nominee · Schakowsky-seat open · Evanston Mayor)',
        'D', 'progressive_d', '2026-03-17',
        candidacy_status='general_candidate',
        notes=('Mayor of Evanston, IL. Won 2026 D primary in 20-candidate field. Former IL state '
               'senator. 2018 D gubernatorial primary candidate.'),
        sources=['https://ballotpedia.org/Daniel_Biss'],
        profile_extra={'next_election_type': 'general', 'next_election_date': '2026-11-03',
                       'background': 'Mayor of Evanston. Former IL state senator. PhD in Math (UChicago).'}),
    rec('Kat Abughazaleh', 'kat-abughazaleh', 'IL', 9,
        'U.S. Representative IL-09 (2026 D Candidate · Schakowsky-seat open · social media activist · lost primary)',
        'D', 'progressive_d', '2026-03-17',
        candidacy_status='lost_primary',
        notes='Social media influencer + Media Matters alum. Close 2nd in IL-09 D primary to Daniel Biss.',
        sources=['https://ballotpedia.org/Kat_Abughazaleh']),
    rec('Laura Fine', 'laura-fine', 'IL', 9,
        'U.S. Representative IL-09 (2026 D Candidate · Schakowsky-seat open · IL state senator · lost primary)',
        'D', 'establishment_d', '2026-03-17',
        candidacy_status='lost_primary',
        notes='IL state senator. Top-tier D primary candidate in IL-09. Lost to Daniel Biss.',
        sources=['https://ballotpedia.org/Laura_Fine']),

    # ════ NY-07 (Velazquez retiring; primary 6/23) ════
    rec('Antonio Reynoso', 'antonio-reynoso', 'NY', 7,
        'U.S. Representative NY-07 (2026 D Candidate · Velazquez-seat open · Brooklyn BP · Velazquez-endorsed)',
        'D', 'progressive_d', '2026-06-23',
        notes=('Brooklyn Borough President. Endorsed by retiring Rep. Velazquez + Rep. Jerry Nadler + '
               'NY AG Tish James + Working Families Party. Not a NYC-DSA member.'),
        sources=['https://ballotpedia.org/Antonio_Reynoso']),
    rec('Claire Valdez', 'claire-valdez', 'NY', 7,
        'U.S. Representative NY-07 (2026 D Candidate · Velazquez-seat open · DSA-endorsed)',
        'D', 'progressive_d', '2026-06-23',
        notes='NYC-DSA member. Endorsed by Mayor Zohran Mamdani. D primary candidate for NY-07.',
        sources=['https://ballotpedia.org/Claire_Valdez']),
    rec('Julie Won', 'julie-won', 'NY', 7,
        'U.S. Representative NY-07 (2026 D Candidate · Velazquez-seat open · NYC Council District 26)',
        'D', 'progressive_d', '2026-06-23',
        notes=('NYC Councilmember (District 26). First woman + first immigrant to represent the '
               'district. South Korean immigrant. D primary candidate for NY-07.'),
        sources=['https://ballotpedia.org/Julie_Won']),
    ph('Vichal Kumar', 'vichal-kumar', 'NY', 7, 'D', '2026-06-23', 'Velazquez seat'),

    # ════ CA-01 (LaMalfa died 1/6/26); SPECIAL ELECTION 6/2 ════
    rec('James Gallagher', 'james-gallagher-ca-01', 'CA', 1,
        'U.S. Representative CA-01 (2026 R Candidate · LaMalfa-vacancy · former CA Assembly Minority Leader · Trump-endorsed)',
        'R', 'maga_conservative_r', '2026-06-02',
        notes=('Former Minority Leader of California State Assembly (2022-2025). Endorsed by Trump, '
               'Speaker Mike Johnson, and Jill LaMalfa (widow of late Rep. Doug LaMalfa). Special '
               'election June 2 to fill LaMalfa\'s seat (he died in office Jan 6 2026).'),
        sources=['https://ballotpedia.org/James_Gallagher',
                 'https://en.wikipedia.org/wiki/2026_California%27s_1st_congressional_district_special_election']),
    rec('Audrey Denney', 'audrey-denney', 'CA', 1,
        'U.S. Representative CA-01 (2026 D Candidate · LaMalfa-vacancy · 2018+2020 D nominee)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Nonprofit consultant + food security activist. D nominee against LaMalfa in 2018 + 2020 '
               '(lost both). D candidate for special election to fill his vacancy.'),
        sources=['https://ballotpedia.org/Audrey_Denney']),
    rec('Mike McGuire', 'mike-mcguire-ca-01', 'CA', 1,
        'U.S. Representative CA-01 (2026 D Candidate · LaMalfa-vacancy · former CA Senate pres. pro tem)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Former President pro tempore of the California State Senate (2024-2025). D candidate '
               'for special election to fill the LaMalfa vacancy in CA-01.'),
        sources=['https://ballotpedia.org/Mike_McGuire']),

    # ════ CA-14 (Swalwell resigned 4/14/26 amid sexual assault allegations); SPECIAL 6/16 ════
    rec('Victor Aguilar Jr.', 'victor-aguilar-jr', 'CA', 14,
        'U.S. Representative CA-14 (2026 D Candidate · Swalwell-vacancy · San Leandro Councilor)',
        'D', 'establishment_d', '2026-06-16',
        notes=('San Leandro city councilmember. D candidate for CA-14 special election. '
               'Swalwell resigned April 14 2026 after suspending his Governor bid following '
               'sexual assault allegations from multiple women.'),
        sources=['https://ballotpedia.org/Victor_Aguilar_Jr.']),
    rec('Melissa Hernandez', 'melissa-hernandez-ca-14', 'CA', 14,
        'U.S. Representative CA-14 (2026 D Candidate · Swalwell-vacancy · BART board president)',
        'D', 'establishment_d', '2026-06-16',
        notes='Bay Area Rapid Transit board president. Former mayor of Dublin, CA.',
        sources=['https://ballotpedia.org/Melissa_Hernandez']),

    # ════ CA-26 (Brownley retiring; jungle primary 6/2) ════
    rec('Monique Limón', 'monique-limon-ca-26', 'CA', 26,
        'U.S. Representative CA-26 (2026 D Candidate · Brownley-seat open · CA Senate pres. pro tem)',
        'D', 'establishment_d', '2026-06-02',
        notes=('President pro tempore of the California State Senate. D candidate for the open CA-26 '
               'seat after Julia Brownley retired.'),
        sources=['https://ballotpedia.org/Monique_Lim%C3%B3n']),
    ph('Chris Espinosa', 'chris-espinosa', 'CA', 26, 'D', '2026-06-02', 'Brownley seat (ex-Grijalva staffer)'),
    ph('Trisha Paytas', 'trisha-paytas', 'CA', 26, 'R', '2026-06-02', 'Brownley seat (influencer)'),

    # ════ MD-05 (Hoyer retiring; primary 6/23) ════
    rec('Adrian Boafo', 'adrian-boafo', 'MD', 5,
        'U.S. Representative MD-05 (2026 D Candidate · Hoyer-seat open · MD state delegate · Hoyer-endorsed)',
        'D', 'establishment_d', '2026-06-23',
        notes=('MD state delegate. Former campaign manager for Hoyer. Endorsed by Hoyer to '
               'succeed him in MD-05.'),
        sources=['https://ballotpedia.org/Adrian_Boafo']),
    rec('Harry Dunn', 'harry-dunn-md-05', 'MD', 5,
        'U.S. Representative MD-05 (2026 D Candidate · Hoyer-seat open · former US Capitol Police)',
        'D', 'establishment_d', '2026-06-23',
        notes=('Former U.S. Capitol Police officer who defended the Capitol on January 6, 2021. '
               'D candidate for the open Hoyer seat.'),
        sources=['https://ballotpedia.org/Harry_Dunn']),
    rec('Wala Blegay', 'wala-blegay', 'MD', 5,
        'U.S. Representative MD-05 (2026 D Candidate · Hoyer-seat open · Prince George\'s Council)',
        'D', 'establishment_d', '2026-06-23',
        notes='Prince George\'s County Council member. D primary candidate for MD-05.',
        sources=['https://ballotpedia.org/Wala_Blegay']),
    ph('Rushern Baker', 'rushern-baker', 'MD', 5, 'D', '2026-06-23', 'Hoyer seat (former PG Co Exec)'),
    ph('Arthur Ellis', 'arthur-ellis', 'MD', 5, 'D', '2026-06-23', 'Hoyer seat (state sen)'),

    # ════ MO-06 (Sam Graves retiring; primary 8/4) ════
    ph('Jim Ingram', 'jim-ingram-mo-06', 'MO', 6, 'R', '2026-08-04', 'Graves seat'),
    ph('Gena Ross', 'gena-ross', 'MO', 6, 'R', '2026-08-04', 'Graves seat'),
    ph('Matthew Levine', 'matthew-levine-mo-06', 'MO', 6, 'D', '2026-08-04', 'Graves seat'),
    ph('Josh Smead', 'josh-smead', 'MO', 6, 'D', '2026-08-04', 'Graves seat'),

    # ════ UT-04 (Owens retiring; primary 6/23) ════
    ph('Ty Jensen', 'ty-jensen', 'UT', 4, 'R', '2026-06-23', 'Owens seat'),
    ph('Jonny Larsen', 'jonny-larsen', 'UT', 4, 'D', '2026-06-23', 'Owens seat'),

    # ════ NV-02 (Amodei retiring; primary 6/9) ════
    rec('James Settelmeyer', 'james-settelmeyer', 'NV', 2,
        'U.S. Representative NV-02 (2026 R Candidate · Amodei-seat open · former NV state sen · Amodei-endorsed)',
        'R', 'maga_conservative_r', '2026-06-09',
        notes=('Former Nevada state senator. Endorsed by retiring Rep. Mark Amodei to succeed him.'),
        sources=['https://ballotpedia.org/James_Settelmeyer']),
    ph('Jesse Watts', 'jesse-watts', 'NV', 2, 'R', '2026-06-09', 'Amodei seat (former Eureka Co Sheriff)'),

    # ════ WA-04 (Newhouse retiring; top-two primary 8/4) ════
    ph('Jerrod Sessler', 'jerrod-sessler', 'WA', 4, 'R', '2026-08-04', 'Newhouse seat'),
    ph('Amanda McKinney', 'amanda-mckinney', 'WA', 4, 'R', '2026-08-04', 'Newhouse seat'),
    ph('Wesley Meier', 'wesley-meier', 'WA', 4, 'D', '2026-08-04', 'Newhouse seat'),
    ph('John Duresky', 'john-duresky', 'WA', 4, 'D', '2026-08-04', 'Newhouse seat'),

    # ════ TN-09 (Cohen withdrew due to redistricting; primary 8/6) ════
    rec('Justin Pearson', 'justin-pearson-tn-09', 'TN', 9,
        'U.S. Representative TN-09 (2026 D Candidate · Cohen-seat open · TN state rep · Tennessee Three)',
        'D', 'progressive_d', '2026-08-06',
        notes=('TN state representative. Part of the "Tennessee Three" expelled and reinstated in 2023. '
               'Memphis-area progressive D candidate for the open TN-09 seat.'),
        sources=['https://ballotpedia.org/Justin_Pearson']),
    ph('Charlotte Bergmann', 'charlotte-bergmann', 'TN', 9, 'R', '2026-08-06', 'Cohen seat'),
    ph('James New', 'james-new-tn-09', 'TN', 9, 'R', '2026-08-06', 'Cohen seat'),

    # ════ PA-03 (Dwight Evans retiring; primary 5/19 TODAY) ════
    rec('Sharif Street', 'sharif-street', 'PA', 3,
        'U.S. Representative PA-03 (2026 D Candidate · Evans-seat open · PA state sen + former PA Dem Party chair)',
        'D', 'progressive_d', '2026-05-19',
        notes=('PA state senator (District 3) + former chair of the Pennsylvania Democratic Party. '
               'D primary candidate for the open Evans seat in Philadelphia.'),
        sources=['https://ballotpedia.org/Sharif_Street']),
    rec('Chris Rabb', 'chris-rabb', 'PA', 3,
        'U.S. Representative PA-03 (2026 D Candidate · Evans-seat open · PA state rep)',
        'D', 'progressive_d', '2026-05-19',
        notes='PA state representative (District 200). D primary candidate for PA-03.',
        sources=['https://ballotpedia.org/Chris_Rabb']),
    rec('Ala Stanford', 'ala-stanford', 'PA', 3,
        'U.S. Representative PA-03 (2026 D Candidate · Evans-seat open · ex-HHS regional director)',
        'D', 'establishment_d', '2026-05-19',
        notes='Former mid-Atlantic regional director, U.S. Department of Health and Human Services. D candidate.',
        sources=['https://ballotpedia.org/Ala_Stanford']),
    rec('Morgan Cephas', 'morgan-cephas', 'PA', 3,
        'U.S. Representative PA-03 (2026 D Candidate · Evans-seat open · PA state rep)',
        'D', 'progressive_d', '2026-05-19',
        notes='PA state representative (District 192). D candidate.',
        sources=['https://ballotpedia.org/Morgan_Cephas']),
    ph('Isaiah T. Martin III', 'isaiah-t-martin-iii', 'PA', 3, 'D', '2026-05-19', 'Evans seat'),
    ph('NaDerah Griffin', 'naderah-griffin', 'PA', 3, 'D', '2026-05-19', 'Evans seat'),
    ph('Pablo McConnie-Saad', 'pablo-mcconnie-saad', 'PA', 3, 'D', '2026-05-19', 'Evans seat'),
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
    by_district = {}
    inserts = replacements = 0
    for r in RECORDS:
        action = upsert(cands, r)
        if action == 'INSERTED':
            inserts += 1
        else:
            replacements += 1
        d = f'{r["state"]}-{r["district"]:02d}'
        by_district.setdefault(d, []).append(r['name'])
    for d, names in sorted(by_district.items()):
        print(f'  {d}: {len(names)} — {", ".join(names[:2])}{"..." if len(names) > 2 else ""}')
    print(f'\n  INSERTS: {inserts} · REPLACEMENTS: {replacements}')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
