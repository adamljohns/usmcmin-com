#!/usr/bin/env python3
"""Enrichment batch 307: 3rd claims for 5 sitting U.S. Representatives.

Archetype_curated federal bucket exhausted (see batch 303 note).
Continues the batch-306 pattern: targets evidence_curated sitting federal
representatives with exactly 2 claims — taken from the bottom of the
alphabet (CA ×5), spanning distinct rubric categories not yet covered.

Targets:
  Scott Peters        (CA-50, D) — border_immigration / voted NO HR2 2023
  Mike Thompson       (CA-04, D) — sanctity_of_life / pro-choice, WHPA co-sponsor
  Mike Levin          (CA-49, D) — biblical_marriage / Respect for Marriage Act + Equality Act
  Judy Chu            (CA-28, D) — self_defense / original AWB-2023 co-sponsor
  George Whitesides   (CA-27, D) — biblical_marriage / Equality Act 2025 introducer

Each claim cites >=1 reliable source and reflects documented 2022-2025 public record.

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


# Each entry: (slug, state, office_keyword, claims-list)
TARGETS = [
    # ---- Scott Peters (CA-50, D, US Representative) ----
    ("scott-peters", "CA", "Representative", [
        claim("sp3", "scott-peters", "border_immigration", 0, False,
              "Voted NO on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023). The bill would have funded border-wall construction, restricted asylum to official ports of entry only, ended catch-and-release, imposed mandatory safe-third-country bars, and mandated E-Verify — a comprehensive enforcement package the rubric identifies as the border-security alignment standard. The bill passed 219-213 with no Democratic support; Peters voted with the unanimous House Democratic caucus against it.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/bill/118th-congress/house-bill/2/summary/00",
               "https://ballotpedia.org/Scott_Peters"]),
    ]),

    # ---- Mike Thompson (CA-04, D, US Representative) ----
    ("mike-thompson-ca-04", "CA", "Representative", [
        claim("mt3", "mike-thompson-ca-04", "sanctity_of_life", 0, False,
              "Although a practicing Catholic, Thompson is vocally pro-choice and explicitly rejects life-from-conception personhood standards. He co-sponsored H.R. 3755, the Women's Health Protection Act of 2021, which would have codified a nationwide right to abortion up to viability (and in many circumstances beyond). He denounced the Supreme Court's Dobbs decision as 'an assault on women' in 2022. In the 119th Congress (2025), he co-sponsored H.R. 4611, the EACH Act of 2025 (Equal Access to Abortion Coverage in Health Insurance Act), expanding taxpayer-funded abortion coverage — actively opposing any personhood-from-conception framework.",
              ["https://en.wikipedia.org/wiki/Mike_Thompson_(California_politician)",
               "https://www.congress.gov/bill/119th-congress/house-bill/4611/text",
               "https://ballotpedia.org/Mike_Thompson_(California)"]),
    ]),

    # ---- Mike Levin (CA-49, D, US Representative) ----
    ("mike-levin", "CA", "Representative", [
        claim("ml3", "mike-levin", "biblical_marriage", 1, False,
              "Voted YES on H.R. 8404, the Respect for Marriage Act (House Vote #373, July 19, 2022), which repealed the Defense of Marriage Act and directed the federal government to recognize same-sex marriages in all states — rejecting the one-man-one-woman definition of marriage. Levin also co-sponsored H.R. 5, the Equality Act, in the 117th Congress (2021-2022), which would enshrine sexual orientation and gender identity as protected classes throughout federal civil-rights law, applying to schools, housing, and public accommodations. Both votes directly oppose the rubric's biblical definition of marriage.",
              ["https://en.wikipedia.org/wiki/Mike_Levin",
               "https://www.govtrack.us/congress/members/mike_levin/412760",
               "https://ballotpedia.org/Mike_Levin"]),
    ]),

    # ---- Judy Chu (CA-28, D, US Representative) ----
    ("judy-chu", "CA", "Representative", [
        claim("jc3", "judy-chu", "self_defense", 1, False,
              "One of 185 original co-sponsors of H.R. 698, the Assault Weapons Ban of 2023 (118th Congress), introduced February 1, 2023. The bill would ban the manufacture, sale, transfer, and possession of semiautomatic 'assault weapons' and large-capacity ammunition magazines — directly opposing the rubric's protection of modern sporting rifles and against magazine bans. Chu also introduced H.R. 4780, the Language Access to Gun Violence Prevention Strategies Act (2023), expanding federal gun-control outreach infrastructure, and consistently votes with the House Gun Violence Prevention Task Force on every major firearm restriction package.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://www.congress.gov/bill/118th-congress/house-bill/4780/text",
               "https://www.govtrack.us/congress/members/judy_chu/412379"]),
    ]),

    # ---- George Whitesides (CA-27, D, US Representative) ----
    ("george-whitesides", "CA", "Representative", [
        claim("gw3", "george-whitesides", "biblical_marriage", 1, False,
              "Listed as a co-introducer of H.R. 15, the Equality Act, in the 119th Congress (2025-2026). The bill adds sexual orientation and gender identity as protected classes across federal civil-rights law, explicitly covering marriage, schools, public accommodations, housing, credit, and employment — writing same-sex marriage equality and LGBTQ non-discrimination into federal statute and directly opposing the rubric's one-man-one-woman marriage standard. Whitesides also backed this framing on his campaign website, pledging to 'protect LGBTQ+ rights' as a congressional priority from the outset of his 2025 term.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/15/text",
               "https://www.govtrack.us/congress/members/george_whitesides/456977",
               "https://ballotpedia.org/George_Whitesides"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
