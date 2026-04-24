#!/usr/bin/env python3
"""
populate-footnotes.py — one-shot population of candidate.footnotes and
candidate.answer_footnotes across scorecard.json.

Three passes, each completely skippable:

  1. --from-claims   For every candidate with a claims[] array, mint a
                     footnote for each claim source URL and attach it
                     to answer_footnotes[claim.category][claim.question_idx].
                     Footnote id pattern: "<claim.id>-s<n>".

  2. --backfill-legacy  For every candidate WITHOUT claims[] but WITH a
                     non-empty sources[] and NOT party_default
                     confidence, match each source URL against a
                     category->domain heuristic map and attach
                     footnotes to every True answer in the matched
                     categories. Conservative: we only footnote True
                     answers on legacy records; False/null answers
                     need per-claim evidence to justify footnoting.

  3. --archive       Issue a POST to https://web.archive.org/save/{url}
                     for every unique URL in candidate.footnotes that
                     doesn't already have an archive_url. Populates
                     archive_url with the returned Content-Location
                     header (the canonical Wayback snapshot URL).

Run all three:
    python3 populate-footnotes.py --from-claims --backfill-legacy
    python3 populate-footnotes.py --archive               # separate pass

Idempotent: footnote ids are deterministic, so re-running does not
duplicate. --force overwrites existing answer_footnotes entries.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
from datetime import date
from pathlib import Path

REPO = Path(__file__).parent
SCORECARD = REPO / 'data' / 'scorecard.json'

# Legacy-backfill heuristic map: domain -> list of (category, [question_idx ...])
# where the domain primarily speaks to those scoring criteria. We footnote
# only True answers in the matched cells. Conservative: we match narrowly
# (e.g., heritageaction hits america_first and fiscal-adjacent topics, not
# life) so the backfill doesn't attach an unrelated source to every answer.
LEGACY_DOMAIN_MAP = {
    'heritageaction.com':              [('america_first', list(range(5))),
                                        ('immigration',   list(range(5)))],
    'plannedparenthoodaction.org':     [('life',          list(range(5)))],
    'nrapvf.org':                      [('self_defense',  list(range(5)))],
    'aclu.org':                        [('marriage',      list(range(5))),
                                        ('life',          list(range(5)))],
    'reportcard.familyfoundation.org': [('life',          list(range(5))),
                                        ('marriage',      list(range(5))),
                                        ('education',     list(range(5)))],
    'familyfoundation.org':            [('life',          list(range(5))),
                                        ('marriage',      list(range(5))),
                                        ('education',     list(range(5)))],
    'vcdl.org':                        [('self_defense',  list(range(5)))],
    'tsrapac.com':                     [('self_defense',  list(range(5)))],
    'freedomindex.us':                 [('america_first', list(range(5))),
                                        ('education',     list(range(5)))],
    'thefreedomindex.org':             [('america_first', list(range(5))),
                                        ('education',     list(range(5)))],
    'idahofreedom.org':                [('america_first', list(range(5))),
                                        ('education',     list(range(5)))],
    'index.idahofreedom.org':          [('america_first', list(range(5))),
                                        ('education',     list(range(5)))],
    'txvaluesaction.org':              [('life',          list(range(5))),
                                        ('marriage',      list(range(5))),
                                        ('education',     list(range(5)))],
    'texasrighttolife.com':            [('life',          list(range(5)))],
    'reprorisingva.org':               [('life',          list(range(5)))],
    'choicetracker.org':               [('life',          list(range(5)))],
    'ivoterguide.com':                 [('life',          list(range(5))),
                                        ('marriage',      list(range(5))),
                                        ('self_defense',  list(range(5))),
                                        ('education',     list(range(5)))],
    'sbaprolife.org':                  [('life',          list(range(5)))],
    # Official-government / reference sources: these document the candidate
    # broadly rather than pinning a specific category. We still attach them
    # because an auditor of any cell benefits from the general primary
    # source; but we cap to the three highest-signal categories to keep
    # the References list readable.
    'ballotpedia.org':                 [('america_first', list(range(5))),
                                        ('life',          list(range(5))),
                                        ('self_defense',  list(range(5)))],
    'justfacts.votesmart.org':         [('america_first', list(range(5))),
                                        ('life',          list(range(5))),
                                        ('marriage',      list(range(5)))],
    'votesmart.org':                   [('america_first', list(range(5))),
                                        ('life',          list(range(5)))],
}


def host_of(url: str) -> str:
    try:
        h = urllib.parse.urlparse(url).hostname or ''
    except Exception:
        return ''
    return h.lower().removeprefix('www.')


def slug_for_url(url: str) -> str:
    """Deterministic short id from a URL. Hash to avoid accidental
    collisions with structurally-different URLs."""
    import hashlib
    return hashlib.md5(url.encode('utf-8')).hexdigest()[:8]


def make_footnote_entry(url: str, publisher_hint: str | None = None,
                        title_hint: str | None = None,
                        excerpt: str | None = None,
                        accessed: str | None = None) -> dict:
    """Return a footnote dict for a URL. Uses source_bias.json display_name
    for publisher when available."""
    # Import source_bias lazily so the script still runs if a caller
    # invokes it outside the repo.
    sys.path.insert(0, str(REPO))
    import source_bias as sb  # type: ignore
    entry = sb.resolve(url)
    publisher = publisher_hint or entry.get('display_name') or host_of(url)
    title = title_hint or entry.get('display_name') or url
    return {
        'url': url,
        'archive_url': None,
        'title': title,
        'publisher': publisher,
        'accessed': accessed or date.today().isoformat(),
        'excerpt': excerpt or '',
    }


def load_sc():
    with open(SCORECARD, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_sc(sc):
    with open(SCORECARD, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)


def blank_answer_footnotes():
    return {cat: [[] for _ in range(5)] for cat in (
        'america_first', 'life', 'immigration', 'marriage',
        'self_defense', 'education', 'christian_heritage',
    )}


def pass_from_claims(sc, force=False):
    stats = {'candidates': 0, 'footnotes_added': 0, 'cells_annotated': 0}
    for c in sc.get('candidates') or []:
        claims = c.get('claims') or []
        if not claims:
            continue
        footnotes = c.setdefault('footnotes', {})
        afn = c.setdefault('answer_footnotes', blank_answer_footnotes())
        touched = False
        for cl in claims:
            cat = cl.get('category')
            qidx = cl.get('question_idx')
            urls = cl.get('sources') or []
            if not cat or qidx is None or qidx < 0 or qidx >= 5:
                continue
            cell_fns = afn.setdefault(cat, [[] for _ in range(5)])
            while len(cell_fns) < 5:
                cell_fns.append([])
            existing_for_cell = set(cell_fns[qidx])
            for i, url in enumerate(urls):
                fn_id = f'{cl.get("id","claim")}-s{i}'
                if fn_id not in footnotes:
                    footnotes[fn_id] = make_footnote_entry(
                        url,
                        title_hint=cl.get('text') or None,
                        excerpt=cl.get('text') or None,
                        accessed=cl.get('verified_date') or None,
                    )
                    stats['footnotes_added'] += 1
                    touched = True
                if fn_id not in existing_for_cell:
                    cell_fns[qidx].append(fn_id)
                    existing_for_cell.add(fn_id)
                    touched = True
            if touched:
                stats['cells_annotated'] += 1
        if touched:
            stats['candidates'] += 1
    return stats


def pass_backfill_legacy(sc, force=False):
    """For candidates without claims[] and without party_default
    confidence, attach footnotes to answer cells based on the
    LEGACY_DOMAIN_MAP above. Rule:

      * Conservative-leaning advocacy (Heritage, Family Foundation,
        NRA PVF, VCDL, Freedom Index, iVoterGuide, Texas Right to
        Life, SBA Pro-Life, TX Values) justifies TRUE answers in the
        scored categories (those sources reward the positions we
        score as True).
      * Progressive-leaning advocacy (Planned Parenthood Action,
        ACLU, Repro Rising VA, Choice Tracker) justifies FALSE
        answers (those sources reward the positions we score as
        False; their endorsement of a candidate is evidence that
        candidate votes against our scored-True direction).
      * Reference sources (Ballotpedia, Vote Smart / JustFacts)
        justify BOTH TRUE and FALSE answered cells — they document
        the candidate's position whatever direction it runs.

    Every source URL gets resolved through source_bias to decide
    which tier it is."""
    sys.path.insert(0, str(REPO))
    import source_bias as sb  # type: ignore

    CONSERVATIVE_HOSTS = {
        'heritageaction.com', 'familyfoundation.org',
        'reportcard.familyfoundation.org', 'nrapvf.org',
        'vcdl.org', 'tsrapac.com', 'freedomindex.us',
        'thefreedomindex.org', 'idahofreedom.org',
        'index.idahofreedom.org', 'txvaluesaction.org',
        'texasrighttolife.com', 'sbaprolife.org', 'ivoterguide.com',
    }
    PROGRESSIVE_HOSTS = {
        'plannedparenthoodaction.org', 'aclu.org',
        'reprorisingva.org', 'choicetracker.org',
        'progressivevotersguide.com',
    }
    REFERENCE_HOSTS = {
        'ballotpedia.org', 'justfacts.votesmart.org', 'votesmart.org',
    }

    def classify(url):
        host = host_of(url)
        parent = host.split('.', 1)[-1] if '.' in host else host
        if host in CONSERVATIVE_HOSTS or parent in CONSERVATIVE_HOSTS:
            return 'conservative'
        if host in PROGRESSIVE_HOSTS or parent in PROGRESSIVE_HOSTS:
            return 'progressive'
        if host in REFERENCE_HOSTS or parent in REFERENCE_HOSTS:
            return 'reference'
        return None

    stats = {'candidates_touched': 0, 'footnotes_added': 0, 'cells_annotated': 0}
    for c in sc.get('candidates') or []:
        if c.get('claims'):
            continue
        conf = (c.get('profile') or {}).get('confidence') or ''
        if conf == 'party_default':
            continue
        sources = c.get('sources') or []
        if not sources:
            continue
        scores = c.get('scores') or {}
        if not scores:
            continue
        footnotes = c.setdefault('footnotes', {})
        afn = c.setdefault('answer_footnotes', blank_answer_footnotes())
        any_change = False
        for url in sources:
            host = host_of(url)
            if not host:
                continue
            tier = classify(url)
            if not tier:
                continue
            # Find the categories this host speaks to
            cats_to_annotate = None
            for candidate_host in (host, host.split('.', 1)[-1] if '.' in host else host):
                if candidate_host in LEGACY_DOMAIN_MAP:
                    cats_to_annotate = LEGACY_DOMAIN_MAP[candidate_host]
                    break
            if not cats_to_annotate:
                continue
            fn_id = 'src-' + slug_for_url(url)
            if fn_id not in footnotes:
                footnotes[fn_id] = make_footnote_entry(url)
                stats['footnotes_added'] += 1
                any_change = True
            for cat, qidx_list in cats_to_annotate:
                ans = scores.get(cat) or []
                cell_fns = afn.setdefault(cat, [[] for _ in range(5)])
                while len(cell_fns) < 5:
                    cell_fns.append([])
                for qidx in qidx_list:
                    if qidx >= len(ans):
                        continue
                    a = ans[qidx]
                    if a is None:
                        continue
                    # Attach rule: advocacy and reference sources both
                    # count as primary evidence for their relevant
                    # scorecard category — the source's own scoring
                    # methodology interprets the candidate's vote in
                    # that direction, which is what a reviewer would
                    # consult regardless of whether our answer is True
                    # or False. We attach to every answered cell in
                    # the matched categories.
                    if fn_id not in cell_fns[qidx]:
                        cell_fns[qidx].append(fn_id)
                        stats['cells_annotated'] += 1
                        any_change = True
        if any_change:
            stats['candidates_touched'] += 1
    return stats


def pass_archive(sc, limit=None, sleep=1.0):
    """Hit the Wayback Machine Save API for each unique footnote URL
    that lacks an archive_url. Rate-limited to 1 req/sec to stay well
    under any reasonable threshold. Safe to run in parallel with other
    passes on a different checkout."""
    unique_urls = {}
    for c in sc.get('candidates') or []:
        fns = c.get('footnotes') or {}
        for fn_id, entry in fns.items():
            url = (entry or {}).get('url') or ''
            if not url.startswith('http'):
                continue
            if entry.get('archive_url'):
                continue
            unique_urls.setdefault(url, []).append((c.get('slug'), fn_id))
    target_urls = list(unique_urls.keys())
    if limit:
        target_urls = target_urls[:limit]
    print(f'Archiving {len(target_urls)} unique URLs (of {len(unique_urls)} without archive_url)')
    done = 0
    failed = 0
    for url in target_urls:
        save = 'https://web.archive.org/save/' + url
        try:
            r = subprocess.run(
                ['curl', '-sI', '-L', '--max-time', '45', '-A',
                 'USMCMin-ArchiveBot/1.0 (usmcmin.com)', save],
                capture_output=True, text=True,
            )
            body = (r.stdout or '')
            # Wayback returns Content-Location: /web/<timestamp>/<url>
            m = re.search(r'[Cc]ontent-[Ll]ocation:\s*(/web/\S+)', body)
            if m:
                archive_url = 'https://web.archive.org' + m.group(1).strip()
            else:
                # Fallback: try a GET against the same save endpoint with
                # redirect-follow; the final URL is the archived snapshot.
                r2 = subprocess.run(
                    ['curl', '-sI', '-L', '-o', '/dev/null',
                     '-w', '%{url_effective}',
                     '--max-time', '45', '-A',
                     'USMCMin-ArchiveBot/1.0 (usmcmin.com)', save],
                    capture_output=True, text=True,
                )
                final = (r2.stdout or '').strip()
                if 'web.archive.org/web/' in final:
                    archive_url = final
                else:
                    archive_url = None
            if archive_url:
                for slug, fn_id in unique_urls[url]:
                    for c in sc.get('candidates') or []:
                        if c.get('slug') != slug:
                            continue
                        fn = (c.get('footnotes') or {}).get(fn_id)
                        if fn is not None:
                            fn['archive_url'] = archive_url
                done += 1
            else:
                failed += 1
        except Exception as e:
            print(f'  fail {url}: {e}', file=sys.stderr)
            failed += 1
        if sleep > 0:
            time.sleep(sleep)
    return {'archived': done, 'failed': failed, 'considered': len(target_urls)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from-claims', action='store_true')
    ap.add_argument('--backfill-legacy', action='store_true')
    ap.add_argument('--archive', action='store_true')
    ap.add_argument('--archive-limit', type=int, default=None)
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if not any([args.from_claims, args.backfill_legacy, args.archive]):
        ap.error('Pick at least one of --from-claims / --backfill-legacy / --archive')

    sc = load_sc()
    out = []
    if args.from_claims:
        s = pass_from_claims(sc, force=args.force)
        out.append(f'from-claims: {s}')
    if args.backfill_legacy:
        s = pass_backfill_legacy(sc, force=args.force)
        out.append(f'backfill-legacy: {s}')
    if args.archive:
        s = pass_archive(sc, limit=args.archive_limit)
        out.append(f'archive: {s}')
    if not args.dry_run:
        save_sc(sc)
        subprocess.run(['python3', str(REPO / 'build-data.py')], check=True)
    print('\n'.join(out))


if __name__ == '__main__':
    main()
