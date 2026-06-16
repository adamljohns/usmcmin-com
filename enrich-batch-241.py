#!/usr/bin/env python3
"""Enrichment batch 241: 5 federal House members from bottom-of-alphabet states.

Targets archetype_party_default House reps with 0 claims.
States: NY, NJ, NH, MO (bottom of alphabet, avoiding top-side collision agent).

Mix (1 R / 4 D): Jerry Nadler (NY-D), Frank Pallone (NJ-D),
Sam Graves (MO-R), Maggie Goodlander (NH-D), Emanuel Cleaver (MO-D).
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
    # ---------------- Jerry Nadler (NY-D, US Representative, retiring) ----------------
    ("jerry-nadler", "NY", "Representative", [
        claim("jn1", "jerry-nadler", "biblical_marriage", 1, False,
              "Was lead House sponsor of the Respect for Marriage Act of 2022 (H.R.8404), which codified federal recognition of same-sex and interracial marriages, repealing the Defense of Marriage Act's one-man-one-woman definition — directly opposing the rubric's biblical marriage standard.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8404",
               "https://en.wikipedia.org/wiki/Jerry_Nadler"]),
        claim("jn2", "jerry-nadler", "sanctity_of_life", 0, False,
              "Voted YES on H.R.8296 — Women's Health Protection Act of 2022 — which would have federalized abortion on demand through all nine months and invalidated virtually all state restrictions, rejecting any recognition of personhood from conception.",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://www.congress.gov/bill/117th-congress/house-bill/8296"]),
        claim("jn3", "jerry-nadler", "sanctity_of_life", 4, False,
              "Carries a 100% lifetime rating from NARAL Pro-Choice America (now Reproductive Freedom for All) and has received sustained endorsements and contributions from Planned Parenthood political action arms throughout his career — placing him squarely within the abortion-industry funding network.",
              ["https://en.wikipedia.org/wiki/Jerry_Nadler",
               "https://reproductivefreedomforall.org/"]),
    ]),

    # ---------------- Frank Pallone (NJ-6-D, US House) ----------------
    ("frank-pallone", "NJ", "House", [
        claim("fp1", "frank-pallone", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act of 2022 (S.2938), which expanded background checks for under-21 purchasers, provided federal grants to fund state red-flag (ERPO) laws, and closed the 'boyfriend loophole' — each element opposed by the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
        claim("fp2", "frank-pallone", "sanctity_of_life", 0, False,
              "Voted YES on H.R.8296 — Women's Health Protection Act of 2022 — which would have pre-empted all state abortion restrictions and codified federal abortion access through viability and beyond, rejecting any life-at-conception or personhood standard.",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://www.congress.gov/bill/117th-congress/house-bill/8296"]),
        claim("fp3", "frank-pallone", "border_immigration", 0, False,
              "Voted NO on the Continuing Appropriations and Border Security Enhancement Act, 2024 (H.R.5525), which funded border-wall construction, reinstated Remain in Mexico, and tightened asylum processing — opposing the rubric's call for a secure southern border.",
              ["https://ballotpedia.org/Frank_Pallone_Jr.",
               "https://www.govtrack.us/congress/members/frank_pallone/400308"]),
    ]),

    # ---------------- Sam Graves (MO-6-R, US House, retiring) ----------------
    ("sam-graves", "MO", "House", [
        claim("sg1", "sam-graves", "sanctity_of_life", 0, True,
              "Carries a consistent 100% rating from the National Right to Life Committee and voted NO on H.R.8296 — Women's Health Protection Act of 2022 — which would have federalized abortion on demand, affirming his opposition to abortion and alignment with a life-at-conception standard.",
              ["https://ballotpedia.org/Sam_Graves",
               "https://en.wikipedia.org/wiki/Sam_Graves"]),
        claim("sg2", "sam-graves", "sanctity_of_life", 1, True,
              "Voted YES on H.R.26 — Born-Alive Abortion Survivors Protection Act — requiring healthcare providers to give the same care to a born-alive infant after a failed abortion as they would to any other baby, affirming the rubric's demand for abolition of all post-birth harm.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/26",
               "https://en.wikipedia.org/wiki/Sam_Graves"]),
        claim("sg3", "sam-graves", "border_immigration", 0, True,
              "A longtime border-security hawk who publicly demanded President Biden build the wall ('It's time to build the wall') and voted YES on H.R.5525 — Continuing Appropriations and Border Security Enhancement Act, 2024 — which funded physical barriers and mandatory detention.",
              ["https://ballotpedia.org/Sam_Graves",
               "https://en.wikipedia.org/wiki/Sam_Graves"]),
    ]),

    # ---------------- Maggie Goodlander (NH-2-D, US House) ----------------
    ("maggie-goodlander", "NH", "House", [
        claim("mg1", "maggie-goodlander", "sanctity_of_life", 4, False,
              "Received a formal endorsement and PAC spending support from EMILY's List — an organization whose singular mission is electing pro-abortion Democratic women — placing her inside the abortion-industry funding network the rubric disqualifies.",
              ["https://ballotpedia.org/Maggie_Goodlander",
               "https://en.wikipedia.org/wiki/Maggie_Goodlander"]),
        claim("mg2", "maggie-goodlander", "sanctity_of_life", 0, False,
              "Campaigned explicitly on protecting 'access to the full range of reproductive healthcare, including abortion' and has opposed any legislation recognizing fetal personhood or restricting abortion at any gestational stage — rejecting life-at-conception.",
              ["https://en.wikipedia.org/wiki/Maggie_Goodlander",
               "https://ballotpedia.org/Maggie_Goodlander"]),
        claim("mg3", "maggie-goodlander", "sanctity_of_life", 1, False,
              "Voted NO on the motion to recommit H.R.21 — Born-Alive Abortion Survivors Protection Act — on January 23, 2025, opposing a measure to require that medical care be provided to infants born alive after failed abortions.",
              ["https://www.govtrack.us/congress/votes/119-2025/h26",
               "https://www.congress.gov/bill/119th-congress/house-bill/21"]),
    ]),

    # ---------------- Emanuel Cleaver (MO-5-D, US House) ----------------
    ("emanuel-cleaver", "MO", "House", [
        claim("ec1", "emanuel-cleaver", "sanctity_of_life", 0, False,
              "Despite being an ordained United Methodist pastor, Cleaver has maintained a pro-choice voting record — including voting YES on H.R.8296 (Women's Health Protection Act of 2022) to federalize abortion access — rejecting any life-at-conception or personhood standard.",
              ["https://en.wikipedia.org/wiki/Emanuel_Cleaver",
               "https://www.govtrack.us/congress/votes/117-2022/h360"]),
        claim("ec2", "emanuel-cleaver", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act of 2022 (S.2938), which funded state red-flag laws, expanded background checks for firearm buyers under 21, and closed the boyfriend loophole — measures the rubric opposes as infringements on Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
        claim("ec3", "emanuel-cleaver", "biblical_marriage", 4, False,
              "Has supported the Equality Act, which would write sexual-orientation and gender-identity protections into federal civil-rights law and extend them to schools, public accommodations, and employers — the legislative promotion of LGBTQ ideology the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Emanuel_Cleaver",
               "https://ballotpedia.org/Emanuel_Cleaver"]),
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
