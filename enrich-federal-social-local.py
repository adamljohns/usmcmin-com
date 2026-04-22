#!/usr/bin/env python3
"""
enrich-federal-social-local.py — add Facebook, YouTube, and district-office
contact info to every US Senator and US House member.

Sources (community-maintained, public domain):
  https://unitedstates.github.io/congress-legislators/legislators-social-media.json
  https://unitedstates.github.io/congress-legislators/legislators-district-offices.json

Matching is by bioguide ID (populated on every federal candidate by
enrich-phones.py in commit b31b57f7f).

For each federal candidate, adds to their profile:
    facebook         — Facebook username/page slug
    youtube          — YouTube channel ID
    district_offices — [ {city, state, phone, address, zip, lat, lng}, ... ]

The district_offices list is particularly high-value: constituents calling
the LOCAL office typically get more personal attention than the DC switch-
board. Every US House rep has at least one district office, often two or
three scattered across their district.

Twitter is already enriched (528/534 from our earlier pass); this script
only fills in profile.twitter if it wasn't already set.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'

SOCIAL_URL = 'https://unitedstates.github.io/congress-legislators/legislators-social-media.json'
OFFICES_URL = 'https://unitedstates.github.io/congress-legislators/legislators-district-offices.json'
SOCIAL_CACHE = Path('/tmp/legislators-social.json')
OFFICES_CACHE = Path('/tmp/legislators-district-offices.json')
UA = 'USMCMin-FederalEnrich/1.0 (usmcmin.com)'


def fetch(url, cache, force=False):
    if cache.exists() and cache.stat().st_size > 1000 and not force:
        with open(cache) as f:
            return json.load(f)
    r = subprocess.run(['curl', '-s', '-L', '-A', UA, '-o', str(cache), url],
                       capture_output=True, timeout=60)
    if r.returncode != 0:
        print(f'ERROR fetching {url}', file=sys.stderr)
        sys.exit(1)
    with open(cache) as f:
        return json.load(f)


def main():
    force = '--force' in sys.argv

    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    # Index both datasets by bioguide
    print('Loading datasets...')
    social = fetch(SOCIAL_URL, SOCIAL_CACHE, force=force)
    offices = fetch(OFFICES_URL, OFFICES_CACHE, force=force)

    social_by_bg = {s['id']['bioguide']: s.get('social', {}) for s in social if s.get('id', {}).get('bioguide')}
    offices_by_bg = {o['id']['bioguide']: o.get('offices', []) for o in offices if o.get('id', {}).get('bioguide')}
    print(f'  social handles: {len(social_by_bg)}')
    print(f'  district-office sets: {len(offices_by_bg)}')

    changed_count = 0
    missing_bg = 0
    fb_added = 0
    yt_added = 0
    tw_added = 0
    offices_added = 0

    for c in data['candidates']:
        if c.get('level') != 'federal':
            continue
        profile = c.setdefault('profile', {})
        bg = profile.get('bioguide')
        if not bg:
            missing_bg += 1
            continue

        social_entry = social_by_bg.get(bg, {})
        changed = False

        if social_entry.get('twitter') and not profile.get('twitter'):
            profile['twitter'] = '@' + social_entry['twitter']
            tw_added += 1
            changed = True
        if social_entry.get('facebook') and not profile.get('facebook'):
            profile['facebook'] = social_entry['facebook']
            fb_added += 1
            changed = True
        if social_entry.get('youtube_id') and not profile.get('youtube'):
            profile['youtube'] = social_entry['youtube_id']
            yt_added += 1
            changed = True

        # District offices — keep the list compact; each office becomes
        # {city, state, phone, address_line, zip}
        dos = offices_by_bg.get(bg, [])
        if dos and not profile.get('district_offices'):
            compact = []
            for o in dos:
                entry = {}
                if o.get('city'): entry['city'] = o['city']
                if o.get('state'): entry['state'] = o['state']
                if o.get('phone'): entry['phone'] = o['phone']
                # Combine address lines
                # Fields can arrive as ints (e.g., suite = 205). Coerce to str.
                addr_parts = []
                if o.get('address'): addr_parts.append(str(o['address']))
                if o.get('suite'): addr_parts.append(str(o['suite']))
                if o.get('building'): addr_parts.append(str(o['building']))
                if addr_parts:
                    entry['address'] = ', '.join(addr_parts)
                if o.get('zip'): entry['zip'] = o['zip']
                if entry:
                    compact.append(entry)
            if compact:
                profile['district_offices'] = compact
                offices_added += 1
                changed = True

        if changed:
            changed_count += 1

    print(f'\nTotal federal candidates changed: {changed_count}')
    print(f'  Twitter added: {tw_added}')
    print(f'  Facebook added: {fb_added}')
    print(f'  YouTube added: {yt_added}')
    print(f'  District-office sets added: {offices_added}')
    if missing_bg:
        print(f'  (skipped {missing_bg} federal candidates lacking bioguide IDs)')

    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)

    print('\nRebuilding per-state files...')
    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
