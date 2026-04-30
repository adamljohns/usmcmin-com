#!/usr/bin/env python3
"""
apply-soros-adjustments.py — Soros / Open Society sibling of
apply-aipac-adjustments.py.

Reads data/soros_adjustments.json. Applies the heavier penalty
curve Adam called for ("Soros money is a big penalty too... even
bigger than AIPAC").

Schedule:
    $0 verified         -> +7
    $1 - $50,000        -> -5
    $50,001 - $250,000  -> -15
    $250,001 - $1M      -> -30
    $1M - $3M           -> -50
    $3M+                -> -75

Each candidate's record gets a `score_adjustments.soros` block
(in addition to any existing `score_adjustments.aipac`). Deltas
sum across all sub-keys so a candidate clean of BOTH AIPAC and
Soros gets +14, while a top-tier recipient of both takes -125.

Run after editing data/soros_adjustments.json.
"""
import json
import os
import subprocess
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
ADJUST = os.path.join(REPO, 'data', 'soros_adjustments.json')

BRACKET_DELTA = {
    'verified_zero':  7,
    '1_to_50k':      -5,
    '50k_to_250k':  -15,
    '250k_to_1m':   -30,
    '1m_to_3m':     -50,
    '3m_plus':      -75,
}


def bracket_for(dollars: float) -> str:
    if dollars <= 0:
        return 'verified_zero'
    if dollars < 50_000:
        return '1_to_50k'
    if dollars < 250_000:
        return '50k_to_250k'
    if dollars < 1_000_000:
        return '250k_to_1m'
    if dollars < 3_000_000:
        return '1m_to_3m'
    return '3m_plus'


def main():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)
    with open(ADJUST, 'r', encoding='utf-8') as f:
        adj = json.load(f)

    today = date.today().isoformat()
    applied = []
    not_found = []

    candidate_index = {c.get('slug'): c for c in sc['candidates']}
    entries = adj.get('entries', {})

    for key, info in entries.items():
        slug = info.get('slug') or key
        cand = candidate_index.get(slug)
        if not cand:
            not_found.append(slug)
            continue

        dollars = float(info.get('dollars') or 0)
        bracket = info.get('category') or bracket_for(dollars)
        delta = BRACKET_DELTA.get(bracket, 0)

        prof = cand.setdefault('profile', {})
        adjustments = prof.setdefault('score_adjustments', {})
        adjustments['soros'] = {
            'delta': delta,
            'bracket': bracket,
            'dollars': dollars,
            'note': info.get('note', ''),
            'sources': list(info.get('sources') or []),
            'applied_on': today,
        }
        applied.append((slug, delta, bracket, int(dollars)))

    sc['meta']['soros_adjustment'] = {
        'description': (
            "Per-candidate score adjustments applied based on documented "
            "Soros / Open Society donor-network campaign contributions. "
            "Heavier penalty curve than AIPAC per Adam's stated methodology."
        ),
        'schedule': {k: v for k, v in BRACKET_DELTA.items()},
        'source_data': 'data/soros_adjustments.json',
        'last_applied': today,
        'applied_count': len(applied),
    }
    sc['meta']['last_updated'] = today

    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)

    print(f'Applied Soros adjustments to {len(applied)} candidate(s):')
    for slug, delta, bracket, dollars in applied:
        sign = '+' if delta > 0 else ''
        print(f'  {slug:25s}  ${dollars:>10,d}  {bracket:18s}  {sign}{delta:+d}')
    if not_found:
        print(f'\nNot in scorecard yet (skipped): {not_found}')

    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
