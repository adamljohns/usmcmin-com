#!/usr/bin/env python3
"""
enrich-from-openstates.py — pull contact info, photos, and supplementary
sources from the openstates/people repository into the 613 state-assembly
records seeded yesterday.

INPUTS:
  * /tmp/os_people/people-main/data/{nv,nj,wi,nh}/legislature/*.yml
    (downloaded from https://github.com/openstates/people, extracted
    from the main-branch zip on 2026-04-23)
  * data/scorecard.json — only records with
    profile.confidence == "party_default" are touched.

FIELDS FILLED (when present in the OpenStates YAML, and only if the
corresponding scorecard field is currently empty):
  * profile.email
  * profile.phone          <- first capitol office voice number
  * profile.office         <- first capitol office address
  * profile.district_office <- first district office address
  * profile.twitter        <- from links[] where URL host is x.com/twitter.com
  * profile.website        <- from links[] flagged `note: homepage`
  * profile.openstates_id  <- ocd-person/<uuid>
  * photo                  <- local asset path once the image is downloaded
  * sources[]              <- merged from OpenStates sources[], deduped;
                              openstates.org profile URL always added.

Photo download: saved to assets/photos/{state}/{slug}.jpg. Skipped if
the file already exists (idempotent). Downloads rate-limited to 4/sec
so we don't hammer the state legislature servers hosting the images.

Match key: (state, chamber=lower, district). Only records that match
on all three are enriched; anything else is left alone.

Run:
    python3 enrich-from-openstates.py                     # all 4 states
    python3 enrich-from-openstates.py --state NV          # one state
    python3 enrich-from-openstates.py --dry-run           # report only
    python3 enrich-from-openstates.py --skip-photos       # data only
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import glob
import urllib.parse
from pathlib import Path

import yaml

REPO = Path(__file__).parent
SCORECARD = REPO / 'data' / 'scorecard.json'
ASSETS_PHOTOS = REPO / 'assets' / 'photos'
OS_ROOT = Path('/tmp/os_people/people-main/data')

STATES = ['nv', 'nj', 'wi', 'nh']


def normalize_district(d):
    """Canonical form for match-key purposes.
      * '9' / 9 / 'District 9'     -> int 9           (NV/NJ/WI)
      * 'Belknap 01' / 'Belknap 1' -> 'Belknap 1'     (NH, zero-padding stripped)
      * 'Coös 2' / 'Coos 2'        -> 'Coos 2'        (diacritics stripped)
    """
    if d is None:
        return None
    s = str(d).strip()
    # Numeric-only
    if s.isdigit():
        return int(s)
    # 'District 9' style
    m = re.fullmatch(r'[Dd]istrict\s+(\d+)', s)
    if m:
        return int(m.group(1))
    # County-prefixed: strip accents + zero-padding on trailing number
    import unicodedata
    s_ascii = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii').strip()
    # Collapse "Word 01" -> "Word 1"
    mm = re.match(r'^([A-Za-z][A-Za-z\s]*?)\s+0*(\d+)$', s_ascii)
    if mm:
        return f'{mm.group(1).strip()} {int(mm.group(2))}'
    return s_ascii


def open_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def find_capitol_phone_and_offices(doc):
    phone, capitol_addr, district_addr = None, None, None
    for off in doc.get('offices') or []:
        cls = (off.get('classification') or '').lower()
        if cls == 'capitol' and phone is None:
            phone = off.get('voice')
            capitol_addr = off.get('address')
        elif cls == 'district' and district_addr is None:
            district_addr = off.get('address')
    return phone, capitol_addr, district_addr


def find_twitter_and_homepage(doc):
    twitter, homepage = None, None
    for link in doc.get('links') or []:
        url = (link.get('url') or '').strip()
        note = (link.get('note') or '').lower()
        if not url:
            continue
        host = urllib.parse.urlparse(url).hostname or ''
        host = host.lower().removeprefix('www.')
        if host in ('twitter.com', 'x.com'):
            if twitter is None:
                # Take the handle from the path
                parts = urllib.parse.urlparse(url).path.strip('/').split('/')
                if parts and parts[0]:
                    twitter = parts[0]
        if note == 'homepage' and homepage is None:
            homepage = url
    # Some YAMLs omit a homepage note; if we still lack one, use the
    # first non-social link.
    if not homepage:
        for link in doc.get('links') or []:
            url = (link.get('url') or '').strip()
            host = urllib.parse.urlparse(url).hostname or ''
            host = host.lower().removeprefix('www.')
            if host and host not in ('twitter.com', 'x.com', 'facebook.com', 'instagram.com'):
                homepage = url
                break
    return twitter, homepage


def download_photo(url: str, dst: Path, ua: str):
    if dst.exists() and dst.stat().st_size > 100:
        return 'exists'
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_suffix(dst.suffix + '.tmp')
    r = subprocess.run(
        ['curl', '-sL', '--max-time', '20', '-A', ua, '-o', str(tmp), url,
         '-w', '%{http_code} %{size_download}'],
        capture_output=True, text=True,
    )
    out = (r.stdout or '').strip()
    if r.returncode != 0:
        tmp.unlink(missing_ok=True)
        return f'fail(curl:{r.returncode})'
    try:
        code, size = out.split()
        size = int(size)
    except Exception:
        tmp.unlink(missing_ok=True)
        return f'fail(parse:{out!r})'
    if code != '200' or size < 500:
        tmp.unlink(missing_ok=True)
        return f'fail(http:{code},size:{size})'
    # Quick sanity: JPEG / PNG magic
    with open(tmp, 'rb') as f:
        head = f.read(8)
    if not (head[:3] == b'\xff\xd8\xff' or head[:8] == b'\x89PNG\r\n\x1a\n' or head[:6] in (b'GIF87a', b'GIF89a')):
        tmp.unlink(missing_ok=True)
        return f'fail(not-image)'
    tmp.rename(dst)
    return 'ok'


def iter_lower_members(state_code: str):
    """Yield (path, doc, normalized_district) for each YAML file whose
    subject is a CURRENT member of the lower chamber. A role is current
    when it has no end_date, or an end_date >= today."""
    from datetime import date as _date
    today = _date.today().isoformat()
    state_lower = state_code.lower()
    root = OS_ROOT / state_lower / 'legislature'
    if not root.exists():
        return
    for path in sorted(root.glob('*.yml')):
        doc = open_yaml(path)
        if not doc:
            continue
        lower = False
        district = None
        for role in doc.get('roles') or []:
            if (role.get('type') or '').lower() != 'lower':
                continue
            end = role.get('end_date')
            if end and str(end) < today:
                continue      # past role, skip
            lower = True
            district = role.get('district')
            break
        if not lower or district is None:
            continue
        yield path, doc, normalize_district(district)


def merge_sources(existing, to_add):
    seen = set(existing)
    out = list(existing)
    for u in to_add:
        if not u:
            continue
        if u in seen:
            continue
        out.append(u)
        seen.add(u)
    return out


def enrich(state_code: str, candidates: list, args) -> dict:
    """Mutates `candidates` in place. Returns a stats dict."""
    state_code_up = state_code.upper()
    state_code_lo = state_code.lower()

    # Build an index of party_default seeded candidates by (state, district)
    idx = {}
    for c in candidates:
        if c.get('state') != state_code_up:
            continue
        if (c.get('profile') or {}).get('confidence') != 'party_default':
            continue
        district = normalize_district(c.get('district'))
        # Only lower-chamber seeded records (office contains Assembly or
        # Representative per seed-state-assemblies.py STATE_CONFIG.office_label)
        off_label = (c.get('office') or '').lower()
        if not any(k in off_label for k in ('assembly', 'representative')):
            continue
        idx.setdefault((state_code_up, district), []).append(c)

    stats = {
        'state': state_code_up,
        'seeded_lower_chamber': sum(len(v) for v in idx.values()),
        'openstates_yaml_count': 0,
        'matched': 0,
        'enriched': 0,
        'photos_downloaded': 0,
        'photos_skipped': 0,
        'photos_failed': 0,
        'unmatched_districts': [],
    }

    ua = 'USMCMin-Enrich/1.0 (usmcmin.com)'

    for path, doc, district in iter_lower_members(state_code_lo):
        stats['openstates_yaml_count'] += 1
        key = (state_code_up, district)
        matches = idx.get(key) or []
        if not matches:
            stats['unmatched_districts'].append(f'{district} ({doc.get("name","?")})')
            continue
        # For multi-rep districts (NH), match by name
        target = None
        if len(matches) == 1:
            target = matches[0]
        else:
            cand_name = (doc.get('name') or '').lower().strip()
            for m in matches:
                if m.get('name','').lower().strip() == cand_name:
                    target = m
                    break
            if target is None:
                # last-resort match by family_name
                family = (doc.get('family_name') or '').lower()
                for m in matches:
                    mn = m.get('name','').lower()
                    if family and mn.endswith(' ' + family):
                        target = m
                        break
        if target is None:
            continue
        stats['matched'] += 1

        prof = target.setdefault('profile', {})
        # Fields to fill if empty
        phone, capitol_addr, district_addr = find_capitol_phone_and_offices(doc)
        twitter, homepage = find_twitter_and_homepage(doc)

        changed = False
        if phone and not prof.get('phone'):
            prof['phone'] = phone
            changed = True
        if capitol_addr and not prof.get('office'):
            prof['office'] = capitol_addr
            changed = True
        if district_addr and not prof.get('district_office'):
            prof['district_office'] = district_addr
            changed = True
        if twitter and not prof.get('twitter'):
            prof['twitter'] = '@' + twitter.lstrip('@')
            changed = True
        if homepage and not target.get('website'):
            target['website'] = homepage
            changed = True
        email = doc.get('email')
        if email and not prof.get('email'):
            prof['email'] = email
            changed = True
        if doc.get('id') and not prof.get('openstates_id'):
            prof['openstates_id'] = doc.get('id')
            changed = True

        # Merge sources
        os_sources = [l.get('url') for l in (doc.get('sources') or []) if l.get('url')]
        os_profile_url = f'https://openstates.org/person/{str(doc.get("id","")).replace("ocd-person/","")}/'
        target['sources'] = merge_sources(target.get('sources') or [], os_sources + [os_profile_url])
        if len(os_sources):
            changed = True

        # Photo
        if not args.skip_photos:
            img_url = doc.get('image')
            if img_url:
                photo_dst = ASSETS_PHOTOS / state_code_lo / f'{target["slug"]}.jpg'
                if photo_dst.exists() and photo_dst.stat().st_size > 500:
                    stats['photos_skipped'] += 1
                    target['photo'] = str(photo_dst.relative_to(REPO))
                else:
                    if args.dry_run:
                        stats['photos_skipped'] += 1
                    else:
                        result = download_photo(img_url, photo_dst, ua)
                        if result == 'ok':
                            stats['photos_downloaded'] += 1
                            target['photo'] = str(photo_dst.relative_to(REPO))
                            changed = True
                            time.sleep(0.25)   # gentle rate-limit
                        elif result == 'exists':
                            stats['photos_skipped'] += 1
                            target['photo'] = str(photo_dst.relative_to(REPO))
                        else:
                            stats['photos_failed'] += 1

        if changed:
            stats['enriched'] += 1

    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--state', choices=['NV', 'NJ', 'WI', 'NH'])
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--skip-photos', action='store_true')
    args = ap.parse_args()

    if not OS_ROOT.exists():
        print('ERROR: OpenStates zip not extracted at /tmp/os_people/', file=sys.stderr)
        sys.exit(1)

    with open(SCORECARD, 'r', encoding='utf-8') as f:
        sc = json.load(f)

    targets = [args.state] if args.state else ['NV', 'NJ', 'WI', 'NH']
    all_stats = []
    for st in targets:
        s = enrich(st.lower(), sc['candidates'], args)
        all_stats.append(s)

    if not args.dry_run:
        with open(SCORECARD, 'w', encoding='utf-8') as f:
            json.dump(sc, f, indent=2, ensure_ascii=False)

    for s in all_stats:
        print(f"\n=== {s['state']} ===")
        print(f"  seeded lower-chamber records: {s['seeded_lower_chamber']}")
        print(f"  OpenStates lower YAMLs:       {s['openstates_yaml_count']}")
        print(f"  matched:                      {s['matched']}")
        print(f"  enriched (any field changed): {s['enriched']}")
        print(f"  photos ok/skipped/failed:     {s['photos_downloaded']}/{s['photos_skipped']}/{s['photos_failed']}")
        if s['unmatched_districts'][:5]:
            print(f"  sample unmatched districts (first 5): {s['unmatched_districts'][:5]}")

    if args.dry_run:
        print('\n(dry-run) no file written.')


if __name__ == '__main__':
    main()
