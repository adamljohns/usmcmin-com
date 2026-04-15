#!/usr/bin/env python3
"""
build-data.py — regenerate data/states/*.json and data/index.json from
data/scorecard.json. Also prunes stale entries from scorecard.meta.states
(e.g. the "_metadata" orphan) and refreshes meta.total_candidates and
meta.last_updated to reflect reality.

Run this AFTER any script that touches scorecard.json (add-state-batch.py,
populate-scores.py, enrich-profiles.py, or manual edits). It is the single
source of truth for converting the master scorecard into the per-state files
that citizen.html and the profile pages read at runtime.

Usage:
    python3 build-data.py          # normal run
    python3 build-data.py --dry    # report what would change, write nothing
    python3 build-data.py --quiet  # only print warnings and errors

Safety:
  * Sanity checks run BEFORE writing. If any fail, nothing is written.
  * Per-state files are written atomically via a temp file + rename.
  * index.json is written atomically.
  * scorecard.json is rewritten only when meta needs updating.
"""
import json
import os
import sys
import datetime
from collections import Counter, defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
SCORECARD_PATH = os.path.join(DATA_DIR, 'scorecard.json')
INDEX_PATH = os.path.join(DATA_DIR, 'index.json')
STATES_DIR = os.path.join(DATA_DIR, 'states')

# Keys in scorecard.meta that should be copied into index.meta verbatim.
# total_candidates, last_updated, and states are recomputed by the splitter.
META_COPY_KEYS = [
    'title', 'version', 'description', 'methodology',
    'scoring_rules', 'survey', 'author',
]


def log(msg, quiet=False):
    if not quiet:
        print(msg)


def warn(msg):
    print(f"!! {msg}", file=sys.stderr)


def atomic_write(path, data, compact=False):
    """Write JSON to path via temp + rename so a crash mid-write can't
    leave the site serving half a file.

    compact=True produces a single-line minified JSON file — used for the
    per-state data/states/*.json files to minimize browser download size.
    compact=False (default) produces indent=2 with a trailing newline —
    used for scorecard.json and index.json since humans occasionally inspect
    those and the extra bytes don't matter (scorecard is local-only, index is
    tiny).
    """
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        if compact:
            json.dump(data, f, separators=(', ', ': '))
        else:
            json.dump(data, f, indent=2)
            f.write('\n')
    os.replace(tmp, path)


def group_candidates_by_state(candidates):
    """Return {state_code: [candidate, ...]} with state codes upper-cased.
    Skips candidates with missing/empty state — those are ignored and
    reported as a warning."""
    by_state = defaultdict(list)
    missing = 0
    for c in candidates:
        st = (c.get('state') or '').strip().upper()
        if not st:
            missing += 1
            continue
        by_state[st].append(c)
    if missing:
        warn(f"{missing} candidates skipped (no state field)")
    return dict(by_state)


def check_duplicates(by_state):
    """Return [(state, slug, count), ...] for duplicate slugs within a state."""
    dupes = []
    for st, members in by_state.items():
        slug_counts = Counter(c.get('slug', '') for c in members if c.get('slug'))
        for slug, n in slug_counts.items():
            if n > 1:
                dupes.append((st, slug, n))
    return dupes


def sanity_check_pre_write(scorecard, by_state):
    """Return a list of error strings. Empty list = safe to write."""
    errors = []

    # 1. total_candidates in scorecard meta matches candidates array length
    actual = len(scorecard['candidates'])
    meta_total = scorecard['meta'].get('total_candidates')
    if meta_total is not None and meta_total != actual:
        # This is something we WILL fix, not an error — just note it.
        pass

    # 2. Duplicate slugs within a state — warning only. These represent real
    # people who share a name, or genuine data dupes. Either way the splitter
    # shouldn't block on them; they're reported so a later cleanup pass can
    # address them. Note: profile HTML files for dupes will collide at
    # candidates/{st}/{slug}.html and one will win.
    dupes = check_duplicates(by_state)
    if dupes:
        warn(f"{len(dupes)} duplicate slug(s) detected (profile files will collide):")
        for st, slug, n in dupes[:10]:
            warn(f"  {st}: '{slug}' appears {n} times")
        if len(dupes) > 10:
            warn(f"  ...and {len(dupes)-10} more")

    # 3. Sum of per-state counts equals total — blocking
    state_sum = sum(len(v) for v in by_state.values())
    if state_sum != actual:
        # Difference is candidates with missing state — warned already but
        # we should note the gap explicitly.
        diff = actual - state_sum
        if diff > 0:
            # Missing state candidates are warned, not fatal.
            pass
        else:
            errors.append(
                f"per-state sum ({state_sum}) > total candidates ({actual}) — "
                "this should never happen, refusing to write"
            )

    # 4. Categories present in scorecard — profile generator and index need them
    if not scorecard.get('categories'):
        errors.append("scorecard.json is missing 'categories' — refusing to write")

    return errors


