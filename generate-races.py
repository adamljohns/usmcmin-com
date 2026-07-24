#!/usr/bin/env python3
"""Generate static RESOLUTE race pages from data/races.json + scorecard.json.

Outputs:
  races/index.html
  races/<race_id>.html

Candidate profiles link here via profile.candidacy.race_id (see generate-profiles.py).
Never invent scores — stubs and missing rows render "Not yet scored".
"""
from __future__ import annotations

import json
import os
import re
from datetime import date
from html import escape
from pathlib import Path

REPO = Path(__file__).resolve().parent
RACES_PATH = REPO / "data" / "races.json"
SCORECARD_PATH = REPO / "data" / "scorecard.json"
OUT_DIR = REPO / "races"

PARTY_LABEL = {
    "R": "Republican",
    "D": "Democrat",
    "L": "Libertarian",
    "I": "Independent",
    "G": "Green",
    "C": "Constitution",
    "NP": "Nonpartisan",
}
PARTY_ORDER = ["R", "D", "L", "I", "G", "C", "NP"]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def calc_score(scores: dict, categories: list) -> dict:
    """Mirror compare.html style: 2 pts per TRUE, answered = non-null cells."""
    answered = 0
    pts = 0
    if not isinstance(scores, dict):
        return {"score": 0, "answered": 0, "max_possible": 0, "pct": 0}
    cat_ids = [c.get("id") for c in categories if c.get("id")]
    for cid in cat_ids:
        arr = scores.get(cid) or []
        if not isinstance(arr, list):
            continue
        for v in arr:
            if v is None or v == "N/A":
                continue
            answered += 1
            if v is True:
                pts += 2
    max_possible = answered * 2
    pct = int(round((pts / max_possible) * 100)) if max_possible else 0
    return {"score": pts, "answered": answered, "max_possible": max_possible, "pct": pct}


def letter_grade(pct: int, answered: int) -> str:
    if answered < 10:
        return "—"
    if pct >= 90:
        return "A"
    if pct >= 80:
        return "B"
    if pct >= 70:
        return "C"
    if pct >= 60:
        return "D"
    return "F"


def grade_color(letter: str) -> str:
    return {
        "A": "#22c55e",
        "B": "#84cc16",
        "C": "#eab308",
        "D": "#f97316",
        "F": "#f44336",
        "—": "#9ca3af",
    }.get(letter, "#9ca3af")


def conf_chip(conf) -> str:
    if not conf:
        return '<span class="race-chip race-chip-null">Not reviewed</span>'
    label = str(conf).replace("_", " ")
    cls = "race-chip-ok" if str(conf).startswith("evidence") else "race-chip-soft"
    return f'<span class="race-chip {cls}">{escape(label)}</span>'


def party_class(p: str) -> str:
    p = (p or "").upper()
    if p in ("R", "D", "L", "I"):
        return f"party-{p.lower()}"
    return "party-o"


def fmt_date(iso: str) -> str:
    if not iso:
        return ""
    try:
        y, m, d = iso.split("-")
        months = [
            "", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
        ]
        return f"{months[int(m)]} {int(d)}, {y}"
    except Exception:
        return iso


def nav_html(active: str = "races") -> str:
    races_cls = ' class="active"' if active == "races" else ""
    return f'''<nav>
  <a href="/" class="nav-brand" style="text-decoration:none">
    <img src="../assets/img/logo.png" alt="U.S.M.C. Ministries" style="object-fit:contain">
    <div class="nav-brand-text">
      <div class="name">U.S.M.C. Ministries</div>
      <div class="tag">Warriors Equipped</div>
    </div>
  </a>
  <ul class="nav-links">
    <li><a href="../citizen.html">RESOLUTE</a></li>
    <li><a href="../find-my-reps.html">Find My Reps</a></li>
    <li><a href="../compare.html">Compare</a></li>
    <li><a href="index.html"{races_cls}>Races</a></li>
    <li><a href="../about.html">About</a></li>
    <li><a href="https://usmcmin.org" target="_blank" rel="noopener">Ministry Site</a></li>
  </ul>
  <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">☽</button>
  <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
</nav>'''


