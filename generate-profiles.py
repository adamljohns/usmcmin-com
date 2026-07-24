#!/usr/bin/env python3
"""Generate individual candidate profile pages from scorecard.json"""
import json
import os
import re

import source_bias as sb
# v5.6 — tier-aware label/description helpers (per-tier rubric drill-down).
# Federal profiles show canonical labels; state/local profiles show tier-
# specific subtitles ("Sanctity of Life — Protect the Vulnerable" at local).
from tier_classify import tier_label, tier_description

# Resolve once at import — used to check for sibling .webp photos at
# generation time (so we only emit <picture> when a WebP actually exists).
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

POINTS_PER_TRUE = 2
MAX_PER_TOPIC = 10
MAX_TOTAL = 100  # v4.0 rubric: 10 categories × 10 pts = 100 (60 God First + 40 America First)
MAX_GOD_FIRST = 60
MAX_AMERICA_FIRST = 40

# RESOLUTE Local civic-tool links by jurisdiction. Local officials whose city
# has a live RESOLUTE Local page get a banner linking to it (live agendas +
# briefs + how-to-weigh-in). Add an entry per city as the tool expands.
# --- Civic-tool cross-data (resolute-local) ----------------------------
# Lazy-loaded once per generate-profiles.py run. Cross-references the
# RESOLUTE Local civic-tool data (~/.openclaw/workspace/resolute-local/
# data/fredericksburg.json) to enrich FXBG council member profiles with
# their actual recorded voting record (votes participated, dissents,
# specific motions they voted against the majority on). Added 2026-05-27
# for Adam's "make it really really helpful to people who desire to know
# what happens in their city" bidirectional-linkage ask.
import os as _os
_CIVIC_VOTING_CACHE = {}  # surname.lower() -> {participated, majority, dissents:[...]}
_CIVIC_VOTING_LOADED = False

def _load_civic_voting():
    """Read resolute-local data once + build a surname→voting-stats map.
    Silently returns empty if the cross-repo file doesn't exist (e.g.,
    when generate-profiles.py runs in isolation)."""
    global _CIVIC_VOTING_LOADED
    if _CIVIC_VOTING_LOADED:
        return _CIVIC_VOTING_CACHE
    _CIVIC_VOTING_LOADED = True
    path = _os.path.expanduser('~/.openclaw/workspace/resolute-local/data/fredericksburg.json')
    if not _os.path.exists(path):
        return _CIVIC_VOTING_CACHE
    try:
        import json as _j
        data = _j.load(open(path))
    except Exception:
        return _CIVIC_VOTING_CACHE
    for m in data.get('meetings', []):
        for r in m.get('resolutions_voted', []) or []:
            ayes_n = r.get('ayes_count', 0)
            nays_n = r.get('nays_count', 0)
            majority_is_ayes = ayes_n >= nays_n
            for who in (r.get('ayes') or []):
                s = _CIVIC_VOTING_CACHE.setdefault(who.lower(),
                    {'participated':0,'ayes':0,'nays':0,'abstain':0,'majority':0,'dissents':[]})
                s['participated'] += 1; s['ayes'] += 1
                if majority_is_ayes: s['majority'] += 1
                else: s['dissents'].append({'date': m.get('date'), 'tally': f'{ayes_n}-{nays_n}', 'title': (r.get('title') or '(motion)')[:100], 'side':'aye-in-minority'})
            for who in (r.get('nays') or []):
                s = _CIVIC_VOTING_CACHE.setdefault(who.lower(),
                    {'participated':0,'ayes':0,'nays':0,'abstain':0,'majority':0,'dissents':[]})
                s['participated'] += 1; s['nays'] += 1
                if not majority_is_ayes: s['majority'] += 1
                else: s['dissents'].append({'date': m.get('date'), 'tally': f'{ayes_n}-{nays_n}', 'title': (r.get('title') or '(motion)')[:100], 'side':'nay-in-minority'})
            for who in (r.get('abstain') or []):
                s = _CIVIC_VOTING_CACHE.setdefault(who.lower(),
                    {'participated':0,'ayes':0,'nays':0,'abstain':0,'majority':0,'dissents':[]})
                s['participated'] += 1; s['abstain'] += 1
    return _CIVIC_VOTING_CACHE


CIVIC_TOOL_MAP = {
    'City of Fredericksburg': 'https://adamljohns.github.io/resolute-local/city/fredericksburg.html',
}

def letter_grade(pct):
    """A 90+, B 80, C 70, D 60, F <60 — standard report-card scale.
    Takes a 0-100 percentage. Per Adam's 2026-05-18 directive, candidates
    are now graded on percentage-of-answered rather than absolute /100,
    so a candidate scored on 45/50 questions with all True gets 100% = A
    (their max is 90, score 90, percent 100) instead of 90% = A. The
    point is to NOT penalize candidates for our inability to find info."""
    if pct >= 90: return 'A'
    if pct >= 80: return 'B'
    if pct >= 70: return 'C'
    if pct >= 60: return 'D'
    return 'F'

def calc_cat_score(answers):
    """Score a category's answer array.
    Values:
      True  → +2 (counts toward score + max)
      False → 0  (counts toward max)
      None  → unanswered (counts toward neither)
      'N/A' → not applicable to this office tier (counts toward neither;
              visually distinct from None per Option B tier-masking)
    """
    if not answers:
        return {'score': 0, 'raw': 0, 'answered': 0, 'na': 0}
    raw = sum(1 for a in answers if a is True)
    answered = sum(1 for a in answers if a is True or a is False)
    na = sum(1 for a in answers if a == 'N/A')
    return {'score': raw * POINTS_PER_TRUE, 'raw': raw, 'answered': answered, 'na': na}

def calc_total(scores, categories, office_tier=None):
    """Sum True×2 + answered across categories.

    v5.0 — when office_tier is given ('federal'|'state'|'local'), only count
    categories that belong to that tier's rubric (those whose `pillars` map
    includes the tier). This excludes federal-only categories (Foreign Policy,
    Industry Capture) from state/local totals and includes the tier's
    Refuse-Overreach / Public Justice categories. office_tier=None counts all
    (back-compat)."""
    total = 0
    answered = 0
    for cat in categories:
        if office_tier is not None:
            pillars = cat.get('pillars')
            if pillars is not None and office_tier not in pillars:
                continue  # category not part of this tier's rubric
        cs = calc_cat_score(scores.get(cat['id'], []))
        total += cs['score']
        answered += cs['answered']
    return {'score': total, 'answered': answered}

def classify_office_tier(c):
    """v4.1+ — return 'federal' | 'state' | 'local' for a candidate based on office.
    Mirror of apply-tier-applicability.py's classifier (kept inline here to avoid
    package-imports). Updates to this function should also update the apply
    script's version."""
    office = c.get('office') or ''
    if not office:
        jur = (c.get('jurisdiction') or '').lower()
        if 'executive branch' in jur or 'judicial branch' in jur:
            return 'federal'
        return 'state'
    o = office.lower()
    if re.search(r'\bcity council\b|\btown council\b|\bborough council\b|'
                 r'\bschool board\b|\bboard of education\b', o):
        return 'local'
    if re.search(r'\b(president|vice president|u\.?s\.?\s+sen|u\.?s\.?\s+hous|u\.?s\.?\s+rep|'
                 r'united states sen|united states hous|united states rep|secretary of|'
                 r'acting attorney general|attorney general of the united states|'
                 r'director of|administrator of|ambassador|chief of staff|deputy chief of staff|'
                 r'homeland security advisor|chief justice|associate justice.+supreme court|'
                 r'special envoy)', o):
        if (re.search(r'^attorney general$|state attorney general|secretary of state|'
                      r'state treasurer|state auditor|state comptroller', o)
                and 'u.s.' not in o and 'united states' not in o):
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
    if re.search(r'\bmayor\b|\bpolice chief\b|\bchief of police\b|city council|city commission|town council|borough council|'
                 r'county (commissioner|supervisor|judge|board)|'
                 r'school board|board of education|'
                 r'district attorney|county attorney|state\'?s attorney|circuit attorney|'
                 r'sheriff|city clerk|city attorney|'
                 r'commonwealth\'?s attorney', o):
        return 'local'
    return 'state'


def question_text_for_tier(cat, q_idx, tier):
    """v4.2/4.3 — return the tier-appropriate question text for display.
    Falls back to the default federal text (questions[q_idx]) if no tier
    variant is set. Per Adam's 2026-05-19 directive: "similar in scope
    but different in implementation"."""
    if tier == 'state':
        qs = cat.get('questions_state') or []
        if q_idx < len(qs) and qs[q_idx]:
            return qs[q_idx]
    elif tier == 'local':
        qs = cat.get('questions_local') or []
        if q_idx < len(qs) and qs[q_idx]:
            return qs[q_idx]
    return cat.get('questions', [''])[q_idx] if q_idx < len(cat.get('questions', [])) else ''


def calc_subtotals(scores, categories, office_tier='federal'):
    """v5.0 — split total into Pillar A (God First) + Pillar B (America First /
    State First / Local First) using each category's `pillars[office_tier]`.

    God First always = Pillar A. Pillar B is whatever the tier's second pillar
    is named (america_first federal, state_first state, local_first local).
    Categories not in the tier's rubric are skipped. Falls back to the legacy
    `tier` field for federal records that predate the `pillars` map.

    Returns {'god_first': a, 'gov_first': b} — `gov_first` is the Pillar-B
    subtotal regardless of its tier-specific name."""
    a = 0  # God First (Pillar A)
    b = 0  # Pillar B (america/state/local first)
    for cat in categories:
        pillars = cat.get('pillars') or {}
        pill = pillars.get(office_tier)
        if pill is None:
            if office_tier == 'federal':
                pill = cat.get('tier')  # legacy fallback
            else:
                continue  # category not part of this tier's rubric
        cs = calc_cat_score(scores.get(cat['id'], []))
        if pill == 'god_first':
            a += cs['score']
        else:
            b += cs['score']
    return {'god_first': a, 'gov_first': b}


def tier_pillar_info(meta, office_tier):
    """v5.0 — return (pillar_b_label, god_max, gov_max) for a candidate's tier
    from meta.rubrics. Maxes = (#categories in pillar) × 10. Defaults to the
    federal 60/40 shape if the tier or rubrics block is missing."""
    rubrics = (meta or {}).get('rubrics') or {}
    r = rubrics.get(office_tier) or rubrics.get('federal') or {}
    b_label = r.get('pillar_b_label', 'America First')
    god_max = (len(r.get('pillar_a', [])) or 6) * 10
    gov_max = (len(r.get('pillar_b', [])) or 4) * 10
    return b_label, god_max, gov_max

def score_color(score, max_val):
    if max_val == 0:
        return '#666'
    pct = score / max_val
    if pct >= 0.8:
        return '#4CAF50'
    if pct >= 0.5:
        return '#FFC107'
    if pct > 0:
        return '#f44336'
    return '#666'

def party_label(party):
    if party == 'R':
        return 'Republican'
    if party == 'D':
        return 'Democrat'
    if party == 'I':
        return 'Independent'
    return 'Nonpartisan'

def party_class(party):
    if party == 'R':
        return 'party-r'
    if party == 'D':
        return 'party-d'
    if party == 'I':
        return 'party-i'
    return 'party-unknown'

def answer_display(val):
    if val is True:
        return '<span style="color:#4CAF50;font-weight:700;">TRUE (+2)</span>'
    if val is False:
        return '<span style="color:#f44336;font-weight:700;">FALSE (0)</span>'
    if val == 'N/A':
        return '<span style="color:#888;font-style:italic;text-decoration:line-through;" title="This question is not scoreable at this office tier — official has no direct authority to act on this issue.">N/A &middot; out of tier</span>'
    return '<span style="color:#666;font-style:italic;">Not yet verified</span>'

# ---- Navigation & photo helpers (added for prev/next + initials fallback) ----

STATE_NAMES_FULL = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
    'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
    'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
    'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
    'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
    'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'District of Columbia', 'US': 'National',
    'PR': 'Puerto Rico',
}

LEVEL_RANK = {'executive': 1, 'judicial': 2, 'federal': 3, 'state': 4, 'local': 5}

def level_rank(level):
    return LEVEL_RANK.get(level or 'state', 6)

def initials(name):
    """Two-letter initials from a name. 'Abigail Spanberger' -> 'AS'."""
    if not name:
        return '??'
    parts = [p for p in name.strip().split() if p and not p.endswith('.')]
    if not parts:
        return name.strip()[:2].upper()
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()

# Dignified palette — derived from a stable hash of the slug so the same person
# always gets the same swatch. No silhouettes, no guessing — initials on a
# named-color block reads as intentional.
INITIALS_PALETTE = [
    ('#1e3a5f', '#93c5fd'),  # navy / light blue
    ('#14532d', '#86efac'),  # forest / mint
    ('#7c2d12', '#fdba74'),  # burnt / tan
    ('#3b0764', '#c4b5fd'),  # plum / lavender
    ('#713f12', '#fde68a'),  # bronze / straw
    ('#064e3b', '#6ee7b7'),  # pine / seafoam
    ('#581c87', '#d8b4fe'),  # royal purple / orchid
    ('#1f2937', '#cbd5e1'),  # slate / silver
    ('#4c1d95', '#a78bfa'),  # indigo / periwinkle
    ('#854d0e', '#fcd34d'),  # umber / gold
]

