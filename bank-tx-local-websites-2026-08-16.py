#!/usr/bin/env python3
"""Bank official website URLs for TX local roster scaffolds (2026-08-16).

Picks the best non-TML official page from each record's sources[] so the
local grind selector + extractor can fetch them. Does not score anything.
"""
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
SCORECARD = BASE / "data" / "scorecard.json"

# slug -> preferred official website (verified from sources[] this turn)
WEBSITES = {
    "joe-boles": "https://www.glenrosetexas.org/city-council",
    "george-freas": "https://www.glenrosetexas.org/city-council",
    "laurin-mapes": "https://www.glenrosetexas.org/city-council",
    "richard-bruning": "https://www.glenrosetexas.org/city-council",
    "danny-l-chambers": "https://www.somervell.co/341/County-Judge",
    "jeff-harris": "https://www.somervell.co/362/Precinct-1",
    "richard-talavera": "https://www.somervell.co/363/Precinct-2",
    "chip-joslin": "https://www.somervell.co/175/Commissioners-Court",
    "wade-busch": "https://www.somervell.co/175/Commissioners-Court",
    "christopher-boedeker": "https://www.johnsoncountytx.org/government/county-judge",
    "rick-bailey": "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-1",
    "kenny-howell": "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-2",
    "mike-white": "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-3",
    "larry-woolley": "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-4",
    "jason-turney": "https://cityofjosephinetx.com/government/city-council/",
    "chris-hill": "https://www.collincountytx.gov/Government/Commissioners-Court/county-judge",
    "bobby-w-stovall": "https://www.huntcounty.net/page/hunt.countyjudge",
}


def main():
    data = json.loads(SCORECARD.read_text())
    by_slug = {c["slug"]: c for c in data["candidates"]}
    changed = []
    for slug, url in WEBSITES.items():
        c = by_slug.get(slug)
        if not c:
            print(f"SKIP missing slug: {slug}", file=sys.stderr)
            continue
        if c.get("website") == url:
            continue
        c["website"] = url
        changed.append(slug)
    if not changed:
        print("no website changes needed")
        return
    SCORECARD.write_text(json.dumps(data, separators=(",", ":")))
    print(f"banked website for {len(changed)} TX locals:", ", ".join(changed))
    subprocess.check_call([sys.executable, "build-data.py", "--quiet"], cwd=BASE)


if __name__ == "__main__":
    main()
