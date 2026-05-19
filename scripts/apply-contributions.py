#!/usr/bin/env python3
"""
apply-contributions.py — merge per-state contributor markdown files from
contributions/<state>/<slug>.md into data/scorecard.json.

Architecture per Adam's 2026-05-18 directive on contributor-friendly
monorepo (instead of 53 separate per-state repos):

  - Contributors edit a single Markdown file per official with YAML
    frontmatter containing proposed score changes + evidence URLs
  - This script reads all contributions/*/* .md files, validates,
    and applies accepted contributions to scorecard.json
  - The .md files stay in the repo as the audit trail
  - Maintainer runs this script (or eventually a persistent agent
    triggered by accepted PRs)

Usage:
    python3 scripts/apply-contributions.py --dry-run
    python3 scripts/apply-contributions.py --apply
    python3 scripts/apply-contributions.py --apply --only va/rob-wittman
    python3 scripts/apply-contributions.py --apply --since 2026-05-19

YAML schema for contributions/<state>/<slug>.md:
  slug:            required, must match existing scorecard slug
  state:           required, 2-letter lowercase
  contributor:     optional name + email
  office:          optional updated office string
  status:          optional 'active' | 'former' | 'lost' | 'lame_duck'
  scores:          dict {category_id: [5 values]} — values are
                   true | false | 'N/A' | null | 'keep'
                   ('keep' means don't change the existing value)
  church_affiliation: optional dict with name/denomination/evidence
  evidence:        list of source URLs backing the changes (required if
                   any scores or status changes are proposed)

Validation rules:
  - slug must exist in scorecard.json (this script does NOT create new
    candidates — use add-missing-federal-figures.py for that)
  - any score change requires at least one entry in `evidence`
  - score values must be one of: True, False, 'N/A', None, 'keep'
  - category IDs must match the 10 canonical v4.0 categories
"""
import json
import os
import re
import sys
from pathlib import Path

SCORECARD = 'data/scorecard.json'
CONTRIB_DIR = 'contributions'

VALID_CATEGORIES = {
    'sanctity_of_life', 'biblical_marriage', 'family_child_sovereignty',
    'christian_liberty', 'economic_stewardship', 'election_integrity',
    'border_immigration', 'self_defense', 'foreign_policy_restraint',
    'industry_capture',
}
VALID_STATUS = {'active', 'former', 'lost', 'lame_duck'}


def parse_frontmatter(text):
    """Extract YAML frontmatter from a contribution Markdown file.
    Returns (frontmatter_dict, narrative_body_str)."""
    if not text.startswith('---'):
        return {}, text
    end_marker = text.find('\n---\n', 4)
    if end_marker == -1:
        return {}, text
    fm_raw = text[4:end_marker]
    body = text[end_marker + 5:]
    # Lightweight YAML parser (no PyYAML dep). Handles:
    #   key: value
    #   key: "quoted value with spaces"
    #   key:           (followed by list or dict on next lines)
    #     - item
    #     key2: value2
    fm = _parse_yaml(fm_raw)
    return fm, body.strip()


def _parse_yaml(text):
    """Minimal YAML parser sufficient for our contribution schema.
    Avoids the PyYAML dependency (Python on macOS is PEP 668 externally-
    managed; would require --break-system-packages to pip-install).

    Supports:
      key: value
      key: "quoted string"
      key:
        - item
        - "quoted item"
      key:
        nested_key: value
        another: [list, of, items]
      [True, False, True, False, "N/A"]   # inline lists
    """
    out = {}
    # Strip comments + blank lines
    lines = []
    for raw in text.split('\n'):
        # Strip line that's only a comment
        stripped = raw.rstrip()
        if not stripped or stripped.lstrip().startswith('#'):
            continue
        # Strip trailing comment, but preserve # in quoted strings
        if '#' in stripped and not _inside_quotes(stripped, stripped.index('#')):
            stripped = stripped[:stripped.index('#')].rstrip()
        lines.append(stripped)

    i = 0
    while i < len(lines):
        line = lines[i]
        # Top-level key (no leading whitespace)
        if not line.startswith(' '):
            if ':' not in line:
                i += 1
                continue
            key, _, rest = line.partition(':')
            key = key.strip()
            rest = rest.strip()
            if rest == '' or rest is None:
                # Block-form value — collect indented children
                children = []
                j = i + 1
                while j < len(lines) and lines[j].startswith('  '):
                    children.append(lines[j][2:])  # strip 2-space indent
                    j += 1
                out[key] = _parse_block(children)
                i = j
            elif rest.startswith('['):
                # Inline list
                out[key] = _parse_inline_list(rest)
                i += 1
            elif rest.startswith('"') and rest.endswith('"'):
                out[key] = rest[1:-1]
                i += 1
            elif rest.startswith("'") and rest.endswith("'"):
                out[key] = rest[1:-1]
                i += 1
            else:
                out[key] = _parse_scalar(rest)
                i += 1
        else:
            i += 1
    return out