def color_for_slug(slug):
    """Stable color pair (bg, fg) for an initials badge."""
    if not slug:
        return INITIALS_PALETTE[0]
    h = 0
    for ch in slug:
        h = (h * 31 + ord(ch)) & 0xFFFFFFFF
    return INITIALS_PALETTE[h % len(INITIALS_PALETTE)]

def build_election_html(candidate, elections_data):
    """Render election-timing block for a candidate's profile.

    Reads candidate.profile.next_election_date (populated by enrich-elections.py)
    and elections_data (loaded once from data/elections.json) to produce a
    'Next Election' banner with a live countdown + registration deadline +
    elections-admin contact for the candidate's state.

    Returns '' if there's nothing useful to show.
    """
    profile = candidate.get('profile') or {}
    next_date = profile.get('next_election_date')
    next_type = profile.get('next_election_type') or 'general'
    seat_up = profile.get('seat_up_next')
    state = (candidate.get('state') or '').upper()

    if not next_date:
        return ''

    # Pull state-level admin info if available
    state_info = (elections_data or {}).get(state) or {}
    admin = state_info.get('elections_admin') or {}
    reg_deadline = state_info.get('registration_deadline_2026')
    early_voting = state_info.get('early_voting_window_2026') or {}

    banner_class = 'seat-up' if seat_up else 'seat-safe'
    header = ('Seat up at next election' if seat_up
              else 'Not up at next scheduled election')
    # Human date (e.g., "November 3, 2026")
    from datetime import date as _date
    try:
        y, m, d = [int(x) for x in next_date.split('-')]
        dt = _date(y, m, d)
        months = ['January','February','March','April','May','June',
                  'July','August','September','October','November','December']
        pretty_date = f'{months[m-1]} {d}, {y}'
    except Exception:
        pretty_date = next_date
        dt = None

    # Days until (computed live in JS so it's always current on page load)
    countdown_script = (
        f'<script>(function(){{var t=new Date("{next_date}T12:00:00Z")-new Date();'
        f'var d=Math.max(0,Math.ceil(t/86400000));'
        f'var el=document.getElementById("countdown-{candidate.get("id")}");'
        f'if(el) el.textContent=d+" day"+(d===1?"":"s");}})();</script>'
    )

    html = f'<div id="prof-election" class="prof-election prof-election-{banner_class}">'
    html += '<div class="prof-election-main">'
    html += f'<div class="prof-election-label">Next Election</div>'
    html += f'<div class="prof-election-date">{pretty_date}</div>'
    html += f'<div class="prof-election-type">{next_type.title()} &middot; {header}</div>'
    html += f'<div class="prof-election-countdown"><span id="countdown-{candidate.get("id")}">—</span> <span class="cd-label">until</span></div>'
    html += '</div>'

    # State election admin info (not per-candidate — shared across the state)
    admin_parts = []
    if reg_deadline:
        admin_parts.append(f'<div class="prof-election-side-item"><strong>Registration deadline:</strong> {reg_deadline}</div>')
    if early_voting.get('start') and early_voting.get('end'):
        ev_note = early_voting.get('note', '')
        ev_note_html = f' <span style="opacity:0.7;">({ev_note})</span>' if ev_note else ''
        admin_parts.append(f'<div class="prof-election-side-item"><strong>Early voting:</strong> {early_voting["start"]} &ndash; {early_voting["end"]}{ev_note_html}</div>')
    if admin.get('phone'):
        tel = 'tel:' + admin["phone"]
        admin_parts.append(f'<div class="prof-election-side-item"><strong>Elections office:</strong> <a href="{tel}">{admin["phone"]}</a></div>')
    if admin.get('voter_info_lookup'):
        admin_parts.append(f'<div class="prof-election-side-item"><strong>Voter status:</strong> <a href="{admin["voter_info_lookup"]}" target="_blank" rel="noopener">Check registration</a></div>')
    if admin.get('website'):
        admin_parts.append(f'<div class="prof-election-side-item"><strong>State elections site:</strong> <a href="{admin["website"]}" target="_blank" rel="noopener">{admin.get("name","Official")}</a></div>')

    if admin_parts:
        html += '<div class="prof-election-side">' + ''.join(admin_parts) + '</div>'

    html += '</div>'
    html += countdown_script
    return html


def build_contact_html(candidate):
    """Render the 'Contact This Official' block.

    Pulls from candidate.profile.phone / .email / .contact_form when set, then
    falls back to sensible defaults:
      - Federal officials: US Capitol switchboard (202-224-3121 Senate, 202-225-3121
        House) with 'ask for Senator/Representative Name' note.
      - All officials: a 'Send Message' link pointing at the first .gov source,
        the candidate website, or the first source URL if nothing better.
      - Twitter handle from profile.twitter if set.
    """
    import re
    level = (candidate.get('level') or '').lower()
    jurisdiction = candidate.get('jurisdiction') or ''
    profile = candidate.get('profile') or {}
    phone = profile.get('phone')
    email = profile.get('email')
    contact_form = profile.get('contact_form')
    website = candidate.get('website') or ''
    sources = candidate.get('sources') or []
    twitter = profile.get('twitter') or ''
    facebook = profile.get('facebook') or ''
    youtube = profile.get('youtube') or ''
    district_offices = profile.get('district_offices') or []

    # Pick best "send a message" URL
    if not contact_form:
        # Prefer an official .gov source
        for s in sources:
            if '.gov' in s and 'ballotpedia' not in s.lower():
                contact_form = s
                break
        if not contact_form and website:
            contact_form = website
        if not contact_form and sources:
            contact_form = sources[0]

    # Federal fallback phone (Capitol switchboard)
    phone_note = ''
    display_phone = phone
    if not display_phone and level == 'federal':
        if 'Senate' in jurisdiction:
            display_phone = '(202) 224-3121'
            phone_note = f'U.S. Capitol switchboard — ask for Senator {candidate["name"]}.'
        elif 'House' in jurisdiction:
            display_phone = '(202) 225-3121'
            phone_note = f'U.S. Capitol switchboard — ask for Representative {candidate["name"]}.'

    # If we have nothing to show, render nothing (keeps profiles lean)
    if not (display_phone or contact_form or email or twitter or facebook
            or youtube or district_offices):
        return ''

    parts = []
    if display_phone:
        tel = 'tel:+1' + re.sub(r'\D', '', display_phone)
        parts.append(
            f'<a class="prof-contact-btn" href="{tel}">'
            f'<span class="prof-contact-icon" aria-hidden="true">&#128222;</span>'
            f'<span class="prof-contact-text">'
            f'<span class="prof-contact-label">Call</span>'
            f'<span class="prof-contact-value">{display_phone}</span>'
            f'</span></a>'
        )
    if contact_form:
        # Truncate long URL to a readable label
        label = 'Send Message'
        parts.append(
            f'<a class="prof-contact-btn" href="{contact_form}" target="_blank" rel="noopener">'
            f'<span class="prof-contact-icon" aria-hidden="true">&#9993;&#65039;</span>'
            f'<span class="prof-contact-text">'
            f'<span class="prof-contact-label">{label}</span>'
            f'<span class="prof-contact-value">Official Page</span>'
            f'</span></a>'
        )
    if email:
        parts.append(
            f'<a class="prof-contact-btn" href="mailto:{email}">'
            f'<span class="prof-contact-icon" aria-hidden="true">&#128231;</span>'
            f'<span class="prof-contact-text">'
            f'<span class="prof-contact-label">Email</span>'
            f'<span class="prof-contact-value">{email}</span>'
            f'</span></a>'
        )
    if twitter:
        handle = twitter.lstrip('@')
        parts.append(
            f'<a class="prof-contact-btn" href="https://x.com/{handle}" target="_blank" rel="noopener">'
            f'<span class="prof-contact-icon" aria-hidden="true">&#119987;</span>'
            f'<span class="prof-contact-text">'
            f'<span class="prof-contact-label">X / Twitter</span>'
            f'<span class="prof-contact-value">@{handle}</span>'
            f'</span></a>'
        )
    if facebook:
        parts.append(
            f'<a class="prof-contact-btn" href="https://facebook.com/{facebook}" target="_blank" rel="noopener">'
            f'<span class="prof-contact-icon" aria-hidden="true">&#128101;</span>'
            f'<span class="prof-contact-text">'
            f'<span class="prof-contact-label">Facebook</span>'
            f'<span class="prof-contact-value">/{facebook}</span>'
            f'</span></a>'
        )
    if youtube:
        parts.append(
            f'<a class="prof-contact-btn" href="https://www.youtube.com/channel/{youtube}" target="_blank" rel="noopener">'
            f'<span class="prof-contact-icon" aria-hidden="true">&#127909;</span>'
            f'<span class="prof-contact-text">'
            f'<span class="prof-contact-label">YouTube</span>'
            f'<span class="prof-contact-value">Channel</span>'
            f'</span></a>'
        )

    # ---- District offices section (for federal officials) ----
    district_html = ''
    if district_offices:
        office_items = []
        for o in district_offices[:6]:  # cap at 6 to keep profile readable
            city = o.get('city', '')
            state_ab = o.get('state', '')
            phone_raw = o.get('phone', '')
            zip_code = o.get('zip', '')
            addr = o.get('address', '')
            parts_line = []
            if city or state_ab:
                parts_line.append(f'<strong>{city}{", " + state_ab if state_ab else ""}</strong>')
            if phone_raw:
                tel = 'tel:+1' + re.sub(r'\D', '', phone_raw)
                parts_line.append(f'<a href="{tel}">{phone_raw}</a>')
            if addr:
                suffix = f' {zip_code}' if zip_code else ''
                parts_line.append(f'{addr}{suffix}')
            if parts_line:
                office_items.append(
                    '<div class="prof-district-office">' + ' &middot; '.join(parts_line) + '</div>'
                )
        if office_items:
            plural = 's' if len(office_items) > 1 else ''
            district_html = (
                '<details class="prof-district-details">'
                f'<summary>&#128205; Local district office{plural} '
                f'({len(office_items)})</summary>'
                '<div class="prof-district-list">'
                + ''.join(office_items)
                + '</div></details>'
            )

    html = '<div id="prof-contact" class="prof-contact">'
    html += '<h2>Contact This Official</h2>'
    html += '<div class="prof-contact-grid">' + ''.join(parts) + '</div>'
    if phone_note:
        html += f'<p class="prof-contact-note">&#128161; {phone_note}</p>'
    if district_html:
        html += district_html
    html += ('<p class="prof-contact-tagline">Reach out directly. Your voice matters. '
             '<em>Proverbs 29:2 — When the righteous are in authority, the people rejoice.</em></p>')
    html += '</div>'
    return html


def compute_nav_groups(candidates, categories):
    """
    Group candidates by (state, level, jurisdiction). Within each group sort by
    score descending, then alphabetically by name. Return a dict keyed by
    candidate id → {prev, next, position, group_size, group_label}.

    prev/next are (slug, name, state) tuples or None at group edges.
    """
    # Score lookup (once per candidate) so we don't recompute during sort.
    scored = []
    for c in candidates:
        t = calc_total(c.get('scores', {}), categories, classify_office_tier(c) or 'federal')
        scored.append((c, t['score']))

    # Group key = (state, level_rank, jurisdiction)
    groups = {}
    for c, score in scored:
        key = (
            (c.get('state') or 'XX').upper(),
            level_rank(c.get('level')),
            c.get('jurisdiction') or '',
        )
        groups.setdefault(key, []).append((c, score))

    # Sort each group: score desc, then name asc (tiebreak)
    nav = {}
    for key, members in groups.items():
        members.sort(key=lambda x: (-x[1], (x[0].get('name') or '').lower()))
        group_label = key[2] or 'Unsorted'
        size = len(members)
        for i, (c, _score) in enumerate(members):
            prev_c = members[i - 1][0] if i > 0 else None
            next_c = members[i + 1][0] if i < size - 1 else None
            nav[c.get('id')] = {
                'position': i + 1,
                'group_size': size,
                'group_label': group_label,
                'prev': prev_c,
                'next': next_c,
            }
    return nav

