#!/usr/bin/env python3
"""
merge-duplicate-records.py — fold a duplicate RESOLUTE Citizen slug into the
canonical record for the SAME person, archive the loser (never delete), and
emit a redirect page at the loser's old URL.

Why a sibling script and not dedup-merge-records.py: that script deletes the
loser outright and leaves /candidates/<st>/<old>.html to 404 (or to linger as a
stale profile). The contract says archive, never delete, and old URLs must keep
working. This does both, plus the evidence fold, in one guarded pass.

What it does, in order (all-or-nothing; writes only after every guard passes):
  1. Finds KEEP and DROP (bare slug, or "slug@ST" when a slug is shared).
     Refuses if either is missing/ambiguous, if states differ, or if
     KEEP == DROP.
  2. STATUS: the merged record must never read "former"/"lost" when either
     record is sitting/active. If KEEP is not active but DROP is, the merge
     aborts unless the spec sets KEEP's status explicitly. After the fold the
     script re-checks and aborts on any violation.
  3. EVIDENCE FOLD (cited cells only, never overwrite):
       a DROP cell is carried into KEEP only if
         - it is TRUE/FALSE (not null / N/A),
         - it carries at least one answer footnote that resolves to a URL,
         - the same cell is applicable at KEEP's tier,
         - the question TEXT is identical at both tiers (questions_<tier>
           falls back to questions[]), so a state "has voted for…" answer
           never lands on a different federal question,
         - KEEP's cell is null/absent (KEEP's existing answers always win).
     Uncited DROP booleans are dropped, never copied.
     Footnotes are re-keyed into KEEP (no id collisions).
  4. SOURCES: DROP's sources[] are appended to KEEP's (deduped), minus any in
     spec.sources_skip.
  5. NOTES: one dated, attributed merge line is appended to KEEP's notes
     (plus spec.notes_append if given).
  6. ARCHIVE: DROP is removed from candidates[] and written verbatim to
     data/merged-records.json with merged_into / merged_date / cid / reason /
     fold stats. Restore = move that object back into candidates[] (and
     delete the redirect page); a full pre-write backup also lands in
     data/.backups/.
  7. REDIRECT: candidates/<st>/<drop>.html becomes a noindex meta-refresh +
     canonical + JS stub to /candidates/<st>/<keep>.html.
     build-sitemap-xml.py already skips meta-refresh/noindex pages, and
     generate-profiles.py never deletes orphan files, so the stub persists.

Spec (JSON), one or more merges:
{
  "_meta": {"author": "...", "cid": "MBP-1007-AM", "date": "2026-10-07"},
  "merges": [
    {"keep": "jb-mccuskey", "drop": "jb-mccuskey-ag-2026",
     "reason": "same person: ...",
     "set": {"status": "active"},             # optional scalar sets on KEEP
     "profile": {"confidence": "..."},        # optional profile sets on KEEP
     "sources_skip": ["https://..."],         # optional
     "notes_append": "...",                   # optional
     "fold_skip": ["border_immigration[0]"], # optional: cited-but-weak cells to leave blank
     "fold_cells": true}                      # default true
  ]
}

Usage:
    python3 merge-duplicate-records.py <spec.json> [--dry-run]
"""
import html
import json
import os
import shutil
import sys
from datetime import date, datetime

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
ARCHIVE = os.path.join(REPO, 'data', 'merged-records.json')
BACKUP_DIR = os.path.join(REPO, 'data', '.backups')

sys.path.insert(0, REPO)
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location('refine_records', os.path.join(REPO, 'refine-records.py'))
_rr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_rr)
classify_office_tier = _rr.classify_office_tier
tier_score_100 = _rr.tier_score_100

INACTIVE = {'former', 'lost', 'deceased', 'retired', 'withdrawn'}


def find(cands, raw):
    slug, _, st = raw.partition('@')
    m = [c for c in cands if c.get('slug') == slug]
    if st:
        m = [c for c in m if (c.get('state') or '').upper() == st.upper()]
    if len(m) != 1:
        raise SystemExit(f'ABORT: {raw!r} matched {len(m)} record(s) — key it "slug@ST".')
    return m[0]


def qtext(cat, q, tier):
    alt = cat.get(f'questions_{tier}') if tier != 'federal' else None
    if alt and q < len(alt) and alt[q]:
        return alt[q]
    qs = cat.get('questions') or []
    return qs[q] if q < len(qs) else None


def applicable(cat, q, tier, rubric_cats):
    aa = cat.get('applicable_at') or []
    return cat['id'] in rubric_cats and q < len(aa) and tier in (aa[q] or [])


def is_active(rec):
    return (rec.get('status') or 'active') not in INACTIVE


