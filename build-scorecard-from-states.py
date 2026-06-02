#!/usr/bin/env python3
"""
build-scorecard-from-states.py — reverse builder.

The PRIMARY direction (build-data.py) reads data/scorecard.json (60 MB
monolith, source of truth today) and writes the per-state files
data/states/*.json + data/index.json + data/scorecard-compact.json.

This script goes the OPPOSITE direction: composes a candidate
scorecard.json from data/states/*.json + data/index.json. It is
Phase 1 of an eventual source-of-truth flip:

  Today:  scorecard.json   →  states/*.json + index.json   (build-data.py)
  Goal:   states/*.json + index.json   →  scorecard.json   (this script)

Phase 1 (this PR): just prove the round-trip works. Run with --verify
to compose a scorecard from the per-state files and diff it against
the committed scorecard.json. If they match byte-for-byte (or only
differ in known-safe ways like key ordering or whitespace), the
per-state files contain everything needed.

Phase 2 (future PR): retarget all 40 add-*.py ingestion scripts to
write into states/*.json instead of scorecard.json, then make this
script the canonical builder.

Phase 3 (future PR): gitignore scorecard.json, regenerate it as a
deploy-time artifact (or move it to LFS). Clears the GitHub 50 MB
warning permanently.

Usage:
    python3 build-scorecard-from-states.py --verify   # compare to committed
    python3 build-scorecard-from-states.py --dry      # print what would write
    python3 build-scorecard-from-states.py --write    # actually write scorecard.json
                                                       # (USE WITH CARE — overwrites
                                                       # the source of truth)
"""
import json
import os
import sys
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / 'data'
STATES_DIR = DATA / 'states'
INDEX_PATH = DATA / 'index.json'
SCORECARD_PATH = DATA / 'scorecard.json'


def load_state_files():
    """Return {state_code: [candidate, ...]} from data/states/*.json."""
    out = {}
    for f in sorted(STATES_DIR.glob('*.json')):
        code = f.stem.upper()
        with open(f) as fp:
            d = json.load(fp)
        out[code] = d.get('candidates', [])
    return out


def compose_scorecard(by_state, index):
    """Build a scorecard.json dict from per-state candidates + index metadata."""
    # Flatten candidates back into a single list, preserving the order
    # build-data.py uses (sorted by state code, then by appearance).
    all_candidates = []
    for code in sorted(by_state.keys()):
        all_candidates.extend(by_state[code])

    return {
        'meta': dict(index.get('meta', {})),
        'categories': list(index.get('categories', [])),
        'candidates': all_candidates,
    }


def candidate_key(c):
    """Stable identity for a candidate — used to align lists for diffing.
    (state, slug) is unique within scorecard.json modulo the dupes that
    sanity_check warns about."""
    return ((c.get('state') or '').upper(), c.get('slug') or '')


def diff_scorecards(composed, original, max_items=10):
    """Compare composed (from states) vs original (committed scorecard.json).
    Returns a list of human-readable difference notes. Empty list = match."""
    diffs = []

    # Top-level structure
    if set(composed.keys()) != set(original.keys()):
        diffs.append(
            f"top-level keys differ: composed={sorted(composed.keys())}, "
            f"original={sorted(original.keys())}"
        )

    # Meta — compare keys that should match. Skip last_updated (changes daily).
    cm = composed.get('meta', {})
    om = original.get('meta', {})
    meta_skip = {'last_updated'}
    for k in set(cm.keys()) | set(om.keys()):
        if k in meta_skip:
            continue
        if cm.get(k) != om.get(k):
            diffs.append(f"meta.{k} differs: {cm.get(k)!r} vs {om.get(k)!r}")

    # Categories — exact match expected
    if composed.get('categories') != original.get('categories'):
        diffs.append("categories differ (counts: composed=%d, original=%d)" % (
            len(composed.get('categories', [])),
            len(original.get('categories', [])),
        ))

    # Candidates — compare counts first, then per-candidate equality
    cc = composed.get('candidates', [])
    oc = original.get('candidates', [])
    if len(cc) != len(oc):
        diffs.append(f"candidate counts differ: composed={len(cc)} vs original={len(oc)}")

    # Per-candidate diff keyed by (state, slug)
    composed_by_key = {candidate_key(c): c for c in cc}
    original_by_key = {candidate_key(c): c for c in oc}

    only_in_composed = set(composed_by_key) - set(original_by_key)
    only_in_original = set(original_by_key) - set(composed_by_key)
    if only_in_composed:
        sample = list(only_in_composed)[:max_items]
        diffs.append(f"only in composed ({len(only_in_composed)}): {sample}")
    if only_in_original:
        sample = list(only_in_original)[:max_items]
        diffs.append(f"only in original ({len(only_in_original)}): {sample}")

    # Field-level diffs on shared candidates
    field_mismatches = 0
    sample_field_diffs = []
    for key in sorted(set(composed_by_key) & set(original_by_key)):
        a = composed_by_key[key]
        b = original_by_key[key]
        if a != b:
            field_mismatches += 1
            if len(sample_field_diffs) < max_items:
                diff_fields = []
                for fk in set(a) | set(b):
                    if a.get(fk) != b.get(fk):
                        diff_fields.append(fk)
                sample_field_diffs.append(f"  {key}: differs in {diff_fields}")
    if field_mismatches:
        diffs.append(f"field-level mismatches on {field_mismatches} candidates:")
        diffs.extend(sample_field_diffs)
        if field_mismatches > max_items:
            diffs.append(f"  ... and {field_mismatches - max_items} more")

    return diffs


def main():
    args = sys.argv[1:]
    verify = '--verify' in args
    dry = '--dry' in args or '--dry-run' in args
    write = '--write' in args

    if not any([verify, dry, write]):
        print(__doc__)
        return 2

    # Load inputs
    by_state = load_state_files()
    with open(INDEX_PATH) as f:
        index = json.load(f)

    total = sum(len(v) for v in by_state.values())
    print(f"Loaded {total:,} candidates across {len(by_state)} states")
    print(f"index.json: {len(index.get('categories', []))} categories")

    composed = compose_scorecard(by_state, index)

    if verify:
        if not SCORECARD_PATH.exists():
            print("ERROR: scorecard.json not found — nothing to diff against")
            return 1
        with open(SCORECARD_PATH) as f:
            original = json.load(f)
        diffs = diff_scorecards(composed, original)
        if not diffs:
            print("\n✓ ROUND-TRIP VERIFIED")
            print("  scorecard.json composed from per-state files matches")
            print("  the committed scorecard.json (modulo last_updated).")
            print("  Per-state files contain everything needed — they")
            print("  are sufficient as the source of truth.")
            return 0
        print(f"\n✗ {len(diffs)} difference(s) found:")
        for d in diffs:
            print(f"  - {d}")
        return 1

    if dry:
        out = json.dumps(composed, indent=2)
        print(f"\nDry composed scorecard: {len(out):,} bytes "
              f"({len(out)/1024/1024:.1f} MB)")
        return 0

    if write:
        # Match build-data.py's atomic-write convention.
        tmp = SCORECARD_PATH.with_suffix('.json.tmp')
        with open(tmp, 'w') as f:
            json.dump(composed, f, indent=2)
            f.write('\n')
        os.replace(tmp, SCORECARD_PATH)
        size = SCORECARD_PATH.stat().st_size
        print(f"\nWrote {SCORECARD_PATH} ({size/1024/1024:.1f} MB)")
        return 0


if __name__ == '__main__':
    sys.exit(main())