def generate_profile(candidate, categories, meta, nav=None):
    c = candidate
    profile = c.get('profile', {}) or {}

    # v4.2/v4.3 — classify candidate's office tier once. Used by question_text_for_tier
    # to pick the right question wording (federal vs state vs local). Falls back to
    # 'federal' for ambiguous/unknown to avoid omitting questions.
    # v5.0 — also drives tier-specific rubric: which categories count + pillar split.
    candidate_tier = classify_office_tier(c) or 'federal'
    total = calc_total(c['scores'], categories, candidate_tier)

    # Foreign-influence + dark-money adjustments. Sums delta across every
    # keyed source under profile.score_adjustments (aipac, soros, etc.)
    # and applies it to the base 70-point category-sum total. Schedule
    # is documented in scorecard.json.meta.aipac_adjustment etc.
    SOURCE_LABELS_ADJ = {
        'aipac': 'AIPAC / pro-Israel-lobby contributions',
        'soros': 'Open Society / Soros donor network',
        'china': 'CCP-linked / United Front-affiliated donors',
        'foreign': 'Other foreign-linked PACs',
    }
    SOURCE_DESCRIPTORS_ADJ = {
        'aipac': 'AIPAC operates a super-PAC (United Democracy Project) that spent over $100M during the 2024 cycle on independent expenditures targeting U.S. candidates who criticize Israeli government policy. The U.S. has no formal mutual-defense treaty with Israel. RESOLUTE Citizen treats documented AIPAC contributions as a failure on foreign_policy_restraint/q4 (the foreign-lobby question) AND applies a dollar-bracket adjustment to the total score.',
        'soros': 'The Open Society Foundations and the Democracy PAC vehicles tied to George Soros / Alex Soros are direct funding rails for the WEF / ESG / Davos capture agenda — Soros is a founding World Economic Forum attendee and OSF is one of its largest civil-society partners. RESOLUTE Citizen treats documented Soros-network contributions as a failure on economic_stewardship/q5, the question that asks whether the candidate opposes WEF/ESG/Davos economic capture and supports anti-trust action against monopolistic financial cartels — accepting money from the architect of that capture is a revealed preference against it. The same Soros DA network is documented to decline prosecution of attacks on pro-life pregnancy centers and refuse to enforce state abortion restrictions; that pattern is tracked separately under sanctity_of_life claims. A dollar-bracket adjustment is also applied to the total score.',
        'china': 'The CCP operates an explicit United Front Work Department to direct overseas members and proxies — including business executives such as Wanxiang Group\'s Pin Ni (named CCP member 15 times in Chinese state media) — to cultivate political relationships in the United States. Federal law (52 U.S.C. § 30121) prohibits foreign nationals including CCP members from donating to U.S. campaigns. RESOLUTE Citizen treats documented contributions from CCP-member or United Front-affiliated donors as a failure on foreign_policy_restraint/q4 (the foreign-lobby question) AND applies a dollar-bracket adjustment to the total score.',
        'foreign': 'Generic foreign-linked PAC contributions outside the AIPAC + Soros + China networks.',
    }

    def render_adjustments_block(lines, base, adjusted):
        if not lines:
            return ''
        rows = []
        for key, delta, dollars, bracket, note, sources in lines:
            label = SOURCE_LABELS_ADJ.get(key, key.upper())
            descr = SOURCE_DESCRIPTORS_ADJ.get(key, '')
            sign = '+' if delta > 0 else ''
            adj_class = 'prof-adj-plus' if delta > 0 else 'prof-adj-minus'
            dollar_str = ('$0 (verified zero)' if (dollars is None or dollars == 0)
                          else f'${int(dollars):,} documented')
            src_html = ''
            if sources:
                src_links = ' · '.join(
                    f'<a href="{u}" target="_blank" rel="noopener">{u.replace("https://","").replace("http://","")[:60]}</a>'
                    for u in sources[:3])
                src_html = f'<div class="prof-adj-sources">Sources: {src_links}</div>'
            rows.append(
                f'<li class="prof-adj-row {adj_class}">'
                f'<div class="prof-adj-row-head">'
                f'<span class="prof-adj-key">{label}</span>'
                f'<span class="prof-adj-delta">{sign}{delta}</span>'
                f'</div>'
                f'<div class="prof-adj-meta">{dollar_str}'
                + (f' · bracket <code>{bracket}</code>' if bracket else '')
                + '</div>'
                + (f'<div class="prof-adj-note">{note}</div>' if note else '')
                + (f'<div class="prof-adj-descriptor">{descr}</div>' if descr else '')
                + src_html
                + '</li>'
            )
        return (
            '<div id="prof-adjustments" class="prof-adjustments" role="note" aria-label="Score adjustments">'
            '<h3>Score adjustments</h3>'
            '<div class="prof-adj-explainer">'
            '<p class="prof-adj-lead"><strong>Foreign-lobby money compromises America First.</strong> '
            'The U.S. has no formal mutual-defense treaty with Israel; AIPAC operates a super-PAC '
            '(United Democracy Project) that spent over $100M during the 2024 cycle on independent '
            'expenditures against U.S. candidates who criticize Israeli government policy. A candidate '
            'who has accepted that money has, in their own revealed preference, accepted a foreign-policy '
            'filter on their congressional vote. The same logic covers China-linked donations, where '
            'federal law also prohibits CCP members from contributing.</p>'
            '<p class="prof-adj-lead">For every candidate with a documented donor record, two things '
            'happen: <strong>(1) the specific category question is marked False</strong> '
            '(<code>foreign_policy_restraint[q4]</code> for AIPAC + China; <code>economic_stewardship[q5]</code> — the '
            'WEF/ESG/Davos capture question — for Soros-network donors), so the per-category subscore drops by 2 points; <strong>(2) an additional '
            'dollar-bracket adjustment is applied to the total</strong>, making the penalty proportional '
            'to the magnitude of the funding. Both impacts are visible on this page.</p>'
            '<p class="prof-adj-lead"><a href="/methodology-foreign-influence.html">Full methodology, '
            'bracket schedules, and primary sources &rarr;</a></p>'
            '</div>'
            f'<div class="prof-adj-summary">Base score <strong>{base}/{MAX_TOTAL}</strong> '
            f'<span class="prof-adj-arrow">→</span> '
            f'Adjusted <strong>{adjusted}/{MAX_TOTAL}</strong></div>'
            '<ul class="prof-adj-list">' + ''.join(rows) + '</ul>'
            '</div>'
        )

    # ─── Sticky TOC + Share helpers (v4.0 navigation upgrade) ────────────
    # Right-rail TOC that highlights the current section as the visitor
    # scrolls; collapses to a hamburger trigger on mobile. Section anchors
    # are added to .prof-total (#prof-score), .prof-church, .prof-adjustments,
    # .prof-contact, .prof-election, h2#prof-categories, .prof-sources,
    # .prof-feedback (already had id="feedback" — kept).
    def render_profile_toc(cand):
        # Build only entries that will actually exist on the page. Score
        # always exists; everything else is conditional.
        items = [('prof-score', 'Score')]
        if (cand.get('church_affiliation') or {}).get('name'):
            items.append(('prof-church', 'Church'))
        if (cand.get('profile') or {}).get('score_adjustments'):
            items.append(('prof-adjustments', 'Adjustments'))
        items.append(('prof-contact', 'Contact'))
        items.append(('prof-election', 'Election'))
        items.append(('prof-categories', 'Categories'))
        # Sources block is rendered only when there are sources; assume it
        # exists for most candidates — the TOC link gracefully no-ops if not.
        items.append(('prof-sources', 'Sources'))
        items.append(('feedback', 'Feedback'))

        links = ''
        for anchor, label in items:
            links += f'<a class="prof-toc-link" href="#{anchor}" data-target="{anchor}">{label}</a>'
        return (
            '<aside class="prof-toc" aria-label="On-page navigation" role="navigation">'
            '<div class="prof-toc-head">On this page</div>'
            f'<nav class="prof-toc-nav">{links}</nav>'
            '</aside>'
        )

    def render_share_button(cand):
        """Pre-filled X/email/SMS/copy-link share dropdown.
        URL is built client-side from window.location so it works on local
        + production. Pre-filled text mentions name + letter grade so the
        share recipient knows what they're getting."""
        nm = cand.get('name', '').replace('"', '&quot;').replace("'", '&#39;')
        return (
            '<details class="prof-share">'
            '<summary class="prof-share-trigger" title="Share this profile">'
            '<span aria-hidden="true">&#x21AA;</span>'
            ' Share'
            '</summary>'
            '<div class="prof-share-menu" role="menu">'
            f'<button class="prof-share-opt" type="button" data-share="x" data-name="{nm}">X / Twitter</button>'
            f'<button class="prof-share-opt" type="button" data-share="email" data-name="{nm}">Email</button>'
            f'<button class="prof-share-opt" type="button" data-share="sms" data-name="{nm}">SMS</button>'
            f'<button class="prof-share-opt" type="button" data-share="copy" data-name="{nm}">Copy Link</button>'
            '</div>'
            '</details>'
        )

    # ─── National-rank callout ─────────────────────────────────────────────
    # Computed in main() — meta['_rank_map'][slug] → (rank, total_ranked).
    # Only renders for candidates with at least one scored answer (others
    # don't appear in the rank table). Visitors get a one-glance idea of
    # "where does this candidate fall among other scored candidates?" with
    # a one-click jump to the live rankings page.
    def render_rank_callout(cand, meta_):
        rank_map = (meta_ or {}).get('_rank_map') or {}
        rank_entry = rank_map.get(cand.get('slug'))
        if not rank_entry:
            return ''
        rank, total = rank_entry
        pct = (rank / total) * 100 if total else 0
        pct_label = f'top {pct:.1f}%' if pct < 50 else f'bottom {(100-pct):.1f}%'
        return (
            '<div class="prof-rank-callout" role="note" aria-label="National rank">'
            '<div class="prof-rank-head">'
            '<span class="prof-rank-icon" aria-hidden="true">&#9733;</span>'
            '<span class="prof-rank-label">National Rank</span>'
            '</div>'
            f'<div class="prof-rank-body">'
            f'<span class="prof-rank-position"><strong>#{rank:,}</strong> of {total:,}</span>'
            f' &middot; <span class="prof-rank-pct">{pct_label}</span>'
            f' <span class="prof-rank-context">among candidates with at least one scored answer</span>'
            '</div>'
            '<a href="../../citizen-rankings.html" class="prof-rank-link">See the full rankings &rarr;</a>'
            '</div>'
        )

    # ─── Church affiliation block (cross-pollination with usmcmin.org) ─────
    # Renders directly under the score block if c['church_affiliation'] is
    # set. Source-of-truth is the parallel agent's notable_attendees on
    # /docs/data/churches.json over at usmcmin.org; backfilled via
    # enrich-church-affiliation-from-org.py.
    def render_church_affiliation_block(cand):
        ca = cand.get('church_affiliation') or {}
        if not (ca.get('name') or ca.get('denomination')):
            return ''
        name = ca.get('name') or 'Christian'
        denom = ca.get('denomination') or ''
        loc = ca.get('location') or ''
        slug = ca.get('slug') or ''
        # Link to .org directory-politicians.html (the cross-ref aggregator)
        org_link = f'https://usmcmin.org/churches/{slug}.html' if slug else 'https://usmcmin.org/directory-politicians.html'
        evidence = ca.get('evidence_url') or org_link
        evidence_date = ca.get('evidence_date') or ''
        association = ca.get('association') or ''
        period = ca.get('period') or ''
        verified = ca.get('verified')
        verify_chip = (
            '<span class="prof-church-verified" title="Verified by .org agent on '
            f'{evidence_date}">verified</span>' if verified
            else '<span class="prof-church-unverified" title="Pending verification">unverified</span>'
        )
        meta_bits = []
        if denom: meta_bits.append(f'<span class="prof-church-denom">{denom}</span>')
        if loc:   meta_bits.append(f'<span class="prof-church-loc">{loc}</span>')
        if association:
            assoc_label = association.replace('_', ' ').title()
            meta_bits.append(f'<span class="prof-church-assoc">{assoc_label}</span>')
        if period: meta_bits.append(f'<span class="prof-church-period">{period}</span>')
        meta_html = ' &middot; '.join(meta_bits)
        return (
            '<div id="prof-church" class="prof-church" role="note" aria-label="Church affiliation">'
            '<div class="prof-church-head">'
            '<span class="prof-church-icon" aria-hidden="true">&#9962;</span>'
            '<span class="prof-church-label">Church Affiliation</span>'
            f'{verify_chip}'
            '</div>'
            f'<div class="prof-church-name"><a href="{org_link}" target="_blank" rel="noopener">{name}</a></div>'
            + (f'<div class="prof-church-meta">{meta_html}</div>' if meta_html else '')
            + f'<div class="prof-church-source">Evidence: <a href="{evidence}" target="_blank" rel="noopener">{evidence[:65]}{("…" if len(evidence) > 65 else "")}</a></div>'
            + '<div class="prof-church-cross">Cross-referenced from the <a href="https://usmcmin.org/directory-politicians.html" target="_blank" rel="noopener">USMC Ministries church directory</a> &mdash; see the <a href="https://usmcmin.org/churches.html" target="_blank" rel="noopener">Nationwide Church Directory</a> for the full 10-point theological scorecard on this church.</div>'
            '</div>'
        )

    adjustments = (profile.get('score_adjustments') or {})
    adj_total = 0
    adj_lines = []  # list of (key, delta, dollars, bracket, note, sources)
    for key, info in adjustments.items():
        d = int(info.get('delta') or 0)
        adj_total += d
        adj_lines.append((
            key,
            d,
            info.get('dollars'),
            info.get('bracket'),
            info.get('note', ''),
            list(info.get('sources') or []),
        ))
    adjusted_score = total['score'] + adj_total
    total['adjusted_score'] = adjusted_score
    total['adjustment'] = adj_total

    total_color = score_color(adjusted_score, MAX_TOTAL)
    bar_width = round((max(0, min(MAX_TOTAL, adjusted_score)) / MAX_TOTAL) * 100) if MAX_TOTAL > 0 else 0

    # v4.0 — God First + America First subtotals + letter grade.
    # Adjustments (AIPAC/Soros/etc.) are reflected in the headline number
    # but NOT in the subtotal pills — those show pure category answers so
    # a visitor can see at a glance how the candidate scored on Christian
    # principle vs. American sovereignty before foreign-money penalties.
    subtotals = calc_subtotals(c['scores'], categories, candidate_tier)
    gf_score = subtotals['god_first']
    af_score = subtotals['gov_first']
    # v5.0 — pillar-B label + maxes vary by tier (federal 60/40 America First;
    # state/local 70/30 State|Local First).
    pillar_b_label, max_god, max_gov = tier_pillar_info(meta, candidate_tier)
    gf_color = score_color(gf_score, max_god)
    af_color = score_color(af_score, max_gov)
    # v5.0 — tier-specific Pillar-B emoji + hover title
    _PILLAR_B_META = {
        'federal': ('\U0001F1FA\U0001F1F8',
                    'America First — border &amp; immigration, self-defense &amp; 2A, '
                    'foreign-policy restraint, industry capture &amp; sovereignty'),
        'state':   ('\U0001F3DB️',
                    'State First — refuse federal overreach (10A sovereignty), '
                    'border enforcement, self-defense &amp; 2A'),
        'local':   ('\U0001F3DB️',
                    'Local First — refuse state overreach (subsidiarity), '
                    'public safety &amp; cooperation, self-defense &amp; 2A'),
    }
    pillar_b_emoji, pillar_b_title = _PILLAR_B_META.get(candidate_tier, _PILLAR_B_META['federal'])
    god_title = ('God First — sanctity of life, biblical marriage, family sovereignty, '
                 'Christian liberty, economic stewardship, election integrity'
                 + (', public justice &amp; law/order' if candidate_tier in ('state', 'local') else ''))

    # v4.0 — Dynamic max per Adam's 2026-05-18 directive: candidate's max
    # is 2 × answered_questions, not always 100. A candidate scored on
    # 45/50 questions caps at 90; the letter grade is the percentage of
    # *their* max, not the global 100. This stops penalizing officials for
    # questions where our research found no public position either way.
    answered_count = total['answered']
    max_possible = answered_count * POINTS_PER_TRUE  # 2pt per answered Q
    # Thin-record guard (2026-07-19 / Adam Harding screenshot):
    # Dynamic-max % of answered was designed so we don't punish missing research,
    # but with only a handful of cells it produced "A / 100%" while OG said 6/100.
    # Below MIN_ANSWERED_FOR_DYNAMIC_GRADE we show absolute /100 (2 pts × global max)
    # and suppress the letter grade so thin seeds cannot look like full A's.
    MIN_ANSWERED_FOR_DYNAMIC_GRADE = 10
    thin_record = answered_count < MIN_ANSWERED_FOR_DYNAMIC_GRADE
    if thin_record:
        pct_of_max = max(0, min(100, round((adjusted_score / MAX_TOTAL) * 100))) if MAX_TOTAL else 0
        grade_letter = '\u2014'  # em dash — grade withheld
    elif max_possible > 0:
        # Cap pct floor at 0 — when adjustments (e.g., -50 Soros) exceed
        # max_possible, raw pct goes negative which displays as nonsense
        # like "-250%". Cap display at 0; the absolute negative score is
        # still visible in the adjusted_score field for full transparency.
        raw_pct = round((adjusted_score / max_possible) * 100)
        pct_of_max = max(0, raw_pct)
        grade_letter = letter_grade(pct_of_max)
    else:
        pct_of_max = 0
        grade_letter = letter_grade(pct_of_max)

    if thin_record:
        thin_score_title = (
            f'Thin evidence seed \u2014 {answered_count} questions answered. '
            f'Showing absolute {adjusted_score}/100 (not dynamic-max %). '
            f'Letter grade suppressed until \u2265{MIN_ANSWERED_FOR_DYNAMIC_GRADE} answered cells. '
            f'Raw dynamic max would be {max_possible} pts ({answered_count}\u00d72).'
        )
        grade_aria = (
            f'Thin seed \u2014 letter grade withheld until \u2265{MIN_ANSWERED_FOR_DYNAMIC_GRADE} answered questions'
        )
    else:
        thin_score_title = (
            'Score on a uniform /100 scale (percentage of dynamic max). '
            'Lets you compare a state councilor, state senator, and U.S. senator at a glance '
            'even though they answer different question counts.'
        )
        grade_aria = f'Letter grade {grade_letter} ({pct_of_max} of 100)'

    # Data-freshness: latest verified_date across this candidate's claims
    # (if any are verified), else fall back to scorecard-level last_updated.
    # Renders under the candidate's name so a visitor instantly knows how
    # recent this score is.
    claim_dates = [cl.get('verified_date') for cl in (c.get('claims') or [])
                   if cl.get('verified') and cl.get('verified_date')]
    freshness_date = max(claim_dates) if claim_dates else (meta or {}).get('last_updated', '')
    freshness_source = 'claim' if claim_dates else 'scorecard'

    # Scoring-confidence chip. profile.confidence == 'party_default' marks
    # records that were seeded from party-line heuristics rather than
    # individual evidence review (see seed-state-assemblies.py). These
    # records should render a visible warning chip so visitors don't
    # conflate them with the evidence-reviewed records on the same page.
    confidence = profile.get('confidence') or 'evidence'
    scoring_rationale = profile.get('scoring_rationale') or ''
    # Also detect records that weren't party-default-seeded but have no
    # scored answers at all (all-null across every category + no claims).
    # These should render a neutral "Awaiting review" banner so a visitor
    # isn't left staring at a profile of dashes without context.
    _scores_dict = c.get('scores') or {}
    _all_null = all(
        all(x is None for x in (_scores_dict.get(cat) or [None]))
        for cat in _scores_dict
    ) if _scores_dict else True
    _has_claims = bool(c.get('claims'))
    if confidence == 'party_default':
        confidence_chip_html = (
            '<div class="prof-confidence-banner" role="note" aria-label="Scoring confidence">'
            '<span class="prof-confidence-chip prof-conf-party-default">Party-default scoring</span>'
            '<span class="prof-confidence-text">Scored by party heuristic, not yet individually reviewed. '
            '<a href="#scoring-rationale">See rationale ↓</a></span>'
            '</div>'
        )
    elif _all_null and not _has_claims:
        confidence_chip_html = (
            '<div class="prof-confidence-banner prof-conf-awaiting" role="note" aria-label="Scoring confidence">'
            '<span class="prof-confidence-chip prof-conf-awaiting-chip">Awaiting review</span>'
            '<span class="prof-confidence-text">This profile is scaffolding — the candidate is in our roster '
            'but no scoring pass has been run yet. If you have evidence of this officials positions, the '
            '<a href="#feedback">feedback form</a> below is the fastest way to seed a first review.</span>'
            '</div>'
        )
    else:
        confidence_chip_html = ''

    # Map link: states with detailed maps (counties + CDs + city dots)
    # route to /map.html?st=XX&slug=<slug>; everywhere else routes to
    # /state.html?st=<code> for the simpler state-outline + roster.
    map_link_html = ''
    _state_code_up = (c.get('state') or '').upper()
    DETAILED_MAP_STATES = ('VA','FL','TX','NY','CA','PA','IL','OH','GA','MI','NC','NJ','AZ')
    if _state_code_up in DETAILED_MAP_STATES:
        _state_full = STATE_NAMES_FULL.get(_state_code_up, _state_code_up)
        map_link_html = (
            '<a class="prof-map-link" '
            f'href="../../map.html?st={_state_code_up}&slug={c.get("slug","")}" '
            f'aria-label="View this district / city on the {_state_full} map">'
            f'🗺️ View on {_state_full} map'
            '</a>'
        )
    elif _state_code_up and _state_code_up not in ('US',):
        _state_full = STATE_NAMES_FULL.get(_state_code_up, _state_code_up)
        map_link_html = (
            '<a class="prof-map-link" '
            f'href="../../state.html?st={_state_code_up}" '
            f'aria-label="Open {_state_full} home page with state shape">'
            f'🗺️ {_state_full} home'
            '</a>'
        )

    # RESOLUTE Local civic-tool banner — for local officials whose city has a
    # live civic page (live agendas + citizen briefs + how to weigh in).
    civic_tool_html = ''
    _civic_url = CIVIC_TOOL_MAP.get((c.get('jurisdiction') or '').strip())
    if _civic_url:
        civic_tool_html = (
            '<a class="prof-civic-link" '
            f'href="{_civic_url}" target="_blank" rel="noopener" '
            'style="display:inline-block;margin-top:8px;background:linear-gradient(90deg,#c9a84c,#D4AF37);'
            'color:#000;font-weight:700;padding:7px 14px;border-radius:6px;text-decoration:none;font-size:0.82rem;" '
            'aria-label="Track this council live on RESOLUTE Local">'
            '📍 Track this council live — agendas, briefs &amp; how to weigh in &rarr;'
            '</a>'
        )

    # CIVIC VOTING RECORD — pulled from RESOLUTE Local minutes data
    # (cross-repo). For FXBG council members (and similar local
    # officials in cities where we have minutes-parsed data), surface
    # their actual recorded voting record from official city minutes:
    # how many votes they participated in, how often they were in the
    # majority, and the specific motions where they dissented. Added
    # 2026-05-27 as the inbound side of the bidirectional linkage.
    civic_voting_html = ''
    if _civic_url:  # only attempt for officials in cities with civic-tool data
        _voting = _load_civic_voting()
        _cand_name = (c.get('name') or '').strip()
        _cand_parts = _cand_name.split()
        _cand_last = ''
        if _cand_parts:
            _cand_last = _cand_parts[-1].rstrip('.,').strip()
            if _cand_last.lower() in ('jr', 'sr', 'ii', 'iii', 'iv') and len(_cand_parts) >= 2:
                _cand_last = _cand_parts[-2].rstrip('.,').strip()
        _stats = _voting.get(_cand_last.lower(), {}) if _cand_last else {}
        if _stats.get('participated', 0) > 0:
            _participated = _stats['participated']
            _maj = _stats.get('majority', 0)
            _maj_pct = round(100 * _maj / _participated) if _participated else 0
            _dissents = _stats.get('dissents', [])
            _dissent_count = len(_dissents)
            _accent_color = '#ffb84d' if _dissent_count > 0 else '#66bb6a'
            _dissents_html = ''
            if _dissents:
                _dissents_html = (
                    '<div style="margin-top:8px;font-size:0.82rem;color:var(--gray,#a8b0bc);">'
                    '<strong style="color:#ffb84d;">Notable dissents (voted against the majority):</strong>'
                    '<ul style="margin:4px 0 0;padding-left:18px;line-height:1.5;">'
                )
                for _d in _dissents[:5]:
                    _dissents_html += (
                        f'<li><span style="color:#ffb84d;font-weight:700;">{_d["tally"]}</span> · '
                        f'<span style="font-size:0.78rem;color:var(--gray);">{_d["date"]}</span> — '
                        f'{_d["title"]}</li>'
                    )
                if len(_dissents) > 5:
                    _dissents_html += f'<li style="font-style:italic;">+{len(_dissents)-5} more in the city minutes →</li>'
                _dissents_html += '</ul></div>'
            else:
                _dissents_html = (
                    '<div style="margin-top:6px;font-size:0.82rem;color:#66bb6a;">'
                    '✓ Voted with the majority on every recorded motion to date.'
                    '</div>'
                )
            civic_voting_html = (
                '<div style="margin-top:10px;padding:12px 14px;background:rgba(76,175,80,0.06);'
                f'border-left:3px solid {_accent_color};border-radius:0 4px 4px 0;font-size:0.88rem;">'
                '<div style="font-size:0.72rem;font-weight:700;letter-spacing:0.6px;text-transform:uppercase;'
                f'color:{_accent_color};margin-bottom:6px;">📊 Live City Council Voting Record</div>'
                f'<div>Recorded votes (from official city minutes): <strong>{_participated}</strong> · '
                f'In majority: <strong>{_maj}</strong> ({_maj_pct}%) · '
                f'Dissents: <strong style="color:{_accent_color};">{_dissent_count}</strong></div>'
                f'{_dissents_html}'
                f'<div style="margin-top:8px;font-size:0.74rem;color:var(--gray,#8a93a0);">'
                f'Source: parsed official city minutes via the RESOLUTE Local civic tool. '
                f'<a href="{_civic_url}#voting-record" target="_blank" rel="noopener" style="color:#D4AF37;">'
                f'See the full per-member voting comparison ↗</a></div>'
                '</div>'
            )

    # FORMER / LOST banner: when c.status is non-active, render a clear
    # banner at the top of the profile so visitors immediately know this
    # person isn't currently in office. Profile remains live + searchable
    # so a future appointment doesn't require re-creating the page.
    status_banner_html = ''
    status = c.get('status') or 'active'
    if status == 'former':
        candidacy_note = (profile.get('candidacy_note') or '').strip()
        status_banner_html = (
            '<div class="prof-status-banner prof-status-former" role="note" aria-label="Former officeholder">'
            '<span class="prof-status-chip">FORMER</span>'
            '<div class="prof-status-text">'
            f'<strong>{c.get("name", "This person")}</strong> is no longer in active government service. '
            'Profile preserved for historical reference + readiness if reappointed.'
            f'{(" " + candidacy_note) if candidacy_note else ""}'
            f' See <a href="../../citizen-formers.html">all former officials &rarr;</a>'
            '</div>'
            '</div>'
        )
    elif status == 'lost':
        candidacy_note = (profile.get('candidacy_note') or '').strip()
        status_banner_html = (
            '<div class="prof-status-banner prof-status-lost" role="note" aria-label="Failed candidate">'
            '<span class="prof-status-chip">LOST</span>'
            '<div class="prof-status-text">'
            f'<strong>{c.get("name", "This candidate")}</strong> lost the election for this position. '
            'Scoring reflects their record at time of candidacy.'
            f'{(" " + candidacy_note) if candidacy_note else ""}'
            f' See <a href="../../citizen-formers.html">all failed candidates &rarr;</a>'
            '</div>'
            '</div>'
        )
    elif status == 'lame_duck':
        candidacy_note = (profile.get('candidacy_note') or '').strip()
        status_banner_html = (
            '<div class="prof-status-banner prof-status-lame" role="note" aria-label="Not seeking re-election">'
            '<span class="prof-status-chip">LAME DUCK</span>'
            '<div class="prof-status-text">'
            f'<strong>{c.get("name", "This official")}</strong> is still in active office '
            'but has announced they will not seek re-election in 2026.'
            f'{(" " + candidacy_note) if candidacy_note else ""}'
            '</div>'
            '</div>'
        )

    # Candidacy banner: when profile.candidacy is set, surface "Running for X"
    # with a deep-link to the side-by-side comparison view for that race.
    candidacy_banner_html = ''
    cand = profile.get('candidacy') or {}
    if cand.get('race_id'):
        is_inc = bool(cand.get('is_incumbent'))
        chip_label = 'Incumbent' if is_inc else 'Challenger'
        chip_class = 'prof-cand-incumbent' if is_inc else 'prof-cand-challenger'
        primary = cand.get('primary_date') or ''
        general = cand.get('general_date') or ''
        dates = []
        if primary: dates.append(f'Primary {primary}')
        if general: dates.append(f'General {general}')
        date_str = ' · '.join(dates)
        decl = cand.get('declared_date') or ''
        decl_str = f', declared {decl}' if decl else ''
        race_id = cand.get('race_id') or ''
        race_link = (
            f' <a href="../../races/{race_id}.html">This race &rarr;</a>'
            if race_id else ''
        )
        candidacy_banner_html = (
            '<div class="prof-candidacy-banner" role="note" aria-label="Candidacy status">'
            f'<span class="prof-candidacy-chip {chip_class}">{chip_label}</span>'
            '<div class="prof-candidacy-text">'
            f'Currently running for <strong>{cand.get("office","")}</strong>'
            f'{decl_str}. {date_str}.'
            f'{race_link}'
            f' <a href="../../compare.html?race={race_id}">'
            f'Compare against other candidates &rarr;</a>'
            '</div>'
            '</div>'
        )

    state_code = (c.get('state') or 'VA').upper()
    state_name = STATE_NAMES_FULL.get(state_code, state_code)
    nav = nav or {}
    prev_c = nav.get('prev')
    next_c = nav.get('next')
    position = nav.get('position', 1)
    group_size = nav.get('group_size', 1)
    group_label = nav.get('group_label') or c.get('jurisdiction') or ''

    # ---- Breadcrumb (replaces single back link) ----
    crumbs = [
        '<a href="../../citizen.html">RESOLUTE Citizen</a>',
        '<a href="../../find-my-reps.html">Find My Reps</a>',
        f'<a href="../../citizen.html?state={state_code}">{state_name}</a>',
    ]
    if group_label and group_label != state_name:
        crumbs.append(f'<a href="../../citizen.html?state={state_code}">{group_label}</a>')
    crumbs.append(f'<span class="crumb-current">{c["name"]}</span>')
    breadcrumb_html = '<nav class="prof-breadcrumb" aria-label="Breadcrumb">' + ' <span class="crumb-sep">›</span> '.join(crumbs) + '</nav>'

    # ---- Prev / Next nav ----
    def nav_link(neighbor, direction, label_arrow):
        if not neighbor:
            return f'<span class="prof-nav-btn prof-nav-disabled">{label_arrow}</span>'
        n_state = (neighbor.get('state') or state_code).lower()
        n_slug = neighbor.get('slug', '')
        n_name = neighbor.get('name', '')
        n_office = neighbor.get('office', '')
        href = f'{n_slug}.html' if n_state == state_code.lower() else f'../{n_state}/{n_slug}.html'
        return (
            f'<a class="prof-nav-btn" href="{href}" data-direction="{direction}">'
            f'<span class="prof-nav-arrow">{label_arrow}</span>'
            f'<span class="prof-nav-text"><span class="prof-nav-name">{n_name}</span>'
            f'<span class="prof-nav-office">{n_office}</span></span></a>'
        )

    position_html = (
        f'<div class="prof-nav-position">{position} of {group_size}'
        + (f' &middot; {group_label}' if group_label else '')
        + '</div>'
    )
    prev_html = nav_link(prev_c, 'prev', '← Prev')
    next_html = nav_link(next_c, 'next', 'Next →')
    prevnext_bar = (
        '<div class="prof-nav-bar">'
        f'{prev_html}{position_html}{next_html}'
        '</div>'
    )

    # Hidden data attributes for keyboard shortcuts (left/right arrows)
    prev_href = ''
    next_href = ''
    if prev_c:
        n_state = (prev_c.get('state') or state_code).lower()
        prev_href = f"{prev_c.get('slug','')}.html" if n_state == state_code.lower() else f"../{n_state}/{prev_c.get('slug','')}.html"
    if next_c:
        n_state = (next_c.get('state') or state_code).lower()
        next_href = f"{next_c.get('slug','')}.html" if n_state == state_code.lower() else f"../{n_state}/{next_c.get('slug','')}.html"

    # ---- Contact block (phone + contact form + email + twitter) ----
    contact_html = build_contact_html(c)

    # ---- Election countdown + state admin info ----
    # elections_data is passed via closure from main() (loaded once)
    election_html = build_election_html(c, meta.get('_elections_data') or {})

    # ---- Photo / initials badge ----
    photo_path = c.get('photo') or ''
    if photo_path:
        # If a sibling .webp exists (built by build-webp.py), emit a
        # <picture> element so WebP-supporting browsers (>96% of users)
        # download the smaller WebP. JPEG remains the fallback for the
        # rare browser that can't handle WebP.
        webp_rel = re.sub(r'\.jpg$', '.webp', photo_path, flags=re.IGNORECASE)
        has_webp = (webp_rel != photo_path and
                    os.path.exists(os.path.join(BASE_DIR, webp_rel)))
        if has_webp:
            photo_html = (
                f'<picture>'
                f'<source type="image/webp" srcset="../../{webp_rel}">'
                f'<img class="prof-photo" src="../../{photo_path}" alt="{c["name"]}" loading="lazy">'
                f'</picture>'
            )
        else:
            photo_html = f'<img class="prof-photo" src="../../{photo_path}" alt="{c["name"]}" loading="lazy">'
    else:
        badge_bg, badge_fg = color_for_slug(c.get('slug', ''))
        badge_text = initials(c['name'])
        photo_html = (
            f'<div class="prof-photo prof-initials" '
            f'style="background:{badge_bg};color:{badge_fg};" '
            f'aria-hidden="true">{badge_text}</div>'
        )

    # ---- JSON-LD Person schema for search engines / AI crawlers ----
    # Built in Python rather than the template so the conditional
    # `sameAs` field is clean. json.dumps quotes correctly + escapes.
    import json as _json
    _ld = {
        '@context': 'https://schema.org',
        '@type': 'Person',
        'name': c['name'],
        'jobTitle': c.get('office', ''),
        'affiliation': {'@type': 'Organization', 'name': c.get('jurisdiction', '')},
        'url': f"https://usmcmin.com/candidates/{state_code.lower()}/{c.get('slug','')}.html",
    }
    if photo_path:
        _ld['image'] = f"https://usmcmin.com/{photo_path}"
    _same_as = []
    if c.get('website'):
        _same_as.append(c['website'])
    _twitter = (c.get('profile') or {}).get('twitter')
    if _twitter:
        _same_as.append(f"https://x.com/{str(_twitter).lstrip('@')}")
    _facebook = (c.get('profile') or {}).get('facebook')
    if _facebook:
        _same_as.append(f"https://facebook.com/{_facebook}")
    if _same_as:
        _ld['sameAs'] = _same_as
    json_ld = _json.dumps(_ld, separators=(',', ':'))

    # Index claims by (category, question_idx) so the per-question
    # rows can render an "i" icon that reveals the specific evidence
    # backing each score cell.
    claims_by_cell = {}
    for cl in (c.get('claims') or []):
        key = (cl.get('category'), cl.get('question_idx'))
        claims_by_cell.setdefault(key, []).append(cl)

    # ---- Footnotes per answer cell (v3.4.0) ----------------------------
    # candidate.footnotes is {fn_id: {url, archive_url, title, publisher,
    # accessed, excerpt}}. candidate.answer_footnotes maps (category,
    # question_idx) -> list[fn_id]. The profile template reads both and
    # renders:
    #   * a small superscript [n] next to each answered question cell
    #   * a References section at the bottom of the profile listing every
    #     footnote used anywhere on the page, with the archive.org URL
    #     when we have one.
    # For records flagged profile.confidence == 'party_default' that lack
    # explicit footnotes, we synthesize a single [P] marker per answered
    # cell that links to the in-page scoring-rationale anchor.
    footnotes_dict = c.get('footnotes') or {}
    answer_footnotes_map = c.get('answer_footnotes') or {}
    # fn_id -> assigned display number (1-based, in first-appearance order)
    fn_display_num = {}
    fn_display_order = []

    def ensure_fn_number(fn_id):
        if fn_id not in fn_display_num:
            fn_display_num[fn_id] = len(fn_display_order) + 1
            fn_display_order.append(fn_id)
        return fn_display_num[fn_id]

    def render_fn_markers_for(cat_id, q_idx, answer_value):
        """Return the <sup>...</sup> HTML to append next to an answer cell.

        Uses the candidate's explicit footnotes if present; otherwise
        falls back to the synthetic party-default marker. For null
        answers (—) we DO still render footnotes when they exist,
        because those footnotes typically point at primary-source
        lookup tools (e.g., TrackAIPAC, OpenSecrets) where a visitor
        can verify the question for themselves — which is precisely
        what an "unknown" score calls for."""
        ids = (answer_footnotes_map.get(cat_id) or [])
        ids = ids[q_idx] if q_idx < len(ids) else []
        if not ids and (profile.get('confidence') == 'party_default'):
            ensure_party_default_fn_id()
            ids = ['_pd']
        # Filter out synthetic _pd marker when the answer IS null — a
        # party-default null doesn't meaningfully point at the
        # rationale card.
        if answer_value is None:
            ids = [fn_id for fn_id in ids if fn_id != '_pd']
        if not ids:
            return ''
        links = []
        for fn_id in ids:
            if fn_id == '_pd':
                num = ensure_fn_number('_pd')
                links.append(f'<a class="prof-fn-link" href="#scoring-rationale" '
                             f'aria-label="See scoring rationale (footnote {num})">{num}</a>')
            else:
                if fn_id not in footnotes_dict:
                    continue
                num = ensure_fn_number(fn_id)
                links.append(f'<a class="prof-fn-link" href="#fn-{fn_id}" '
                             f'aria-label="See footnote {num}">{num}</a>')
        if not links:
            return ''
        # Slightly different styling for null-answer markers: the
        # prof-fn-sup-lookup class signals "this is a lookup hint, not
        # a citation for a known answer." CSS gives it a muted color.
        cls = 'prof-fn-sup prof-fn-sup-lookup' if answer_value is None else 'prof-fn-sup'
        return (
            f'<sup class="{cls}" aria-label="References for this answer">'
            '[' + ','.join(links) + ']</sup>'
        )

    _pd_seeded = [False]

    def ensure_party_default_fn_id():
        # Ensures the synthetic party-default footnote exists in the
        # References section when we render at least one [P]-style marker.
        if _pd_seeded[0]:
            return
        footnotes_dict.setdefault('_pd', {
            'url': '#scoring-rationale',
            'title': 'Party-default scoring heuristic — see rationale card below',
            'publisher': 'U.S.M.C. Ministries · RESOLUTE Citizen',
            'accessed': freshness_date or '',
            'excerpt': 'This answer was scored via the party-default heuristic. '
                       'See the "Scoring rationale" card below for the full methodology. '
                       'Individual voting-record review is pending.',
            'archive_url': None,
            'synthetic': True,
        })
        _pd_seeded[0] = True

    def render_references_section():
        if not fn_display_order:
            return ''
        items = []
        for fn_id in fn_display_order:
            entry = footnotes_dict.get(fn_id) or {}
            num = fn_display_num[fn_id]
            url = entry.get('url') or ''
            archive_url = entry.get('archive_url')
            title = entry.get('title') or url
            publisher = entry.get('publisher') or ''
            accessed = entry.get('accessed') or ''
            excerpt = entry.get('excerpt') or ''
            is_synthetic = bool(entry.get('synthetic'))
            bias_chip_html = ''
            if url and not is_synthetic and url.startswith('http'):
                entry_bias = sb.resolve(url)
                tone = sb.badge_tone(entry_bias)
                bias_chip_html = (
                    f'<span class="prof-bias-chip prof-bias-{tone}" '
                    f'title="{entry_bias.get("note") or entry_bias.get("display_name") or url}">'
                    f'{sb.badge_label(entry_bias)}</span>'
                )
            lines = []
            # Primary link
            if url.startswith('#'):
                lines.append(f'<a class="prof-fn-title" href="{url}">{title}</a>')
            elif url:
                lines.append(f'<a class="prof-fn-title" href="{url}" target="_blank" rel="noopener">{title}</a>')
            else:
                lines.append(f'<span class="prof-fn-title">{title}</span>')
            # Publisher + accessed
            meta_bits = []
            if publisher:
                meta_bits.append(publisher)
            if accessed:
                meta_bits.append(f'accessed {accessed}')
            meta_line = ' · '.join(meta_bits)
            # Archive link
            archive_html = ''
            if archive_url:
                archive_html = (
                    f' · <a class="prof-fn-archive" href="{archive_url}" '
                    f'target="_blank" rel="noopener">Wayback archive</a>'
                )
            elif url.startswith('http'):
                # Render a "Fetch archived copy" link that jumps to the
                # Wayback Machine's on-demand capture URL for that source.
                wm = 'https://web.archive.org/web/2/' + url
                archive_html = (
                    f' · <a class="prof-fn-archive" href="{wm}" '
                    f'target="_blank" rel="noopener">Fetch Wayback archive</a>'
                )
            items.append(
                f'<li class="prof-fn-item" id="fn-{fn_id}">'
                f'<span class="prof-fn-num">[{num}]</span>'
                f'<div class="prof-fn-body">'
                f'{lines[0]} {bias_chip_html}'
                f'<div class="prof-fn-meta">{meta_line}{archive_html}</div>'
                + (f'<blockquote class="prof-fn-excerpt">{excerpt}</blockquote>' if excerpt else '')
                + '</div></li>'
            )
        return (
            '<section id="references" class="prof-references" aria-label="References">'
            '<h2>References &amp; footnotes</h2>'
            '<p class="prof-references-lead">Every answer above with a <sup>[n]</sup> marker '
            'corresponds to one of the footnotes below. Wayback-archive links preserve the page '
            "as it read at our access date so a reader can verify the citation even if the "
            'original URL changes or disappears.</p>'
            '<ol class="prof-fn-list">' + ''.join(items) + '</ol>'
            '</section>'
        )

    def render_claim_sources(claim_sources):
        parts = []
        for url in claim_sources or []:
            entry = sb.resolve(url)
            tone = sb.badge_tone(entry)
            name = entry.get('display_name') or url
            parts.append(
                f'<li class="prof-q-claim-src"><a href="{url}" target="_blank" rel="noopener">{name}</a>'
                f'<span class="prof-bias-chip prof-bias-{tone}" title="{entry.get("note", name)}">{sb.badge_label(entry)}</span></li>'
            )
        return '<ul class="prof-q-claim-src-list">' + ''.join(parts) + '</ul>' if parts else ''

    def render_claims_block(cat_id, q_idx):
        items = claims_by_cell.get((cat_id, q_idx), [])
        if not items:
            return ''
        rows = []
        for cl in items:
            cid = cl.get('id', '')
            text = cl.get('text', '')
            verified = cl.get('verified')
            vdate = cl.get('verified_date') or ''
            disputed = cl.get('disputed')
            badge = ''
            if disputed:
                badge = '<span class="prof-q-claim-badge disputed">Disputed</span>'
            elif verified:
                badge = f'<span class="prof-q-claim-badge verified">Verified{" " + vdate if vdate else ""}</span>'
            dispute_href = f'?claim={cid}#feedback'
            rows.append(
                '<li class="prof-q-claim" id="' + cid + '">'
                f'<p class="prof-q-claim-text">{text}</p>'
                + render_claim_sources(cl.get('sources') or [])
                + '<div class="prof-q-claim-meta">' + badge
                + f'<a class="prof-q-claim-dispute" href="{dispute_href}" '
                'data-claim-dispute="1">Dispute this claim</a></div></li>'
            )
        n = len(items)
        label = f'{n} claim' + ('' if n == 1 else 's')
        return (
            '<details class="prof-q-claims">'
            f'<summary class="prof-q-claim-toggle" aria-label="Show evidence for this answer">'
            f'<span class="prof-q-claim-i" aria-hidden="true">i</span> {label}</summary>'
            '<ol class="prof-q-claim-list">' + ''.join(rows) + '</ol>'
            '</details>'
        )

    # Build category breakdown
    # Map scorecard category id to a petition-template slug. Only the
    # seven RESOLUTE categories; the "custom" template handles anything
    # outside this set. Keeps the deep-link explicit rather than implicit.
    PETITION_CAT_MAP = {
        'life': 'life', 'marriage': 'marriage', 'immigration': 'immigration',
        'self_defense': 'self_defense', 'education': 'education',
        'america_first': 'america_first', 'christian_heritage': 'christian_heritage',
    }
    # Deep-dive page slugs for each v4.x category. Files live under
    # /citizen/<slug>.html — the rubric metric on each profile becomes a link
    # so a reader can jump from "Sanctity of Life · 0/10" to the full
    # rubric/anchor-scripture/disqualifier list for that category.
    # Added 2026-05-19 per Adam's clickable-metrics directive.
    CAT_DEEPDIVE_MAP = {
        'sanctity_of_life': 'sanctity-of-life',
        'biblical_marriage': 'biblical-marriage',
        'family_child_sovereignty': 'family-child-sovereignty',
        'christian_liberty': 'christian-liberty',
        'economic_stewardship': 'economic-stewardship',
        'election_integrity': 'election-integrity',
        'border_immigration': 'border-immigration',
        'self_defense': 'self-defense-2a',
        'foreign_policy_restraint': 'foreign-policy-restraint',
        'industry_capture': 'industry-capture',
        'public_justice': 'public-justice',
        'refuse_federal_overreach': 'refuse-federal-overreach',
        'refuse_state_overreach': 'refuse-state-overreach',
    }

    cat_html = ''
    for cat in categories:
        # v5.0 — only render categories in this candidate's tier rubric.
        # (Federal-only categories like Foreign Policy are hidden for state/local;
        # Refuse-Overreach / Public Justice are hidden for federal.)
        _pillars = cat.get('pillars')
        if _pillars is not None and candidate_tier not in _pillars:
            continue
        cs = calc_cat_score(c['scores'].get(cat['id'], []))
        color = score_color(cs['score'], MAX_PER_TOPIC) if cs['answered'] > 0 else '#666'
        pet_cat = PETITION_CAT_MAP.get(cat['id'])
        pet_state = (c.get('state') or '').upper() if c.get('state') else ''
        petition_btn = ''
        # v5.6 — tier-aware label so state/local profiles display the
        # tier-specific subtitle (e.g. 'Sanctity of Life — Protect the
        # Vulnerable' at local). Federal falls back to canonical.
        _cat_label = tier_label(cat, candidate_tier)
        if pet_cat and pet_state and pet_state not in ('US',):
            petition_btn = (
                f'<a class="prof-cat-petition" '
                f'href="../../petition.html?state={pet_state}&cat={pet_cat}" '
                f'aria-label="Draft a petition to your {pet_state} reps about {_cat_label}" '
                f'title="Draft a petition to your {pet_state} reps about {_cat_label}">'
                '&#9993;&#xFE0F; Petition your reps'
                '</a>'
            )
        elif pet_cat:
            # US-level candidates (e.g., POTUS, SCOTUS) — still offer petition
            # without a specific state; petition.html will require state input.
            petition_btn = (
                f'<a class="prof-cat-petition" '
                f'href="../../petition.html?cat={pet_cat}" '
                f'aria-label="Draft a petition to your reps about {_cat_label}" '
                f'title="Draft a petition to your reps about {_cat_label}">'
                '&#9993;&#xFE0F; Petition your reps'
                '</a>'
            )
        deepdive_slug = CAT_DEEPDIVE_MAP.get(cat['id'])
        if deepdive_slug:
            cat_html += f'''
    <div class="prof-category">
      <div class="prof-cat-header">
        <a class="prof-cat-link" href="../../citizen/{deepdive_slug}.html" title="Open the full {_cat_label} rubric — questions, anchor Scripture, disqualifiers, and tier variants">
          <img src="../../assets/icons/{cat['icon']}" alt="" width="24" height="24">
          <h3>{_cat_label}</h3>
          <span class="prof-cat-score" style="color:{color};">{cs['score']}/{MAX_PER_TOPIC}</span>
          <span class="prof-cat-deepdive" aria-hidden="true">deep dive →</span>
        </a>
        {petition_btn}
      </div>
      <div class="prof-questions">'''
        else:
            cat_html += f'''
    <div class="prof-category">
      <div class="prof-cat-header">
        <img src="../../assets/icons/{cat['icon']}" alt="" width="24" height="24">
        <h3>{_cat_label}</h3>
        <span class="prof-cat-score" style="color:{color};">{cs['score']}/{MAX_PER_TOPIC}</span>
        {petition_btn}
      </div>
      <div class="prof-questions">'''
        questions = cat.get('questions', [])
        answers = c['scores'].get(cat['id'], [None]*5)
        for i in range(len(questions)):
            # v4.2/v4.3 — pick the tier-appropriate question text. Federal
            # officials see the default; state officials see questions_state[i]
            # if set; local officials see questions_local[i] if set.
            q = question_text_for_tier(cat, i, candidate_tier)
            a = answers[i] if i < len(answers) else None
            claims_block = render_claims_block(cat['id'], i)
            fn_markers = render_fn_markers_for(cat['id'], i, a)
            cat_html += f'''
        <div class="prof-q">
          <div class="prof-q-text">{q}</div>
          <div class="prof-q-answer">{answer_display(a)}{fn_markers}</div>
          {claims_block}
        </div>'''
        cat_html += '''
      </div>
    </div>'''

    # Profile details
    profile_html = ''
    twitter = profile.get('twitter', '')
    fields = [
        ('Religion', profile.get('religion')),
        ('Education', profile.get('education')),
        ('Birthplace', profile.get('birthplace')),
        ('Background', profile.get('background')),
        ('Net Worth', profile.get('net_worth')),
        ('NRA Rating', profile.get('nra_rating')),
        ('Heritage Action Score', profile.get('heritage_action')),
        ('Committees', profile.get('committees')),
        ('Previous Election Opponent', profile.get('prev_election_opponent')),
        ('Next Election Year', profile.get('next_election_year')),
    ]
    if twitter:
        handle = twitter.lstrip('@')
        fields.append(('X / Twitter', f'<a href="https://x.com/{handle}" target="_blank" rel="noopener" style="color:var(--accent);">@{handle}</a>'))
    campaign_website = profile.get('campaign_website', '')
    if campaign_website:
        fields.append(('Campaign Website', f'<a href="{campaign_website}" target="_blank" rel="noopener" style="color:var(--accent);">{campaign_website}</a>'))
    for label, val in fields:
        if val:
            profile_html += f'<div class="prof-detail"><strong>{label}:</strong> {val}</div>'

    contenders = profile.get('next_election_contenders', [])
    if contenders:
        profile_html += f'<div class="prof-detail"><strong>Upcoming Contenders:</strong> {", ".join(contenders)}</div>'

    notes = c.get('notes', '')
    website = c.get('website', '')
    sources = c.get('sources', [])
    # Smart source labels based on domain
    SOURCE_LABELS = {
        'ballotpedia.org': 'Ballotpedia Profile',
        'vpap.org': 'VPAP — Virginia Public Access Project',
        'lis.virginia.gov': 'Virginia Legislative Information System',
        'heritageaction.com': 'Heritage Action Scorecard',
        'congress.gov': 'Congress.gov — Official Record',
        'senate.gov': 'Official Senate Page',
        'house.gov': 'Official House Page',
        'supremecourt.gov': 'U.S. Supreme Court',
        'whitehouse.gov': 'The White House',
        'nrapvf.org': 'NRA Political Victory Fund',
        'plannedparenthoodaction.org': 'Planned Parenthood Action',
        'choicetracker.org': 'Choice Tracker — Abortion Votes',
        'votesmart.org': 'Vote Smart — Voting Record',
        'opensecrets.org': 'OpenSecrets — Campaign Finance',
        'fredericksburgva.gov': 'City of Fredericksburg Official',
        'spotsylvania.va.us': 'Spotsylvania County Official',
        'staffordcountyva.gov': 'Stafford County Official',
        'fredericksburgfreepress.com': 'Fredericksburg Free Press',
        'fxbgadvance.com': 'FXBG Advance',
        'progressivevotersguide.com': 'Progressive Voters Guide',
        'x.com': 'X / Twitter',
        'twitter.com': 'X / Twitter',
        'capitol.texas.gov': 'Texas Capitol — Legislature',
        'legislature.idaho.gov': 'Idaho Legislature',
        'gov.texas.gov': 'Texas Governor Official',
    }

    def get_source_label(url):
        for domain, label in SOURCE_LABELS.items():
            if domain in url:
                return label
        # Fallback: clean display
        display = url.replace('https://', '').replace('http://', '')
        if len(display) > 55:
            display = display[:52] + '...'
        return display

    sources_html = ''
    if sources:
        # Source Diversity strip — aggregate bias counts across this
        # candidate's sources. Shows the skeptical visitor at a glance
        # whether the score was built against a balanced evidence base
        # or against a monoculture of one tilt.
        diversity = sb.diversity_counts(sources)
        # Order left-to-right: bias spectrum, then civic sources.
        bands = [
            ('left',       'Left'),
            ('lean_left',  'Lean Left'),
            ('center',     'Center'),
            ('lean_right', 'Lean Right'),
            ('right',      'Right'),
            ('official',   'Official'),
            ('reference',  'Reference'),
            ('social',     'Social'),
            ('neutral',    'Other'),
        ]
        diversity_chips = []
        for key, label in bands:
            n = diversity.get(key, 0)
            if n > 0:
                css_tone = key.replace('_', '-')
                diversity_chips.append(
                    f'<span class="prof-div-chip prof-bias-{css_tone}">{n} {label}</span>'
                )
        diversity_strip_html = ''
        if len(sources) >= 2 and diversity_chips:
            diversity_strip_html = (
                '<div class="prof-source-diversity" role="group" '
                'aria-label="Source diversity breakdown for this profile">'
                + ''.join(diversity_chips) +
                '</div>'
            )
        sources_html = '<div id="prof-sources" class="prof-sources"><h2>Sources &amp; Evidence</h2>'
        sources_html += diversity_strip_html
        sources_html += '<div class="prof-source-list">'
        for src in sources:
            label = get_source_label(src)
            entry = sb.resolve(src)
            chip_label = sb.badge_label(entry)
            chip_tone = sb.badge_tone(entry)
            # Display name from bias entry is preferred when the SOURCE_LABELS
            # table didn't have a custom label for this URL.
            display_name = entry.get('display_name')
            if display_name and label and label.startswith(('ballotpedia', 'https', 'http')):
                label = display_name
            chip_title = entry.get('note') or entry.get('display_name') or chip_label
            sources_html += (
                '<div class="prof-source-row">'
                f'<a href="{src}" target="_blank" rel="noopener">{label}</a>'
                f'<span class="prof-bias-chip prof-bias-{chip_tone}" '
                f'title="{chip_title}">{chip_label}</span>'
                '</div>'
            )
        sources_html += '</div>'
        sources_html += (
            '<p class="prof-bias-attribution">Bias ratings sourced from '
            '<a href="https://www.allsides.com/media-bias/ratings" target="_blank" rel="noopener">AllSides</a> '
            'and <a href="https://adfontesmedia.com/interactive-media-bias-chart/" target="_blank" rel="noopener">Ad Fontes Media</a>. '
            'Classifications for government, reference, and advocacy domains are maintained by U.S.M.C. Ministries; '
            'see <a href="https://github.com/adamljohns/usmcmin-com/blob/main/data/source_bias.json" target="_blank" rel="noopener">source_bias.json</a>.'
            '</p>'
        )
        sources_html += '</div>'

    # v4.3 — tier callout. For state/local candidates, surface a small chip
    # showing how many of the 50 rubric questions actually apply at their
    # office level. Federal candidates already see "X of 50 answered" with
    # 50 being the full possible — no chip needed. (Added 2026-05-19 per
    # Adam's "surface state/local tier badges" directive.)
    applicable_total = 0
    for cat in categories:
        # v5.0 — only count questions in categories that are in this tier's rubric
        _pillars = cat.get('pillars')
        if _pillars is not None and candidate_tier not in _pillars:
            continue
        aa = cat.get('applicable_at') or []
        for tiers in aa:
            if candidate_tier in tiers:
                applicable_total += 1
    if applicable_total == 0:
        applicable_total = 50  # safety fallback if applicable_at metadata is absent

    if candidate_tier in ('state', 'local'):
        tier_pretty = 'State' if candidate_tier == 'state' else 'Local'
        tier_pill_class = f'prof-tier-pill-{candidate_tier}'
        tier_callout_html = (
            f'<div class="prof-tier-callout" '
            f'title="This office is classified at the {candidate_tier} tier per the v4.1 applicability matrix. '
            f'{applicable_total} of the 50 rubric questions are scoreable at this chair; the rest are marked N/A '
            f'because the office does not decide them. Dynamic-max grading divides by 2 × answered, never by 100.">'
            f'<span class="prof-tier-pill {tier_pill_class}">{tier_pretty} tier</span>'
            f'<span class="prof-tier-note"><strong>{applicable_total} of 50 rubric questions apply</strong> '
            f'at this office level &mdash; federal-only questions are marked N/A and excluded from the dynamic max. '
            f'<a href="/scoring-system.html#tiered-grading">How tier grading works &rarr;</a></span>'
            f'</div>'
        )
    else:
        tier_callout_html = ''

    _adj_sign = '+' if adj_total > 0 else ''
    _adj_dir = 'plus' if adj_total > 0 else 'minus'
    _adj_section_html = (
        f'&middot; <span class="prof-total-adj prof-total-adj-{_adj_dir}">\n'
        f'          {_adj_sign}{adj_total}\n'
        f'        </span>\n'
        f'        foreign-influence adjustment'
    ) if adj_total != 0 else ''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['name']} — RESOLUTE Citizen Scorecard | U.S.M.C. Ministries</title>
  <meta name="description" content="RESOLUTE Citizen Scorecard for {c['name']} ({party_label(c['party'])}). {c['office']}, {c['jurisdiction']}. Score: {pct_of_max}/100 ({grade_letter}).">

  <!-- Canonical URL for SEO + social previews -->
  <link rel="canonical" href="https://usmcmin.com/candidates/{state_code.lower()}/{c.get('slug','')}.html">

  <!-- Open Graph (Facebook, LinkedIn, iMessage previews) -->
  <meta property="og:site_name" content="RESOLUTE Citizen Scorecard">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{c['name']} — {total['score']}/{MAX_TOTAL} on the RESOLUTE Citizen Scorecard">
  <meta property="og:description" content="{party_label(c['party'])} · {c['office']}, {c['jurisdiction']}. Score {pct_of_max}/100 ({grade_letter}) on the RESOLUTE Citizen {candidate_tier} rubric. Click to see voting record + sources.">
  <meta property="og:url" content="https://usmcmin.com/candidates/{state_code.lower()}/{c.get('slug','')}.html">
  <meta property="og:image" content="{('https://usmcmin.com/' + photo_path) if photo_path else 'https://usmcmin.com/assets/og/og-citizen.jpg'}">
  <meta property="og:image:alt" content="{c['name']}">

  <!-- Twitter / X Card -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{c['name']} — {total['score']}/{MAX_TOTAL}">
  <meta name="twitter:description" content="{party_label(c['party'])} · {c['office']}. RESOLUTE Citizen Scorecard.">
  <meta name="twitter:image" content="{('https://usmcmin.com/' + photo_path) if photo_path else 'https://usmcmin.com/assets/og/og-citizen.jpg'}">

  <!-- JSON-LD Person schema for search engines -->
  <script type="application/ld+json">{json_ld}</script>

  <link rel="stylesheet" href="../../assets/css/main.min.css">
  <link rel="icon" type="image/svg+xml" href="../../assets/icons/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="../../assets/icons/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="../../assets/icons/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="../../assets/icons/apple-touch-icon.png">
  <link rel="stylesheet" href="../../assets/css/profile.min.css">
