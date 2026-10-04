#!/usr/bin/env python3
"""One-time re-file of OSM stub listings whose category came from the old
fall-through mapping (2026-10-04, MBP-1003-NIGHT).

Only touches listings with ingest_source == "osm" whose current category is
exactly what the pre-2026-10-04 importer derived from their OSM tags — i.e.
nobody has hand-edited it since. The new category comes from the same OSM tags
via import-osm-stubs.category_from_tags. Usage: recategorize-osm-stubs.py OLD_IMPORTER.py [--apply]
"""
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from commerce_common import load_osm_tags, osm_tags_for  # noqa: E402

DATA = HERE.parent / "data" / "businesses.json"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    old = load(Path(sys.argv[1]), "old_import")
    new = load(HERE / "import-osm-stubs.py", "new_import")
    apply = "--apply" in sys.argv
    data = json.loads(DATA.read_text())
    osm = load_osm_tags()
    moves = Counter()
    changed = []
    for b in data["businesses"]:
        if b.get("ingest_source") != "osm":
            continue
        tags = osm_tags_for(b, osm)
        if not tags or b.get("category") != old.category_from_tags(tags):
            continue
        cat = new.category_from_tags(tags)
        if cat != b["category"]:
            moves[(b["category"], cat)] += 1
            changed.append(b["slug"])
            if apply:
                b["category"] = cat
    for (a, c), n in moves.most_common():
        print(f"{n:4d}  {a} -> {c}")
    print(f"{len(changed)} listings {'re-filed' if apply else 'would move'}")
    if apply:
        # keep the file's current compact form so the diff is only the moved categories
        DATA.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
