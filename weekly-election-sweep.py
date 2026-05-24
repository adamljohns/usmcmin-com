#!/usr/bin/env python3
"""
weekly-election-sweep.py — Surface scorecard records that need attention.

Operationalizes MAINTENANCE.md §3. Produces a markdown report of:
  1. RESOLVED-BUT-PENDING — records still marked `primary_candidate` whose
     election date has already passed. These races have happened; the result
     needs to be web-verified and the status updated.
  2. UPCOMING — races within the next N days (default 30), so you know what's
     about to need attention.
  3. STALE INCUMBENTS — sitting members whose `next_election_date` has passed
     but who are still `incumbent_seeking_reelection` (primary may have
     resolved; confirm they advanced).

This script DRAFTS a report. It does NOT change data — per the cardinal rule,
results must be web-verified by a human/agent before any status change.

Usage:
    python3 weekly-election-sweep.py [--days 30] [--out sweep-report.md]
"""
import json
import argparse
import datetime
from pathlib import Path
from collections import defaultdict

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'


def parse_date(s):
    try:
        return datetime.date.fromisoformat((s or '')[:10])
    except (ValueError, TypeError):
        return None


def office_short(c):
    o = (c.get('office') or '').strip()
    return o[:60] + '…' if len(o) > 61 else o


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--days', type=int, default=30, help='upcoming window (days)')
    ap.add_argument('--today', default=None, help='override today (YYYY-MM-DD)')
    ap.add_argument('--out', default=None, help='write report to file instead of stdout')
    ap.add_argument('--digest', action='store_true',
                    help='compact Telegram-friendly summary (counts + resolved-pending only)')
    args = ap.parse_args()

    today = parse_date(args.today) if args.today else datetime.date.today()
    horizon = today + datetime.timedelta(days=args.days)

    data = json.loads(SCORECARD.read_text())
    cands = data['candidates']

    resolved_pending = []
    upcoming = []
    stale_incumbents = []

    for c in cands:
        p = c.get('profile', {})
        ed = parse_date(p.get('next_election_date'))
        if not ed:
            continue
        cs = c.get('candidacy_status')
        row = (c.get('state'), c.get('district'), c.get('name'),
               office_short(c), ed.isoformat(), c.get('slug'))
        if cs == 'primary_candidate':
            if ed < today:
                resolved_pending.append(row)
            elif ed <= horizon:
                upcoming.append(row)
        elif cs == 'incumbent_seeking_reelection' and ed < today and p.get('next_election') == 2026:
            stale_incumbents.append(row)

    def fmt_section(title, rows, note):
        lines = [f'## {title} — {len(rows)}', '', f'_{note}_', '']
        if not rows:
            lines.append('_None._')
            return '\n'.join(lines) + '\n'
        by_state = defaultdict(list)
        for r in rows:
            by_state[r[0]].append(r)
        for st in sorted(by_state):
            lines.append(f'### {st} ({len(by_state[st])})')
            for state, dist, name, office, edate, slug in sorted(by_state[st], key=lambda x: (str(x[1]), x[2])):
                d = f'-{dist:02d}' if isinstance(dist, int) else ''
                lines.append(f'- **{name}** ({st}{d}) · {edate} · `{slug}`  \n  {office}')
            lines.append('')
        return '\n'.join(lines) + '\n'

    if args.digest:
        # Compact summary for Telegram (cap ~3500 chars)
        lines = [f'Scorecard sweep — {today.isoformat()}',
                 f'{len(resolved_pending)} resolved-pending · {len(upcoming)} upcoming({args.days}d) · '
                 f'{len(stale_incumbents)} incumbent-confirms',
                 '', '⚠️ RESOLVED, NEEDS RESULT (verify + update):']
        by_state = defaultdict(list)
        for r in resolved_pending:
            by_state[r[0]].append(r[2])
        for st in sorted(by_state):
            names = by_state[st]
            shown = ', '.join(names[:6]) + (f' +{len(names)-6} more' if len(names) > 6 else '')
            lines.append(f'• {st} ({len(names)}): {shown}')
        lines.append('')
        lines.append('Run `python3 weekly-election-sweep.py` in the repo for the full report.')
        out = '\n'.join(lines)[:3900]
        if args.out:
            Path(args.out).write_text(out)
        else:
            print(out)
        return

    report = []
    report.append('# Scorecard Election Sweep')
    report.append(f'\n_Generated {today.isoformat()} · horizon {args.days}d · '
                  f'{len(cands)} records scanned_\n')
    report.append('> **Cardinal rule:** web-verify every result before changing status. '
                  'Cite a reputable source (AP/NBC/CNN/state SoS) in the record.\n')
    report.append(fmt_section(
        '⚠️  RESOLVED BUT STILL PENDING (verify result + update)',
        resolved_pending,
        'Marked `primary_candidate` but the election date has passed. Web-verify '
        'the winner; set winners → `general_candidate`/`won`, losers → '
        '`lost_primary`. Add the opposing nominee if missing.'))
    report.append(fmt_section(
        '🔁  STALE INCUMBENTS (confirm they advanced)',
        stale_incumbents,
        'Sitting members still `incumbent_seeking_reelection` whose 2026 primary '
        'date has passed. Confirm they won renomination (most do); flag any upsets '
        'like Massie (KY-04).'))
    report.append(fmt_section(
        '📅  UPCOMING (next %d days)' % args.days,
        upcoming,
        'Races about to resolve. Pre-stage research; check back after the date.'))

    out = '\n'.join(report)
    if args.out:
        Path(args.out).write_text(out)
        print(f'Wrote {args.out} — {len(resolved_pending)} resolved-pending, '
              f'{len(stale_incumbents)} stale-incumbent, {len(upcoming)} upcoming')
    else:
        print(out)


if __name__ == '__main__':
    main()
