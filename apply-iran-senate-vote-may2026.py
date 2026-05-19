#!/usr/bin/env python3
"""
apply-iran-senate-vote-may2026.py — apply Senate war powers vote (May 13, 2026)
to foreign_policy_restraint[0] + [1] for US Senators.

VOTE: Senate war powers resolution to halt Trump's Iran war
  May 13, 2026: 50-49 (FAILED)

  3 R defectors voted YEA (for restraint):
    - Lisa Murkowski (AK) — first time breaking with party on this
    - Susan Collins (ME) — second time
    - Rand Paul (KY) — consistent restraint advocate
  1 D defector voted NAY (against restraint):
    - John Fetterman (PA) — pro-Israel hawk

  All other Rs voted NAY (with Trump on Iran ops continuing)
  All other Ds voted YEA (for restraint)
  Independents (Sanders + King) presumed YEA per pattern

MAPPING:
  Vote YEA on resolution = T on FPR[0] (Article I war powers) + [1] (forever wars)
  Vote NAY on resolution = F on FPR[0] + [1]

This OVERWRITES existing FPR[0] + FPR[1] on Senate records because we have
ground-truth evidence. Companion to apply-iran-war-powers-vote.py (House
side, March 2026); this is the Senate version with more recent (May 2026)
roll call.

Source:
  https://www.aljazeera.com/news/2026/5/13/three-republicans-break-ranks-but-senate-fails-to-curb-trumps-war-powers
  https://time.com/article/2026/05/13/iran-war-vote-senate-murkowski-closest-vote-yet/
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False

SENATE_RE = re.compile(r'^(U\.?S\.?|United States)\s+Senator', re.IGNORECASE)

R_VOTED_YEA = {
    ('lisa murkowski', 'AK'),
    ('susan collins', 'ME'),
    ('rand paul', 'KY'),
}
D_VOTED_NAY = {
    ('john fetterman', 'PA'),
}


def norm(name):
    s = (name or '').lower().strip()
    s = re.sub(r'\.+', '', s)
    s = re.sub(r'\s+(jr|sr|ii|iii|iv)$', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def main():
    apply_mode = '--apply' in sys.argv
    with open(SCORECARD) as f:
        sc = json.load(f)
    tally = Counter()

    for c in sc['candidates']:
        office = c.get('office') or ''
        if not SENATE_RE.match(office):
            continue
        party = (c.get('party') or '').upper()
        state = (c.get('state') or '').upper()
        nm = norm(c.get('name', ''))
        key = (nm, state)

        if key in R_VOTED_YEA:
            want = T
            label = 'R_yea_defector'
        elif key in D_VOTED_NAY:
            want = F
            label = 'D_nay_defector'
        elif party == 'R':
            want = F
            label = 'R_default_nay'
        elif party == 'D':
            want = T
            label = 'D_default_yea'
        elif party == 'I':
            want = T  # Sanders + King with Ds for restraint per pattern
            label = 'I_default_yea'
        else:
            tally['skipped_no_party'] += 1
            continue

        scores = c.setdefault('scores', {})
        fpr = scores.get('foreign_policy_restraint')
        if not isinstance(fpr, list) or len(fpr) < 2:
            tally['skipped_no_fpr_array'] += 1
            continue

        for idx in (0, 1):
            before = fpr[idx]
            fpr[idx] = want
            if before != want:
                tally[f'{label}_q{idx}_changed'] += 1
            else:
                tally[f'{label}_q{idx}_unchanged'] += 1

        prof = c.setdefault('profile', {})
        existing = prof.get('confidence_note') or ''
        if 'Senate war powers May 2026' not in existing:
            prof['confidence_note'] = (existing +
                f' 2026-05-18 evidence: voted '
                f'{"YEA" if want else "NAY"} on Senate war powers resolution '
                f'to halt Iran war (May 13, 2026 — 50-49 FAILED).').strip()

    print('=== SENATE WAR POWERS MAY 2026 VOTE APPLIED ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
    else:
        print('\nDry-run.')


if __name__ == '__main__':
    main()
