#!/usr/bin/env python3
"""
add-fl-batch.py — add a curated batch of Florida officials to scorecard.json.

Covers gaps identified in the audit:
  - Florida Supreme Court (7 justices)
  - Tallahassee city government (mayor + commission)
  - St. Petersburg city government (mayor + city council)

Each official is added with:
  - Level/jurisdiction/office
  - Party (R/D/I or None for nonpartisan judicial)
  - Default scores based on appointing-governor / party lean
  - Empty notes/sources (to be populated incrementally)

After adding, runs build-data.py automatically.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'

# Default score templates
CONSERVATIVE_R = {
    "america_first": [True, True, True, None, True],
    "life": [True, True, True, True, True],
    "immigration": [True, True, None, None, None],
    "marriage": [True, True, True, True, False],
    "christian_heritage": [False, False, False, False, False],
    "self_defense": [True, True, True, True, True],
    "education": [True, True, True, None, True]
}
PROGRESSIVE_D = {
    "america_first": [False, False, True, None, False],
    "life": [False, False, False, False, False],
    "immigration": [False, False, False, False, False],
    "marriage": [False, False, False, False, False],
    "christian_heritage": [False, False, False, False, False],
    "self_defense": [False, False, False, False, False],
    "education": [False, False, False, False, False]
}
# For judicial officials — we score based on their rulings and appointing governor's
# philosophy, not on stated partisan positions. DeSantis appointees tend to be
# conservative-originalist; Crist-era appointees tend to be moderate-to-progressive.
# Most Florida Supreme Court justices haven't ruled on every category, so we leave
# many nulls until we review specific rulings.
JUDICIAL_UNKNOWN = {k: [None]*5 for k in CONSERVATIVE_R}

def slugify(name):
    return (name.lower()
              .replace(' ', '-')
              .replace('.', '')
              .replace("'", '')
              .replace(',', '')
              .replace('"', '')
              .replace('—', '-'))


def make_candidate(name, office, jurisdiction, level, party, district=None,
                   scores=None, notes='', sources=None, profile=None,
                   website=None):
    """Build a candidate dict in the scorecard schema."""
    if scores is None:
        if party == 'R':
            scores = {k: list(v) for k, v in CONSERVATIVE_R.items()}
        elif party == 'D':
            scores = {k: list(v) for k, v in PROGRESSIVE_D.items()}
        else:
            scores = {k: [None]*5 for k in CONSERVATIVE_R}
    return {
        'name': name,
        'slug': slugify(name),
        'office': office,
        'jurisdiction': jurisdiction,
        'level': level,
        'party': party,
        'district': district,
        'state': 'FL',
        # id filled in later
        'scores': scores,
        'notes': notes,
        'photo': None,
        'website': website,
        'sources': sources or [],
        'profile': profile or {
            'religion': None, 'net_worth': None, 'birthplace': None,
            'education': None, 'background': None,
            'prev_election_opponent': None,
            'next_election_year': None,
            'next_election_contenders': [],
        },
    }


# ---- Florida Supreme Court (7 justices) ----
# Nonpartisan bench. All but one (Labarga) appointed by Republican governors.
# Scoring held mostly null; we'll populate from specific rulings later.
# Source: https://www.floridasupremecourt.org/Justices
FL_SUPREMES = [
    make_candidate(
        'Carlos G. Muñiz',
        'Chief Justice, Florida Supreme Court',
        'Supreme Court of Florida',
        'judicial', None,
        notes='Chief Justice since July 2024. Appointed to bench by Gov. DeSantis in January 2019. '
              'Former General Counsel to Gov. Rick Scott, former Deputy AG of Florida, and former '
              'Chief of Staff to AG Pam Bondi. Authored opinion overturning Roe-era abortion precedent '
              'in Florida in 2024 (Planned Parenthood v. Moody).',
        scores={
            **JUDICIAL_UNKNOWN,
            'life': [True, True, True, None, None],  # PP v. Moody 2024 ruling
            'christian_heritage': [None, None, None, None, None],
        },
        sources=[
            'https://www.floridasupremecourt.org/Justices/Chief-Justice-Carlos-G-Muniz',
            'https://ballotpedia.org/Carlos_Muniz',
        ],
        profile={'religion': None, 'net_worth': None, 'birthplace': 'Jacksonville, Florida',
                 'education': 'University of Virginia (BA), Yale Law School (JD)',
                 'background': 'Appointed Jan 2019 by Gov. DeSantis. Former Deputy AG of Florida.',
                 'prev_election_opponent': None, 'next_election_year': 2028,
                 'next_election_contenders': []},
    ),
    make_candidate(
        'Charles T. Canady',
        'Associate Justice, Florida Supreme Court',
        'Supreme Court of Florida',
        'judicial', None,
        notes='Appointed to Florida Supreme Court in 2008 by Gov. Charlie Crist. Served as Chief '
              'Justice 2010-2012 and 2018-2022. Former US Representative (R-FL) 1993-2001. Known '
              'for originalist jurisprudence. Authored the 2022 opinion ending the Florida '
              'Supreme Court\'s 30-year practice of issuing advisory opinions on redistricting.',
        scores={
            **JUDICIAL_UNKNOWN,
            'life': [True, True, True, None, None],
        },
        sources=[
            'https://www.floridasupremecourt.org/Justices/Justice-Charles-T-Canady',
            'https://ballotpedia.org/Charles_Canady',
        ],
        profile={'religion': 'Southern Baptist', 'net_worth': None, 'birthplace': 'Lakeland, Florida',
                 'education': 'Haverford College (BA), Yale Law School (JD)',
                 'background': 'US House 1993-2001. Appointed to FL Supreme Court 2008 by Gov. Crist.',
                 'prev_election_opponent': None, 'next_election_year': 2028,
                 'next_election_contenders': []},
    ),
    make_candidate(
        'Jorge Labarga',
        'Associate Justice, Florida Supreme Court',
        'Supreme Court of Florida',
        'judicial', None,
        notes='Appointed to Florida Supreme Court 2009 by Gov. Charlie Crist. Served as Chief '
              'Justice 2014-2018. Most moderate member of the court. First Cuban-American to serve '
              'as Chief Justice of the Florida Supreme Court. Frequent dissenter in the post-DeSantis '
              'conservative majority era.',
        sources=[
            'https://www.floridasupremecourt.org/Justices/Justice-Jorge-Labarga',
            'https://ballotpedia.org/Jorge_Labarga',
        ],
        profile={'religion': None, 'net_worth': None, 'birthplace': 'Cuba',
                 'education': 'University of Florida (BA, JD)',
                 'background': 'Appointed 2009 by Gov. Crist. Served as Chief Justice 2014-2018.',
                 'prev_election_opponent': None, 'next_election_year': 2028,
                 'next_election_contenders': []},
    ),
    make_candidate(
        'John D. Couriel',
        'Associate Justice, Florida Supreme Court',
        'Supreme Court of Florida',
        'judicial', None,
        notes='Appointed to Florida Supreme Court in May 2020 by Gov. DeSantis. Former federal '
              'prosecutor in Miami. Conservative-originalist jurist.',
        scores={
            **JUDICIAL_UNKNOWN,
            'life': [True, True, True, None, None],
        },
        sources=[
            'https://www.floridasupremecourt.org/Justices/Justice-John-D-Couriel',
            'https://ballotpedia.org/John_Couriel',
        ],
        profile={'religion': None, 'net_worth': None, 'birthplace': None,
                 'education': 'Harvard University (BA), Harvard Law School (JD)',
                 'background': 'Appointed May 2020 by Gov. DeSantis. Former federal prosecutor.',
                 'prev_election_opponent': None, 'next_election_year': 2028,
                 'next_election_contenders': []},
    ),
    make_candidate(
        'Jamie R. Grosshans',
        'Associate Justice, Florida Supreme Court',
        'Supreme Court of Florida',
        'judicial', None,
        notes='Appointed to Florida Supreme Court September 2020 by Gov. DeSantis. Former Fifth '
              'District Court of Appeal judge. Known for textualist/originalist interpretation.',
        scores={
            **JUDICIAL_UNKNOWN,
            'life': [True, True, True, None, None],
        },
        sources=[
            'https://www.floridasupremecourt.org/Justices/Justice-Jamie-R-Grosshans',
            'https://ballotpedia.org/Jamie_Grosshans',
        ],
        profile={'religion': None, 'net_worth': None, 'birthplace': None,
                 'education': 'University of Mississippi (BA, JD)',
                 'background': 'Appointed September 2020 by Gov. DeSantis.',
                 'prev_election_opponent': None, 'next_election_year': 2028,
                 'next_election_contenders': []},
    ),
    make_candidate(
        'Renatha Francis',
        'Associate Justice, Florida Supreme Court',
        'Supreme Court of Florida',
        'judicial', None,
        notes='Appointed to Florida Supreme Court in 2022 by Gov. DeSantis, making her the first '
              'Jamaican-born justice on the Florida Supreme Court. Conservative jurist.',
        scores={
            **JUDICIAL_UNKNOWN,
            'life': [True, True, True, None, None],
        },
        sources=[
            'https://www.floridasupremecourt.org/Justices/Justice-Renatha-Francis',
            'https://ballotpedia.org/Renatha_Francis',
        ],
        profile={'religion': None, 'net_worth': None, 'birthplace': 'Jamaica',
                 'education': 'Florida Coastal School of Law (JD)',
                 'background': 'Appointed 2022 by Gov. DeSantis. First Jamaican-born FL Supreme Court justice.',
                 'prev_election_opponent': None, 'next_election_year': 2028,
                 'next_election_contenders': []},
    ),
    make_candidate(
        'Meredith L. Sasso',
        'Associate Justice, Florida Supreme Court',
        'Supreme Court of Florida',
        'judicial', None,
        notes='Appointed to Florida Supreme Court in 2023 by Gov. DeSantis. Previously served on '
              'the Sixth District Court of Appeal. Conservative-originalist.',
        scores={
            **JUDICIAL_UNKNOWN,
            'life': [True, True, True, None, None],
        },
        sources=[
            'https://www.floridasupremecourt.org/Justices/Justice-Meredith-L-Sasso',
            'https://ballotpedia.org/Meredith_Sasso',
        ],
        profile={'religion': None, 'net_worth': None, 'birthplace': None,
                 'education': None,
                 'background': 'Appointed 2023 by Gov. DeSantis.',
                 'prev_election_opponent': None, 'next_election_year': 2028,
                 'next_election_contenders': []},
    ),
]

# ---- Tallahassee (state capital) city government ----
# Mayor + 4 city commissioners. All Democrats in Tallahassee which leans strongly D.
# Source: https://www.talgov.com/citycommission
TALLAHASSEE = [
    make_candidate(
        'John E. Dailey',
        'Mayor',
        'City of Tallahassee',
        'local', 'D',
        notes='Mayor of Tallahassee since 2018, re-elected 2022. Former Leon County Commissioner. '
              'Has supported Tallahassee\'s sanctuary-adjacent policies and progressive urban initiatives.',
        sources=[
            'https://www.talgov.com/citycommission/mayor',
            'https://ballotpedia.org/John_Dailey_(Florida)',
        ],
        profile={'religion': None, 'net_worth': None, 'birthplace': 'Tallahassee, Florida',
                 'education': 'Florida State University (BA, MA)',
                 'background': 'Leon County Commissioner 2006-2018. Mayor since 2018.',
                 'prev_election_opponent': None, 'next_election_year': 2026,
                 'next_election_contenders': []},
    ),
    make_candidate(
        'Dianne Williams-Cox',
        'City Commissioner, Seat 1',
        'City of Tallahassee',
        'local', 'D',
        notes='Tallahassee City Commissioner since 2018. Re-elected 2022.',
        sources=[
            'https://www.talgov.com/citycommission',
            'https://ballotpedia.org/Dianne_Williams-Cox',
        ],
    ),
    make_candidate(
        'Curtis Richardson',
        'City Commissioner, Seat 2',
        'City of Tallahassee',
        'local', 'D',
        notes='Tallahassee City Commissioner since 2014. Former Florida State Representative.',
        sources=[
            'https://www.talgov.com/citycommission',
            'https://ballotpedia.org/Curtis_Richardson',
        ],
    ),
    make_candidate(
        'Jeremy Matlow',
        'City Commissioner, Seat 3',
        'City of Tallahassee',
        'local', 'D',
        notes='Tallahassee City Commissioner since 2018. Progressive activist wing.',
        sources=[
            'https://www.talgov.com/citycommission',
            'https://ballotpedia.org/Jeremy_Matlow',
        ],
    ),
    make_candidate(
        'Jacqueline "Jack" Porter',
        'City Commissioner, Seat 5',
        'City of Tallahassee',
        'local', 'D',
        notes='Tallahassee City Commissioner since 2020. Progressive-wing Democrat.',
        sources=[
            'https://www.talgov.com/citycommission',
            'https://ballotpedia.org/Jack_Porter',
        ],
    ),
]

# ---- St. Petersburg (4th largest FL city) ----
# Mayor-council system. Officially nonpartisan but mostly D-leaning.
# Source: https://www.stpete.org/government/city_council
ST_PETE = [
    make_candidate(
        'Kenneth T. Welch',
        'Mayor',
        'City of St. Petersburg',
        'local', 'D',
        notes='First Black mayor of St. Petersburg, elected November 2021. Previously served as '
              'Pinellas County Commissioner from 2000-2020. Focus on affordable housing and '
              'Historic Gas Plant / Tropicana Field redevelopment.',
        sources=[
            'https://www.stpete.org/government/mayor/index.php',
            'https://ballotpedia.org/Ken_Welch_(Florida)',
        ],
        profile={'religion': None, 'net_worth': None, 'birthplace': 'St. Petersburg, Florida',
                 'education': 'USF (BA), USF (MBA)',
                 'background': 'Pinellas County Commissioner 2000-2020. Mayor since 2022.',
                 'prev_election_opponent': 'Robert Blackmon (R) in 2021 Mayor race',
                 'next_election_year': 2025, 'next_election_contenders': []},
    ),
    make_candidate(
        'Copley Gerdes',
        'City Council, District 1',
        'City of St. Petersburg',
        'local', 'D',
        notes='St. Petersburg City Council, District 1. Elected 2021.',
        sources=[
            'https://www.stpete.org/government/city_council',
            'https://ballotpedia.org/Copley_Gerdes',
        ],
    ),
    make_candidate(
        'Brandi Gabbard',
        'City Council, District 2',
        'City of St. Petersburg',
        'local', 'D',
        notes='St. Petersburg City Council, District 2, since 2017.',
        sources=[
            'https://www.stpete.org/government/city_council',
            'https://ballotpedia.org/Brandi_Gabbard',
        ],
    ),
    make_candidate(
        'Mike Harting',
        'City Council, District 3',
        'City of St. Petersburg',
        'local', 'D',
        notes='St. Petersburg City Council, District 3. Elected 2023.',
        sources=[
            'https://www.stpete.org/government/city_council',
        ],
    ),
    make_candidate(
        'Lisset Hanewicz',
        'City Council, District 4',
        'City of St. Petersburg',
        'local', 'D',
        notes='St. Petersburg City Council, District 4. Elected 2021.',
        sources=[
            'https://www.stpete.org/government/city_council',
        ],
    ),
    make_candidate(
        'Deborah Figgs-Sanders',
        'City Council, District 5',
        'City of St. Petersburg',
        'local', 'D',
        notes='St. Petersburg City Council, District 5. Elected 2019, re-elected 2023.',
        sources=[
            'https://www.stpete.org/government/city_council',
            'https://ballotpedia.org/Deborah_Figgs-Sanders',
        ],
    ),
    make_candidate(
        'Gina Driscoll',
        'City Council, District 6',
        'City of St. Petersburg',
        'local', 'D',
        notes='St. Petersburg City Council, District 6. Elected 2017, re-elected 2021.',
        sources=[
            'https://www.stpete.org/government/city_council',
            'https://ballotpedia.org/Gina_Driscoll',
        ],
    ),
    make_candidate(
        'Corey Givens Jr.',
        'City Council, District 7',
        'City of St. Petersburg',
        'local', 'D',
        notes='St. Petersburg City Council, District 7. Elected 2025 special election.',
        sources=[
            'https://www.stpete.org/government/city_council',
        ],
    ),
    make_candidate(
        'Richie Floyd',
        'City Council, District 8',
        'City of St. Petersburg',
        'local', 'D',
        notes='St. Petersburg City Council, District 8, since 2021. Democratic Socialist.',
        sources=[
            'https://www.stpete.org/government/city_council',
            'https://ballotpedia.org/Richie_Floyd',
        ],
    ),
]

FORT_LAUDERDALE = [
    make_candidate(
        'Dean Trantalis',
        'Mayor',
        'City of Fort Lauderdale',
        'local', 'D',
        notes='Mayor of Fort Lauderdale since 2018, re-elected unopposed in 2022. Former Fort '
              'Lauderdale City Commissioner. First openly gay mayor of Fort Lauderdale. Supported '
              'Pride programming, affordable housing, and climate resilience initiatives.',
        sources=[
            'https://www.fortlauderdale.gov/government/our-mayor',
            'https://ballotpedia.org/Dean_Trantalis',
        ],
        profile={'religion': None, 'net_worth': None, 'birthplace': 'Poughkeepsie, New York',
                 'education': 'Boston University (BA), Nova Southeastern (JD)',
                 'background': 'Fort Lauderdale City Commissioner 2003-2006 and 2013-2018. Mayor since 2018.',
                 'prev_election_opponent': None, 'next_election_year': 2026,
                 'next_election_contenders': []},
    ),
]

HIALEAH = [
    make_candidate(
        'Esteban Bovo Jr.',
        'Mayor',
        'City of Hialeah',
        'local', 'R',
        notes='Mayor of Hialeah since November 2021. Cuban-American Republican. Former Miami-Dade '
              'County Commissioner (2011-2020) and Florida State Representative (2008-2010). '
              'Strong conservative on immigration enforcement, anti-communism (Cuba), and fiscal policy.',
        sources=[
            'https://www.hialeahfl.gov/155/Mayors-Office',
            'https://ballotpedia.org/Esteban_Bovo',
        ],
        profile={'religion': 'Catholic', 'net_worth': None, 'birthplace': 'Miami, Florida',
                 'education': 'Miami Dade College (AA), Florida International University (BA)',
                 'background': 'FL House 2008-2010. Miami-Dade Commissioner 2011-2020. Hialeah Mayor since 2021.',
                 'prev_election_opponent': 'Julio Martinez (R) in 2021 Mayor race',
                 'next_election_year': 2025, 'next_election_contenders': []},
    ),
]

ALL_NEW = FL_SUPREMES + TALLAHASSEE + ST_PETE + FORT_LAUDERDALE + HIALEAH


def main():
    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    # Find next available id
    max_id = max(c.get('id', 0) for c in data['candidates'])
    next_id = max_id + 1

    # Check for duplicates (same name + state already in scorecard)
    existing_keys = {(c['name'], c.get('state'), c.get('office')) for c in data['candidates']}
    added = 0
    skipped = 0
    for c in ALL_NEW:
        key = (c['name'], c.get('state'), c.get('office'))
        if key in existing_keys:
            print(f"  SKIP (already exists): {c['name']} / {c['office']}")
            skipped += 1
            continue
        c['id'] = next_id
        next_id += 1
        data['candidates'].append(c)
        added += 1
        print(f"  ADD: {c['name']} ({c['office']})")

    data['meta']['total_candidates'] = len(data['candidates'])

    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nAdded: {added}, skipped (dupes): {skipped}")
    print(f"New total: {len(data['candidates'])}")

    # Rebuild per-state files + index.json
    print("\nRebuilding per-state files via build-data.py...")
    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
