"""
source_bias.py — resolve any URL against data/source_bias.json.

Used by generate-profiles.py to render bias badges next to every
source URL, and by (future) extract-claims.py to annotate claims
with source-diversity metadata.

Resolution strategy (first match wins):
  1. Exact host match (after stripping `www.` and trailing dot).
  2. Registrable-parent host match (e.g., `www.sub.example.com` →
     try `sub.example.com` → try `example.com`).
  3. Rule-based fallbacks for obviously-classifiable patterns:
       *.house.gov, *.senate.gov          → official_gov federal
       governor.<state>.gov, gov.<state>.gov → official_gov state
       any *.gov, *.mil                    → official_gov (conservative)
  4. Unknown → returns a minimal entry with type="unknown" so callers
     can still render something truthful ("Unclassified source").

The helper is deliberately pure-Python with no external deps so
this module can be imported by build-time scripts and by any
future CI check that validates sources.
"""

from __future__ import annotations

import json
import os
import re
from typing import Optional
from urllib.parse import urlparse

_BIAS_PATH = os.path.join(os.path.dirname(__file__), 'data', 'source_bias.json')

# Populated lazily on first resolve().
_DATA: Optional[dict] = None
_DOMAINS: Optional[dict] = None


def _load() -> dict:
    global _DATA, _DOMAINS
    if _DATA is None:
        with open(_BIAS_PATH, 'r', encoding='utf-8') as f:
            _DATA = json.load(f)
        _DOMAINS = _DATA.get('domains', {})
    return _DATA


def _host_from_url(url: str) -> str:
    """Lowercased host with `www.` stripped; empty string on parse failure."""
    try:
        parsed = urlparse(url.strip())
        host = (parsed.hostname or '').lower().rstrip('.')
        if host.startswith('www.'):
            host = host[4:]
        return host
    except Exception:
        return ''


# Ordered (most-specific first) fallback rules. Each entry is a
# (predicate(host) -> bool, template entry dict).
_FALLBACK_RULES = [
    (
        lambda h: h.endswith('.house.gov') or h == 'house.gov',
        {
            'display_name': 'U.S. House — Member Site',
            'type': 'official_gov',
            '_match': 'rule:*.house.gov',
        },
    ),
    (
        lambda h: h.endswith('.senate.gov') or h == 'senate.gov',
        {
            'display_name': 'U.S. Senate — Member Site',
            'type': 'official_gov',
            '_match': 'rule:*.senate.gov',
        },
    ),
    (
        lambda h: re.match(r'^(governor|gov)\.[a-z]{2}\.gov$', h) is not None,
        {
            'display_name': "State Governor's Office",
            'type': 'official_gov',
            '_match': 'rule:governor.<st>.gov',
        },
    ),
    (
        lambda h: h.endswith('.uscourts.gov') or h == 'uscourts.gov',
        {
            'display_name': 'U.S. Courts',
            'type': 'official_gov',
            '_match': 'rule:*.uscourts.gov',
        },
    ),
    (
        lambda h: h.endswith('.mil') or h == 'mil',
        {
            'display_name': 'U.S. Military',
            'type': 'official_gov',
            '_match': 'rule:*.mil',
        },
    ),
    # Generic .gov fallback must run AFTER the specific ones above.
    (
        lambda h: h.endswith('.gov'),
        {
            'display_name': 'Official Government Source',
            'type': 'official_gov',
            '_match': 'rule:*.gov',
        },
    ),
]


def resolve(url: str) -> dict:
    """
    Resolve a URL to a bias entry. Always returns a dict with at least
    `type` and `display_name`. Callers should treat an unknown return
    as something to flag visually, not a hard error.

    The returned dict is a shallow copy of the source data plus a
    synthesized `_host` key for logging/debugging and a `_match`
    key indicating how the lookup resolved.
    """
    _load()
    host = _host_from_url(url)
    if not host:
        return {'type': 'unknown', 'display_name': 'Unresolvable URL', '_host': '', '_match': 'none'}

    # 1. Exact host match.
    entry = _DOMAINS.get(host)
    if entry is not None:
        out = dict(entry)
        out['_host'] = host
        out['_match'] = 'exact'
        return out

    # 2. Registrable-parent walk: `a.b.c.d` → `b.c.d` → `c.d`.
    parts = host.split('.')
    for i in range(1, len(parts) - 1):
        parent = '.'.join(parts[i:])
        entry = _DOMAINS.get(parent)
        if entry is not None:
            out = dict(entry)
            out['_host'] = host
            out['_match'] = f'parent:{parent}'
            return out

    # 3. Rule-based fallbacks.
    for predicate, template in _FALLBACK_RULES:
        if predicate(host):
            out = dict(template)
            out['_host'] = host
            return out

    # 4. Truly unknown.
    return {
        'type': 'unknown',
        'display_name': host or 'Unclassified source',
        '_host': host,
        '_match': 'none',
    }