</head>
<body>

<nav>
  <a href="/" class="nav-brand" style="text-decoration:none">
    <img src="../../assets/img/logo.png" alt="U.S.M.C. Ministries" style="object-fit:contain">
    <div class="nav-brand-text">
      <div class="name">U.S.M.C. Ministries</div>
      <div class="tag">Warriors Equipped</div>
    </div>
  </a>
  <!-- Reverted 2026-05-23: Citizen ▾ dropdown removed per Adam's feedback —
       scorecard pages reachable via index hero, footer, and direct URL. -->
  <ul class="nav-links">
    <li><a href="../../mission.html">Mission</a></li>
    <li><a href="../../shop.html">Shop</a></li>
    <li><a href="../../books.html">Books</a></li>
    <li><a href="../../coaching.html">Coaching</a></li>
    <li><a href="../../fitness/">Fitness</a></li>
    <li><a href="../../finance/">Finance</a></li>
    <li><a href="../../about.html">About</a></li>
    <li><a href="https://usmcmin.org" target="_blank">Ministry Site</a></li>
  </ul>
  <a href="../../coaching.html" class="btn nav-cta">Book a Session</a>
  <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">&#9789;</button>
  <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
</nav>

<div class="prof-container">
  {breadcrumb_html}

  {render_profile_toc(c)}

  <div class="prof-jump-row">
    <div class="prof-jump">
      <label for="profJumpSelect">Jump to:</label>
      <select id="profJumpSelect" data-state="{state_code}" data-current-slug="{c.get('slug','')}">
        <option value="">Loading {state_name} officials…</option>
      </select>
    </div>
    {render_share_button(c)}
  </div>

  {prevnext_bar}

  <div class="prof-header">
    <div class="prof-header-row">
      {photo_html}
      <div class="prof-header-text">
        <div class="prof-jurisdiction">{c['jurisdiction']}</div>
        <h1 class="prof-name">{c['name']}</h1>
        <div class="prof-office">{c['office']}</div>
        <span class="prof-party {party_class(c['party'])}">{party_label(c['party'])}</span>
        {f'<a href="{website}" target="_blank" rel="noopener" style="margin-left:12px;color:var(--accent);font-size:0.85rem;">Campaign Website &rarr;</a>' if website else ''}
      </div>
    </div>
    {status_banner_html}
    {confidence_chip_html}
    {candidacy_banner_html}
    {map_link_html}
    {civic_tool_html}
    {civic_voting_html}
  </div>

  <div id="prof-score" class="prof-total">
    <div class="prof-total-main">
      <div class="prof-total-label">RESOLUTE Citizen Score</div>
      <div class="prof-total-headline">
        <span class="prof-total-score" style="color:{total_color};" title="{thin_score_title}">{pct_of_max}</span>
        <span class="prof-total-max" title="Uniform /100 display scale — every official is shown on the same 100-point visual whether they're scored on 22, 43, or 50 questions. The underlying math is unchanged: {adjusted_score} earned of {max_possible} dynamic max (2 pts × {answered_count} answered).">/ 100</span>
        <span class="prof-grade" style="color:{total_color};border-color:{total_color};" aria-label="{grade_aria}">{grade_letter}</span>
      </div>
      <div class="prof-total-detail">
        <span class="prof-raw" title="Raw dynamic-max number: 2 points × {answered_count} answered questions. Federal officials max out at /100 when all 50 questions are scored. State officials max out at /86 (43 applicable × 2). Local officials max out at /44 (22 applicable × 2). The headline above normalizes all of these to a uniform /100 visual; this caption keeps the raw integer for transparency.">Raw: <strong>{adjusted_score}</strong> of <strong>{max_possible}</strong> dynamic max</span>
        &middot; <span class="prof-answered" title="Number of questions with researched public-record evidence. Out of {applicable_total} applicable at this office tier (or 50 total if federal). The remaining are unanswered — see scoring-system.html for methodology.">{answered_count} of {applicable_total} answered</span>
        {_adj_section_html}
      </div>
      {tier_callout_html}
      {f'<div class="prof-freshness" title="Data freshness source: {freshness_source}">Last verified: <time datetime="{freshness_date}">{freshness_date}</time>{" · from claim evidence" if freshness_source == "claim" else " · scorecard-level timestamp"}</div>' if freshness_date else ''}
    </div>
    <div class="prof-total-right">
      <div class="prof-subtotals" aria-label="Subtotals — God First {gf_score} of {max_god}, {pillar_b_label} {af_score} of {max_gov}">
        <div class="prof-sub prof-sub-gf" title="{god_title}">
          <span class="prof-sub-label">&#10013; God First</span>
          <span class="prof-sub-val" style="color:{gf_color};">{gf_score}<span class="prof-sub-max">/ {max_god}</span></span>
        </div>
        <div class="prof-sub prof-sub-af" title="{pillar_b_title}">
          <span class="prof-sub-label">{pillar_b_emoji} {pillar_b_label}</span>
          <span class="prof-sub-val" style="color:{af_color};">{af_score}<span class="prof-sub-max">/ {max_gov}</span></span>
        </div>
      </div>
      <div class="prof-total-bar" aria-hidden="true">
        <div class="prof-total-fill" style="width:{bar_width}%;background:{total_color};"></div>
      </div>
    </div>
  </div>

  {render_rank_callout(c, meta)}

  {render_church_affiliation_block(c)}

  {render_adjustments_block(adj_lines, total['score'], adjusted_score) if adj_lines else ''}

  {contact_html}

  {election_html}

  {f"""<div class="prof-details">
    <h2>Official Profile</h2>
    {profile_html}
    {f'<div class="prof-notes">{notes}</div>' if notes else ''}
  </div>""" if profile_html or notes else ''}

  <h2 id="prof-categories" style="color:var(--accent);font-family:var(--font-main);margin-bottom:16px;">Category Breakdown</h2>
  {cat_html}

  {sources_html}

  {render_references_section()}

  {f"""<div id="scoring-rationale" class="prof-rationale" role="note">
    <h2>Scoring rationale</h2>
    <p>{scoring_rationale}</p>
    <p class="prof-rationale-footnote">This record was seeded from the {c.get('jurisdiction','')} roster using the RESOLUTE Citizen party-default heuristic, documented in <a href="https://github.com/adamljohns/usmcmin-com/blob/main/seed-state-assemblies.py" target="_blank" rel="noopener">seed-state-assemblies.py</a>. Individual voting-record review is pending; when specific claims are promoted via the apply-claims.py pipeline, this confidence label will update and the per-claim evidence will surface in the category breakdown above. If you have evidence that a specific answer above is wrong, please file a dispute using the form below.</p>
  </div>""" if confidence == 'party_default' else ''}

  <!-- Bottom prev/next -->
  {prevnext_bar}

  <!-- Feedback Form -->
  <div id="feedback" class="prof-feedback" style="padding:20px 24px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);margin-top:16px;scroll-margin-top:80px;">
    <h2 style="color:var(--accent);font-size:1rem;margin-bottom:8px;">Have Information About This Official?</h2>
    <p style="color:var(--gray);font-size:0.82rem;margin-bottom:14px;line-height:1.6;">Help us improve this scorecard. If you have evidence of this official's positions — voting records, social media posts, public statements, or corrections — submit it below and we'll review and update the profile.</p>
    <div id="feedbackDisputeBanner" style="display:none;padding:10px 12px;margin-bottom:10px;background:rgba(227,182,98,0.12);border:1px solid rgba(227,182,98,0.4);border-radius:6px;color:#e3b662;font-size:0.82rem;line-height:1.5;">
      You are disputing claim <code id="feedbackClaimId"></code>. Please describe the issue and link to the primary source that contradicts it.
    </div>
    <form id="feedbackForm" style="display:flex;flex-direction:column;gap:10px;">
      <input type="hidden" name="candidate_name" value="{c['name']}">
      <input type="hidden" name="candidate_slug" value="{c.get('slug', '')}">
      <input type="hidden" name="candidate_state" value="{c.get('state', '')}">
      <input type="hidden" name="candidate_office" value="{c.get('office', '')}">
      <input type="hidden" name="page_url" id="feedbackPageUrl" value="">
      <input type="hidden" name="submitted_at" id="feedbackSubmittedAt" value="">
      <input type="hidden" name="dispute_claim_id" id="feedbackClaimIdHidden" value="">
      <input type="hidden" name="dispute_claim_text" id="feedbackClaimTextHidden" value="">
      <input type="hidden" name="dispute_claim_category" id="feedbackClaimCategoryHidden" value="">
      <input type="hidden" name="form_opened_at" id="feedbackFormOpenedAt" value="">
      <div id="feedbackReasonRow" style="display:none;flex-direction:column;gap:4px;">
        <label for="feedbackReason" style="font-size:0.78rem;color:var(--gray);">Why are you disputing this claim?</label>
        <select name="dispute_reason" id="feedbackReason" style="padding:10px 14px;background:var(--bg-dark,#0A0A0A);border:1px solid var(--border);border-radius:8px;color:var(--white);font-size:0.9rem;">
          <option value="">Select a reason…</option>
          <option value="factual_error">Factual error — the claim misrepresents what happened</option>
          <option value="outdated">Outdated — the situation has changed materially</option>
          <option value="missing_context">Missing context — technically true but misleading</option>
          <option value="misattribution">Misattribution — wrong person, wrong vote, wrong bill</option>
          <option value="source_broken">Source is broken or points at the wrong page</option>
          <option value="other">Other (explain below)</option>
        </select>
      </div>
      <!-- Honeypot: bots love empty fields named like they matter. Humans leave it empty. -->
      <input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;top:-9999px;opacity:0;height:0;width:0;" value="">
      <input type="text" name="submitter_name" placeholder="Your name" required style="padding:10px 14px;background:var(--bg-dark,#0A0A0A);border:1px solid var(--border);border-radius:8px;color:var(--white);font-size:0.9rem;">
      <input type="email" name="submitter_email" placeholder="Your email" required style="padding:10px 14px;background:var(--bg-dark,#0A0A0A);border:1px solid var(--border);border-radius:8px;color:var(--white);font-size:0.9rem;">
      <textarea name="feedback" rows="4" placeholder="What should we know? Include links to sources if possible..." required style="padding:10px 14px;background:var(--bg-dark,#0A0A0A);border:1px solid var(--border);border-radius:8px;color:var(--white);font-size:0.9rem;resize:vertical;"></textarea>
      <button type="submit" id="feedbackSubmitBtn" style="background:linear-gradient(90deg,#c9a84c,#D4AF37);color:#000;font-weight:700;font-size:0.9rem;padding:11px 22px;border-radius:8px;border:none;cursor:pointer;align-self:flex-start;">Submit Feedback</button>
    </form>
    <div id="feedbackSuccess" style="display:none;padding:14px;background:rgba(76,175,80,.15);border:1px solid #4CAF50;border-radius:8px;color:#7edd80;margin-top:12px;font-size:0.88rem;">Thank you! We'll review your submission and update the profile if verified.</div>
  </div>
  <script>
  (function(){{
    // Record when the form was rendered so the submit handler can
    // check the minimum human-interaction time (honeypot timing).
    var openedAt = Date.now();
    var openedAtField = document.getElementById('feedbackFormOpenedAt');
    if (openedAtField) openedAtField.value = String(openedAt);
    var pageUrlField = document.getElementById('feedbackPageUrl');
    if (pageUrlField) pageUrlField.value = window.location.href;

    // If the URL carries ?claim=... treat this visit as a claim-dispute.
    // Pre-populate the textarea with the claim's text and expose the
    // claim id + verbatim text + category as hidden fields for the
    // reviewer's triage. Capturing the claim text at dispute time is
    // important: the underlying claim can be edited later; the dispute
    // record should remember what the disputer actually saw.
    var params = new URLSearchParams(window.location.search);
    var claimId = params.get('claim');
    if (claimId) {{
      var banner = document.getElementById('feedbackDisputeBanner');
      var badge = document.getElementById('feedbackClaimId');
      var hidden = document.getElementById('feedbackClaimIdHidden');
      var textHidden = document.getElementById('feedbackClaimTextHidden');
      var catHidden = document.getElementById('feedbackClaimCategoryHidden');
      var reasonRow = document.getElementById('feedbackReasonRow');
      var submitBtn = document.getElementById('feedbackSubmitBtn');
      var successBox = document.getElementById('feedbackSuccess');
      var textarea = document.querySelector('#feedbackForm textarea[name="feedback"]');
      if (banner) banner.style.display = 'block';
      if (badge) badge.textContent = claimId;
      if (hidden) hidden.value = claimId;
      if (reasonRow) reasonRow.style.display = 'flex';
      if (submitBtn) submitBtn.textContent = 'Submit Dispute';
      if (successBox) successBox.textContent = 'Dispute received. We will review the claim and publish the outcome in the scorecard changelog. Thank you for strengthening the audit trail.';
      var claimEl = document.getElementById(claimId);
      var claimTextEl = claimEl && claimEl.querySelector('.prof-q-claim-text');
      var claimText = (claimTextEl && claimTextEl.textContent.trim()) || '';
      if (textHidden) textHidden.value = claimText;
      // Derive category from the claim id if it follows the
      // "<slug>-<category>-<idx>" pattern (per our schema convention).
      if (catHidden) {{
        var parts = claimId.split('-');
        // Best-effort: everything except the leading "<slug>" and
        // trailing numeric index. Leaves intact categories like
        // "self_defense" and "christian_heritage".
        if (parts.length >= 3) {{
          var tail = parts[parts.length - 1];
          if (/^\\d+$/.test(tail)) {{
            catHidden.value = parts.slice(1, parts.length - 1).join('-');
          }}
        }}
      }}
      if (textarea) {{
        var prefill = 'Disputing claim ' + claimId + ':';
        if (claimText) prefill += '\\n> ' + claimText;
        prefill += '\\n\\nMy concern (please cite a primary source):\\n';
        textarea.value = prefill;
        var details = claimEl && claimEl.closest('details');
        if (details) details.open = true;
      }}
    }}
  }})();
  document.getElementById('feedbackForm').addEventListener('submit',function(e){{
    e.preventDefault();
    var fd = new FormData(this);
    // Honeypot: bots fill every text field. Humans leave the off-screen
    // "website" input empty. Abort silently on non-empty to avoid
    // telling the bot it was caught.
    if ((fd.get('website') || '').toString().trim() !== '') {{
      document.getElementById('feedbackForm').style.display='none';
      document.getElementById('feedbackSuccess').style.display='block';
      return;
    }}
    // Timing check: reject submissions made <3 seconds after the form
    // was rendered. Even skim-reading the context takes longer.
    var openedAt = Number(document.getElementById('feedbackFormOpenedAt').value || '0');
    if (openedAt && (Date.now() - openedAt) < 3000) {{
      alert('That felt fast — if you are human, please take a moment to review and resubmit.');
      return;
    }}
    document.getElementById('feedbackSubmittedAt').value = new Date().toISOString();
    fd.set('submitted_at', document.getElementById('feedbackSubmittedAt').value);
    var claimId = document.getElementById('feedbackClaimIdHidden').value;
    var subjectPrefix = claimId ? 'RESOLUTE Citizen DISPUTE (' + claimId + '): ' : 'RESOLUTE Citizen Feedback: ';
    fd.append('_subject', subjectPrefix + '{c["name"]}');
    fd.append('_template','table');
    fd.append('_captcha','false');
    fetch('https://formsubmit.co/ajax/usmcministries2022@gmail.com',{{method:'POST',body:fd}})
    .then(function(res){{
      if(!res.ok) throw new Error('Server error');
      document.getElementById('feedbackForm').style.display='none';
      document.getElementById('feedbackSuccess').style.display='block';
    }})
    .catch(function(){{
      alert('Failed to submit. Please check your connection and try again.');
    }});
  }});
  </script>
