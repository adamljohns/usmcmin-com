#!/usr/bin/env python3
"""Enrichment batch 210: 4th claims for 5 sitting U.S. Senators from the bottom
of the alphabet (WY, WV, WI). archetype_curated bucket exhausted; pivoting to
evidence_curated senators with exactly 3 claims.

Targets: John Barrasso (WY-R), Cynthia Lummis (WY-R),
         Shelley Moore Capito (WV-R), Ron Johnson (WI-R),
         Jim Justice (WV-R).
Each adds one sourced claim in a distinct rubric category not yet covered.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, name_slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{name_slug}-{category}-{q_idx}-{cid}",
        "category": category,
        "question_idx": q_idx,
        "score_impact": score_impact,
        "kind": kind,
        "text": text,
        "sources": sources,
        "verified": True,
        "verified_date": TODAY,
        "disputed": False,
        "confidence": "high",
    }


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------------- John Barrasso (WY-R, US Senator) ----------------
    ("john-barrasso", "WY", "Senator", [
        claim("jb4", "john-barrasso", "election_integrity", 0, True,
              "As Senate Majority Whip, led floor debate on the SAVE Act (H.R.22, 119th Congress), which requires documentary proof of U.S. citizenship to register to vote in federal elections and mandates removal of noncitizens from voter rolls. Barrasso declared 'Voter ID and proof of citizenship are safeguards for our elections, not restrictions' and 'The SAVE America Act is how we make elections safe, secure, and a true reflection of the will of American citizens.' He backed the Senate companion bill (S.128) and championed multiple Senate advancement votes in 2025-2026.",
              ["https://www.barrasso.senate.gov/barrasso-praises-the-save-america-act/",
               "https://www.barrasso.senate.gov/newsroom-news-releases-barrasso-americans-deserve-secure-elections/",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),

    # ---------------- Cynthia Lummis (WY-R, US Senator) ----------------
    ("cynthia-lummis", "WY", "Senator", [
        claim("cl4", "cynthia-lummis", "border_immigration", 0, True,
              "Co-introduced the WALL Act with Senator Inhofe to fully fund completion of the southern border wall using identified funding sources (no tax increases). Also was an original cosponsor and named introducer of the Laken Riley Act (S.5, 119th Congress), which requires ICE to arrest and detain illegal immigrants who commit theft, burglary, or violent offenses until deportation. Stated: 'Laken Riley's tragic passing is the unfortunate consequence of this administration's reckless open border policies and acceptance of sanctuary cities that willfully allow illegal aliens convicted of crimes to reside in our communities.'",
              ["https://www.lummis.senate.gov/press-releases/lummis-cosponsors-wall-act-to-fully-fund-border-wall-and-protect-wyoming/",
               "https://www.lummis.senate.gov/press-releases/barrasso-lummis-join-republican-senators-in-introducing-thelaken-riley-act/",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Shelley Moore Capito (WV-R, US Senator) ----------------
    ("shelley-moore-capito", "WV", "Senator", [
        claim("smc4", "shelley-moore-capito", "border_immigration", 1, True,
              "Co-sponsored and voted YES on the Laken Riley Act (S.5, 119th Congress, signed Jan. 29, 2025), which mandates ICE detention of illegal immigrants accused of theft-related crimes and assault on law enforcement pending removal from the United States — the first mandatory-deportation law of its kind. Capito applauded the Trump Administration's deportation enforcement: 'I support the actions the Administration has taken on deportation...it will make our country safer.' The bill passed 64-35 and was the first legislation signed in Trump's second term.",
              ["https://www.capito.senate.gov/news/press-releases/capito-votes-to-pass-laken-riley-act",
               "https://www.capito.senate.gov/news/in-the-news/capito-applauds-trump-administration-deportation-efforts-passage-of-laken-riley-act",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Ron Johnson (WI-R, US Senator) ----------------
    ("ron-johnson", "WI", "Senator", [
        claim("rj4", "ron-johnson", "sanctity_of_life", 0, True,
              "Named original cosponsor of the Born-Alive Abortion Survivors Protection Act (S.6, 119th Congress, introduced Jan. 2025), which requires health care practitioners to provide the same degree of care to infants born alive after a failed abortion as any other newborn. Johnson has consistently voted for pro-life bills, received a lifetime A-grade from SBA Pro-Life America, and has stated 'as a compassionate society we have an obligation to protect life, especially the life of the most vulnerable among us — the unborn.' Opposes embryonic stem cell research on moral grounds.",
              ["https://www.ronjohnson.senate.gov/2020/2/johnson-votes-to-support-pro-life-bills",
               "https://sbaprolife.org/senator/ron-johnson",
               "https://www.congress.gov/bill/119th-congress/senate-bill/6"]),
    ]),

    # ---------------- Jim Justice (WV-R, US Senator) ----------------
    ("jim-justice", "WV", "Senator", [
        claim("jj4", "jim-justice", "economic_stewardship", 2, True,
              "Voted YES on the One Big Beautiful Bill Act (H.R.1, 51-50, signed July 4, 2025), which enacted the most significant federal entitlement reform in decades — imposing work requirements on Medicaid and SNAP, cutting approximately $1.5 trillion in mandatory federal spending — while permanently extending the 2017 individual tax rates to prevent automatic tax hikes. Justice stated the bill 'provides lasting tax relief, establishes common-sense reform to our social programs while protecting those who are most vulnerable' and that he worked closely with President Trump to safeguard West Virginia's interests. As governor, Justice also turned a $500 million inherited budget deficit into a historic $1.8 billion surplus through spending discipline.",
              ["https://www.justice.senate.gov/press-releases/senator-justice-statement-on-senate-passage-of-one-big-beautiful-bill/",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://www.govtrack.us/congress/members/jim_justice/456969"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        office = (c.get("office") or "")
        if office_keyword.lower() not in office.lower():
            continue
        return c
    return None


def main():
    scorecard = json.loads(SCORECARD.read_text())
    upgraded = 0
    claims_added = 0
    for slug, state, office_keyword, claims in TARGETS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  ✗ NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
            continue
        existing = m.get("claims") or []
        existing_ids = {x.get("id") for x in existing}
        new_claims = [c for c in claims if c["id"] not in existing_ids]
        existing.extend(new_claims)
        m["claims"] = existing
        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        old_conf = prof.get("confidence")
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY
        scores = m.get("scores") or {}
        for cl in new_claims:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
