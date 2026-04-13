#!/usr/bin/env python3
"""Generate individual issue detail pages from issues.json"""
import json
import os

def generate_issue_page(issue):
    slug = issue['slug']
    urgency_class = {'critical': 'urgency-critical', 'soon': 'urgency-soon', 'info': 'urgency-info'}.get(issue.get('urgency', 'info'), 'urgency-info')
    card_class = {'critical': 'issue-card-urgent', 'soon': 'issue-card-upcoming', 'info': 'issue-card-info'}.get(issue.get('urgency', 'info'), 'issue-card-info')

    supporters_html = ''
    if issue.get('supporters'):
        supporters_html = '<h3>Who Supports This</h3><ul>'
        for s in issue['supporters']:
            supporters_html += f'<li>{s}</li>'
        supporters_html += '</ul>'

    opponents_html = ''
    if issue.get('opponents'):
        opponents_html = '<h3>Who Opposes This</h3><ul>'
        for o in issue['opponents']:
            opponents_html += f'<li>{o}</li>'
        opponents_html += '</ul>'

    sources_html = ''
    if issue.get('sources'):
        sources_html = '<div class="issue-sources"><h3>Sources &amp; Resources</h3>'
        for src in issue['sources']:
            label = src.get('label', src.get('url', ''))
            url = src.get('url', '#')
            sources_html += f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'
        sources_html += '</div>'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{issue['title']} — RESOLUTE Citizen | U.S.M.C. Ministries</title>
  <meta name="description" content="{issue.get('summary', '')}">
  <link rel="stylesheet" href="../assets/css/main.css">
  <link rel="icon" href="../assets/img/favicon.png" type="image/png">
  <style>
    .issue-container {{ max-width: 900px; margin: 0 auto; padding: 20px; }}
    .issue-back {{ display: inline-block; color: var(--accent); text-decoration: none; font-size: 0.85rem; margin-bottom: 20px; }}
    .issue-back:hover {{ text-decoration: underline; }}

    .issue-header {{
      padding: 32px 24px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 24px;
      border-left: 4px solid {'#f44336' if issue.get('urgency') == 'critical' else '#FFC107' if issue.get('urgency') == 'soon' else 'var(--accent)'};
    }}
    .issue-date {{
      font-size: 0.72rem;
      color: #c9a84c;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 8px;
    }}
    .issue-urgency {{
      display: inline-block;
      font-size: 0.65rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      padding: 2px 8px;
      border-radius: 4px;
      margin-left: 8px;
    }}
    .{urgency_class} {{ background: {'rgba(244,67,54,0.15); color: #f44336;' if issue.get('urgency') == 'critical' else 'rgba(255,193,7,0.15); color: #FFC107;' if issue.get('urgency') == 'soon' else 'rgba(107,114,128,0.15); color: #9ca3af;'} }}
    .issue-header h1 {{
      font-size: clamp(1.4rem, 3vw, 2rem);
      color: var(--white);
      margin-bottom: 6px;
      font-weight: 800;
    }}
    .issue-location {{ font-size: 0.88rem; color: var(--gray); }}

    .issue-body {{
      padding: 24px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 24px;
    }}
    .issue-body p {{ color: var(--gray); font-size: 0.92rem; line-height: 1.8; margin-bottom: 12px; }}
    .issue-body h3 {{ color: var(--white); font-size: 1.05rem; margin: 20px 0 10px; font-family: var(--font-main); }}
    .issue-body ul {{ margin-left: 20px; color: var(--gray); font-size: 0.9rem; line-height: 1.8; }}
    .issue-body ul li {{ margin-bottom: 6px; }}

    .issue-analysis {{
      padding: 24px;
      background: rgba(201,168,76,0.04);
      border: 1px solid rgba(201,168,76,0.15);
      border-radius: var(--radius);
      margin-bottom: 24px;
    }}
    .issue-analysis h2 {{ color: #c9a84c; font-size: 1rem; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 1px; }}
    .issue-analysis p {{ color: var(--gray); font-size: 0.92rem; line-height: 1.8; }}
    .issue-analysis .scripture {{
      margin-top: 16px;
      font-style: italic;
      color: var(--gray);
      font-size: 0.9rem;
      padding-top: 12px;
      border-top: 1px solid rgba(201,168,76,0.15);
    }}
    .issue-analysis .scripture cite {{ color: #c9a84c; font-style: normal; font-weight: 600; font-size: 0.82rem; }}

    .issue-sources {{
      padding: 20px 24px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 24px;
    }}
    .issue-sources h3 {{ color: var(--accent); font-size: 1rem; margin-bottom: 12px; }}
    .issue-sources a {{ color: var(--accent); text-decoration: none; font-size: 0.85rem; display: block; margin-bottom: 6px; }}
    .issue-sources a:hover {{ text-decoration: underline; }}

    footer {{ text-align: center; padding: 30px 20px; color: var(--gray); font-size: 0.82rem; border-top: 1px solid var(--border); margin-top: 40px; }}
    footer a {{ color: var(--accent); text-decoration: none; }}
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
    <li><a href="../mission.html">Mission</a></li>
    <li><a href="../shop.html">Shop</a></li>
    <li><a href="../coaching.html">Coaching</a></li>
    <li><a href="../about.html">About</a></li>
    <li><a href="https://usmcmin.org" target="_blank">Ministry Site</a></li>
  </ul>
  <a href="../coaching.html" class="btn nav-cta">Book a Session</a>
  <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">&#9789;</button>
  <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
</nav>

<div class="issue-container">
  <a href="../citizen-issues.html" class="issue-back">&larr; Back to Issues</a>

  <div class="issue-header">
    <div class="issue-date">
      {issue.get('date', '')}
      <span class="issue-urgency {urgency_class}">{issue.get('urgency_label', '')}</span>
    </div>
    <h1>{issue['title']}</h1>
    <div class="issue-location">{issue.get('location', '')}</div>
  </div>

  <div class="issue-body">
    {issue.get('body', '')}
    {supporters_html}
    {opponents_html}
  </div>

  <div class="issue-analysis">
    <h2>RESOLUTE Citizen Analysis</h2>
    <p>{issue.get('analysis', '')}</p>
    <div class="scripture">
      <p>"{issue.get('scripture', '')}"</p>
      <cite>&mdash; {issue.get('scripture_ref', '')}</cite>
    </div>
  </div>

  {sources_html}
</div>

<footer>
  <p><strong>RESOLUTE Citizen</strong> &mdash; a module of <a href="https://usmcmin.org">U.S.M.C. Ministries</a></p>
  <p style="margin-top:6px;font-size:0.72rem;"><a href="../citizen-issues.html">All Issues</a> | <a href="../citizen.html">Candidate Scorecard</a> | <a href="../sitemap.html">Sitemap</a></p>
</footer>

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
</body>
</html>'''

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data', 'issues.json')
    issues_dir = os.path.join(base_dir, 'issues')
    os.makedirs(issues_dir, exist_ok=True)

    with open(data_path, 'r') as f:
        data = json.load(f)

    count = 0
    for issue in data['issues']:
        slug = issue.get('slug', '')
        if not slug:
            continue
        html = generate_issue_page(issue)
        filepath = os.path.join(issues_dir, f'{slug}.html')
        with open(filepath, 'w') as f:
            f.write(html)
        count += 1

    print(f'Generated {count} issue detail pages in {issues_dir}/')

if __name__ == '__main__':
    main()
