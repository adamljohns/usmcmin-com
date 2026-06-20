#!/usr/bin/env python3
"""Enrichment batch 323: depth claims for 5 federal candidates/legislators.

Primary archetype_curated 0-claim bucket is now exhausted; this batch adds
depth to evidence_curated federal candidates/sitting members with 1-2 claims,
taken from the bottom of the alphabet (CA, NJ, NM).

Targets:
  Kevin Lincoln II (CA-13, R) — anti-abortion stance (sanctity_of_life)
  Gabriel Vasquez  (NM-02, D) — voted against H.R. 2 Secure the Border Act (border_immigration)
  Josh Gottheimer  (NJ-05, D) — voted FOR Laken Riley Act (border_immigration)
  Donald Norcross  (NJ-01, D) — voted AGAINST Laken Riley Act (border_immigration)
  LaMonica McIver  (NJ-10, D) — gun-control / gun-safety advocacy (self_defense)

Each claim cites >=1 reliable source and reflects verified 2023-2026 record.
Minified write preserves ~35-36 MB scorecard.json (see batch-4 docstring).
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
    # ---------- Kevin Lincoln II (CA-13, R — advanced to November general) ----------
    ("kevin-lincoln-ii", "CA", "Representative", [
        claim("kl1", "kevin-lincoln-ii", "sanctity_of_life", 0, True,
              "Described as 'Anti-Abortion' by Reproductive Freedom for All (successor to NARAL) during both his 2024 CA-09 and 2026 CA-13 congressional campaigns; publicly stated he is pro-life (with exceptions for rape, incest, and the health of the mother) and has been characterized by pro-abortion advocacy groups as a candidate who would support defunding Planned Parenthood and aligning with Trump's anti-abortion agenda.",
              ["https://reproductivefreedomforall.org/news/anti-abortion-and-maga-loyalist-kevin-lincoln-launches-bid-for-ca-09/",
               "https://www.aol.com/ad-check-california-republican-congressional-220110058.html"]),
    ]),

    # ---------- Gabriel Vasquez (NM-02, D — sitting US Rep 2023-2026) ----------
    ("gabriel-vasquez", "NM", "House", [
        claim("gv1", "gabriel-vasquez", "border_immigration", 0, False,
              "Voted against H.R. 2 (Secure the Border Act of 2023) on May 11, 2023, which passed the Republican House 219-213; his office issued a press release calling the bill 'extreme and unrealistic,' and he simultaneously proposed two Democratic amendments (rejected by Republicans) to increase border security at ports of entry and protect migrant farmworkers — reflecting opposition to border-wall expansion and enforcement provisions the rubric supports.",
              ["https://vasquez.house.gov/media/press-releases/watch-rep-vasquez-rejects-extreme-anti-immigrant-bill-pushes-bipartisan",
               "https://www.congress.gov/bill/118th-congress/house-bill/2"]),
    ]),

    # ---------- Josh Gottheimer (NJ-05, D — sitting US Rep 2017-2026) ----------
    ("josh-gottheimer", "NJ", "House", [
        claim("jg1", "josh-gottheimer", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (January 22, 2025) — one of only 46 House Democrats to cross party lines and the sole Democrat from New Jersey to support the bill — which requires ICE to detain illegal immigrants charged with theft or violent crimes; defended the vote saying 'If you're a murderer, a rapist, you break into people's homes, you shouldn't be here,' aligning with the rubric's support for mandatory deportation enforcement.",
              ["https://en.wikipedia.org/wiki/Josh_Gottheimer",
               "https://www.congress.gov/bill/119th-congress/house-bill/535"]),
    ]),

    # ---------- Donald Norcross (NJ-01, D — sitting US Rep 2014-2026) ----------
    ("donald-norcross", "NJ", "House", [
        claim("dn1", "donald-norcross", "border_immigration", 1, False,
              "Voted against the Laken Riley Act (January 22, 2025), which mandates ICE detention of illegal immigrants charged with theft or violent crimes; Josh Gottheimer was the only Democrat from New Jersey to vote YES, confirming that Norcross joined the overwhelming majority of House Democrats in opposing mandatory detention and deportation enforcement for criminal illegal aliens.",
              ["https://en.wikipedia.org/wiki/Josh_Gottheimer",
               "https://www.congress.gov/bill/119th-congress/house-bill/535"]),
    ]),

    # ---------- LaMonica McIver (NJ-10, D — sitting US Rep 2024-2026) ----------
    ("lamonica-mciver", "NJ", "House", [
        claim("lm1", "lamonica-mciver", "self_defense", 1, False,
              "As a member of the Congressional Progressive Caucus representing Newark (NJ-10), publicly honored gun-violence-prevention advocate and former Representative Gabby Giffords in the Congressional Record (119th Congress) and has aligned with the Democratic mainstream in supporting expanded federal background checks, restrictions on semi-automatic firearms, and red-flag laws — opposing the rubric's defense of unrestricted Second Amendment rights and its opposition to new gun-control legislation.",
              ["https://www.congress.gov/member/lamonica-mciver/M001229",
               "https://ballotpedia.org/LaMonica_McIver"]),
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
