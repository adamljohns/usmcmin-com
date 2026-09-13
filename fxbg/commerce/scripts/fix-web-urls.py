#!/usr/bin/env python3
"""Correct dead/wrong web URLs in businesses.json (2026-08-24 grind)."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"

# slug -> (new web, optional phone patch, optional source to append)
FIXES: dict[str, tuple[str, str | None, dict | None]] = {
    "holy-cross-academy": (
        "https://www.holycrossweb.com/",
        None,
        {"label": "Holy Cross Academy — official site", "url": "https://www.holycrossweb.com/"},
    ),
    "marie-william-capital": (
        "https://mariewilliamcapital.com/",
        None,
        {"label": "Marie William Capital — official site", "url": "https://mariewilliamcapital.com/"},
    ),
    "purvis-ford": (
        "https://www.purvisford.net/",
        None,
        {"label": "Purvis Ford — official dealer site", "url": "https://www.purvisford.net/"},
    ),
    "primavera-pizzeria-fxbg": (
        "https://www.orderprimaverapizzaandgrill.com/",
        None,
        {
            "label": "Primavera Pizzeria & Grill — 600 William St ordering site",
            "url": "https://www.orderprimaverapizzaandgrill.com/",
        },
    ),
    "stockyards-fxbg": (
        "https://www.stockyardsfxbg.com/",
        "(540) 670-2884",
        {"label": "Stockyards Restaurant & Bar — official site", "url": "https://www.stockyardsfxbg.com/"},
    ),
    "du-jardin-home-garden-fxbg": (
        "https://www.facebook.com/dujardinhomeandgarden/",
        None,
        {
            "label": "Du Jardin Home and Garden — Facebook (no active standalone site)",
            "url": "https://www.facebook.com/dujardinhomeandgarden/",
        },
    ),
    "bradford-pest-control-fxbg": (
        "https://www.bradfordbug.com/",
        None,
        {"label": "Bradford Pest Control — bradfordbug.com", "url": "https://www.bradfordbug.com/"},
    ),
    "lets-break-bread-fxbg": (
        "https://www.facebook.com/letsbreakbreadfxbg/",
        None,
        {
            "label": "Let's Break Bread — Facebook (domain dead; social verified)",
            "url": "https://www.facebook.com/letsbreakbreadfxbg/",
        },
    ),
    "modern-plumbing-concepts-fxbg": (
        "https://www.facebook.com/ModernPlumbingConcepts/",
        None,
        {
            "label": "Modern Plumbing Concepts — Facebook (modernplumbingconcepts.com dead)",
            "url": "https://www.facebook.com/ModernPlumbingConcepts/",
        },
    ),
}


def main() -> None:
    data = json.loads(DATA.read_text())
    changed = []
    for biz in data.get("businesses") or []:
        slug = biz.get("slug")
        if slug not in FIXES:
            continue
        new_web, phone, src = FIXES[slug]
        old_web = biz.get("web")
        if old_web != new_web:
            biz["web"] = new_web
            changed.append(f"{slug}: web {old_web} -> {new_web}")
        if phone and not biz.get("phone"):
            biz["phone"] = phone
            changed.append(f"{slug}: phone set {phone}")
        if src:
            sources = biz.setdefault("sources", [])
            urls = {(s.get("url") or "").rstrip("/") for s in sources}
            key = src["url"].rstrip("/")
            if key not in urls:
                sources.insert(0, src)
                changed.append(f"{slug}: source added")
    data["updated"] = date.today().isoformat()
    DATA.write_text(json.dumps(data, separators=(",", ":")))
    print(f"fixed {len(FIXES)} slugs, {len(changed)} edits")
    for line in changed:
        print(" ", line)


if __name__ == "__main__":
    main()
