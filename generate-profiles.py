#!/usr/bin/env python3
"""Generate individual candidate profile pages from scorecard.json"""
import json
import os

import source_bias as sb

POINTS_PER_TRUE = 2
MAX_PER_TOPIC = 10
MAX_TOTAL = 70

def calc_cat_score(answers):
    if not answers:
        return {'score': 0, 'raw': 0, 'answered': 0}
    raw = sum(1 for a in answers if a is True)
    answered = sum(1 for a in answers if a is not None)
    return {'score': raw * POINTS_PER_TRUE, 'raw': raw, 'answered': answered}

def calc_total(scores, categories):
    total = 0
    answered = 0
    for cat in categories:
        cs = calc_cat_score(scores.get(cat['id'], []))
        total += cs['score']
        answered += cs['answered']
    return {'score': total, 'answered': answered}

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

    html = f'<div class="prof-election prof-election-{banner_class}">'
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

    html = '<div class="prof-contact">'
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
        t = calc_total(c.get('scores', {}), categories)
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
    total = calc_total(c['scores'], categories)
    total_color = score_color(total['score'], MAX_TOTAL)
    bar_width = round((total['score'] / MAX_TOTAL) * 100) if MAX_TOTAL > 0 else 0
    profile = c.get('profile', {}) or {}

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
    DETAILED_MAP_STATES = ('VA', 'FL', 'TX')
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
        candidacy_banner_html = (
            '<div class="prof-candidacy-banner" role="note" aria-label="Candidacy status">'
            f'<span class="prof-candidacy-chip {chip_class}">{chip_label}</span>'
            '<div class="prof-candidacy-text">'
            f'Currently running for <strong>{cand.get("office","")}</strong>'
            f'{decl_str}. {date_str}.'
            f' <a href="../../compare.html?race={cand.get("race_id")}">'
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
        photo_html = f'<img class="prof-photo" src="../../{photo_path}" alt="{c["name"]}" loading="lazy">'
    else:
        badge_bg, badge_fg = color_for_slug(c.get('slug', ''))
        badge_text = initials(c['name'])
        photo_html = (
            f'<div class="prof-photo prof-initials" '
            f'style="background:{badge_bg};color:{badge_fg};" '
            f'aria-hidden="true">{badge_text}</div>'
        )

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

    cat_html = ''
    for cat in categories:
        cs = calc_cat_score(c['scores'].get(cat['id'], []))
        color = score_color(cs['score'], MAX_PER_TOPIC) if cs['answered'] > 0 else '#666'
        pet_cat = PETITION_CAT_MAP.get(cat['id'])
        pet_state = (c.get('state') or '').upper() if c.get('state') else ''
        petition_btn = ''
        if pet_cat and pet_state and pet_state not in ('US',):
            petition_btn = (
                f'<a class="prof-cat-petition" '
                f'href="../../petition.html?state={pet_state}&cat={pet_cat}" '
                f'aria-label="Draft a petition to your {pet_state} reps about {cat["label"]}" '
                f'title="Draft a petition to your {pet_state} reps about {cat["label"]}">'
                '&#9993;&#xFE0F; Petition your reps'
                '</a>'
            )
        elif pet_cat:
            # US-level candidates (e.g., POTUS, SCOTUS) — still offer petition
            # without a specific state; petition.html will require state input.
            petition_btn = (
                f'<a class="prof-cat-petition" '
                f'href="../../petition.html?cat={pet_cat}" '
                f'aria-label="Draft a petition to your reps about {cat["label"]}" '
                f'title="Draft a petition to your reps about {cat["label"]}">'
                '&#9993;&#xFE0F; Petition your reps'
                '</a>'
            )
        cat_html += f'''
    <div class="prof-category">
      <div class="prof-cat-header">
        <img src="../../assets/icons/{cat['icon']}" alt="" width="24" height="24">
        <h3>{cat['label']}</h3>
        <span class="prof-cat-score" style="color:{color};">{cs['score']}/{MAX_PER_TOPIC}</span>
        {petition_btn}
      </div>
      <div class="prof-questions">'''
        questions = cat.get('questions', [])
        answers = c['scores'].get(cat['id'], [None]*5)
        for i, q in enumerate(questions):
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
        sources_html = '<div class="prof-sources"><h2>Sources &amp; Evidence</h2>'
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

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['name']} — RESOLUTE Citizen Scorecard | U.S.M.C. Ministries</title>
  <meta name="description" content="RESOLUTE Citizen Scorecard for {c['name']} ({party_label(c['party'])}). {c['office']}, {c['jurisdiction']}. Score: {total['score']}/{MAX_TOTAL}.">
  <link rel="stylesheet" href="../../assets/css/main.css">
  <link rel="icon" href="../../assets/img/favicon.png" type="image/png">
  <style>
    .prof-container {{ max-width: 900px; margin: 0 auto; padding: 20px; }}
    .prof-back {{ display: inline-block; color: var(--accent); text-decoration: none; font-size: 0.85rem; margin-bottom: 20px; }}
    .prof-back:hover {{ text-decoration: underline; }}

    /* Breadcrumb */
    .prof-breadcrumb {{
      font-size: 0.78rem;
      color: var(--gray);
      margin-bottom: 14px;
      line-height: 1.6;
      word-break: break-word;
    }}
    .prof-breadcrumb a {{
      color: var(--accent);
      text-decoration: none;
    }}
    .prof-breadcrumb a:hover {{ text-decoration: underline; }}
    .prof-breadcrumb .crumb-sep {{ color: var(--gray); margin: 0 2px; opacity: 0.6; }}
    .prof-breadcrumb .crumb-current {{ color: var(--white); font-weight: 600; }}

    /* Jump-to dropdown */
    .prof-jump {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 18px;
      flex-wrap: wrap;
    }}
    .prof-jump label {{
      font-size: 0.78rem;
      color: var(--gray);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .prof-jump select {{
      flex: 1;
      min-width: 220px;
      padding: 8px 12px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 6px;
      color: var(--white);
      font-size: 0.85rem;
      cursor: pointer;
    }}
    .prof-jump select:hover {{ border-color: var(--accent); }}

    /* Prev / Next nav bar */
    .prof-nav-bar {{
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: stretch;
      gap: 10px;
      margin: 18px 0;
    }}
    .prof-nav-btn {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 12px 14px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      color: var(--white);
      text-decoration: none;
      font-size: 0.82rem;
      line-height: 1.3;
      min-height: 54px;
      transition: border-color 0.15s, background 0.15s;
    }}
    .prof-nav-btn:hover {{
      border-color: var(--accent);
      background: rgba(212,175,55,0.06);
    }}
    .prof-nav-btn[data-direction="next"] {{
      justify-content: flex-end;
      text-align: right;
      flex-direction: row-reverse;
    }}
    .prof-nav-btn.prof-nav-disabled {{
      opacity: 0.35;
      cursor: default;
      pointer-events: none;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--gray);
    }}
    .prof-nav-arrow {{
      font-weight: 700;
      color: var(--accent);
      flex-shrink: 0;
    }}
    .prof-nav-text {{
      display: flex;
      flex-direction: column;
      gap: 2px;
      overflow: hidden;
    }}
    .prof-nav-name {{
      font-weight: 600;
      color: var(--white);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .prof-nav-office {{
      font-size: 0.72rem;
      color: var(--gray);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .prof-nav-position {{
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 10px 16px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      font-size: 0.78rem;
      color: var(--gray);
      text-align: center;
      white-space: nowrap;
    }}
    @media (max-width: 640px) {{
      .prof-nav-bar {{
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto;
      }}
      .prof-nav-position {{
        grid-column: 1 / -1;
        order: -1;
      }}
    }}

    /* Photo / initials */
    .prof-header-row {{
      display: flex;
      gap: 20px;
      align-items: flex-start;
    }}
    .prof-header-row .prof-header-text {{ flex: 1; min-width: 0; }}
    .prof-photo {{
      width: 96px;
      height: 96px;
      border-radius: 50%;
      flex-shrink: 0;
      object-fit: cover;
      border: 2px solid var(--border);
    }}
    .prof-initials {{
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-main);
      font-size: 2rem;
      font-weight: 800;
      letter-spacing: 1px;
      user-select: none;
    }}
    @media (max-width: 520px) {{
      .prof-header-row {{ flex-direction: column; align-items: center; text-align: center; }}
      .prof-photo {{ width: 80px; height: 80px; }}
      .prof-initials {{ font-size: 1.7rem; }}
    }}

    .prof-header {{
      padding: 32px 24px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 24px;
    }}
    .prof-jurisdiction {{
      font-size: 0.72rem;
      color: var(--accent);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 8px;
    }}
    .prof-name {{
      font-size: clamp(1.6rem, 4vw, 2.4rem);
      color: var(--white);
      margin-bottom: 6px;
      font-weight: 800;
    }}
    .prof-office {{
      font-size: 1rem;
      color: var(--gray);
      margin-bottom: 12px;
    }}
    .prof-party {{
      display: inline-block;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 6px;
    }}
    .party-r {{ background: rgba(220,38,38,0.15); color: #ef4444; border: 1px solid rgba(220,38,38,0.3); }}
    .party-d {{ background: rgba(37,99,235,0.15); color: #3b82f6; border: 1px solid rgba(37,99,235,0.3); }}
    .party-i {{ background: rgba(168,85,247,0.15); color: #a855f7; border: 1px solid rgba(168,85,247,0.3); }}
    .party-unknown {{ background: rgba(107,114,128,0.15); color: #9ca3af; border: 1px solid rgba(107,114,128,0.3); }}

    /* Election / countdown block */
    .prof-election {{
      display: grid;
      grid-template-columns: minmax(220px, 1fr) 1.2fr;
      gap: 18px;
      padding: 18px 22px;
      border-radius: var(--radius);
      margin-bottom: 20px;
      border: 1px solid var(--border);
    }}
    .prof-election-seat-up {{
      background: linear-gradient(135deg, rgba(76,175,80,0.10) 0%, rgba(201,168,76,0.10) 100%);
      border-left: 4px solid #c9a84c;
    }}
    .prof-election-seat-safe {{
      background: var(--bg-card);
      border-left: 4px solid var(--border);
      opacity: 0.92;
    }}
    .prof-election-main {{ display: flex; flex-direction: column; gap: 4px; }}
    .prof-election-label {{
      font-size: 0.7rem;
      color: #c9a84c;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      font-weight: 700;
    }}
    .prof-election-date {{
      font-size: 1.35rem;
      color: var(--white);
      font-weight: 800;
      font-family: var(--font-main);
    }}
    .prof-election-type {{
      font-size: 0.82rem;
      color: var(--gray);
      margin-bottom: 4px;
    }}
    .prof-election-countdown {{
      font-size: 1.1rem;
      color: var(--white);
      margin-top: 4px;
    }}
    .prof-election-countdown span:first-child {{
      font-weight: 800;
      color: #c9a84c;
      font-size: 1.5rem;
    }}
    .prof-election-countdown .cd-label {{
      color: var(--gray);
      font-size: 0.85rem;
    }}
    .prof-election-side {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 0.82rem;
      color: var(--gray);
      line-height: 1.5;
      border-left: 1px dashed var(--border);
      padding-left: 16px;
    }}
    .prof-election-side a {{ color: var(--accent); text-decoration: none; }}
    .prof-election-side a:hover {{ text-decoration: underline; }}
    .prof-election-side strong {{ color: var(--white); font-weight: 600; }}
    @media (max-width: 640px) {{
      .prof-election {{
        grid-template-columns: 1fr;
        gap: 10px;
      }}
      .prof-election-side {{
        border-left: none;
        padding-left: 0;
        border-top: 1px dashed var(--border);
        padding-top: 12px;
      }}
    }}

    /* Contact block */
    .prof-contact {{
      padding: 20px 24px;
      background: linear-gradient(135deg, rgba(201,168,76,0.10) 0%, rgba(30,58,95,0.06) 100%);
      border: 1px solid rgba(201,168,76,0.3);
      border-radius: var(--radius);
      margin-bottom: 24px;
    }}
    .prof-contact h2 {{
      color: #c9a84c;
      font-size: 1.05rem;
      margin-bottom: 14px;
      font-family: var(--font-main);
      letter-spacing: 0.3px;
    }}
    .prof-contact-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 10px;
    }}
    .prof-contact-btn {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 11px 14px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--white);
      text-decoration: none;
      font-size: 0.85rem;
      transition: border-color 0.15s, background 0.15s, transform 0.1s;
    }}
    .prof-contact-btn:hover {{
      border-color: #c9a84c;
      background: rgba(201,168,76,0.06);
      transform: translateY(-1px);
    }}
    .prof-contact-icon {{
      font-size: 1.25rem;
      flex-shrink: 0;
      filter: saturate(1.1);
    }}
    .prof-contact-text {{
      display: flex;
      flex-direction: column;
      gap: 2px;
      min-width: 0;
      flex: 1;
    }}
    .prof-contact-label {{
      font-size: 0.7rem;
      color: var(--gray);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      font-weight: 600;
    }}
    .prof-contact-value {{
      font-size: 0.88rem;
      color: var(--white);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .prof-contact-note {{
      font-size: 0.78rem;
      color: var(--gray);
      margin-top: 10px;
      padding-top: 10px;
      border-top: 1px dashed var(--border);
      line-height: 1.5;
    }}
    .prof-contact-tagline {{
      font-size: 0.72rem;
      color: var(--gray);
      margin-top: 8px;
      font-style: italic;
      line-height: 1.5;
    }}
    .prof-contact-tagline em {{
      color: rgba(201,168,76,0.8);
      font-style: italic;
    }}

    /* District offices (collapsible) */
    .prof-district-details {{
      margin-top: 12px;
      padding-top: 10px;
      border-top: 1px dashed var(--border);
      font-size: 0.82rem;
    }}
    .prof-district-details summary {{
      cursor: pointer;
      color: #c9a84c;
      font-weight: 600;
      padding: 4px 0;
      outline: none;
      user-select: none;
    }}
    .prof-district-details summary:hover {{ text-decoration: underline; }}
    .prof-district-details[open] summary {{ margin-bottom: 8px; }}
    .prof-district-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      padding-left: 6px;
      border-left: 2px solid rgba(201,168,76,0.25);
      padding-top: 2px;
    }}
    .prof-district-office {{
      color: var(--gray);
      line-height: 1.55;
      padding: 4px 8px;
    }}
    .prof-district-office strong {{
      color: var(--white);
      margin-right: 6px;
    }}
    .prof-district-office a {{
      color: var(--accent);
      text-decoration: none;
    }}
    .prof-district-office a:hover {{ text-decoration: underline; }}

    .prof-sources {{
      padding: 16px 24px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-top: 16px;
    }}
    .prof-sources h2 {{
      color: var(--accent);
      font-size: 1rem;
      margin-bottom: 10px;
      font-family: var(--font-main);
    }}
    .prof-source-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .prof-source-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .prof-sources a {{
      color: var(--accent);
      text-decoration: none;
      font-size: 0.82rem;
      word-break: break-all;
      flex: 1 1 auto;
      min-width: 0;
    }}
    .prof-sources a:hover {{ text-decoration: underline; }}
    .prof-bias-chip {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 10px;
      font-size: 0.64rem;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      font-weight: 700;
      white-space: nowrap;
      flex: 0 0 auto;
      border: 1px solid transparent;
    }}
    .prof-bias-left       {{ background: #1d4ed8; color: #fff; }}
    .prof-bias-lean-left  {{ background: #60a5fa; color: #0b1220; }}
    .prof-bias-center     {{ background: #9ca3af; color: #0b1220; }}
    .prof-bias-lean-right {{ background: #f87171; color: #2b0a0a; }}
    .prof-bias-right      {{ background: #b91c1c; color: #fff; }}
    .prof-bias-official   {{ background: #0e7490; color: #fff; }}
    .prof-bias-reference  {{ background: #475569; color: #fff; }}
    .prof-bias-social     {{ background: #334155; color: #cbd5e1; border-color: #475569; }}
    .prof-bias-neutral    {{ background: #1f2937; color: #cbd5e1; border-color: #374151; }}
    .prof-source-diversity {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 12px;
      padding-bottom: 12px;
      border-bottom: 1px dashed var(--border);
    }}
    .prof-div-chip {{
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.4px;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    .prof-bias-attribution {{
      margin-top: 10px;
      padding-top: 10px;
      border-top: 1px solid var(--border);
      font-size: 0.7rem;
      color: var(--text-muted, #94a3b8);
      line-height: 1.5;
    }}
    .prof-bias-attribution a {{
      color: var(--text-muted, #94a3b8);
      text-decoration: underline;
      display: inline;
      font-size: inherit;
      word-break: normal;
    }}

    .prof-total {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 20px 24px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 24px;
    }}
    .prof-total-score {{
      font-size: 2.4rem;
      font-weight: 800;
    }}
    .prof-total-max {{
      font-size: 1rem;
      color: var(--gray);
    }}
    .prof-total-bar {{
      flex: 1;
      height: 10px;
      background: var(--border);
      border-radius: 5px;
      overflow: hidden;
    }}
    .prof-total-fill {{
      height: 100%;
      border-radius: 5px;
      transition: width 0.4s;
    }}
    .prof-freshness {{
      margin-top: 6px;
      font-size: 0.72rem;
      color: var(--text-muted, #94a3b8);
      letter-spacing: 0.2px;
    }}
    .prof-confidence-banner {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-top: 12px;
      padding: 10px 14px;
      background: rgba(217, 119, 6, 0.08);
      border: 1px solid rgba(217, 119, 6, 0.35);
      border-radius: 8px;
    }}
    .prof-confidence-chip {{
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    .prof-conf-party-default {{ background: #b45309; color: #fff; }}
    .prof-conf-awaiting {{
      background: rgba(71, 85, 105, 0.1);
      border-color: rgba(71, 85, 105, 0.4);
    }}
    .prof-conf-awaiting-chip {{ background: #475569; color: #fff; }}
    .prof-conf-awaiting .prof-confidence-text {{ color: #94a3b8; }}
    .prof-conf-awaiting .prof-confidence-text a {{ color: #cbd5e1; }}

    /* Candidacy banner — "Running for X / Compare ->" */
    .prof-candidacy-banner {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 10px;
      padding: 12px 16px;
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 8px;
    }}
    .prof-candidacy-chip {{
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    .prof-cand-incumbent {{ background: #166534; color: #d1fae5; }}
    .prof-cand-challenger {{ background: #0369a1; color: #fff; }}
    .prof-candidacy-text {{
      flex: 1;
      font-size: 0.86rem;
      color: var(--white);
      line-height: 1.55;
      min-width: 220px;
    }}
    .prof-candidacy-text a {{
      color: #38bdf8;
      text-decoration: underline;
      font-weight: 600;
    }}

    .prof-map-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-top: 10px;
      padding: 6px 12px;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.4px;
      color: #5eead4;
      background: rgba(94, 234, 212, 0.08);
      border: 1px solid rgba(94, 234, 212, 0.35);
      border-radius: 16px;
      text-decoration: none;
    }}
    .prof-map-link:hover {{
      background: rgba(94, 234, 212, 0.18);
      color: #99f6e4;
      text-decoration: none;
    }}
    .prof-confidence-text {{
      font-size: 0.82rem;
      color: var(--text-muted, #d97706);
      line-height: 1.5;
    }}
    .prof-confidence-text a {{
      color: #fcd34d;
      text-decoration: underline;
      font-weight: 600;
    }}
    .prof-rationale {{
      margin-top: 18px;
      padding: 18px 22px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-left: 4px solid #b45309;
      border-radius: var(--radius);
      scroll-margin-top: 80px;
    }}
    .prof-rationale h2 {{
      font-size: 1rem;
      color: #fcd34d;
      margin-bottom: 8px;
      font-family: var(--font-main);
      letter-spacing: 0.3px;
    }}
    .prof-rationale p {{
      font-size: 0.86rem;
      color: var(--white);
      line-height: 1.65;
      margin-bottom: 10px;
    }}
    .prof-rationale p:last-child {{ margin-bottom: 0; }}
    .prof-rationale-footnote {{
      color: var(--text-muted, #94a3b8) !important;
      font-size: 0.78rem !important;
    }}
    .prof-rationale-footnote a {{ color: var(--accent); }}

    /* Per-answer footnote markers + References section (v3.4.0) */
    .prof-fn-sup {{
      font-size: 0.66rem;
      font-weight: 700;
      margin-left: 4px;
      letter-spacing: 0.3px;
    }}
    .prof-fn-sup .prof-fn-link {{
      color: var(--accent, #e3b662);
      text-decoration: none;
      padding: 0 2px;
    }}
    .prof-fn-sup .prof-fn-link:hover {{
      text-decoration: underline;
    }}
    .prof-fn-sup .prof-fn-link + .prof-fn-link::before {{ content: ""; }}
    .prof-fn-sup-lookup .prof-fn-link {{
      color: var(--text-muted, #94a3b8);
      opacity: 0.85;
    }}
    .prof-fn-sup-lookup::before {{
      content: "look up: ";
      font-size: 0.6rem;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      color: var(--text-muted, #94a3b8);
      margin-right: 3px;
      font-weight: 600;
    }}
    .prof-references {{
      margin-top: 18px;
      padding: 18px 22px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
    }}
    .prof-references h2 {{
      color: var(--accent);
      font-size: 1rem;
      margin-bottom: 8px;
      font-family: var(--font-main);
      letter-spacing: 0.3px;
    }}
    .prof-references-lead {{
      color: var(--gray);
      font-size: 0.82rem;
      line-height: 1.6;
      margin-bottom: 14px;
    }}
    .prof-fn-list {{
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .prof-fn-item {{
      display: flex;
      gap: 10px;
      align-items: flex-start;
      padding: 10px 12px;
      border-left: 3px solid var(--accent, #e3b662);
      background: rgba(255,255,255,0.02);
      border-radius: 0 6px 6px 0;
      scroll-margin-top: 80px;
    }}
    .prof-fn-item:target {{
      background: rgba(227,182,98,0.1);
      border-left-color: #fcd34d;
    }}
    .prof-fn-num {{
      font-family: "SF Mono", ui-monospace, monospace;
      color: var(--accent, #e3b662);
      font-weight: 700;
      font-size: 0.82rem;
      flex: 0 0 auto;
      padding-top: 2px;
    }}
    .prof-fn-body {{
      flex: 1 1 auto;
      min-width: 0;
    }}
    .prof-fn-title {{
      color: var(--white, #f5f5f5);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.88rem;
      line-height: 1.5;
      word-break: break-word;
    }}
    .prof-fn-title:hover {{
      text-decoration: underline;
      color: var(--accent, #e3b662);
    }}
    .prof-fn-meta {{
      margin-top: 4px;
      font-size: 0.75rem;
      color: var(--text-muted, #94a3b8);
      line-height: 1.5;
    }}
    .prof-fn-meta a {{
      color: var(--text-muted, #94a3b8);
      text-decoration: underline;
    }}
    .prof-fn-archive {{
      color: #9ca3af;
    }}
    .prof-fn-archive:hover {{
      color: var(--accent, #e3b662);
    }}
    .prof-fn-excerpt {{
      margin-top: 6px;
      padding: 6px 10px;
      border-left: 2px solid var(--border);
      color: var(--gray);
      font-size: 0.82rem;
      font-style: italic;
      line-height: 1.55;
    }}
    .prof-freshness time {{
      color: var(--accent, #e3b662);
      font-weight: 600;
    }}
    .prof-total-label {{
      font-size: 0.82rem;
      color: var(--gray);
      text-transform: uppercase;
      letter-spacing: 1px;
      font-weight: 600;
    }}

    .prof-details {{
      padding: 20px 24px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 24px;
    }}
    .prof-details h2 {{
      color: var(--accent);
      font-size: 1.1rem;
      margin-bottom: 12px;
      font-family: var(--font-main);
    }}
    .prof-detail {{
      font-size: 0.88rem;
      color: var(--gray);
      margin-bottom: 8px;
      line-height: 1.6;
    }}
    .prof-detail strong {{ color: var(--white); }}
    .prof-notes {{
      font-size: 0.88rem;
      color: var(--gray);
      line-height: 1.7;
      font-style: italic;
      margin-top: 12px;
      padding-top: 12px;
      border-top: 1px solid var(--border);
    }}

    .prof-category {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 16px;
      overflow: hidden;
    }}
    .prof-cat-header {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 14px 20px;
      border-bottom: 1px solid var(--border);
      flex-wrap: wrap;
    }}
    .prof-cat-header h3 {{
      flex: 1;
      color: var(--white);
      font-size: 1rem;
      font-family: var(--font-main);
    }}
    .prof-cat-score {{
      font-size: 1.3rem;
      font-weight: 700;
    }}
    .prof-cat-petition {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 4px 10px;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.3px;
      text-transform: uppercase;
      text-decoration: none;
      color: var(--accent, #e3b662);
      border: 1px solid rgba(227, 182, 98, 0.35);
      border-radius: 12px;
      transition: all 0.15s;
      white-space: nowrap;
    }}
    .prof-cat-petition:hover {{
      background: rgba(227, 182, 98, 0.12);
      border-color: var(--accent, #e3b662);
      text-decoration: none;
    }}
    .prof-cat-petition:focus-visible {{
      outline: 2px solid var(--accent, #e3b662);
      outline-offset: 2px;
    }}
    .prof-questions {{ padding: 0; }}
    .prof-q {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      padding: 10px 20px;
      border-bottom: 1px solid var(--border);
      gap: 16px;
    }}
    .prof-q:last-child {{ border-bottom: none; }}
    .prof-q-text {{
      flex: 1;
      font-size: 0.85rem;
      color: var(--gray);
      line-height: 1.5;
    }}
    .prof-q-answer {{
      font-size: 0.78rem;
      white-space: nowrap;
    }}
    .prof-q-claims {{
      flex-basis: 100%;
      margin-top: 4px;
      margin-left: 0;
      font-size: 0.82rem;
    }}
    .prof-q-claim-toggle {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      list-style: none;
      color: var(--accent, #e3b662);
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.3px;
      padding: 2px 0;
      outline: none;
    }}
    .prof-q-claim-toggle::-webkit-details-marker {{ display: none; }}
    .prof-q-claim-toggle::before {{
      content: "▸";
      font-size: 0.75rem;
      transition: transform 0.15s;
    }}
    .prof-q-claims[open] > .prof-q-claim-toggle::before {{
      transform: rotate(90deg);
    }}
    .prof-q-claim-i {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 16px;
      height: 16px;
      border: 1px solid currentColor;
      border-radius: 50%;
      font-family: Georgia, serif;
      font-style: italic;
      font-size: 0.7rem;
      font-weight: 700;
    }}
    .prof-q-claim-toggle:focus-visible {{
      outline: 2px solid var(--accent, #e3b662);
      outline-offset: 2px;
      border-radius: 4px;
    }}
    .prof-q-claim-list {{
      margin: 8px 0 4px 0;
      padding: 0;
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .prof-q-claim {{
      padding: 10px 12px;
      border-left: 3px solid var(--accent, #e3b662);
      background: rgba(255,255,255,0.02);
      border-radius: 0 6px 6px 0;
    }}
    .prof-q-claim-text {{
      margin: 0 0 8px 0;
      color: var(--white, #f5f5f5);
      line-height: 1.55;
    }}
    .prof-q-claim-src-list {{
      list-style: none;
      padding: 0;
      margin: 0 0 8px 0;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .prof-q-claim-src {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .prof-q-claim-src a {{
      color: var(--accent, #e3b662);
      text-decoration: none;
      word-break: break-all;
      font-size: 0.78rem;
    }}
    .prof-q-claim-src a:hover {{ text-decoration: underline; }}
    .prof-q-claim-meta {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      font-size: 0.7rem;
      color: var(--text-muted, #94a3b8);
    }}
    .prof-q-claim-badge {{
      padding: 2px 8px;
      border-radius: 10px;
      font-weight: 700;
      letter-spacing: 0.3px;
      text-transform: uppercase;
      font-size: 0.64rem;
    }}
    .prof-q-claim-badge.verified {{ background: #166534; color: #d1fae5; }}
    .prof-q-claim-badge.disputed {{ background: #78350f; color: #fed7aa; }}
    .prof-q-claim-dispute {{
      color: var(--text-muted, #94a3b8);
      text-decoration: underline;
    }}
    .prof-q-claim-dispute:hover {{
      color: var(--accent, #e3b662);
    }}

    footer {{
      text-align: center;
      padding: 30px 20px;
      color: var(--gray);
      font-size: 0.82rem;
      border-top: 1px solid var(--border);
      margin-top: 40px;
    }}
    footer a {{ color: var(--accent); text-decoration: none; }}

    @media (max-width: 600px) {{
      .prof-q {{ flex-direction: column; gap: 6px; }}
      .prof-total {{ flex-wrap: wrap; }}
    }}
  </style>
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
  <ul class="nav-links">
    <li><a href="../../mission.html">Mission</a></li>
    <li><a href="../../shop.html">Shop</a></li>
    <li><a href="../../books.html">Books</a></li>
    <li><a href="../../coaching.html">Coaching</a></li>
    <li><a href="../../fitness/fitness.html">Fitness</a></li>
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

  <div class="prof-jump">
    <label for="profJumpSelect">Jump to:</label>
    <select id="profJumpSelect" data-state="{state_code}" data-current-slug="{c.get('slug','')}">
      <option value="">Loading {state_name} officials…</option>
    </select>
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
    {confidence_chip_html}
    {candidacy_banner_html}
    {map_link_html}
  </div>

  <div class="prof-total">
    <div>
      <div class="prof-total-label">RESOLUTE Citizen Score</div>
      <div>
        <span class="prof-total-score" style="color:{total_color};">{total['score']}</span>
        <span class="prof-total-max">/ {MAX_TOTAL}</span>
      </div>
      {f'<div class="prof-freshness" title="Data freshness source: {freshness_source}">Last verified: <time datetime="{freshness_date}">{freshness_date}</time>{" · from claim evidence" if freshness_source == "claim" else " · scorecard-level timestamp"}</div>' if freshness_date else ''}
    </div>
    <div class="prof-total-bar">
      <div class="prof-total-fill" style="width:{bar_width}%;background:{total_color};"></div>
    </div>
  </div>

  {contact_html}

  {election_html}

  {f"""<div class="prof-details">
    <h2>Official Profile</h2>
    {profile_html}
    {f'<div class="prof-notes">{notes}</div>' if notes else ''}
  </div>""" if profile_html or notes else ''}

  <h2 style="color:var(--accent);font-family:var(--font-main);margin-bottom:16px;">Category Breakdown</h2>
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
<script>
(function(){{
  var p = window.location.pathname;
  fetch('https://usmcmin.goatcounter.com/counter/' + encodeURIComponent(p) + '.json')
    .then(function(r){{ return r.json(); }})
    .then(function(d){{
      var el = document.getElementById('pageViews');
      if (el && d && typeof d.count !== 'undefined') el.textContent = d.count + ' views';
    }})
    .catch(function(){{}});
}})();
</script>

<!-- Keyboard shortcuts: left/right = prev/next. Reads current hrefs from the
     DOM so that the sort-override pass below can update them and the keys
     follow automatically. -->
<script>
(function(){{
  document.addEventListener('keydown', function(e){{
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    var dir = e.key === 'ArrowLeft' ? 'prev' : 'next';
    var btn = document.querySelector('a.prof-nav-btn[data-direction="' + dir + '"]');
    if (btn && btn.href) {{ window.location.href = btn.href; }}
  }});
}})();
</script>

<!-- Jump-to dropdown + Prev/Next sort override.
     The static prev/next baked in at generation time walks (level, jurisdiction,
     score-desc). When the user has chosen a sort on the list page (?sort= or
     localStorage rc-sort), this script re-fetches the state JSON, recomputes
     the order across the entire state, and rewrites both nav-bars so prev/next
     follows the order the user just saw. No sort active = static order wins. -->
<script>
(function(){{
  var sel = document.getElementById('profJumpSelect');
  if (!sel) return;
  var st = (sel.getAttribute('data-state') || 'VA').toLowerCase();
  var currentSlug = sel.getAttribute('data-current-slug') || '';

  // ---- Score helpers (mirror server-side, no categories needed) ----
  // Per-state JSONs do not include the categories array, so we compute the
  // total directly by walking the keys of candidate.scores.
  var POINTS_PER_TRUE = 2;
  function calcTotal(scores){{
    if (!scores) return 0;
    var t = 0;
    for (var k in scores) {{
      if (!Object.prototype.hasOwnProperty.call(scores, k)) continue;
      var arr = scores[k] || [];
      for (var i = 0; i < arr.length; i++) {{
        if (arr[i] === true) t += POINTS_PER_TRUE;
      }}
    }}
    return t;
  }}

  var LEVEL_RANK = {{ executive: 1, judicial: 2, federal: 3, state: 4, local: 5 }};
  var PARTY_RANK = {{ R: 1, D: 2, I: 3 }};

  function makeComparator(sortKey){{
    function totalOf(c){{ return calcTotal(c.scores); }}
    function nameTie(a, b){{ return (a.name||'').toLowerCase().localeCompare((b.name||'').toLowerCase()); }}
    switch (sortKey) {{
      case 'score-asc':
        return function(a, b){{ return (totalOf(a) - totalOf(b)) || nameTie(a, b); }};
      case 'name':
        return nameTie;
      case 'level-score':
        return function(a, b){{
          return ((LEVEL_RANK[a.level]||6) - (LEVEL_RANK[b.level]||6))
              || (totalOf(b) - totalOf(a))
              || nameTie(a, b);
        }};
      case 'jurisdiction-score':
        return function(a, b){{
          return ((a.jurisdiction||'').toLowerCase().localeCompare((b.jurisdiction||'').toLowerCase()))
              || (totalOf(b) - totalOf(a))
              || nameTie(a, b);
        }};
      case 'party-score':
        return function(a, b){{
          return ((PARTY_RANK[a.party]||4) - (PARTY_RANK[b.party]||4))
              || (totalOf(b) - totalOf(a))
              || nameTie(a, b);
        }};
      case 'score-desc':
      default:
        return function(a, b){{ return (totalOf(b) - totalOf(a)) || nameTie(a, b); }};
    }}
  }}

  var SORT_LABELS = {{
    'score-desc': 'Score High → Low',
    'score-asc': 'Score Low → High',
    'name': 'Name A → Z',
    'level-score': 'Level + Score',
    'jurisdiction-score': 'Jurisdiction + Score',
    'party-score': 'Party + Score'
  }};

  function activeSort(){{
    var fromUrl = null;
    try {{ fromUrl = new URL(window.location).searchParams.get('sort'); }} catch(e) {{}}
    var fromStorage = null;
    try {{ fromStorage = localStorage.getItem('rc-sort'); }} catch(e) {{}}
    var v = fromUrl || fromStorage;
    return SORT_LABELS[v] ? v : null; // null = no override, keep static order
  }}

  function buildNavBtnHtml(neighbor, direction, arrow){{
    if (!neighbor) {{
      return '<span class="prof-nav-btn prof-nav-disabled">' + arrow + '</span>';
    }}
    var name = (neighbor.name || '').replace(/[<>]/g, '');
    var office = (neighbor.office || '').replace(/[<>]/g, '');
    var href = (neighbor.slug || '') + '.html';
    return '<a class="prof-nav-btn" href="' + href + '" data-direction="' + direction + '">'
      + '<span class="prof-nav-arrow">' + arrow + '</span>'
      + '<span class="prof-nav-text"><span class="prof-nav-name">' + name + '</span>'
      + '<span class="prof-nav-office">' + office + '</span></span></a>';
  }}

  function rerenderNav(prev, next, position, total, sortLabel){{
    var bars = document.querySelectorAll('.prof-nav-bar');
    var prevHtml = buildNavBtnHtml(prev, 'prev', '← Prev');
    var nextHtml = buildNavBtnHtml(next, 'next', 'Next →');
    var posHtml = '<div class="prof-nav-position">' + position + ' of ' + total
                + (sortLabel ? ' &middot; ' + sortLabel : '') + '</div>';
    bars.forEach(function(bar){{
      bar.innerHTML = prevHtml + posHtml + nextHtml;
    }});
  }}

  fetch('../../data/states/' + st + '.json')
    .then(function(r){{ return r.json(); }})
    .then(function(data){{
      var cands = (data && data.candidates) || [];

      // ---- Jump-to dropdown (alphabetical within jurisdiction groups) ----
      var groups = {{}};
      cands.forEach(function(c){{
        var j = c.jurisdiction || 'Other';
        if (!groups[j]) groups[j] = [];
        groups[j].push(c);
      }});
      var groupNames = Object.keys(groups).sort();
      sel.innerHTML = '<option value="">Jump to another official…</option>';
      groupNames.forEach(function(g){{
        var og = document.createElement('optgroup');
        og.label = g + ' (' + groups[g].length + ')';
        groups[g].sort(function(a, b){{
          return (a.name || '').localeCompare(b.name || '');
        }});
        groups[g].forEach(function(c){{
          var opt = document.createElement('option');
          opt.value = c.slug + '.html';
          opt.textContent = c.name + (c.office ? ' — ' + c.office : '');
          if (c.slug === currentSlug) {{
            opt.selected = true;
            opt.textContent = '★ ' + opt.textContent + ' (current)';
          }}
          og.appendChild(opt);
        }});
        sel.appendChild(og);
      }});
      sel.addEventListener('change', function(){{
        if (sel.value) window.location.href = sel.value;
      }});

      // ---- Prev/Next sort override ----
      // If no sort is active, leave the baked-in static order alone.
      var sortKey = activeSort();
      if (!sortKey) return;
      var sorted = cands.slice().sort(makeComparator(sortKey));
      var idx = -1;
      for (var i = 0; i < sorted.length; i++) {{
        if (sorted[i].slug === currentSlug) {{ idx = i; break; }}
      }}
      if (idx === -1) return;
      var prev = idx > 0 ? sorted[idx - 1] : null;
      var next = idx < sorted.length - 1 ? sorted[idx + 1] : null;
      rerenderNav(prev, next, idx + 1, sorted.length, SORT_LABELS[sortKey]);
    }})
    .catch(function(){{
      sel.innerHTML = '<option value="">Could not load officials list</option>';
    }});
}})();
</script>

<script>
(function() {{
  var navToggle = document.querySelector('.nav-toggle');
  var navLinks = document.querySelector('.nav-links');
  if (navToggle && navLinks) {{
    navToggle.addEventListener('click', function() {{ navLinks.classList.toggle('open'); }});
  }}
}})();
</script>
<script>
(function() {{
  var toggle = document.getElementById('themeToggle');
  var saved = localStorage.getItem('usmc-theme');
  if (saved !== 'light') {{
    document.documentElement.setAttribute('data-theme', 'dark');
    toggle.textContent = '\\u2600\\uFE0F';
  }}
  toggle.addEventListener('click', function() {{
    var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (isDark) {{
      document.documentElement.removeAttribute('data-theme');
      localStorage.setItem('usmc-theme', 'light');
      toggle.textContent = '\\uD83C\\uDF19';
    }} else {{
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('usmc-theme', 'dark');
      toggle.textContent = '\\u2600\\uFE0F';
    }}
  }});
}})();
</script>
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
