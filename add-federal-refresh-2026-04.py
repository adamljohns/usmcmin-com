#!/usr/bin/env python3
"""
add-federal-refresh-2026-04.py — one-shot federal-seat reconciliation
for April 2026 turnover.

Findings from the audit (verified against Wikipedia 2026-04-22):

  * CA-1 (Doug LaMalfa, R) — VACANT since his death Jan 6, 2026.
    Special primary Jun 2, 2026; general Aug 4, 2026.
  * NJ-11 (Mikie Sherrill, D) — Sherrill resigned Nov 20, 2025 to
    become Governor of New Jersey (already tracked in scorecard).
    Analilia Mejia (D) sworn in Apr 20, 2026 after special election.
    She is a brand-new current rep who was not in our data.
  * TX-23 (Tony Gonzales, R) — VACANT since his resignation
    Apr 14, 2026. Special election TBD.
  * CA-14 (Eric Swalwell, D) — VACANT since his resignation
    Apr 14, 2026. Already in scorecard but status was stale.

This script:
  1. Adds Analilia Mejia (M001246) as NJ-11 with initial scoring
     based on her stated public positions (Bernie Sanders 2020
     political director, Medicare-for-All, abolish-ICE, $25
     minimum wage, pro-union labor advocacy).
  2. Adds VACANT placeholders for CA-1 and TX-23 with notes
     citing the resignation/death and special-election status.
  3. Updates the existing Eric Swalwell record to mark him as
     "Former Representative" with a note; keeps the record for
     the audit trail.
  4. Triggers build-data.py and notes that generate-profiles.py
     + build-stats.py should run after.

Safe to re-run: merges by slug.

Sources verified 2026-04-22:
  - https://en.wikipedia.org/wiki/California%27s_1st_congressional_district
  - https://en.wikipedia.org/wiki/New_Jersey%27s_11th_congressional_district
  - https://en.wikipedia.org/wiki/Texas%27s_23rd_congressional_district
  - https://en.wikipedia.org/wiki/Eric_Swalwell
  - https://en.wikipedia.org/wiki/Analilia_Mejia
"""
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')


def empty_scores():
    return {cat: [None] * 5 for cat in [
        'america_first', 'life', 'immigration', 'marriage',
        'christian_heritage', 'self_defense', 'education',
    ]}


def false_scores(skip_christian_heritage=True):
    out = {cat: [False] * 5 for cat in [
        'america_first', 'life', 'immigration', 'marriage',
        'self_defense', 'education',
    ]}
    out['christian_heritage'] = [None] * 5 if skip_christian_heritage else [False] * 5
    return out


# --- NEW: Analilia Mejia (NJ-11, D) ---
MEJIA = {
    'name': 'Analilia Mejia',
    'slug': 'analilia-mejia',
    'office': 'US Representative',
    'jurisdiction': 'New Jersey',
    'level': 'federal',
    'party': 'D',
    'district': 11,
    'state': 'NJ',
    'scores': false_scores(),
    'notes': (
        "Sworn in April 20, 2026 after special election to fill the seat "
        "vacated by Mikie Sherrill (now NJ Governor). Former national "
        "political director for Bernie Sanders's 2020 presidential campaign; "
        "deputy director of the U.S. Women's Bureau under Biden. "
        "Co-executive director of the Center for Popular Democracy. "
        "Public positions: Medicare for All, $25/hr minimum wage, "
        "abolition of ICE, tuition-free public college, expansion of "
        "labor protections. Defeated Joe Hathaway (R) 59.76% to 40.24%."
    ),
    'photo': None,
    'website': None,
    'sources': [
        'https://en.wikipedia.org/wiki/Analilia_Mejia',
        'https://en.wikipedia.org/wiki/New_Jersey%27s_11th_congressional_district',
        'https://ballotpedia.org/Analilia_Mejia',
    ],
    'profile': {
        'religion': None,
        'net_worth': None,
        'birthplace': 'Elizabeth, New Jersey',
        'education': 'Rutgers University–New Brunswick (BA Comparative Literature, 2000; MPP 2002; MA Labor Relations 2003)',
        'background': (
            "National political director for Bernie Sanders's 2020 presidential "
            "campaign. Deputy Director, U.S. Department of Labor Women's Bureau "
            "(2021–2023). Co-executive director, Center for Popular Democracy. "
            "Sworn in to U.S. House April 20, 2026."
        ),
        'next_election_date': '2026-11-03',
        'next_election_type': 'general',
        'seat_up_next': True,
        'bioguide': 'M001246',
        # Phone + contact_form left null: her DC office phone and contact
        # form are not yet published on house.gov (she was sworn in 2 days
        # before this commit). A follow-up enrichment pass can fill these
        # once her member page goes live.
        'phone': None,
        'office': None,
        'contact_form': None,
        'sworn_in_date': '2026-04-20',
    },
}

