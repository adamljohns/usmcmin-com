#!/usr/bin/env python3
"""VA major-city council roster + socials. Official city pages 2026-09-05.

Adds missing sitting members (VB D8, Norfolk Ward 5, all Alexandria, all Roanoke).
Sets official bio/council URLs + verified personal socials. Does not invent scores.
"""
from __future__ import annotations

import json
from copy import deepcopy
from datetime import date
from pathlib import Path

BASE = Path(__file__).parent
SCORECARD = BASE / "data" / "scorecard.json"
TODAY = date.today().isoformat()

LOCAL_SCORES = {
    "sanctity_of_life": [None, None, "N/A", "N/A", "N/A"],
    "biblical_marriage": [None, "N/A", None, "N/A", None],
    "family_child_sovereignty": [None, None, None, "N/A", "N/A"],
    "christian_liberty": [None, "N/A", None, None, None],
    "economic_stewardship": ["N/A", "N/A", None, "N/A", "N/A"],
    "election_integrity": [None, None, "N/A", "N/A", None],
    "border_immigration": ["N/A", None, None, "N/A", "N/A"],
    "self_defense": [None, None, "N/A", "N/A", "N/A"],
    "foreign_policy_restraint": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "industry_capture": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "public_justice": [None, None, None, None, None],
    "refuse_federal_overreach": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "refuse_state_overreach": [None, None, None, None, None],
}

NOTE = (
    "Roster/socials pass 2026-09-05 from the city's official council page. "
    "RESOLUTE local cells not scored this hop — blank > guessed party default."
)


def scaffold(name, slug, office, jurisdiction, website, sources, extra_profile=None):
    prof = {
        "religion": None,
        "education": None,
        "background": None,
        "confidence": None,
        "last_refined": TODAY,
    }
    if extra_profile:
        prof.update({k: v for k, v in extra_profile.items() if v})
    rec = {
        "name": name,
        "slug": slug,
        "office": office,
        "jurisdiction": jurisdiction,
        "level": "local",
        "party": None,
        "district": None,
        "state": "VA",
        "status": "active",
        "scores": deepcopy(LOCAL_SCORES),
        "notes": NOTE,
        "photo": None,
        "website": website,
        "sources": sources,
        "profile": prof,
        "claims": [],
    }
    return rec


# Official listing pages
FXBG_LIST = "https://www.fredericksburgva.gov/263/Council-Members"
VB_LIST = "https://clerk.virginiabeach.gov/city-council/city-council-members"
NFK_LIST = "https://www.norfolk.gov/200/City-Council"
ALX_LIST = "https://www.alexandriava.gov/Council"
ROA_LIST = "https://www.roanokeva.gov/1001/Members-of-City-Council"
ROA_DIR = "https://www.roanokeva.gov/Directory.aspx?did=64"

NEW = [
    scaffold(
        "Stacy Cummings", "stacy-cummings-vb",
        "City Council - District 8", "City of Virginia Beach",
        VB_LIST, [VB_LIST, "https://voter.virginiabeach.gov/elections/elected-officials"],
    ),
    scaffold(
        "Thomas R. Smigiel Jr.", "thomas-r-smigiel-jr",
        "City Council - Ward 5", "City of Norfolk",
        "https://www.norfolk.gov/539/Thomas-R-Smigiel-Jr",
        [NFK_LIST, "https://www.norfolk.gov/539/Thomas-R-Smigiel-Jr"],
    ),
    scaffold(
        "Alyia Gaskins", "alyia-gaskins",
        "Mayor", "City of Alexandria",
        "https://alexandriava.gov/city-council/person/mayor-alyia-gaskins",
        [ALX_LIST, "https://alexandriava.gov/city-council/person/mayor-alyia-gaskins"],
    ),
    scaffold(
        "Sarah Bagley", "sarah-bagley-alx",
        "Vice Mayor / City Council", "City of Alexandria",
        ALX_LIST, [ALX_LIST],
    ),
    scaffold(
        "Canek Aguirre", "canek-aguirre",
        "City Council", "City of Alexandria",
        ALX_LIST, [ALX_LIST],
    ),
    scaffold(
        "John Taylor Chapman", "john-chapman-alx",
        "City Council", "City of Alexandria",
        ALX_LIST, [ALX_LIST],
    ),
    scaffold(
        "Abdel-Rahman Elnoubi", "abdel-rahman-elnoubi",
        "City Council", "City of Alexandria",
        "https://www.alexandriava.gov/index.php/city-council/person/councilman-abdel-rahman-elnoubi",
        [ALX_LIST, "https://www.alexandriava.gov/city-council/person/councilman-abdel-rahman-elnoubi"],
    ),
    scaffold(
        "Jacinta E. Greene", "jacinta-e-greene",
        "City Council", "City of Alexandria",
        "https://www.alexandriava.gov/city-council/person/councilwoman-jacinta-e-greene",
        [ALX_LIST, "https://www.alexandriava.gov/city-council/person/councilwoman-jacinta-e-greene"],
    ),
    scaffold(
        "Sandy Marks", "sandy-marks-alx",
        "City Council", "City of Alexandria",
        ALX_LIST, [ALX_LIST],
    ),
    scaffold(
        "Joseph L. Cobb", "joseph-l-cobb",
        "Mayor", "City of Roanoke",
        "https://www.roanokeva.gov/1007/Joseph-L-Cobb",
        [ROA_LIST, ROA_DIR, "https://www.roanokeva.gov/1007/Joseph-L-Cobb"],
    ),
    scaffold(
        "S. Terry McGuire", "s-terry-mcguire",
        "Vice Mayor / City Council", "City of Roanoke",
        "https://www.roanokeva.gov/2778/S-Terry-McGuire",
        [ROA_LIST, ROA_DIR, "https://www.roanokeva.gov/2778/S-Terry-McGuire"],
    ),
    scaffold("Peter J. Volosin", "peter-j-volosin", "City Council", "City of Roanoke", ROA_LIST, [ROA_LIST, ROA_DIR]),
    scaffold("Nicolas S. Hagen", "nicolas-s-hagen", "City Council", "City of Roanoke", ROA_LIST, [ROA_LIST, ROA_DIR]),
    scaffold("Evelyn W. Powers", "evelyn-w-powers", "City Council", "City of Roanoke", ROA_LIST, [ROA_LIST, ROA_DIR]),
    scaffold("Phazhon T. Nash", "phazhon-t-nash", "City Council", "City of Roanoke", ROA_LIST, [ROA_LIST, ROA_DIR]),
    scaffold("Vivian Sanchez-Jones", "vivian-sanchez-jones", "City Council", "City of Roanoke", ROA_LIST, [ROA_LIST, ROA_DIR]),
]

