#!/usr/bin/env python3
"""
enrich-scorecard-v4.py — apply both baseline-scoring enrichment passes
DIRECTLY to data/scorecard.json (the master source-of-truth that
build-data.py regenerates state files FROM).

Combines the logic from:
  • enrich-from-adjustments.py (AIPAC + Soros)
  • enrich-from-senate-votes.py (RFMA, BSCA, FTPA roll calls)

Run from repo root:
    python3 enrich-scorecard-v4.py --apply
After this, run:
    python3 build-data.py
    python3 generate-profiles.py
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

# ─────────────── Senate vote tables (from enrich-from-senate-votes.py) ───────────────
RFMA_R_YEAS = {
    'roy blunt': 'MO', 'richard burr': 'NC', 'shelley moore capito': 'WV',
    'susan collins': 'ME', 'joni ernst': 'IA', 'cynthia lummis': 'WY',
    'lisa murkowski': 'AK', 'rob portman': 'OH', 'mitt romney': 'UT',
    'dan sullivan': 'AK', 'thom tillis': 'NC', 'todd young': 'IN',
}
BSCA_R_YEAS = {
    'roy blunt': 'MO', 'richard burr': 'NC', 'shelley moore capito': 'WV',
    'bill cassidy': 'LA', 'susan collins': 'ME', 'john cornyn': 'TX',
    'joni ernst': 'IA', 'lindsey graham': 'SC', 'mitch mcconnell': 'KY',
    'lisa murkowski': 'AK', 'rob portman': 'OH', 'mitt romney': 'UT',
    'thom tillis': 'NC', 'pat toomey': 'PA', 'todd young': 'IN',
}
FTPA_D_YEAS = {
    'mark warner': 'VA', 'tim kaine': 'VA', 'cory booker': 'NJ',
    'andy kim': 'NJ', 'chris murphy': 'CT', 'richard blumenthal': 'CT',
    'kirsten gillibrand': 'NY', 'chuck schumer': 'NY', 'elizabeth warren': 'MA',
    'ed markey': 'MA', 'tina smith': 'MN', 'amy klobuchar': 'MN',
    'jack reed': 'RI', 'sheldon whitehouse': 'RI', 'chris coons': 'DE',
    'jon ossoff': 'GA', 'raphael warnock': 'GA', 'dick durbin': 'IL',
    'alex padilla': 'CA', 'adam schiff': 'CA', 'maria cantwell': 'WA',
    'patty murray': 'WA', 'jeff merkley': 'OR', 'ron wyden': 'OR',
    'michael bennet': 'CO', 'john hickenlooper': 'CO', 'martin heinrich': 'NM',
    'ben ray lujan': 'NM', 'mazie hirono': 'HI', 'brian schatz': 'HI',
    'jeanne shaheen': 'NH', 'maggie hassan': 'NH', 'bernie sanders': 'VT',
    'peter welch': 'VT', 'tammy baldwin': 'WI', 'gary peters': 'MI',
    'elissa slotkin': 'MI', 'tammy duckworth': 'IL', 'angela alsobrooks': 'MD',
    'chris van hollen': 'MD',
}

def norm_name(name):
    if not name: return ''
    n = name.lower().strip()
    n = re.sub(r'^(sen\.?|senator|rep\.?|representative|gov\.?|hon\.?)\s+', '', n)
    n = re.sub(r'\s+(jr\.?|sr\.?|ii|iii|iv)\.?$', '', n)
    n = re.sub(r'\b[a-z]\.?\b', '', n)
    n = re.sub(r'\s+', ' ', n).strip()
    return n

def main():
    apply = '--apply' in sys.argv
    overwrite_conflicts = '--overwrite-conflicts' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    tally = Counter()
    conflict_log = []   # for --overwrite-conflicts mode reporting

    # ─── PASS 1: score_adjustments → fpr[3] and es[4] ───
    for c in sc['candidates']:
        sa = (c.get('profile') or {}).get('score_adjustments') or {}
        scores = c.setdefault('scores', {})

        if sa.get('aipac') or sa.get('china'):
            # Skip if it's a verified_zero (positive) adjustment, not a negative one
            aipac = sa.get('aipac') or {}
            china = sa.get('china') or {}
            negative_adj = (aipac.get('delta', 0) < 0) or (china.get('delta', 0) < 0)
            if negative_adj:
                fpr = scores.get('foreign_policy_restraint')
                if isinstance(fpr, list) and len(fpr) >= 4 and fpr[3] is None:
                    fpr[3] = False
                    tally['fpr_q4_set'] += 1

        if sa.get('soros'):
            soros = sa['soros'] or {}
            if soros.get('delta', 0) < 0:
                es = scores.get('economic_stewardship')
                if isinstance(es, list) and len(es) >= 5 and es[4] is None:
                    es[4] = False
                    tally['es_q5_set'] += 1

    # ─── PASS 2: senate vote backfill ───
    name_index = {}
    for idx, c in enumerate(sc['candidates']):
        nm = norm_name(c.get('name', ''))
        if nm:
            name_index.setdefault(nm, []).append(idx)

    def apply_vote(table, category, q_idx, label):
        for name_key, expected_state in table.items():
            for idx in name_index.get(name_key, []):
                c = sc['candidates'][idx]
                if expected_state.upper() != (c.get('state') or '').upper():
                    continue
                scores = c.setdefault('scores', {})
                arr = scores.get(category)
                if not isinstance(arr, list) or len(arr) <= q_idx: continue
                if arr[q_idx] is None:
                    arr[q_idx] = False
                    tally[f'{label}_set'] += 1
                elif arr[q_idx] is True:
                    # CONFLICT: candidate currently carries True (likely from
                    # the v3→v4 migration carry-over where the old question
                    # had looser wording the senator could honestly score
                    # True on, while the v4 wording is tighter and their
                    # YEA vote on this bill contradicts it.
                    if overwrite_conflicts:
                        arr[q_idx] = False
                        tally[f'{label}_conflict_flipped'] += 1
                        conflict_log.append(
                            f'  flipped {c.get("name", "?")} ({c.get("state", "?")}) '
                            f'{category}[{q_idx}] True → False ({label} YEA vote)')
                    else:
                        tally[f'{label}_conflict'] += 1
                        conflict_log.append(
                            f'  kept  {c.get("name", "?")} ({c.get("state", "?")}) '
                            f'{category}[{q_idx}] = True (YEA on {label} — flip with --overwrite-conflicts)')
                else:
                    tally[f'{label}_already_false'] += 1
                break

    apply_vote(RFMA_R_YEAS, 'biblical_marriage', 1, 'RFMA')
    apply_vote(BSCA_R_YEAS, 'self_defense', 1, 'BSCA')
    apply_vote(FTPA_D_YEAS, 'election_integrity', 3, 'FTPA')

    print('=== ENRICHMENT RESULTS (scorecard.json) ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')

    if conflict_log:
        print(f'\n=== CONFLICTS ({len(conflict_log)}) ===')
        for line in conflict_log:
            print(line)

    if apply:
        # indent=2 + trailing newline to match build-data.py's
        # atomic_write(compact=False) convention. Compact mode here
        # explodes git diffs by 2.2M lines.
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
        print('Next: python3 build-data.py  → python3 generate-profiles.py')
    else:
        print('\nDry-run. Re-run with --apply to write.')
        if not overwrite_conflicts:
            print('Add --overwrite-conflicts to flip the True-conflict senators above to False.')

if __name__ == '__main__':
    main()
