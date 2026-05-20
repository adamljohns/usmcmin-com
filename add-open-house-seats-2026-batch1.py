#!/usr/bin/env python3
"""
add-open-house-seats-2026-batch1.py — Pass 2 House primary work, batch 1.

Top 10 highest-priority open House seats:
  NE-02 (Bacon R retiring; primary 5/12 ALREADY HAPPENED)
  ME-02 (Golden D retiring; primary 6/9)
  NY-21 (Stefanik R retiring; primary 6/23)
  CA-48 (Issa R retiring; jungle primary 6/2)
  MT-01 (Zinke R retiring; primary 6/2)
  AZ-01 (Schweikert R running Gov; primary 7/21)
  MI-10 (James R running Gov; primary 8/4)
  SC-01 (Mace R running Gov; primary 6/9)
  NY-12 (Nadler D retiring; primary 6/23)
  CA-11 (Pelosi D retiring; jungle primary 6/2)

~90 candidates total. Top-tier candidates (Trump-endorsed, prior nominee,
state-party-endorsed, prominent name) get archetype-based scoring;
lower-tier get placeholder (all null) records pending evidence.

Subsequent batches will cover the remaining ~40 open House seats.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None

# Re-use the same archetype table from add-open-senate-seats-2026.py
ARCHETYPES = {
    'maga_conservative_r': {
        'sanctity_of_life':         [T, T, T, T, T],
        'biblical_marriage':        [T, T, T, T, T],
        'family_child_sovereignty': [T, T, T, T, T],
        'christian_liberty':        [T, T, T, T, N],
        'economic_stewardship':     [T, N, T, N, T],
        'election_integrity':       [N, T, N, T, T],
        'border_immigration':       [T, T, T, T, T],
        'self_defense':             [T, T, T, T, T],
        'foreign_policy_restraint': [N, N, N, F, N],
        'industry_capture':         [N, N, N, T, N],
    },
    'establishment_r': {
        'sanctity_of_life':         [T, F, T, T, T],
        'biblical_marriage':        [N, F, T, N, N],
        'family_child_sovereignty': [N, N, T, N, N],
        'christian_liberty':        [T, N, N, N, N],
        'economic_stewardship':     [N, F, N, N, F],
        'election_integrity':       [F, T, F, F, T],
        'border_immigration':       [T, T, T, T, T],
        'self_defense':             [T, F, F, T, T],
        'foreign_policy_restraint': [F, F, F, F, F],
        'industry_capture':         [F, F, F, N, F],
    },
    'progressive_d': {
        'sanctity_of_life':         [F, F, F, F, F],
        'biblical_marriage':        [F, F, F, F, F],
        'family_child_sovereignty': [F, F, F, F, F],
        'christian_liberty':        [F, F, F, F, F],
        'economic_stewardship':     [F, F, F, N, T],
        'election_integrity':       [F, F, F, F, F],
        'border_immigration':       [F, F, F, F, F],
        'self_defense':             [F, F, F, F, F],
        'foreign_policy_restraint': [N, T, N, N, N],
        'industry_capture':         [N, F, T, N, T],
    },
    'establishment_d': {
        'sanctity_of_life':         [F, F, F, F, F],
        'biblical_marriage':        [F, F, F, F, F],
        'family_child_sovereignty': [F, F, F, F, F],
        'christian_liberty':        [F, F, F, F, F],
        'economic_stewardship':     [F, F, F, F, F],
        'election_integrity':       [F, F, F, F, F],
        'border_immigration':       [F, F, F, F, F],
        'self_defense':             [F, F, F, F, F],
        'foreign_policy_restraint': [F, F, F, F, F],
        'industry_capture':         [F, F, F, F, F],
    },
    'populist_right': {
        'sanctity_of_life':         [T, T, T, T, T],
        'biblical_marriage':        [T, T, T, T, T],
        'family_child_sovereignty': [T, T, T, T, T],
        'christian_liberty':        [T, T, T, T, N],
        'economic_stewardship':     [T, N, F, N, T],
        'election_integrity':       [N, T, T, T, T],
        'border_immigration':       [T, T, T, T, T],
        'self_defense':             [T, T, T, T, T],
        'foreign_policy_restraint': [T, T, T, F, T],
        'industry_capture':         [T, T, T, N, T],
    },
}


def scores_from(archetype, overrides=None):
    base = {cid: list(row) for cid, row in ARCHETYPES[archetype].items()}
    if overrides:
        for cid, row in overrides.items():
            base[cid] = list(row)
    return base


def empty_scores():
    return {cid: [None]*5 for cid in [
        'sanctity_of_life','biblical_marriage','family_child_sovereignty','christian_liberty',
        'economic_stewardship','election_integrity','border_immigration','self_defense',
        'foreign_policy_restraint','industry_capture',
    ]}


def make_record(name, slug, state, district, office, party, archetype=None,
                primary_date='', notes='', sources=None, profile_extra=None,
                candidacy_status='primary_candidate', confidence_note=''):
    return {
        'name': name, 'slug': slug, 'state': state,
        'office': office,
        'jurisdiction': 'United States House of Representatives',
        'party': party, 'level': 'federal', 'district': district,
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '',
        'sources': sources or [f'https://ballotpedia.org/{state}_{district}_2026_House'],
        'notes': notes,
        'footnotes': [], 'answer_footnotes': {},
        'scores': scores_from(archetype) if archetype else empty_scores(),
        'profile': {
            'next_election': 2026,
            'next_election_type': 'primary',
            'seat_up_next': True,
            'next_election_date': primary_date,
            'confidence': 'archetype_curated' if archetype else 'low_evidence',
            'confidence_note': confidence_note or
                (f'2026-05-19 — ingested for 2026 open House seat ({state}-{district}). '
                 f'Archetype: {archetype}.' if archetype
                 else f'2026-05-19 — placeholder for 2026 open House seat ({state}-{district}). All scores null pending evidence.'),
            **(profile_extra or {}),
        },
    }


def placeholder(name, slug, state, district, party, primary_date, seat_context=''):
    label = {'R': 'R', 'D': 'D', 'I': 'I', 'NPP': 'No Party Pref'}[party]
    office = f'U.S. Representative {state}-{district:02d} (2026 {label} Candidate · open seat{(" · " + seat_context) if seat_context else ""})'
    return make_record(
        name=name, slug=slug, state=state, district=district,
        office=office, party=party, archetype=None,
        primary_date=primary_date, candidacy_status='primary_candidate',
        notes=f'{name} — on the 2026 {state}-{district:02d} primary ballot. '
              f'Placeholder record for ballot completeness.',
    )


# ════════════════════════════════════════════════════════════════════════
# NE-02 (Bacon R retiring; primary 5/12 already happened)
# Brinker Harding (R Nominee, Trump-endorsed, unopposed)
# Denise Powell (D Nominee, won razor-thin primary over John Cavanaugh)
# ════════════════════════════════════════════════════════════════════════
NE02 = [
    make_record(
        name='Brinker Harding', slug='brinker-harding', state='NE', district=2,
        office='U.S. Representative NE-02 (2026 R Nominee · Bacon-seat open · Trump-endorsed)',
        party='R', archetype='maga_conservative_r',
        primary_date='2026-05-12',
        candidacy_status='general_candidate',
        notes=('Omaha city councilman. Ran unopposed in 2026 R primary for NE-02 — '
               'the "blue dot" district Kamala Harris won in 2024. Trump-endorsed. '
               'Will face Denise Powell (D) in November.'),
        sources=[
            'https://ballotpedia.org/Nebraska%27s_2nd_Congressional_District_election,_2026',
            'https://omaha.com/news/local/government-politics/elections/article_7ad4ea6a-f651-4401-950a-9128de9ef734.html',
        ],
        profile_extra={'background': 'Omaha city councilman.', 'next_election_type': 'general', 'next_election_date': '2026-11-03'},
    ),
    make_record(
        name='Denise Powell', slug='denise-powell-ne-02', state='NE', district=2,
        office='U.S. Representative NE-02 (2026 D Nominee · Bacon-seat open)',
        party='D', archetype='progressive_d',
        primary_date='2026-05-12',
        candidacy_status='general_candidate',
        notes=('Political organizer. Won 2026 D primary by ~2 points over state Sen. '
               'John Cavanaugh in the "blue dot" district. Will face Brinker Harding (R).'),
        sources=['https://www.cnn.com/2026/05/12/politics/nebraska-blue-dot-2nd-district-primary-tuesday',
                 'https://www.npr.org/2026/05/13/g-s1-121987/denise-powell-democrat-wins-nebraska-second-congressional-district'],
        profile_extra={'background': 'Political organizer.', 'next_election_type': 'general', 'next_election_date': '2026-11-03'},
    ),
    placeholder('Kishla Askins', 'kishla-askins', 'NE', 2, 'D', '2026-05-12', 'Bacon seat, lost'),
    placeholder('Melanie Williams', 'melanie-williams-ne-02', 'NE', 2, 'D', '2026-05-12', 'Bacon seat, lost (Dem Socialist)'),
    placeholder('Crystal Rhoades', 'crystal-rhoades', 'NE', 2, 'D', '2026-05-12', 'Bacon seat, lost'),
    placeholder('John Cavanaugh', 'john-cavanaugh-ne-02', 'NE', 2, 'D', '2026-05-12', 'Bacon seat, lost (state senator)'),
]

# ════════════════════════════════════════════════════════════════════════
# ME-02 (Golden D retiring; primary 6/9)
# R: James Clark, Paul LePage (former Gov)
# D: Joe Baldacci, Matthew Dunlap, Paige Loud, Jordan Wood
# ════════════════════════════════════════════════════════════════════════
ME02 = [
    make_record(
        name='Paul LePage', slug='paul-lepage', state='ME', district=2,
        office='U.S. Representative ME-02 (2026 R Candidate · Golden-seat open · former Maine Governor)',
        party='R', archetype='maga_conservative_r',
        primary_date='2026-06-09',
        notes=('Former Maine Governor (2011-2019). 2022 R nominee for Maine Governor (lost to '
               'Janet Mills). Polarizing populist R. Announced May 2025 for the 2026 ME-02 race. '
               'Likely R primary front-runner.'),
        sources=['https://ballotpedia.org/Paul_LePage', 'https://en.wikipedia.org/wiki/Paul_LePage'],
        profile_extra={'background': 'Two-term Governor of Maine (2011-2019). Hard-line populist R.',
                       'religion': 'Catholic'},
    ),
    placeholder('James Clark', 'james-clark-me-02', 'ME', 2, 'R', '2026-06-09', 'Golden seat'),
    placeholder('Joe Baldacci', 'joe-baldacci', 'ME', 2, 'D', '2026-06-09', 'Golden seat (Bangor city councilor)'),
    placeholder('Matthew Dunlap', 'matthew-dunlap', 'ME', 2, 'D', '2026-06-09', 'Golden seat (former ME SecState)'),
    placeholder('Paige Loud', 'paige-loud', 'ME', 2, 'D', '2026-06-09', 'Golden seat'),
    placeholder('Jordan Wood', 'jordan-wood', 'ME', 2, 'D', '2026-06-09', 'Golden seat'),
]

# ════════════════════════════════════════════════════════════════════════
# NY-21 (Stefanik R retiring; primary 6/23)
# R: Allen Caruso, Anthony Constantino, Robert Smullen (state party endorsed)
# D: Stuart Amoriell, Blake Gendebien, Dylan Hewitt
# ════════════════════════════════════════════════════════════════════════
NY21 = [
    make_record(
        name='Robert Smullen', slug='robert-smullen', state='NY', district=21,
        office='U.S. Representative NY-21 (2026 R Candidate · Stefanik-seat open · NY GOP-endorsed)',
        party='R', archetype='maga_conservative_r',
        primary_date='2026-06-23',
        notes=('NY State Assemblyman. Endorsed by NY Republican State Committee. '
               'Marine Corps veteran. R primary candidate for the open NY-21 seat '
               'after Stefanik exited gubernatorial race + Congress.'),
        sources=['https://ballotpedia.org/Robert_Smullen',
                 'https://ballotpedia.org/New_York%27s_21st_Congressional_District_election,_2026'],
        profile_extra={'background': 'NY State Assembly. Marine Corps veteran.'},
    ),
    placeholder('Anthony Constantino', 'anthony-constantino', 'NY', 21, 'R', '2026-06-23', 'Stefanik seat (business owner)'),
    placeholder('Allen Caruso', 'allen-caruso', 'NY', 21, 'R', '2026-06-23', 'Stefanik seat'),
    placeholder('Blake Gendebien', 'blake-gendebien', 'NY', 21, 'D', '2026-06-23', 'Stefanik seat (dairy farmer)'),
    placeholder('Stuart Amoriell', 'stuart-amoriell', 'NY', 21, 'D', '2026-06-23', 'Stefanik seat (Lake Placid business owner)'),
    placeholder('Dylan Hewitt', 'dylan-hewitt-ny-21', 'NY', 21, 'D', '2026-06-23', 'Stefanik seat'),
]

# ════════════════════════════════════════════════════════════════════════
# CA-48 (Issa R retiring; CA jungle primary 6/2)
# R: Jim Desmond (Issa-endorsed, SD County Supervisor) — only major R
# D: Marni von Wilpert, Ammar Campa-Najjar (2018+2020 nominee), Brandon Riker, +others
# ════════════════════════════════════════════════════════════════════════
CA48 = [
    make_record(
        name='Jim Desmond', slug='jim-desmond', state='CA', district=48,
        office='U.S. Representative CA-48 (2026 R Candidate · Issa-seat open · Issa-endorsed)',
        party='R', archetype='maga_conservative_r',
        primary_date='2026-06-02',
        notes=('San Diego County Supervisor. Endorsed by retiring Rep. Darrell Issa. '
               'Only major R in the CA-48 jungle primary after Issa\'s announcement. '
               'District redrawn by 2024 Prop 50 — now more competitive.'),
        sources=['https://ballotpedia.org/Jim_Desmond',
                 'https://timesofsandiego.com/politics/2026/03/06/desmond-issa-48th-district-reelection-retirement/'],
        profile_extra={'background': 'San Diego County Supervisor. Former mayor of San Marcos.'},
    ),
    placeholder('Marni von Wilpert', 'marni-von-wilpert', 'CA', 48, 'D', '2026-06-02', 'Issa seat (SD City Councilmember)'),
    placeholder('Ammar Campa-Najjar', 'ammar-campa-najjar', 'CA', 48, 'D', '2026-06-02', 'Issa seat (2x prior nominee)'),
    placeholder('Brandon Riker', 'brandon-riker', 'CA', 48, 'D', '2026-06-02', 'Issa seat (Palm Springs businessman)'),
    placeholder('Nicholas Davis', 'nicholas-davis-ca-48', 'CA', 48, 'D', '2026-06-02', 'Issa seat'),
    placeholder('Anuj Dixit', 'anuj-dixit', 'CA', 48, 'D', '2026-06-02', 'Issa seat'),
    placeholder('Marc Iannarino', 'marc-iannarino', 'CA', 48, 'D', '2026-06-02', 'Issa seat'),
    placeholder('Curtis Morrison', 'curtis-morrison', 'CA', 48, 'D', '2026-06-02', 'Issa seat'),
    placeholder('Brian Nash', 'brian-nash-ca-48', 'CA', 48, 'D', '2026-06-02', 'Issa seat'),
    placeholder('Jerlilia Ryans', 'jerlilia-ryans', 'CA', 48, 'D', '2026-06-02', 'Issa seat'),
    placeholder('Whitney Shanahan', 'whitney-shanahan', 'CA', 48, 'D', '2026-06-02', 'Issa seat'),
    placeholder('Suzanne Till', 'suzanne-till', 'CA', 48, 'D', '2026-06-02', 'Issa seat'),
    placeholder('Mike Bucy', 'mike-bucy', 'CA', 48, 'NPP', '2026-06-02', 'Issa seat (No Party Pref)'),
    placeholder('Albert James Mora', 'albert-james-mora', 'CA', 48, 'NPP', '2026-06-02', 'Issa seat (No Party Pref)'),
]

# ════════════════════════════════════════════════════════════════════════
# MT-01 (Zinke R retiring; primary 6/2)
# R: Aaron Flint (radio host), Al Olszewski (former state legislator)
# D: Ryan Busse (former gun industry exec), Matt Rains, Sam Forstag, Russ Cleveland
# ════════════════════════════════════════════════════════════════════════
MT01 = [
    make_record(
        name='Aaron Flint', slug='aaron-flint', state='MT', district=1,
        office='U.S. Representative MT-01 (2026 R Candidate · Zinke-seat open · radio host)',
        party='R', archetype='maga_conservative_r',
        primary_date='2026-06-02',
        notes=('Conservative talk radio host (Voices of Montana). U.S. Air Force veteran. '
               'Announced hours after Zinke\'s retirement.'),
        sources=['https://ballotpedia.org/Aaron_Flint',
                 'https://dailymontanan.com/2026/03/04/zinkes-out-everyones-piling-in-whats-next-for-montanas-1st-congressional-district/'],
        profile_extra={'background': 'Conservative talk radio host. Air Force veteran.'},
    ),
    make_record(
        name='Al Olszewski', slug='al-olszewski', state='MT', district=1,
        office='U.S. Representative MT-01 (2026 R Candidate · Zinke-seat open · former state legislator)',
        party='R', archetype='maga_conservative_r',
        primary_date='2026-06-02',
        notes=('Former Kalispell-area state legislator and orthopedic surgeon. Prior R '
               'primary candidate for MT Governor (2020) and US Senate (2022). Conservative '
               'firebrand.'),
        sources=['https://ballotpedia.org/Al_Olszewski'],
        profile_extra={'background': 'Orthopedic surgeon. Former MT state legislator. '
                                     'Prior R primary candidate for Governor + US Senate.'},
    ),
    make_record(
        name='Ryan Busse', slug='ryan-busse', state='MT', district=1,
        office='U.S. Representative MT-01 (2026 D Candidate · Zinke-seat open · 2024 MT Gov nominee)',
        party='D', archetype='establishment_d',
        primary_date='2026-06-02',
        notes=('Former firearms industry executive turned gun-control advocate (left Kimber '
               'Manufacturing). 2024 D nominee for Montana Governor (lost to Gianforte). '
               'Author of "Gunfight."'),
        sources=['https://ballotpedia.org/Ryan_Busse'],
        profile_extra={'background': 'Former firearms industry executive (Kimber). Gun-control advocate. '
                                     '2024 D nominee for MT Governor. Author of "Gunfight" (2021).'},
    ),
    placeholder('Matt Rains', 'matt-rains-mt-01', 'MT', 1, 'D', '2026-06-02', 'Zinke seat (rancher, West Point grad)'),
    placeholder('Sam Forstag', 'sam-forstag', 'MT', 1, 'D', '2026-06-02', 'Zinke seat (smokejumper)'),
    placeholder('Russ Cleveland', 'russ-cleveland', 'MT', 1, 'D', '2026-06-02', 'Zinke seat (rancher/small-biz owner)'),
]

# ════════════════════════════════════════════════════════════════════════
# AZ-01 (Schweikert R running Gov; primary 7/21)
# Massive 9R + 12D field
# ════════════════════════════════════════════════════════════════════════
AZ01 = [
    make_record(
        name='Gina Swoboda', slug='gina-swoboda', state='AZ', district=1,
        office='U.S. Representative AZ-01 (2026 R Candidate · Schweikert-seat open · AZ GOP Chair)',
        party='R', archetype='maga_conservative_r',
        primary_date='2026-07-21',
        notes=('Arizona Republican Party Chairwoman. R primary candidate for the open AZ-01 '
               'seat after Schweikert announced gubernatorial bid.'),
        sources=['https://ballotpedia.org/Gina_Swoboda'],
        profile_extra={'background': 'Arizona Republican Party Chairwoman.'},
    ),
    make_record(
        name='Shawnna Bolick', slug='shawnna-bolick', state='AZ', district=1,
        office='U.S. Representative AZ-01 (2026 R Candidate · Schweikert-seat open · state senator)',
        party='R', archetype='maga_conservative_r',
        primary_date='2026-07-21',
        notes='AZ state senator. R primary candidate for AZ-01.',
        sources=['https://ballotpedia.org/Shawnna_Bolick'],
        profile_extra={'background': 'Arizona state senator. Former state representative.'},
    ),
    placeholder('Joseph Chaplik', 'joseph-chaplik', 'AZ', 1, 'R', '2026-07-21', 'Schweikert seat (former state rep)'),
    placeholder('Jay Feely', 'jay-feely', 'AZ', 1, 'R', '2026-07-21', 'Schweikert seat (CBS analyst, ex-NFL)'),
    placeholder('Thomas Galvin', 'thomas-galvin', 'AZ', 1, 'R', '2026-07-21', 'Schweikert seat (Maricopa BOS chair)'),
    placeholder('Alexander Kolodin', 'alexander-kolodin', 'AZ', 1, 'R', '2026-07-21', 'Schweikert seat (state rep)'),
    placeholder('Michelle Ugenti-Rita', 'michelle-ugenti-rita', 'AZ', 1, 'R', '2026-07-21', 'Schweikert seat (former state sen)'),
    placeholder('John Trobough', 'john-trobough', 'AZ', 1, 'R', '2026-07-21', 'Schweikert seat'),
    placeholder('Amish Shah', 'amish-shah', 'AZ', 1, 'D', '2026-07-21', 'Schweikert seat (2024 D nominee)'),
    placeholder('Marlene Galan Woods', 'marlene-galan-woods', 'AZ', 1, 'D', '2026-07-21', 'Schweikert seat (2024 D 3rd)'),
    placeholder('Mark Robert Gordon', 'mark-robert-gordon', 'AZ', 1, 'D', '2026-07-21', 'Schweikert seat (atty)'),
    placeholder('Jonathan Treble', 'jonathan-treble', 'AZ', 1, 'D', '2026-07-21', 'Schweikert seat (entrepreneur)'),
    placeholder('Brian Del Vecchio', 'brian-del-vecchio', 'AZ', 1, 'D', '2026-07-21', 'Schweikert seat (admin law judge)'),
    placeholder('Rick McCartney', 'rick-mccartney-az-01', 'AZ', 1, 'D', '2026-07-21', 'Schweikert seat (businessman)'),
]

# ════════════════════════════════════════════════════════════════════════
# MI-10 (James R running Gov; primary 8/4)
# R: Casey Armitage, Robert Lulgjuraj
# D: Tim Greimel (Pontiac mayor, ex-state House leader), Christina Hines (ex-prosecutor), +others
# ════════════════════════════════════════════════════════════════════════
MI10 = [
    make_record(
        name='Tim Greimel', slug='tim-greimel', state='MI', district=10,
        office='U.S. Representative MI-10 (2026 D Candidate · James-seat open · Pontiac Mayor)',
        party='D', archetype='establishment_d',
        primary_date='2026-08-04',
        notes=('Mayor of Pontiac, Michigan. Former Michigan House Democratic Leader. '
               'D primary candidate for the open MI-10 seat after James left to run for Governor.'),
        sources=['https://ballotpedia.org/Tim_Greimel'],
        profile_extra={'background': 'Mayor of Pontiac, MI. Former Michigan House Democratic Leader.'},
    ),
    placeholder('Christina Hines', 'christina-hines', 'MI', 10, 'D', '2026-08-04', 'James seat (former prosecutor)'),
    placeholder('Tripp Adams', 'tripp-adams', 'MI', 10, 'D', '2026-08-04', 'James seat'),
    placeholder('Eric Chung', 'eric-chung-mi-10', 'MI', 10, 'D', '2026-08-04', 'James seat'),
    placeholder('Brian Steven Jaye', 'brian-steven-jaye', 'MI', 10, 'D', '2026-08-04', 'James seat'),
    placeholder('Casey Armitage', 'casey-armitage', 'MI', 10, 'R', '2026-08-04', 'James seat (MI Open Carry President)'),
    placeholder('Robert Lulgjuraj', 'robert-lulgjuraj', 'MI', 10, 'R', '2026-08-04', 'James seat (former Macomb prosecutor)'),
]

# ════════════════════════════════════════════════════════════════════════
# SC-01 (Mace R running Gov; primary 6/9, runoff 6/23)
# 10R + 4D field
# ════════════════════════════════════════════════════════════════════════
SC01 = [
    make_record(
        name='Mark Smith', slug='mark-smith-sc-01', state='SC', district=1,
        office='U.S. Representative SC-01 (2026 R Candidate · Mace-seat open · state legislator)',
        party='R', archetype='maga_conservative_r',
        primary_date='2026-06-09',
        notes=('SC state representative from Daniel Island. Only sitting state legislator '
               'in the SC-01 R primary field of 10. Funeral home operator.'),
        sources=['https://ballotpedia.org/Mark_Smith_(South_Carolina)'],
        profile_extra={'background': 'SC State Representative. Funeral home operator. Daniel Island.'},
    ),
    placeholder('Dan Brown', 'dan-brown-sc-01', 'SC', 1, 'R', '2026-06-09', 'Mace seat'),
    placeholder('Jay Byars', 'jay-byars', 'SC', 1, 'R', '2026-06-09', 'Mace seat (county councilmember)'),
    placeholder('Logan Cunningham', 'logan-cunningham', 'SC', 1, 'R', '2026-06-09', 'Mace seat (county councilmember)'),
    placeholder('Tyler Dykes', 'tyler-dykes', 'SC', 1, 'R', '2026-06-09', 'Mace seat'),
    placeholder('Jack Ellison', 'jack-ellison', 'SC', 1, 'R', '2026-06-09', 'Mace seat'),
    placeholder('Jenny Costa Honeycutt', 'jenny-costa-honeycutt', 'SC', 1, 'R', '2026-06-09', 'Mace seat (county councilmember)'),
    placeholder('Sam McCown', 'sam-mccown', 'SC', 1, 'R', '2026-06-09', 'Mace seat'),
    placeholder('Justin Myers', 'justin-myers-sc-01', 'SC', 1, 'R', '2026-06-09', 'Mace seat'),
    placeholder('Alex Pelbath', 'alex-pelbath', 'SC', 1, 'R', '2026-06-09', 'Mace seat'),
    placeholder('Mac Deford', 'mac-deford', 'SC', 1, 'D', '2026-06-09', 'Mace seat'),
    placeholder('Max Diaz', 'max-diaz-sc-01', 'SC', 1, 'D', '2026-06-09', 'Mace seat'),
    placeholder('Matt Fulmer', 'matt-fulmer', 'SC', 1, 'D', '2026-06-09', 'Mace seat'),
    placeholder('Mayra Rivera-Vázquez', 'mayra-rivera-vazquez', 'SC', 1, 'D', '2026-06-09', 'Mace seat'),
]

# ════════════════════════════════════════════════════════════════════════
# NY-12 (Nadler D retiring; primary 6/23)
# Leading D: Alex Bores, George Conway, Micah Lasher (Nadler-endorsed), Jack Schlossberg
# ════════════════════════════════════════════════════════════════════════
NY12 = [
    make_record(
        name='Micah Lasher', slug='micah-lasher', state='NY', district=12,
        office='U.S. Representative NY-12 (2026 D Candidate · Nadler-seat open · Nadler-endorsed)',
        party='D', archetype='progressive_d',
        primary_date='2026-06-23',
        notes=('NY State Assembly member (elected 2024). Former staffer to Nadler, Bloomberg, '
               'and Hochul. Widely seen as Nadler\'s heir apparent. Endorsed by Nadler '
               'February 9, 2026.'),
        sources=['https://ballotpedia.org/Micah_Lasher'],
        profile_extra={'background': 'NY State Assembly. Former staffer to Rep. Nadler, Mayor '
                                     'Bloomberg, and Gov. Hochul. Nadler\'s endorsed successor.'},
    ),
    make_record(
        name='Jack Schlossberg', slug='jack-schlossberg', state='NY', district=12,
        office='U.S. Representative NY-12 (2026 D Candidate · Nadler-seat open · JFK grandson)',
        party='D', archetype='progressive_d',
        primary_date='2026-06-23',
        notes=('Grandson of President John F. Kennedy. Vogue political commentator. '
               'Public-facing Democratic activist. D primary candidate for NY-12.'),
        sources=['https://ballotpedia.org/Jack_Schlossberg', 'https://en.wikipedia.org/wiki/Jack_Schlossberg'],
        profile_extra={'background': 'Grandson of President John F. Kennedy and Caroline Kennedy. '
                                     'Vogue political commentator. Harvard JD + MBA.'},
    ),
    make_record(
        name='George Conway', slug='george-conway-ny-12', state='NY', district=12,
        office='U.S. Representative NY-12 (2026 D Candidate · Nadler-seat open · ex-R Trump critic)',
        party='D', archetype='establishment_d',
        primary_date='2026-06-23',
        notes=('Former Republican attorney. Co-founder of The Lincoln Project. Ex-husband of '
               'Trump 2016 campaign manager Kellyanne Conway. Switched to D for 2026 NY-12 run. '
               'Age 62.'),
        sources=['https://ballotpedia.org/George_Conway'],
        profile_extra={'background': 'Conservative attorney turned anti-Trump activist. '
                                     'Co-founder Lincoln Project. Former Republican; D candidate 2026.'},
    ),
    make_record(
        name='Alex Bores', slug='alex-bores', state='NY', district=12,
        office='U.S. Representative NY-12 (2026 D Candidate · Nadler-seat open · state assemblyman)',
        party='D', archetype='progressive_d',
        primary_date='2026-06-23',
        notes=('NY State Assembly member (elected 2022). Former software engineer + manager.'),
        sources=['https://ballotpedia.org/Alex_Bores'],
        profile_extra={'background': 'NY State Assembly (2023-). Former software engineer/manager.'},
    ),
    placeholder('Laura Dunn', 'laura-dunn-ny-12', 'NY', 12, 'D', '2026-06-23', 'Nadler seat'),
    placeholder('Nina Schwalbe', 'nina-schwalbe', 'NY', 12, 'D', '2026-06-23', 'Nadler seat'),
    placeholder('Chris Diep', 'chris-diep', 'NY', 12, 'D', '2026-06-23', 'Nadler seat'),
    placeholder('Patrick Timmins', 'patrick-timmins', 'NY', 12, 'D', '2026-06-23', 'Nadler seat'),
    placeholder('Micah Bergdale', 'micah-bergdale', 'NY', 12, 'D', '2026-06-23', 'Nadler seat'),
]

# ════════════════════════════════════════════════════════════════════════
# CA-11 (Pelosi D retiring; jungle primary 6/2)
# D field: Saikat Chakrabarti, Connie Chan (Pelosi-endorsed), Scott Wiener (CA Dem Party endorsed)
# R: David Ganezer (token)
# ════════════════════════════════════════════════════════════════════════
CA11 = [
    make_record(
        name='Connie Chan', slug='connie-chan-ca-11', state='CA', district=11,
        office='U.S. Representative CA-11 (2026 D Candidate · Pelosi-seat open · Pelosi-endorsed)',
        party='D', archetype='progressive_d',
        primary_date='2026-06-02',
        notes=('San Francisco Supervisor. Endorsed by Nancy Pelosi to succeed her in CA-11. '
               'Progressive Asian-American Democrat representing SF\'s Richmond district.'),
        sources=['https://ballotpedia.org/Connie_Chan',
                 'https://thehill.com/homenews/campaign/5884230-pelosi-endorses-connie-chan/'],
        profile_extra={'background': 'San Francisco Board of Supervisors. Richmond district '
                                     '(Sunset/Avenues). Pelosi\'s endorsed successor.'},
    ),
    make_record(
        name='Scott Wiener', slug='scott-wiener-ca-11', state='CA', district=11,
        office='U.S. Representative CA-11 (2026 D Candidate · Pelosi-seat open · CA State Senator · CADP-endorsed)',
        party='D', archetype='progressive_d',
        primary_date='2026-06-02',
        notes=('California State Senator (elected 2016). Former SF Supervisor. Endorsed by '
               'California Democratic Party. Prominent YIMBY + LGBTQ+ activist legislator.'),
        sources=['https://ballotpedia.org/Scott_Wiener'],
        profile_extra={'background': 'California State Senator. Former SF Supervisor. YIMBY + LGBTQ+ activist.'},
    ),
    make_record(
        name='Saikat Chakrabarti', slug='saikat-chakrabarti', state='CA', district=11,
        office='U.S. Representative CA-11 (2026 D Candidate · Pelosi-seat open · ex-Sanders/AOC staffer)',
        party='D', archetype='progressive_d',
        primary_date='2026-06-02',
        notes=('Software engineer. Former chief of staff to Rep. Alexandria Ocasio-Cortez. '
               'Co-founder of Justice Democrats + Brand New Congress. Progressive insurgent.'),
        sources=['https://ballotpedia.org/Saikat_Chakrabarti', 'https://en.wikipedia.org/wiki/Saikat_Chakrabarti'],
        profile_extra={'background': 'Software engineer. Former chief of staff to AOC. '
                                     'Co-founder Justice Democrats. Co-founder Brand New Congress.'},
    ),
    placeholder('Cole Bettles', 'cole-bettles', 'CA', 11, 'D', '2026-06-02', 'Pelosi seat'),
    placeholder('Omed Hamid', 'omed-hamid', 'CA', 11, 'D', '2026-06-02', 'Pelosi seat'),
    placeholder('Darren Helton', 'darren-helton', 'CA', 11, 'D', '2026-06-02', 'Pelosi seat'),
    placeholder('Marie Hurabiell', 'marie-hurabiell', 'CA', 11, 'D', '2026-06-02', 'Pelosi seat'),
    placeholder('Daniel Wheeler', 'daniel-wheeler-ca-11', 'CA', 11, 'D', '2026-06-02', 'Pelosi seat'),
    placeholder('Jingchao Xiong', 'jingchao-xiong', 'CA', 11, 'D', '2026-06-02', 'Pelosi seat'),
    placeholder('David Ganezer', 'david-ganezer', 'CA', 11, 'R', '2026-06-02', 'Pelosi seat (token R)'),
]

ALL_BATCH_1 = NE02 + ME02 + NY21 + CA48 + MT01 + AZ01 + MI10 + SC01 + NY12 + CA11


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
    for rec in ALL_BATCH_1:
        action = upsert(cands, rec)
        if action == 'INSERTED':
            inserts += 1
        else:
            replacements += 1
        d = f'{rec["state"]}-{rec["district"]:02d}'
        by_district.setdefault(d, []).append(rec['name'])

    for d, names in sorted(by_district.items()):
        print(f'  {d}: {len(names)} candidates — {", ".join(names[:3])}{"..." if len(names) > 3 else ""}')

    print(f'\n  INSERTS: {inserts} · REPLACEMENTS: {replacements} (total {len(ALL_BATCH_1)} records)')

    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')
    print(f'Wrote {SCORECARD}')


if __name__ == '__main__':
    main()
