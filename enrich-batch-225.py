#!/usr/bin/env python3
"""Enrichment batch 225: third-claim enrichment for 5 PA U.S. Representatives.

Targets evidence_curated federal representatives at the bottom of the alphabet
with exactly 2 claims, adding one distinct-category claim each.

Mix (3 R / 2 D): Lloyd Smucker (PA-11-R), John Joyce (PA-13-R),
Brian Fitzpatrick (PA-01-R), Chris Deluzio (PA-17-D), Brendan Boyle (PA-02-D).

Sources: govtrack.us, congress.gov, sbaprolife.org, ballotpedia.org,
justfacts.votesmart.org, en.wikipedia.org.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ---------------- Lloyd Smucker (PA-11-R, U.S. Representative) ----------------
    ("lloyd-smucker", "PA", "Representative", [
        claim("ls3", "lloyd-smucker", "self_defense", 1, True,
              "NRA-endorsed in 2024 with an A-rated gun-rights record; voted NO on the Bipartisan Background Checks Act (H.R. 8) twice (2019 and 2021), opposing expanded background-check mandates on private firearm transfers — consistent with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://justfacts.votesmart.org/candidate/key-votes/102454/lloyd-smucker/37/guns",
               "https://ballotpedia.org/Lloyd_Smucker"]),
    ]),

    # ---------------- John Joyce (PA-13-R, U.S. Representative) ----------------
    ("john-joyce", "PA", "Representative", [
        claim("jj3", "john-joyce", "election_integrity", 0, True,
              "Signed the December 2020 congressional amicus brief to the Supreme Court in Texas v. Pennsylvania — backed by 126 House Republicans — calling for mail-in-ballot results in four swing states to be set aside over election-integrity concerns, an anti-mass-mail-in posture consistent with the rubric.",
              ["https://ballotpedia.org/John_Joyce_(Pennsylvania)",
               "https://en.wikipedia.org/wiki/John_Joyce_(American_politician)"]),
    ]),

    # ---------------- Brian Fitzpatrick (PA-01-R, U.S. Representative) ----------------
    ("brian-fitzpatrick", "PA", "Representative", [
        claim("bf3", "brian-fitzpatrick", "sanctity_of_life", 0, False,
              "One of only three House Republicans to vote YES on H.R. 8297, the Ensuring Access to Abortion Act of 2022 (July 15, 2022 House Vote #362), which prohibits states from blocking residents seeking out-of-state abortions; SBA Pro-Life America gave him a failing grade, stating his votes are 'antithetical to the pro-life position.'",
              ["https://sbaprolife.org/representative/brian-fitzpatrick",
               "https://www.govtrack.us/congress/votes/117-2022/h362"]),
    ]),

    # ---------------- Chris Deluzio (PA-17-D, U.S. Representative) ----------------
    ("chris-deluzio", "PA", "Representative", [
        claim("cd3", "chris-deluzio", "border_immigration", 1, False,
              "Voted NO on H.R. 5525, the Continuing Appropriations and Border Security Enhancement Act of 2024, opposing the border-security-enforcement provisions; consistently supports 'humane' immigration pathways over the mandatory-deportation and wall-construction policies the rubric calls for.",
              ["https://ballotpedia.org/Chris_Deluzio",
               "https://www.govtrack.us/congress/members/chris_deluzio/456936"]),
    ]),

    # ---------------- Brendan Boyle (PA-02-D, U.S. Representative) ----------------
    ("brendan-boyle", "PA", "Representative", [
        claim("bb3", "brendan-boyle", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, June 24, 2022 House Vote #299), expanding background checks for under-21 firearm buyers; a gun-control proponent who calls America's gun-violence rate 'an epidemic' and supports further restrictions on semi-automatic firearms — directly opposing the rubric's Second Amendment protections.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Brendan_Boyle"]),
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
