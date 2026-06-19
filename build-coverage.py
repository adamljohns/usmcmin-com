#!/usr/bin/env python3
"""
build-coverage.py — emit data/coverage-by-state.json: a state-by-state
transparency rollup of how much of the scorecard is backed by cited
public-record evidence (vs party-default scaffolding).

READS data/scorecard.json (master) READ-ONLY. NEVER modifies it.
Writes ONE new file: data/coverage-by-state.json.

"evidence_scored" here means a candidate carries AT LEAST ONE answer that
is backed by a citation — i.e. some entry in `answer_footnotes` has a
non-empty footnote-ref list. That is the evidence-first line the site
draws: a cited public-record position, as opposed to a party-default
answer with no source. (A candidate can have True/False answers from
party-default scaffolding and still NOT be evidence_scored.)

Level buckets use tier_classify.classify_office_tier (federal|state|local)
so they line up with build-search-index.py and the profile pages.

Output schema:
  {
    "generated": "<ISO-8601 UTC>",
    "generated_from": "data/scorecard.json",
    "national": {
      "total": <int>, "evidence_scored": <int>, "pct": <float 0-100>,
      "by_level": {"federal": {...}, "state": {...}, "local": {...}}
    },
    "states": [
      {"state": "VA", "total": .., "evidence_scored": .., "pct": ..,
       "by_level": {"federal": {"total":..,"evidence_scored":..,"pct":..},
                    "state": {...}, "local": {...}}},
      ...  # sorted by state code
    ]
  }

Run from repo root: python3 build-coverage.py
"""
import json
import os
from datetime import datetime, timezone

from tier_classify import classify_office_tier

SRC = 'data/scorecard.json'
STATS = 'data/stats.json'
OUT = 'data/coverage-by-state.json'
LEVELS = ('federal', 'state', 'local')


def is_evidence_scored(c):
    """True if the candidate has >=1 answer carrying a citation footnote."""
    af = c.get('answer_footnotes') or {}
    for refs_per_q in af.values():
        if isinstance(refs_per_q, list):
            for refs in refs_per_q:
                if isinstance(refs, list) and refs:
                    return True
    return False


def pct(scored, total):
    return round(scored / total * 100, 1) if total else 0.0


def blank_level():
    return {'total': 0, 'evidence_scored': 0}


def main():
    with open(SRC) as f:
        sc = json.load(f)
    candidates = sc.get('candidates', [])

    states = {}            # code -> {total, evidence_scored, by_level{level:{total,evidence_scored}}}
    nat = {'total': 0, 'evidence_scored': 0,
           'by_level': {lv: blank_level() for lv in LEVELS}}

    for c in candidates:
        code = (c.get('state') or 'US').upper()
        level = classify_office_tier(c) or 'federal'
        if level not in LEVELS:
            level = 'federal'
        ev = is_evidence_scored(c)

        st = states.setdefault(code, {
            'total': 0, 'evidence_scored': 0,
            'by_level': {lv: blank_level() for lv in LEVELS},
        })
        st['total'] += 1
        st['by_level'][level]['total'] += 1
        nat['total'] += 1
        nat['by_level'][level]['total'] += 1
        if ev:
            st['evidence_scored'] += 1
            st['by_level'][level]['evidence_scored'] += 1
            nat['evidence_scored'] += 1
            nat['by_level'][level]['evidence_scored'] += 1

    def finish(node):
        node['pct'] = pct(node['evidence_scored'], node['total'])
        for lv in LEVELS:
            b = node['by_level'][lv]
            b['pct'] = pct(b['evidence_scored'], b['total'])
        return node

    finish(nat)
    state_rows = [finish({'state': code, **st})
                  for code, st in sorted(states.items())]

    payload = {
        'generated': datetime.now(timezone.utc).isoformat(),
        'generated_from': SRC,
        'national': nat,
        'states': state_rows,
    }

    with open(OUT, 'w') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write('\n')

    # Validate: the JSON parses, and the national total is a sane match for
    # the committed stats.json snapshot (small drift is expected — the
    # refinement crons own scorecard.json and stats.json is a periodic
    # snapshot, so they can disagree by a handful of candidates).
    with open(OUT) as f:
        reparsed = json.load(f)
    assert reparsed['national']['total'] == len(candidates), 'national total != candidate count'

    try:
        stats_total = json.load(open(STATS))['totals']['candidates']
        drift = nat['total'] - stats_total
        flag = 'OK' if abs(drift) <= 25 else 'WARN — large drift, investigate'
        print(f"national total {nat['total']} vs stats.json {stats_total} (drift {drift:+d}) — {flag}")
    except Exception as e:
        print(f"stats.json cross-check skipped: {e}")

    size_kb = os.path.getsize(OUT) / 1024
    print(f"Wrote {OUT} — {len(state_rows)} states, "
          f"{nat['evidence_scored']}/{nat['total']} evidence-scored "
          f"({nat['pct']}%), {size_kb:.1f} KB")


if __name__ == '__main__':
    main()
