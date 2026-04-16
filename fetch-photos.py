#!/usr/bin/env python3
"""
fetch-photos.py — download official portraits from Wikipedia/Wikimedia Commons
for candidates in scorecard.json and update the photo field.

Targets the highest-profile officials first: President, VP, Cabinet, SCOTUS,
governors, and US senators. These are almost all public domain (US government
works). Downloads to assets/photos/{state}/{slug}.jpg and sets candidate.photo
to the relative path.

Usage:
    python3 fetch-photos.py              # fetch photos for top officials
    python3 fetch-photos.py --all        # fetch photos for ALL candidates (slow)
    python3 fetch-photos.py --dry        # report what would be fetched, download nothing
    python3 fetch-photos.py --force      # re-download even if photo already exists on disk

Rate-limits to ~2 requests/second to be a good Wikipedia API citizen.
"""
import json
import os
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'
PHOTOS_DIR = BASE_DIR / 'assets' / 'photos'
WIKI_THUMB_SIZE = 300  # px — enough for a 96px avatar at 3x retina

# Wikipedia article name overrides for candidates whose names don't directly
# match their Wikipedia article title (disambiguation, middle names, etc.).
WIKI_NAME_OVERRIDES = {
    'donald-j-trump': 'Donald Trump',
    'john-g-roberts-jr': 'John Roberts (judge)',
    'samuel-a-alito-jr': 'Samuel Alito',
    'neil-m-gorsuch': 'Neil Gorsuch',
    'brett-m-kavanaugh': 'Brett Kavanaugh',
    'ketanji-brown-jackson': 'Ketanji Brown Jackson',
    'sonia-sotomayor': 'Sonia Sotomayor',
    'elena-kagan': 'Elena Kagan',
    'amy-coney-barrett': 'Amy Coney Barrett',
    'clarence-thomas': 'Clarence Thomas',
    'jd-vance': 'JD Vance',
    'marco-rubio': 'Marco Rubio',
    'pete-hegseth': 'Pete Hegseth',
    'robert-f-kennedy-jr': 'Robert F. Kennedy Jr.',
    'tulsi-gabbard': 'Tulsi Gabbard',
    'kristi-noem': 'Kristi Noem',
    'doug-burgum': 'Doug Burgum',
    'lee-zeldin': 'Lee Zeldin',
    'susie-wiles': 'Susie Wiles',
    'nick-begich-iii': 'Nick Begich III',
    'eleanor-holmes-norton': 'Eleanor Holmes Norton',
    'bobby-scott': 'Bobby Scott (politician)',
}


def wiki_portrait_url(name, slug):
    """Query Wikipedia API for a person's main image thumbnail URL."""
    query_name = WIKI_NAME_OVERRIDES.get(slug, name)
    params = urllib.parse.urlencode({
        'action': 'query',
        'titles': query_name,
        'prop': 'pageimages',
        'format': 'json',
        'pithumbsize': WIKI_THUMB_SIZE,
        'redirects': 1,
    })
    url = f"https://en.wikipedia.org/w/api.php?{params}"
    r = subprocess.run(
        ['curl', '-s', '-A', 'USMCMin-PhotoEnrich/1.0 (usmcmin.com)', url],
        capture_output=True, text=True, timeout=15,
    )
    if r.returncode != 0:
        return None
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        return None
    pages = data.get('query', {}).get('pages', {})
    for pid, page in pages.items():
        if pid == '-1':
            continue
        thumb = page.get('thumbnail', {})
        if thumb and thumb.get('source'):
            return thumb['source']
    return None


def download_image(url, dest):
    """Download an image from url to dest path. Returns True on success.
    Validates that the result is actually a JPEG (magic bytes FF D8)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ['curl', '-s', '-L', '-o', str(dest), url],
        capture_output=True, timeout=30,
    )
    if r.returncode != 0 or not dest.exists():
        return False
    # Check file size and JPEG magic bytes
    if dest.stat().st_size < 1000:
        dest.unlink()
        return False
    with open(dest, 'rb') as f:
        magic = f.read(2)
    if magic != b'\xff\xd8':
        # Got an HTML error page or other non-JPEG response
        dest.unlink()
        return False
    return True


def select_targets(candidates, fetch_all=False):
    """Return the list of candidates to fetch photos for."""
    if fetch_all:
        return [c for c in candidates if c.get('slug')]

    # High-profile targets: executive, judicial, governors, US senators
    targets = []
    for c in candidates:
        if not c.get('slug'):
            continue
        level = c.get('level', '')
        office = (c.get('office') or '').lower()
        jurisdiction = (c.get('jurisdiction') or '').lower()

        if level in ('executive', 'judicial'):
            targets.append(c)
        elif 'governor' in office:
            targets.append(c)
        elif level == 'federal' and 'senate' in jurisdiction and 'state' not in jurisdiction:
            targets.append(c)
        # Skip House + state legislators + local for now (too many, do in batches)

    return targets


def main():
    args = set(sys.argv[1:])
    dry = '--dry' in args or '--dry-run' in args
    force = '--force' in args
    fetch_all = '--all' in args

    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    targets = select_targets(data['candidates'], fetch_all=fetch_all)
    print(f"Photo targets: {len(targets)} candidates")

    fetched = 0
    skipped = 0
    failed = 0
    already = 0
    changed = False

    for i, c in enumerate(targets):
        slug = c['slug']
        state = (c.get('state') or 'us').lower()
        photo_rel = f"assets/photos/{state}/{slug}.jpg"
        photo_path = BASE_DIR / photo_rel

        # Skip if photo already exists on disk (unless --force)
        if photo_path.exists() and not force:
            if not c.get('photo'):
                # File exists but scorecard doesn't know — fix the reference
                c['photo'] = photo_rel
                changed = True
            already += 1
            continue

        if dry:
            print(f"  [{i+1}/{len(targets)}] WOULD fetch: {c['name']} ({state})")
            skipped += 1
            continue

        # Rate limit: ~2 req/s (one for API, one for download)
        if fetched > 0:
            time.sleep(0.5)

        url = wiki_portrait_url(c['name'], slug)
        if not url:
            print(f"  [{i+1}/{len(targets)}] ✗ {c['name']} — no Wikipedia image")
            failed += 1
            continue

        if download_image(url, photo_path):
            c['photo'] = photo_rel
            changed = True
            fetched += 1
            size_kb = round(photo_path.stat().st_size / 1024)
            if (fetched % 10 == 0) or fetched <= 5:
                print(f"  [{i+1}/{len(targets)}] ✓ {c['name']} ({size_kb} KB)")
        else:
            print(f"  [{i+1}/{len(targets)}] ✗ {c['name']} — download failed")
            failed += 1

    print(f"\nResults: {fetched} fetched, {already} already existed, "
          f"{failed} failed, {skipped} skipped")

    if changed and not dry:
        # Update scorecard.json with photo paths
        with open(SCORECARD_PATH, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Updated scorecard.json with {fetched + (1 if already else 0)} photo paths")

        # Rebuild per-state files
        print("\nRebuilding per-state files via build-data.py...")
        subprocess.run(
            [sys.executable, str(BASE_DIR / 'build-data.py')],
            check=True,
        )
    elif dry:
        print("DRY RUN — no files written")


if __name__ == '__main__':
    main()