def badge_label(entry: dict) -> str:
    """
    Short (≤ ~18 char) label for the bias chip on a source link.
    Examples:
      AllSides: Lean Left → "Lean Left"
      type=official_gov   → "Official"
      type=advocacy, lean=Right → "Right Advocacy"
      type=think_tank, lean=Right → "Right Think Tank"
      type=reference      → "Reference"
    """
    t = entry.get('type', 'unknown')
    allsides = entry.get('allsides')
    lean = entry.get('lean')

    if t == 'mainstream':
        return allsides or 'Mainstream'
    if t == 'official_gov':
        return 'Official'
    if t == 'reference':
        return allsides or 'Reference'
    if t == 'encyclopedia':
        return 'Encyclopedia'
    if t == 'think_tank':
        return f'{allsides or lean or ""} Think Tank'.strip()
    if t == 'advocacy':
        return f'{allsides or lean or ""} Advocacy'.strip()
    if t == 'local_news':
        return allsides or lean or 'Local News'
    if t == 'legal':
        return 'Primary Legal'
    if t == 'social':
        return 'Social'
    if t == 'cdn':
        return 'Hosted File'
    return 'Unclassified'


def badge_tone(entry: dict) -> str:
    """
    Return a short tone key that the CSS renders:
      left        — strongly left-leaning media/advocacy
      lean-left
      center
      lean-right
      right
      official    — official government source
      reference   — non-partisan civic data
      social      — social platform, user-driven
      neutral     — unclassified / encyclopedia / cdn / local news

    Advocacy and think_tank entries map to the AllSides rating if
    available, else to their `lean`.
    """
    allsides = entry.get('allsides')
    lean = entry.get('lean')
    t = entry.get('type', 'unknown')

    if t == 'official_gov':
        return 'official'
    if t == 'reference':
        # Honor AllSides if rated, else treat as reference-neutral.
        return {
            'Left': 'left', 'Lean Left': 'lean-left',
            'Center': 'center', 'Lean Right': 'lean-right',
            'Right': 'right',
        }.get(allsides, 'reference')
    if t == 'social':
        return 'social'
    if t in ('cdn', 'unknown', 'encyclopedia', 'legal'):
        return 'neutral'

    key = allsides or lean
    return {
        'Left': 'left', 'Lean Left': 'lean-left',
        'Center': 'center', 'Lean Right': 'lean-right',
        'Right': 'right',
    }.get(key, 'neutral')


def diversity_counts(urls: list) -> dict:
    """
    Given a list of source URLs, return aggregate counts keyed by a
    small vocabulary the UI renders as the Source Diversity strip.

    Keys: left, lean_left, center, lean_right, right, official,
          reference, social, neutral.
    """
    buckets = {
        'left': 0, 'lean_left': 0, 'center': 0, 'lean_right': 0, 'right': 0,
        'official': 0, 'reference': 0, 'social': 0, 'neutral': 0,
    }
    for url in urls or []:
        entry = resolve(url)
        tone = badge_tone(entry)
        key = tone.replace('-', '_')
        if key in buckets:
            buckets[key] += 1
        else:
            buckets['neutral'] += 1
    return buckets


if __name__ == '__main__':
    # Hand-sanity: pipe one URL per line on stdin.
    import sys
    for line in sys.stdin:
        u = line.strip()
        if not u:
            continue
        e = resolve(u)
        print(f'{u}\n  label: {badge_label(e)}  tone: {badge_tone(e)}  match: {e.get("_match")}')
