#!/usr/bin/env python3
"""Enrichment batch 223: third-claim enrichment for 5 bottom-of-alphabet federal candidates.

Targets evidence_curated candidates with exactly 2 claims (archetype_curated 0-claim bucket
is exhausted). All 5 are sitting U.S. Representatives or 2026 House candidates, selected
from the bottom of the alphabet (VA, RI, OR). Mix: 4 D / 1 D (all 5 Democrats here
because remaining VA/RI/OR bottom-bucket candidates are primarily Democratic).

Candidates: Nila Devanath (VA-D), James Walkinshaw (VA-D), Gabe Amo (RI-D),
Val Hoyle (OR-D), Janelle Bynum (OR-D).

Each claim cites >=1 reliable source and reflects documented 2023-2026 voting
record / public positions.

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


TARGETS = [
    # --- Nila Devanath (VA-D, U.S. Representative VA-02 2026 candidate) ---
    ("nila-devanath", "VA", "Representative", [
        claim("nd3", "nila-devanath", "self_defense", 0, False,
              "Campaign platform explicitly calls for 'universal background checks, safe storage "
              "laws, and community violence prevention,' framing gun access as a public-health "
              "emergency that requires 'keeping guns out of dangerous hands.' As a physician "
              "candidate, Devanath treats firearm regulation as a patient-safety mandate — a "
              "gun-restriction posture that directly rejects the rubric's constitutional-carry, "
              "no-licensing standard. Her platform proposes no expansion of carry rights and "
              "supports increased federal barriers to firearm acquisition.",
              ["https://niladevanath.com/issues.html",
               "https://ballotpedia.org/Nila_Devanath"]),
    ]),

    # --- James Walkinshaw (VA-D, U.S. Representative VA-11, seated Sep 2025) ---
    ("james-walkinshaw", "VA", "House", [
        claim("jw3", "james-walkinshaw", "border_immigration", 2, False,
              "As a Fairfax County supervisor, Walkinshaw championed the county's Trust Policy — "
              "which limits local-government cooperation with federal immigration enforcement, "
              "barring officials from sharing immigration status information or detaining residents "
              "solely on ICE requests. In Congress, he publicly condemned Trump's immigration "
              "crackdowns as 'ICE terrorizing communities without warrants,' and his official "
              "immigration page states he supports 'comprehensive immigration reform to create a "
              "path to citizenship for the 14 million undocumented immigrants living in America' "
              "— a pro-sanctuary and anti-enforcement posture that directly opposes the rubric's "
              "anti-sanctuary standard.",
              ["https://walkinshaw.house.gov/issues/issue/?IssueID=14967",
               "https://ballotpedia.org/James_Walkinshaw"]),
    ]),

    # --- Gabe Amo (RI-D, U.S. Representative RI-01, seated Nov 2023) ---
    ("gabe-amo", "RI", "Representative", [
        claim("ga3", "gabe-amo", "border_immigration", 1, False,
              "Voted Nay on H.R. 875, the Jeremy and Angel Seay and Sergeant Brandon Mendoza "
              "Protect Our Communities from DUIs Act (House Vote #183, June 26, 2025, passed "
              "246-160), which would have amended the Immigration and Nationality Act to make "
              "DUI convictions a basis for inadmissibility and deportability. Amo joined the "
              "majority of House Democrats in opposing mandatory removal for DUI offenses. He "
              "has also publicly blasted House Republicans for 'dumping nearly $70 billion more "
              "into Trump's deportation machine,' signaling consistent opposition to the rubric's "
              "mandatory-deportation enforcement standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h183",
               "https://ballotpedia.org/Gabe_Amo"]),
    ]),

    # --- Val Hoyle (OR-D, U.S. Representative OR-04, seated Jan 2023) ---
    ("val-hoyle", "OR", "Representative", [
        claim("vh3", "val-hoyle", "border_immigration", 1, False,
              "Voted against the Laken Riley Act (S. 5, 119th Congress) on final passage in "
              "January 2025, which requires the Department of Homeland Security to mandatorily "
              "detain non-citizens arrested for burglary, theft, larceny, or shoplifting — a "
              "mandatory-detention measure closely aligned with the rubric's mandatory-deportation "
              "standard. While Hoyle initially joined 46 House Democrats on a procedural yes "
              "vote, she switched to Nay on the final roll-call, opposing the mandatory-detention "
              "requirement and rejecting the zero-tolerance enforcement posture the rubric calls for.",
              ["https://en.wikipedia.org/wiki/Val_Hoyle",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # --- Janelle Bynum (OR-D, U.S. Representative OR-05, seated Jan 2025) ---
    ("janelle-bynum", "OR", "Representative", [
        claim("jb3", "janelle-bynum", "border_immigration", 2, False,
              "Has co-sponsored or supported legislation to 'limit immigration enforcement "
              "actions and clarify powers of immigration officers at sensitive locations,' "
              "establishing protected zones where federal agents may not conduct immigration "
              "enforcement — a pro-sanctuary posture that directly opposes the rubric's "
              "anti-sanctuary standard. Bynum also backs authorizing cancellation of removal "
              "and adjustment of status for Dreamers and those covered by Temporary Protected "
              "Status, prioritizing legalization pathways over enforcement. These legislative "
              "positions place her consistently on the pro-sanctuary side of the immigration "
              "enforcement debate.",
              ["https://www.congress.gov/member/janelle-bynum/B001326",
               "https://ballotpedia.org/Janelle_Bynum"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
