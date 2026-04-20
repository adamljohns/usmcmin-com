#!/usr/bin/env python3
"""
audit-photos.py — verify every photo referenced in scorecard.json exists
on disk AND is a real image (not an HTML error page that slipped through).

Deletes bad files, clears the photo path in scorecard, and re-runs build-data.py.

Usage:
    python3 audit-photos.py              # scan + fix
    python3 audit-photos.py --dry        # scan, report, change nothing
"""
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
SCORECARD = BASE / 'data' / 'scorecard.json'


def is_valid_image(path):
    if not path.exists():
        return False
    if path.stat().st_size < 1000:
        return False
    with open(path, 'rb') as f:
        magic = f.read(4)
    return magic[:2] == b'\xff\xd8' or magic[:4] == b'\x89PNG'


def main():
    dry = '--dry' in sys.argv

    with open(SCORECARD) as f:
        data = json.load(f)

    candidates_with_photo = [c for c in data['candidates'] if c.get('photo')]
    print(f"Candidates with photo field set: {len(candidates_with_photo)}")

    orphaned_on_disk = []  # files exist but not referenced
    bad_files = []         # photo field set but file bad/missing
    good = 0

    # Check everything referenced in scorecard
    referenced = set()
    for c in candidates_with_photo:
        photo_path = BASE / c['photo']
        referenced.add(photo_path)
        if is_valid_image(photo_path):
            good += 1
        else:
            bad_files.append((c, photo_path))

    # Check for files on disk not referenced in scorecard
    for p in (BASE / 'assets' / 'photos').rglob('*.jpg'):
        if p not in referenced:
            orphaned_on_disk.append(p)

    print(f"  Valid images: {good}")
    print(f"  Bad/missing: {len(bad_files)}")
    print(f"  Orphaned on disk (not referenced): {len(orphaned_on_disk)}")

    if dry:
        for c, p in bad_files[:20]:
            print(f"  BAD: {c['name']} -> {p}")
        for p in orphaned_on_disk[:20]:
            print(f"  ORPHAN: {p}")
        print("\nDRY RUN — nothing changed")
        return

    # Fix: delete bad files and clear scorecard refs
    fixed = 0
    for c, p in bad_files:
        if p.exists():
            p.unlink()
        c['photo'] = None
        fixed += 1

    # Delete orphans (rare, but happens if a candidate was removed)
    for p in orphaned_on_disk:
        p.unlink()

    if fixed or orphaned_on_disk:
        with open(SCORECARD, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\nFixed {fixed} bad refs, deleted {len(orphaned_on_disk)} orphans")
        # Rebuild per-state
        subprocess.run(
            [sys.executable, str(BASE / 'build-data.py'), '--quiet'],
            check=True,
        )
        print("Rebuilt per-state files")
    else:
        print("\nAll clean.")


if __name__ == '__main__':
    main()
