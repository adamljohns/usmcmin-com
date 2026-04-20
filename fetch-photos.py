#!/usr/bin/env python3
"""
fetch-photos.py — download official portraits from Wikipedia/Wikimedia Commons
for candidates in scorecard.json and update the photo field.

Downloads to assets/photos/{state}/{slug}.jpg and sets candidate.photo
to the relative path.

Usage:
    python3 fetch-photos.py                          # fetch top officials (gov/sen/scotus/exec)
    python3 fetch-photos.py --all                    # fetch photos for ALL candidates
    python3 fetch-photos.py --state FL               # fetch all FL candidates
    python3 fetch-photos.py --state FL --level state # fetch FL state-level only
    python3 fetch-photos.py --office senate          # fetch offices matching 'senate'
    python3 fetch-photos.py --dry                    # report, download nothing
    python3 fetch-photos.py --force                  # re-download existing photos
    python3 fetch-photos.py --limit 50               # cap at 50 fetches
    python3 fetch-photos.py --retry                  # re-try candidates without photos

Rate-limits to ~1.5 req/sec to be a good Wikipedia API citizen and avoid
Commons CDN rate limiting (which returns 2KB HTML error pages).
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
    'esteban-bovo-jr': 'Esteban Bovo',
    'carlos-g-muñiz': 'Carlos G. Muñiz',
}


def _wiki_api(params):
    """Call the Wikipedia API with the given params dict. Returns parsed JSON
    or None on failure."""
    url = f"https://en.wikipedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    r = subprocess.run(
        ['curl', '-s',
         '-A', 'USMCMin-PhotoEnrich/1.0 (usmcmin.com; admin@usmcmin.com)',
         url],
        capture_output=True, text=True, timeout=15,
    )
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


def _thumb_from_query(data):
    """Extract a thumbnail URL from an action=query|prop=pageimages response."""
    pages = (data or {}).get('query', {}).get('pages', {})
    for pid, page in pages.items():
        if pid == '-1':
            continue
        thumb = page.get('thumbnail', {})
        if thumb and thumb.get('source'):
            return thumb['source']
    return None


def wiki_portrait_url(name, slug, state=None, office=None):
    """Query Wikipedia API for a person's main image thumbnail URL.

    Strategy:
      1. Direct title lookup with redirects (handles well-known names).
      2. If override exists in WIKI_NAME_OVERRIDES, use that title.
      3. Fallback: opensearch with name + state + 'politician' to
         disambiguate state legislators from common-name collisions.
    """
    # 1 & 2: direct title lookup (using override if present)
    query_name = WIKI_NAME_OVERRIDES.get(slug, name)
    data = _wiki_api({
        'action': 'query', 'titles': query_name, 'prop': 'pageimages',
        'format': 'json', 'pithumbsize': WIKI_THUMB_SIZE, 'redirects': 1,
    })
    url = _thumb_from_query(data)
    if url:
        return url

    # 3: Disambiguation search. Try "name state politician" and take top result.
    if state:
        state_full = {
            'AL':'Alabama','AK':'Alaska','AZ':'Arizona','AR':'Arkansas',
            'CA':'California','CO':'Colorado','CT':'Connecticut','DE':'Delaware',
            'FL':'Florida','GA':'Georgia','HI':'Hawaii','ID':'Idaho',
            'IL':'Illinois','IN':'Indiana','IA':'Iowa','KS':'Kansas',
            'KY':'Kentucky','LA':'Louisiana','ME':'Maine','MD':'Maryland',
            'MA':'Massachusetts','MI':'Michigan','MN':'Minnesota','MS':'Mississippi',
            'MO':'Missouri','MT':'Montana','NE':'Nebraska','NV':'Nevada',
            'NH':'New Hampshire','NJ':'New Jersey','NM':'New Mexico','NY':'New York',
            'NC':'North Carolina','ND':'North Dakota','OH':'Ohio','OK':'Oklahoma',
            'OR':'Oregon','PA':'Pennsylvania','RI':'Rhode Island','SC':'South Carolina',
            'SD':'South Dakota','TN':'Tennessee','TX':'Texas','UT':'Utah',
            'VT':'Vermont','VA':'Virginia','WA':'Washington','WV':'West Virginia',
            'WI':'Wisconsin','WY':'Wyoming','DC':'District of Columbia',
        }.get((state or '').upper(), state or '')
        query = f"{name} {state_full} politician".strip()
        search = _wiki_api({
            'action': 'opensearch', 'search': query, 'limit': 3, 'format': 'json',
        })
        # opensearch returns [query, [titles], [descs], [urls]]
        if isinstance(search, list) and len(search) >= 2 and search[1]:
            # Try each result; pick the first one that has an image
            for candidate_title in search[1][:3]:
                data = _wiki_api({
                    'action': 'query', 'titles': candidate_title, 'prop': 'pageimages',
                    'format': 'json', 'pithumbsize': WIKI_THUMB_SIZE, 'redirects': 1,
                })
                url = _thumb_from_query(data)
                if url:
                    return url

    return None


def download_image(url, dest, retries=2):
    """Download an image from url to dest path. Returns True on success.
    Validates that the result is actually a JPEG or PNG (magic bytes)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(retries + 1):
        r = subprocess.run(
            ['curl', '-s', '-L',
             '-A', 'USMCMin-PhotoEnrich/1.0 (usmcmin.com; admin@usmcmin.com)',
             '-o', str(dest), url],
            capture_output=True, timeout=30,
        )
        if r.returncode != 0 or not dest.exists():
            if attempt < retries:
                time.sleep(2.0)
                continue
            return False
        # Check file size and magic bytes (JPEG FF D8, PNG 89 50)
        if dest.stat().st_size < 1000:
            dest.unlink()
            if attempt < retries:
                time.sleep(2.0)
                continue
            return False
        with open(dest, 'rb') as f:
            magic = f.read(4)
        if magic[:2] == b'\xff\xd8' or magic[:4] == b'\x89PNG':
            # Valid image; if it's a PNG we keep the .jpg extension — the
            # browser will still render it correctly based on Content-Type.
            return True
        # Got an HTML error page or other non-image response
        dest.unlink()
        if attempt < retries:
            # CDN rate limit — back off longer
            time.sleep(3.0)
            continue
        return False
    return False


