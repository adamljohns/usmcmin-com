#!/usr/bin/env python3
"""Roster fix: the DE record 'tonya-williams' (Lt Gov) is a phantom — no such
person is/was Delaware's LG. The real sitting LG is Kyle Evans Gay (D), sworn in
2025-01-21. Clone the phantom's complete schema into a correct kyle-evans-gay
record; the phantom is then removed via dedup-merge-records.py and the survivor
re-scored from evidence via the refinement engine."""
import copy
import json
import os

REPO = os.path.dirname(os.path.abspath(__file__))
SC = os.path.join(REPO, "data", "scorecard.json")

with open(SC, encoding="utf-8") as f:
    sc = json.load(f)
cands = sc["candidates"]

if any(c.get("slug") == "kyle-evans-gay" for c in cands):
    print("kyle-evans-gay already present — nothing to add.")
    raise SystemExit(0)

src = next((c for c in cands if c.get("slug") == "tonya-williams"), None)
if src is None:
    raise SystemExit("ABORT: phantom tonya-williams not found.")

new = copy.deepcopy(src)
new["name"] = "Kyle Evans Gay"
new["slug"] = "kyle-evans-gay"
# unique id (handle int or str id schemes)
ids = [c.get("id") for c in cands]
if all(isinstance(i, int) for i in ids if i is not None):
    new["id"] = max(i for i in ids if isinstance(i, int)) + 1
else:
    new["id"] = "kyle-evans-gay"
new["office"] = "Lieutenant Governor"
new["party"] = "D"
new["website"] = "https://ltgov.delaware.gov"
new["photo"] = None
new["notes"] = ("27th Lieutenant Governor of Delaware (D), sworn in 2025-01-21. Replaces "
                "phantom record 'tonya-williams' (no such DE LG existed).")
new["sources"] = [
    "https://news.delaware.gov/2025/01/23/kyle-evans-gay-takes-her-oath-becoming-delawares-27th-lieutenant-governor/",
    "https://ballotpedia.org/Kyle_Evans_Gay",
    "https://legis.delaware.gov",
]
new["profile"] = {
    "religion": None,
    "net_worth": None,
    "birthplace": None,
    "education": None,
    "background": "Delaware State Senator, SD-5 (2021-2025); 27th Lieutenant Governor of Delaware, sworn in 2025-01-21.",
    "prev_election_opponent": "Ruth Briggs King (R)",
    "next_election_year": 2028,
    "next_election_contenders": [],
    "confidence_note": "2026-06-17 — roster correction: prior record 'tonya-williams' was a phantom (no such DE LG). Replaced with the verified sitting LG, Kyle Evans Gay (D).",
}

cands.append(new)
tmp = SC + ".tmp"
with open(tmp, "w", encoding="utf-8") as f:
    json.dump(sc, f, ensure_ascii=False, separators=(",", ":"))
os.replace(tmp, SC)
print(f"Added kyle-evans-gay (id={new['id']}); {len(cands)} candidates total.")