# --- VACANT: CA-1 (LaMalfa died 2026-01-06) ---
VACANT_CA1 = {
    'name': 'VACANT (CA-1)',
    'slug': 'vacant-ca-1',
    'office': 'US Representative',
    'jurisdiction': 'California',
    'level': 'federal',
    'party': None,
    'district': 1,
    'state': 'CA',
    'scores': empty_scores(),
    'notes': (
        "Seat vacant since the death of Doug LaMalfa (R) on January 6, 2026. "
        "California has scheduled a special primary for June 2, 2026 and a "
        "special general election for August 4, 2026 (cancelled if any "
        "candidate wins >50% in the primary)."
    ),
    'sources': [
        'https://en.wikipedia.org/wiki/California%27s_1st_congressional_district',
    ],
    'profile': {
        'next_election_date': '2026-06-02',
        'next_election_type': 'special_primary',
        'seat_up_next': True,
    },
}

# --- VACANT: TX-23 (Gonzales resigned 2026-04-14) ---
VACANT_TX23 = {
    'name': 'VACANT (TX-23)',
    'slug': 'vacant-tx-23',
    'office': 'US Representative',
    'jurisdiction': 'Texas',
    'level': 'federal',
    'party': None,
    'district': 23,
    'state': 'TX',
    'scores': empty_scores(),
    'notes': (
        "Seat vacant since Tony Gonzales (R) resigned effective April 14, 2026. "
        "Texas has not yet scheduled a special election as of this update."
    ),
    'sources': [
        'https://en.wikipedia.org/wiki/Texas%27s_23rd_congressional_district',
    ],
    'profile': {
        'next_election_date': None,
        'next_election_type': 'special_primary',
        'seat_up_next': True,
    },
}


def patch_swalwell(sc):
    """Mark Swalwell as a Former Representative — his seat is now vacant."""
    for c in sc['candidates']:
        if c.get('slug') == 'eric-swalwell' and c.get('state') == 'CA':
            c['office'] = 'Former US Representative'
            prof = c.setdefault('profile', {})
            prof['bioguide'] = prof.get('bioguide') or 'S001193'
            prof['former_seat'] = 'US House, CA-14'
            prof['resigned_date'] = '2026-04-14'
            prof['seat_up_next'] = False
            notes = c.get('notes') or ''
            if 'Resigned' not in notes:
                c['notes'] = (notes + ' Resigned effective April 14, 2026; '
                              'announced April 13. CA-14 seat vacant pending '
                              'special election.').strip()
            sources = list(c.get('sources') or [])
            if 'https://en.wikipedia.org/wiki/Eric_Swalwell' not in sources:
                sources.append('https://en.wikipedia.org/wiki/Eric_Swalwell')
            c['sources'] = sources
            return True
    return False


# --- VACANT: CA-14 (Swalwell resigned 2026-04-14) ---
VACANT_CA14 = {
    'name': 'VACANT (CA-14)',
    'slug': 'vacant-ca-14',
    'office': 'US Representative',
    'jurisdiction': 'California',
    'level': 'federal',
    'party': None,
    'district': 14,
    'state': 'CA',
    'scores': empty_scores(),
    'notes': (
        "Seat vacant since Eric Swalwell (D) resigned effective April 14, 2026. "
        "California has not yet scheduled a special election as of this update."
    ),
    'sources': [
        'https://en.wikipedia.org/wiki/Eric_Swalwell',
    ],
    'profile': {
        'next_election_date': None,
        'next_election_type': 'special_primary',
        'seat_up_next': True,
    },
}


def upsert(sc, record):
    """Replace by slug+state if exists, else append. Mint a fresh id."""
    for i, c in enumerate(sc['candidates']):
        if c.get('slug') == record['slug'] and c.get('state') == record['state']:
            record['id'] = c.get('id') or (max(x.get('id', 0) for x in sc['candidates']) + 1)
            sc['candidates'][i] = record
            return 'replaced'
    record['id'] = max((x.get('id', 0) for x in sc['candidates']), default=0) + 1
    sc['candidates'].append(record)
    return 'added'


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)

    actions = []
    for rec in [MEJIA, VACANT_CA1, VACANT_TX23, VACANT_CA14]:
        action = upsert(sc, rec)
        actions.append(f'{action} {rec["slug"]} ({rec["state"]}-{rec.get("district","?")})')
    if patch_swalwell(sc):
        actions.append('patched eric-swalwell -> Former Rep')
    else:
        actions.append('NOTE: eric-swalwell not found; skipped patch')

    # Refresh meta.
    sc.setdefault('meta', {})
    sc['meta']['total_candidates'] = len(sc['candidates'])
    sc['meta']['last_updated'] = '2026-04-22'

    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)

    print('\n'.join(' - ' + a for a in actions))
    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
