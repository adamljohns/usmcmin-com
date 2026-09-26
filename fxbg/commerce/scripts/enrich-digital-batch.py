#!/usr/bin/env python3
"""HEAD-probe web URLs for a batch of slugs only."""
from __future__ import annotations

import importlib.util
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"
SPEC = importlib.util.spec_from_file_location(
    "edi", ROOT / "scripts" / "enrich-digital-integrity.py"
)
edi = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(edi)  # type: ignore


def main() -> None:
    slugs = set(sys.argv[1:])
    if not slugs:
        print("usage: enrich-digital-batch.py slug [slug...]", file=sys.stderr)
        sys.exit(2)
    data = json.loads(DATA.read_text())
    n = 0
    for biz in data.get("businesses") or []:
        if biz.get("slug") not in slugs:
            continue
        url = (biz.get("web") or "").strip()
        scores = biz.setdefault("scores", {})
        if not url:
            continue
        pr = edi.probe(url)
        band, meta = edi.band_from_probe(pr, bool(biz.get("phone")))
        scores["digital_integrity"] = band
        meta["verified"] = date.today().isoformat()
        scores["digital_integrity_meta"] = meta
        n += 1
    data["updated"] = date.today().isoformat()
    DATA.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print(f"digital batch probe: {n} listing(s)")


if __name__ == "__main__":
    main()
