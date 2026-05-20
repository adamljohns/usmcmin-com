#!/usr/bin/env python3
"""
add-competitive-house-2026-pass4-batch3.py — Pass 4 batch 3.

Toss-up + lean districts: VA-02/07, NC-13/08, NV-01/03, CO-08, CA-41, NY-01,
WA-08, IA-01. ~14 records of 2024 nominees + announced 2026 challengers.
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

def rec(name, slug, state, district, office, party, archetype=None, primary_date='', notes='',
        sources=None, profile_extra=None, candidacy_status='primary_candidate'):
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
            'confidence_note': f'2026-05-20 — competitive district challenger ({state}-{district}). Archetype: {archetype}.' if archetype else '2026-05-20 — competitive district placeholder.',
            **(profile_extra or {}),
        },
    }

RECORDS = [
    # ══ VA-02 (R incumbent Jen Kiggans · D primary 6/16) ══
    rec('Missy Cotter Smasal', 'missy-cotter-smasal', 'VA', 2,
        'U.S. Representative VA-02 (2026 D Candidate · 2024 nominee · Navy vet)',
        'D', 'establishment_d', '2026-06-16',
        notes=('U.S. Navy veteran. 2024 D nominee against Jen Kiggans (lost narrowly). '
               'Considering 2026 rematch in Hampton Roads swing district.'),
        sources=['https://ballotpedia.org/Missy_Cotter_Smasal']),

    # ══ VA-07 (D incumbent Eugene Vindman · R primary 6/16) ══
    rec('Yesli Vega', 'yesli-vega', 'VA', 7,
        'U.S. Representative VA-07 (2026 R Candidate · 2022 + 2024 nominee · Prince William Co supervisor)',
        'R', 'maga_conservative_r', '2026-06-16',
        notes=('Prince William County Supervisor (Coles District). 2022 R nominee for VA-07 '
               '(lost to Spanberger). 2024 R nominee (lost to Vindman). May run 2026.'),
        sources=['https://ballotpedia.org/Yesli_Vega']),

    # ══ NC-13 (R incumbent Brad Knott · D primary 3/3 DONE) ══
    rec('Frank Pierce', 'frank-pierce-nc-13', 'NC', 13,
        'U.S. Representative NC-13 (2026 D Candidate · 2024 nominee · Navy vet)',
        'D', 'establishment_d', '2026-03-03',
        notes='Navy veteran. 2024 D nominee for NC-13 (lost to Knott). 2026 D candidate.',
        sources=['https://ballotpedia.org/Frank_Pierce']),

    # ══ NV-03 (D incumbent Susie Lee · R primary 6/9) ══
    rec('Drew Johnson', 'drew-johnson', 'NV', 3,
        'U.S. Representative NV-03 (2026 R Candidate · 2024 nominee · former think tank exec)',
        'R', 'establishment_r', '2026-06-09',
        notes=('Conservative think tank executive (formerly Yankee Institute, Beacon Center). '
               '2024 R nominee for NV-03 (lost narrowly to Susie Lee). 2026 R candidate.'),
        sources=['https://ballotpedia.org/Drew_Johnson']),

    # ══ NV-01 (D incumbent Dina Titus · R primary 6/9) ══
    rec('Mark Robertson', 'mark-robertson', 'NV', 1,
        'U.S. Representative NV-01 (2026 R Candidate · 2024 nominee · Army veteran)',
        'R', 'establishment_r', '2026-06-09',
        notes='Army veteran. 2024 R nominee for NV-01 (lost to Dina Titus). 2026 R candidate.',
        sources=['https://ballotpedia.org/Mark_Robertson']),

    # ══ CO-08 (R incumbent Gabe Evans · D primary 6/30) ══
    rec('Yadira Caraveo', 'yadira-caraveo', 'CO', 8,
        'U.S. Representative CO-08 (2026 D Candidate · former rep · 2022 winner / 2024 loser to Evans)',
        'D', 'establishment_d', '2026-06-30',
        notes=('Former U.S. Representative CO-08 (2023-2025, first to hold new seat after redistricting). '
               'Pediatrician. Former CO state representative. Lost to Gabe Evans in 2024 by ~2,500 votes. '
               'Running again 2026.'),
        sources=['https://ballotpedia.org/Yadira_Caraveo']),

    # ══ CA-41 (R incumbent Ken Calvert · top-2 6/2) ══
    rec('Will Rollins', 'will-rollins', 'CA', 41,
        'U.S. Representative CA-41 (2026 D Candidate · former federal prosecutor · 2022 + 2024 nominee)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Former federal prosecutor (national security cases). 2022 + 2024 D nominee against '
               'Ken Calvert (lost both, narrowly in 2024). Openly gay candidate. May run again 2026.'),
        sources=['https://ballotpedia.org/Will_Rollins']),

    # ══ NY-01 (R incumbent Nick LaLota · D primary 6/23) ══
    rec('John Avlon', 'john-avlon', 'NY', 1,
        'U.S. Representative NY-01 (2026 D Candidate · 2024 nominee · former CNN anchor + speechwriter)',
        'D', 'establishment_d', '2026-06-23',
        notes=('Former CNN anchor and senior political analyst. Former chief speechwriter for '
               'NYC Mayor Giuliani. 2024 D nominee for NY-01 (lost to LaLota). May run 2026.'),
        sources=['https://ballotpedia.org/John_Avlon']),

    # ══ WA-08 (D incumbent Kim Schrier · R primary 8/4) ══
    rec('Carmen Goers', 'carmen-goers', 'WA', 8,
        'U.S. Representative WA-08 (2026 R Candidate · 2024 nominee · former Boeing engineer)',
        'R', 'establishment_r', '2026-08-04',
        notes=('Former Boeing engineer. 2024 R nominee for WA-08 (lost to Schrier). 2026 R candidate.',),
        sources=['https://ballotpedia.org/Carmen_Goers']),

    # ══ IA-01 (R incumbent Mariannette Miller-Meeks · D primary 6/2) ══
    rec('Christina Bohannan', 'christina-bohannan', 'IA', 1,
        'U.S. Representative IA-01 (2026 D Candidate · 2022 + 2024 nominee · former IA state rep)',
        'D', 'establishment_d', '2026-06-02',
        notes=('Former IA state representative. Law professor. 2022 + 2024 D nominee against '
               'Miller-Meeks (lost both narrowly). Running 2026 in Iowa swing seat.'),
        sources=['https://ballotpedia.org/Christina_Bohannan']),

    # ══ MN-03 (D incumbent Kelly Morrison · R primary 8/11) ══
    rec('Tad Jude', 'tad-jude', 'MN', 3,
        'U.S. Representative MN-03 (2026 R Candidate · former judge · long-time MN politician)',
        'R', 'establishment_r', '2026-08-11',
        notes='Former MN District Court judge. Long-time MN politician (state legislator). R candidate MN-03 2026.',
        sources=['https://ballotpedia.org/Tad_Jude']),

    # ══ CO-03 (R incumbent Jeff Hurd · D primary 6/30) ══
    rec('Adam Frisch', 'adam-frisch', 'CO', 3,
        'U.S. Representative CO-03 (2026 D Candidate · 2022 + 2024 nominee · Aspen city councilor)',
        'D', 'establishment_d', '2026-06-30',
        notes=('Former Aspen city councilor. 2022 D nominee against Lauren Boebert (lost by 546 '
               'votes). 2024 nominee against Jeff Hurd (lost). Running 2026 in CO-03 swing seat.'),
        sources=['https://ballotpedia.org/Adam_Frisch']),

    # ══ AZ-01 (R incumbent David Schweikert RUNNING FOR GOV · open · D primary 8/4) ══
    rec('Amish Shah', 'amish-shah-az-01', 'AZ', 1,
        'U.S. Representative AZ-01 (2026 D Candidate · former AZ state rep · 2024 nominee · physician)',
        'D', 'establishment_d', '2026-08-04',
        notes=('Physician, former AZ state representative. 2024 D nominee for AZ-01 (lost narrowly '
               'to Schweikert). Running 2026 in newly-open seat (Schweikert running for AZ Governor).'),
        sources=['https://ballotpedia.org/Amish_Shah']),

    # ══ ME-02 (D incumbent Jared Golden · R primary 6/9) ══
    rec('Austin Theriault', 'austin-theriault', 'ME', 2,
        'U.S. Representative ME-02 (2026 R Candidate · 2024 nominee · former NASCAR driver)',
        'R', 'establishment_r', '2026-06-09',
        notes=('Former NASCAR driver. Former Maine state representative. 2024 R nominee for ME-02 '
               '(lost narrowly to Jared Golden). Running 2026.'),
        sources=['https://ballotpedia.org/Austin_Theriault']),
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
        dist_str = f'{r["district"]:02d}' if r['district'] else 'AL'
        print(f'  {action} {r["name"]:<28s} ({r["state"]}-{dist_str} {r["party"]})')
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
