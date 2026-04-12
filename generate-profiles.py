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

def generate_profile(candidate, categories, meta):
    c = candidate
    total = calc_total(c['scores'], categories)
    total_color = score_color(total['score'], MAX_TOTAL)
    bar_width = round((total['score'] / MAX_TOTAL) * 100) if MAX_TOTAL > 0 else 0
    profile = c.get('profile', {}) or {}

    # Build category breakdown
    cat_html = ''
    for cat in categories:
        cs = calc_cat_score(c['scores'].get(cat['id'], []))
        color = score_color(cs['score'], MAX_PER_TOPIC) if cs['answered'] > 0 else '#666'
        cat_html += f'''
    <div class="prof-category">
      <div class="prof-cat-header">
        <img src="../assets/icons/{cat['icon']}" alt="" width="24" height="24">
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
        ('Previous Election Opponent', profile.get('prev_election_opponent')),
        ('Next Election Year', profile.get('next_election_year')),
    ]
    if twitter:
        handle = twitter.lstrip('@')
        fields.append(('X / Twitter', f'<a href="https://x.com/{handle}" target="_blank" rel="noopener" style="color:var(--accent);">@{handle}</a>'))
    for label, val in fields:
        if val:
            profile_html += f'<div class="prof-detail"><strong>{label}:</strong> {val}</div>'

    contenders = profile.get('next_election_contenders', [])
    if contenders:
        profile_html += f'<div class="prof-detail"><strong>Upcoming Contenders:</strong> {", ".join(contenders)}</div>'

    notes = c.get('notes', '')
    website = c.get('website', '')
    sources = c.get('sources', [])
    sources_html = ''
    if sources:
        sources_html = '<div class="prof-sources"><h2>Sources &amp; Evidence</h2>'
        for src in sources:
            display = src.replace('https://', '').replace('http://', '')
            if len(display) > 60:
                display = display[:57] + '...'
            sources_html += f'<a href="{src}" target="_blank" rel="noopener">{display}</a>'
        sources_html += '</div>'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['name']} — RESOLUTE Citizen Scorecard | U.S.M.C. Ministries</title>
  <meta name="description" content="RESOLUTE Citizen Scorecard for {c['name']} ({party_label(c['party'])}). {c['office']}, {c['jurisdiction']}. Score: {total['score']}/{MAX_TOTAL}.">
  <link rel="stylesheet" href="../assets/css/main.css">
  <link rel="icon" href="../assets/img/favicon.png" type="image/png">
  <style>
    .prof-container {{ max-width: 900px; margin: 0 auto; padding: 20px; }}
    .prof-back {{ display: inline-block; color: var(--accent); text-decoration: none; font-size: 0.85rem; margin-bottom: 20px; }}
    .prof-back:hover {{ text-decoration: underline; }}

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
    <img src="../assets/img/logo.png" alt="U.S.M.C. Ministries" style="object-fit:contain">
    <div class="nav-brand-text">
      <div class="name">U.S.M.C. Ministries</div>
      <div class="tag">Warriors Equipped</div>
    </div>
  </a>
  <ul class="nav-links">
    <li><a href="../citizen.html" class="active">RESOLUTE Citizen</a></li>
    <li><a href="../shop.html">Shop</a></li>
    <li><a href="../coaching.html">Coaching</a></li>
    <li><a href="../about.html">About</a></li>
  </ul>
</nav>

<div class="prof-container">
  <a href="../citizen.html" class="prof-back">&larr; Back to Scorecard</a>

  <div class="prof-header">
    <div class="prof-jurisdiction">{c['jurisdiction']}</div>
    <h1 class="prof-name">{c['name']}</h1>
    <div class="prof-office">{c['office']}</div>
    <span class="prof-party {party_class(c['party'])}">{party_label(c['party'])}</span>
    {f'<a href="{website}" target="_blank" rel="noopener" style="margin-left:12px;color:var(--accent);font-size:0.85rem;">Campaign Website &rarr;</a>' if website else ''}
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

  {f"""<div class="prof-details">
    <h2>Candidate Profile</h2>
    {profile_html}
    {f'<div class="prof-notes">{notes}</div>' if notes else ''}
  </div>""" if profile_html or notes else ''}

  <h2 style="color:var(--accent);font-family:var(--font-main);margin-bottom:16px;">Category Breakdown</h2>
  {cat_html}

  {sources_html}
</div>

<footer>
  <p><strong>RESOLUTE Citizen</strong> &mdash; a module of <a href="https://usmcmin.org">U.S.M.C. Ministries</a></p>
  <p style="margin-top:6px;font-size:0.72rem;">Each True = +2 points &middot; Max 60 &middot; Primary sources only &middot; <a href="https://usmcmin.org/bible.html?ref=Proverbs+29:2">Proverbs 29:2</a></p>
</footer>

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
    count = 0

    for candidate in data['candidates']:
        slug = candidate.get('slug', '')
        if not slug:
            continue
        html = generate_profile(candidate, categories, meta)
        filepath = os.path.join(candidates_dir, f'{slug}.html')
        with open(filepath, 'w') as f:
            f.write(html)
        count += 1

    print(f'Generated {count} candidate profile pages in {candidates_dir}/')

if __name__ == '__main__':
    main()
