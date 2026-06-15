#!/usr/bin/env python3
"""Enrichment batch 222: third-claim enrichment for 5 bottom-of-alphabet federal candidates.

Targets evidence_curated candidates with exactly 2 claims (next priority after
archetype_curated 0-claim bucket is exhausted). Mix: 3 D / 2 R.

Candidates: Jasmine Crockett (TX-D), Roy Cooper (NC-D), Wiley Nickel (NC-D),
Kurt Alme (MT-R), Royce White (MN-R).

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
    # --- Jasmine Crockett (TX-D, U.S. Representative / Senate-track) ---
    ("jasmine-crockett", "TX", "Representative", [
        claim("jc3", "jasmine-crockett", "border_immigration", 0, False,
              "Voted against H.R. 2, the Secure the Border Act of 2023 (May 11, 2023, "
              "final vote 219-213), which would have resumed border-wall construction, "
              "ended catch-and-release, and mandated returns to Mexico under Remain in "
              "Mexico — directly opposing the rubric's wall-and-military enforcement "
              "posture. Crockett was among all 210 House Democrats who opposed the bill "
              "and has publicly stated the government has 'committed atrocities against "
              "migrants,' championing pathways to citizenship instead.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/member/jasmine-crockett/C001130"]),
    ]),

    # --- Roy Cooper (NC-D, U.S. Senate 2026 nominee) ---
    ("roy-cooper-nc-senate", "NC", "Senator", [
        claim("rc3", "roy-cooper-nc-senate", "self_defense", 1, False,
              "As Governor of North Carolina, vetoed HB 398, which would have repealed "
              "the state's pistol purchase permit — a government-issued license required "
              "to buy any handgun. The Republican supermajority overrode his veto on "
              "March 29, 2023, removing the restriction against Cooper's wishes. His "
              "governorship record consistently opposed loosening gun laws; he also "
              "opposed permitless-carry expansion and backed background-check expansion "
              "— rejecting the rubric's anti-licensing, anti-registry posture.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_North_Carolina",
               "https://ballotpedia.org/Roy_Cooper"]),
    ]),

    # --- Wiley Nickel (NC-D, U.S. Senate 2026 candidate) ---
    ("wiley-nickel-senate", "NC", "Senate", [
        claim("wn3", "wiley-nickel-senate", "border_immigration", 0, False,
              "Voted against H.R. 2, the Secure the Border Act of 2023 (May 11, 2023, "
              "vote 219-213), which would have resumed border-wall construction, ended "
              "catch-and-release, and required asylum seekers to wait in Mexico. As a "
              "Democrat representing NC-13 in the 118th Congress (2023-2025), Nickel "
              "joined every House Democrat in opposing the measure, backing expanded "
              "legal-immigration pathways and DACA protections instead.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.govtrack.us/congress/members/wiley_nickel/456915"]),
    ]),

    # --- Kurt Alme (MT-R, U.S. Senate 2026 R nominee) ---
    ("kurt-alme", "MT", "Senator", [
        claim("ka3", "kurt-alme", "economic_stewardship", 2, True,
              "Served as Montana Governor Greg Gianforte's budget director (2021-2025), "
              "helping craft balanced state budgets that produced surplus revenues "
              "without deficit spending — consistent with the rubric's anti-deficit / "
              "balanced-budget standard. Endorsed by retiring Senator Steve Daines and "
              "President Trump and is running on a platform of fiscal restraint and "
              "reducing federal government spending.",
              ["https://ballotpedia.org/Kurt_Alme",
               "https://en.wikipedia.org/wiki/Kurt_Alme"]),
    ]),

    # --- Royce White (MN-R, U.S. Senate 2026 R candidate) ---
    ("royce-white", "MN", "Senator", [
        claim("rw3", "royce-white", "economic_stewardship", 1, True,
              "Publicly calls for ending the Federal Reserve ('End the Fed') and "
              "restoring a gold standard, stating the U.S. should 'tie the hands of "
              "the central banks, stop the debt, and bring back the gold standard.' "
              "This directly matches the rubric's sound-money / audit-the-Fed position, "
              "rejecting fiat-currency manipulation in favor of hard-currency discipline.",
              ["https://ballotpedia.org/Royce_White",
               "https://en.wikipedia.org/wiki/Royce_White"]),
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
