#!/usr/bin/env python3
"""Generate business profile HTML from businesses.json (v0.4 template)."""
from __future__ import annotations

import html
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"
OUT = ROOT / "business"

FACTORS = [
    ("ownership", "1. Ownership clarity"),
    ("truth", "2. Truth in marketing"),
    ("christ_centered_brand", "3. Christ-centered public brand"),
    ("family_safety", "4. Family & child safety"),
    ("worker_dignity", "5. Worker dignity"),
    ("community_fruit", "6. Community fruit"),
    ("reliability", "7. Reliability"),
    ("financial_integrity", "8. Financial integrity"),
    ("digital_integrity", "9. Digital integrity"),
    ("network_worthiness", "10. Network worthiness"),
]

BAND_LABEL = {
    "green": "🟢 Green — Recommended",
    "yellow": "🟡 Yellow — Caution",
    "red": "🔴 Red — Not recommended",
    "black": "⬛ Black — Avoid",
    "gray": "⚪ Gray — Unrated",
}


def esc(s: str) -> str:
    return html.escape(s or "")


def color_profile(scores: dict) -> str:
    counts = Counter(str(scores.get(k, "gray")).lower() for k, _ in FACTORS)
    parts = []
    for color in ("green", "yellow", "red", "black", "gray"):
        n = counts.get(color, 0)
        if n:
            parts.append(f"{n} {color.title()}")
    return " · ".join(parts)


def evidence_chip(scores: dict, factor: str) -> str:
    band = str(scores.get(factor, "gray")).lower()
    meta = scores.get(f"{factor}_meta") or {}
    sc = meta.get("source_count", 0)
    reason = meta.get("reason", "")
    if band == "gray" or reason == "insufficient":
        return "insufficient evidence"
    if band in ("red", "black"):
        cc = meta.get("concern_count", 1)
        return f"{cc} concern{'s' if cc != 1 else ''}"
    if sc:
        return f"{sc} source{'s' if sc != 1 else ''}"
    return "affirmative"


def factor_detail(biz: dict, factor: str, band: str) -> str:
    meta = (biz.get("scores") or {}).get(f"{factor}_meta") or {}
    if band == "gray" or meta.get("reason") == "insufficient":
        return '<p class="insufficient">Insufficient public evidence — not a finding.</p>'
    sources = biz.get("sources") or []
    if not sources:
        return "<p>Scored from public brand and operator notes on file.</p>"
    items = "".join(
        f'<li><a href="{esc(s.get("url", ""))}" target="_blank" rel="noopener">{esc(s.get("label") or s.get("url", ""))}</a></li>'
        for s in sources
    )
    return f"<ul>{items}</ul>"


def botb_line(biz: dict) -> str:
    botb = biz.get("botb") or {}
    if not botb:
        return ""
    parts = []
    if botb.get("year"):
        parts.append(f"Best of the Burg {botb['year']}")
    if botb.get("category"):
        parts.append(botb["category"])
    if botb.get("result"):
        parts.append(botb["result"])
    return " · ".join(parts)


def render_profile(biz: dict) -> str:
    scores = biz.get("scores") or {}
    overall = str(biz.get("overall") or "gray").lower()
    prof = color_profile(scores)

    meta_bits = [
        esc(biz.get("category") or ""),
        esc(biz.get("address") or ""),
        esc(biz.get("city") or ""),
        esc(biz.get("state") or ""),
        esc(biz.get("zip") or ""),
    ]
    if biz.get("phone"):
        meta_bits.append(esc(biz["phone"]))
    botb = botb_line(biz)
    if botb:
        meta_bits.insert(0, esc(botb))

    factors_html = []
    for key, label in FACTORS:
        band = str(scores.get(key, "gray")).lower()
        chip = evidence_chip(scores, key)
        detail = factor_detail(biz, key, band)
        factors_html.append(
            f"""<li class="factor-row">
  <details>
    <summary>
      <span class="factor-label">{esc(label)}</span>
      <span class="factor-band {band}">{band.upper()}</span>
      <span class="evidence-chip">{esc(chip)}</span>
    </summary>
    <div class="factor-detail">{detail}</div>
  </details>
</li>"""
        )

    sources = biz.get("sources") or []
    src_html = ""
    if sources:
        items = "".join(
            f'<li><a href="{esc(s.get("url", ""))}" target="_blank" rel="noopener">{esc(s.get("label") or "Source")}</a></li>'
            for s in sources
        )
        src_html = f"""<div class="panel">
  <h2>Sources</h2>
  <ul>{items}</ul>
</div>"""

    network = biz.get("network_path") or ""
    network_html = ""
    if network:
        network_html = f"""<div class="panel">
  <h2>Network path</h2>
  <p>{esc(network)}</p>
</div>"""

    owner = biz.get("owner_operator") or ""
    owner_html = ""
    if owner:
        owner_html = f"""<div class="panel">
  <h2>Who owns / operates it</h2>
  <p>{esc(owner)}</p>
</div>"""

    summary = biz.get("summary") or ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(biz.get("name", ""))} — Christ-Centered Commerce</title>
  <meta name="description" content="10-Factor Christ-Centered Commerce scorecard for {esc(biz.get('name', ''))}." />
  <link rel="stylesheet" href="../assets/commerce.css" />
</head>
<body>
  <div class="soft-banner">Rubric v0.4 · Evidence before heat</div>
  <nav class="site-nav">
    <a href="../index.html">Hub</a>
    <a href="../directory.html">Directory</a>
    <a href="../categories/index.html">Categories</a>
    <a href="../methodology.html">Methodology</a>
    <a href="../about.html">About</a>
    <a href="../suggest.html">Suggest</a>
  </nav>
  <div class="wrap-narrow">
    <a class="back" href="../index.html">← Christ-Centered Commerce</a>
    <header class="profile-header">
      <div class="overall-band {overall}">{BAND_LABEL.get(overall, overall.upper())}</div>
      <h1 class="profile-title">{esc(biz.get("name", ""))}</h1>
      <div class="meta">{" · ".join(x for x in meta_bits if x)}</div>
      <div class="color-profile-chip"><span>{esc(prof)}</span></div>
    </header>

    <div class="panel">
      <h2>Verdict</h2>
      <p>{esc(summary)}</p>
    </div>

    {owner_html}
    {network_html}

    <div class="panel">
      <h2>10-Factor Scorecard</h2>
      <ul class="factor-list">
        {"".join(factors_html)}
      </ul>
    </div>

    {src_html}

    <div class="panel">
      <h2>See an error?</h2>
      <p>Submit a correction with sources.</p>
      <div class="cta-row"><a class="btn solid" href="../suggest.html">Submit feedback →</a></div>
    </div>

    <footer>Christ-Centered Commerce · C5iSR · Evidence before heat</footer>
  </div>
  <script src="../assets/commerce.js"></script>
</body>
</html>
"""


def main() -> None:
    slugs = [s.strip() for s in sys.argv[1:] if s.strip()]
    data = json.loads(DATA.read_text())
    businesses = data.get("businesses") or []
    if slugs:
        businesses = [b for b in businesses if b.get("slug") in slugs]
    OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for biz in businesses:
        slug = biz.get("slug")
        if not slug:
            continue
        path = OUT / f"{slug}.html"
        path.write_text(render_profile(biz))
        count += 1
    print(f"rendered {count} profiles -> {OUT}")


if __name__ == "__main__":
    main()
