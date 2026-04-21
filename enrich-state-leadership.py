#!/usr/bin/env python3
"""
enrich-state-leadership.py — tag the current Senate President / Pro Tem
and House Speaker in each state, using Wikipedia as the verification
source.

Strategy:
  1. For each (state, chamber) pair, query Wikipedia's page for the
     leadership office (e.g., "Speaker of the California State Assembly").
  2. Extract the "Incumbent" field from the article's infobox.
  3. Match that name to a candidate in the scorecard by (state, slug).
  4. Tag the profile with a 'leadership_role' field and a notes appendix.

Only applies when BOTH the Wikipedia article loads AND the matched
candidate is found in scorecard. Everything else is skipped (conservative
— we'd rather miss than mis-label).
"""
import json
import re
import subprocess
import sys
import time
import unicodedata
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'

UA = 'USMCMin-Leadership/1.0 (usmcmin.com)'


STATE_NAME = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota',
    'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska',
    'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina',
    'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon',
    'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
    'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
    'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',
}

# Per-state chamber names (some states use "Assembly" instead of "House",
# "General Assembly" for the whole legislature, etc.). The Wikipedia
# article titles follow predictable patterns.
HOUSE_ARTICLE = {
    'CA': 'Speaker of the California State Assembly',
    'NY': 'Speaker of the New York State Assembly',
    'NV': 'Speaker of the Nevada Assembly',
    'NJ': 'Speaker of the New Jersey General Assembly',
    'WI': 'Speaker of the Wisconsin State Assembly',
    'FL': 'Speaker of the Florida House of Representatives',
    'TX': 'Speaker of the Texas House of Representatives',
    'IL': 'Speaker of the Illinois House of Representatives',
    'OH': 'Speaker of the Ohio House of Representatives',
    'PA': 'Speaker of the Pennsylvania House of Representatives',
    'VA': 'Speaker of the Virginia House of Delegates',
    # Default template for everyone else
    # 'XX': f'Speaker of the {STATE_NAME[XX]} House of Representatives'
}

SENATE_ARTICLE = {
    'CA': 'President pro tempore of the California State Senate',
    'NY': 'Temporary President of the New York State Senate',
    'FL': 'President of the Florida Senate',
    'TX': 'Lieutenant Governor of Texas',  # TX: Lt Gov IS Senate Pres
    'PA': 'President pro tempore of the Pennsylvania State Senate',
    'IL': 'President of the Illinois Senate',
    'OH': 'President of the Ohio Senate',
    'VA': 'President of the Senate of Virginia',  # VA: Lt Gov IS Senate Pres
}


def wiki_extract(title):
    """Fetch the plain-text extract (intro paragraph) of a Wikipedia article."""
    params = urllib.parse.urlencode({
        'action': 'query', 'prop': 'extracts', 'exintro': 1, 'explaintext': 1,
        'titles': title, 'format': 'json', 'redirects': 1,
    })
    url = f'https://en.wikipedia.org/w/api.php?{params}'
    r = subprocess.run(
        ['curl', '-s', '-A', UA, url], capture_output=True, text=True, timeout=15,
    )
    if r.returncode != 0:
        return None
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        return None
    pages = data.get('query', {}).get('pages', {})
    for pid, p in pages.items():
        if pid == '-1':
            return None
        return p.get('extract', '') or None
    return None


def wiki_infobox_raw(title):
    """Fetch the raw wikitext of the infobox to parse 'incumbent' field."""
    params = urllib.parse.urlencode({
        'action': 'parse', 'page': title, 'prop': 'wikitext',
        'format': 'json', 'redirects': 1,
    })
    url = f'https://en.wikipedia.org/w/api.php?{params}'
    r = subprocess.run(
        ['curl', '-s', '-A', UA, url], capture_output=True, text=True, timeout=15,
    )
    if r.returncode != 0:
        return None
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        return None
    return (data.get('parse') or {}).get('wikitext', {}).get('*')


