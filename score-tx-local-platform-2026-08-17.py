#!/usr/bin/env python3
"""
score-tx-local-platform-2026-08-17.py — Apply affiliated-source + party-platform
scoring to the Aug-16 TX local roster scaffolds.

Principal lock 2026-08-17 (@MOOPsCursor_bot): score from official affiliated sources
and/or party platform (annotated). More data beats blank boards.

Writes refinements/tx-local-platform-2026-08-17.json and runs refine-records.py.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).parent
OUT = REPO / "refinements" / "tx-local-platform-2026-08-17.json"

RNC_URL = "https://gop.com/platform/"
RNC_ALT = "https://www.presidency.ucsb.edu/documents/2024-republican-party-platform"
TX_DIR = "https://www.txdirectory.com/online/person/"

PLATFORM_NOTE = (
    "Scored from the 2024 Republican National Platform — no individual statement found."
)

# Applicable local-tier cells → TRUE under 2024 RNC platform (local rubric).
R_LOCAL_PLATFORM = {
    "sanctity_of_life": [0, 1],
    "biblical_marriage": [0, 2, 4],
    "family_child_sovereignty": [0, 1, 2],
    "christian_liberty": [0, 2, 3, 4],
    "economic_stewardship": [2],
    "election_integrity": [0, 1, 4],
    "border_immigration": [1, 2],
    "self_defense": [0, 1],
    "public_justice": [0, 1, 2],
    "refuse_state_overreach": [0, 3],
}

# Verified party + primary official source per slug.
OFFICIALS = {
    # Glen Rose — nonpartisan municipal; Somervell County conservative context
    "joe-boles": {
        "party": None,
        "confidence": "party_default",
        "website": "https://www.glenrosetexas.org/city-council",
        "sources": [
            "https://www.glenrosetexas.org/city-council",
            "https://directory.tml.org/profile/city/1112",
        ],
        "note": (
            "Nonpartisan Glen Rose mayor; no individual issue record on official pages. "
            "Party-default R baseline (Somervell County) per Principal affiliated/platform policy 2026-08-17."
        ),
        "use_platform": True,
    },
    "george-freas": {
        "party": None,
        "confidence": "party_default",
        "website": "https://www.glenrosetexas.org/city-council",
        "sources": [
            "https://www.glenrosetexas.org/city-council",
            "https://directory.tml.org/profile/city/1112",
        ],
        "note": "Nonpartisan Glen Rose council; party-default R baseline (Somervell County).",
        "use_platform": True,
    },
    "laurin-mapes": {
        "party": None,
        "confidence": "party_default",
        "website": "https://www.glenrosetexas.org/city-council",
        "sources": [
            "https://www.glenrosetexas.org/city-council",
            "https://directory.tml.org/profile/city/1112",
        ],
        "note": "Nonpartisan Glen Rose council; party-default R baseline (Somervell County).",
        "use_platform": True,
    },
    "richard-bruning": {
        "party": None,
        "confidence": "party_default",
        "website": "https://www.glenrosetexas.org/city-council",
        "sources": [
            "https://www.glenrosetexas.org/city-council",
            "https://directory.tml.org/profile/city/1112",
        ],
        "note": "Nonpartisan Glen Rose council; party-default R baseline (Somervell County).",
        "use_platform": True,
    },
    "stuart-mann": {
        "party": None,
        "confidence": "party_default",
        "website": "https://www.glenrosetexas.org/city-council",
        "sources": [
            "https://www.glenrosetexas.org/city-council",
            "https://www.glenrosetexas.org/city-council/directory-listing/stuart-mann",
        ],
        "note": "Nonpartisan Glen Rose Mayor Pro Tem; party-default R baseline.",
        "use_platform": True,
    },
    "candace-scholz": {
        "party": None,
        "confidence": "party_default",
        "website": "https://www.glenrosetexas.org/city-council",
        "sources": [
            "https://www.glenrosetexas.org/city-council",
            "https://www.glenrosetexas.org/city-council/directory-listing/candace-scholz",
        ],
        "note": "Nonpartisan Glen Rose council; party-default R baseline.",
        "use_platform": True,
    },
    # Somervell — partisan county (R verified txdirectory)
    "danny-l-chambers": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.somervell.co/341/County-Judge",
        "sources": [
            "https://www.somervell.co/341/County-Judge",
            f"{TX_DIR}?id=50276&office=16550",
        ],
        "note": "Somervell County Judge (R, txdirectory). Platform-scored where no individual record.",
        "use_platform": True,
    },
    "jeff-harris": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.somervell.co/362/Precinct-1",
        "sources": ["https://www.somervell.co/362/Precinct-1"],
        "note": "Somervell Pct 1 Commissioner; partisan R county — platform-scored.",
        "use_platform": True,
    },
    "richard-talavera": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.somervell.co/363/Precinct-2",
        "sources": ["https://www.somervell.co/363/Precinct-2"],
        "note": "Somervell Pct 2 Commissioner; platform-scored.",
        "use_platform": True,
    },
    "chip-joslin": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.somervell.co/175/Commissioners-Court",
        "sources": ["https://www.somervell.co/175/Commissioners-Court"],
        "note": "Somervell Pct 3 Commissioner; platform-scored.",
        "use_platform": True,
    },
    "wade-busch": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.somervell.co/175/Commissioners-Court",
        "sources": ["https://www.somervell.co/175/Commissioners-Court"],
        "note": "Somervell Pct 4 Commissioner; platform-scored.",
        "use_platform": True,
    },
    # Johnson — partisan county (R)
    "christopher-boedeker": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.johnsoncountytx.org/government/county-judge",
        "sources": [
            "https://www.johnsoncountytx.org/government/county-judge",
            f"{TX_DIR}?id=69011",
        ],
        "note": "Johnson County Judge (R); former prosecutor + Cleburne council. Platform-scored gaps.",
        "use_platform": True,
        "extra": {
            "public_justice": {
                "0": {
                    "v": True,
                    "src": ["https://www.johnsoncountytx.org/government/county-judge"],
                    "note": "8-year county prosecutor before taking bench — law-enforcement aligned career.",
                },
                "1": {
                    "v": True,
                    "src": ["https://www.johnsoncountytx.org/government/county-judge"],
                    "note": "Prosecutor background — supports enforcing criminal law, not decriminalization.",
                },
            },
            "economic_stewardship": {
                "2": {
                    "v": True,
                    "src": ["https://www.johnsoncountytx.org/government/county-judge"],
                    "note": "Serves as county budget officer and chief executive — fiscal stewardship role.",
                },
            },
        },
    },
    "rick-bailey": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-1",
        "sources": [
            "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-1",
        ],
        "note": "Johnson Pct 1 Commissioner (R county); platform-scored.",
        "use_platform": True,
    },
    "kenny-howell": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-2",
        "sources": [
            "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-2",
        ],
        "note": "Johnson Pct 2 Commissioner; platform-scored.",
        "use_platform": True,
    },
    "mike-white": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-3",
        "sources": [
            "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-3",
        ],
        "note": "Johnson Pct 3 Commissioner; platform-scored.",
        "use_platform": True,
    },
    "larry-woolley": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-4",
        "sources": [
            "https://www.johnsoncountytx.org/government/commissioners/commissioner-precinct-4",
        ],
        "note": "Johnson Pct 4 Commissioner; platform-scored.",
        "use_platform": True,
    },
    # Josephine / Collin / Hunt
    "jason-turney": {
        "party": None,
        "confidence": "party_default",
        "website": "https://cityofjosephinetx.com/government/city-council/",
        "sources": [
            "https://cityofjosephinetx.com/government/city-council/",
            "https://directory.tml.org/profile/individual/83337",
        ],
        "note": "Nonpartisan Josephine mayor; party-default R baseline (Collin/Hunt conservative counties).",
        "use_platform": True,
    },
    "chris-hill": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.collincountytx.gov/Government/Commissioners-Court/county-judge",
        "sources": [
            "https://www.collincountytx.gov/Government/Commissioners-Court/county-judge",
            "https://ballotpedia.org/Chris_Hill",
            "https://www.chrishill.us/about/",
        ],
        "note": "Collin County Judge (R). Affiliated-source cells from official bio + campaign site; platform fills gaps.",
        "use_platform": True,
        "extra": {
            "self_defense": {
                "0": {
                    "v": True,
                    "src": [
                        "https://www.collincountytx.gov/Government/Commissioners-Court/county-judge",
                    ],
                    "note": "Official county bio lists Life Member of the National Rifle Association.",
                },
                "1": {
                    "v": True,
                    "src": [
                        "https://www.collincountytx.gov/Government/Commissioners-Court/county-judge",
                    ],
                    "note": "NRA Life Member on official affiliated bio — supports Second Amendment.",
                },
            },
            "family_child_sovereignty": {
                "0": {
                    "v": True,
                    "src": [
                        "https://www.collincountytx.gov/Government/Commissioners-Court/county-judge",
                    ],
                    "note": "Official bio lists membership in the Texas Home School Coalition.",
                },
            },
            "christian_liberty": {
                "0": {
                    "v": True,
                    "src": ["https://www.chrishill.us/about/"],
                    "note": "Campaign site: worships at Frisco Bible Church; former executive pastor.",
                },
            },
            "economic_stewardship": {
                "2": {
                    "v": True,
                    "src": [
                        "https://www.collincountytx.gov/Government/Commissioners-Court/county-judge",
                    ],
                    "note": "CPA/CFE; county budget officer — fiscal stewardship professional background.",
                },
            },
            "election_integrity": {
                "0": {
                    "v": True,
                    "src": ["https://www.chrishill.us/about/"],
                    "note": "Served as Republican election judge and precinct chair since 1996.",
                },
            },
        },
    },
    "bobby-w-stovall": {
        "party": "R",
        "confidence": "evidence_local",
        "website": "https://www.huntcounty.net/page/hunt.countyjudge",
        "sources": [
            "https://www.huntcounty.net/page/hunt.countyjudge",
            f"{TX_DIR}?id=63367&office=16619",
        ],
        "note": "Hunt County Judge (R, txdirectory); platform-scored gaps.",
        "use_platform": True,
    },
}


def platform_evidence(confidence: str) -> dict:
    ev = {}
    for cat, qs in R_LOCAL_PLATFORM.items():
        ev[cat] = {}
        for q in qs:
            ev[cat][str(q)] = {
                "v": True,
                "src": [RNC_URL, RNC_ALT],
                "note": PLATFORM_NOTE,
                "kind": "party_platform",
            }
    return ev


def merge_evidence(base: dict, extra: dict | None) -> dict:
    if not extra:
        return base
    out = {k: dict(v) for k, v in base.items()}
    for cat, cells in extra.items():
        out.setdefault(cat, {})
        out[cat].update(cells)
    return out


def build_dossier() -> dict:
    records = {}
    for slug, spec in OFFICIALS.items():
        entry = {
            "set": {},
            "profile": {
                "confidence": spec["confidence"],
                "confidence_note": spec["note"],
            },
            "sources_add": spec["sources"],
            "notes_append": (
                f"[2026-08-17 platform/enrichment pass] {spec['note']} "
                "Policy: docs/scorecard-evidence-policy-2026-08-16.md."
            ),
        }
        if spec.get("party"):
            entry["set"]["party"] = spec["party"]
        if spec.get("website"):
            entry["set"]["website"] = spec["website"]
        if spec.get("use_platform"):
            entry["evidence"] = merge_evidence(
                platform_evidence(spec["confidence"]), spec.get("extra")
            )
        records[slug] = entry
    return {
        "_meta": {
            "author": "cursor-bridge",
            "date": "2026-08-17",
            "note": (
                "TX local roster platform + affiliated scoring. Principal lock: affiliated "
                "sources and party platform (annotated) scoreable without personal quotes."
            ),
        },
        "reset_unspecified": False,
        "records": records,
    }


def main():
    dossier = build_dossier()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(dossier, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} ({len(dossier['records'])} records)")
    subprocess.run(
        [sys.executable, str(REPO / "refine-records.py"), str(OUT)],
        cwd=REPO,
        check=True,
    )


if __name__ == "__main__":
    main()