# Existing sitting records: official bio + verified personal socials only.
# twitter = handle (no @). campaign_website = campaign URL.
UPDATES = {
    "kerry-devine": {
        "website": "https://www.fredericksburgva.gov/691/Kerry-P-Devine-Mayor",
        "sources": [FXBG_LIST, "https://www.fredericksburgva.gov/691/Kerry-P-Devine-Mayor"],
    },
    "charlie-frye-jr": {
        "website": "https://www.fredericksburgva.gov/674/Charlie-L-Frye-Jr-Ward-4",
        "twitter": "ChuckFryeJr",
        "sources": [
            FXBG_LIST,
            "https://www.fredericksburgva.gov/674/Charlie-L-Frye-Jr-Ward-4",
            "https://x.com/ChuckFryeJr",
        ],
    },
    "jannan-holmes": {
        "website": "https://www.fredericksburgva.gov/1944/Jannan-W-Holmes-At-Large",
        "sources": [
            FXBG_LIST,
            "https://www.fredericksburgva.gov/1944/Jannan-W-Holmes-At-Large",
            "https://www.linkedin.com/in/jannan-holmes-8483796",
        ],
    },
    "will-mackintosh": {
        "website": "https://www.fredericksburgva.gov/1943/Will-B-Mackintosh-At-Large",
        "campaign_website": "https://www.yeswewillfxbg.com/",
        "sources": [
            FXBG_LIST,
            "https://www.fredericksburgva.gov/1943/Will-B-Mackintosh-At-Large",
            "https://www.yeswewillfxbg.com/",
        ],
    },
    "matt-rowe-fxbg": {
        "website": "https://www.fredericksburgva.gov/2188/Matt-D-Rowe-Ward-1",
        "campaign_website": "https://matt4fxbg.com/",
        "sources": [
            FXBG_LIST,
            "https://www.fredericksburgva.gov/2188/Matt-D-Rowe-Ward-1",
            "https://matt4fxbg.com/",
            "https://www.facebook.com/MattRoweFXBG/",
        ],
    },
    "joy-crump-fxbg": {
        "website": "https://www.fredericksburgva.gov/1800/Joy-Y-Crump-Ward-2",
        "campaign_website": "https://joyforfxbg.com/",
        "sources": [
            FXBG_LIST,
            "https://www.fredericksburgva.gov/1800/Joy-Y-Crump-Ward-2",
            "https://www.facebook.com/ChefJoyCrump/",
            "https://joyforfxbg.com/",
        ],
    },
    "susanna-finn": {
        "website": "https://www.fredericksburgva.gov/2098/Susanna-R-Finn-Ward-3",
        "sources": [
            FXBG_LIST,
            "https://www.fredericksburgva.gov/2098/Susanna-R-Finn-Ward-3",
            "https://www.facebook.com/profile.php?id=61572830267145",
            "https://www.instagram.com/susannafinn_fxbg/",
        ],
    },
    "kenny-alexander": {
        "website": "https://www.norfolk.gov/3515/Mayor-Kenneth-Cooper-Alexander-PhD",
        "sources": [NFK_LIST, "https://www.norfolk.gov/3515/Mayor-Kenneth-Cooper-Alexander-PhD"],
    },
    "martin-thomas-jr": {
        "website": "https://www.norfolk.gov/542/Vice-Mayor-Martin-A-Thomas-Jr",
        "sources": [NFK_LIST, "https://www.norfolk.gov/542/Vice-Mayor-Martin-A-Thomas-Jr"],
    },
    "courtney-doyle": {
        "website": "https://www.norfolk.gov/4111/Courtney-R-Doyle",
        "twitter": "CourtneyDoyleVA",
        "sources": [
            NFK_LIST,
            "https://www.norfolk.gov/4111/Courtney-R-Doyle",
            "https://www.facebook.com/CourtneyDoyleNFK",
            "https://x.com/CourtneyDoyleVA",
        ],
    },
    "mamie-johnson": {
        "website": "https://www.norfolk.gov/2932/Mamie-B-Johnson",
        "sources": [NFK_LIST, "https://www.norfolk.gov/2932/Mamie-B-Johnson"],
    },
    "john-paige": {
        "website": "https://www.norfolk.gov/538/John-E-JP-Paige",
        "sources": [NFK_LIST, "https://www.norfolk.gov/538/John-E-JP-Paige"],
    },
    "jeremy-mcgee": {
        "website": "https://www.norfolk.gov/6429/Jeremy-D-McGee",
        "sources": [NFK_LIST, "https://www.norfolk.gov/6429/Jeremy-D-McGee"],
    },
    "carlos-clanton": {
        "website": "https://www.norfolk.gov/6428/Carlos-J-Clanton",
        "sources": [NFK_LIST, "https://www.norfolk.gov/6428/Carlos-J-Clanton"],
    },
    "bobby-dyer": {"website": VB_LIST, "sources": [VB_LIST]},
    "hutch-hutcheson": {"website": VB_LIST, "sources": [VB_LIST]},
    "barbara-henley": {"website": VB_LIST, "sources": [VB_LIST]},
    "michael-berlucchi": {"website": VB_LIST, "sources": [VB_LIST]},
    "amelia-ross-hammond": {"website": VB_LIST, "sources": [VB_LIST]},
    "rosemary-wilson": {"website": VB_LIST, "sources": [VB_LIST]},
    "worth-remick": {"website": VB_LIST, "sources": [VB_LIST]},
    "cal-jackson-green": {"website": VB_LIST, "sources": [VB_LIST]},
    "joshua-schulman": {"website": VB_LIST, "sources": [VB_LIST]},
    "jennifer-rouse": {"website": VB_LIST, "sources": [VB_LIST]},
}


