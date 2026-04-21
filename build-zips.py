#!/usr/bin/env python3
"""
build-zips.py — produce data/zips.json for Find My Reps ZIP input.

Source: https://raw.githubusercontent.com/OpenSourceActivismTech/us-zipcodes-congress/master/zccd.csv
  (ZCTA -> Congressional District, 2020 relationship file. Public domain.)

We filter to the states where we have scorecard + places coverage
(FL, VA, TX, CA, NY, PA, IL, OH) to keep the shipped file small and fast,
and fold split ZIPs into arrays. A ZIP that crosses multiple CDs gets
"cds": [7, 8] and the UI tells the user their district is one of those.

Output format (compact JSON, one dict keyed by ZIP):
  { "32901": { "state": "FL", "cds": [8] }, ... }
"""
import csv
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / 'data' / 'zips.json'
CACHE = Path('/tmp/zccd.csv')
SOURCE_URL = 'https://raw.githubusercontent.com/OpenSourceActivismTech/us-zipcodes-congress/master/zccd.csv'

# All 50 states + DC. A visitor anywhere in the US can type their ZIP and
# we'll at least resolve their US House district — even if we haven't
# deeply enriched local/state officials for that state yet.
COVERED_STATES = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA',
    'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
    'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
    'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
}


def fetch():
    if CACHE.exists() and CACHE.stat().st_size > 100_000:
        return
    print(f'Fetching {SOURCE_URL}...')
    r = subprocess.run(
        ['curl', '-s', '-L', '-o', str(CACHE),
         '-A', 'USMCMin-ZIPBuild/1.0 (usmcmin.com)', SOURCE_URL],
        capture_output=True, timeout=60,
    )
    if r.returncode != 0 or not CACHE.exists() or CACHE.stat().st_size < 100_000:
        print('ERROR: failed to fetch', file=sys.stderr)
        sys.exit(1)


def main():
    fetch()
    by_zip = {}
    total_rows = 0
    covered_rows = 0
    with open(CACHE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_rows += 1
            st = row.get('state_abbr', '').strip()
            if st not in COVERED_STATES:
                continue
            zcta = (row.get('zcta') or '').strip().zfill(5)
            cd = (row.get('cd') or '').strip()
            if not zcta or not cd:
                continue
            try:
                cd_int = int(cd)
            except ValueError:
                continue
            # At-large states (AK, DE, ND, SD, VT, WY, DC) use cd=0 in the
            # source CSV — unitedstates/congress-legislators and our scorecard
            # use district=1 for at-large. Normalize to 1 so Find My Reps'
            # district match works without special-casing in JS.
            if cd_int == 0:
                cd_int = 1
            if zcta not in by_zip:
                by_zip[zcta] = {'state': st, 'cds': []}
            if cd_int not in by_zip[zcta]['cds']:
                by_zip[zcta]['cds'].append(cd_int)
            covered_rows += 1

    # Sort CD lists for determinism
    for v in by_zip.values():
        v['cds'].sort()

    # Output compact (no spaces) to minimize shipped size
    with open(OUT, 'w') as f:
        json.dump(by_zip, f, separators=(',', ':'))

    size = OUT.stat().st_size
    # Stats
    split_zips = sum(1 for v in by_zip.values() if len(v['cds']) > 1)
    print(f'Read {total_rows} source rows; {covered_rows} in covered states')
    print(f'Unique ZIPs: {len(by_zip)}')
    print(f'Split ZIPs (multi-CD): {split_zips}')
    print(f'Per state:')
    from collections import Counter
    counts = Counter(v['state'] for v in by_zip.values())
    for s in sorted(counts.keys()):
        print(f'  {s}: {counts[s]} ZIPs')
    print(f'Output: {OUT} ({size:,} bytes, ~{size/1024:.0f} KB)')


if __name__ == '__main__':
    main()
