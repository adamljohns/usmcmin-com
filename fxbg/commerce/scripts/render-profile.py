#!/usr/bin/env python3
"""Generate business profile HTML from businesses.json (v0.4 template)."""
from __future__ import annotations

import html
import json
import re
from urllib.parse import urlencode
import sys
from collections import Counter
from pathlib import Path

from commerce_common import (
    category_label, directions_url, display_phone, load_osm_tags, location_note, osm_tags_for, pretty_hours, real_address,
    tel_href,
)

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
    items = "".join(source_li(s) for s in sources)
    return f"<ul>{items}</ul>"


def source_li(s: dict) -> str:
    """A dead source stays as evidence text but is never linked (expired, hijacked or 404 pages)."""
    label = esc(s.get("label") or s.get("url", "") or "Source")
    if s.get("dead"):
        return f'<li>{label} <span class="meta">(link no longer works — checked {esc(s["dead"])})</span></li>'
    return f'<li><a href="{esc(s.get("url", ""))}" target="_blank" rel="noopener">{label}</a></li>'


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


def closed_panel(biz: dict) -> str:
    if not biz.get("closed"):
        return ""
    ev = "".join(
        f'<li><a href="{esc(e.get("url", ""))}" target="_blank" rel="noopener">{esc(e.get("label") or e.get("url", ""))}</a></li>'
        for e in biz.get("closed_evidence") or [])
    return f"""<div class="panel" style="border-color:#f44336">
  <h2>Reported closed</h2>
  <p>Public listings report this business as closed. It is no longer shown in the directory. Still open? <a href="../suggest.html">Tell us</a>.</p>
  {f"<ul>{ev}</ul>" if ev else ""}
</div>"""


def contact_panel(biz: dict, tags: dict) -> str:
    """Address, phone, website, directions and hours — only what is on file."""
    rows = []
    addr = real_address(biz)
    place = ", ".join(x for x in (biz.get("city"), biz.get("state")) if x)
    if addr:
        line = addr if (biz.get("city") or "") in addr else f"{addr}, {place}"
        if biz.get("zip") and biz["zip"] not in line:
            line += f" {biz['zip']}"
        rows.append(f"<p><strong>Address:</strong> {esc(line)}</p>")
    elif location_note(biz):
        rows.append(f"<p><strong>Location:</strong> {esc(location_note(biz))}</p>")
    else:
        rows.append(f"<p><strong>Address:</strong> street address not confirmed yet · {esc(place or 'Fredericksburg area')}"
                    f"{(' ' + esc(biz['zip'])) if biz.get('zip') else ''}</p>")
    if biz.get("phone"):
        tel = tel_href(biz["phone"])
        ph = f'<a href="{tel}">{esc(display_phone(biz["phone"]))}</a>' if tel else esc(biz["phone"])
        rows.append(f"<p><strong>Phone:</strong> {ph}</p>")
    own = biz.get("hours_source") or {}
    if biz.get("hours") and own.get("url"):
        checked = f", checked {esc(own['checked'])}" if own.get("checked") else ""
        rows.append("<p><strong>Hours:</strong><br>" + "<br>".join(esc(h) for h in biz["hours"])
                    + f'<br><span class="meta">From <a href="{esc(own["url"])}" target="_blank" rel="noopener">the business\'s website</a>{checked}.</span></p>')
    stale = biz.get("osm_hours_stale")  # moved since the OSM survey — old hours belong to the old storefront
    hours = [] if (biz.get("hours") or stale) else pretty_hours(tags.get("opening_hours", ""))
    if hours:
        checked = tags.get("check_date:opening_hours") or tags.get("check_date")
        note = f"OpenStreetMap community data{', last checked ' + esc(checked) if checked else ''} — call ahead to confirm."
        rows.append("<p><strong>Hours:</strong><br>" + "<br>".join(esc(h) for h in hours)
                    + f'<br><span class="meta">{note}</span></p>')
    buttons = []
    if biz.get("web"):
        buttons.append(f'<a class="btn solid" href="{esc(biz["web"])}" target="_blank" rel="noopener">Website →</a>')
    tel = tel_href(biz.get("phone") or "")
    if tel:
        buttons.append(f'<a class="btn" href="{tel}">Call</a>')
    maps = directions_url(biz)
    if maps:
        label = "Directions" if addr else ("Map location" if biz.get("ingest_source") == "osm" else "Find on map")
        buttons.append(f'<a class="btn" href="{esc(maps)}" target="_blank" rel="noopener">{label}</a>')
    btn_html = f'<div class="cta-row">{"".join(buttons)}</div>' if buttons else ""
    return f"""<div class="panel">
  <h2>Visit &amp; contact</h2>
  {"".join(rows)}
  {btn_html}
</div>"""