</div>

<footer>
  <p><strong>RESOLUTE Citizen</strong> &mdash; a module of <a href="https://usmcmin.org">U.S.M.C. Ministries</a></p>
  <p style="margin-top:6px;font-size:0.72rem;">Each True = +2 points &middot; Max {MAX_TOTAL} &middot; Primary sources only &middot; <a href="https://usmcmin.org/bible.html?ref=Proverbs+29:2">Proverbs 29:2</a></p>
  <p style="margin-top:6px;font-size:0.7rem;"><span id="pageViews"></span></p>
</footer>
<script src="../../assets/js/profile.min.js" defer></script>
<script data-goatcounter="https://usmcmin.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<noscript><img src="https://usmcmin.goatcounter.com/count?p=/candidates/{c.get('state','').lower()}/{c.get('slug','')}" alt=""></noscript>
</body>
</html>'''

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data', 'scorecard.json')
    candidates_dir = os.path.join(base_dir, 'candidates')

    os.makedirs(candidates_dir, exist_ok=True)

    with open(data_path, 'r') as f:
        data = json.load(f)

    categories = data['categories']
    meta = data['meta']

    # Load elections.json once and attach to meta so build_election_html can
    # read it via closure through the meta arg passed to generate_profile.
    elections_path = os.path.join(base_dir, 'data', 'elections.json')
    if os.path.exists(elections_path):
        with open(elections_path, 'r') as f:
            meta = dict(meta)  # don't mutate the scorecard's own meta
            meta['_elections_data'] = json.load(f)

    count = 0
    states_seen = set()

    # Build navigation map once: for each candidate id, know prev/next peers
    # within the same (state, level, jurisdiction) group, ordered by score desc.
    nav_map = compute_nav_groups(data['candidates'], categories)

    # Precompute national rank table — candidate.slug → (rank, total_scored,
    # percentile_top). Used by the "where this candidate ranks" callout.
    # Only ranks candidates with at least one scored answer (no point in
    # ranking 8,000 zeroes against each other — the rank would be ~halfway
    # for everyone and meaningless).
    rank_rows = []
    for c in data['candidates']:
        scores = c.get('scores') or {}
        any_scored = any(isinstance(v, list) and any(a is not None for a in v) for v in scores.values())
        if not any_scored:
            continue
        tot = calc_total(scores, categories, classify_office_tier(c) or 'federal')['score']
        adj = sum((info.get('delta') or 0) for info in ((c.get('profile') or {}).get('score_adjustments') or {}).values())
        rank_rows.append((c.get('slug'), tot + adj))
    rank_rows.sort(key=lambda r: -r[1])  # descending
    rank_map = {}
    total_ranked = len(rank_rows)
    for i, (slug, _) in enumerate(rank_rows):
        rank_map[slug] = (i + 1, total_ranked)
    meta['_rank_map'] = rank_map

    for candidate in data['candidates']:
        slug = candidate.get('slug', '')
        if not slug:
            continue
        state = (candidate.get('state', 'VA') or 'VA').lower()
        states_seen.add(state)
        state_dir = os.path.join(candidates_dir, state)
        os.makedirs(state_dir, exist_ok=True)
        nav = nav_map.get(candidate.get('id'))
        html = generate_profile(candidate, categories, meta, nav=nav)
        filepath = os.path.join(state_dir, f'{slug}.html')
        with open(filepath, 'w') as f:
            f.write(html)
        count += 1

    print(f'Generated {count} candidate profile pages across {len(states_seen)} states: {", ".join(sorted(states_seen))}')

if __name__ == '__main__':
    main()
