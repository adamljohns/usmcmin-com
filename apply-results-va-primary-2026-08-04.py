#!/usr/bin/env python3
"""
apply-results-va-primary-2026-08-04.py — Virginia 8/4/2026 REPUBLICAN primary.

Civic research by Sheriff Roy (FXBG desk), pulled against the VA Department of
Elections (ELECT) public API and results index on 2026-08-05 ~18:50 EDT.

WHAT WAS ON THE FXBG-AREA REPUBLICAN BALLOT (federal only):
  * U.S. Senate (statewide) — Mizusawa / Williams / Farington
  * U.S. House VA-07        — Ollivant / Harding / Smithers
  * NO local Republican primaries (ELECT's own candidate-list note)
  * NO General Assembly Republican primary identified for FXBG/Spotsy/Stafford

RESULTS APPLIED:
  VA-07 R : Douglas Ollivant WON 13,337 (56.58%); Philip Harding 7,229 (30.67%);
            Ricky Smithers 3,005 (12.75%). Race total 23,571.
            → Ollivant faces Eugene Vindman (D incumbent) in November.
  SENATE R: Bert Mizusawa WON — advances against Mark Warner (D) in November.
            Vote totals deliberately LEFT NULL: ELECT-attributed secondary
            snapshots conflict badly (Center Square 66,117/35,272/24,453 vs
            WSLS 103,540/57,515/39,424 at ~89.5% precincts), and ELECT's own
            API returned an empty contestGroups, so no figure could be pinned
            to the primary source. A null beats a wrong number in a public
            database.

*** EVERYTHING HERE IS UNOFFICIAL. ***
ELECT still lists this election under Unofficial Results and the public API
reports isOfficialResults=false (statewide asOf 2026-08-05T22:42:36Z). For
multi-locality federal offices, results become official only on State Board of
Elections certification — a local Electoral Board canvass (FXBG noticed Aug 5
noon; provisional Aug 10) is necessary process, not certification. Every record
this script touches is stamped UNOFFICIAL, and a re-run pass is required once
SBE certifies.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
TODAY = '2026-08-05'

SRC = [
    'https://www.elections.virginia.gov/resultsreports/election-results/',
    'https://enr.elections.virginia.gov/results/public/virginia/elections/2026-August-Republican-Primary',
    'https://www.potomaclocal.com/2026/08/05/ollivant-wins-gop-nod-in-competitive-7th-district-beckwith-advances-in-10th-as-mizusawa-to-face-warner/',
]

# slug → (office suffix, confidence note)
WINNERS = {
    'douglas-ollivant': (
        ' · WON 8/4 R PRIMARY VA-07 (56.58%, UNOFFICIAL) — R nominee vs Eugene Vindman',
        f'{TODAY} — Won the VA-07 Republican primary 8/4/2026 with 13,337 votes (56.58%) '
        'of 23,571 cast; Harding 7,229 (30.67%), Smithers 3,005 (12.75%). UNOFFICIAL: ELECT '
        'has not certified (isOfficialResults=false at pull time); figures are ELECT-attributed '
        'via Potomac Local. Advances to face Rep. Eugene Vindman (D) in November.'),
    'bert-mizusawa': (
        ' · WON 8/4 R U.S. SENATE PRIMARY (UNOFFICIAL) — R nominee vs Mark Warner',
        f'{TODAY} — Won the Virginia Republican U.S. Senate primary 8/4/2026. UNOFFICIAL: ELECT '
        'has not certified. Vote totals deliberately not recorded — ELECT-attributed secondary '
        'snapshots conflict (66,117/35,272/24,453 vs 103,540/57,515/39,424) and ELECT\'s API '
        'returned no contest rows, so no total could be sourced to the primary record. '
        'Advances to face Sen. Mark Warner (D) in November.'),
}

# slug → (office suffix, confidence note)
LOSERS = {
    'philip-harding': (
        ' · LOST 8/4 R primary VA-07 (30.67%, UNOFFICIAL)',
        f'{TODAY} — Lost the VA-07 Republican primary 8/4/2026 with 7,229 votes (30.67%) '
        'to Douglas Ollivant. UNOFFICIAL — ELECT has not certified.'),
    'ricky-smithers': (
        ' · LOST 8/4 R primary VA-07 (12.75%, UNOFFICIAL)',
        f'{TODAY} — Lost the VA-07 Republican primary 8/4/2026 with 3,005 votes (12.75%) '
        'to Douglas Ollivant. UNOFFICIAL — ELECT has not certified.'),
    'david-williams': (
        ' · LOST 8/4 R U.S. Senate primary (UNOFFICIAL)',
        f'{TODAY} — Lost the Virginia Republican U.S. Senate primary 8/4/2026 to Bert Mizusawa. '
        'UNOFFICIAL — ELECT has not certified; vote totals not recorded because '
        'ELECT-attributed snapshots conflict.'),
    'kim-farington': (
        ' · LOST 8/4 R U.S. Senate primary (UNOFFICIAL)',
        f'{TODAY} — Lost the Virginia Republican U.S. Senate primary 8/4/2026 to Bert Mizusawa. '
        'UNOFFICIAL — ELECT has not certified; vote totals not recorded because '
        'ELECT-attributed snapshots conflict.'),
}

# Structured result rows, kept separate from the prose so a later certification
# pass can overwrite numbers without re-parsing notes.
RESULTS = {
    'douglas-ollivant': dict(votes=13337, pct=56.58, outcome='won'),
    'philip-harding':   dict(votes=7229,  pct=30.67, outcome='lost'),
    'ricky-smithers':   dict(votes=3005,  pct=12.75, outcome='lost'),
    'bert-mizusawa':    dict(votes=None,  pct=None,  outcome='won'),
    'david-williams':   dict(votes=None,  pct=None,  outcome='lost'),
    'kim-farington':    dict(votes=None,  pct=None,  outcome='lost'),
}

RACE = {
    'douglas-ollivant': 'U.S. House VA-07 (R primary)',
    'philip-harding':   'U.S. House VA-07 (R primary)',
    'ricky-smithers':   'U.S. House VA-07 (R primary)',
    'bert-mizusawa':    'U.S. Senate — Virginia (R primary)',
    'david-williams':   'U.S. Senate — Virginia (R primary)',
    'kim-farington':    'U.S. Senate — Virginia (R primary)',
}


def find(cands, slug):
    return next((c for c in cands if c.get('slug') == slug and c.get('state') == 'VA'), None)


def touch_sources(c):
    for s in SRC:
        if s not in (c.get('sources') or []):
            c.setdefault('sources', []).append(s)


def stamp(c, slug, suffix, note, status):
    c['candidacy_status'] = status
    if suffix.strip() not in (c.get('office') or ''):
        c['office'] = (c.get('office') or '').rstrip() + suffix
    p = c.setdefault('profile', {})
    p['next_election'] = 2026
    if status == 'general_candidate':
        p['next_election_type'] = 'general'
        p['next_election_date'] = '2026-11-03'
    existing = p.get('confidence_note', '') or ''
    if note not in existing:
        p['confidence_note'] = (existing + ' · ' if existing else '') + note
    r = RESULTS[slug]
    p['primary_result'] = {
        'date': '2026-08-04',
        'race': RACE[slug],
        'party': 'R',
        'outcome': r['outcome'],
        'votes': r['votes'],
        'percentage': r['pct'],
        'certified': False,
        'certification_note': (
            'UNOFFICIAL. ELECT lists the race under Unofficial Results and the public API '
            'reports isOfficialResults=false. Federal multi-locality offices are official only '
            'on State Board of Elections certification; the local Electoral Board canvass '
            '(FXBG Aug 5 noon; provisional Aug 10) does not certify them. Re-pull after SBE.'),
        'sources': SRC,
    }
    touch_sources(c)


def main():
    data = json.loads(SCORECARD.read_text())
    cands = data['candidates']
    log, missing = [], []

    for slug, (suffix, note) in WINNERS.items():
        c = find(cands, slug)
        if not c:
            missing.append(slug); continue
        stamp(c, slug, suffix, note, 'general_candidate')
        log.append(f'{slug:20} → general_candidate (WON, unofficial)')

    for slug, (suffix, note) in LOSERS.items():
        c = find(cands, slug)
        if not c:
            missing.append(slug); continue
        stamp(c, slug, suffix, note, 'lost_primary')
        log.append(f'{slug:20} → lost_primary (unofficial)')

    if missing:
        raise SystemExit(f'ABORT — slugs not found, nothing written: {missing}')

    # scorecard.json is stored MINIFIED on purpose: build-data.py notes it
    # renders to ~60MB under indent=2, past the 50MB GitHub warns at and
    # toward the 100MB it rejects. Write it the same way build-data.py does,
    # atomically via a temp file, so a crash can't leave a half-written 36MB
    # master. (apply-results-ky-senate-2026.py writes indent=2 here — that is
    # a latent bug, not a pattern to copy.)
    tmp = SCORECARD.with_suffix('.json.tmp')
    with open(tmp, 'w') as f:
        json.dump(data, f, separators=(',', ':'))
    tmp.replace(SCORECARD)

    print('VA 8/4/2026 Republican primary results applied (ALL UNOFFICIAL):')
    for l in log:
        print('  ' + l)
    print('\nNo local or General Assembly R primaries were on the FXBG-area ballot.')
    print('Re-run a certification pass once ELECT/SBE marks the race official.')
    print('\nNEXT: python3 build-data.py   # propagate into data/states/*.json + index.json')


if __name__ == '__main__':
    main()
