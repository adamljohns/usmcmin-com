#!/usr/bin/env python3
"""
build-webp.py — convert candidate JPEG portraits to WebP for ~30% smaller
downloads on supporting browsers (>96% of users in 2026).

WebP files are written ALONGSIDE the .jpg files (same path, .webp ext)
so:
  1. The .jpg path keeps working — old links don't break.
  2. The profile template can emit a <picture> element with both, and
     the browser auto-picks WebP when it can.

Output: assets/photos/{state}/{slug}.webp for every assets/photos/{state}/
{slug}.jpg that:
  - Doesn't already have a .webp sibling, OR
  - Has a .webp sibling that's older than the .jpg (meaning the JPEG
    was re-fetched/re-optimized)

Usage:
    python3 build-webp.py              # convert all (skip up-to-date)
    python3 build-webp.py --force      # re-convert everything
    python3 build-webp.py --dry        # report only

Tooling: ImageMagick (`magick`) for the conversion. macOS sips lacks
WebP write support in current versions. quality 75 matches the JPEG
optimization defaults — the human eye doesn't distinguish at the 96px
avatar render size.
"""
import os
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
PHOTOS = BASE / 'assets' / 'photos'
QUALITY = 75


def main():
    args = sys.argv[1:]
    dry = '--dry' in args
    force = '--force' in args

    jpegs = sorted(PHOTOS.rglob('*.jpg'))
    print(f'JPEG portraits found: {len(jpegs)}')

    candidates = []
    for jpg in jpegs:
        webp = jpg.with_suffix('.webp')
        if force or not webp.exists() or webp.stat().st_mtime < jpg.stat().st_mtime:
            candidates.append((jpg, webp))

    print(f'Need conversion: {len(candidates)}')
    if dry:
        sample_in = sum(j.stat().st_size for j, _ in candidates[:50])
        print(f'  (Sample: first 50 JPEGs total {sample_in/1024/1024:.1f} MB)')
        print('DRY RUN — nothing written')
        return

    converted = 0
    failed = 0
    saved_bytes = 0
    for i, (jpg, webp) in enumerate(candidates):
        before = jpg.stat().st_size
        try:
            r = subprocess.run(
                ['magick', str(jpg),
                 '-quality', str(QUALITY),
                 str(webp)],
                capture_output=True, timeout=20,
            )
        except subprocess.TimeoutExpired:
            failed += 1
            if webp.exists():
                webp.unlink()
            continue
        if r.returncode != 0 or not webp.exists() or webp.stat().st_size < 500:
            failed += 1
            if webp.exists():
                webp.unlink()
            continue
        # Validate WebP magic bytes (RIFF....WEBP)
        with open(webp, 'rb') as f:
            head = f.read(12)
        if head[:4] != b'RIFF' or head[8:12] != b'WEBP':
            failed += 1
            webp.unlink()
            continue
        after = webp.stat().st_size
        saved_bytes += (before - after)
        converted += 1
        if converted % 200 == 0 or converted <= 3:
            rel = jpg.relative_to(BASE)
            print(f'  [{i+1}/{len(candidates)}] {rel}: '
                  f'{before/1024:.0f}KB → {after/1024:.0f}KB')

    print(f'\nConverted: {converted}')
    print(f'Failed: {failed}')
    print(f'Saved (vs JPEG totals): {saved_bytes/1024/1024:.1f} MB')

    # Final inventory
    total_jpg = sum(p.stat().st_size for p in jpegs)
    total_webp = sum(p.stat().st_size for p in PHOTOS.rglob('*.webp'))
    print(f'JPEG total:  {total_jpg/1024/1024:.1f} MB')
    print(f'WebP total:  {total_webp/1024/1024:.1f} MB '
          f'({(1 - total_webp/total_jpg) * 100:.1f}% smaller)')


if __name__ == '__main__':
    main()