def _inside_quotes(s, pos):
    """Return True if position `pos` inside `s` is inside a string literal."""
    in_double = False
    in_single = False
    for i, ch in enumerate(s):
        if i >= pos:
            return in_double or in_single
        if ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "'" and not in_double:
            in_single = not in_single
    return False


def _parse_block(lines):
    """Parse a block (list of '- item' or nested 'key: value')."""
    if not lines:
        return None
    if lines[0].lstrip().startswith('- '):
        # List of items
        items = []
        for line in lines:
            item = line.lstrip()
            if item.startswith('- '):
                v = item[2:].strip()
                if v.startswith('"') and v.endswith('"'):
                    items.append(v[1:-1])
                elif v.startswith("'") and v.endswith("'"):
                    items.append(v[1:-1])
                else:
                    items.append(_parse_scalar(v))
        return items
    else:
        # Nested dict
        out = {}
        i = 0
        while i < len(lines):
            line = lines[i]
            if ':' not in line:
                i += 1
                continue
            key, _, rest = line.partition(':')
            key = key.strip()
            rest = rest.strip()
            if rest.startswith('['):
                out[key] = _parse_inline_list(rest)
            elif rest.startswith('"') and rest.endswith('"'):
                out[key] = rest[1:-1]
            else:
                out[key] = _parse_scalar(rest)
            i += 1
        return out


def _parse_inline_list(s):
    """Parse '[a, b, c]' style inline list."""
    s = s.strip()
    if s.startswith('[') and s.endswith(']'):
        inner = s[1:-1]
    else:
        return [s]
    items = []
    cur = ''
    depth = 0
    in_str = False
    str_char = ''
    for ch in inner:
        if in_str:
            cur += ch
            if ch == str_char:
                in_str = False
            continue
        if ch in '"\'':
            in_str = True
            str_char = ch
            cur += ch
            continue
        if ch == ',' and depth == 0:
            items.append(_parse_scalar(cur.strip()))
            cur = ''
        else:
            cur += ch
    if cur.strip():
        items.append(_parse_scalar(cur.strip()))
    return items


def _parse_scalar(v):
    """Parse a scalar value: true / false / null / "string" / 'string' / number / bare-word."""
    if not v:
        return None
    if v == 'true' or v == 'True':
        return True
    if v == 'false' or v == 'False':
        return False
    if v == 'null' or v == 'None' or v == '~':
        return None
    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]
    if v.startswith("'") and v.endswith("'"):
        return v[1:-1]
    # Number?
    try:
        if '.' in v:
            return float(v)
        return int(v)
    except ValueError:
        return v  # bare word


def load_contributions():
    """Return list of (filepath, frontmatter, body) tuples for every
    contribution file under contributions/<state>/* .md (skipping _template)."""
    out = []
    base = Path(CONTRIB_DIR)
    if not base.exists():
        return out
    for state_dir in sorted(base.iterdir()):
        if not state_dir.is_dir() or state_dir.name.startswith('_'):
            continue
        for md_file in sorted(state_dir.glob('*.md')):
            text = md_file.read_text()
            fm, body = parse_frontmatter(text)
            out.append((str(md_file), fm, body))
    return out


def validate(fm, body, source_path):
    """Return list of validation errors (empty list = valid)."""
    errors = []
    if not fm.get('slug'):
        errors.append(f'{source_path}: missing required field "slug"')
    if not fm.get('state'):
        errors.append(f'{source_path}: missing required field "state"')
    if fm.get('status') and fm['status'] not in VALID_STATUS:
        errors.append(f'{source_path}: invalid status "{fm["status"]}" (must be one of {VALID_STATUS})')
    scores = fm.get('scores') or {}
    has_score_change = False
    for cat_id, vals in scores.items():
        if cat_id not in VALID_CATEGORIES:
            errors.append(f'{source_path}: unknown category "{cat_id}"')
            continue
        if not isinstance(vals, list) or len(vals) != 5:
            errors.append(f'{source_path}: category "{cat_id}" must be a list of 5 values')
            continue
        for i, v in enumerate(vals):
            if v not in (True, False, None, 'N/A', 'keep'):
                errors.append(f'{source_path}: {cat_id}[{i}] = {v!r} — must be true/false/null/"N/A"/"keep"')
            if v != 'keep':
                has_score_change = True
    if (has_score_change or fm.get('status') or fm.get('office')) and not (fm.get('evidence') or []):
        errors.append(f'{source_path}: proposes changes but provides no evidence URLs')
    return errors


