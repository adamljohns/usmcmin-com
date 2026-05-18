#!/usr/bin/env python3
"""
enrich-from-adjustments.py — backfill v4.0 scoring on candidates whose
profile.score_adjustments structure (populated 2026-04 by the earlier
foreign-influence enrichment cycles) already encodes high-confidence
position evidence.

What this does:
  • candidates with `score_adjustments.aipac` → foreign_policy_restraint[3] = false
    (Q4: "Candidate has never accepted donations from foreign-backed lobbies (e.g., AIPAC)")
  • candidates with `score_adjustments.soros` → economic_stewardship[4] = false
    (Q5: "opposes WEF/ESG/Davos economic capture and supports anti-trust action against
    monopolistic financial cartels") — Soros donor network is a primary funder of the
    ESG / WEF capture infrastructure; donor-side acceptance = position against
  • candidates with `score_adjustments.china` → also foreign_policy_restraint[3] = false
    (same Q: "foreign-linked PACs")

Only writes when the slot is currently null (does not overwrite human-curated answers).
Run from repo root:
    python3 enrich-from-adjustments.py [--dry-run] [--apply]
"""
import json
import os
import sys
from collections import Counter

STATES_DIR = 'data/states'

def main():
    apply = '--apply' in sys.argv
    tally = Counter()
    affected_candidates = set()

    state_files = sorted(f for f in os.listdir(STATES_DIR) if f.endswith('.json'))
    for fn in state_files:
        fp = os.path.join(STATES_DIR, fn)
        with open(fp) as f:
            sd = json.load(f)
        changed = False
        state_code = fn.replace('.json', '').upper()

        for c in sd.get('candidates', []):
            sa = (c.get('profile') or {}).get('score_adjustments') or {}
            scores = c.get('scores') or {}

            # AIPAC or China → foreign_policy_restraint[3] = false (foreign-lobby Q)
            if (sa.get('aipac') or sa.get('china')):
                fpr = scores.get('foreign_policy_restraint')
                if isinstance(fpr, list) and len(fpr) >= 4 and fpr[3] is None:
                    fpr[3] = False
                    tally['fpr_q4_set'] += 1
                    affected_candidates.add(f'{state_code}/{c.get("slug")}')
                    changed = True
                elif isinstance(fpr, list) and len(fpr) >= 4 and fpr[3] is False:
                    tally['fpr_q4_already_false'] += 1
                elif isinstance(fpr, list) and len(fpr) >= 4 and fpr[3] is True:
                    tally['fpr_q4_conflict_true'] += 1
                    print(f'  ⚠️  CONFLICT [{state_code}] {c.get("name")} has score=True but AIPAC adjustment exists')

            # Soros → economic_stewardship[4] = false (anti-WEF/ESG capture Q)
            if sa.get('soros'):
                es = scores.get('economic_stewardship')
                if isinstance(es, list) and len(es) >= 5 and es[4] is None:
                    es[4] = False
                    tally['es_q5_set'] += 1
                    affected_candidates.add(f'{state_code}/{c.get("slug")}')
                    changed = True

        if changed and apply:
            with open(fp, 'w') as f:
                json.dump(sd, f, ensure_ascii=False, separators=(',', ':'))

    print('\n=== ENRICHMENT FROM score_adjustments ===')
    print(f'foreign_policy_restraint[3] (foreign-lobby) set to False: {tally["fpr_q4_set"]}')
    print(f'   (already False / no change): {tally["fpr_q4_already_false"]}')
    print(f'   (conflicting True flagged): {tally["fpr_q4_conflict_true"]}')
    print(f'economic_stewardship[4] (anti-WEF/ESG) set to False: {tally["es_q5_set"]}')
    print(f'Unique candidates affected: {len(affected_candidates)}')

    if not apply:
        print('\nDry-run only. Re-run with --apply to write.')

if __name__ == '__main__':
    main()
