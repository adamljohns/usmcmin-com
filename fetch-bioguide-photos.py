#!/usr/bin/env python3
"""
fetch-bioguide-photos.py — download official Congressional headshots from
bioguide.congress.gov for every federal candidate who has a bioguide ID but
no photo. This uses the predictable URL pattern:

    https://bioguide.congress.gov/bioguide/photo/{LETTER}/{BIOGUIDE}.jpg

Which reliably returns a JPEG for every current member of Congress.

Supplements fetch-photos.py (which relies on Wikipedia and misses lesser-known
reps). Where both succeed, we prefer the bioguide photo since it's the
canonical official portrait used by Congress itself.

Run after enrich-phones.py so candidates have bioguide IDs populated.
"""
import json
import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'
PHOTOS_DIR = BASE_DIR / 'assets' / 'photos'
UA = 'USMCMin-BioPhoto/1.0 (usmcmin.com)'


def bioguide_url(bioguide):
    letter = bioguide[0]
    return f'https://bioguide.congress.gov/bioguide/photo/{letter}/{bioguide}.jpg'


def download(url, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ['curl', '-sL', '-A', UA, '-o', str(dest), url],
        capture_output=True, timeout=30,
    )
    if r.returncode != 0 or not dest.exists():
        return False
    if dest.stat().st_size < 1000:
        dest.unlink()
        return False
    with open(dest, 'rb') as f:
        magic = f.read(2)
    if magic != b'\xff\xd8':
        dest.unlink()
        return False
    return True


def main():
    force = '--force' in sys.argv

    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    federal = [c for c in data['candidates']
               if c.get('level') == 'federal'
               and (c.get('profile') or {}).get('bioguide')]
    print(f'Federal candidates with bioguide IDs: {len(federal)}')

    fetched = 0
    already = 0
    failed = 0
    changed = False

    for i, c in enumerate(federal):
        profile = c.get('profile') or {}
        bg = profile.get('bioguide')
        state = (c.get('state') or 'us').lower()
        slug = c.get('slug')
        photo_rel = f'assets/photos/{state}/{slug}.jpg'
        photo_path = BASE_DIR / photo_rel

        if photo_path.exists() and not force:
            if not c.get('photo'):
                c['photo'] = photo_rel
                changed = True
            already += 1
            continue

        if fetched > 0:
            time.sleep(0.4)  # Be a good citizen of bioguide.congress.gov

        if download(bioguide_url(bg), photo_path):
            c['photo'] = photo_rel
            changed = True
            fetched += 1
            size_kb = round(photo_path.stat().st_size / 1024)
            if fetched % 50 == 0 or fetched <= 3:
                print(f'  [{i+1}/{len(federal)}] {c["name"]} ({bg}) {size_kb}KB')
        else:
            failed += 1
            print(f'  [{i+1}/{len(federal)}] ✗ {c["name"]} ({bg}) — download failed')

    print(f'\nResults: {fetched} fetched, {already} already had a photo, {failed} failed')

    if changed:
        with open(SCORECARD_PATH, 'w') as f:
            json.dump(data, f, indent=2)
        subprocess.run(
            [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
            check=True,
        )


if __name__ == '__main__':
    main()
