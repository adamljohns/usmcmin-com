#!/usr/bin/env python3
"""
enrich-phones.py — populate direct DC office phone numbers and contact URLs
for every US Senator and US Representative in scorecard.json, using the
well-maintained unitedstates/congress-legislators public dataset.

Source: https://unitedstates.github.io/congress-legislators/legislators-current.json
  (The `unitedstates` project is a community-maintained canonical list of
  current members of Congress with phone, office, contact form, bioguide,
  Twitter, etc. Same source used by GovTrack, ProPublica, and many civic
  apps. Public domain.)

For each federal candidate, we set:
    profile.phone        — direct DC office phone (e.g., "202-224-5274")
    profile.office       — DC office address
    profile.contact_form — contact form URL on the member's .gov site
    profile.bioguide     — bioguide ID (canonical congressional identifier)

Matching is strict — we require state + chamber + (district for House OR
name+state for Senate). Unmatched members are reported but not modified.

Idempotent: re-running overrides any existing values only if the upstream
dataset has changed.
"""
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'
SOURCE_URL = 'https://unitedstates.github.io/congress-legislators/legislators-current.json'
CACHE_PATH = Path('/tmp/legislators-current.json')


def fetch_legislators(force=False):
    """Fetch the current legislators JSON. Caches in /tmp to avoid repeated
    network calls during a single session; use --force to re-fetch."""
    if CACHE_PATH.exists() and not force:
        try:
            with open(CACHE_PATH) as f:
                return json.load(f)
        except Exception:
            pass
    print(f'Fetching {SOURCE_URL} ...')
    result = subprocess.run(
        ['curl', '-s', '-o', str(CACHE_PATH), '-L',
         '-A', 'USMCMin-PhoneEnrich/1.0 (usmcmin.com)',
         SOURCE_URL],
        capture_output=True, timeout=60,
    )
    if result.returncode != 0:
        print(f'ERROR: curl failed: {result.stderr.decode()}', file=sys.stderr)
        sys.exit(1)
    with open(CACHE_PATH) as f:
        return json.load(f)


def normalize_name(name):
    """Lowercase, strip accents + punctuation + title suffixes for fuzzy match."""
    if not name:
        return ''
    import unicodedata
    # Strip accents: "Luján" -> "Lujan"
    s = unicodedata.normalize('NFKD', name)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace('.', '').replace(',', '').replace("'", '').strip()
    # Strip common suffixes
    for suffix in [' jr', ' sr', ' iii', ' ii', ' iv']:
        if s.endswith(suffix):
            s = s[:-len(suffix)]
    return ' '.join(s.split())


def build_indexes(legislators):
    """Return (by_state_house_district, by_state_senate_name, by_name).

    Legislator records have:
      name.first, name.last, name.official_full (often includes middle initial)
    Our scorecard typically has "First Last" without middle. We register BOTH
    official_full AND plain "first last" as keys so either form matches.
    """
    by_house = {}        # (state, district) -> legislator
    by_senate = {}       # (state, normalized_name) -> legislator
    by_name_state = {}   # (state, normalized_name) -> legislator (global fallback)

    def register(state, names, leg, kind):
        for name in names:
            key = normalize_name(name)
            if not key:
                continue
            if kind == 'sen':
                by_senate.setdefault((state, key), leg)
            by_name_state.setdefault((state, key), leg)

    for leg in legislators:
        terms = leg.get('terms') or []
        if not terms:
            continue
        t = terms[-1]  # current term
        state = t.get('state')
        nm = leg.get('name') or {}
        first = nm.get('first') or ''
        last = nm.get('last') or ''
        nick = nm.get('nickname') or ''
        official_full = nm.get('official_full') or f'{first} {last}'
        plain = f'{first} {last}'
        nick_plain = f'{nick} {last}' if nick else ''
        names = [official_full, plain] + ([nick_plain] if nick_plain else [])

        if t.get('type') == 'rep':
            d = t.get('district')
            by_house[(state, d)] = leg
            # At-large states: the unitedstates dataset uses 0 for single-member
            # (at-large) districts (AK, DE, ND, SD, VT, WY). Scorecards often
            # number them as 1. Register both keys so either form matches.
            if d == 0:
                by_house[(state, 1)] = leg
            register(state, names, leg, 'rep')
            # Also register last-name-only for House fallback (less reliable
            # since two House members in the same state could share a last
            # name, but rare enough to be worth trying)
            if last:
                by_name_state.setdefault((state, normalize_name(last)), leg)
        elif t.get('type') == 'sen':
            register(state, names, leg, 'sen')
            # Senators: last name + state is unique (each state has <=2 senators
            # and they have distinct last names). Register last-name-only so
            # "Dick Durbin" matches "Richard Durbin".
            if last:
                by_senate.setdefault((state, normalize_name(last)), leg)
                by_name_state.setdefault((state, normalize_name(last)), leg)

    return by_house, by_senate, by_name_state


