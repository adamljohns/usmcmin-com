#!/usr/bin/env python3
"""Import next N OpenStreetMap candidates as gray stub listings in businesses.json."""
from __future__ import annotations

import json
import math
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"
CACHE = ROOT / "data" / "osm-candidates.json"

AMENITY_MAP = {
    "restaurant": "restaurant",
    "fast_food": "restaurant",
    "cafe": "cafe",
    "bar": "bar-restaurant",
    "pub": "bar-restaurant",
    "pharmacy": "pharmacy",
    "bank": "bank",
    "dentist": "dental",
    "doctors": "medical",
    "veterinary": "veterinary",
    "fuel": "gas-station",
    "car_repair": "auto-repair",
    "hairdresser": "salon",
    "beauty": "salon",
    "clothes": "retail",
    "hardware": "hardware",
    "furniture": "retail",
    "electronics": "retail",
    "mobile_phone": "retail",
    "car": "auto-dealer",
    "bakery": "bakery",
    "butcher": "retail",
    "convenience": "convenience",
    "supermarket": "grocery",
    "marketplace": "retail",
    "ice_cream": "restaurant",
    "optician": "retail",
    "travel_agency": "professional-services",
    "insurance": "insurance",
    "accountant": "professional-cpa-legal-insurance",
    "lawyer": "professional-cpa-legal-insurance",
    "estate_agent": "real-estate",
}

SHOP_MAP = {
    "hairdresser": "salon",
    "beauty": "salon",
    "clothes": "retail",
    "hardware": "hardware",
    "furniture": "retail",
    "electronics": "retail",
    "mobile_phone": "retail",
    "car": "auto-dealer",
    "bakery": "bakery",
    "butcher": "retail",
    "convenience": "convenience",
    "supermarket": "grocery",
    "mall": "retail",
    "department_store": "retail",
    "gift": "retail",
    "jewelry": "retail",
    "shoes": "retail",
    "sports": "retail",
    "pet": "retail",
    "florist": "retail",
    "trade": "home-services",
    "car_repair": "auto-repair",
    "tyres": "auto-repair",
}


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:80] or "listing"


def norm_name(name: str) -> str:
    s = name.lower()
    for tok in (" llc", " inc", " corp", " co.", " company", " the "):
        s = s.replace(tok, " ")
    return re.sub(r"\s+", " ", s).strip()


def haversine_m(a: tuple[float, float], b: tuple[float, float]) -> float:
    lat1, lon1 = a
    lat2, lon2 = b
    r = 6371000
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    x = math.sin(dlat / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlon / 2) ** 2
    return 2 * r * math.asin(math.sqrt(x))


def category_from_tags(tags: dict) -> str:
    if tags.get("shop"):
        return SHOP_MAP.get(tags["shop"], "retail")
    if tags.get("amenity"):
        return AMENITY_MAP.get(tags["amenity"], "retail")
    if tags.get("office"):
        return "professional-services"
    if tags.get("craft"):
        return "home-services"
    if tags.get("healthcare"):
        return "medical"
    return "retail"


def city_from_tags(tags: dict) -> str:
    for k in ("addr:city", "addr:suburb", "addr:county"):
        if tags.get(k):
            return tags[k]
    return "Fredericksburg area"


def default_scores() -> dict:
    base = {f: "gray" for f in (
        "ownership", "truth", "christ_centered_brand", "family_safety", "worker_dignity",
        "community_fruit", "reliability", "financial_integrity", "digital_integrity",
        "network_worthiness",
    )}
    for f in list(base):
        base[f"{f}_meta"] = {"band": "gray", "reason": "insufficient", "source_count": 0, "concern_count": 0}
    return base


def existing_keys(businesses: list) -> tuple[set[str], set[str], list[tuple[str, float, float]]]:
    slugs: set[str] = set()
    names: set[str] = set()
    geo: list[tuple[str, float, float]] = []
    for b in businesses:
        slugs.add(b.get("slug") or "")
        names.add(norm_name(b.get("name") or ""))
        if b.get("lat") is not None and b.get("lng") is not None:
            geo.append((norm_name(b.get("name") or ""), float(b["lat"]), float(b["lng"])))
    return slugs, names, geo


def duplicate(name: str, lat: float, lng: float, geo: list) -> bool:
    nn = norm_name(name)
    for gn, glat, glng in geo:
        if gn == nn and haversine_m((lat, lng), (glat, glng)) < 120:
            return True
        if haversine_m((lat, lng), (glat, glng)) < 35 and (
            nn.startswith(gn[:12]) or gn.startswith(nn[:12])
        ):
            return True
    return False


def stub_from_osm(row: dict, slug: str) -> dict:
    tags = row.get("tags") or {}
    web = (tags.get("website") or tags.get("contact:website") or "").strip()
    if web and not web.startswith("http"):
        web = "https://" + web
    phone = tags.get("phone") or tags.get("contact:phone") or ""
    addr_parts = [
        tags.get("addr:housenumber"),
        tags.get("addr:street"),
    ]
    address = " ".join(p for p in addr_parts if p).strip() or "Address on file (OSM)"
    sources = [
        {
            "label": "OpenStreetMap — community map import",
            "url": f"https://www.openstreetmap.org/{row.get('osm_type', 'node')}/{row.get('osm_id')}",
        }
    ]
    if web:
        sources.insert(0, {"label": "Official site (OSM tag)", "url": web})
    return {
        "id": slug,
        "name": row["name"],
        "slug": slug,
        "category": category_from_tags(tags),
        "lat": row["lat"],
        "lng": row["lng"],
        "address": address,
        "city": city_from_tags(tags),
        "state": tags.get("addr:state") or "VA",
        "zip": tags.get("addr:postcode") or "",
        "region": "FXBG",
        "web": web or "",
        "phone": phone,
        "owner_operator": "Imported from OpenStreetMap — pending Christ-centered commerce review.",
        "overall": "gray",
        "featured": False,
        "scores": default_scores(),
        "summary": "Community-sourced map listing — not yet evidence-scored. Gray overall until review.",
        "sources": sources,
        "ingest_source": "osm",
        "ingest_date": date.today().isoformat(),
        "publish": True,
        "claimed": False,
        "c5isr_fit": "watchlist",
        "updated": date.today().isoformat(),
    }


def main() -> None:
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    if not CACHE.is_file():
        print(f"missing {CACHE} — run fetch-osm-candidates.py first", file=sys.stderr)
        sys.exit(2)
    cache = json.loads(CACHE.read_text())
    data = json.loads(DATA.read_text())
    businesses = data.get("businesses") or []
    slugs, names, geo = existing_keys(businesses)
    added: list[str] = []
    skipped = 0
    for row in cache.get("candidates") or []:
        if len(added) >= limit:
            break
        name = row.get("name") or ""
        if duplicate(name, row["lat"], row["lng"], geo):
            skipped += 1
            continue
        base = slugify(name)
        slug = base
        n = 2
        while slug in slugs:
            slug = f"{base}-{n}"
            n += 1
        slugs.add(slug)
        names.add(norm_name(name))
        geo.append((norm_name(name), row["lat"], row["lng"]))
        businesses.append(stub_from_osm(row, slug))
        added.append(slug)
    data["businesses"] = businesses
    data["updated"] = date.today().isoformat()
    meta = data.setdefault("osm_ingest", {})
    meta["last_import"] = date.today().isoformat()
    meta["last_added_count"] = len(added)
    meta["last_skipped_dupe"] = skipped
    meta["total_after"] = len(businesses)
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"imported {len(added)} stub(s), skipped {skipped} dupes, total {len(businesses)}")


if __name__ == "__main__":
    main()