def add_sources(rec, urls):
    src = list(rec.get("sources") or [])
    for u in urls:
        if u and u not in src:
            src.append(u)
    rec["sources"] = src


def main():
    sc = json.loads(SCORECARD.read_text())
    cands = sc["candidates"]
    by_slug = {}
    for c in cands:
        by_slug.setdefault(c.get("slug"), []).append(c)

    int_ids = [c["id"] for c in cands if isinstance(c.get("id"), int)]
    next_id = (max(int_ids) + 1) if int_ids else 9000

    added = []
    for rec in NEW:
        hits = by_slug.get(rec["slug"]) or []
        if any((h.get("state") == "VA") for h in hits):
            print("SKIP exists", rec["slug"])
            continue
        rec["id"] = next_id
        next_id += 1
        cands.append(rec)
        by_slug.setdefault(rec["slug"], []).append(rec)
        added.append(rec["slug"])

    patched = []
    for slug, upd in UPDATES.items():
        hits = [c for c in (by_slug.get(slug) or []) if c.get("state") == "VA"]
        if not hits:
            print("MISS update", slug)
            continue
        rec = hits[0]
        if rec.get("status") == "former":
            print("SKIP former", slug)
            continue
        if upd.get("website"):
            rec["website"] = upd["website"]
        prof = rec.setdefault("profile", {})
        if upd.get("twitter"):
            prof["twitter"] = upd["twitter"]
        if upd.get("campaign_website"):
            prof["campaign_website"] = upd["campaign_website"]
        prof["last_refined"] = TODAY
        add_sources(rec, upd.get("sources") or [])
        patched.append(slug)

    sc.setdefault("meta", {})["last_updated"] = TODAY
    SCORECARD.write_text(json.dumps(sc, indent=2, ensure_ascii=False) + "\n")
    print(f"added {len(added)}: {added}")
    print(f"patched {len(patched)}: {patched}")


if __name__ == "__main__":
    main()