def extract_incumbent_from_wikitext(wikitext):
    """From MediaWiki-format infobox, pull the current 'incumbent' name.

    The wikitext value can look like:
      | incumbent = [[Robert Rivas]]
      | incumbent = [[Robert Rivas|Rivas]]
      | incumbent = Ben Albritton
      | incumbent = [[Don Scott (politician)|Don Scott]]
    and may have a pipe mid-link before the line ends (the pipe is INSIDE
    a [[Name|display]], not the infobox field separator).
    """
    if not wikitext:
        return None
    # Match the whole line after 'incumbent =' — or 'officeholder', 'holder',
    # 'current_holder' (variant infobox field names). Greedy up to newline.
    m = None
    for field in ['incumbent', 'officeholder', 'current_holder', 'holder']:
        m = re.search(r'(?i)\n\s*\|\s*' + field + r'\s*=\s*([^\n]+)', wikitext)
        if m:
            break
    if not m:
        return None
    val = m.group(1).strip()
    # Strip wiki markup: [[Name|display]] -> display, [[Name]] -> Name
    val = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', lambda m: m.group(2) or m.group(1), val)
    # Strip HTML tags
    val = re.sub(r'<[^>]+>', '', val)
    # Strip wiki template invocations like {{nowrap|...}}
    val = re.sub(r'\{\{[^}]+\}\}', '', val)
    # Strip any trailing parentheses info
    val = re.sub(r'\s*\([^)]+\)\s*$', '', val)
    # If multiple "| field = value" on one line (rare), cut at the first
    # field separator that isn't inside a link.
    val = val.split('|')[0]
    val = val.strip()
    return val or None


def slugify(name):
    """Match the scorecard's slug convention."""
    s = unicodedata.normalize('NFKD', name)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return (s.lower().replace(' ', '-').replace('.', '').replace("'", '')
             .replace(',', '').replace('"', '').replace('—', '-'))


def house_article_for(state):
    return HOUSE_ARTICLE.get(state,
                              f'Speaker of the {STATE_NAME[state]} House of Representatives')


def senate_article_for(state):
    return SENATE_ARTICLE.get(state,
                               f'President of the {STATE_NAME[state]} Senate')


def apply_leadership(candidate, role_label, source_url):
    profile = candidate.setdefault('profile', {})
    changed = False
    if profile.get('leadership_role') != role_label:
        profile['leadership_role'] = role_label
        changed = True
    # Ensure source is in sources
    srcs = candidate.get('sources') or []
    if source_url and source_url not in srcs:
        srcs.append(source_url)
        candidate['sources'] = srcs
        changed = True
    # Append a notes blurb if not already there
    note = f'{role_label} — verified via {source_url}.'
    existing = candidate.get('notes') or ''
    if role_label not in existing:
        candidate['notes'] = (existing + ' ' + note).strip() if existing else note
        changed = True
    return changed


def main():
    only = sys.argv[1:] if len(sys.argv) > 1 and sys.argv[1] != '--all' else list(STATE_NAME.keys())
    if '--all' in sys.argv:
        only = list(STATE_NAME.keys())

    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    # Build state -> slug -> candidate lookup (state-level only)
    by_state_slug = {}
    for c in data['candidates']:
        if c.get('level') == 'state':
            by_state_slug[(c.get('state'), c.get('slug'))] = c

    tagged = 0
    attempted = 0
    for state in only:
        if state not in STATE_NAME:
            continue
        for chamber, article_fn, role_fn in [
            ('house', house_article_for, lambda s: f'Speaker of the {STATE_NAME[s]} House'),
            ('senate', senate_article_for, lambda s: f'President of the {STATE_NAME[s]} Senate'),
        ]:
            title = article_fn(state)
            attempted += 1
            wikitext = wiki_infobox_raw(title)
            time.sleep(0.4)  # be polite
            name = extract_incumbent_from_wikitext(wikitext) if wikitext else None
            if not name:
                continue
            # Try to find the candidate in scorecard
            slug = slugify(name)
            c = by_state_slug.get((state, slug))
            if not c:
                # Sometimes the slug has suffix or different form — try contains
                for (st, sl), cand in by_state_slug.items():
                    if st == state and slug in sl:
                        c = cand
                        break
            if not c:
                print(f'  {state} {chamber}: "{name}" NOT in scorecard (slug={slug})')
                continue
            role_label = role_fn(state)
            if apply_leadership(c, role_label, f'https://en.wikipedia.org/wiki/{title.replace(" ", "_")}'):
                tagged += 1
                print(f'  ✓ {state} {chamber}: {name} tagged as {role_label}')

    print(f'\nAttempted: {attempted} chamber lookups. Tagged: {tagged} officials.')

    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)

    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()
