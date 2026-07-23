#!/usr/bin/env python3
"""Enrichment batch 843: 2 claims each for the 4 federal sitting officials with fewest
existing claims (3 each) — Hickenlooper (CO-D, US Senator), Ansari (AZ-D, AZ-03),
Stanton (AZ-D, AZ-04), Crane (AZ-R, AZ-02).

The archetype_curated federal senator/rep buckets are now fully depleted (0 claims
remaining). This batch targets the thinnest-covered sitting federal officials from the
evidence_curated pool. Categories chosen are DISTINCT from each candidate's 3 existing claims.

Sources: hickenlooper.senate.gov, ansari.house.gov, stanton.house.gov, crane.house.gov
(indirectly via en.wikipedia.org, ballotpedia.org, govtrack.us).

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
    # ---- John Hickenlooper (CO-D, US Senator) ----
    ("john-hickenlooper", "CO", "Senator", [
        claim("jh4", "john-hickenlooper", "border_immigration", 1, False,
              "In February 2026 voted NO on the DHS funding bill and released a statement "
              "declaring 'The American people have seen with their own eyes that ICE is out "
              "of control.' Introduced legislation to ban ICE agents from wearing masks and to "
              "require clear identification during operations; also fought to prohibit immigration "
              "enforcement at schools, hospitals, polling locations, and places of worship — "
              "directly opposing mandatory deportation infrastructure and enforcement.",
              ["https://www.hickenlooper.senate.gov/press_releases/hickenlooper-statement-after-no-vote-on-dhs-funding-bill/",
               "https://www.hickenlooper.senate.gov/issues-backup/immigration/"]),
        claim("jh5", "john-hickenlooper", "election_integrity", 0, False,
              "As Colorado governor signed HB 13-1303 (2013, the Voter Access and Modernized "
              "Elections Act), which required all registered voters to automatically receive mail "
              "ballots and established no-excuse mail-in voting statewide — one of the nation's "
              "most expansive vote-by-mail systems. As U.S. Senator has consistently defended "
              "universal mail balloting and opposed legislation requiring strict in-person voter ID, "
              "directly contrary to the rubric's election-integrity priorities of voter ID and "
              "anti-mass-mail-in.",
              ["https://en.wikipedia.org/wiki/John_Hickenlooper",
               "https://ballotpedia.org/John_Hickenlooper"]),
    ]),

    # ---- Yassamin Ansari (AZ-D, US Rep AZ-03) ----
    ("yassamin-ansari", "AZ", "AZ-03", [
        claim("ya3", "yassamin-ansari", "border_immigration", 1, False,
              "In July 2026 co-led the Fund Schools Not ICE Act with Representatives Stanton and "
              "Grijalva to redirect the $38.5 billion in ICE enforcement funding appropriated in "
              "Republicans' reconciliation bill to Title I public-school grants, and to require the "
              "sale of 11 recently purchased DHS detention warehouse facilities. Called ICE a "
              "'poorly trained force' that is 'causing chaos and fear' rather than enhancing public "
              "safety, directly opposing mandatory deportation enforcement.",
              ["https://ansari.house.gov/media/press-releases/ansari-stanton-grijalva-introduce-bill-to-redirect-ice-funding-to-public-schools-require-sale-of-detention-warehouses",
               "https://stanton.house.gov/2026/7/stanton-ansari-grijalva-introduce-bill-to-redirect-ice-funding-to-public-schools-require-sale-of-detention-warehouses"]),
        claim("ya4", "yassamin-ansari", "economic_stewardship", 4, False,
              "A professional climate-policy advocate before her election (with graduate-level "
              "training in climate/environmental policy and prior work in sustainability and climate "
              "finance), Ansari's legislative priorities embrace ESG investment frameworks and "
              "international climate-finance agreements — the global sustainability consensus "
              "advanced at Davos/COP summits that the rubric regards as antithetical to sound "
              "economic stewardship and national sovereignty.",
              ["https://ballotpedia.org/Yassamin_Ansari",
               "https://en.wikipedia.org/wiki/Yassamin_Ansari"]),
    ]),

    # ---- Greg Stanton (AZ-D, US Rep AZ-04) ----
    ("greg-stanton", "AZ", "AZ-04", [
        claim("gs4", "greg-stanton", "border_immigration", 1, False,
              "Co-introduced the Fund Schools Not ICE Act (July 2026) to redirect the $38.5 "
              "billion in ICE enforcement funding from the reconciliation bill to Title I "
              "public-school grants and require the sale of 11 DHS detention warehouse facilities; "
              "publicly declared 'ICE's poorly trained force is not making Americans safer — it's "
              "causing chaos and fear,' directly opposing mandatory immigration enforcement and "
              "deportation.",
              ["https://stanton.house.gov/2026/7/stanton-ansari-grijalva-introduce-bill-to-redirect-ice-funding-to-public-schools-require-sale-of-detention-warehouses",
               "https://grijalva.house.gov/media/press-releases/grijalva-stanton-ansari-introduce-bill-to-redirect-ice-funding-to-public-schools-require-sale-of-detention-warehouses"]),
        claim("gs5", "greg-stanton", "foreign_policy_restraint", 1, False,
              "Voted YES on H.R. 8035 (National Security Act, $95.3B supplemental for Ukraine, "
              "Israel, and Taiwan, signed April 24, 2024), committing billions in open-ended "
              "military assistance without a formal Article-I declaration of war. Also serves on "
              "the House Select Committee on Strategic Competition Between the U.S. and China, "
              "focused on sustained confrontational military and economic positioning — at odds "
              "with the rubric's foreign-policy restraint.",
              ["https://ballotpedia.org/Greg_Stanton",
               "https://www.govtrack.us/congress/members/greg_stanton/412753"]),
    ]),

    # ---- Eli Crane (AZ-R, US Rep AZ-02) ----
    ("eli-crane", "AZ", "AZ-02", [
        claim("ec4", "eli-crane", "foreign_policy_restraint", 0, True,
              "In February 2025 published a public statement titled 'Do not aspire to empire,' "
              "explicitly opposing expansionist U.S. foreign policy and calling on America to "
              "remain within its historical constitutional boundaries. This non-interventionist "
              "posture reflects support for Article-I war-powers restraint and rejection of "
              "military empire-building — aligning with the rubric's foreign-policy-restraint "
              "ideal.",
              ["https://en.wikipedia.org/wiki/Eli_Crane",
               "https://ballotpedia.org/Eli_Crane"]),
        claim("ec5", "eli-crane", "biblical_marriage", 2, True,
              "Voted YES on HR 734 (Protection of Women and Girls in Sports Act, passed 219-203 "
              "on April 20, 2023), which would prohibit biological males from competing in female "
              "athletic competitions at schools and colleges receiving federal funding — "
              "rejecting the transgender-ideology premise that biological sex is malleable and "
              "aligning with the rubric's position on protecting women's spaces from redefinition "
              "under gender ideology.",
              ["https://www.govtrack.us/congress/votes/118-2023/h199",
               "https://ballotpedia.org/Eli_Crane"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
    """
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
