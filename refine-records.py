#!/usr/bin/env python3
"""
refine-records.py — the reusable RESOLUTE Citizen refinement engine.

Takes an *evidence dossier* (a JSON file) and applies it to
data/scorecard.json safely, idempotently, and tier-correctly. This is the
sustainable engine behind the city-by-city / state-by-state finalization
effort: research a candidate, encode the evidence in a dossier, run this.

Why an engine (vs. another one-off apply-*.py): every refinement now goes
through ONE validated path that

  1. Backs up scorecard.json before writing.
  2. Derives each candidate's tier (federal/state/local) and the *exact*
     applicable questions FROM scorecard.json's own categories[].applicable_at
     and meta.rubrics — so N/A masking is always correct and self-updating
     if the rubric changes.
  3. Rebuilds the full scores dict for ALL categories: applicable cells take
     the dossier's evidence value (true/false/null); every out-of-tier cell
     is forced to "N/A". This auto-fixes records that pre-date a rubric
     change (e.g. local records missing public_justice / refuse_state_overreach).
  4. Writes per-answer citations: footnotes{} + answer_footnotes{} keyed by
     CATEGORY ID (the v3.4 schema the profile generator reads), replacing any
     stale old-pillar-keyed answer_footnotes.
  5. Validates the result (no scoreable cell left "N/A"; no out-of-tier cell
     left non-N/A) and prints an old->new /100 diff per record.

Dossier format (JSON):
{
  "_meta": {"author": "...", "date": "2026-06-01", "note": "FXBG finalize"},
  "records": {
    "<slug>": {
      "set":     {"party":"D","status":"active","candidacy_status":"...","office":"...","website":"...","photo":"..."},
      "profile": {"confidence":"evidence_local","religion":"...","background":"...","education":"..."},
      "notes_set":    "replace notes entirely (optional)",
      "notes_append": "append to notes (optional)",
      "sources_add":  ["https://...", "..."],
      "evidence": {
        "<category_id>": {
          "0": {"v": true,  "src": ["https://..."], "note": "why"},
          "1": {"v": false, "src": ["https://..."], "note": "why"},
          "2": {"v": null,  "src": ["https://..."], "note": "looked, no public position"}
        }
      }
    }
  }
}

Notes:
- "v" must be one of true / false / null. Only cells APPLICABLE at the
  candidate's tier may carry evidence; evidence on an out-of-tier cell is a
  hard error (protects against scoring a school-board member on foreign policy).
- Omit a cell entirely to leave it at its current value (or null if new).
- Run with --dry-run to preview the diff without writing.
- Run with --no-build to skip the build pipeline (just write scorecard.json).

Usage:
    python3 refine-records.py refinements/fxbg-2026-06.json
    python3 refine-records.py refinements/fxbg-2026-06.json --dry-run
    python3 refine-records.py refinements/fxbg-2026-06.json --no-build
"""
import json
import os
import re
import sys
import shutil
import subprocess
from datetime import date, datetime

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
BACKUP_DIR = os.path.join(REPO, 'data', '.backups')

VALID_VALUES = (True, False, None)

# Human-friendly publisher names for common sources (footnote display).
PUBLISHER_MAP = {
    'ballotpedia.org': 'Ballotpedia',
    'vpap.org': 'Virginia Public Access Project',
    'fredericksburgva.gov': 'City of Fredericksburg',
    'cityschools.com': 'Fredericksburg City Public Schools',
    'fxbgadvance.com': 'Fredericksburg Advance',
    'fredericksburgfreepress.com': 'Fredericksburg Free Press',
    'progressivevotersguide.com': 'Progressive Voters Guide',
    'fredericksburg.com': 'The Free Lance-Star',
    'virginiascope.com': 'Virginia Scope',
    'wfls.com': 'WFLS',
    'whsv.com': 'WHSV',
    'nbc12.com': 'NBC12',
    'wric.com': 'WRIC',
    'wtvr.com': 'WTVR CBS 6',
    'apnews.com': 'Associated Press',
    'lis.virginia.gov': 'Virginia Legislative Information System',
    'legacy.lis.virginia.gov': 'Virginia LIS',
    'votesmart.org': 'Vote Smart',
    'opensecrets.org': 'OpenSecrets',
    'fec.gov': 'Federal Election Commission',
    'wikipedia.org': 'Wikipedia',
    'x.com': 'X (Twitter)',
    'twitter.com': 'X (Twitter)',
    'facebook.com': 'Facebook',
    'richmond.com': 'Richmond Times-Dispatch',
    'cardinalnews.org': 'Cardinal News',
    'virginiamercury.com': 'Virginia Mercury',
}


