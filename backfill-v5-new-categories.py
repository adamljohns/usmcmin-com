#!/usr/bin/env python3
"""
backfill-v5-new-categories.py — seed the 3 new v5.0 categories from each
candidate's EXISTING scoring pattern (not raw party), leaving null when the
record is too sparse or too mixed to infer. Additive only — never overwrites
existing answers (the new categories are null on every record pre-backfill).

Lean is derived from the 6 shared God First categories the candidate is ALREADY
scored on:
  - god_true_rate = True / (True+False)
  - >= MIN_ANSWERED answered AND rate >= 0.60  → conservative lean  → T-template
  - >= MIN_ANSWERED answered AND rate <= 0.40  → progressive lean   → F-template
  - otherwise                                  → leave null (don't guess)

Templates mirror the disclosed party-default archetype already used across the
bulk records (conservatives back law/order + resist overreach; progressives the
inverse). The last Refuse-Overreach cell is left null to preserve a little
individual headroom rather than asserting a perfect record.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None
MIN_ANSWERED = 10  # need a decent sample of God First answers to infer lean

SHARED_GOD = ['sanctity_of_life', 'biblical_marriage', 'family_child_sovereignty',
              'christian_liberty', 'economic_stewardship', 'election_integrity']

# New-category templates by lean
TEMPLATES = {
    'conservative': {
        'public_justice':           [T, T, T, T, T],
        'refuse_federal_overreach': [T, T, T, T, N],
        'refuse_state_overreach':   [T, T, T, T, N],
    },
    'progressive': {
        'public_justice':           [F, F, F, F, F],
        'refuse_federal_overreach': [F, F, F, F, F],
        'refuse_state_overreach':   [F, F, F, F, F],
    },
}

# Which new categories apply at which tier (from pillars in the migration)
TIER_NEW_CATS = {
    'state': ['public_justice', 'refuse_federal_overreach'],
    'local': ['public_justice', 'refuse_state_overreach'],
    'federal': [],  # federal rubric has none of the new categories
}


def classify_office_tier(c):
    import re
    office = (c.get('office') or '')
    if not office:
        jur = (c.get('jurisdiction') or '').lower()
        return 'federal' if ('executive branch' in jur or 'judicial branch' in jur) else 'state'
    o = office.lower()
    if re.search(r'\b(president|vice president|u\.?s\.?\s+sen|u\.?s\.?\s+hous|u\.?s\.?\s+rep|'
                 r'united states sen|united states hous|united states rep|secretary of|'
                 r'acting attorney general|attorney general of the united states|director of|'
                 r'administrator of|ambassador|chief of staff|deputy chief of staff|'
                 r'homeland security advisor|chief justice|associate justice.+supreme court|'
                 r'special envoy)', o):
        if re.search(r'^attorney general$|state attorney general', o) and 'united states' not in o:
            return 'state'
        return 'federal'
    if re.search(r'\bgovernor\b|^lt\.?\s+governor|lieutenant governor|state senator|state senate|'
                 r'state representative|state hous|state assembl|^delegate$|delegate \(|'
                 r'house of delegates', o):
        return 'state'
    if re.search(r'^attorney general$|secretary of state$|state treasurer|state auditor|'
                 r'state comptroller', o):
        return 'state'
    if 'state supreme court' in o or re.search(r'(chief justice|justice).+state', o):
        return 'state'
    if re.search(r"\bmayor\b|city council|town council|borough council|"
                 r"county (commissioner|supervisor|judge|board)|school board|board of education|"
                 r"district attorney|county attorney|state'?s attorney|circuit attorney|"
                 r"sheriff|city clerk|city attorney|commonwealth'?s attorney", o):
        return 'local'
    return 'state'


def derive_lean(scores):
    t = f = 0
    for cid in SHARED_GOD:
        for v in scores.get(cid, []):
            if v is True:
                t += 1
            elif v is False:
                f += 1
    answered = t + f
    if answered < MIN_ANSWERED:
        return None
    rate = t / answered
    if rate >= 0.60:
        return 'conservative'
    if rate <= 0.40:
        return 'progressive'
    return None


def main():
    data = json.loads(SCORECARD.read_text())
    cands = data['candidates']

    seeded = skipped_ambiguous = skipped_federal = 0
    by_lean = {'conservative': 0, 'progressive': 0}

    for c in cands:
        tier = classify_office_tier(c)
        new_cats = TIER_NEW_CATS.get(tier, [])
        if not new_cats:
            skipped_federal += 1
            continue
        scores = c.setdefault('scores', {})
        # Only seed categories that are currently absent or all-null (never overwrite)
        targets = [cat for cat in new_cats
                   if not any(v is not None for v in scores.get(cat, []))]
        if not targets:
            continue
        lean = derive_lean(scores)
        if lean is None:
            skipped_ambiguous += 1
            continue
        for cat in targets:
            scores[cat] = list(TEMPLATES[lean][cat])
        by_lean[lean] += 1
        seeded += 1
        # disclosure
        prof = c.setdefault('profile', {})
        note = prof.get('confidence_note', '') or ''
        add = (f'2026-05-21 — v5.0 new-category seed ({lean} lean inferred from '
               f'existing God First pattern; party-default archetype, not individual evidence).')
        if add not in note:
            prof['confidence_note'] = (note + ' · ' if note else '') + add

    SCORECARD.write_text(json.dumps(data, indent=2) + '\n')
    print(f'Seeded new-category scores for {seeded} candidates '
          f'(conservative={by_lean["conservative"]}, progressive={by_lean["progressive"]})')
    print(f'  left null (ambiguous/sparse God First record): {skipped_ambiguous}')
    print(f'  skipped (federal — no new categories): {skipped_federal}')


if __name__ == '__main__':
    main()
