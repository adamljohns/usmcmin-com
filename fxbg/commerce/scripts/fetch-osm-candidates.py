#!/usr/bin/env python3
"""Download FXBG-area POIs from OpenStreetMap Overpass → data/osm-candidates.json."""
from __future__ import annotations

import json
import ssl
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "osm-candidates.json"

# Fredericksburg · Stafford · Spotsylvania corridor
BBOX = (38.12, -77.72, 38.48, -77.28)  # south, west, north, east

OVERPASS_SERVERS = (
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass-api.de/api/interpreter",
)

QUERY = """
[out:json][timeout:90];
(
  nwr["name"]["shop"]({s},{w},{n},{e});
  nwr["name"]["amenity"~"restaurant|cafe|fast_food|bar|pub|pharmacy|bank|dentist|doctors|veterinary|fuel|car_repair|hairdresser|beauty|clothes|hardware|furniture|electronics|mobile_phone|car|bakery|butcher|convenience|supermarket|marketplace|ice_cream|optician|travel_agency|insurance|accountant|lawyer|estate_agent"]({s},{w},{n},{e});
  nwr["name"]["office"]({s},{w},{n},{e});
  nwr["name"]["craft"]({s},{w},{n},{e});
  nwr["name"]["healthcare"]({s},{w},{n},{e});
);
out center tags;
"""


def tiles(bbox: tuple[float, float, float, float], parts: int = 2):
    s, w, n, e = bbox
    lat_step = (n - s) / parts
    lon_step = (e - w) / parts
    for i in range(parts):
        for j in range(parts):
            yield (s + i * lat_step, w + j * lon_step, s + (i + 1) * lat_step, w + (j + 1) * lon_step)


def run_query(bbox: tuple[float, float, float, float]) -> list:
    q = QUERY.format(s=bbox[0], w=bbox[1], n=bbox[2], e=bbox[3])
    body = q.encode()
    last_err = None
    for base in OVERPASS_SERVERS:
        req = urllib.request.Request(base, data=body, headers={**UA, "Content-Type": "text/plain"})
        ctx = ssl.create_default_context()
        try:
            with urllib.request.urlopen(req, timeout=120, context=ctx) as r:
                raw = json.load(r)
            return raw.get("elements") or []
        except Exception as e:
            last_err = e
    raise RuntimeError(last_err)

UA = {"User-Agent": "C5iSR-CommerceBot/0.4 (+https://usmcmin.com/fxbg/commerce/)"}


def latlng(el: dict) -> tuple[float | None, float | None]:
    if "lat" in el and "lon" in el:
        return float(el["lat"]), float(el["lon"])
    c = el.get("center") or {}
    if "lat" in c and "lon" in c:
        return float(c["lat"]), float(c["lon"])
    return None, None


def main() -> None:
    seen: set[int | str] = set()
    rows = []
    for tile in tiles(BBOX, 2):
        for el in run_query(tile):
            oid = el.get("id")
            if oid in seen:
                continue
            seen.add(oid)
            tags = el.get("tags") or {}
            name = (tags.get("name") or "").strip()
            if not name or len(name) < 2:
                continue
            lat, lng = latlng(el)
            if lat is None:
                continue
            rows.append(
                {
                    "osm_id": el.get("id"),
                    "osm_type": el.get("type"),
                    "name": name,
                    "lat": lat,
                    "lng": lng,
                    "tags": tags,
                }
            )
    payload = {
        "fetched": date.today().isoformat(),
        "bbox": {"south": BBOX[0], "west": BBOX[1], "north": BBOX[2], "east": BBOX[3]},
        "count": len(rows),
        "candidates": rows,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(f"wrote {len(rows)} OSM candidates -> {OUT}")


if __name__ == "__main__":
    main()
