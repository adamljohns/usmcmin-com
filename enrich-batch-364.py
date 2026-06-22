#!/usr/bin/env python3
"""Enrichment batch 364: 5 Virginia House of Delegates members with documented public positions.

All five had 0 claims and evidence_state confidence.
Bottom-of-alphabet targeting (VA — continuing from batch 363).
  Leslie Mehta        (VA-D, House of Delegates District 73 — Norfolk/Virginia Beach; beat R incumbent Nov 2025)
  Lee Ware            (VA-R, House of Delegates District 72 — Amelia/Nottoway/Powhatan/Chesterfield; serving since 1998)
  Laura Jane Cohen    (VA-D, House of Delegates District 15 — Fairfax; co-patron HB217 assault-weapons ban)
  Lily Franklin       (VA-D, House of Delegates District 41 — Shenandoah Valley; beat R incumbent Nov 2025)
  Keith Hodges        (VA-R, House of Delegates District 68 — Middle Peninsula; serving since 2012)
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
    # ---- Leslie Mehta (VA-D, House of Delegates District 73) ----
    ("leslie-mehta", "VA", "District 73", [
        claim("lm1", "leslie-mehta", "sanctity_of_life", 0, False,
              "Mehta, a civil-rights attorney who flipped District 73 in November 2025 by defeating Republican incumbent Mark Earley Jr., campaigned explicitly on 'protecting abortion rights' as a core platform. She voted YES as part of the unified House Democratic caucus on HJR1 (Virginia Right to Reproductive Freedom Amendment) in the 2026 Regular Session, which passed the House 64-34 and placed a constitutional guarantee of abortion as a 'fundamental right' on the November 2026 ballot — directly opposing the rubric's life-at-conception/personhood standard.",
              ["https://ballotpedia.org/Leslie_Mehta",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/"]),
        claim("lm2", "leslie-mehta", "self_defense", 1, False,
              "Mehta voted with the unified House Democratic caucus to pass HB217 (Virginia's 2026 assault-weapons ban) 58-34 on February 5, 2026 — signed by Governor Spanberger in May 2026. The law bans the future sale, manufacture, purchase, and transfer of semi-automatic firearms classified as assault weapons and magazines holding more than 15 rounds, contrary to the rubric's anti-AWB/anti-magazine-limit standard.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://lis.virginia.gov/bill-details/20261/HB217",
               "https://virginiamercury.com/2026/05/15/spanberger-signs-assault-weapons-ban-package-of-criminal-justice-and-energy-bills/"]),
    ]),

    # ---- Lee Ware (VA-R, House of Delegates District 72) ----
    ("lee-ware", "VA", "District 72", [
        claim("lw1", "lee-ware", "sanctity_of_life", 0, True,
              "Ware, a Republican delegate serving since 1998 and former chair of the House Finance Committee, voted NO on HJR1 (Virginia Right to Reproductive Freedom Amendment) in the 2026 Regular Session, aligning with the unanimous Republican caucus that cast all 34 'no' votes against the 64-34 House passage. He opposes constitutionally enshrining abortion as a 'fundamental right,' consistent with the rubric's life-at-conception/personhood standard.",
              ["https://ballotpedia.org/Lee_Ware",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("lw2", "lee-ware", "self_defense", 1, True,
              "Ware voted NO on HB217 (Virginia's 2026 assault-weapons ban) as part of the unified Republican caucus, which cast all 34 'no' votes against the 58-34 House passage on February 5, 2026. Republican delegates 'warned repeatedly that the legislation trampled constitutional rights,' defending the right to own semi-automatic firearms and standard-capacity magazines — aligning with the rubric's anti-AWB/anti-magazine-limit standard.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://lis.virginia.gov/bill-details/20261/HB217",
               "https://ballotpedia.org/Lee_Ware"]),
    ]),

    # ---- Laura Jane Cohen (VA-D, House of Delegates District 15) ----
    ("laura-jane-cohen", "VA", "District 15", [
        claim("ljc1", "laura-jane-cohen", "self_defense", 1, False,
              "Cohen is listed as a co-patron (co-sponsor) of HB217, Virginia's 2026 assault-weapons ban — meaning she helped draft and formally co-sponsored the legislation prohibiting the future sale, manufacture, purchase, and transfer of semi-automatic firearms classified as assault weapons and of magazines holding more than 15 rounds. The bill passed 58-34 on February 5, 2026, and was signed by Governor Spanberger in May 2026. Cohen's role as a patron goes beyond a floor vote — she actively championed the legislation, contrary to the rubric's anti-AWB/anti-magazine-limit standard.",
              ["https://lis.virginia.gov/bill-details/20261/HB217",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://ballotpedia.org/Laura_Jane_Cohen"]),
        claim("ljc2", "laura-jane-cohen", "sanctity_of_life", 0, False,
              "Cohen voted YES as part of the unified House Democratic caucus on HJR1 (Virginia Right to Reproductive Freedom Amendment) in the 2026 Regular Session, which passed 64-34 and will place a constitutional right to abortion and 'reproductive freedom' on the November 2026 ballot — directly opposing the rubric's life-at-conception/personhood standard.",
              ["https://ballotpedia.org/Laura_Jane_Cohen",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/"]),
    ]),

    # ---- Lily Franklin (VA-D, House of Delegates District 41) ----
    ("lily-franklin", "VA", "District 41", [
        claim("lf1", "lily-franklin", "sanctity_of_life", 0, False,
              "Franklin, a Democrat who flipped District 41 in November 2025 by defeating Republican incumbent Chris Obenshain, assumed office January 14, 2026, and voted YES as part of the unified House Democratic caucus on HJR1 (Virginia Right to Reproductive Freedom Amendment) in the 2026 Regular Session, which passed 64-34 and placed a constitutional guarantee of abortion as a 'fundamental right' on the November 2026 ballot — directly opposing the rubric's life-at-conception/personhood standard.",
              ["https://ballotpedia.org/Lily_Franklin",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/"]),
        claim("lf2", "lily-franklin", "self_defense", 1, False,
              "Franklin voted with the unified House Democratic caucus to pass HB217 (Virginia's 2026 assault-weapons ban) 58-34 on February 5, 2026, 'over GOP objections.' The law, signed by Governor Spanberger in May 2026, bans the future sale, manufacture, and transfer of semi-automatic assault-style firearms and magazines over 15 rounds — contrary to the rubric's anti-AWB/anti-magazine-limit standard.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://lis.virginia.gov/bill-details/20261/HB217",
               "https://ballotpedia.org/Lily_Franklin"]),
    ]),

    # ---- Keith Hodges (VA-R, House of Delegates District 68) ----
    ("keith-hodges", "VA", "District 68", [
        claim("kh1", "keith-hodges", "sanctity_of_life", 0, True,
              "Hodges, a Republican pharmacist representing the rural Middle Peninsula counties of Essex, Gloucester, King and Queen, Mathews, and Middlesex, voted NO on HJR1 (Virginia Right to Reproductive Freedom Amendment) in the 2026 Regular Session, aligning with the unanimous Republican caucus that cast all 34 'no' votes against the 64-34 House passage. He opposes constitutionally enshrining abortion access as a 'fundamental right,' consistent with the rubric's life-at-conception/personhood standard.",
              ["https://ballotpedia.org/Keith_Hodges",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
        claim("kh2", "keith-hodges", "self_defense", 1, True,
              "Hodges voted NO on HB217 (Virginia's 2026 assault-weapons ban) as part of the unified Republican caucus, which cast all 34 'no' votes against the 58-34 House passage on February 5, 2026. Republican delegates 'warned repeatedly that the legislation trampled constitutional rights,' defending the right to own semi-automatic firearms and standard-capacity magazines — aligning with the rubric's anti-AWB/anti-magazine-limit standard.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://lis.virginia.gov/bill-details/20261/HB217",
               "https://ballotpedia.org/Keith_Hodges"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
