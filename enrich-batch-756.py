#!/usr/bin/env python3
"""Enrichment batch 756: third claims for 4 sitting U.S. Representatives with 2 claims.

Primary archetype_curated bucket is fully exhausted (all federal officials upgraded to
evidence_curated by batches 1-755). This batch adds a 3rd distinct-category claim to the
4 sitting U.S. Representatives who had only 2 claims, working from the bottom of the
alphabet (AZ → CA → DC).

Targets (all D): Adelita Grijalva (AZ-07), Yassamin Ansari (AZ-03),
Nancy Pelosi (CA-11), Eleanor Holmes Norton (DC-at-large).
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
    # -------- Adelita Grijalva (AZ-07, D) --------
    ("adelita-grijalva", "AZ", "House", [
        claim("ag1", "adelita-grijalva", "border_immigration", 1, False,
              "Voted against the FY2026 DHS Funding Bill that expanded ICE funding, calling ICE 'corrupted to the core' and opposing mandatory deportation; co-introduced the Fund Schools Not ICE Act (July 2026) to redirect $38.5 billion in ICE reconciliation funding to Title I public schools and require DHS to sell 11 newly-purchased detention facilities — directly opposing the rubric's support for mandatory deportation of illegal immigrants.",
              ["https://grijalva.house.gov/media/press-releases/rep-grijalva-reacts-to-passage-of-republican-dhs-funding-bill",
               "https://stanton.house.gov/2026/7/stanton-ansari-grijalva-introduce-bill-to-redirect-ice-funding-to-public-schools-require-sale-of-detention-warehouses"]),
    ]),

    # -------- Yassamin Ansari (AZ-03, D) --------
    ("yassamin-ansari", "AZ", "Representative", [
        claim("ya1", "yassamin-ansari", "self_defense", 1, False,
              "An original cosponsor of the Assault Weapons Ban of 2025 (H.R. 3115, 185 cosponsors), which would ban the manufacture and sale of semiautomatic assault-style weapons and magazines over 15 rounds; endorsed by Giffords PAC during her 2024 campaign and publicly supports universal background checks, raising the minimum purchase age for semiautomatic firearms to 21, and closing the 'boyfriend loophole' — comprehensively opposing the rubric's defense of Second Amendment rights from restrictions.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3115/cosponsors",
               "https://giffords.org/candidates/yassamin-ansari/"]),
    ]),

    # -------- Nancy Pelosi (CA-11, D) --------
    ("nancy-pelosi", "CA", "Representative", [
        claim("np1", "nancy-pelosi", "self_defense", 1, False,
              "As Speaker, led the House passage of H.R. 1808 (Assault Weapons Ban of 2022, Roll Call #410, 217-213, July 29 2022) banning manufacture and sale of semiautomatic assault-style weapons and high-capacity magazines; also voted YES on the Bipartisan Safer Communities Act (S. 2938) which allocated $750 million to fund state red-flag (ERPO) laws; holds a lifetime F rating from the NRA.",
              ["https://www.govtrack.us/congress/votes/117-2022/h410",
               "https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://pelosi.house.gov/news/press-releases/transcript-of-pelosi-floor-speech-on-the-assault-weapons-ban"]),
    ]),

    # -------- Adam Gray (CA-13, D-moderate) --------
    ("adam-gray", "CA", "Representative", [
        claim("agray1", "adam-gray", "self_defense", 1, True,
              "One of only 5 House Democrats (out of 213) to vote YES on H.R. 1181 (Protecting Privacy in Purchases Act, House Vote #240, July 14 2026), prohibiting credit card networks from assigning specific merchant category codes to gun retailers — blocking a de facto gun-purchase tracking system. Also notably absent from the 185-cosponsor Assault Weapons Ban of 2025 (H.R. 3115) co-sponsor list, and carried an NRA 'B' rating during a decade in the California State Assembly — aligning with the rubric's opposition to government tracking and restriction of lawful gun purchases.",
              ["https://www.govtrack.us/congress/votes/119-2026/h240",
               "https://www.congress.gov/bill/119th-congress/house-bill/3115/cosponsors",
               "https://www.kqed.org/news/11922322/adam-gray-talks-water-guns-and-bucking-his-own-party"]),
    ]),

    # -------- Eleanor Holmes Norton (DC, D) --------
    ("eleanor-holmes-norton", "DC", "Delegate", [
        claim("ehn1", "eleanor-holmes-norton", "biblical_marriage", 0, False,
              "A cosponsor of H.R. 8404, the Respect for Marriage Act (2022), codifying federal recognition of same-sex unions and requiring the federal government to recognize any marriage lawful in the state where it was performed; also cosponsored H.Res.269 (Transgender Bill of Rights, March 2023) recognizing a federal duty to protect transgender and nonbinary rights to medical care and economic security — rejecting the one-man-one-woman definition of marriage.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8404/cosponsors",
               "https://www.congress.gov/bill/118th-congress/house-resolution/269/cosponsors",
               "https://norton.house.gov/media/press-releases/norton-condemns-lee-amendment-attacking-dcs-lgbtq-residents"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