def redirect_html(keep, drop):
    st = (keep.get('state') or 'us').lower()
    url = f'https://usmcmin.com/candidates/{st}/{keep["slug"]}.html'
    rel = f'{keep["slug"]}.html'
    name = html.escape(keep.get('name') or keep['slug'])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="robots" content="noindex,follow">
  <meta http-equiv="refresh" content="0;url={rel}">
  <title>{name} — RESOLUTE Citizen profile moved</title>
  <link rel="canonical" href="{url}">
  <script>location.replace({json.dumps(rel)});</script>
</head>
<body>
  <!-- merged duplicate slug {html.escape(drop["slug"])} -> {html.escape(keep["slug"])}; archived in data/merged-records.json -->
  <p>This profile moved: <a href="{rel}">{name}</a>.</p>
</body>
</html>
'''


def merge_one(sc, m, today, run_cid):
    cands = sc['candidates']
    keep = find(cands, m['keep'])
    drop = find(cands, m['drop'])
    if keep is drop:
        raise SystemExit('ABORT: keep and drop are the same record.')
    if (keep.get('state') or '').upper() != (drop.get('state') or '').upper():
        raise SystemExit(f'ABORT: state mismatch {keep.get("state")} vs {drop.get("state")}.')

    cats = sc['categories']
    rubrics = sc['meta']['rubrics']

    # --- status guard (never mark a sitting official former) ---
    was_active = is_active(keep) or is_active(drop)
    for k, v in (m.get('set') or {}).items():
        keep[k] = v
    if 'status' in (m.get('set') or {}) and m['set']['status'] in INACTIVE and (is_active(keep) or is_active(drop)):
        raise SystemExit(f'ABORT: spec sets {keep["slug"]} status={m["set"]["status"]} but a record is active.')
    if is_active(drop) and not is_active(keep):
        raise SystemExit(f'ABORT: {drop["slug"]} is active but {keep["slug"]} is {keep.get("status")} — '
                         'set keep status explicitly in the spec.')

    ktier = classify_office_tier(keep)
    dtier = classify_office_tier(drop)
    krub = rubrics[ktier]
    krub_cats = set(krub['pillar_a'] + krub['pillar_b'])
    drub_cats = set(rubrics[dtier]['pillar_a'] + rubrics[dtier]['pillar_b'])
    old_score = tier_score_100(keep.get('scores') or {}, None, ktier, krub)

    kscores = keep.setdefault('scores', {})
    kfn = keep.setdefault('footnotes', {})
    kaf = keep.setdefault('answer_footnotes', {})
    dscores = drop.get('scores') or {}
    dfn = drop.get('footnotes') or {}
    daf = drop.get('answer_footnotes') or {}
    url_to_fid = {v.get('url'): k for k, v in kfn.items() if isinstance(v, dict) and v.get('url')}

    def fid_for(fn):
        u = fn['url']
        if u in url_to_fid:
            return url_to_fid[u]
        n = len(kfn) + 1
        while f'm{n}' in kfn:
            n += 1
        fid = f'm{n}'
        kfn[fid] = dict(fn)
        url_to_fid[u] = fid
        return fid

    stats = {'folded': [], 'skipped_uncited': 0, 'skipped_keep_has_value': 0,
             'skipped_text_differs': 0, 'skipped_not_applicable': 0, 'skipped_by_spec': 0}
    fold_skip = set(m.get('fold_skip') or [])   # e.g. ["border_immigration[0]"]: cited but inferential
    if m.get('fold_cells', True):
        for cat in cats:
            cid = cat['id']
            drow = dscores.get(cid) or []
            for q in range(5):
                dv = drow[q] if q < len(drow) else None
                if dv not in (True, False):
                    continue
                if f'{cid}[{q}]' in fold_skip:
                    stats['skipped_by_spec'] += 1
                    continue
                if not applicable(cat, q, dtier, drub_cats):
                    continue
                refs = ((daf.get(cid) or [[]] * 5) + [[]] * 5)[q] or []
                fns = [dfn[r] for r in refs if isinstance(dfn.get(r), dict) and dfn[r].get('url')]
                if not fns:
                    stats['skipped_uncited'] += 1
                    continue
                if not applicable(cat, q, ktier, krub_cats):
                    stats['skipped_not_applicable'] += 1
                    continue
                if qtext(cat, q, ktier) != qtext(cat, q, dtier):
                    stats['skipped_text_differs'] += 1
                    continue
                krow = kscores.setdefault(cid, [None] * 5)
                while len(krow) < 5:
                    krow.append(None)
                if krow[q] in (True, False):
                    stats['skipped_keep_has_value'] += 1
                    continue
                krow[q] = dv
                arow = kaf.setdefault(cid, [[] for _ in range(5)])
                while len(arow) < 5:
                    arow.append([])
                arow[q] = [fid_for(fn) for fn in fns]
                stats['folded'].append(f'{cid}[{q}]={dv}')

    # --- sources ---
    skip = set(m.get('sources_skip') or [])
    srcs = list(keep.get('sources') or [])
    for s in (drop.get('sources') or []):
        if s not in srcs and s not in skip:
            srcs.append(s)
    keep['sources'] = srcs

    # --- profile ---
    prof = keep.setdefault('profile', {})
    for k, v in (m.get('profile') or {}).items():
        prof[k] = v
    prof['last_refined'] = today

    # --- notes ---
    line = (f'Merged duplicate record {drop["slug"]} into this one on {today} ({run_cid}): {m.get("reason", "same person")}. '
            f'{len(stats["folded"])} cited cell(s) carried over; uncited answers from the duplicate were not carried. '
            f'Old URL redirects here.')
    if m.get('notes_append'):
        line += ' ' + m['notes_append'].strip()
    n = keep.get('notes')
    if isinstance(n, dict):
        n = '\n'.join(f'{k.replace("_", " ")}: {v}' for k, v in n.items() if v)
    keep['notes'] = ((n or '').strip() + '\n\n' + line).strip()

    # --- post-check ---
    if was_active and not is_active(keep):
        raise SystemExit(f'ABORT: {keep["slug"]} would end inactive.')
    for cat in cats:
        row = kscores.get(cat['id']) or []
        for q in range(min(5, len(row))):
            # pre-existing stale out-of-tier cells are left alone (refine-records masks them
            # on its next pass); the fold itself can never write one (checked above).
            if not applicable(cat, q, ktier, krub_cats) and row[q] not in ('N/A', None):
                print(f'   note: pre-existing out-of-tier {keep["slug"]} {cat["id"]}[{q}]={row[q]!r} (untouched)')
    new_score = tier_score_100(kscores, None, ktier, krub)

    cands.remove(drop)
    arch = {'merged_into': keep['slug'], 'merged_into_state': keep.get('state'),
            'merged_date': today, 'cid': run_cid, 'reason': m.get('reason'),
            'fold': {k: v for k, v in stats.items()},
            'restore': 'move .record back into scorecard.json candidates[] and delete the redirect page',
            'record': drop}
    return keep, drop, arch, ktier, dtier, old_score, new_score, stats


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry = '--dry-run' in sys.argv
    if len(args) != 1:
        raise SystemExit('usage: merge-duplicate-records.py <spec.json> [--dry-run]')
    spec = json.load(open(args[0], encoding='utf-8'))
    meta = spec.get('_meta') or {}
    cid = meta.get('cid') or 'unattributed'
    today = meta.get('date') or date.today().isoformat()

    raw = open(SCORECARD, encoding='utf-8').read()
    sc = json.loads(raw)
    archive = json.load(open(ARCHIVE, encoding='utf-8')) if os.path.exists(ARCHIVE) else {'merged': []}

    pages = []
    for m in spec['merges']:
        if any(a['record'].get('slug') == m['drop'].partition('@')[0] and
               (a.get('merged_into') == m['keep'].partition('@')[0]) for a in archive['merged']):
            print(f'{m["drop"]} already merged into {m["keep"]} — skip (idempotent)')
            continue
        keep, drop, arch, kt, dt, o, n, st = merge_one(sc, m, today, cid)
        archive['merged'].append(arch)
        pages.append((keep, drop))
        print(f'MERGE {drop["slug"]} ({dt}, status={drop.get("status")}) -> {keep["slug"]} ({kt}, status={keep.get("status")})')
        print(f'   score {o} -> {n}; folded {len(st["folded"])}: {", ".join(st["folded"]) or "-"}')
        print(f'   skipped: uncited={st["skipped_uncited"]} keep_has_value={st["skipped_keep_has_value"]} '
              f'text_differs={st["skipped_text_differs"]} not_applicable={st["skipped_not_applicable"]} '
              f'by_spec={st["skipped_by_spec"]}')

    if dry or not pages:
        print('[dry-run] nothing written.' if dry else 'nothing to do.')
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)
    backup = os.path.join(BACKUP_DIR, f'scorecard.{datetime.now():%Y%m%d-%H%M%S}.pre-merge.json')
    shutil.copy2(SCORECARD, backup)
    sc.setdefault('meta', {})['last_updated'] = today
    # match the file's existing layout (minified vs indented) to keep the diff honest
    minified = not raw.lstrip().startswith('{\n')
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        if minified:
            json.dump(sc, f, ensure_ascii=False, separators=(',', ':'))
        else:
            json.dump(sc, f, indent=2, ensure_ascii=False)
        f.write('\n')
    with open(ARCHIVE, 'w', encoding='utf-8') as f:
        json.dump(archive, f, indent=1, ensure_ascii=False)
        f.write('\n')
    for keep, drop in pages:
        p = os.path.join(REPO, 'candidates', (drop.get('state') or 'us').lower(), f'{drop["slug"]}.html')
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(redirect_html(keep, drop))
        print(f'redirect: {os.path.relpath(p, REPO)} -> {keep["slug"]}.html')
    print(f'backup: {os.path.relpath(backup, REPO)}\nwrote scorecard.json + merged-records.json')


if __name__ == '__main__':
    main()
