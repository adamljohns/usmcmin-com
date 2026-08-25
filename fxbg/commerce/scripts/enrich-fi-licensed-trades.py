#!/usr/bin/env python3
"""Affirmative FI upgrades for licensed trades with sourced evidence (v0.4)."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"

TRADE_CATS = {
    "plumbing",
    "hvac",
    "roofing",
    "electrical",
    "electrical-contractor",
    "pest-control",
    "auto-repair",
    "home-services",
    "home-builder",
    "landscaping",
    "flooring",
    "orthodontics",
    "property-management",
    "esthetics",
    "remodeling",
    "appliance-repair",
    "home-cleaning",
    "signs-graphics",
    "fence",
    "inspection",
}

FI_AFFIRMATIVE = re.compile(
    r"\b(licensed|bonded|insured|bbb\s*a\+?|bbb\s+accredited|state\s+license|"
    r"contractor\s+license|professional\s+license|class\s+[a-d]\s+license|"
    r"va\s+class\s+[a-d]|certified\s+contractor|certainteed\s+certified|"
    r"registered\s+contractor|fully\s+insured|dporc|board\s+of\s+dentistry)\b",
    re.I,
)

WEAK_SOURCE = re.compile(
    r"(chamber|yelp|facebook|google\.com/maps|tripadvisor|botb|readerschoice|"
    r"instagram|twitter|x\.com|nextdoor|birdeye|homeadvisor|porch\.com|hubbiz|"
    r"101apartmentforrent|1stpriorityplumbing)",
    re.I,
)

STRONG_SOURCE = re.compile(
    r"(bbb\.org|certainteed\.com|dporc\.virginia\.gov|dpor\.virginia\.gov|"
    r"\.gov/|state\.va\.us|fit20\.com)",
    re.I,
)


def combined_text(biz: dict) -> str:
    parts = [
        biz.get("owner_operator") or "",
        biz.get("summary") or "",
        biz.get("notes_internal") or "",
    ]
    return " ".join(parts)


def official_sources(sources: list) -> list:
    out = []
    for s in sources or []:
        url = s.get("url") or ""
        label = s.get("label") or ""
        if not url:
            continue
        if WEAK_SOURCE.search(url) or WEAK_SOURCE.search(label):
            continue
        out.append(s)
    return out


def has_strong_source(sources: list) -> bool:
    for s in sources or []:
        blob = f"{s.get('url', '')} {s.get('label', '')}"
        if STRONG_SOURCE.search(blob):
            return True
    return False


def qualifies_fi_green(biz: dict) -> tuple[bool, str]:
    text = combined_text(biz)
    sources = biz.get("sources") or []
    official = official_sources(sources)
    if not FI_AFFIRMATIVE.search(text):
        return False, "no affirmative text"
    if has_strong_source(sources):
        return True, "strong regulator/BBB/certifier source"
    if official and re.search(
        r"\b(licensed|bonded|insured|class\s+[a-d]|contractor\s+license|bbb\s*a)\b",
        text,
        re.I,
    ):
        return True, "official source + license/bond/BBB"
    if biz.get("category") in TRADE_CATS and official and len(official) >= 1:
        if re.search(r"\b(certified|bbb)\b", text, re.I):
            return True, "trade + certifier/BBB + official site"
    return False, "insufficient"


def main() -> None:
    data = json.loads(DATA.read_text())
    upgraded = []
    skipped = []
    for biz in data.get("businesses") or []:
        scores = biz.setdefault("scores", {})
        if scores.get("financial_integrity") == "green":
            continue
        ok, reason = qualifies_fi_green(biz)
        if not ok:
            if FI_AFFIRMATIVE.search(combined_text(biz)):
                skipped.append(f"{biz['slug']}: {reason}")
            continue
        scores["financial_integrity"] = "green"
        official = official_sources(biz.get("sources") or [])
        scores["financial_integrity_meta"] = {
            "band": "green",
            "reason": "affirmative",
            "source_count": max(len(official), 1),
            "concern_count": 0,
            "verified": date.today().isoformat(),
            "note": reason,
        }
        upgraded.append(f"{biz['slug']} ({reason})")

    data["updated"] = date.today().isoformat()
    DATA.write_text(json.dumps(data, separators=(",", ":")))
    print(f"FI green upgrades: {len(upgraded)}")
    for line in upgraded:
        print(" ", line)
    if skipped:
        print(f"skipped with partial signal: {len(skipped)}")
        for line in skipped[:8]:
            print(" ", line)


if __name__ == "__main__":
    main()
