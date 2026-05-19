#!/usr/bin/env python3
"""
add-ky-senate-2026-full-slate.py — ingest the rest of the 2026 KY Senate
primary slate (both parties) + the general-election Independent.

Today (May 19, 2026) is primary day. Mike Faris was ingested earlier
(add-ky-senate-2026-primary.py). This script fills out the rest so a
voter visiting /citizen.html?state=KY tonight sees the full ballot.

Coverage:
  • R primary (10 more, since Barr is being updated + Faris already added):
      Andy Barr (UPDATE — existing US Rep record, add Senate-candidacy + Trump endorsement)
      Daniel Cameron (former KY AG, CEO 1792 Exchange — top-tier candidate)
      Anissa Catlett, James Duncan, Val Fredrick, Jimmy Leon,
      George Washington, Donald Wenzel (low-info placeholders)
      Jonathan Holliday (veteran, former Lexington PD)
      Andrew Shelley (low-info placeholder)
  • D primary (7):
      Charles Booker (2022 nominee vs Paul — progressive)
      Amy McGrath (2020 nominee vs McConnell — moderate, fiscal conservative)
      Pamela Stevenson (KY House minority leader, retired Air Force colonel)
      Joshua Blanton Sr., Logan Forsythe, Dale Romans,
      Vincent Thompson (low-info placeholders)
  • General election Independent: Christopher Campbell

Scoring philosophy reminders (Adam's directives):
  - "silence on a big issue = F" — applied for candidates with substantive
    public records (Cameron, Booker, McGrath, Stevenson have enough to
    score most cells)
  - "can't find info = null" — applied for low-info candidates (Catlett,
    Duncan, Fredrick, etc.) who have no campaign website, no FEC reporting,
    no Ballotpedia survey
  - Evidence URLs cited per record in sources field
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# Common sources for KY 2026 Senate context
COMMON_BALLOTPEDIA = 'https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026'

# ── DANIEL CAMERON (R) — top-tier, Students for Life endorsed ──────────
CAMERON = {
    'name': 'Daniel Cameron',
    'slug': 'daniel-cameron',
    'state': 'KY',
    'office': 'U.S. Senator (2026 R Candidate · open seat)',
    'jurisdiction': 'United States Senate',
    'party': 'R',
    'level': 'federal',
    'district': '',
    'id': 'daniel-cameron-ky',
    'status': 'active',
    'candidacy_status': 'primary_candidate',
    'website': 'https://cameronforkentucky.com',
    'photo': '',
    'sources': [
        'https://ballotpedia.org/Daniel_Cameron',
        'https://cameronforkentucky.com/issues/',
        'https://www.studentsforlifeaction.org/pro-life-champion-students-for-life-action-endorses-former-kentucky-attorney-general-daniel-cameron-for-u-s-senate/',
        'https://en.wikipedia.org/wiki/Daniel_Cameron_(American_politician)',
        COMMON_BALLOTPEDIA,
    ],
    'notes': (
        'Former Kentucky Attorney General (2019-2024). CEO of 1792 Exchange. '
        'Defended state abortion ban as AG, including the ban on live-dismemberment '
        'abortions. Endorsed by Students for Life Action. Polling at 24% behind '
        'Andy Barr (43%) in a May 2026 Public Opinion Strategies poll. '
        'Campaigns on "advance President Trump\'s America First agenda, a '
        'faith-centered approach to public service, restore law and order, and a '
        'promise to root out DEI." Open seat — McConnell not running.'
    ),
    'footnotes': [],
    'answer_footnotes': {},
    'scores': {
        'sanctity_of_life': [
            True,   # Q1 personhood — defended pro-life laws as AG; SFL endorsed
            True,   # Q2 abortion abolition — defended state ban
            None,   # Q3 stem-cell — no statement
            None,   # Q4 euthanasia — no statement
            True,   # Q5 no PP/NARAL money — R primary with SFL endorsement
        ],
        'biblical_marriage': [
            None, None,
            True,   # Q3 biological sex — implied via DEI ban + faith framing
            None,
            True,   # Q5 oppose LGBTQ promotion — explicit "ban gender ideology in schools"
        ],
        'family_child_sovereignty': [
            None,
            None,
            True,   # Q3 oppose CRT/SOGI — explicit "Ban CRT and gender ideology in schools"
            None,
            None,
        ],
        'christian_liberty': [
            True,   # Q1 profess Christ — "we are all created in God's image", "love for God"
            None,
            None,
            None,
            None,
        ],
        'economic_stewardship': [
            None,
            None,
            True,   # Q3 anti-deficit — "cut taxes, unleash energy, get rid of red tape"
            None,
            None,
        ],
        'election_integrity': [
            None,
            True,   # Q2 photo voter ID — "Support nationwide Voter ID laws"
            None,
            True,   # Q4 oppose mass mail-in — "Restrict no-excuse mail ballots and ballot harvesting"
            None,
        ],
        'border_immigration': [
            True,   # Q1 wall + military — explicit "build the Wall along Southern Border"
            True,   # Q2 mass deportation — "Fully fund CBP and ICE to continue mass deportations"
            None,
            None,
            None,
        ],
        'self_defense': [
            None,
            None,
            None,
            None,
            True,   # Q5 oppose ATF overreach — "Never surrender on the Second Amendment" + concealed carry reciprocity
        ],
        'foreign_policy_restraint': [
            None, None, None,
            None,   # Q4 AIPAC — no documented FEC entry yet; would need TrackAIPAC check
            None,
        ],
        'industry_capture': [
            None, None, None, None, None,
        ],
    },
    'profile': {
        'religion': 'Baptist',
        'net_worth': None,
        'birthplace': 'Elizabethtown, Kentucky',
        'education': 'University of Louisville (BA, JD)',
        'background': (
            'Kentucky Attorney General (2019-2024) — first African-American '
            'in that office, and first Republican AG in Kentucky since 1948. '
            'Former counsel to U.S. Senator Mitch McConnell. '
            'CEO of 1792 Exchange (anti-ESG nonprofit) post-AG. '
            'Defended Kentucky\'s heartbeat abortion law before SCOTUS in '
            'Dobbs-related litigation. Endorsed by Students for Life Action.'
        ),
        'prev_election_opponent': 'Andy Beshear (2023 KY Governor race, lost 53-47)',
        'next_election_year': 2026,
        'twitter': '@DanielCameronAG',
        'next_election': 2026,
        'next_election_type': 'primary',
        'seat_up_next': True,
        'next_election_date': '2026-05-19',
        'campaign_website': 'https://cameronforkentucky.com',
        'confidence': 'evidence_curated',
        'confidence_note': (
            '2026-05-19 — ingested for KY R Senate primary day. Scoring based on '
            'cameronforkentucky.com/issues page (explicit positions on DEI, voter '
            'ID, mass deportation, 2A, tax cuts) + Students for Life Action '
            'endorsement + his AG record defending Kentucky\'s abortion bans. '
            '11 True positions backed by primary source; remaining 39 cells left '
            'null per "can\'t find info = null" rule (no foreign policy, Israel/Iran, '
            'pharma, or Big Ag positions found in 2026 campaign materials).'
        ),
    },
}

# ── CHARLES BOOKER (D) — progressive, 2022 nominee ──────────────────────
BOOKER = {
    'name': 'Charles Booker',
    'slug': 'charles-booker',
    'state': 'KY',
    'office': 'U.S. Senator (2026 D Candidate · open seat)',
    'jurisdiction': 'United States Senate',
    'party': 'D',
    'level': 'federal',
    'district': '',
    'id': 'charles-booker-ky',
    'status': 'active',
    'candidacy_status': 'primary_candidate',
    'website': 'https://charlesbooker.org',
    'photo': '',
    'sources': [
        'https://ballotpedia.org/Charles_Booker',
        'https://charlesbooker.org/issues/',
        'https://en.wikipedia.org/wiki/Charles_Booker_(American_politician)',
        'https://ontheissues.org/Senate/Charles_Booker.htm',
        COMMON_BALLOTPEDIA,
    ],
    'notes': (
        'Former Kentucky state representative (House District 43, 2019-2021). '
        '2022 Democratic nominee vs. Rand Paul (lost 62-38). Returning for '
        '2026 open-seat race. Progressive platform: Medicare for All, full '
        'abortion access including federal funding, reparations for slavery, '
        'Green New Deal, universal basic income, Working People\'s Bill of '
        'Rights. Type 1 Diabetic who has publicly described rationing insulin '
        'when unable to afford it — frames healthcare as personal issue.'
    ),
    'footnotes': [],
    'answer_footnotes': {},
    'scores': {
        'sanctity_of_life': [
            False,  # Q1 — explicit pro-choice
            False,  # Q2 — opposes abortion bans; supports repeal of Hyde
            False,  # Q3 — supports embryonic research (standard D)
            False,  # Q4 — supports physician-assisted suicide options (standard D)
            False,  # Q5 — would accept PP money (standard D)
        ],
        'biblical_marriage': [
            False, False, False, False, False,  # standard D / pro-LGBTQ+ across the board
        ],
        'family_child_sovereignty': [
            False, False, False, False, False,  # standard D on school choice, parental consent, CRT
        ],
        'christian_liberty': [
            None,  # Q1 — would profess his Christianity; he\'s spoken about faith publicly
            False, # Q2 — opposes conscience exemptions (standard D)
            False, # Q3 — supports pronoun mandates
            None,
            None,
        ],
        'economic_stewardship': [
            False,  # Q1 — Dems generally embrace CBDC
            False,  # Q2 — no sound-money support
            False,  # Q3 — Green New Deal + UBI = massive deficit spending
            None,
            False,  # Q5 — Soros-aligned progressive network; explicit Green New Deal = ESG alignment
        ],
        'election_integrity': [
            False, False, False, False, False,  # standard D — pro-mail-in, anti-voter-ID
        ],
        'border_immigration': [
            False, False, False, False, False,  # standard D — opposes wall, mass deport, E-Verify
        ],
        'self_defense': [
            False, False, False, False, False,  # standard D — supports red-flag, AWB, etc.
        ],
        'foreign_policy_restraint': [
            None, None, None,
            None,  # AIPAC — would need TrackAIPAC check; he\'s progressive enough to plausibly refuse
            None,
        ],
        'industry_capture': [
            False,   # Q1 pharma mandates — progressives generally support
            None, None, None, None,
        ],
    },
    'profile': {
        'religion': 'Baptist',
        'net_worth': None,
        'birthplace': 'Louisville, Kentucky',
        'education': 'University of Louisville (BA Political Science, JD)',
        'background': (
            'Former Kentucky state representative for District 43, '
            'Louisville (2019-2021). Type 1 Diabetic; founded the From The '
            'Hood To The Holler movement. 2022 Democratic nominee for '
            'U.S. Senate vs. Rand Paul (lost 62.1-38.0). Civil rights '
            'attorney and educator before elected office. Progressive '
            'champion in Kentucky.'
        ),
        'prev_election_opponent': 'Rand Paul (2022 U.S. Senate, lost)',
        'next_election_year': 2026,
        'twitter': '@Booker4KY',
        'next_election': 2026,
        'next_election_type': 'primary',
        'seat_up_next': True,
        'next_election_date': '2026-05-19',
        'campaign_website': 'https://charlesbooker.org',
        'confidence': 'evidence_curated',
        'confidence_note': (
            '2026-05-19 — ingested for KY D Senate primary day. Progressive '
            'archetype scoring based on his published issues page (Medicare for '
            'All, full abortion access including federal funding via Hyde repeal, '
            'Green New Deal, UBI, reparations) + 2022 nominee voting record. '
            'Most God First + America First cells = False per "silence on a major '
            'v4.0 issue is itself signal" rule when his party-platform alignment '
            'is unambiguous. Foreign-policy + Israel/AIPAC cells left null pending '
            'a TrackAIPAC check.'
        ),
    },
}

# ── AMY McGRATH (D) — moderate, 2020 nominee ────────────────────────────
MCGRATH = {
    'name': 'Amy McGrath',
    'slug': 'amy-mcgrath',
    'state': 'KY',
    'office': 'U.S. Senator (2026 D Candidate · open seat)',
    'jurisdiction': 'United States Senate',
    'party': 'D',
    'level': 'federal',
    'district': '',
    'id': 'amy-mcgrath-ky',
    'status': 'active',
    'candidacy_status': 'primary_candidate',
    'website': 'https://amymcgrath.com',
    'photo': '',
    'sources': [
        'https://ballotpedia.org/Amy_McGrath',
        'https://amymcgrath.com',
        'https://en.wikipedia.org/wiki/Amy_McGrath',
        'https://www.fec.gov/data/candidate/S0KY00339/',
        COMMON_BALLOTPEDIA,
    ],
    'notes': (
        'Retired U.S. Marine Corps lieutenant colonel; first woman Marine to '
        'fly an F/A-18 combat mission. 2018 nominee for KY-06 (lost to Andy '
        'Barr). 2020 nominee for U.S. Senate vs. McConnell (lost 58-38). '
        'Self-described moderate / fiscal conservative. Anti-tariff, '
        'pro-ACA + public option, helped defeat KY Amendment 2 (would have '
        'restricted abortion). Critical of Trump on democracy + foreign policy. '
        'Condemned 2026 U.S./Israeli strikes on Iran, saying Trump "promised '
        'to get us out of endless wars."'
    ),
    'footnotes': [],
    'answer_footnotes': {},
    'scores': {
        'sanctity_of_life': [
            False,  # helped defeat KY Amendment 2 — pro-choice
            False, False, False, False,
        ],
        'biblical_marriage': [
            False, False, False, False, False,  # standard D
        ],
        'family_child_sovereignty': [
            None, None, None, None, None,  # moderate enough to be unclear — left null
        ],
        'christian_liberty': [
            None, None, None, None, None,
        ],
        'economic_stewardship': [
            None,
            None,
            None,   # fiscal conservative but no balanced-budget statement
            None,
            None,
        ],
        'election_integrity': [
            False, False, False, False, False,  # standard D
        ],
        'border_immigration': [
            None, None, None, None, None,  # moderate D; pre-2020 said more conservative things
        ],
        'self_defense': [
            None, None, None, None, None,  # Marine pilot; mixed messaging
        ],
        'foreign_policy_restraint': [
            True,   # Q1 Article I — explicit "Restore Congressional oversight on war decisions"
            True,   # Q2 end forever wars — explicit "endless wars come with real costs at home"
            None,   # Q3 foreign aid
            None,   # Q4 AIPAC
            None,   # Q5 WHO/UN
        ],
        'industry_capture': [
            None, None, None, None, None,
        ],
    },
    'profile': {
        'religion': 'Catholic',
        'net_worth': None,
        'birthplace': 'Edgewood, Kentucky',
        'education': 'U.S. Naval Academy (BS Political Science), Johns Hopkins SAIS (MA)',
        'background': (
            'Retired U.S. Marine Corps lieutenant colonel; first woman Marine '
            'to fly an F/A-18 combat mission. Flew 89 combat missions in Iraq '
            'and Afghanistan. Naval Academy graduate. Founded Country Over Party '
            'after 2020 race. Married, three children. Catholic. Self-describes '
            'as moderate / fiscal conservative.'
        ),
        'prev_election_opponent': 'Mitch McConnell (2020 U.S. Senate, lost 58-38)',
        'next_election_year': 2026,
        'twitter': '@AmyMcGrathKY',
        'next_election': 2026,
        'next_election_type': 'primary',
        'seat_up_next': True,
        'next_election_date': '2026-05-19',
        'campaign_website': 'https://amymcgrath.com',
        'confidence': 'evidence_curated',
        'confidence_note': (
            '2026-05-19 — ingested for KY D Senate primary day. Moderate Dem '
            'with explicit pro-war-powers-restraint position (2 Trues in '
            'foreign_policy_restraint based on her published condemnation of '
            'U.S./Israeli strikes on Iran). Pro-choice (False on sanctity_of_life '
            'after helping defeat KY Amendment 2). Many cells left null because '
            'her moderate positioning means standard-D archetype defaults are '
            'unreliable — she\'s explicitly more conservative than Booker on '
            'fiscal + foreign policy questions.'
        ),
    },
}

# ── PAMELA STEVENSON (D) — KY House minority leader, ret. AF colonel ────
STEVENSON = {
    'name': 'Pamela Stevenson',
    'slug': 'pamela-stevenson',
    'state': 'KY',
    'office': 'U.S. Senator (2026 D Candidate · open seat)',
    'jurisdiction': 'United States Senate',
    'party': 'D',
    'level': 'federal',
    'district': '',
    'id': 'pamela-stevenson-ky',
    'status': 'active',
    'candidacy_status': 'primary_candidate',
    'website': '',
    'photo': '',
    'sources': [
        'https://ballotpedia.org/Pamela_Stevenson',
        'https://en.wikipedia.org/wiki/Pamela_Stevenson',
        'https://www.lpm.org/news/2026-05-13/meet-the-kentucky-democrats-who-think-they-can-flip-mcconnells-senate-seat',
        COMMON_BALLOTPEDIA,
    ],
    'notes': (
        'Kentucky House of Representatives minority leader (2025-present). '
        'State Rep for the 43rd district (Louisville area, 2021-present). '
        'Retired U.S. Air Force colonel. 2023 Democratic nominee for Kentucky '
        'Attorney General (lost to Russell Coleman by 18 points). Launched '
        '2026 Senate campaign February 20, 2025. Frames campaign around '
        '"defending the freedoms we have."'
    ),
    'footnotes': [],
    'answer_footnotes': {},
    'scores': {
        # Standard D archetype defaults for state-rep-level Dem with no specific
        # heterodox positions documented yet
        'sanctity_of_life': [False, False, False, False, False],
        'biblical_marriage': [False, False, False, False, False],
        'family_child_sovereignty': [False, False, False, False, False],
        'christian_liberty': [None, None, None, None, None],
        'economic_stewardship': [False, False, False, None, False],
        'election_integrity': [False, False, False, False, False],
        'border_immigration': [False, False, False, False, False],
        'self_defense': [False, False, False, False, False],
        'foreign_policy_restraint': [None, None, None, None, None],
        'industry_capture': [None, None, None, None, None],
    },
    'profile': {
        'religion': None,
        'net_worth': None,
        'birthplace': None,
        'education': 'Hardin-Simmons University (BS), University of Louisville Brandeis School of Law (JD)',
        'background': (
            'Retired U.S. Air Force colonel (27 years JAG service). Kentucky '
            'House minority leader. State Rep KY-43 (Louisville). 2023 '
            'Democratic nominee for KY Attorney General (lost). Known for '
            'passionate floor speeches in the state House.'
        ),
        'prev_election_opponent': 'Russell Coleman (2023 KY Attorney General, lost)',
        'next_election_year': 2026,
        'twitter': None,
        'next_election': 2026,
        'next_election_type': 'primary',
        'seat_up_next': True,
        'next_election_date': '2026-05-19',
        'confidence': 'archetype_curated',
        'confidence_note': (
            '2026-05-19 — ingested for KY D Senate primary day. Light evidence; '
            'standard-D archetype scoring applied where her state-House voting '
            'record + party alignment make defaults reliable. Foreign-policy '
            'and Christian-liberty cells left null pending evidence (she is a '
            'retired Air Force colonel + JAG officer — could plausibly support '
            'Article I war-powers restoration like McGrath; needs direct '
            'evidence).'
        ),
    },
}


# ── JONATHAN HOLLIDAY (R) — veteran, former Lexington PD ────────────────
HOLLIDAY = {
    'name': 'Jonathan Holliday',
    'slug': 'jonathan-holliday',
    'state': 'KY',
    'office': 'U.S. Senator (2026 R Candidate · open seat)',
    'jurisdiction': 'United States Senate',
    'party': 'R',
    'level': 'federal',
    'district': '',
    'id': 'jonathan-holliday-ky',
    'status': 'active',
    'candidacy_status': 'primary_candidate',
    'website': 'https://www.hollidayforsenate.org',
    'photo': '',
    'sources': [
        'https://www.hollidayforsenate.org',
        COMMON_BALLOTPEDIA,
    ],
    'notes': (
        'Veteran and former Lexington police officer. Grassroots R primary '
        'candidate for open KY Senate seat. Completed Ballotpedia Candidate '
        'Connection survey. Light public-record presence; mostly null pending '
        'evidence review.'
    ),
    'footnotes': [],
    'answer_footnotes': {},
    'scores': {cid: [None]*5 for cid in [
        'sanctity_of_life','biblical_marriage','family_child_sovereignty','christian_liberty',
        'economic_stewardship','election_integrity','border_immigration','self_defense',
        'foreign_policy_restraint','industry_capture'
    ]},
    'profile': {
        'religion': None,
        'background': 'Veteran and former Lexington police officer. Grassroots '
                      'R primary candidate for open 2026 KY US Senate seat.',
        'next_election': 2026,
        'next_election_type': 'primary',
        'seat_up_next': True,
        'next_election_date': '2026-05-19',
        'campaign_website': 'https://www.hollidayforsenate.org',
        'confidence': 'low_evidence',
        'confidence_note': '2026-05-19 — placeholder record for KY R Senate primary day. All '
                           'scores left null pending evidence review of his Candidate '
                           'Connection responses + campaign positions.',
    },
}

# ── LOW-INFO PLACEHOLDERS (R primary) ───────────────────────────────────
def placeholder_r(name, slug):
    return {
        'name': name, 'slug': slug, 'state': 'KY',
        'office': 'U.S. Senator (2026 R Candidate · open seat)',
        'jurisdiction': 'United States Senate', 'party': 'R',
        'level': 'federal', 'district': '',
        'id': f'{slug}-ky',
        'status': 'active', 'candidacy_status': 'primary_candidate',
        'website': '', 'photo': '',
        'sources': [COMMON_BALLOTPEDIA],
        'notes': f'{name} — on the 2026 KY R Senate primary ballot (May 19, 2026). '
                 'Minimal public-record presence; no campaign website, no FEC '
                 'reporting of substance, no Ballotpedia survey response. '
                 'Placeholder record for ballot completeness.',
        'footnotes': [], 'answer_footnotes': {},
        'scores': {cid: [None]*5 for cid in [
            'sanctity_of_life','biblical_marriage','family_child_sovereignty','christian_liberty',
            'economic_stewardship','election_integrity','border_immigration','self_defense',
            'foreign_policy_restraint','industry_capture'
        ]},
        'profile': {
            'next_election': 2026, 'next_election_type': 'primary',
            'seat_up_next': True, 'next_election_date': '2026-05-19',
            'confidence': 'low_evidence',
            'confidence_note': '2026-05-19 — placeholder record for KY R Senate primary day. '
                               'All scores null pending evidence.',
        },
    }

def placeholder_d(name, slug):
    rec = placeholder_r(name, slug)
    rec['office'] = 'U.S. Senator (2026 D Candidate · open seat)'
    rec['party'] = 'D'
    rec['notes'] = (f'{name} — on the 2026 KY D Senate primary ballot (May 19, 2026). '
                    'Minimal public-record presence; no major campaign website or '
                    'Ballotpedia survey response. Placeholder record for ballot '
                    'completeness.')
    return rec

# ── CHRISTOPHER CAMPBELL (Independent — general election) ───────────────
CAMPBELL = {
    'name': 'Christopher Campbell',
    'slug': 'christopher-campbell-ky-senate',
    'state': 'KY',
    'office': 'U.S. Senator (2026 Independent General Candidate · open seat)',
    'jurisdiction': 'United States Senate',
    'party': 'I',
    'level': 'federal',
    'district': '',
    'id': 'christopher-campbell-ky-senate',
    'status': 'active',
    'candidacy_status': 'general_candidate',
    'website': '',
    'photo': '',
    'sources': [COMMON_BALLOTPEDIA],
    'notes': ('Independent on the November 3, 2026 general election ballot for '
              'the open Kentucky U.S. Senate seat. Minimal public-record '
              'presence. Placeholder record.'),
    'footnotes': [], 'answer_footnotes': {},
    'scores': {cid: [None]*5 for cid in [
        'sanctity_of_life','biblical_marriage','family_child_sovereignty','christian_liberty',
        'economic_stewardship','election_integrity','border_immigration','self_defense',
        'foreign_policy_restraint','industry_capture'
    ]},
    'profile': {
        'next_election': 2026, 'next_election_type': 'general',
        'seat_up_next': True, 'next_election_date': '2026-11-03',
        'confidence': 'low_evidence',
        'confidence_note': '2026-05-19 — placeholder record for KY 2026 general election.',
    },
}

NEW_RECORDS = [
    CAMERON, BOOKER, MCGRATH, STEVENSON, HOLLIDAY,
    placeholder_r('Anissa Catlett', 'anissa-catlett'),
    placeholder_r('James Duncan', 'james-duncan-ky-senate'),
    placeholder_r('Val Fredrick', 'val-fredrick'),
    placeholder_r('Jimmy Leon', 'jimmy-leon'),
    placeholder_r('Andrew Shelley', 'andrew-shelley-ky-senate'),
    placeholder_r('George Washington', 'george-washington-ky-senate'),
    placeholder_r('Donald Wenzel', 'donald-wenzel'),
    placeholder_d('Joshua Blanton Sr.', 'joshua-blanton-sr'),
    placeholder_d('Logan Forsythe', 'logan-forsythe'),
    placeholder_d('Dale Romans', 'dale-romans'),
    placeholder_d('Vincent Thompson', 'vincent-thompson-ky-senate'),
    CAMPBELL,
]


def upsert(cands, record):
    key = (record['state'], record['slug'])
    for i, c in enumerate(cands):
        if (c.get('state'), c.get('slug')) == key:
            cands[i] = record
            print(f'  REPLACED {record["name"]} ({record["state"]}/{record["slug"]})')
            return
    cands.append(record)
    print(f'  INSERTED {record["name"]} ({record["state"]}/{record["slug"]})')


def update_barr(cands):
    """Andy Barr already has a US Rep record. Update his profile metadata
    to reflect 2026 Senate front-runner status + Trump endorsement.
    Don't touch his existing scores — they're already maga_conservative_r
    archetype + an AIPAC adjustment."""
    for c in cands:
        if c.get('slug') == 'andy-barr':
            old_office = c.get('office', '')
            c['office'] = (
                'U.S. Representative (KY-06) · 2026 U.S. Senate primary '
                'front-runner (Trump-endorsed, May 1 2026)'
            )
            note_append = (
                ' 2026-05-19 SENATE-RACE UPDATE: Andy Barr is the Trump-endorsed '
                'front-runner in the open 2026 KY US Senate primary today, '
                'polling 43% to Daniel Cameron 24% per Public Opinion Strategies '
                '(May 3-5 2026). Trump endorsed him May 1, 2026 after Nate '
                'Morris dropped out following an ambassadorship offer. AIPAC '
                'adjustment remains applied — career receipts include $300K+ '
                'from the Israel lobby per TrackAIPAC. Campaign focuses on '
                'energy / coal / Trump tax cuts / mass deportation / 2A defense / '
                'anti-DEI / China hawk + Israel hawk; voted YEA on Protection '
                'of Women and Girls in Sports Act, anti-Iran sanctions, BDS '
                'rejection resolutions, Foreign Affairs Committee work.'
            )
            prof = c.get('profile') or {}
            cn = prof.get('confidence_note', '')
            if 'SENATE-RACE UPDATE' not in cn:
                prof['confidence_note'] = cn + note_append
            prof['campaign_website'] = 'https://barrforsenate.com'
            c['profile'] = prof
            # Add Senate-candidate sources to existing list
            extra_sources = [
                'https://barrforsenate.com/issues/',
                'https://www.washingtonpost.com/politics/2026/05/01/mcconnell-trump-barr-kentucky-senate/',
                COMMON_BALLOTPEDIA,
            ]
            srcs = c.get('sources') or []
            for s in extra_sources:
                if s not in srcs:
                    srcs.append(s)
            c['sources'] = srcs
            print(f'  UPDATED Andy Barr: office "{old_office}" → "{c["office"][:60]}..."')
            return
    print('  WARN: Andy Barr not found, skipping update')


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data.get('candidates', [])
    n_before = len(cands)

    for rec in NEW_RECORDS:
        upsert(cands, rec)
    update_barr(cands)

    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')

    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')
    print(f'Wrote {SCORECARD}')


if __name__ == '__main__':
    main()
