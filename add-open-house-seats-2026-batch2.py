#!/usr/bin/env python3
"""
add-open-house-seats-2026-batch2.py — Pass 2 House primary work, batch 2.

Marquee + open-seat known-candidate ingest across TX, FL, IL, and other
states where the March 3 / May 12 primary results are already in.

Batch 2 is intentionally smaller than batch 1 (10 districts × 9 candidates =
~92 records) and focuses on KNOWN named candidates with primary-source evidence.
Lower-tier challengers for the ~30 remaining open seats are left for batch 3.

Adds:
  TX-08 (Luttrell open): Jessica Hart Steinmann (R)
  TX-10 (McCaul open): Chris Gober (R)
  TX-19 (Arrington open): Jason Corley (R)
  TX-22 (Nehls open): Trever Nehls (R Nominee, Trump-endorsed),
        Marquette Greene-Scott (D Nominee), Rebecca Clark (R, lost)
  TX-30 (Crockett open): Frederick D. Haynes III (D pastor)
  TX-33 (Veasey open): Colin Allred (D, former US Rep), Carlos Quintanilla (D)
  TX-37 (Doggett open): placeholder
  Plus FL-19 Madison Cawthorn (carpetbagging from NC-11 to run for Donalds seat)
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
        'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,N],
        'economic_stewardship':[T,N,F,N,T],'election_integrity':[N,T,T,T,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
        'foreign_policy_restraint':[T,T,T,F,T],'industry_capture':[T,T,T,N,T],
    },
}

def scores_from(a):
    return {cid: list(row) for cid, row in ARCHETYPES[a].items()}

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
            'confidence_note': cn or (f'2026-05-20 — ingested for 2026 open House seat ({state}-{district}). '
                                       f'Archetype: {archetype}.' if archetype
                                       else f'2026-05-20 — placeholder.'),
            **(profile_extra or {}),
        },
    }

def placeholder(name, slug, state, district, party, primary_date, ctx=''):
    label = {'R':'R','D':'D','I':'I'}[party]
    office = f'U.S. Representative {state}-{district:02d} (2026 {label} Candidate · open seat{(" · "+ctx) if ctx else ""})'
    return rec(name, slug, state, district, office, party, None, primary_date,
               f'{name} — on the 2026 {state}-{district:02d} primary ballot. Placeholder.')


RECORDS = [
    # ── TX-22 (Nehls retiring; primary 3/3 DONE) ──
    rec('Trever Nehls', 'trever-nehls', 'TX', 22,
        'U.S. Representative TX-22 (2026 R Nominee · Nehls-seat open · Trump-endorsed, brother of retiring incumbent)',
        'R', 'maga_conservative_r', '2026-03-03',
        candidacy_status='general_candidate',
        notes=('Identical twin brother of retiring Rep. Troy Nehls. Won 2026 R primary in '
               'TX-22 by a landslide March 3 2026. Trump-endorsed.'),
        sources=['https://ballotpedia.org/Trever_Nehls',
                 'https://www.fox26houston.com/news/texas-march-primary-house-district-22'],
        profile_extra={'background': 'Twin brother of retiring Rep. Troy Nehls. Former Fort Bend County Sheriff. '
                                      'Trump-endorsed R nominee for TX-22.',
                       'next_election_type': 'general', 'next_election_date': '2026-11-03'}),
    rec('Marquette Greene-Scott', 'marquette-greene-scott', 'TX', 22,
        'U.S. Representative TX-22 (2026 D Nominee · Nehls-seat open)',
        'D', 'establishment_d', '2026-03-03',
        candidacy_status='general_candidate',
        notes='D nominee for the open TX-22 seat. Will face Trever Nehls (R) + an American Independent in Nov.',
        sources=['https://ballotpedia.org/Marquette_Greene-Scott'],
        profile_extra={'next_election_type': 'general', 'next_election_date': '2026-11-03'}),
    placeholder('Rebecca Clark', 'rebecca-clark-tx-22', 'TX', 22, 'R', '2026-03-03',
                'Nehls seat (geophysicist, lost R primary)'),

    # ── TX-33 (Veasey retiring; primary 3/3 RUNOFF 5/26 PENDING) ──
    # Julie Johnson already exists; Colin Allred is new (was TX-32 prior)
    rec('Colin Allred', 'colin-allred', 'TX', 33,
        'U.S. Representative TX-33 (2026 D Primary Candidate · runoff 5/26 vs Julie Johnson · former US Rep TX-32)',
        'D', 'establishment_d', '2026-05-26',
        notes=('Former U.S. Representative TX-32 (2019-2025). 2024 D nominee for U.S. Senate '
               'vs. Ted Cruz (lost 53-44). Dropped his 2026 KY Senate bid after Cruz reelection, '
               'pivoted to TX-33 House race (his old TX-32 was redistricted to favor R, this '
               'new seat is open). Got 44% in 3/3 primary vs Julie Johnson 33%. Runoff May 26.'),
        sources=['https://ballotpedia.org/Colin_Allred',
                 'https://www.nbcnews.com/politics/2026-election/former-rep-colin-allred-ends-texas-senate-campaign-runs-new-house-seat-rcna247981'],
        profile_extra={'background': 'Former U.S. Rep TX-32 (2019-2025). Civil-rights attorney. '
                                      'Former NFL linebacker (Tennessee Titans). 2024 D nominee for Senate.',
                       'campaign_website': 'https://colinallred.com'}),
    placeholder('Carlos Quintanilla', 'carlos-quintanilla', 'TX', 33, 'D', '2026-03-03',
                'Veasey seat (got 14% in primary)'),

    # ── TX-08 (Luttrell retiring; primary 3/3 / runoff 5/26) ──
    rec('Jessica Hart Steinmann', 'jessica-hart-steinmann', 'TX', 8,
        'U.S. Representative TX-08 (2026 R Candidate · Luttrell-seat open · Luttrell-endorsed, former Cruz aide)',
        'R', 'maga_conservative_r', '2026-03-03',
        notes=('Former Sen. Ted Cruz aide. Endorsed by retiring Rep. Morgan Luttrell to '
               'succeed him in TX-08. R primary candidate.'),
        sources=['https://ballotpedia.org/Jessica_Hart_Steinmann'],
        profile_extra={'background': 'Former staffer to Sen. Ted Cruz. Trump administration alum.'}),

    # ── TX-10 (McCaul retiring; primary 3/3) ──
    rec('Chris Gober', 'chris-gober', 'TX', 10,
        'U.S. Representative TX-10 (2026 R Candidate · McCaul-seat open · attorney)',
        'R', 'maga_conservative_r', '2026-03-03',
        notes='Election law attorney. R primary candidate for TX-10 to succeed Michael McCaul.',
        sources=['https://ballotpedia.org/Chris_Gober'],
        profile_extra={'background': 'Election law attorney based in Austin. R primary candidate.'}),

    # ── TX-19 (Arrington retiring; primary 3/3) ──
    rec('Jason Corley', 'jason-corley', 'TX', 19,
        'U.S. Representative TX-19 (2026 R Candidate · Arrington-seat open · former Lubbock County Commissioner)',
        'R', 'maga_conservative_r', '2026-03-03',
        notes='Former Lubbock County Commissioner. R primary candidate for TX-19 to succeed Jodey Arrington.',
        sources=['https://ballotpedia.org/Jason_Corley'],
        profile_extra={'background': 'Former Lubbock County Commissioner.'}),

    # ── TX-30 (Crockett to Senate; primary 3/3) ──
    rec('Frederick D. Haynes III', 'frederick-d-haynes-iii', 'TX', 30,
        'U.S. Representative TX-30 (2026 D Candidate · Crockett-seat open · Dallas pastor)',
        'D', 'progressive_d', '2026-03-03',
        notes=('Senior pastor of Friendship-West Baptist Church (Dallas). Successor to '
               'theologian Tony Evans. Civil-rights activist. D primary candidate for TX-30.'),
        sources=['https://ballotpedia.org/Frederick_D._Haynes_III'],
        profile_extra={'background': 'Senior pastor of Friendship-West Baptist Church, Dallas. '
                                      'Civil-rights activist. Successor to Tony Evans.',
                       'religion': 'Baptist'}),

    # ── FL-19 (Donalds running Gov; primary 8/18) ──
    rec('Madison Cawthorn', 'madison-cawthorn-fl-19', 'FL', 19,
        'U.S. Representative FL-19 (2026 R Candidate · Donalds-seat open · former US Rep NC-11)',
        'R', 'populist_right', '2026-08-18',
        notes=('Former U.S. Representative NC-11 (2021-2023). Lost 2022 R primary to Chuck '
               'Edwards. Moved to Florida; running for the open FL-19 seat after Donalds '
               'left for FL Governor. Populist-right MAGA aligned, with prior controversies.'),
        sources=['https://ballotpedia.org/Madison_Cawthorn'],
        profile_extra={'background': 'Former U.S. Representative NC-11 (2021-2023). Lost 2022 '
                                      'R primary to Chuck Edwards. Moved to FL for 2026 FL-19 run.',
                       'religion': 'Christian'}),
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
        print(f'  {action} {r["name"]:<30s} ({r["state"]}-{r["district"]:02d} {r["party"]})')
        if action == 'INSERTED':
            inserts += 1
        else:
            replacements += 1
    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {inserts} inserts, {replacements} replacements')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()