def build_state_file(state_code, candidates):
    """Return the dict to write for data/states/{st}.json."""
    return {
        'meta': {
            'state': state_code,
            'count': len(candidates),
        },
        'candidates': candidates,
    }


def build_index(scorecard, by_state, state_file_sizes):
    """Construct the new index.json structure. State list excludes orphans
    like '_metadata' by sourcing only from actual candidates."""
    today = datetime.date.today().isoformat()
    state_codes = sorted(by_state.keys())

    meta = {}
    for k in META_COPY_KEYS:
        if k in scorecard['meta']:
            meta[k] = scorecard['meta'][k]
    meta['total_candidates'] = sum(len(v) for v in by_state.values())
    meta['last_updated'] = today
    meta['states'] = state_codes

    states_block = {}
    for code in state_codes:
        members = by_state[code]
        fname = f"states/{code.lower()}.json"
        size_bytes = state_file_sizes.get(code, 0)
        states_block[code] = {
            'count': len(members),
            'file': fname,
            'size_kb': max(1, round(size_bytes / 1024)),
        }

    return {
        'meta': meta,
        'categories': scorecard.get('categories', []),
        'states': states_block,
    }


def prune_scorecard_meta(scorecard, by_state):
    """Prune stale entries from scorecard.meta.states (e.g. '_metadata' orphan)
    and refresh total_candidates + last_updated. Returns True if anything
    was changed."""
    changed = False
    today = datetime.date.today().isoformat()

    actual_states = sorted(by_state.keys())
    existing_states = scorecard['meta'].get('states', [])
    if existing_states != actual_states:
        scorecard['meta']['states'] = actual_states
        changed = True

    actual_total = sum(len(v) for v in by_state.values())
    if scorecard['meta'].get('total_candidates') != actual_total:
        scorecard['meta']['total_candidates'] = actual_total
        changed = True

    if scorecard['meta'].get('last_updated') != today:
        scorecard['meta']['last_updated'] = today
        changed = True

    return changed


def main():
    args = sys.argv[1:]
    dry = '--dry' in args or '--dry-run' in args
    quiet = '--quiet' in args

    if not os.path.exists(SCORECARD_PATH):
        warn(f"scorecard.json not found at {SCORECARD_PATH}")
        return 2

    log(f"Reading {SCORECARD_PATH}", quiet)
    with open(SCORECARD_PATH, 'r') as f:
        scorecard = json.load(f)

    candidates = scorecard.get('candidates', [])
    log(f"  {len(candidates)} candidates in master", quiet)

    by_state = group_candidates_by_state(candidates)
    log(f"  {len(by_state)} distinct states", quiet)

    errors = sanity_check_pre_write(scorecard, by_state)
    if errors:
        warn("Sanity checks failed — NOT writing:")
        for e in errors:
            warn(f"  - {e}")
        return 1

    # Ensure states dir exists
    os.makedirs(STATES_DIR, exist_ok=True)

    # ---- Write per-state files ----
    state_file_sizes = {}
    written = 0
    for state_code in sorted(by_state.keys()):
        members = by_state[state_code]
        state_data = build_state_file(state_code, members)
        fpath = os.path.join(STATES_DIR, f"{state_code.lower()}.json")
        if dry:
            # measure what the file would be
            raw = json.dumps(state_data, indent=2) + '\n'
            state_file_sizes[state_code] = len(raw)
            continue
        atomic_write(fpath, state_data, compact=True)
        state_file_sizes[state_code] = os.path.getsize(fpath)
        written += 1

    # ---- Build + write index.json ----
    index = build_index(scorecard, by_state, state_file_sizes)
    if not dry:
        atomic_write(INDEX_PATH, index)

    # ---- Prune + optionally rewrite scorecard meta ----
    scorecard_changed = prune_scorecard_meta(scorecard, by_state)
    if scorecard_changed and not dry:
        atomic_write(SCORECARD_PATH, scorecard)

    # ---- Remove stale per-state files for states that no longer exist ----
    removed = []
    actual_lowers = {s.lower() for s in by_state.keys()}
    for fn in os.listdir(STATES_DIR):
        if not fn.endswith('.json'):
            continue
        code = fn[:-5]
        if code not in actual_lowers:
            removed.append(fn)
            if not dry:
                os.remove(os.path.join(STATES_DIR, fn))

    # ---- Summary ----
    if dry:
        log("DRY RUN — no files written", quiet)
    log(
        f"Wrote {written} per-state file(s), "
        f"index.json, "
        f"{'scorecard.json (meta refreshed)' if scorecard_changed else 'scorecard.json unchanged'}",
        quiet,
    )
    if removed:
        log(f"Removed stale per-state files: {', '.join(removed)}", quiet)
    log(
        f"Total: {sum(len(v) for v in by_state.values())} candidates "
        f"across {len(by_state)} states",
        quiet,
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