def apply_contribution(sc, fm, body, source_path, dry_run=True):
    """Apply one validated contribution to scorecard. Returns list of
    change descriptions."""
    changes = []
    slug = fm.get('slug')
    target = None
    for c in sc.get('candidates', []):
        if c.get('slug') == slug:
            target = c
            break
    if target is None:
        return [f'  ! {source_path}: slug "{slug}" not found in scorecard']

    # Office update
    if fm.get('office') and fm['office'] != target.get('office'):
        changes.append(f"  office: {target.get('office', '')!r} → {fm['office']!r}")
        if not dry_run:
            target['office'] = fm['office']

    # Status update
    if fm.get('status') and fm['status'] != target.get('status'):
        changes.append(f"  status: {target.get('status', 'active')!r} → {fm['status']!r}")
        if not dry_run:
            target['status'] = fm['status']

    # Score updates
    scores_in = fm.get('scores') or {}
    target_scores = target.setdefault('scores', {})
    for cat_id, vals in scores_in.items():
        arr = target_scores.get(cat_id) or [None] * 5
        for i, v in enumerate(vals):
            if v == 'keep':
                continue
            if arr[i] != v:
                changes.append(f"  scores[{cat_id}][{i}]: {arr[i]!r} → {v!r}")
                if not dry_run:
                    arr[i] = v
        if not dry_run:
            target_scores[cat_id] = arr

    # Church affiliation
    ca = fm.get('church_affiliation') or {}
    if ca and ca != (target.get('church_affiliation') or {}):
        changes.append(f"  church_affiliation: setting to {ca.get('name')}")
        if not dry_run:
            target['church_affiliation'] = ca

    # Append narrative body as a note (with provenance)
    if body and body.strip():
        contributor = fm.get('contributor') or 'anonymous'
        prefix = f"\n\n[2026-{contributor.replace(' ', '-')}-contribution] "
        existing_notes = target.get('notes') or ''
        if isinstance(existing_notes, str) and body[:80] not in existing_notes:
            changes.append(f"  notes: appending contributor narrative ({len(body)} chars)")
            if not dry_run:
                target['notes'] = existing_notes + prefix + body

    # Evidence as confidence note
    evidence = fm.get('evidence') or []
    if evidence and (changes):
        prof = target.setdefault('profile', {})
        existing = prof.get('confidence_note') or ''
        new_note = f' [Contributor evidence ({len(evidence)} URLs) — see {source_path}]'
        if not dry_run and new_note not in existing:
            prof['confidence_note'] = (existing + new_note).strip()

    return changes


def main():
    apply_mode = '--apply' in sys.argv
    only = None
    for i, arg in enumerate(sys.argv):
        if arg == '--only' and i + 1 < len(sys.argv):
            only = sys.argv[i + 1]

    contribs = load_contributions()
    if only:
        contribs = [c for c in contribs if only in c[0]]
    print(f'Found {len(contribs)} contribution files.')

    # Validate first
    all_errors = []
    for fp, fm, body in contribs:
        errs = validate(fm, body, fp)
        all_errors.extend(errs)
    if all_errors:
        print(f'\n=== VALIDATION ERRORS ({len(all_errors)}) ===')
        for e in all_errors:
            print(e)
        if not apply_mode:
            print('\nRun with --apply once errors are resolved.')
        return 1

    # Apply
    with open(SCORECARD) as f:
        sc = json.load(f)

    total_changes = 0
    for fp, fm, body in contribs:
        print(f'\n--- {fp} ({fm.get("slug")}) ---')
        changes = apply_contribution(sc, fm, body, fp, dry_run=not apply_mode)
        for c in changes:
            print(c)
        total_changes += len(changes)

    print(f'\n=== TOTAL CHANGES: {total_changes} ===')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
        print('Next: python3 build-data.py && python3 generate-profiles.py && python3 build-search-index.py')
    else:
        print('\nDry-run. Re-run with --apply to write.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