def select_targets(candidates, fetch_all=False, state_filter=None,
                   level_filter=None, office_filter=None, retry_missing=False):
    """Return the list of candidates to fetch photos for, applying filters."""
    targets = []

    for c in candidates:
        if not c.get('slug'):
            continue
        state = (c.get('state') or '').upper()
        level = c.get('level') or ''
        office = (c.get('office') or '').lower()
        jurisdiction = (c.get('jurisdiction') or '').lower()

        # Apply filters
        if state_filter and state != state_filter.upper():
            continue
        if level_filter and level != level_filter.lower():
            continue
        if office_filter and office_filter.lower() not in office:
            continue

        # --retry: only candidates that don't have a photo yet
        if retry_missing and c.get('photo'):
            continue

        # Default behavior (no filters + not --all): high-profile only
        if not (fetch_all or state_filter or level_filter or office_filter or retry_missing):
            if level in ('executive', 'judicial'):
                targets.append(c)
            elif 'governor' in office:
                targets.append(c)
            elif level == 'federal' and 'senate' in jurisdiction and 'state' not in jurisdiction:
                targets.append(c)
            continue

        targets.append(c)

    return targets


def parse_args():
    """Tiny argparse replacement — avoids argparse boilerplate."""
    argv = sys.argv[1:]
    opts = {
        'dry': False, 'force': False, 'fetch_all': False,
        'state': None, 'level': None, 'office': None,
        'limit': None, 'retry': False,
    }
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ('--dry', '--dry-run'):
            opts['dry'] = True
        elif a == '--force':
            opts['force'] = True
        elif a == '--all':
            opts['fetch_all'] = True
        elif a == '--retry':
            opts['retry'] = True
        elif a == '--state' and i + 1 < len(argv):
            opts['state'] = argv[i + 1]
            i += 1
        elif a == '--level' and i + 1 < len(argv):
            opts['level'] = argv[i + 1]
            i += 1
        elif a == '--office' and i + 1 < len(argv):
            opts['office'] = argv[i + 1]
            i += 1
        elif a == '--limit' and i + 1 < len(argv):
            opts['limit'] = int(argv[i + 1])
            i += 1
        i += 1
    return opts


def main():
    opts = parse_args()
    dry, force = opts['dry'], opts['force']

    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    targets = select_targets(
        data['candidates'],
        fetch_all=opts['fetch_all'],
        state_filter=opts['state'],
        level_filter=opts['level'],
        office_filter=opts['office'],
        retry_missing=opts['retry'],
    )
    if opts['limit']:
        targets = targets[:opts['limit']]
    filters_desc = []
    if opts['state']: filters_desc.append(f"state={opts['state']}")
    if opts['level']: filters_desc.append(f"level={opts['level']}")
    if opts['office']: filters_desc.append(f"office~{opts['office']}")
    if opts['retry']: filters_desc.append("only missing")
    if opts['fetch_all']: filters_desc.append("all")
    if opts['limit']: filters_desc.append(f"limit={opts['limit']}")
    filters_str = f" ({', '.join(filters_desc)})" if filters_desc else " (top officials default)"
    print(f"Photo targets: {len(targets)} candidates{filters_str}")

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

        # Rate limit: ~1.5 req/s to stay well under Wikipedia's limit and
        # avoid the Commons CDN returning HTML error pages under load.
        if fetched > 0:
            time.sleep(0.7)

        url = wiki_portrait_url(
            c['name'], slug,
            state=(c.get('state') or '').upper(),
            office=c.get('office') or '',
        )
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
