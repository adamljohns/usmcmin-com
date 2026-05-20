#!/usr/bin/env python3
"""
add-open-senate-seats-2026.py — ingest the 2026 US Senate slates for the
10 remaining open seats (KY already shipped 2026-05-19).

Open seats this script covers:
  AL — Tuberville running for Governor (R primary May 19 2026 — TODAY)
  IA — Ernst retiring (R+D primary Jun 2 2026)
  IL — Durbin retiring (primary ALREADY HAPPENED Mar 17 — nominees set)
  MI — Peters retiring (R+D primary Aug 4 2026)
  MN — Smith retiring (R+D primary Aug 11 2026)
  MT — Daines retiring (R+D primary Jun 2 2026)
  NC — Tillis retiring (primary ALREADY HAPPENED Mar 3 — nominees set)
  NH — Shaheen retiring (R+D primary Sep 8 2026)
  OK — Mullin appointed DHS Sec / Armstrong interim (R+D primary Jun 16 2026)
  WY — Lummis retiring (R+D primary Aug 18 2026)

Strategy:
  • For incumbents already in DB running for Senate (Hinson, Moore, Stevens,
    Craig, Pappas, Hern, Hageman, Krishnamoorthi, Kelly, Marshall, Stratton,
    Flanagan): UPDATE office field + profile.confidence_note with Senate-race
    metadata (Andy Barr precedent from 2026-05-19 KY commit).
  • For new candidates with substantive published positions: INSERT with
    archetype-based scoring + record-level evidence cites.
  • For low-info challengers (no campaign website, no FEC reporting, no
    Ballotpedia survey): placeholder records with all nulls.

Archetype score templates extend rescore-top-50-federal.py's 6-category
templates to the full 10-category v4.x rubric. Defaults for sanctity_of_life,
biblical_marriage, border_immigration, self_defense follow well-established
caucus patterns; individual overrides where evidence diverges.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None

# ── 10-category archetype templates ──────────────────────────────────
# Extends rescore-top-50-federal.py's 6-cat templates with reasonable
# defaults for sanctity_of_life, biblical_marriage, border_immigration,
# self_defense based on caucus voting patterns.
ARCHETYPES = {
    'maga_conservative_r': {
        'sanctity_of_life':          [T, T, T, T, T],
        'biblical_marriage':         [T, T, T, T, T],
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, N],
        'economic_stewardship':      [T, N, T, N, T],
        'election_integrity':        [N, T, N, T, T],
        'border_immigration':        [T, T, T, T, T],
        'self_defense':              [T, T, T, T, T],
        'foreign_policy_restraint':  [N, N, N, F, N],
        'industry_capture':          [N, N, N, T, N],
    },
    'establishment_r': {
        'sanctity_of_life':          [T, F, T, T, T],   # pro-life but mixed IVF
        'biblical_marriage':         [N, F, T, N, N],   # voted for RFMA = F on Q2
        'family_child_sovereignty':  [N, N, T, N, N],
        'christian_liberty':         [T, N, N, N, N],
        'economic_stewardship':      [N, F, N, N, F],
        'election_integrity':        [F, T, F, F, T],
        'border_immigration':        [T, T, T, T, T],
        'self_defense':              [T, F, F, T, T],   # supports basic 2A but voted for BSCA
        'foreign_policy_restraint':  [F, F, F, F, F],
        'industry_capture':          [F, F, F, N, F],
    },
    'progressive_d': {
        'sanctity_of_life':          [F, F, F, F, F],
        'biblical_marriage':         [F, F, F, F, F],
        'family_child_sovereignty':  [F, F, F, F, F],
        'christian_liberty':         [F, F, F, F, F],
        'economic_stewardship':      [F, F, F, N, T],
        'election_integrity':        [F, F, F, F, F],
        'border_immigration':        [F, F, F, F, F],
        'self_defense':              [F, F, F, F, F],
        'foreign_policy_restraint':  [N, T, N, N, N],
        'industry_capture':          [N, F, T, N, T],
    },
    'establishment_d': {
        'sanctity_of_life':          [F, F, F, F, F],
        'biblical_marriage':         [F, F, F, F, F],
        'family_child_sovereignty':  [F, F, F, F, F],
        'christian_liberty':         [F, F, F, F, F],
        'economic_stewardship':      [F, F, F, F, F],
        'election_integrity':        [F, F, F, F, F],
        'border_immigration':        [F, F, F, F, F],
        'self_defense':              [F, F, F, F, F],
        'foreign_policy_restraint':  [F, F, F, F, F],
        'industry_capture':          [F, F, F, F, F],
    },
    'populist_right': {
        'sanctity_of_life':          [T, T, T, T, T],
        'biblical_marriage':         [T, T, T, T, T],
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, N],
        'economic_stewardship':      [T, N, F, N, T],
        'election_integrity':        [N, T, T, T, T],
        'border_immigration':        [T, T, T, T, T],
        'self_defense':              [T, T, T, T, T],
        'foreign_policy_restraint':  [T, T, T, F, T],
        'industry_capture':          [T, T, T, N, T],
    },
}


def scores_from_archetype(archetype, overrides=None):
    """Return a 10-category scores dict from an archetype, with optional
    per-category overrides (full 5-element list per category)."""
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


def make_record(name, slug, state, office, party, archetype=None, overrides=None,
                primary_date=None, notes='', sources=None, profile_extra=None,
                confidence='archetype_curated', confidence_note='',
                candidacy_status='primary_candidate', level='federal',
                jurisdiction='United States Senate'):
    rec = {
        'name': name, 'slug': slug, 'state': state,
        'office': office, 'jurisdiction': jurisdiction,
        'party': party, 'level': level, 'district': '',
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': candidacy_status,
        'website': (profile_extra or {}).get('campaign_website', ''),
        'photo': '',
        'sources': sources or [],
        'notes': notes, 'footnotes': [], 'answer_footnotes': {},
        'scores': scores_from_archetype(archetype, overrides) if archetype else empty_scores(),
        'profile': {
            'next_election': 2026,
            'next_election_type': 'primary',
            'seat_up_next': True,
            'next_election_date': primary_date or '',
            'confidence': confidence,
            'confidence_note': confidence_note or
                (f'2026-05-19 — ingested for 2026 open Senate seat. '
                 f'Archetype: {archetype}.' if archetype
                 else '2026-05-19 — placeholder for ballot completeness.'),
        },
    }
    if profile_extra:
        rec['profile'].update(profile_extra)
    return rec


def placeholder(name, slug, state, party, primary_date, suffix=''):
    label = 'R' if party == 'R' else ('D' if party == 'D' else 'I')
    office_label = 'open seat' if suffix == '' else suffix
    return make_record(
        name=name, slug=slug, state=state,
        office=f'U.S. Senator (2026 {label} Candidate · {office_label})',
        party=party, archetype=None, primary_date=primary_date,
        notes=(f'{name} — on the 2026 {state} {label} US Senate primary ballot. '
               'Minimal public-record presence. Placeholder record for ballot completeness.'),
        sources=[f'https://ballotpedia.org/United_States_Senate_election_in_{state}_2026'],
        confidence='low_evidence',
    )


# ────────────────────────────────────────────────────────────────────────
# NEW INSERTS — top-tier candidates with archetype scoring
# ────────────────────────────────────────────────────────────────────────

# Mike Rogers (MI) — former US Rep MI-08 (2001-2015), former FBI agent,
# 2024 Senate nominee (lost narrowly to Slotkin), 2026 nominee with $45M SLF
# pledge. Defended Trump on election conspiracies in 2024+2026. NOT the
# Alabama Mike Rogers (different person, already in DB).
ROGERS_MI = make_record(
    name='Mike Rogers',
    slug='mike-rogers-mi-senate',
    state='MI',
    office='U.S. Senator (2026 R Candidate · Peters seat)',
    party='R',
    archetype='establishment_r',
    overrides={
        # Rogers said he won't change MI's 2022 abortion-rights amendment —
        # "left to the states". That's NOT the same as voting to restrict
        # at the federal level. Treat as N (no federal-vote evidence yet).
        'sanctity_of_life': [N, N, N, N, N],
        # Trump-endorsed for 2024 + 2026 → MAGA-aligned on most issues
        'border_immigration': [T, T, T, T, T],
        'self_defense': [T, T, T, T, T],
    },
    primary_date='2026-08-04',
    notes=('Former U.S. Representative MI-08 (2001-2015). Former Army officer + '
           'FBI special agent (organized crime, Chicago). 2024 R Senate nominee, '
           'lost narrowly to Elissa Slotkin. 2026 R Senate nominee for Peters '
           'open seat, backed by Senate Leadership Fund ($45M outside spending). '
           'Has supported Trump tariffs; voted against Medicare drug-price '
           'negotiation; favors states-rights framing on abortion (will not '
           'attempt to change MI 2022 amendment). Endorsed by Trump.'),
    sources=[
        'https://ballotpedia.org/Mike_Rogers_(Michigan)',
        'https://rogersforsenate.com/',
        'https://en.wikipedia.org/wiki/Mike_Rogers_(Michigan_politician)',
    ],
    profile_extra={
        'religion': 'Christian',
        'background': ('Former U.S. Representative MI-08. Former Army officer '
                       '+ FBI special agent. House Intelligence Committee chair '
                       '(2011-2015). Radio host post-Congress. 2024 + 2026 KY '
                       '[sic] Senate nominee. Trump-endorsed.'),
        'campaign_website': 'https://rogersforsenate.com',
        'next_election_year': 2026,
    },
    confidence_note=('2026-05-19 — establishment_r archetype with Trump-MAGA '
                     'border/2A overrides. Sanctity_of_life all null pending '
                     'federal-vote evidence (his 2024+2026 trail emphasizes '
                     'states-rights framing, not federal abortion restrictions).'),
)

# Mallory McMorrow (MI) — progressive D state senator, viral 2022 anti-CRT
# floor speech opposing GOP attacks
MCMORROW = make_record(
    name='Mallory McMorrow',
    slug='mallory-mcmorrow',
    state='MI',
    office='U.S. Senator (2026 D Candidate · Peters seat)',
    party='D',
    archetype='progressive_d',
    primary_date='2026-08-04',
    notes=('Michigan state senator (District 11, Royal Oak area, 2019-present). '
           'Gained national attention for 2022 floor speech rebuking GOP '
           'attacks linking pro-LGBTQ+ Democrats to "groomer" smears. 2026 '
           'D Senate candidate framing campaign as "call for change in the '
           'Democratic Party."'),
    sources=[
        'https://ballotpedia.org/Mallory_McMorrow',
        'https://en.wikipedia.org/wiki/Mallory_McMorrow',
    ],
    profile_extra={
        'religion': 'Catholic',
        'background': ('Michigan state senator. Industrial designer prior '
                       'to politics. Viral 2022 floor speech rebuking GOP '
                       'anti-LGBTQ+ rhetoric.'),
        'next_election_year': 2026,
    },
)

# Abdul El-Sayed (MI) — progressive D, physician, Bernie Sanders-aligned
EL_SAYED = make_record(
    name='Abdul El-Sayed',
    slug='abdul-el-sayed',
    state='MI',
    office='U.S. Senator (2026 D Candidate · Peters seat)',
    party='D',
    archetype='progressive_d',
    primary_date='2026-08-04',
    notes=('Physician + former Wayne County health director. 2018 D '
           'gubernatorial candidate (lost primary to Gretchen Whitmer). '
           'Bernie Sanders-aligned progressive. 2026 D Senate candidate.'),
    sources=[
        'https://ballotpedia.org/Abdul_El-Sayed',
        'https://en.wikipedia.org/wiki/Abdul_El-Sayed',
    ],
    profile_extra={
        'religion': 'Muslim',
        'background': ('Physician (Rhodes Scholar). Former Wayne County '
                       'health director. 2018 MI gubernatorial primary '
                       'candidate. Progressive activist + Sanders surrogate.'),
        'next_election_year': 2026,
    },
)

# Joe Tate (MI) — former MI House Speaker, state rep
TATE = make_record(
    name='Joe Tate',
    slug='joe-tate-mi-senate',
    state='MI',
    office='U.S. Senator (2026 D Candidate · Peters seat)',
    party='D',
    archetype='establishment_d',
    primary_date='2026-08-04',
    notes=('Former Speaker of the Michigan House of Representatives (2023-'
           '2024) — first Black Speaker in Michigan history. Current state '
           'representative. Marine Corps veteran. NFL alumni (Atlanta Falcons '
           'practice squad).'),
    sources=[
        'https://ballotpedia.org/Joe_Tate',
    ],
    profile_extra={
        'religion': None,
        'background': ('Marine Corps veteran. Former NFL practice-squad '
                       'player. Former Speaker of Michigan House (first '
                       'Black Speaker).'),
        'next_election_year': 2026,
    },
)

# Michael Whatley (NC) — won R primary 64.6%, former RNC chair, Trump-endorsed
WHATLEY = make_record(
    name='Michael Whatley',
    slug='michael-whatley',
    state='NC',
    office='U.S. Senator (2026 R Nominee · Tillis seat)',
    party='R',
    archetype='maga_conservative_r',
    primary_date='2026-03-03',
    notes=('Former Republican National Committee chair (2024-2025). NC R '
           'Senate nominee — won March 3 2026 primary with 64.6% over author '
           'Don Brown. Trump-endorsed front-runner throughout. Former NC GOP '
           'chair. Will face former Governor Roy Cooper (D) in November.'),
    sources=[
        'https://ballotpedia.org/Michael_Whatley',
        'https://en.wikipedia.org/wiki/Michael_Whatley',
        'https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_North_Carolina',
    ],
    profile_extra={
        'religion': 'Christian',
        'background': ('Former RNC chair (2024-2025). Former NC GOP chair. '
                       'Energy industry attorney. Trump-endorsed for Senate.'),
        'next_election_year': 2026,
        'next_election_type': 'general',
        'next_election_date': '2026-11-03',
    },
    candidacy_status='general_candidate',
    confidence_note=('2026-05-19 — maga_conservative_r archetype. Trump-endorsed '
                     'RNC chair = solid MAGA-aligned scoring. Won R primary '
                     'decisively (64.6% over Don Brown).'),
)

# Roy Cooper (NC) — D nominee, former 2-term governor, won D primary 92%
COOPER_NC = make_record(
    name='Roy Cooper',
    slug='roy-cooper-nc-senate',
    state='NC',
    office='U.S. Senator (2026 D Nominee · Tillis seat)',
    party='D',
    archetype='establishment_d',
    primary_date='2026-03-03',
    notes=('Former Governor of North Carolina (2017-2025). Former NC Attorney '
           'General (2001-2017). 2026 D Senate nominee — won March 3 primary '
           'with 92% after Wiley Nickel withdrew + endorsed him. Will face '
           'Michael Whatley (R) in November. Top D pickup target for 2026.'),
    sources=[
        'https://ballotpedia.org/Roy_Cooper',
        'https://en.wikipedia.org/wiki/Roy_Cooper',
    ],
    profile_extra={
        'religion': 'Baptist',
        'background': ('Former 2-term Governor of North Carolina (2017-2025). '
                       'Former Attorney General (2001-2017). Long-time NC '
                       'Democratic establishment figure. Vetoed multiple '
                       'state abortion + LGBTQ-restriction bills as governor.'),
        'next_election_year': 2026,
        'next_election_type': 'general',
        'next_election_date': '2026-11-03',
    },
    candidacy_status='general_candidate',
    confidence_note=('2026-05-19 — establishment_d archetype. As governor, '
                     'vetoed pro-life + parental-rights + anti-LGBTQ-promotion '
                     'bills — consistent with D archetype defaults.'),
)

# Don Tracy (IL) — won R primary 40%, former IL GOP chair
TRACY = make_record(
    name='Don Tracy',
    slug='don-tracy',
    state='IL',
    office='U.S. Senator (2026 R Nominee · Durbin seat)',
    party='R',
    archetype='establishment_r',
    primary_date='2026-03-17',
    notes=('Former Illinois Republican Party chair. Springfield attorney. '
           'Won R primary March 17 2026 with 40% over Jeannie Evans + Casey '
           'Chlebek. Will face Lt. Gov. Juliana Stratton (D) in November.'),
    sources=[
        'https://ballotpedia.org/Don_Tracy',
    ],
    profile_extra={
        'religion': None,
        'background': ('Former IL Republican Party chair. Attorney based '
                       'in Springfield, IL.'),
        'next_election_year': 2026,
        'next_election_type': 'general',
        'next_election_date': '2026-11-03',
    },
    candidacy_status='general_candidate',
)

# Kurt Alme (MT) — R primary front-runner, former US Attorney
ALME = make_record(
    name='Kurt Alme',
    slug='kurt-alme',
    state='MT',
    office='U.S. Senator (2026 R Candidate · Daines seat)',
    party='R',
    archetype='maga_conservative_r',
    primary_date='2026-06-02',
    notes=('Former U.S. Attorney for Montana. Endorsed by Trump + Sen. Tim '
           'Sheehy + Gov. Greg Gianforte + retiring Sen. Steve Daines. '
           'Daines withdrew minutes before filing deadline and immediately '
           'endorsed Alme. Lee Calhoun + Charles Walking Child are the other '
           'two R primary candidates.'),
    sources=[
        'https://ballotpedia.org/United_States_Senate_election_in_Montana,_2026',
        'https://montanafreepress.org/2026/03/04/republican-u-s-senate-steve-daines-withdraws/',
    ],
    profile_extra={
        'religion': None,
        'background': ('Former U.S. Attorney for District of Montana. '
                       'Trump-endorsed front-runner backed by entire MT '
                       'GOP establishment for open Daines seat.'),
        'next_election_year': 2026,
    },
)

# John E. Sununu (NH) — former R Sen, governor's son
SUNUNU_NH = make_record(
    name='John E. Sununu',
    slug='john-sununu',
    state='NH',
    office='U.S. Senator (2026 R Candidate · Shaheen seat)',
    party='R',
    archetype='establishment_r',
    primary_date='2026-09-08',
    notes=('Former U.S. Senator from New Hampshire (2003-2009). Former U.S. '
           'Representative NH-01 (1997-2003). Son of former NH Governor + '
           'White House Chief of Staff John H. Sununu. Brother of former NH '
           'Governor Chris Sununu. 2026 R Senate primary front-runner '
           'against former MA Senator Scott Brown.'),
    sources=[
        'https://ballotpedia.org/John_E._Sununu',
        'https://en.wikipedia.org/wiki/John_E._Sununu',
    ],
    profile_extra={
        'religion': 'Catholic',
        'background': ('Former U.S. Senator (2003-2009). Former U.S. '
                       'Representative NH-01. Son + brother of NH '
                       'governors. Establishment Republican.'),
        'next_election_year': 2026,
    },
)

# Scott Brown (NH) — former MA Sen, 2014 NH Sen candidate (lost to Shaheen)
BROWN_NH = make_record(
    name='Scott Brown',
    slug='scott-brown-nh-senate',
    state='NH',
    office='U.S. Senator (2026 R Candidate · Shaheen seat)',
    party='R',
    archetype='establishment_r',
    primary_date='2026-09-08',
    notes=('Former U.S. Senator from Massachusetts (2010-2013), won '
           'Ted Kennedy seat in special election. Lost 2014 NH Senate race '
           'to Jeanne Shaheen 51-48. Former U.S. Ambassador to New Zealand '
           '+ Samoa under Trump (2017-2020). Returning for 2026 NH open seat.'),
    sources=[
        'https://ballotpedia.org/Scott_Brown',
        'https://en.wikipedia.org/wiki/Scott_Brown_(politician)',
    ],
    profile_extra={
        'religion': 'Christian',
        'background': ('Former U.S. Senator MA (2010-2013) — won Kennedy '
                       'seat. Former U.S. Ambassador to NZ + Samoa under '
                       'Trump. Lost 2014 NH Senate to Shaheen.'),
        'next_election_year': 2026,
    },
)

# Royce White (MN) — R, former NBA player, 2024 nominee against Klobuchar
WHITE_MN = make_record(
    name='Royce White',
    slug='royce-white',
    state='MN',
    office='U.S. Senator (2026 R Candidate · Smith seat)',
    party='R',
    archetype='populist_right',
    primary_date='2026-08-11',
    notes=('Former NBA player (Houston Rockets 1st-round draft pick, 2012). '
           '2024 Minnesota R Senate nominee against Amy Klobuchar (lost 56-39). '
           'Right-wing podcaster + activist. Vocal anti-globalist, anti-WEF, '
           'anti-CBDC, anti-AIPAC positions. 2026 R primary candidate for '
           'Smith open seat.'),
    sources=[
        'https://ballotpedia.org/Royce_White',
        'https://en.wikipedia.org/wiki/Royce_White',
    ],
    profile_extra={
        'religion': 'Muslim',
        'background': ('Former NBA player + mental-health activist. '
                       'Right-wing podcaster. 2024 R Senate nominee in MN. '
                       'Vocal anti-WEF, anti-CBDC, anti-AIPAC, anti-Israel-'
                       'lobby positions.'),
        'next_election_year': 2026,
    },
    confidence_note=('2026-05-19 — populist_right archetype with anti-AIPAC + '
                     'explicit foreign-policy-restraint signal (his public '
                     'positions are aggressively anti-Israel-lobby + '
                     'pro-Article-I — overrides the AIPAC F default).'),
    overrides={
        'foreign_policy_restraint': [T, T, T, T, T],  # explicit anti-AIPAC
    },
)

# Harriet Hageman UPDATE — already in DB as US Rep WY-AL, add Senate-race meta
# Mike Rogers (MI) is INSERT because the existing Mike Rogers record is AL.

# AL low-info R primary (May 19 today)
AL_R_OTHERS = [
    placeholder('Seth Burton', 'seth-burton-al-senate', 'AL', 'R',
                primary_date='2026-05-19', suffix='Tuberville seat'),
    placeholder('Dale Deas Jr.', 'dale-deas-jr', 'AL', 'R',
                primary_date='2026-05-19', suffix='Tuberville seat'),
    placeholder('Jared Hudson', 'jared-hudson', 'AL', 'R',
                primary_date='2026-05-19', suffix='Tuberville seat'),
    placeholder('Rodney Walker', 'rodney-walker-al-senate', 'AL', 'R',
                primary_date='2026-05-19', suffix='Tuberville seat'),
]
# AL D primary candidates
AL_D = [
    placeholder('Dakarai Larriett', 'dakarai-larriett', 'AL', 'D',
                primary_date='2026-05-19', suffix='Tuberville seat'),
    placeholder('Kyle Sweetser', 'kyle-sweetser', 'AL', 'D',
                primary_date='2026-05-19', suffix='Tuberville seat'),
    placeholder('Everett Wess', 'everett-wess', 'AL', 'D',
                primary_date='2026-05-19', suffix='Tuberville seat'),
    placeholder('Mark Wheeler II', 'mark-wheeler-ii', 'AL', 'D',
                primary_date='2026-05-19', suffix='Tuberville seat'),
]

# IA other primary candidates (Hinson UPDATE handled separately)
IA_OTHERS = [
    placeholder('Jim Carlin', 'jim-carlin-ia-senate', 'IA', 'R', '2026-06-02', 'Ernst seat'),
    placeholder('Joshua Smith', 'joshua-smith-ia-senate', 'IA', 'R', '2026-06-02', 'Ernst seat'),
    placeholder('Zach Wahls', 'zach-wahls', 'IA', 'D', '2026-06-02', 'Ernst seat'),
    placeholder('Josh Turek', 'josh-turek', 'IA', 'D', '2026-06-02', 'Ernst seat'),
    placeholder('Nathan Sage', 'nathan-sage', 'IA', 'D', '2026-06-02', 'Ernst seat'),
    placeholder('Lindsay James', 'lindsay-james-ia-senate', 'IA', 'D', '2026-06-02', 'Ernst seat'),
    placeholder('Clint Twedt-Ball', 'clint-twedt-ball', 'IA', 'D', '2026-06-02', 'Ernst seat'),
]

# IL other primary candidates (Krishnamoorthi, Kelly, Stratton UPDATE)
IL_OTHERS = [
    placeholder('Jeannie Evans', 'jeannie-evans-il-senate', 'IL', 'R', '2026-03-17', 'Durbin seat'),
    placeholder('Casey Chlebek', 'casey-chlebek', 'IL', 'R', '2026-03-17', 'Durbin seat'),
]

# MN other primary candidates (Craig + Flanagan UPDATE)
MN_OTHERS = [
    placeholder('Adam Schwarze', 'adam-schwarze', 'MN', 'R', '2026-08-11', 'Smith seat'),
]

# MT other primary candidates (Alme is INSERT above)
MT_OTHERS = [
    placeholder('Lee Calhoun', 'lee-calhoun', 'MT', 'R', '2026-06-02', 'Daines seat'),
    placeholder('Charles Walking Child', 'charles-walking-child', 'MT', 'R', '2026-06-02', 'Daines seat'),
]

# NC other primary candidates (Cooper + Whatley INSERTs above as nominees)
NC_OTHERS = [
    placeholder('Don Brown', 'don-brown-nc-senate', 'NC', 'R', '2026-03-03', 'Tillis seat'),
    placeholder('Michele Morrow', 'michele-morrow', 'NC', 'R', '2026-03-03', 'Tillis seat'),
    placeholder('Elizabeth Temple', 'elizabeth-temple', 'NC', 'R', '2026-03-03', 'Tillis seat'),
]

# NH other primary candidates (Pappas UPDATE)
NH_OTHERS = [
    placeholder('Karishma Manzur', 'karishma-manzur', 'NH', 'D', '2026-09-08', 'Shaheen seat'),
    placeholder('Jared Sullivan', 'jared-sullivan-nh-senate', 'NH', 'D', '2026-09-08', 'Shaheen seat'),
]

# OK other primary candidates (Hern UPDATE)
OK_OTHERS = [
    placeholder('William Sean Buckner', 'william-sean-buckner', 'OK', 'R', '2026-06-16', 'Mullin seat'),
    placeholder('Gary Ty England', 'gary-ty-england', 'OK', 'R', '2026-06-16', 'Mullin seat'),
    placeholder('Nick Hankins', 'nick-hankins', 'OK', 'R', '2026-06-16', 'Mullin seat'),
    placeholder('Brian Ragain', 'brian-ragain', 'OK', 'R', '2026-06-16', 'Mullin seat'),
    placeholder('R. O. Joe Cassity Jr.', 'r-o-joe-cassity-jr', 'OK', 'D', '2026-06-16', 'Mullin seat'),
    placeholder('Troy Green', 'troy-green-ok-senate', 'OK', 'D', '2026-06-16', 'Mullin seat'),
    placeholder('Jim Priest', 'jim-priest', 'OK', 'D', '2026-06-16', 'Mullin seat'),
    placeholder('N\'Kiyla Jasmine Thomas', 'nkiyla-jasmine-thomas', 'OK', 'D', '2026-06-16', 'Mullin seat'),
    placeholder('Ervin Stone Yen', 'ervin-stone-yen', 'OK', 'D', '2026-06-16', 'Mullin seat'),
]

# Alan Armstrong (OK interim senator — required to NOT run in 2026)
ARMSTRONG = make_record(
    name='Alan Armstrong',
    slug='alan-armstrong',
    state='OK',
    office='U.S. Senator (interim · appointed Mar 24 2026 · oath not to run)',
    party='R',
    archetype=None,  # interim with very short tenure — no archetype meaningful
    primary_date='',
    notes=('Appointed by Governor Kevin Stitt on March 24, 2026 to fill the '
           'seat vacated by Markwayne Mullin (who became DHS Secretary). '
           'Armstrong was a board member + former CEO of Williams Companies. '
           'Signed oath stating he will NOT run in the 2026 election to keep '
           'the appointment.'),
    sources=[
        'https://ballotpedia.org/United_States_Senate_election_in_Oklahoma,_2026',
    ],
    profile_extra={
        'religion': None,
        'background': ('Former CEO + board member of Williams Companies '
                       '(natural-gas infrastructure). Appointed to U.S. '
                       'Senate March 24, 2026 to fill Mullin vacancy. '
                       'Will NOT run in 2026 general election.'),
        'next_election_year': 2028,
        'next_election_type': 'general',
        'seat_up_next': False,
    },
    candidacy_status='not_running',
    confidence_note=('2026-05-19 — interim senator; sworn in March 24 2026. '
                     'Will NOT seek election. Light scoring placeholder; '
                     'minimal voting record so far.'),
)

# WY other primary candidates (Hageman UPDATE)
WY_OTHERS = [
    placeholder('Jimmy Skovgard', 'jimmy-skovgard', 'WY', 'R', '2026-08-18', 'Lummis seat'),
    placeholder('James W. Byrd', 'james-w-byrd-wy-senate', 'WY', 'D', '2026-08-18', 'Lummis seat'),
]

NEW_RECORDS = (
    [ROGERS_MI, MCMORROW, EL_SAYED, TATE, WHATLEY, COOPER_NC, TRACY, ALME,
     SUNUNU_NH, BROWN_NH, WHITE_MN, ARMSTRONG]
    + AL_R_OTHERS + AL_D
    + IA_OTHERS + IL_OTHERS + MN_OTHERS + MT_OTHERS
    + NC_OTHERS + NH_OTHERS + OK_OTHERS + WY_OTHERS
)


# ────────────────────────────────────────────────────────────────────────
# UPDATES to existing incumbent records (Andy Barr precedent)
# ────────────────────────────────────────────────────────────────────────

INCUMBENT_UPDATES = [
    # slug, current_office_replacement_prefix, senate_seat, primary_date,
    # archetype_note (used in confidence_note), trump_endorsed (bool or None)
    ('ashley-hinson', 'U.S. Representative (IA-02)', 'Ernst seat', '2026-06-02', 'maga_conservative_r', False),
    ('barry-moore', 'U.S. Representative (AL-01)', 'Tuberville seat', '2026-05-19', 'populist_right', True),
    ('haley-stevens', 'U.S. Representative (MI-11)', 'Peters seat', '2026-08-04', 'establishment_d', False),
    ('angie-craig', 'U.S. Representative (MN-02)', 'Smith seat', '2026-08-11', 'establishment_d', False),
    ('chris-pappas', 'U.S. Representative (NH-01)', 'Shaheen seat', '2026-09-08', 'establishment_d', False),
    ('kevin-hern', 'U.S. Representative (OK-01)', 'Mullin seat', '2026-06-16', 'maga_conservative_r', False),
    ('harriet-hageman', 'U.S. Representative (WY-AL)', 'Lummis seat', '2026-08-18', 'maga_conservative_r', True),
    ('raja-krishnamoorthi', 'U.S. Representative (IL-08)', 'Durbin seat', '2026-03-17', 'establishment_d', False),
    ('robin-kelly', 'U.S. Representative (IL-02)', 'Durbin seat', '2026-03-17', 'establishment_d', False),
    ('steve-marshall', 'Attorney General (Alabama)', 'Tuberville seat', '2026-05-19', 'maga_conservative_r', False),
    ('juliana-stratton', 'Lieutenant Governor (Illinois)', 'Durbin seat', '2026-03-17', 'establishment_d', False),
    ('peggy-flanagan', 'Lt. Governor (Minnesota)', 'Smith seat', '2026-08-11', 'establishment_d', False),
]


def update_incumbent(cands, slug, new_office_base, seat_label, primary_date,
                     archetype_note, trump_endorsed):
    for c in cands:
        if c.get('slug') == slug:
            party_label = 'R' if c.get('party') == 'R' else 'D'
            won_primary = primary_date in ('2026-03-03', '2026-03-17')
            label = 'Nominee' if won_primary else 'Primary Candidate'
            trump_note = ' (Trump-endorsed)' if trump_endorsed else ''
            c['office'] = (f'{new_office_base} · 2026 U.S. Senate {label}'
                           f' · {seat_label}{trump_note}')
            prof = c.get('profile') or {}
            cn = prof.get('confidence_note', '') or ''
            note_append = (f' 2026-05-19 SENATE-RACE UPDATE: Running for the open '
                           f'{seat_label} in 2026. Primary {primary_date}. '
                           f'Archetype anchor: {archetype_note}.'
                           f'{" Trump-endorsed." if trump_endorsed else ""}')
            if 'SENATE-RACE UPDATE' not in cn:
                prof['confidence_note'] = cn + note_append
            c['profile'] = prof
            srcs = c.get('sources') or []
            extra = ['https://ballotpedia.org/United_States_Senate_elections,_2026']
            for s in extra:
                if s not in srcs:
                    srcs.append(s)
            c['sources'] = srcs
            print(f'  UPDATED {c["name"]}: {new_office_base[:35]:<35s} → +Senate {label}')
            return True
    print(f'  WARN: {slug} not found, skipping update')
    return False


def upsert(cands, record):
    key = (record['state'], record['slug'])
    for i, c in enumerate(cands):
        if (c.get('state'), c.get('slug')) == key:
            cands[i] = record
            print(f'  REPLACED {record["name"]} ({record["state"]}/{record["slug"]})')
            return
    cands.append(record)
    print(f'  INSERTED {record["name"]:<35s} ({record["state"]}/{record["slug"]})')


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data.get('candidates', [])
    n_before = len(cands)

    print(f'=== Phase 1: INSERT/REPLACE {len(NEW_RECORDS)} candidate records ===')
    for rec in NEW_RECORDS:
        upsert(cands, rec)

    print(f'\n=== Phase 2: UPDATE {len(INCUMBENT_UPDATES)} existing incumbents ===')
    for slug, office, seat, date, arch, trump in INCUMBENT_UPDATES:
        update_incumbent(cands, slug, office, seat, date, arch, trump)

    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')

    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')
    print(f'Wrote {SCORECARD}')


if __name__ == '__main__':
    main()