def shared_css() -> str:
    return '''
    .race-wrap { max-width: 1100px; margin: 0 auto; padding: 22px 16px 70px; }
    .race-crumb { font-size: 0.82rem; color: var(--gray); margin: 12px 0 18px; line-height: 1.6; }
    .race-crumb a { color: var(--accent); text-decoration: none; }
    .race-crumb a:hover { text-decoration: underline; }
    .race-hero {
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 22px 20px;
      margin-bottom: 22px;
      background: rgba(255,255,255,0.02);
    }
    .race-kicker {
      display: inline-block;
      font-size: 0.68rem;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 10px;
    }
    .race-hero h1 {
      margin: 0 0 8px;
      font-size: clamp(1.55rem, 3.6vw, 2.2rem);
      color: var(--white);
      font-weight: 800;
      line-height: 1.2;
    }
    .race-meta {
      color: var(--gray);
      font-size: 0.92rem;
      line-height: 1.7;
      margin: 0 0 14px;
    }
    .race-meta strong { color: var(--white); }
    .race-actions { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 8px; }
    .race-btn {
      display: inline-block;
      padding: 10px 14px;
      border-radius: 10px;
      font-size: 0.86rem;
      font-weight: 700;
      text-decoration: none;
      border: 1px solid var(--border);
      color: var(--white);
      background: rgba(255,255,255,0.04);
    }
    .race-btn-primary {
      background: rgba(201,162,39,0.18);
      border-color: rgba(201,162,39,0.45);
      color: var(--accent);
    }
    .race-btn:hover { filter: brightness(1.08); }
    .race-section { margin: 28px 0 10px; }
    .race-section h2 {
      margin: 0 0 12px;
      font-size: 1.05rem;
      letter-spacing: 0.4px;
      color: var(--white);
    }
    .race-party {
      margin: 0 0 18px;
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
    }
    .race-party-head {
      padding: 10px 14px;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 1px;
      text-transform: uppercase;
      border-bottom: 1px solid var(--border);
      background: rgba(255,255,255,0.03);
    }
    .race-cand {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 10px 16px;
      padding: 14px;
      border-bottom: 1px solid var(--border);
      align-items: center;
    }
    .race-cand:last-child { border-bottom: 0; }
    .race-cand-name {
      font-size: 1.02rem;
      font-weight: 750;
      color: var(--white);
      text-decoration: none;
    }
    .race-cand-name:hover { color: var(--accent); }
    .race-cand-sub { color: var(--gray); font-size: 0.82rem; margin-top: 3px; line-height: 1.5; }
    .race-scorebox { text-align: right; min-width: 110px; }
    .race-score {
      font-size: 1.35rem;
      font-weight: 800;
      font-variant-numeric: tabular-nums;
    }
    .race-score-sub { color: var(--gray); font-size: 0.75rem; margin-top: 2px; }
    .race-chip {
      display: inline-block;
      margin-top: 6px;
      padding: 3px 8px;
      border-radius: 999px;
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.3px;
      border: 1px solid var(--border);
      color: var(--gray);
    }
    .race-chip-ok { color: #86efac; border-color: rgba(34,197,94,0.35); background: rgba(34,197,94,0.08); }
    .race-chip-soft { color: #fde68a; border-color: rgba(234,179,8,0.35); background: rgba(234,179,8,0.08); }
    .race-chip-null { color: #9ca3af; }
    .party-r { color: #f87171; }
    .party-d { color: #60a5fa; }
    .party-l { color: #fbbf24; }
    .party-i { color: #c4b5fd; }
    .party-o { color: var(--gray); }
    .race-sources { margin-top: 8px; padding-left: 18px; color: var(--gray); font-size: 0.84rem; line-height: 1.7; }
    .race-sources a { color: var(--accent); word-break: break-all; }
    .race-note {
      margin-top: 18px;
      padding: 12px 14px;
      border-left: 3px solid var(--accent);
      background: rgba(201,162,39,0.08);
      color: var(--gray);
      font-size: 0.86rem;
      line-height: 1.6;
    }
    .race-index-list { display: grid; gap: 12px; }
    .race-card {
      display: block;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      text-decoration: none;
      background: rgba(255,255,255,0.02);
    }
    .race-card:hover { border-color: rgba(201,162,39,0.45); }
    .race-card h3 { margin: 0 0 6px; color: var(--white); font-size: 1.05rem; }
    .race-card p { margin: 0; color: var(--gray); font-size: 0.86rem; line-height: 1.55; }
    .race-state-head {
      margin: 28px 0 10px;
      font-size: 0.78rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--accent);
      font-weight: 800;
    }
    @media (max-width: 640px) {
      .race-cand { grid-template-columns: 1fr; }
      .race-scorebox { text-align: left; }
    }
    '''


