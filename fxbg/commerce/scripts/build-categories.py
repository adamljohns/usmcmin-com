#!/usr/bin/env python3
"""Generate category landing pages under categories/ (v0.4)."""
from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path

from commerce_common import category_label, display_phone, load_osm_tags, osm_tags_for, real_address, search_terms

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
    return category_label(cat)


def card(biz: dict) -> str:
    overall = str(biz.get("overall") or "gray").lower()
    color = BAND_COLOR.get(overall, "#888")
    return f"""<a class="biz-card" href="../business/{esc(biz['slug'])}.html" style="border-color:{color}55">
  <div class="eyebrow" style="color:{color}">{overall.upper()}</div>
  <h3>{esc(biz.get('name', ''))}</h3>
  <div class="meta">{esc(real_address(biz) or biz.get('city') or '')}{(' · ' + esc(display_phone(biz['phone']))) if biz.get('phone') else ''}</div>
</a>"""


def render_category(cat: str, listings: list[dict]) -> str:
    overall = Counter(str(b.get("overall", "gray")).lower() for b in listings)
    bands = " · ".join(f"{overall[c]} {c.title()}" for c in ("green", "yellow", "gray", "red") if overall.get(c))
    band_rank = {"green": 0, "yellow": 1, "gray": 2, "red": 3, "black": 4}
    cards = "\n".join(card(b) for b in sorted(
        listings, key=lambda x: (band_rank.get(str(x.get("overall") or "gray").lower(), 9), x.get("name", ""))))
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
    <a href="../suggest.html">Suggest</a>
  </nav>
  <div class="wrap">
    <a class="back" href="index.html">← All categories</a>
    <div class="module-tag">{esc(label(cat))}</div>
    <h1 class="profile-title">{esc(label(cat))}</h1>
    <p class="meta">{len(listings)} listing{'s' if len(listings) != 1 else ''} · {esc(bands)} · scored listings first · <a href="../directory.html?cat={esc(cat)}">search &amp; filter these →</a></p>
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


GROUPS = [
    ("Home & Trades", ("plumb", "hvac", "electric", "roof", "landscap", "home-", "flooring", "pest", "moving", "appliance",
                       "hardware", "builder", "painting", "construction", "home-cleaning", "contractor", "fence", "locksmith", "self-storage", "nursery-garden", "pressure")),
    ("Auto", ("auto", "car-", "tire", "gas-station", "motorcycle")),
    ("Food & Drink", ("restaurant", "cafe", "coffee", "bakery", "brew", "bar-", "catering", "grocery", "convenience",
                      "food", "pizza", "deli", "winery", "liquor", "ice-cream", "donut", "butcher")),
    ("Health & Care", ("medical", "dental", "dentist", "orthodont", "chiropract", "physical-therapy", "mental-health", "pharmacy",
                       "audiology", "oncology", "primary-care", "eye-care", "optometr", "health", "veterinary", "dermatolog",
                       "funeral", "cardiolog", "allergy", "hospital", "acupunct", "counsel", "assisted-living", "massage")),
    ("Family, School & Church", ("childcare", "preschool", "school", "tutor", "nonprofit", "church", "ministry", "pet-", "dog-")),
    ("Personal Care & Fitness", ("salon", "barber", "esthetic", "tattoo", "fitness", "gym", "spa", "nail", "martial-arts", "dance", "golf")),
    ("Money, Legal & Property", ("bank", "credit-union", "financial", "accounting", "cpa", "law", "legal", "insurance",
                                 "real-estate", "professional", "government", "check-cashing", "consult", "mortgage")),
    ("Shopping", ("retail", "furniture", "jewelry", "florist", "bookstore", "thrift", "tobacco", "bicycle", "art-", "gift",
                  "clothing", "boutique", "antique", "printing", "pet-supply", "photography", "dry-cleaning")),
]


def group_for(cat: str) -> str:
    for name, keys in GROUPS:
        if any(k in cat for k in keys):
            return name
    return "More"