def classify_office_tier(c):
    """EXACT mirror of generate-profiles.py classify_office_tier (v4.1+).
    Keep in sync if that function changes."""
    office = c.get('office') or ''
    if not office:
        jur = (c.get('jurisdiction') or '').lower()
        if 'executive branch' in jur or 'judicial branch' in jur:
            return 'federal'
        return 'state'
    o = office.lower()
    if re.search(r'\b(president|vice president|u\.?s\.?\s+sen|u\.?s\.?\s+hous|u\.?s\.?\s+rep|'
                 r'united states sen|united states hous|united states rep|secretary of|'
                 r'acting attorney general|attorney general of the united states|'
                 r'director of|administrator of|ambassador|chief of staff|deputy chief of staff|'
                 r'homeland security advisor|chief justice|associate justice.+supreme court|'
                 r'special envoy)', o):
        if re.search(r'^attorney general$|state attorney general', o) and 'united states' not in o:
            return 'state'
        return 'federal'
    if re.search(r'\bgovernor\b|^lt\.?\s+governor|lieutenant governor|'
                 r'state senator|state senate|state representative|state hous|'
                 r'state assembl|^delegate$|delegate \(', o):
        return 'state'
    if re.search(r'^attorney general$|secretary of state$|state treasurer|state auditor|'
                 r'state comptroller', o):
        return 'state'
    if 'state supreme court' in o or re.search(r'(chief justice|justice).+state', o):
        return 'state'
    if re.search(r'\bmayor\b|city council|town council|borough council|'
                 r'county (commissioner|supervisor|judge|board)|'
                 r'school board|board of education|'
                 r'district attorney|sheriff|city clerk|city attorney|'
                 r'commonwealth\'?s attorney', o):
        return 'local'
    return 'state'


def domain_of(url):
    m = re.match(r'https?://([^/]+)', url or '')
    if not m:
        return ''
    host = m.group(1).lower()
    if host.startswith('www.'):
        host = host[4:]
    return host


def publisher_for(url):
    host = domain_of(url)
    if host in PUBLISHER_MAP:
        return PUBLISHER_MAP[host]
    # try the registrable domain (strip subdomain)
    parts = host.split('.')
    if len(parts) >= 2:
        reg = '.'.join(parts[-2:])
        if reg in PUBLISHER_MAP:
            return PUBLISHER_MAP[reg]
    return host or 'Source'


def calc_cat_score(answers):
    """EXACT mirror of generate-profiles.calc_cat_score: True→+2 (score+answered);
    False→answered only; None/'N/A'→neither. Returns (raw_true_points, answered_count)."""
    raw = sum(1 for a in answers if a is True)
    answered = sum(1 for a in answers if a is True or a is False)
    return raw * 2, answered


def tier_score_100(scores, categories_by_id, tier, rubric):
    """Compute the displayed /100 headline exactly as generate-profiles.py does:
    a dynamic-max percentage = (True×2 summed) / (answered×2) × 100 over the
    tier's rubric categories. null and N/A are excluded from the denominator
    (they neither help nor penalize). Returns None if nothing is answered."""
    cat_ids = rubric['pillar_a'] + rubric['pillar_b']
    total_score = 0
    answered = 0
    for cid in cat_ids:
        s, a = calc_cat_score(scores.get(cid, []))
        total_score += s
        answered += a
    if answered == 0:
        return None
    return round((total_score / (answered * 2)) * 100)


