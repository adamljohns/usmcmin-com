#!/usr/bin/env python3
"""build-resolute-digests.py — compact RESOLUTE digests for the OpenClaw PSA agents.

Reads the LIVE pushed scorecard.json + issues.json (via `git show origin/main:…`,
falling back to the working tree) and writes small, agent-readable JSON snapshots to
~/.openclaw/shared-memory/context/ — matching the cron-fed snapshot pattern the agents
already consume (news-rss-latest.json, fxbg-civic-latest.json):

  resolute-measures-latest.json        -> Sheriff Roy : "what new laws / ballot measures are being voted on"
  resolute-congress-latest.json        -> Rush        : Adam's VA delegation, cited votes inline ("my congressman")
  resolute-congress-index-latest.json  -> Rush        : every sitting US House member + Senator, terse, for lookup

The agents have read + web_fetch only (no shell), so these files are their lookup table;
the live site (usmcmin.com) is the citation + web_fetch target for the full detail.
"""
import json, os, re, subprocess, sys
from datetime import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.expanduser('~/.openclaw/shared-memory/context')
SITE = 'https://usmcmin.com'


def load_live(relpath):
    """Latest pushed version via git; fall back to the working tree."""
    try:
        subprocess.run(['git', '-C', REPO, 'fetch', 'origin', 'main', '-q'], timeout=60, check=False)
        blob = subprocess.check_output(['git', '-C', REPO, 'show', f'origin/main:{relpath}'], timeout=120)
        return json.loads(blob)
    except Exception as e:
        sys.stderr.write(f'git show {relpath} failed ({e}); reading working tree\n')
        with open(os.path.join(REPO, relpath), encoding='utf-8') as f:
            return json.load(f)


def pct(c):
    """Headline score = TRUE / (TRUE+FALSE) across all scoreable cells (null / N/A excluded)."""
    t = f = 0
    for arr in (c.get('scores') or {}).values():
        for v in arr:
            if v is True:
                t += 1
            elif v is False:
                f += 1
    return round(100 * t / (t + f)) if (t + f) else None


def prof_url(c):
    return f"{SITE}/candidates/{(c.get('state') or '').lower()}/{c.get('slug')}.html"


def top_claims(c, n=4):
    out = []
    for cl in (c.get('claims') or [])[:n]:
        srcs = cl.get('sources') or []
        out.append({
            'text': cl.get('text'),
            'impact': 'supports' if cl.get('score_impact') else 'opposes',
            'category': cl.get('category'),
            'src': srcs[0] if srcs else None,
        })
    return out


def ratings(c):
    p = c.get('profile') or {}
    r = {}
    for k, label in (('nra_rating', 'NRA'), ('heritage_action', 'Heritage Action'),
                     ('planned_parenthood', 'Planned Parenthood')):
        if p.get(k):
            r[label] = p[k]
    return r


def clean_seat(c):
    """Terse seat label — strip any '(...)' or ' · ...' annotation off the office string."""
    off = c.get('office') or ''
    return re.split(r'\s+\(|\s+·\s+', off)[0].strip()


def is_incumbent(c):
    """A currently-sitting US House member or Senator (not a challenger/nominee/dropout).
    Primary signal: a bioguide ID (Congress members have one; challengers don't). Fallback:
    a clean seat string with no candidacy annotation (catches sitting members missing a bioguide)."""
    if c.get('level') != 'federal' or (c.get('status') or 'active') != 'active':
        return False
    if (c.get('profile') or {}).get('bioguide'):
        return True
    off = (c.get('office') or '')
    low = off.lower()
    if any(w in low for w in ('candidate', 'nominee', 'challenger', 'withdrew', 'suspend', ' lost', 'former')):
        return False  # challengers carry a candidacy annotation; sitting members don't
    if off.strip() in ('U.S. Senator', 'United States Senator', 'U.S. Senate'):
        return True
    return bool(re.search(r'district\s+\d+', low) or re.search(r'\b[a-z]{2}-\d+\b', low))


