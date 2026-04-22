#!/usr/bin/env python3
"""Generate individual candidate profile pages from scorecard.json"""
import json
import os

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

    # Build category breakdown
    cat_html = ''
    for cat in categories:
        cs = calc_cat_score(c['scores'].get(cat['id'], []))
        color = score_color(cs['score'], MAX_PER_TOPIC) if cs['answered'] > 0 else '#666'
        cat_html += f'''
    <div class="prof-category">
      <div class="prof-cat-header">
        <img src="../../assets/icons/{cat['icon']}" alt="" width="24" height="24">
        <h3>{cat['label']}</h3>
        <span class="prof-cat-score" style="color:{color};">{cs['score']}/{MAX_PER_TOPIC}</span>
      </div>
      <div class="prof-questions">'''
        questions = cat.get('questions', [])
        answers = c['scores'].get(cat['id'], [None]*5)
        for i, q in enumerate(questions):
            a = answers[i] if i < len(answers) else None
            cat_html += f'''
        <div class="prof-q">
          <div class="prof-q-text">{q}</div>
          <div class="prof-q-answer">{answer_display(a)}</div>
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
        sources_html = '<div class="prof-sources"><h2>Sources &amp; Evidence</h2>'
        for src in sources:
            label = get_source_label(src)
            sources_html += f'<a href="{src}" target="_blank" rel="noopener">{label}</a>'
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
    .prof-sources a {{
      color: var(--accent);
      text-decoration: none;
      font-size: 0.82rem;
      display: block;
      margin-bottom: 4px;
      word-break: break-all;
    }}
    .prof-sources a:hover {{ text-decoration: underline; }}

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
    .prof-questions {{ padding: 0; }}
    .prof-q {{
      display: flex;
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
  </div>

  <div class="prof-total">
    <div>
      <div class="prof-total-label">RESOLUTE Citizen Score</div>
      <div>
        <span class="prof-total-score" style="color:{total_color};">{total['score']}</span>
        <span class="prof-total-max">/ {MAX_TOTAL}</span>
      </div>
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

  <!-- Bottom prev/next -->
  {prevnext_bar}

  <!-- Feedback Form -->
  <div class="prof-feedback" style="padding:20px 24px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);margin-top:16px;">
    <h2 style="color:var(--accent);font-size:1rem;margin-bottom:8px;">Have Information About This Official?</h2>
    <p style="color:var(--gray);font-size:0.82rem;margin-bottom:14px;line-height:1.6;">Help us improve this scorecard. If you have evidence of this official's positions — voting records, social media posts, public statements, or corrections — submit it below and we'll review and update the profile.</p>
    <form id="feedbackForm" style="display:flex;flex-direction:column;gap:10px;">
      <input type="hidden" name="candidate_name" value="{c['name']}">
      <input type="hidden" name="candidate_state" value="{c.get('state', '')}">
      <input type="hidden" name="candidate_office" value="{c.get('office', '')}">
      <input type="text" name="submitter_name" placeholder="Your name" required style="padding:10px 14px;background:var(--bg-dark,#0A0A0A);border:1px solid var(--border);border-radius:8px;color:var(--white);font-size:0.9rem;">
      <input type="email" name="submitter_email" placeholder="Your email" required style="padding:10px 14px;background:var(--bg-dark,#0A0A0A);border:1px solid var(--border);border-radius:8px;color:var(--white);font-size:0.9rem;">
      <textarea name="feedback" rows="4" placeholder="What should we know? Include links to sources if possible..." required style="padding:10px 14px;background:var(--bg-dark,#0A0A0A);border:1px solid var(--border);border-radius:8px;color:var(--white);font-size:0.9rem;resize:vertical;"></textarea>
      <button type="submit" style="background:linear-gradient(90deg,#c9a84c,#D4AF37);color:#000;font-weight:700;font-size:0.9rem;padding:11px 22px;border-radius:8px;border:none;cursor:pointer;align-self:flex-start;">Submit Feedback</button>
    </form>
    <div id="feedbackSuccess" style="display:none;padding:14px;background:rgba(76,175,80,.15);border:1px solid #4CAF50;border-radius:8px;color:#7edd80;margin-top:12px;font-size:0.88rem;">Thank you! We'll review your submission and update the profile if verified.</div>
  </div>
  <script>
  document.getElementById('feedbackForm').addEventListener('submit',function(e){{
    e.preventDefault();
    var fd=new FormData(this);
    fd.append('_subject','RESOLUTE Citizen Feedback: {c["name"]}');
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
