#!/usr/bin/env python3
"""
seed-state-assemblies.py — bulk seed the state lower-chamber rosters
for NV (42), NJ (80), WI (99), and NH (~400). Together these close
the ~621-seat coverage gap flagged by the rep-completeness audit.

BLENDED SOURCING (per Adam's direction):
  * Primary identity data (name, district, party): Wikipedia state-
    chamber pages, parsed with a rowspan-aware HTML walker into
    per-state JSON blobs under /tmp/ before this script reads them.
  * Per-member directory sources cited on every record:
      - OpenStates state legislator index
      - Ballotpedia state-chamber article
      - Wikipedia state-chamber article
  * Text identity verified 2026-04-22 / 2026-04-23.

SCORING METHODOLOGY (party_default, explicitly justified):
  The RESOLUTE Citizen scorecard evaluates candidates against seven
  historically-orthodox Protestant Christian policy categories. For
  every record this script creates, the initial scores follow the
  heuristic below with the candidate's `profile.confidence` field
  set to "party_default" so the UI can render a "Party-default
  scoring" chip distinguishing these records from the evidence-
  reviewed records (DeSantis, Spanberger, the 531 federal officials
  with voting-record notes).

  Democratic (D) party default (overwhelmingly opposes our scoring
  criterion — all six measurable categories false, christian_heritage
  null since that category is not a standard D/R cleavage):
    america_first:      [F, F, F, F, F]
    life:               [F, F, F, F, F]
    immigration:        [F, F, F, F, F]
    marriage:           [F, F, F, F, F]
    self_defense:       [F, F, F, F, F]
    education:          [F, F, F, F, F]
    christian_heritage: [N, N, N, N, N]

  Republican (R) party default (supports most but not all; some
  questions need specific evidence before we go True):
    america_first:      [T, T, N, N, T]      # flag display, America-first rhetoric, election-integrity generally yes
    life:               [T, T, N, T, N]      # affirms conception-to-personhood and opposes funding
    immigration:        [T, T, N, N, N]      # border/deport yes; Anglo-Saxon specific items null
    marriage:           [T, N, T, T, N]      # traditional marriage + bio-sex generally; anti-sodomy penalties not universal
    self_defense:       [T, T, T, N, T]      # 2A as core; red-flag opposition varies by state R
    education:          [T, T, T, N, N]      # parental rights + anti-CRT; school prayer and sex-ed specifics vary
    christian_heritage: [N, N, N, N, N]      # not a mainstream R platform item

  Independent (I) / Libertarian / unknown: all null. Reviewer must
  make a per-candidate determination.

  Each record carries a profile.scoring_rationale string that names
  the party_default variant applied plus a one-sentence justification,
  so a reviewer or a skeptical visitor can see at-a-glance how the
  baseline was reached.

  This baseline is DEFENSIBLE for two reasons:
    1. It is explicitly labeled as party_default, not evidence-based.
       The UI renders it differently from reviewed scores.
    2. It matches the overwhelming empirical voting clustering in
       state legislatures on these seven categories. Outliers get
       corrected via extract-claims.py + apply-claims.py as each
       individual's voting record is researched.

MERGE BEHAVIOR: merges by (slug, state). If a candidate with the same
slug+state already exists, is left unchanged (we do not overwrite
hand-curated records). New records are appended with a fresh id.

Run:
    # Generate rosters via:
    #   bash /tmp/fetch-rosters.sh  (curls Wikipedia pages to /tmp/)
    #   python3 /tmp/parse_nh_v2.py  (parses NH -> /tmp/nh_house.json)
    #   python3 /tmp/parse_nj.py     (parses NJ -> /tmp/nj_assembly.json)
    # Then:
    python3 seed-state-assemblies.py --state NV  # or NJ / WI / NH
    python3 seed-state-assemblies.py --all       # all four in sequence
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')

# --- Per-state configuration ---
STATE_CONFIG = {
    'NV': {
        'name': 'Nevada',
        'chamber_name': 'Nevada State Assembly',
        'office_label': 'State Assembly Member',
        'roster_path': '/tmp/nv_assembly.json',
        'openstates_url': 'https://openstates.org/nv/legislators/',
        'ballotpedia_url': 'https://ballotpedia.org/Nevada_State_Assembly',
        'wikipedia_url': 'https://en.wikipedia.org/wiki/Nevada_State_Assembly',
        'state_gov_url': 'https://www.leg.state.nv.us/App/Legislator/A/Assembly/Current',
        'district_type': 'numeric',      # 42 numeric districts
    },
    'NJ': {
        'name': 'New Jersey',
        'chamber_name': 'New Jersey General Assembly',
        'office_label': 'General Assembly Member',
        'roster_path': '/tmp/nj_assembly.json',
        'openstates_url': 'https://openstates.org/nj/legislators/',
        'ballotpedia_url': 'https://ballotpedia.org/New_Jersey_General_Assembly',
        'wikipedia_url': 'https://en.wikipedia.org/wiki/New_Jersey_General_Assembly',
        'state_gov_url': 'https://www.njleg.state.nj.us/legislative-roster',
        'district_type': 'numeric',
    },
    'WI': {
        'name': 'Wisconsin',
        'chamber_name': 'Wisconsin State Assembly',
        'office_label': 'State Assembly Member',
        'roster_path': '/tmp/wi_assembly.json',
        'openstates_url': 'https://openstates.org/wi/legislators/',
        'ballotpedia_url': 'https://ballotpedia.org/Wisconsin_State_Assembly',
        'wikipedia_url': 'https://en.wikipedia.org/wiki/Wisconsin_State_Assembly',
        'state_gov_url': 'https://docs.legis.wisconsin.gov/2025/legislators/assembly',
        'district_type': 'numeric',
    },
    'NH': {
        'name': 'New Hampshire',
        'chamber_name': 'New Hampshire House of Representatives',
        'office_label': 'State Representative',
        'roster_path': '/tmp/nh_house.json',
        'openstates_url': 'https://openstates.org/nh/legislators/',
        'ballotpedia_url': 'https://ballotpedia.org/New_Hampshire_House_of_Representatives',
        'wikipedia_url': 'https://en.wikipedia.org/wiki/New_Hampshire_House_of_Representatives',
        'state_gov_url': 'https://gencourt.state.nh.us/house/members/',
        'district_type': 'county-number',   # 'Belknap 01', 'Hillsborough 28' etc.
    },
}

CATS_7 = [
    'america_first', 'life', 'immigration', 'marriage',
    'self_defense', 'education', 'christian_heritage',
]

PARTY_DEFAULT_R = {
    'america_first':      [True, True, None, None, True],
    'life':               [True, True, None, True, None],
    'immigration':        [True, True, None, None, None],
    'marriage':           [True, None, True, True, None],
    'self_defense':       [True, True, True, None, True],
    'education':          [True, True, True, None, None],
    'christian_heritage': [None, None, None, None, None],
}
PARTY_DEFAULT_D = {
    'america_first':      [False] * 5,
    'life':               [False] * 5,
    'immigration':        [False] * 5,
    'marriage':           [False] * 5,
    'self_defense':       [False] * 5,
    'education':          [False] * 5,
    'christian_heritage': [None] * 5,
}
PARTY_DEFAULT_I = {cat: [None] * 5 for cat in CATS_7}


def scoring_for_party(party: str) -> dict:
    if party == 'R':
        return {cat: list(vals) for cat, vals in PARTY_DEFAULT_R.items()}
    if party == 'D':
        return {cat: list(vals) for cat, vals in PARTY_DEFAULT_D.items()}
    return {cat: list(vals) for cat, vals in PARTY_DEFAULT_I.items()}


def party_rationale(party: str) -> str:
    if party == 'R':
        return (
            "Party-default scoring applied for (R). Republicans in state legislatures "
            "vote overwhelmingly with their caucus on America-first, life, immigration, "
            "self-defense, and parental-rights-in-education categories; True marks on "
            "those categories reflect the modal R vote in recent sessions. Marriage "
            "question-4 (civil penalties for sexual immorality) is not a universal R "
            "position and left null pending specific evidence. Christian-heritage (PCH/CBG) "
            "items left null because the confessional Christian-nationalism framing is "
            "not a standard party-line item."
        )
    if party == 'D':
        return (
            "Party-default scoring applied for (D). Democrats in state legislatures vote "
            "overwhelmingly with their caucus against each of the six measurable RESOLUTE "
            "criteria (abortion rights, immigration accommodation, gun-control, LGBT "
            "inclusion, opposition to school choice, and rejection of an explicit Christian "
            "framing on policy); all six measurable categories set False. Christian-heritage "
            "(PCH/CBG) left null because the absence of evidence there would be misleading "
            "either direction — a D member could be a devout Christian in private life."
        )
    return (
        "Party-default scoring withheld. Independent / Libertarian / unknown-party "
        "members are scored all-null pending individual evidence review; every record "
        "here is a placeholder awaiting claim-extraction."
    )


def make_slug(name: str, state: str, district) -> str:
    # Normalize: lowercase, strip accents, replace spaces, keep letters/digits/-
    import unicodedata
    norm = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    slug = re.sub(r"[^\w\s'-]", '', norm).lower().strip()
    slug = re.sub(r"[\s'_]+", '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug


def build_record(cfg: dict, state_code: str, member: dict, next_id: int) -> dict:
    party = (member.get('party') or 'I').upper()
    district_raw = member.get('district')
    if cfg['district_type'] == 'numeric':
        district_field = int(district_raw) if str(district_raw).isdigit() else district_raw
        district_label = f'District {district_field}'
    else:
        district_field = str(district_raw)
        district_label = district_field
    name = member['name'].strip()
    slug_base = make_slug(name, state_code, district_field)
    slug = f'{slug_base}-{state_code.lower()}-{str(district_field).lower().replace(" ", "-")}'
    scores = scoring_for_party(party)

    sources = [
        cfg['openstates_url'],
        cfg['ballotpedia_url'],
        cfg['wikipedia_url'],
        cfg['state_gov_url'],
    ]

    return {
        'name': name,
        'slug': slug,
        'office': cfg['office_label'],
        'jurisdiction': cfg['chamber_name'],
        'level': 'state',
        'party': party if party in ('R', 'D', 'I') else 'I',
        'district': district_field,
        'state': state_code,
        'id': next_id,
        'scores': scores,
        'notes': (
            f"Seeded 2026-04-23 from the {cfg['chamber_name']} roster. "
            "Initial scoring follows the documented party-default heuristic "
            "(see profile.scoring_rationale). No individual voting-record "
            "enrichment has been performed yet; this record is a scaffolding "
            "entry awaiting claim-extraction review. "
            f"District: {district_label}. Party: {party}."
        ),
        'photo': None,
        'website': None,
        'sources': sources,
        'profile': {
            'religion': None,
            'net_worth': None,
            'birthplace': None,
            'education': None,
            'background': None,
            'next_election_year': None,
            'next_election_contenders': [],
            'twitter': None,
            'confidence': 'party_default',
            'scoring_rationale': party_rationale(party),
            'seeded_on': '2026-04-23',
            'seed_sources': {
                'openstates': cfg['openstates_url'],
                'ballotpedia': cfg['ballotpedia_url'],
                'wikipedia': cfg['wikipedia_url'],
                'state_gov': cfg['state_gov_url'],
            },
        },
    }


def seed_state(state_code: str) -> tuple:
    cfg = STATE_CONFIG[state_code]
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)
    with open(cfg['roster_path'], 'r', encoding='utf-8') as f:
        roster = json.load(f)

    existing = {(c.get('slug'), c.get('state')) for c in sc['candidates']}
    existing_offices_in_state = {
        (c.get('slug'), c.get('state'))
        for c in sc['candidates']
        if c.get('state') == state_code
    }
    # Also guard against adding a duplicate if the same name+district already exists via a different slug
    existing_name_dist = {
        (c.get('name', '').lower(), c.get('state'), str(c.get('district') or '').lower())
        for c in sc['candidates']
    }

    next_id = max((c.get('id', 0) for c in sc['candidates']), default=0) + 1
    added = 0
    skipped = 0

    for m in roster:
        if not m.get('name') or not m.get('party'):
            skipped += 1
            continue
        district_val = m.get('district')
        if cfg['district_type'] == 'numeric':
            try:
                district_val = int(district_val)
            except (ValueError, TypeError):
                skipped += 1
                continue
        rec = build_record(cfg, state_code, m, next_id)
        key = (rec['slug'], rec['state'])
        dup_key = (rec['name'].lower(), rec['state'], str(rec['district']).lower())
        if key in existing or dup_key in existing_name_dist:
            skipped += 1
            continue
        sc['candidates'].append(rec)
        existing.add(key)
        existing_name_dist.add(dup_key)
        next_id += 1
        added += 1

    # Refresh meta counts
    sc.setdefault('meta', {})
    sc['meta']['total_candidates'] = len(sc['candidates'])
    sc['meta']['last_updated'] = date.today().isoformat()

    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)

    return added, skipped, len(sc['candidates'])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--state', choices=list(STATE_CONFIG.keys()))
    ap.add_argument('--all', action='store_true', help='Run all four states (NV, NJ, WI, NH) in sequence')
    ap.add_argument('--no-build', action='store_true', help='Skip build-data.py call at the end')
    args = ap.parse_args()

    if not args.state and not args.all:
        ap.error('Pass --state XX or --all')

    targets = list(STATE_CONFIG.keys()) if args.all else [args.state]
    summary = []
    for st in targets:
        try:
            added, skipped, total = seed_state(st)
            summary.append(f'{st}: +{added} added, {skipped} skipped (total {total})')
        except FileNotFoundError as e:
            summary.append(f'{st}: FAILED — roster file missing: {e}')
    print('\n'.join(summary))

    if not args.no_build:
        subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