def own_words_panel(biz: dict) -> str:
    """The business's own one-line self-description, quoted verbatim from its website."""
    text, src = biz.get("description"), biz.get("description_source") or {}
    if not text or not src.get("url"):
        return ""
    checked = f", checked {esc(src['checked'])}" if src.get("checked") else ""
    return f"""<div class="panel">
  <h2>In their own words</h2>
  <p>&ldquo;{esc(text)}&rdquo;</p>
  <p class="meta">Quoted from <a href="{esc(src['url'])}" target="_blank" rel="noopener">the business's website</a>{checked}. Their description, not our review.</p>
</div>"""


def render_duplicate(biz: dict, target: dict) -> str:
    """Folded OSM duplicate: send visitors (and search engines) to the full listing."""
    name = esc(target.get("name", ""))
    href = f"{esc(target['slug'])}.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{name} — Christ-Centered Commerce</title>
  <meta name="robots" content="noindex" />
  <link rel="canonical" href="https://usmcmin.com/fxbg/commerce/business/{href}" />
  <meta http-equiv="refresh" content="0; url={href}" />
  <link rel="stylesheet" href="../assets/commerce.css" />
</head>
<body>
  <div class="wrap-narrow">
    <p>This listing has moved to <a href="{href}">{name}</a>.</p>
  </div>
</body>
</html>
"""


def json_ld(biz: dict, tags: dict) -> str:
    """schema.org LocalBusiness from facts on file only (no ratings — bands are not stars)."""
    ld = {"@context": "https://schema.org", "@type": "LocalBusiness", "name": biz.get("name", ""),
          "url": f"https://usmcmin.com/fxbg/commerce/business/{biz.get('slug')}.html"}
    addr = real_address(biz)
    if addr:
        ld["address"] = {k: v for k, v in {
            "@type": "PostalAddress", "streetAddress": addr, "addressLocality": biz.get("city") or "",
            "addressRegion": biz.get("state") or "VA", "postalCode": biz.get("zip") or ""}.items() if v}
    if biz.get("phone"):
        ld["telephone"] = biz["phone"]
    if biz.get("web"):
        ld["sameAs"] = biz["web"]
    if biz.get("ingest_source") == "osm" and biz.get("lat") is not None and biz.get("lng") is not None:
        ld["geo"] = {"@type": "GeoCoordinates", "latitude": biz["lat"], "longitude": biz["lng"]}
    oh = tags.get("opening_hours", "")
    if oh and not biz.get("hours") and not biz.get("osm_hours_stale") and re.fullmatch(r"[A-Za-z0-9:,;\- /]+", oh):
        ld["openingHours"] = [x.strip() for x in oh.split(";") if x.strip()]
    body = json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")
    return f'<script type="application/ld+json">{body}</script>'


def place_bits(biz: dict, tags: dict) -> tuple[str, str]:
    """(where, contact) for <title>/description: the street address on file, else the community-map street,
    else the ZIP — so chain locations get distinct titles. Contact lists only what is on file."""
    where = real_address(biz) or location_note(biz)
    if not where:
        num, street = (tags.get("addr:housenumber") or "").strip(), (tags.get("addr:street") or "").strip()
        where = f"{num} {street}".strip() if street else ""
    if not where and (biz.get("map_area") or {}).get("text"):
        where = biz["map_area"]["text"]  # reverse geocode of the map point, e.g. "near Plank Road, Chancellor"
    if not where and biz.get("zip"):
        where = f"ZIP {biz['zip']}"
    have = ["address" if real_address(biz) else "location"]
    if biz.get("phone"):
        have.append("phone")
    if biz.get("hours") or (tags.get("opening_hours") and not biz.get("osm_hours_stale")):
        have.append("hours")
    if biz.get("web"):
        have.append("website")
    contact = ", ".join(have[:-1]) + (" and " if len(have) > 1 else "") + have[-1]
    return where, contact


def render_profile(biz: dict, osm: dict | None = None, alt_tags: dict | None = None) -> str:
    scores = biz.get("scores") or {}
    overall = str(biz.get("overall") or "gray").lower()
    prof = color_profile(scores)
    tags = osm_tags_for(biz, osm or {}) or alt_tags or {}
    cat = biz.get("category") or "other"
    cat_slug = cat.replace("_", "-")
    where, contact = place_bits(biz, tags)

    meta_bits = [
        f'<a href="../categories/{esc(cat_slug)}.html">{esc(category_label(cat))}</a>',
        esc(biz.get("city") or ""),
    ]
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
        items = "".join(source_li(s) for s in sources)
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
    unreviewed = all(str(scores.get(k, "gray")).lower() == "gray" for k, _ in FACTORS)
    suggest_href = "../suggest.html?" + urlencode({
        "type": "correct", "business_name": biz.get("name", ""), "business_id": biz.get("slug", ""),
        "category": cat})
    origin = "This listing comes from a community map (OpenStreetMap) and " if biz.get("ingest_source") == "osm" else "This listing "
    if unreviewed:
        verdict_html = f"""<div class="panel">
  <h2>Not reviewed yet</h2>
  <p>{origin}has not been reviewed against the 10 factors yet. Gray means insufficient public evidence — neutral, not a bad mark.</p>
  <div class="cta-row"><a class="btn" href="{esc(suggest_href)}">Know this business? Tell us →</a></div>