def page_shell(title: str, description: str, canonical: str, body: str, active: str = "races") -> str:
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <script>(function(){{try{{var s=localStorage.getItem('usmc-theme')||localStorage.getItem('theme');if(s!=='light')document.documentElement.setAttribute('data-theme','dark');}}catch(e){{}}}})();</script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="{escape(canonical)}">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta property="og:site_name" content="RESOLUTE Citizen Scorecard">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{escape(canonical)}">
  <meta property="og:image" content="https://usmcmin.com/assets/og/og-citizen.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title)}">
  <meta name="twitter:description" content="{escape(description)}">
  <link rel="stylesheet" href="../assets/css/main.min.css">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="../assets/icons/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="../assets/icons/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="../assets/icons/apple-touch-icon.png">
  <style>{shared_css()}</style>
</head>
<body>
{nav_html(active)}
<div class="race-wrap">
{body}
</div>
<script src="../assets/js/main.min.js" defer></script>
</body>
</html>
'''


def index_by_slug(candidates: list) -> dict:
    out = {}
    for c in candidates:
        slug = c.get("slug")
        if not slug:
            continue
        st = (c.get("state") or "").upper()
        out[(st, slug)] = c
        # also bare slug fallback for single-state races
        out.setdefault(slug, c)
    return out


def find_cand(index: dict, state: str, slug: str):
    st = (state or "VA").upper()
    return index.get((st, slug)) or index.get(slug)


def render_candidate_row(c, slug: str, state: str, categories: list, is_incumbent_slug: str | None) -> str:
    st = (state or "VA").lower()
    if not c:
        return f'''<div class="race-cand">
  <div>
    <div class="race-cand-name" style="opacity:.75">{escape(slug)}</div>
    <div class="race-cand-sub">Listed in race manifest — not found in scorecard yet</div>
  </div>
  <div class="race-scorebox">
    <div class="race-score" style="color:#9ca3af;">—</div>
    <div class="race-score-sub">Not yet scored</div>
    {conf_chip(None)}
  </div>
</div>'''

    name = c.get("name") or slug
    party = (c.get("party") or "").upper()
    office = c.get("office") or ""
    conf = (c.get("profile") or {}).get("confidence")
    tot = calc_score(c.get("scores") or {}, categories)
    letter = letter_grade(tot["pct"], tot["answered"])
    color = grade_color(letter)
    href = f"../candidates/{st}/{escape(c.get('slug') or slug)}.html"
    badges = []
    if is_incumbent_slug and (c.get("slug") == is_incumbent_slug or slug == is_incumbent_slug):
        badges.append("Incumbent")
    badge_html = (" · ".join(badges) + " · ") if badges else ""
    if tot["answered"] == 0:
        score_html = f'''<div class="race-score" style="color:#9ca3af;">—</div>
    <div class="race-score-sub">Not yet scored</div>'''
    else:
        # Uniform /100 display when we have answers: use pct as headline when max known
        headline = tot["pct"] if tot["max_possible"] else tot["score"]
        score_html = f'''<div class="race-score" style="color:{color};">{headline}<span style="font-size:.7em;font-weight:600;color:var(--gray)">/100</span> <span style="font-size:.75em">{escape(letter)}</span></div>
    <div class="race-score-sub">{tot["answered"]} answered · raw {tot["score"]}/{tot["max_possible"]}</div>'''

    return f'''<div class="race-cand">
  <div>
    <a class="race-cand-name" href="{href}">{escape(name)}</a>
    <div class="race-cand-sub"><span class="{party_class(party)}">{escape(PARTY_LABEL.get(party, party or "Unknown"))}</span> · {escape(badge_html + office)}</div>
  </div>
  <div class="race-scorebox">
    {score_html}
    {conf_chip(conf)}
  </div>
