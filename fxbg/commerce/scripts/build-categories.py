#!/usr/bin/env python3
"""Generate category landing pages under categories/ (v0.4)."""
from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"
OUT = ROOT / "categories"

BAND_COLOR = {
    "green": "#4CAF50",
    "yellow": "#FFC107",
    "red": "#f44336",
    "black": "#888",
    "gray": "#888",
}


def esc(s: str) -> str:
    return html.escape(s or "")


def slugify(cat: str) -> str:
    return cat.replace("_", "-")


def label(cat: str) -> str:
    return cat.replace("-", " ").title()


def card(biz: dict) -> str:
    overall = str(biz.get("overall") or "gray").lower()
    color = BAND_COLOR.get(overall, "#888")
    return f"""<a class="biz-card" href="../business/{esc(biz['slug'])}.html" style="border-color:{color}55">
  <div class="eyebrow" style="color:{color}">{overall.upper()}</div>
  <h3>{esc(biz.get('name', ''))}</h3>
  <div class="meta">{esc(biz.get('address') or biz.get('city') or '')}</div>
</a>"""


def render_category(cat: str, listings: list[dict]) -> str:
    overall = Counter(str(b.get("overall", "gray")).lower() for b in listings)
    bands = " · ".join(f"{overall[c]} {c.title()}" for c in ("green", "yellow", "gray", "red") if overall.get(c))
    cards = "\n".join(card(b) for b in sorted(listings, key=lambda x: x.get("name", "")))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(label(cat))} — Christ-Centered Commerce</title>
  <meta name="description" content="{len(listings)} Fredericksburg-area {esc(label(cat))} listings — 10-Factor scorecard." />
  <link rel="stylesheet" href="../assets/commerce.css" />
  <style>
    .cat-grid {{ display:grid; gap:12px; }}
    @media (min-width:640px) {{ .cat-grid {{ grid-template-columns:1fr 1fr; }} }}
  </style>
</head>
<body>
  <div class="soft-banner">Rubric v0.4 · Category browse</div>
  <nav class="site-nav">
    <a href="../index.html">Hub</a>
    <a href="../directory.html">Directory</a>
    <a href="index.html" class="active">Categories</a>
    <a href="../methodology.html">Methodology</a>
    <a href="../about.html">About</a>
  </nav>
  <div class="wrap">
    <a class="back" href="index.html">← All categories</a>
    <div class="module-tag">{esc(label(cat))}</div>
    <h1 class="profile-title">{esc(label(cat))}</h1>
    <p class="meta">{len(listings)} listings · {esc(bands)}</p>
    <div class="panel">
      <div class="cat-grid">
        {cards}
      </div>
    </div>
  </div>
  <script src="../assets/commerce.js"></script>
</body>
</html>
"""


def render_index(counts: list[tuple[str, int]]) -> str:
    rows = "\n".join(
        f"""<a class="sister-card" href="{esc(slugify(cat))}.html">
  <div class="kicker">{n} listings</div>
  <strong>{esc(label(cat))}</strong>
</a>"""
        for cat, n in counts
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Categories — Christ-Centered Commerce</title>
  <link rel="stylesheet" href="../assets/commerce.css" />
  <style>.cat-index {{ display:grid; gap:12px; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); }}</style>
</head>
<body>
  <div class="soft-banner">Rubric v0.4 · Browse by category</div>
  <nav class="site-nav">
    <a href="../index.html">Hub</a>
    <a href="../directory.html">Directory</a>
    <a href="index.html" class="active">Categories</a>
    <a href="../methodology.html">Methodology</a>
    <a href="../about.html">About</a>
  </nav>
  <div class="wrap">
    <div class="module-tag">Categories</div>
    <h1 class="profile-title">Browse by <span style="color:var(--gold)">Category</span></h1>
    <p class="meta">{len(counts)} categories · tap for filtered listings</p>
    <div class="panel cat-index">
      {rows}
    </div>
  </div>
</body>
</html>
"""


def main() -> None:
    data = json.loads(DATA.read_text())
    businesses = data.get("businesses") or []
    by_cat: dict[str, list] = {}
    for biz in businesses:
        cat = biz.get("category") or "other"
        by_cat.setdefault(cat, []).append(biz)
    counts = sorted(by_cat.items(), key=lambda x: (-len(x[1]), x[0]))
    OUT.mkdir(parents=True, exist_ok=True)
    for cat, listings in counts:
        if len(listings) < 2:
            continue
        path = OUT / f"{slugify(cat)}.html"
        path.write_text(render_category(cat, listings))
    (OUT / "index.html").write_text(render_index([(c, len(l)) for c, l in counts if len(l) >= 2]))
    built = sum(1 for _, l in counts if len(l) >= 2)
    print(f"built categories/index.html + {built} category pages -> {OUT}")


if __name__ == "__main__":
    main()