def trunc(s, n=240):
    s = (s or '').strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def main():
    now = datetime.now().isoformat(timespec='seconds')
    sc = load_live('data/scorecard.json')
    iss = load_live('data/issues.json')
    C = sc['candidates']
    os.makedirs(OUT, exist_ok=True)

    # ---- Sheriff Roy: 2026 ballot measures / "new laws being voted on" ----
    measures = []
    for m in iss['issues']:
        measures.append({
            'title': m.get('title'),
            'state': m.get('state'),
            'date': m.get('date'),
            'category': m.get('category'),
            'urgency_label': m.get('urgency_label'),
            'summary': trunc(m.get('summary'), 160),
            'url': f"{SITE}/issues/{m.get('slug')}.html",
        })
    measures.sort(key=lambda x: (x.get('state') or 'ZZ', x.get('title') or ''))
    roy = {
        'ts_local': now,
        'source': 'usmcmin.com — RESOLUTE Citizen (2026 statewide ballot measures)',
        'note': ('Curated, source-cited 2026 ballot measures + constitutional amendments. '
                 'Refreshed by com.moop.resolute-digests. Cite the per-measure url; full hub at '
                 + SITE + '/citizen-issues.html'),
        'count': len(measures),
        'measures': measures,
    }
    with open(os.path.join(OUT, 'resolute-measures-latest.json'), 'w', encoding='utf-8') as fh:
        json.dump(roy, fh, ensure_ascii=False, separators=(',', ':'))

    # ---- Rush: Adam's VA delegation, cited votes inline ("my congressman") ----
    home = {}
    for c in C:
        if c.get('state') == 'VA' and is_incumbent(c):
            home[c['slug']] = {
                'name': c.get('name'), 'seat': clean_seat(c), 'party': c.get('party'),
                'score': pct(c), 'confidence': (c.get('profile') or {}).get('confidence'),
                'url': prof_url(c), 'ratings': ratings(c), 'top_claims': top_claims(c),
            }
    rush_home = {
        'ts_local': now,
        'source': 'usmcmin.com — RESOLUTE Citizen scorecard',
        'note': ("Curated, cited position record (key votes, sponsorships, ratings) — NOT a live "
                 "roll-call feed. Adam's US House member is Rob Wittman (VA-01). "
                 "Refreshed by com.moop.resolute-digests."),
        'home_delegation': home,
        'index_file': '~/.openclaw/shared-memory/context/resolute-congress-index-latest.json',
    }
    with open(os.path.join(OUT, 'resolute-congress-latest.json'), 'w', encoding='utf-8') as fh:
        json.dump(rush_home, fh, indent=1, ensure_ascii=False)

    # ---- Rush: every sitting US House member + Senator, terse, for lookup ----
    index = []
    for c in C:
        if is_incumbent(c):
            index.append({'n': c.get('name'), 'st': c.get('state'), 'seat': clean_seat(c),
                          'p': c.get('party'), 'score': pct(c), 'url': prof_url(c)})
    index.sort(key=lambda x: (x.get('st') or 'ZZ', x.get('seat') or ''))
    rush_index = {
        'ts_local': now,
        'source': 'usmcmin.com — RESOLUTE Citizen scorecard',
        'note': 'Every sitting US House member + Senator, terse. For full cited votes, web_fetch the url (profile page).',
        'count': len(index),
        'index': index,
    }
    with open(os.path.join(OUT, 'resolute-congress-index-latest.json'), 'w', encoding='utf-8') as fh:
        json.dump(rush_index, fh, ensure_ascii=False, separators=(',', ':'))

    print(f"OK {now}")
    print(f"  measures:            {len(measures):4}  -> resolute-measures-latest.json")
    print(f"  home_delegation(VA): {len(home):4}  -> resolute-congress-latest.json")
    print(f"  federal index:       {len(index):4}  -> resolute-congress-index-latest.json")


if __name__ == '__main__':
    main()