</div>'''


def render_race_page(race_id: str, race: dict, index: dict, categories: list) -> str:
    office = race.get("office") or race_id
    state = (race.get("state") or "VA").upper()
    primary = race.get("primary_date") or ""
    general = race.get("general_date") or ""
    incumbent = race.get("incumbent")
    note = race.get("incumbent_note") or ""
    area = race.get("area_note") or ""
    by_party = race.get("candidates_by_party") or {}

    parties = [p for p in PARTY_ORDER if p in by_party]
    for p in by_party:
        if p not in parties:
            parties.append(p)

    party_blocks = []
    for p in parties:
        slugs = by_party.get(p) or []
        rows = "\n".join(
            render_candidate_row(find_cand(index, state, s), s, state, categories, incumbent)
            for s in slugs
        )
        party_blocks.append(
            f'''<div class="race-party">
  <div class="race-party-head {party_class(p)}">{escape(PARTY_LABEL.get(p, p))} primary / ticket</div>
  {rows}
</div>'''
        )

    sources = race.get("sources") or []
    src_html = ""
    if sources:
        items = "\n".join(
            f'<li><a href="{escape(u)}" target="_blank" rel="noopener">{escape(u)}</a></li>'
            for u in sources
        )
        src_html = f'<div class="race-section"><h2>Sources</h2><ul class="race-sources">{items}</ul></div>'

    meta_bits = [f"<strong>State:</strong> {escape(state)}"]
    if primary:
        meta_bits.append(f"<strong>Primary:</strong> {escape(fmt_date(primary))} ({escape(primary)})")
    if general:
        meta_bits.append(f"<strong>General:</strong> {escape(fmt_date(general))} ({escape(general)})")
    if note:
        meta_bits.append(escape(note))

    area_html = f'<p class="race-meta">{escape(area)}</p>' if area else ""

    body = f'''
  <nav class="race-crumb" aria-label="Breadcrumb">
    <a href="../citizen.html">RESOLUTE Citizen</a> ›
    <a href="index.html">Races</a> ›
    <a href="../citizen.html?state={escape(state)}">{escape(state)}</a> ›
    <span>{escape(office)}</span>
  </nav>

  <header class="race-hero">
    <div class="race-kicker">Race page · {escape(state)} · 2026</div>
    <h1>{escape(office)}</h1>
    <p class="race-meta">{" · ".join(meta_bits)}</p>
    {area_html}
    <div class="race-actions">
      <a class="race-btn race-btn-primary" href="../compare.html?race={escape(race_id)}">Compare side-by-side →</a>
      <a class="race-btn" href="../citizen.html?state={escape(state)}">Browse {escape(state)} officials</a>
      <a class="race-btn" href="index.html">All races</a>
    </div>
  </header>

  <section class="race-section">
    <h2>Candidates</h2>
    {"".join(party_blocks) if party_blocks else "<p class='race-meta'>No candidates listed yet.</p>"}
  </section>

  {src_html}

  <div class="race-note">
    Scores come only from cited RESOLUTE evidence. “Not yet scored” means the candidate is on the race board but has no verified rubric answers yet — not a zero, not an endorsement.
    Generated {escape(date.today().isoformat())}.
  </div>
