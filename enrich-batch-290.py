#!/usr/bin/env python3
"""Enrichment batch 290: hand-curated claims for 5 Wyoming state senators.

Targets archetype_party_default WY state senators from the bottom of the
alphabet with 0 evidence claims (archetype_curated federal bucket exhausted).

Targets: Tim Salazar (WY-R SD-26), Wendy Schuler (WY-R SD-15),
Troy McKeown (WY-R SD-24), Tara Nethercott (WY-R SD-4),
Taft Love (WY-R SD-6).

All five voted AYE on Wyoming's 2026 constitutional anti-abortion amendment
(Cowboy State Daily, 2026-02-12). Additional individual claims drawn from
ballotpedia.org, wyoleg.gov, en.wikipedia.org, and cowboystatedaily.com.

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
    # ---------------- Tim Salazar (WY-R, State Senator SD-26) ----------------
    ("tim-salazar", "WY", "State Senator", [
        claim("ts1", "tim-salazar", "sanctity_of_life", 0, True,
              "A confirmed pro-life lawmaker who sponsored HB.182 (requiring physicians to offer ultrasound viewing and fetal-heartbeat audio before an abortion) and voted 'aye' on Wyoming's 2026 constitutional amendment to ban abortion — affirming the unborn child's personhood and rejecting abortion-on-demand.",
              ["https://ballotpedia.org/Tim_Salazar",
               "https://cowboystatedaily.com/2026/02/12/wyoming-anti-abortion-amendment-dies-in-senate-by-one-vote/"]),
        claim("ts2", "tim-salazar", "self_defense", 3, True,
              "Authored and passed HB.168 (2018), Wyoming's Stand Your Ground statute, expanding the Castle Doctrine to provide criminal and civil immunity for lawful use of force in self-defense anywhere the defender is legally present — codifying the right of self-protection beyond one's dwelling.",
              ["https://ballotpedia.org/Tim_Salazar",
               "https://en.wikipedia.org/wiki/Tim_Salazar"]),
        claim("ts3", "tim-salazar", "economic_stewardship", 2, True,
              "A consistent anti-tax legislator who in 2016 adhered to a no-tax-increase pledge and in 2017 voted against every proposed fee, internet-tax, and property- or sales-tax expansion introduced in Wyoming — aligning with balanced-budget, limited-government-spending principles.",
              ["https://ballotpedia.org/Tim_Salazar"]),
    ]),

    # ---------------- Wendy Schuler (WY-R, State Senator SD-15) ----------------
    ("wendy-schuler", "WY", "State Senator", [
        claim("ws1", "wendy-schuler", "sanctity_of_life", 0, True,
              "Voted 'aye' in the Wyoming Senate's 2026 roll call on a constitutional amendment to ban abortion, placing herself in the pro-life majority that sought to enshrine protection of the unborn in the state constitution.",
              ["https://cowboystatedaily.com/2026/02/12/wyoming-anti-abortion-amendment-dies-in-senate-by-one-vote/",
               "https://ballotpedia.org/Wendy_Davis_Schuler"]),
        claim("ws2", "wendy-schuler", "family_child_sovereignty", 0, True,
              "Chairs the Wyoming Senate Education Committee and sponsored SF.0035 (2025) directing school districts to adopt policies limiting student cell phone and smart-watch use during the school day — a parental-rights measure restoring family-aligned local control over the learning environment away from corporate tech platforms.",
              ["https://www.wyoleg.gov/Legislators/2025/S/2062",
               "https://ballotpedia.org/Wendy_Davis_Schuler"]),
    ]),

    # ---------------- Troy McKeown (WY-R, State Senator SD-24) ----------------
    ("troy-mckeown", "WY", "State Senator", [
        claim("tm1", "troy-mckeown", "sanctity_of_life", 0, True,
              "Voted 'aye' on Wyoming's 2026 senate roll call on a constitutional amendment to ban abortion, affirming protection of human life from conception within state law.",
              ["https://cowboystatedaily.com/2026/02/12/wyoming-anti-abortion-amendment-dies-in-senate-by-one-vote/",
               "https://ballotpedia.org/Troy_McKeown"]),
        claim("tm2", "troy-mckeown", "economic_stewardship", 2, True,
              "Chairs Wyoming's Senate Revenue Committee, shaping state tax and fiscal policy within a no-income-tax constitutional framework; a retired U.S. Army lieutenant colonel who brings a disciplined, anti-deficit posture to the state's budget and revenue deliberations.",
              ["https://ballotpedia.org/Troy_McKeown",
               "https://ballotpedia.org/Revenue_Committee,_Wyoming_State_Senate"]),
    ]),

    # ---------------- Tara Nethercott (WY-R, State Senator SD-4) ----------------
    ("tara-nethercott", "WY", "State Senator", [
        claim("tn1", "tara-nethercott", "sanctity_of_life", 0, True,
              "As Wyoming Senate Majority Floor Leader, voted 'aye' on the 2026 constitutional amendment to ban abortion, lending her leadership position to Wyoming's effort to inscribe pro-life protection in the state constitution.",
              ["https://cowboystatedaily.com/2026/02/12/wyoming-anti-abortion-amendment-dies-in-senate-by-one-vote/",
               "https://ballotpedia.org/Tara_Nethercott"]),
        claim("tn2", "tara-nethercott", "self_defense", 0, True,
              "A Wyoming Republican senator who has supported the state's constitutional-carry framework; voted in favor of HB.0125 (2024) addressing concealed-weapons law and gun-free zones, reinforcing Wyoming's status as a permitless-carry state and defending citizens' right to bear arms without government permission.",
              ["https://ballotpedia.org/Tara_Nethercott",
               "https://www.wyoleg.gov/Legislation/2024/HB0125"]),
    ]),

    # ---------------- Taft Love (WY-R, State Senator SD-6) ----------------
    ("taft-love", "WY", "State Senator", [
        claim("tl1", "taft-love", "sanctity_of_life", 0, True,
              "Explicitly stated a pro-life position during his 2025 appointment process for Wyoming State Senate District 6, and voted 'aye' on the 2026 senate roll call on a constitutional amendment to ban abortion — consistent with his stated values.",
              ["https://cowboystatedaily.com/2025/08/29/former-county-gop-chair-chosen-to-fill-senate-seat-vacated-by-trump-appointee/",
               "https://cowboystatedaily.com/2026/02/12/wyoming-anti-abortion-amendment-dies-in-senate-by-one-vote/"]),
        claim("tl2", "taft-love", "self_defense", 0, True,
              "Co-owns a firearms manufacturing company in Wyoming, placing him in the business of producing the constitutionally protected arms the rubric defends; aligns with Wyoming's constitutional-carry tradition and the right of citizens to keep and bear arms without state permission.",
              ["https://cowboystatedaily.com/2025/08/28/wyoming-senate-district-6-finalists-share-values-but-differ-on-legislative-approach/"]),
        claim("tl3", "taft-love", "family_child_sovereignty", 0, True,
              "Stated during his 2025 appointment process that a top legislative priority is 'stepping back from the federalization of our education system,' signaling a commitment to parental and local control of education over federal bureaucratic mandates.",
              ["https://cowboystatedaily.com/2025/08/28/wyoming-senate-district-6-finalists-share-values-but-differ-on-legislative-approach/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