</div>"""
    else:
        verdict_html = f"""<div class="panel">
  <h2>Verdict</h2>
  <p>{esc(summary)}</p>
</div>"""
    factor_list = f"""<ul class="factor-list">
        {"".join(factors_html)}
      </ul>"""
    if unreviewed:
        scorecard_html = f"""<div class="panel">
  <details>
    <summary><strong>10-Factor Scorecard</strong> — all Gray (not reviewed)</summary>
    {factor_list}
  </details>
</div>"""
    else:
        scorecard_html = f"""<div class="panel">
      <h2>10-Factor Scorecard</h2>
      {factor_list}
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(biz.get("name", ""))}{(", " + esc(where)) if where else ""} — {esc(category_label(cat))}, {esc(biz.get("city") or "Fredericksburg")} · Christ-Centered Commerce</title>
  <meta name="description" content="{esc(biz.get('name', ''))}{(" at " + esc(where)) if where else ""} ({esc(category_label(cat))}, {esc(biz.get('city') or 'Fredericksburg area')}) — {esc(contact)} on file, and the 10-Factor Christ-Centered Commerce scorecard." />
  <link rel="stylesheet" href="../assets/commerce.css" />
  {json_ld(biz, tags)}
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
    <a class="back" href="../categories/{esc(cat_slug)}.html">← All {esc(category_label(cat))} listings</a>
    <header class="profile-header">
      <div class="overall-band {overall}">{BAND_LABEL.get(overall, overall.upper())}</div>
      <h1 class="profile-title">{esc(biz.get("name", ""))}</h1>
      <div class="meta">{" · ".join(x for x in meta_bits if x)}</div>
      <div class="color-profile-chip"><span>{esc(prof)}</span></div>
    </header>

    {closed_panel(biz)}
    {contact_panel(biz, tags)}{own_words_panel(biz)}

    {verdict_html}

    {owner_html}
    {network_html}

    {scorecard_html}

    {src_html}

    <div class="panel">
      <h2>See an error?</h2>
      <p>Submit a correction with sources.</p>
      <div class="cta-row"><a class="btn solid" href="{esc(suggest_href)}">Submit a correction →</a></div>
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
    osm = load_osm_tags()
    if slugs:
        businesses = [b for b in businesses if b.get("slug") in slugs]
    OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    every = {b.get("slug"): b for b in data.get("businesses") or []}
    # curated slug -> OSM tags of a folded duplicate (hours for listings with no OSM source)
    dup_tags = {b["duplicate_of"]: osm_tags_for(b, osm) for b in every.values() if b.get("duplicate_of")}
    for biz in businesses:
        slug = biz.get("slug")
        if not slug:
            continue
        path = OUT / f"{slug}.html"
        target = every.get(biz.get("duplicate_of") or "")
        if target and biz.get("publish") is False:
            path.write_text(render_duplicate(biz, target))
        else:
            path.write_text(render_profile(biz, osm, dup_tags.get(slug)))
        count += 1
    print(f"rendered {count} profiles -> {OUT}")


if __name__ == "__main__":
    main()