def match_candidate(c, by_house, by_senate, by_name_state):
    """Return the matching legislator dict or None."""
    state = (c.get('state') or '').upper()
    jurisdiction = c.get('jurisdiction') or ''
    district = c.get('district') if isinstance(c.get('district'), int) else None
    name_key = normalize_name(c.get('name') or '')

    # Last-name-only fallback: scorecard names like "Nick Begich III" have
    # suffixes not in the dataset's last-name field. Normalize and try the
    # last token.
    last_token_key = normalize_name(
        (c.get('name') or '').split()[-1] if c.get('name') else ''
    )
    # Actually the last token can be a suffix ("III"); walk backward from end
    # to find a non-suffix last token
    tokens = [normalize_name(x) for x in (c.get('name') or '').split()]
    tokens = [x for x in tokens if x not in ('iii','ii','iv','jr','sr')]
    last_token_key = tokens[-1] if tokens else ''

    if 'House of Representatives' in jurisdiction:
        if district is not None:
            leg = by_house.get((state, district))
            if leg:
                return leg
        # Fallback: name match
        leg = by_name_state.get((state, name_key))
        if leg:
            return leg
        # Final fallback: last name only
        return by_name_state.get((state, last_token_key))
    elif 'Senate' in jurisdiction and 'State Senate' not in jurisdiction:
        # "United States Senate" contains the substring "State" via "States",
        # so we must check for the compound 'State Senate' explicitly rather
        # than using `'State' not in jurisdiction` (the bug I hit before).
        leg = by_senate.get((state, name_key))
        if leg:
            return leg
        # Try last-name-only — works because each state has at most 2 senators
        leg = by_senate.get((state, last_token_key))
        if leg:
            return leg
        # Broad fallback
        return by_name_state.get((state, name_key)) or by_name_state.get((state, last_token_key))
    return None


def apply(candidate, leg):
    """Update candidate.profile with phone + office + contact_form + bioguide.
    Returns True if anything changed."""
    terms = leg.get('terms') or []
    if not terms:
        return False
    t = terms[-1]
    profile = candidate.setdefault('profile', {})
    changed = False

    phone = t.get('phone')
    office = t.get('office')
    form = t.get('contact_form')
    bioguide = (leg.get('id') or {}).get('bioguide')

    if phone and profile.get('phone') != phone:
        profile['phone'] = phone
        changed = True
    if office and profile.get('office') != office:
        profile['office'] = office
        changed = True
    if form and profile.get('contact_form') != form:
        profile['contact_form'] = form
        changed = True
    if bioguide and profile.get('bioguide') != bioguide:
        profile['bioguide'] = bioguide
        changed = True

    return changed


def main():
    force = '--force' in sys.argv[1:]

    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    legislators = fetch_legislators(force=force)
    print(f'Loaded {len(legislators)} current legislators')

    by_house, by_senate, by_name_state = build_indexes(legislators)

    matched = 0
    unmatched = []
    federal = [c for c in data['candidates'] if c.get('level') == 'federal']
    for c in federal:
        jurisdiction = c.get('jurisdiction') or ''
        # Only US Senate + US House — skip DC delegate (non-voting, jurisdiction is "District of Columbia")
        if 'United States' not in jurisdiction:
            continue
        leg = match_candidate(c, by_house, by_senate, by_name_state)
        if leg is None:
            unmatched.append(c)
            continue
        if apply(c, leg):
            matched += 1

    print(f'Enriched: {matched}')
    print(f'Unmatched: {len(unmatched)}')
    for c in unmatched[:10]:
        print(f'  - {c.get("name")} ({c.get("state")}, {c.get("jurisdiction")}, D{c.get("district")})')
    if len(unmatched) > 10:
        print(f'  ...and {len(unmatched)-10} more')

    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)

    print('\nRebuilding per-state files...')
    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
