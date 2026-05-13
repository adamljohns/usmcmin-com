#!/usr/bin/env python3
"""
apply-aipac-adjustments.py — apply AIPAC bonus / penalty to the
RESOLUTE Citizen total based on data/aipac_adjustments.json.

Methodology (from Adam, 2026-04-29):
  "Configure any candidate receiving AIPAC funding to be heavily
   penalized in their score in proportion to the millions they've
   gotten in campaign contributions; any who receive zero funds
   should be boosted by at least 7 points."

Schedule (data/aipac_adjustments.json carries authoritative copy):

    $0 verified         -> +7  (RESOLUTE bonus)
    $1 - $50,000        -> -3
    $50,001 - $250,000  -> -10
    $250,001 - $1M      -> -20
    $1M - $3M           -> -35
    $3M+                -> -50

Each candidate's record gets a `score_adjustments` block:

    score_adjustments: {
      aipac: {
        delta: -10,
        bracket: "50k_to_250k",
        dollars: 175000,
        note: "...",
        sources: ["...", "..."],
        applied_on: "YYYY-MM-DD"
      }
    }

The RENDERER (generate-profiles.py + citizen.html / citizen-table.html
total computations) reads `score_adjustments.aipac.delta` and adds it
to the base 70-point category-sum total to produce the final score.

Run once after editing data/aipac_adjustments.json; idempotent.
"""
import json
import os
import subprocess
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
ADJUST = os.path.join(REPO, 'data', 'aipac_adjustments.json')

# Bracket -> point delta mapping.  Source of truth: aipac_adjustments.json
# `_meta.schedule` strings; this dict translates the bracket name into the
# numeric delta.
BRACKET_DELTA = {
    'verified_zero': 7,
    '1_to_50k':       -3,
    '50k_to_250k':   -10,
    '250k_to_1m':    -20,
    '1m_to_3m':      -35,
    '3m_plus':       -50,
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
    applied_on = []
    not_found = []

    entries = adj.get('entries', {})
    candidate_index = {c.get('slug'): c for c in sc['candidates']}

    for key, info in entries.items():
        slug = info.get('slug') or key
        cand = candidate_index.get(slug)
        if not cand:
            not_found.append(slug)
            continue

        dollars = float(info.get('dollars') or 0)
        # Allow explicit category override (in case a record has unusual
        # context that the bracket rule wouldn't capture cleanly).
        bracket = info.get('category') or bracket_for(dollars)
        delta = BRACKET_DELTA.get(bracket, 0)

        prof = cand.setdefault('profile', {})
        adjustments = prof.setdefault('score_adjustments', {})
        adjustments['aipac'] = {
            'delta': delta,
            'bracket': bracket,
            'dollars': dollars,
            'note': info.get('note', ''),
            'sources': list(info.get('sources') or []),
            'applied_on': today,
        }
        applied_on.append((slug, delta, bracket, int(dollars)))

    # Update meta with methodology + schedule mirror so a reader of
    # scorecard.json sees the rule that produced the adjustments.
    sc['meta']['aipac_adjustment'] = {
        'description': (
            "Per-candidate score adjustments applied based on documented "
            "AIPAC / pro-Israel-lobby campaign contributions. +7 points "
            "for verified-zero; graduated penalties from -3 to -50 in "
            "proportion to documented dollar totals. Adjustments are "
            "applied to the candidate's profile.score_adjustments.aipac "
            "block; the renderer adds delta to the base 70-point total."
        ),
        'schedule': {
            'verified_zero': 7,
            '1_to_50k':      -3,
            '50k_to_250k':  -10,
            '250k_to_1m':   -20,
            '1m_to_3m':     -35,
            '3m_plus':      -50,
        },
        'source_data': 'data/aipac_adjustments.json',
        'last_applied': today,
        'applied_count': len(applied_on),
    }
    sc['meta']['last_updated'] = today

    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)

    print(f'Applied AIPAC adjustments to {len(applied_on)} candidate(s):')
    for slug, delta, bracket, dollars in applied_on:
        sign = '+' if delta > 0 else ''
        print(f'  {slug:30s}  ${dollars:>10,d}   {bracket:18s}  {sign}{delta:+d}')
    if not_found:
        print(f'\nNot found in scorecard (skipped): {not_found}')

    subprocess.run(['python3', os.path.join(REPO, 'build-data.py')], check=True)


if __name__ == '__main__':
    main()
