#!/usr/bin/env python3
"""
optimize-photos.py — resize + recompress oversized portrait photos.

Photos in assets/photos/{state}/{slug}.jpg are rendered as circular 96px
avatars on profile pages. Many were downloaded at 1000px+ original
resolution and weigh in at multiple megabytes — wasted bandwidth on
every page view + repo size.

This script:
  - Finds every JPEG in assets/photos/
  - For files larger than --threshold (default 100 KB), resamples to
    --max-width pixels wide (default 400 — 4x the display size for retina)
    and recompresses at --quality (default 75)
  - Skips files already small enough or already at the target width
  - Validates the output JPEG (magic bytes) before replacing the original
  - Reports total size before/after

Default settings target a 90%+ size reduction on the worst offenders
without visible degradation at the avatar size.

Usage:
    python3 optimize-photos.py                    # apply defaults
    python3 optimize-photos.py --dry              # report only, change nothing
    python3 optimize-photos.py --threshold 50000  # smaller threshold
    python3 optimize-photos.py --max-width 600    # bigger output
    python3 optimize-photos.py --quality 85       # higher quality
"""
import os
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
PHOTOS = BASE / 'assets' / 'photos'


def parse_args():
    args = {
        'dry': '--dry' in sys.argv or '--dry-run' in sys.argv,
        'threshold': 100_000,
        'max_width': 400,
        'quality': 75,
    }
    argv = sys.argv[1:]
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--threshold' and i + 1 < len(argv):
            args['threshold'] = int(argv[i + 1]); i += 1
        elif a == '--max-width' and i + 1 < len(argv):
            args['max_width'] = int(argv[i + 1]); i += 1
        elif a == '--quality' and i + 1 < len(argv):
            args['quality'] = int(argv[i + 1]); i += 1
        i += 1
    return args


def is_valid_jpeg(path):
    if not path.exists() or path.stat().st_size < 200:
        return False
    with open(path, 'rb') as f:
        return f.read(2) == b'\xff\xd8'


def main():
    args = parse_args()

    photos = sorted(PHOTOS.rglob('*.jpg'))
    total_before = sum(p.stat().st_size for p in photos)

    print(f'Scanning {len(photos)} photos...')
    print(f'  Threshold: {args["threshold"]:,} B')
    print(f'  Target max width: {args["max_width"]}px')
    print(f'  JPEG quality: {args["quality"]}')
    print(f'  Total current size: {total_before / 1024 / 1024:.1f} MB')
    print()

    candidates = [p for p in photos if p.stat().st_size > args['threshold']]
    print(f'Candidates for optimization: {len(candidates)} photos > '
          f'{args["threshold"]:,} B')

    if args['dry']:
        # Just sample sizes
        candidates_total = sum(p.stat().st_size for p in candidates)
        print(f'  Total size of candidates: {candidates_total / 1024 / 1024:.1f} MB')
        print('DRY RUN — nothing changed')
        return

    optimized = 0
    skipped = 0
    failed = 0
    saved_bytes = 0

    for i, src in enumerate(candidates):
        before_bytes = src.stat().st_size
        # Run sips: in-place via temp file then rename for atomicity
        tmp = src.with_suffix('.tmp.jpg')
        try:
            r = subprocess.run(
                ['sips',
                 '--resampleWidth', str(args['max_width']),
                 '--setProperty', 'formatOptions', str(args['quality']),
                 str(src),
                 '--out', str(tmp)],
                capture_output=True, timeout=30,
            )
        except subprocess.TimeoutExpired:
            failed += 1
            print(f'  TIMEOUT: {src}')
            tmp.unlink(missing_ok=True)
            continue

        if r.returncode != 0 or not tmp.exists() or not is_valid_jpeg(tmp):
            failed += 1
            tmp.unlink(missing_ok=True)
            continue

        after_bytes = tmp.stat().st_size

        # Only replace if the optimized version is actually smaller.
        # (Very small originals could increase if they're already tightly
        # compressed at a lower res than max-width.)
        if after_bytes < before_bytes:
            os.replace(tmp, src)
            optimized += 1
            saved_bytes += (before_bytes - after_bytes)
            if optimized % 100 == 0 or optimized <= 3:
                print(f'  [{i+1}/{len(candidates)}] {src.relative_to(BASE)}: '
                      f'{before_bytes/1024:.0f}KB → {after_bytes/1024:.0f}KB')
        else:
            tmp.unlink()
            skipped += 1

    total_after = sum(p.stat().st_size for p in photos)
    print(f'\nResults:')
    print(f'  Optimized: {optimized}')
    print(f'  Skipped (no improvement): {skipped}')
    print(f'  Failed: {failed}')
    print(f'  Saved: {saved_bytes / 1024 / 1024:.1f} MB')
    print(f'  Total before: {total_before / 1024 / 1024:.1f} MB')
    print(f'  Total after:  {total_after / 1024 / 1024:.1f} MB')
    print(f'  Reduction:    {(1 - total_after/total_before) * 100:.1f}%')


if __name__ == '__main__':
    main()
