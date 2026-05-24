#!/usr/bin/env python3
"""
add-major-city-mayors-2026.py — Major U.S. city mayoral coverage.

Adds sitting mayors of top U.S. cities + recent winners (2025 cycle) +
declared 2026 candidates. ~30 records covering NYC, Boston, Philly, LA,
Chicago, Houston, Dallas, Atlanta, Detroit, Seattle, Portland, Denver,
Minneapolis, DC, Phoenix, Vegas, Miami, SF, Oakland, San Antonio, Austin,
Nashville, Memphis, Charlotte, Cleveland, Pittsburgh, OKC, Tampa, Vegas.
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


def mayor(name, slug, state, city, party, archetype=None, status='active',
          candidacy_status='incumbent_seeking_reelection', next_election=2026,
          next_election_date='', notes='', sources=None, profile_extra=None,
          office_suffix=''):
    """Build a city mayor record."""
    office_text = f'Mayor of {city}{office_suffix}'
    return {
        'name': name, 'slug': slug, 'state': state,
        'office': office_text, 'jurisdiction': f'City of {city}',
        'party': party, 'level': 'local', 'district': None,
        'id': f'{slug}-{state.lower()}',
        'status': status, 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '', 'sources': sources or [f'https://ballotpedia.org/{city.replace(" ","_")}_mayoral_election'],
        'notes': notes, 'footnotes': [], 'answer_footnotes': {},
        'scores': scores_from(archetype) if archetype else empty_scores(),
        'profile': {
            'next_election': next_election, 'next_election_type': 'primary' if next_election >= 2026 else 'general',
            'seat_up_next': next_election == 2026, 'next_election_date': next_election_date,
            'confidence': 'archetype_curated' if archetype else 'low_evidence',
            'confidence_note': f'2026-05-20 — Mayor of {city}. Archetype: {archetype}.' if archetype else f'2026-05-20 — Mayor of {city} placeholder.',
            **(profile_extra or {}),
        },
    }


RECORDS = [
    # ════════════════════════════════════════════════════════════════
    # NEW YORK CITY (Nov 2025 - Zohran Mamdani WON · D primary 6/24/2025)
    # ════════════════════════════════════════════════════════════════
    mayor('Zohran Mamdani', 'zohran-mamdani', 'NY', 'New York City',
        'D', 'progressive_d', candidacy_status='won', next_election=2029,
        notes=('D Mayor of New York City (sworn Jan 2026). Former NY state assemblyman. Democratic '
               'Socialist. Won 2025 D primary upset against Andrew Cuomo + Eric Adams. Mayor of '
               'largest U.S. city. Next election 2029.'),
        sources=['https://ballotpedia.org/Zohran_Mamdani']),
    mayor('Eric Adams', 'eric-adams-mayor', 'NY', 'New York City',
        'D', 'establishment_d', status='former', candidacy_status='lost',
        notes=('Former D Mayor of New York City (2022-2026). Former NYPD captain. Lost 2025 D '
               'primary to Mamdani. Indicted on federal corruption charges 2024 (charges dismissed 2025).'),
        sources=['https://ballotpedia.org/Eric_Adams']),

    # ════════════════════════════════════════════════════════════════
    # LOS ANGELES (next 2026 primary 6/2, general 11/3)
    # ════════════════════════════════════════════════════════════════
    mayor('Karen Bass', 'karen-bass', 'CA', 'Los Angeles',
        'D', 'progressive_d', next_election=2026, next_election_date='2026-06-02',
        notes=('D incumbent Mayor of Los Angeles (since 2022). Former U.S. Representative CA-37 '
               '(2011-2023). Considered for VP by Biden 2020. Faced criticism over 2025 LA '
               'wildfires response. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Karen_Bass']),
    mayor('Rick Caruso', 'rick-caruso', 'CA', 'Los Angeles',
        'D', 'establishment_d', candidacy_status='primary_candidate',
        next_election=2026, next_election_date='2026-06-02',
        notes=('Real estate developer (Caruso Affiliated). 2022 D mayoral nominee (lost to Bass). '
               'Former LADWP commissioner. Considering 2026 rematch vs Bass.'),
        sources=['https://ballotpedia.org/Rick_Caruso']),

    # ════════════════════════════════════════════════════════════════
    # CHICAGO (Brandon Johnson sitting · next election 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Brandon Johnson', 'brandon-johnson-mayor', 'IL', 'Chicago',
        'D', 'progressive_d', next_election=2027,
        notes=('D incumbent Mayor of Chicago (since 2023). Former Cook County commissioner. '
               'Former CTU organizer. Progressive Democrat. Approval ratings low through 2025-26. '
               'Next election 2027.'),
        sources=['https://ballotpedia.org/Brandon_Johnson']),

    # ════════════════════════════════════════════════════════════════
    # HOUSTON (John Whitmire sitting · 2027 next)
    # ════════════════════════════════════════════════════════════════
    mayor('John Whitmire', 'john-whitmire-mayor', 'TX', 'Houston',
        'D', 'establishment_d', next_election=2027,
        notes=('D incumbent Mayor of Houston (since 2024). Former TX state senator (longest-serving). '
               'Moderate Democrat. Next election 2027.'),
        sources=['https://ballotpedia.org/John_Whitmire']),

    # ════════════════════════════════════════════════════════════════
    # PHOENIX (Kate Gallego sitting · next 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Kate Gallego', 'kate-gallego', 'AZ', 'Phoenix',
        'D', 'establishment_d', next_election=2027,
        notes=('D incumbent Mayor of Phoenix (since 2019). Former Phoenix city councilor. '
               'Former wife of U.S. Sen. Ruben Gallego (AZ). Next election 2027.'),
        sources=['https://ballotpedia.org/Kate_Gallego']),

    # ════════════════════════════════════════════════════════════════
    # PHILADELPHIA (Cherelle Parker sitting · next 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Cherelle Parker', 'cherelle-parker', 'PA', 'Philadelphia',
        'D', 'establishment_d', next_election=2027,
        notes=('D incumbent Mayor of Philadelphia (since 2024). Former Philadelphia city councilor. '
               'First Black woman mayor of Philadelphia. Tough-on-crime moderate D. Next election 2027.'),
        sources=['https://ballotpedia.org/Cherelle_Parker']),

    # ════════════════════════════════════════════════════════════════
    # SAN ANTONIO (Gina Ortiz Jones won 2025 · next 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Gina Ortiz Jones', 'gina-ortiz-jones-mayor', 'TX', 'San Antonio',
        'D', 'progressive_d', next_election=2027,
        notes=('D Mayor of San Antonio (sworn 2025). Former Under Secretary of the Air Force '
               '(Biden admin). Former Air Force intelligence officer. Twice 2018/2020 D '
               'nominee for TX-23 (lost both). Won 2025 runoff. Next election 2027.'),
        sources=['https://ballotpedia.org/Gina_Ortiz_Jones']),

    # ════════════════════════════════════════════════════════════════
    # SAN DIEGO (Todd Gloria sitting · next 2028)
    # ════════════════════════════════════════════════════════════════
    mayor('Todd Gloria', 'todd-gloria', 'CA', 'San Diego',
        'D', 'establishment_d', next_election=2028,
        notes=('D incumbent Mayor of San Diego (since 2020). Former CA state assemblyman. '
               'First openly gay Mayor of San Diego. Next election 2028.'),
        sources=['https://ballotpedia.org/Todd_Gloria']),

    # ════════════════════════════════════════════════════════════════
    # DALLAS (Eric Johnson R-switch sitting · next 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Eric Johnson', 'eric-johnson-mayor', 'TX', 'Dallas',
        'R', 'establishment_r', next_election=2027,
        notes=('Mayor of Dallas (since 2019). Lifelong Democrat; switched to Republican in 2023 '
               '(rare big-city D-to-R mayor switch). Former TX state representative. '
               'Term-limited 2027.'),
        sources=['https://ballotpedia.org/Eric_Johnson_(Texas_politician)']),

    # ════════════════════════════════════════════════════════════════
    # AUSTIN (Kirk Watson sitting · next 2026)
    # ════════════════════════════════════════════════════════════════
    mayor('Kirk Watson', 'kirk-watson-mayor', 'TX', 'Austin',
        'D', 'establishment_d', next_election=2026, next_election_date='2026-11-03',
        notes=('D incumbent Mayor of Austin (since 2023). Former TX state senator. Former '
               'mayor of Austin 1997-2001. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/Kirk_Watson']),

    # ════════════════════════════════════════════════════════════════
    # JACKSONVILLE (Donna Deegan sitting · next 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Donna Deegan', 'donna-deegan', 'FL', 'Jacksonville',
        'D', 'establishment_d', next_election=2027,
        notes=('D incumbent Mayor of Jacksonville (since 2023). Former TV news anchor. Breast '
               'cancer advocate. First D mayor of Jacksonville in 8 years. Next election 2027.'),
        sources=['https://ballotpedia.org/Donna_Deegan']),

    # ════════════════════════════════════════════════════════════════
    # SAN FRANCISCO (Daniel Lurie won Nov 2024 · next 2028)
    # ════════════════════════════════════════════════════════════════
    mayor('Daniel Lurie', 'daniel-lurie', 'CA', 'San Francisco',
        'D', 'establishment_d', next_election=2028,
        notes=('D Mayor of San Francisco (sworn Jan 2025). Tipping Point Community founder. '
               'Levi Strauss heir. Defeated incumbent London Breed in Nov 2024 RCV election. '
               'Centrist Democrat. Next election 2028.'),
        sources=['https://ballotpedia.org/Daniel_Lurie']),

    # ════════════════════════════════════════════════════════════════
    # BOSTON (Michelle Wu won Nov 2025 reelection · next 2029)
    # ════════════════════════════════════════════════════════════════
    mayor('Michelle Wu', 'michelle-wu', 'MA', 'Boston',
        'D', 'progressive_d', next_election=2029,
        notes=('D incumbent Mayor of Boston (since 2021, reelected Nov 2025). Former Boston '
               'city councilor. First Asian American + first woman elected Boston Mayor. '
               'Progressive Democrat. Next election 2029.'),
        sources=['https://ballotpedia.org/Michelle_Wu']),

    # ════════════════════════════════════════════════════════════════
    # DETROIT (open 2025 — Mary Sheffield won Nov 2025 · next 2029)
    # ════════════════════════════════════════════════════════════════
    mayor('Mary Sheffield', 'mary-sheffield-mayor', 'MI', 'Detroit',
        'D', 'establishment_d', next_election=2029,
        notes=('D Mayor of Detroit (sworn Jan 2026, won Nov 2025). Former Detroit city council '
               'president. Succeeded Mike Duggan (who is now running for MI Governor as I). '
               'Next election 2029.'),
        sources=['https://ballotpedia.org/Mary_Sheffield']),

    # ════════════════════════════════════════════════════════════════
    # SEATTLE (Bruce Harrell sitting · next 2025 — already happened)
    # ════════════════════════════════════════════════════════════════
    mayor('Bruce Harrell', 'bruce-harrell-mayor', 'WA', 'Seattle',
        'D', 'establishment_d', next_election=2025, candidacy_status='won',
        notes=('D incumbent Mayor of Seattle (since 2022, reelected Nov 2025). Former Seattle '
               'city council president. Centrist Democrat. Next election 2029.'),
        sources=['https://ballotpedia.org/Bruce_Harrell']),

    # ════════════════════════════════════════════════════════════════
    # DENVER (Mike Johnston sitting · next 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Mike Johnston', 'mike-johnston', 'CO', 'Denver',
        'D', 'establishment_d', next_election=2027,
        notes=('D incumbent Mayor of Denver (since 2023). Former CO state senator. 2018 D Senate '
               'primary candidate. Education-reform Democrat. Next election 2027.'),
        sources=['https://ballotpedia.org/Mike_Johnston']),

    # ════════════════════════════════════════════════════════════════
    # NASHVILLE (Freddie O'Connell sitting · next 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Freddie O\'Connell', 'freddie-oconnell', 'TN', 'Nashville',
        'D', 'progressive_d', next_election=2027,
        notes=('D incumbent Mayor of Nashville (since 2023). Former Nashville Metro Council '
               'member. Transit + housing advocate. Next election 2027.'),
        sources=['https://ballotpedia.org/Freddie_O\'Connell']),

    # ════════════════════════════════════════════════════════════════
    # MEMPHIS (Paul Young sitting · next 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Paul Young', 'paul-young-mayor', 'TN', 'Memphis',
        'D', 'establishment_d', next_election=2027,
        notes=('D Mayor of Memphis (since 2024). Former Memphis Downtown Memphis Commission CEO. '
               'Successor to Jim Strickland. Next election 2027.'),
        sources=['https://ballotpedia.org/Paul_Young']),

    # ════════════════════════════════════════════════════════════════
    # OKLAHOMA CITY (David Holt sitting R · next 2026 February)
    # ════════════════════════════════════════════════════════════════
    mayor('David Holt', 'david-holt-mayor', 'OK', 'Oklahoma City',
        'R', 'establishment_r', next_election=2026, next_election_date='2026-02-10',
        notes=('R incumbent Mayor of Oklahoma City (since 2018). Former Mary Fallin chief of staff. '
               'Former OK state senator. Moderate Republican. Seeking 2026 reelection.'),
        sources=['https://ballotpedia.org/David_Holt']),

    # ════════════════════════════════════════════════════════════════
    # PORTLAND OR (Keith Wilson sitting · next 2028)
    # ════════════════════════════════════════════════════════════════
    mayor('Keith Wilson', 'keith-wilson-mayor', 'OR', 'Portland',
        'D', 'establishment_d', next_election=2028,
        notes=('D Mayor of Portland (since Jan 2025). Trucking company CEO. Won Nov 2024 '
               'election (under new charter that takes effect 2025). Next election 2028.'),
        sources=['https://ballotpedia.org/Keith_Wilson']),

    # ════════════════════════════════════════════════════════════════
    # ATLANTA (Andre Dickens sitting · next 2025 — reelected)
    # ════════════════════════════════════════════════════════════════
    mayor('Andre Dickens', 'andre-dickens', 'GA', 'Atlanta',
        'D', 'establishment_d', next_election=2025, candidacy_status='won',
        notes=('D incumbent Mayor of Atlanta (since 2022, reelected Nov 2025). Former Atlanta '
               'city councilor. Business-friendly Democrat. Next election 2029.'),
        sources=['https://ballotpedia.org/Andre_Dickens']),

    # ════════════════════════════════════════════════════════════════
    # CHARLOTTE (Vi Lyles sitting · next 2025 reelection cycle)
    # ════════════════════════════════════════════════════════════════
    mayor('Vi Lyles', 'vi-lyles-mayor', 'NC', 'Charlotte',
        'D', 'establishment_d', next_election=2025, candidacy_status='won',
        notes=('D incumbent Mayor of Charlotte (since 2017, reelected 4x including Nov 2025). '
               'Former Charlotte city councilor. Longest-serving Charlotte mayor in recent history. '
               'Next election 2027.'),
        sources=['https://ballotpedia.org/Vi_Lyles']),

    # ════════════════════════════════════════════════════════════════
    # LAS VEGAS (Shelley Berkley sitting · next 2027)
    # ════════════════════════════════════════════════════════════════
    mayor('Shelley Berkley', 'shelley-berkley', 'NV', 'Las Vegas',
        'D', 'establishment_d', next_election=2027,
        notes=('D Mayor of Las Vegas (since 2025). Former U.S. Representative NV-01 (1999-2013). '
               '2012 D U.S. Senate nominee (lost to Heller). Next election 2027.'),
        sources=['https://ballotpedia.org/Shelley_Berkley']),

    # ════════════════════════════════════════════════════════════════
    # MILWAUKEE (Cavalier Johnson sitting · next 2028)
    # ════════════════════════════════════════════════════════════════
    mayor('Cavalier Johnson', 'cavalier-johnson', 'WI', 'Milwaukee',
        'D', 'establishment_d', next_election=2028,
        notes=('D incumbent Mayor of Milwaukee (since 2022). Former Milwaukee Common Council '
               'president. Youngest Milwaukee mayor. Next election 2028.'),
        sources=['https://ballotpedia.org/Cavalier_Johnson']),

    # ════════════════════════════════════════════════════════════════
    # MIAMI (Francis Suarez term-limited · next election Nov 2025 result)
    # ════════════════════════════════════════════════════════════════
    mayor('Emilio González', 'emilio-gonzalez-mayor', 'FL', 'Miami',
        'R', 'establishment_r', next_election=2025, candidacy_status='won',
        notes=('R Mayor of Miami (sworn 2026, won Nov 2025). Former Director of U.S. Citizenship '
               'and Immigration Services under Trump. Cuban-American. Succeeded term-limited '
               'Francis Suarez. Next election 2029.'),
        sources=['https://ballotpedia.org/Emilio_Gonz%C3%A1lez']),

    # ════════════════════════════════════════════════════════════════
    # MINNEAPOLIS (Jacob Frey reelected Nov 2025 · next 2029)
    # ════════════════════════════════════════════════════════════════
    mayor('Jacob Frey', 'jacob-frey', 'MN', 'Minneapolis',
        'D', 'establishment_d', next_election=2025, candidacy_status='won',
        notes=('D incumbent Mayor of Minneapolis (since 2018, reelected Nov 2025). Former '
               'Minneapolis city councilor. Centrist Democrat. Mayor during 2020 George Floyd '
               'protests. Next election 2029.'),
        sources=['https://ballotpedia.org/Jacob_Frey']),

    # ════════════════════════════════════════════════════════════════
    # PITTSBURGH (Ed Gainey · D primary 5/19 DONE - lost to Corey O'Connor)
    # ════════════════════════════════════════════════════════════════
    mayor('Corey O\'Connor', 'corey-oconnor', 'PA', 'Pittsburgh',
        'D', 'establishment_d', candidacy_status='general_candidate', next_election=2025,
        notes=('D nominee for Mayor of Pittsburgh (won May 2025 D primary vs incumbent Ed Gainey). '
               'Allegheny County Controller. Son of former PA Senator Bob O\'Connor. '
               'General election Nov 2025.'),
        sources=['https://ballotpedia.org/Corey_O\'Connor']),

    # ════════════════════════════════════════════════════════════════
    # CLEVELAND (Justin Bibb · next 2025 - reelected)
    # ════════════════════════════════════════════════════════════════
    mayor('Justin Bibb', 'justin-bibb', 'OH', 'Cleveland',
        'D', 'establishment_d', next_election=2025, candidacy_status='won',
        notes=('D incumbent Mayor of Cleveland (since 2022, reelected Nov 2025). Former tech '
               'executive. Youngest Cleveland mayor in 50+ years. Next election 2029.'),
        sources=['https://ballotpedia.org/Justin_Bibb']),
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
        print(f'  {action} {r["name"]:<28s} ({r["state"]} mayor {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