def render_index(counts: list[tuple[str, int]]) -> str:
    grouped: dict[str, list[tuple[str, int]]] = {}
    for cat, n in counts:
        grouped.setdefault(group_for(cat), []).append((cat, n))
    sections = []
    for name in [g for g, _ in GROUPS] + ["More"]:
        items = sorted(grouped.get(name, []), key=lambda x: label(x[0]))
        if not items:
            continue
        links = " · ".join(
            f'<a href="{esc(slugify(cat))}.html">{esc(label(cat))}</a> <span class="meta">({n})</span>' for cat, n in items)
        total = sum(n for _, n in items)
        sections.append(f"""<div class="panel">
  <h2>{esc(name)} <span class="meta">· {total} listings</span></h2>
  <p class="cat-links">{links}</p>
</div>""")
    rows = "\n".join(sections)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Categories — Christ-Centered Commerce</title>
  <link rel="stylesheet" href="../assets/commerce.css" />
  <style>.cat-links {{ line-height:2; }} .cat-links a {{ white-space:nowrap; }} .cat-links .meta {{ display:inline; margin:0; }}</style>
</head>
<body>
  <div class="soft-banner">Rubric v0.4 · Browse by category</div>
  <nav class="site-nav">
    <a href="../index.html">Hub</a>
    <a href="../directory.html">Directory</a>
    <a href="index.html" class="active">Categories</a>
    <a href="../methodology.html">Methodology</a>
    <a href="../about.html">About</a>
    <a href="../suggest.html">Suggest</a>
  </nav>
  <div class="wrap">
    <div class="module-tag">Categories</div>
    <h1 class="profile-title">Browse by <span style="color:var(--gold)">Category</span></h1>
    <p class="meta">{len(counts)} categories · tap for filtered listings · <a href="../directory.html">or search the directory →</a></p>
    {rows}
  </div>
</body>
</html>
"""


def main() -> None:
    data = json.loads(DATA.read_text())
    businesses = data.get("businesses") or []
    by_cat: dict[str, list] = {}
    for biz in businesses:
        if biz.get("publish") is False:
            continue
        cat = biz.get("category") or "other"
        by_cat.setdefault(cat, []).append(biz)
    counts = sorted(by_cat.items(), key=lambda x: (-len(x[1]), x[0]))
    OUT.mkdir(parents=True, exist_ok=True)
    for cat, listings in counts:
        path = OUT / f"{slugify(cat)}.html"
        path.write_text(render_category(cat, listings))
    (OUT / "index.html").write_text(render_index([(c, len(l)) for c, l in counts]))
    print(f"built categories/index.html + {len(counts)} category pages -> {OUT}")
    write_directory_index(data, businesses)


BOILERPLATE_PREFIX = "Community-sourced map listing"


def write_directory_index(data: dict, businesses: list[dict]) -> None:
    """Slim JSON for directory.html and the hub map (businesses.json is ~5 MB)."""
    osm = load_osm_tags()
    rows = []
    for b in businesses:
        if b.get("publish") is False:
            continue
        summary = b.get("summary") or ""
        if summary.startswith(BOILERPLATE_PREFIX):
            summary = ""
        row = {
            "s": b.get("slug"),
            "n": b.get("name"),
            "c": b.get("category") or "other",
            "o": str(b.get("overall") or "gray").lower(),
            "a": real_address(b),
            "t": b.get("city") or "",
            "p": display_phone(b.get("phone") or ""),
            "w": 1 if b.get("web") else 0,
            "k": search_terms(b, osm_tags_for(b, osm)),
            "d": summary[:160],
        }
        if b.get("lat") is not None and b.get("lng") is not None:
            row["y"], row["x"] = round(b["lat"], 5), round(b["lng"], 5)
        if b.get("featured"):
            row["f"] = 1
        if b.get("adam_visited"):
            row["v"] = 1
        rows.append({k: v for k, v in row.items() if v not in ("", 0, None)})
    out = {
        "updated": data.get("updated"),
        "rubric_version": data.get("rubric_version"),
        "labels": {c: category_label(c) for c in sorted({r["c"] for r in rows})},
        "rows": rows,
    }
    path = ROOT / "data" / "directory-index.json"
    path.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
    print(f"wrote {path.name}: {len(rows)} rows, {path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
