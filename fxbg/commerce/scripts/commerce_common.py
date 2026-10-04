"""Shared helpers for the commerce page builders (render-profile, build-categories).

Everything here only re-presents facts already on file: businesses.json and the
OpenStreetMap tags cached in data/osm-candidates.json. Nothing is looked up or
guessed.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
OSM_CACHE = ROOT / "data" / "osm-candidates.json"

# Address strings that are placeholders, not street addresses.
_PLACEHOLDER_RE = re.compile(
    r"^(address on file|fredericksburg( area| region|, va)?|spotsylvania, va|multiple |"
    r"fredericksburg / |fredericksburg area \(|garrisonville )",
    re.I,
)

LABEL_OVERRIDES = {
    "professional-cpa-legal-insurance": "CPA, Legal & Insurance",
    "hvac": "HVAC",
    "bar-restaurant": "Bar & Restaurant",
    "bakery-cafe": "Bakery & Cafe",
    "brewery-restaurant": "Brewery & Restaurant",
    "restaurant-bbq": "BBQ Restaurant",
    "restaurant-american-diner": "American Diner",
    "nursery-garden-center": "Nursery & Garden Center",
    "auto-repair": "Auto Repair",
    "auto-dealer": "Auto Dealer",
    "gas-station": "Gas Station",
}

_DAYS = {"Mo": "Mon", "Tu": "Tue", "We": "Wed", "Th": "Thu", "Fr": "Fri", "Sa": "Sat", "Su": "Sun", "PH": "Holidays"}


def category_label(cat: str) -> str:
    cat = cat or "other"
    if cat in LABEL_OVERRIDES:
        return LABEL_OVERRIDES[cat]
    if cat.startswith("restaurant-") and cat != "restaurant-fast-casual":
        return cat.split("-", 1)[1].replace("-", " ").title() + " Restaurant"
    return cat.replace("-", " ").title()


def real_address(biz: dict) -> str:
    """Street address (starts with a house number) if one is on file, else ''."""
    addr = (biz.get("address") or "").strip()
    if not addr or _PLACEHOLDER_RE.match(addr) or not re.match(r"\d", addr):
        return ""
    return addr


def location_note(biz: dict) -> str:
    """A descriptive location on file that is not a street address ('' if none)."""
    addr = (biz.get("address") or "").strip()
    if not addr or real_address(biz) or addr.lower().startswith("address on file"):
        return ""
    if addr.lower().rstrip(".") in {"fredericksburg area", "fredericksburg, va", "fredericksburg region", "spotsylvania, va"}:
        return ""
    return addr


def load_osm_tags() -> dict[str, dict]:
    """Map OpenStreetMap URL -> tags, from the cached candidate pull."""
    if not OSM_CACHE.exists():
        return {}
    data = json.loads(OSM_CACHE.read_text())
    out = {}
    for c in data.get("candidates") or []:
        out[f"https://www.openstreetmap.org/{c.get('osm_type')}/{c.get('osm_id')}"] = c.get("tags") or {}
    return out


def osm_tags_for(biz: dict, osm: dict[str, dict]) -> dict:
    for s in biz.get("sources") or []:
        url = s.get("url") or ""
        if "openstreetmap.org/" in url:
            return osm.get(url, {})
    return {}


def pretty_hours(raw: str) -> list[str]:
    """OSM opening_hours -> display lines. Unparsed text is shown as-is."""
    raw = (raw or "").strip()
    if not raw:
        return []
    if raw == "24/7":
        return ["Open 24 hours"]
    lines = []
    for part in re.split(r";\s*", raw):
        part = part.strip()
        if not part:
            continue
        part = re.sub(r"\b(Mo|Tu|We|Th|Fr|Sa|Su|PH)\b", lambda m: _DAYS[m.group(1)], part)
        part = part.replace("00:00-00:00", "open 24 hours").replace(" off", " closed")
        if re.match(r"^\d", part):
            part = "Daily " + part
        lines.append(part)
    return lines


def directions_url(biz: dict) -> str:
    addr = real_address(biz)
    if addr:
        q = ", ".join(x for x in (biz.get("name"), addr, biz.get("city"), biz.get("state"), biz.get("zip")) if x)
        return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(q)
    # OSM coordinates are surveyed points; hand-entered listings often carry a rough
    # area centroid, so search those by name + town instead.
    if biz.get("ingest_source") == "osm" and biz.get("lat") is not None and biz.get("lng") is not None:
        return f"https://www.google.com/maps/search/?api=1&query={biz['lat']},{biz['lng']}"
    q = ", ".join(x for x in (biz.get("name"), biz.get("city") or "Fredericksburg", biz.get("state") or "VA") if x)
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(q)


def display_phone(phone: str) -> str:
    """US numbers as (540) 555-1234; anything else (extensions, multiple numbers) as-is."""
    digits = re.sub(r"\D", "", phone or "")
    if len(digits) == 11 and digits[0] == "1":
        digits = digits[1:]
    if len(digits) == 10 and re.fullmatch(r"[+\d\s().\-]+", (phone or "").strip()):
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return (phone or "").strip()


def tel_href(phone: str) -> str:
    main = re.split(r"\s*(?:x|ext\.?|extension|/|;|,| or )\s*", phone or "", maxsplit=1, flags=re.I)[0]
    digits = re.sub(r"[^\d+]", "", main)
    return f"tel:{digits}" if len(digits) >= 10 else ""


def search_terms(biz: dict, tags: dict) -> str:
    """Extra words a neighbour might type (cuisine, OSM shop/craft type)."""
    bits = []
    for k in ("cuisine", "shop", "amenity", "craft", "office", "healthcare", "healthcare:speciality", "brand"):
        v = tags.get(k)
        if v and v != "yes":
            bits.append(v.replace(";", " ").replace("_", " "))
    for c in biz.get("categories_secondary") or []:
        bits.append(c.replace("-", " "))
    return " ".join(bits).lower()