'''
    title = f"{office} — RESOLUTE Race Page"
    desc = f"RESOLUTE Citizen race board for {office}. Primary {primary or 'TBD'}, general {general or 'TBD'}. Compare scored candidates with citations."
    canonical = f"https://usmcmin.com/races/{race_id}.html"
    return page_shell(title, desc, canonical, body)


def render_index(races: dict) -> str:
    # group by state
    by_state: dict[str, list] = {}
    for rid, race in races.items():
        st = (race.get("state") or "??").upper()
        by_state.setdefault(st, []).append((rid, race))
    for st in by_state:
        by_state[st].sort(key=lambda x: (x[1].get("primary_date") or "9999", x[1].get("office") or ""))

    blocks = []
    for st in sorted(by_state.keys()):
        cards = []
        for rid, race in by_state[st]:
            office = race.get("office") or rid
            primary = fmt_date(race.get("primary_date") or "")
            general = fmt_date(race.get("general_date") or "")
            n = sum(len(v or []) for v in (race.get("candidates_by_party") or {}).values())
            cards.append(
                f'''<a class="race-card" href="{escape(rid)}.html">
  <h3>{escape(office)}</h3>
  <p>Primary {escape(primary or "TBD")} · General {escape(general or "TBD")} · {n} candidates listed</p>
</a>'''
            )
        blocks.append(f'<div class="race-state-head">{escape(st)}</div><div class="race-index-list">{"".join(cards)}</div>')

    body = f'''
  <nav class="race-crumb" aria-label="Breadcrumb">
    <a href="../citizen.html">RESOLUTE Citizen</a> ›
    <span>Races</span>
  </nav>
  <header class="race-hero">
    <div class="race-kicker">RESOLUTE Citizen</div>
    <h1>Race boards</h1>
    <p class="race-meta">Each race page groups declared candidates, links to full profiles, and opens the side-by-side compare tool. Start with your area; expand the commonwealth from here.</p>
    <div class="race-actions">
      <a class="race-btn race-btn-primary" href="../compare.html">Open compare tool →</a>
      <a class="race-btn" href="../find-my-reps.html">Find my reps</a>
    </div>
  </header>
  {"".join(blocks) if blocks else "<p class='race-meta'>No races in data/races.json yet.</p>"}
  <div class="race-note">Race manifests live in <code>data/races.json</code>. Candidate scores never get invented on these pages.</div>
'''
    return page_shell(
        "Race Boards — RESOLUTE Citizen",
        "Browse RESOLUTE Citizen race boards. Compare candidates in the same election with cited scores.",
        "https://usmcmin.com/races/index.html",
        body,
    )


def patch_profile_race_links(race_ids: set[str]) -> int:
    """Enhance candidacy banners: add This race → /races/<id>.html next to compare link."""
    cand_root = REPO / "candidates"
    if not cand_root.exists():
        return 0
    n = 0
    # Match compare link already present
    pat = re.compile(
        r'(Currently running for <strong>.*?</strong>\..*?)'
        r'( <a href="\.\./\.\./compare\.html\?race=([a-z0-9\-]+)">Compare against other candidates &rarr;</a>)',
        re.S,
    )

    def repl(m):
        nonlocal n
        race_id = m.group(3)
        if race_id not in race_ids:
            return m.group(0)
        if f'races/{race_id}.html' in m.group(0):
            return m.group(0)
        n += 1
        return (
            f'{m.group(1)}'
            f' <a href="../../races/{race_id}.html">This race →</a>'
            f'{m.group(2)}'
        )

    for html_path in cand_root.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8")
        if "compare.html?race=" not in text:
            continue
        new = pat.sub(repl, text)
        if new != text:
            html_path.write_text(new, encoding="utf-8")
    return n


def main():
    races_doc = load_json(RACES_PATH)
    scorecard = load_json(SCORECARD_PATH)
    races = races_doc.get("races") or {}
    categories = scorecard.get("categories") or []
    candidates = scorecard.get("candidates") or []
    index = index_by_slug(candidates)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # index
    (OUT_DIR / "index.html").write_text(render_index(races), encoding="utf-8")

    for rid, race in races.items():
        # sanitize filename
        safe = re.sub(r"[^a-zA-Z0-9\-_]", "-", rid)
        path = OUT_DIR / f"{safe}.html"
        path.write_text(render_race_page(rid, race, index, categories), encoding="utf-8")
        print(f"wrote {path.relative_to(REPO)}")

    patched = patch_profile_race_links(set(races.keys()))
    print(f"wrote races/index.html ({len(races)} races); patched {patched} candidate profile race links")


if __name__ == "__main__":
    main()