def apply_record(rec, dossier_entry, categories, categories_by_id, rubrics, fresh_date,
                 reset_unspecified=False):
    """Mutate rec in place per the dossier entry. Returns a report dict.

    reset_unspecified: when True, any tier-applicable cell with NO evidence in
    the dossier is set to null (clears prior speculative answers) rather than
    preserving the existing value. Use for full finalizations where the dossier
    is the complete, deliberate scoring of a record."""
    slug = rec.get('slug')
    name = rec.get('name')
    reset_unspecified = dossier_entry.get('reset_unspecified', reset_unspecified)

    # --- snapshot old tier score for the diff ---
    tier = classify_office_tier(rec)
    rubric = rubrics[tier]
    old_score = tier_score_100(rec.get('scores', {}), categories_by_id, tier, rubric)

    # --- 1. scalar field sets ---
    for k, v in (dossier_entry.get('set') or {}).items():
        rec[k] = v

    # tier may change if office was edited
    tier = classify_office_tier(rec)
    rubric = rubrics[tier]
    rubric_cats = set(rubric['pillar_a'] + rubric['pillar_b'])

    # --- 2. profile sub-object ---
    prof = rec.setdefault('profile', {})
    for k, v in (dossier_entry.get('profile') or {}).items():
        prof[k] = v
    prof['last_refined'] = fresh_date
    if 'confidence' not in prof and 'confidence' not in (dossier_entry.get('profile') or {}):
        prof['confidence'] = f'evidence_{tier}'

    # --- 3. notes ---
    if 'notes_set' in dossier_entry:
        rec['notes'] = dossier_entry['notes_set']
    elif dossier_entry.get('notes_append'):
        existing = (rec.get('notes') or '').strip()
        add = dossier_entry['notes_append'].strip()
        if add and add not in existing:
            rec['notes'] = (existing + ('\n\n' if existing else '') + add).strip()

    # --- 4. sources ---
    sources = list(rec.get('sources') or [])
    for s in (dossier_entry.get('sources_add') or []):
        if s not in sources:
            sources.append(s)

    # --- 5. rebuild scores tier-correctly for ALL categories ---
    evidence = dossier_entry.get('evidence') or {}
    old_scores = rec.get('scores', {}) or {}
    new_scores = {}
    footnotes = dict(rec.get('footnotes') or {})  # keep any non-synthetic existing
    # drop any synthetic party-default footnote (we are upgrading to evidence)
    footnotes.pop('_pd', None)
    answer_footnotes = {}
    url_to_fnid = {}
    cells_changed = 0
    cells_with_evidence = 0
    issues = []

    def fnid_for(url):
        if url in url_to_fnid:
            return url_to_fnid[url]
        fid = f'r{len(url_to_fnid) + 1}'
        url_to_fnid[url] = fid
        return fid

    for cat in categories:
        cid = cat['id']
        aa = cat.get('applicable_at') or []
        in_rubric = cid in rubric_cats
        row = []
        fn_row = [[] for _ in range(5)]
        ev_cat = evidence.get(cid, {})
        for q in range(5):
            applicable = in_rubric and (q < len(aa)) and (tier in (aa[q] or []))
            if not applicable:
                # any evidence supplied for an out-of-tier cell is an error
                if str(q) in ev_cat:
                    issues.append(f'{slug}: evidence on out-of-tier cell {cid}[{q}] (tier={tier}) — ignored')
                row.append('N/A')
                continue
            cell = ev_cat.get(str(q))
            if cell is not None:
                v = cell.get('v', None)
                if v not in VALID_VALUES:
                    raise ValueError(f'{slug}: {cid}[{q}] value {v!r} not in true/false/null')
                row.append(v)
                cells_with_evidence += 1
                for u in (cell.get('src') or []):
                    fid = fnid_for(u)
                    if fid not in fn_row[q]:
                        fn_row[q].append(fid)
                    if fid not in footnotes:
                        footnotes[fid] = {
                            'url': u,
                            'title': cell.get('note') or publisher_for(u),
                            'publisher': publisher_for(u),
                            'accessed': fresh_date,
                            'excerpt': cell.get('note') or '',
                            'archive_url': None,
                        }
            else:
                # No evidence supplied for this applicable cell.
                # reset_unspecified → null it (clear prior guesses);
                # otherwise preserve an existing real answer (else null).
                if reset_unspecified:
                    row.append(None)
                else:
                    prev = old_scores.get(cid, [])
                    pv = prev[q] if q < len(prev) else None
                    row.append(pv if pv in VALID_VALUES else None)
        # detect change vs old
        prev = old_scores.get(cid, [])
        for q in range(5):
            pv = prev[q] if q < len(prev) else None
            if row[q] != pv:
                cells_changed += 1
        new_scores[cid] = row
        if in_rubric and any(fid for sub in fn_row for fid in sub):
            answer_footnotes[cid] = fn_row

    rec['scores'] = new_scores
    rec['footnotes'] = footnotes
    rec['answer_footnotes'] = answer_footnotes
    rec['sources'] = sources

    new_score = tier_score_100(new_scores, categories_by_id, tier, rubric)

    # --- 6. validate ---
    for cat in categories:
        cid = cat['id']
        aa = cat.get('applicable_at') or []
        in_rubric = cid in rubric_cats
        for q in range(5):
            applicable = in_rubric and (q < len(aa)) and (tier in (aa[q] or []))
            val = new_scores[cid][q]
            if applicable and val == 'N/A':
                issues.append(f'{slug}: scoreable cell {cid}[{q}] left N/A')
            if (not applicable) and val != 'N/A':
                issues.append(f'{slug}: out-of-tier cell {cid}[{q}] = {val!r} (should be N/A)')

    return {
        'slug': slug, 'name': name, 'tier': tier,
        'old_score': old_score, 'new_score': new_score,
        'cells_changed': cells_changed, 'cells_with_evidence': cells_with_evidence,
        'sources': len(sources), 'footnotes': len(footnotes),
        'issues': issues,
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = {a for a in sys.argv[1:] if a.startswith('--')}
    if not args:
        raise SystemExit('usage: refine-records.py <dossier.json> [--dry-run] [--no-build]')
    dossier_path = args[0]
    dry = '--dry-run' in flags
    no_build = '--no-build' in flags

    with open(dossier_path, encoding='utf-8') as f:
        dossier = json.load(f)
    records_spec = dossier.get('records') or {}
    if not records_spec:
        raise SystemExit(f'no records in {dossier_path}')

    with open(SCORECARD, encoding='utf-8') as f:
        sc = json.load(f)
    categories = sc['categories']
    categories_by_id = {c['id']: c for c in categories}
    rubrics = sc['meta']['rubrics']
    by_slug = {c.get('slug'): c for c in sc['candidates']}

    fresh_date = date.today().isoformat()
    dossier_reset = bool(dossier.get('reset_unspecified', False))
    reports = []
    all_issues = []
    missing = []
    for slug, entry in records_spec.items():
        rec = by_slug.get(slug)
        if not rec:
            missing.append(slug)
            continue
        rep = apply_record(rec, entry, categories, categories_by_id, rubrics, fresh_date,
                           reset_unspecified=dossier_reset)
        reports.append(rep)
        all_issues.extend(rep['issues'])

    # --- report ---
    print(f'\n{"="*78}\nRefinement: {dossier_path}')
    meta = dossier.get('_meta', {})
    if meta:
        print(f'  {meta.get("note","")} — {meta.get("author","")} {meta.get("date","")}')
    print(f'{"="*78}')
    print(f'{"slug":30s} {"tier":6s} {"old":>4s} {"new":>4s}  {"chg":>3s} {"ev":>3s} {"src":>3s}')
    print('-' * 78)
    for r in sorted(reports, key=lambda x: x['slug']):
        arrow = '' if r['old_score'] == r['new_score'] else ' *'
        os_ = '—' if r['old_score'] is None else str(r['old_score'])
        ns_ = '—' if r['new_score'] is None else str(r['new_score'])
        print(f'{r["slug"][:30]:30s} {r["tier"]:6s} {os_:>4s} {ns_:>4s}  '
              f'{r["cells_changed"]:>3d} {r["cells_with_evidence"]:>3d} {r["sources"]:>3d}{arrow}')
    print('-' * 78)
    print(f'{len(reports)} record(s) refined, {sum(r["cells_with_evidence"] for r in reports)} evidence cells set')
    if missing:
        print(f'\n!! {len(missing)} slug(s) NOT FOUND: {missing}')
    if all_issues:
        print(f'\n!! {len(all_issues)} VALIDATION ISSUE(S):')
        for i in all_issues:
            print(f'   - {i}')

    hard_errors = [i for i in all_issues if 'left N/A' in i or 'should be N/A' in i]
    if hard_errors:
        raise SystemExit('\nABORT: hard validation errors — not writing. Fix the dossier.')

    if dry:
        print('\n[dry-run] no files written.')
        return

    # --- backup + write ---
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = os.path.join(BACKUP_DIR, f'scorecard.{ts}.json')
    shutil.copy2(SCORECARD, backup)
    print(f'\nBackup: {os.path.relpath(backup, REPO)}')

    sc.setdefault('meta', {})['last_updated'] = fresh_date
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'Wrote {os.path.relpath(SCORECARD, REPO)}')

    if no_build:
        print('[--no-build] skipping build pipeline. Run it before deploy:')
        print('  python3 build-data.py && python3 build-search-index.py && '
              'python3 generate-profiles.py && python3 build-category-pages.py && '
              'python3 build-sitemap-xml.py')
        return

    print('\nRunning build pipeline...')
    for step in ['build-data.py', 'build-search-index.py']:
        print(f'  $ python3 {step}')
        subprocess.run(['python3', os.path.join(REPO, step)], check=True, cwd=REPO)
    print('  (run generate-profiles.py + build-category-pages.py + build-sitemap-xml.py '
          'next; skipped here for speed — they regenerate thousands of files)')


if __name__ == '__main__':
    main()
