#!/usr/bin/env python3
"""Enrichment batch 469: hand-curated claims for 5 WA State Senators.

Primary federal bucket (archetype_curated senators/reps with 0 claims) is
now exhausted; pivoting to archetype_party_default State Senators at the
bottom of the alphabet. All 5 targets are WA Democrats whose 2023-2025
records are well-documented.

Targets: Bob Hasegawa (WA-11), John Lovick (WA-44), Jessica Bateman (WA-22),
Drew Hansen (WA-23), Emily Alvarado (WA-34).

Each claim cites >=1 reliable source and reflects 2023-2025 voting
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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------------- Bob Hasegawa (WA-11, D, State Senator) ----------------
    ("bob-hasegawa", "WA", "Senator", [
        claim("bh1", "bob-hasegawa", "family_child_sovereignty", 0, False,
              "Co-sponsored SB 5599 (2023), which allows licensed youth shelters to notify the Department of Children, Youth and Families instead of parents when a minor seeks gender-affirming care or reproductive health services — stripping parental notification rights for life-and-identity decisions. Signed into law July 2023.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023&Initiative=false",
               "https://komonews.com/news/local/senate-bill-5599-transgender-at-risk-youth-gender-affirming-reproductive-care-washington-state-shelters-dcyf-foster-kids-protests-rallies-governor-jay-inslee-olympia-state-capitol-lgbtq-children"]),
        claim("bh2", "bob-hasegawa", "self_defense", 1, False,
              "Voted yes on HB 1240 (April 2023), Washington's assault-style weapons ban prohibiting the sale, transfer, and import of AR-15s, AK-47s, and more than 50 named firearms; the Senate cleared the ban 27-21 on a near-party-line vote.",
              ["https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/",
               "https://ballotpedia.org/Bob_Hasegawa"]),
    ]),

    # ---------------- John Lovick (WA-44, D, State Senator) ----------------
    ("john-lovick", "WA", "Senator", [
        claim("jl1", "john-lovick", "self_defense", 1, False,
              "Voted yes on HB 1240 (April 2023), Washington's assault-style weapons ban banning AR-15s, AK-47s, and 50+ firearm models; notable as a former U.S. Coast Guard member and Snohomish County Sheriff who nonetheless supported the restriction. Senate vote: 27-21.",
              ["https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/",
               "https://ballotpedia.org/John_Lovick"]),
        claim("jl2", "john-lovick", "family_child_sovereignty", 0, False,
              "Voted yes on SB 5599 (2023), allowing licensed shelters to contact DCYF rather than parents when a minor seeks gender-affirming care or reproductive health services, overriding parental authority in those sensitive decisions.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023&Initiative=false",
               "https://senatedemocrats.wa.gov/lovick/"]),
    ]),

    # ---------------- Jessica Bateman (WA-22, D, State Senator) ----------------
    ("jessica-bateman", "WA", "Senator", [
        claim("jb1", "jessica-bateman", "sanctity_of_life", 0, False,
              "As a state House member, sponsored HB 1115 (2023) eliminating cost-sharing and copays for abortion care statewide and co-sponsored legislation authorizing the Washington Department of Corrections to distribute mifepristone — rejecting any recognition of personhood from conception and expanding abortion infrastructure.",
              ["https://senatedemocrats.wa.gov/bateman/biography/",
               "https://app.leg.wa.gov/BillSponsorship/Member?Chamber=House&ChannelName=bateman&Biennium=2023-24"]),
        claim("jb2", "jessica-bateman", "self_defense", 1, False,
              "As a House member, voted yes on HB 1240 (March 2023), Washington's assault-style weapons ban banning AR-15s, AK-47s, and 50+ firearm models; the House passed the bill 55-42 on a near-party-line vote.",
              ["https://www.seattletimes.com/seattle-news/politics/wa-house-votes-to-ban-assault-weapons/",
               "https://ballotpedia.org/Jessica_Bateman"]),
    ]),

    # ---------------- Drew Hansen (WA-23, D, State Senator) ----------------
    ("drew-hansen", "WA", "Senator", [
        claim("dh1", "drew-hansen", "sanctity_of_life", 0, False,
              "Sponsored HB 1469 (2023), Washington's 'Shield Law' that bars compliance with out-of-state subpoenas tied to abortion or gender-affirming care, prohibits cooperation with out-of-state investigations, and bans extradition for such services performed legally in Washington — actively expanding abortion access while denying any personhood or life-protection framework.",
              ["https://legiscan.com/WA/bill/HB1469/2023",
               "https://medium.com/wagovernor/inslee-signs-laws-to-protect-reproductive-health-and-gender-affirming-care-db8917021cd7"]),
        claim("dh2", "drew-hansen", "self_defense", 1, False,
              "Supported Washington's ongoing gun-restriction agenda; voted yes as a senator on the 2025 permit-to-purchase legislation that cleared the Washington Senate and imposed new licensing requirements before citizens may acquire firearms — a policy the rubric's self-defense standard opposes.",
              ["https://washingtonstatestandard.com/2025/03/08/controversial-permit-to-purchase-gun-bill-clears-washington-senate/",
               "https://ballotpedia.org/Drew_Hansen"]),
    ]),

    # ---------------- Emily Alvarado (WA-34, D, State Senator) ----------------
    ("emily-alvarado", "WA", "Senator", [
        claim("ea1", "emily-alvarado", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates of Washington for her 2025 special election to the State Senate, placing her squarely within the abortion-advocacy network the rubric's 'never took PP/NARAL/EMILY money' standard identifies as disqualifying.",
              ["https://ballotpedia.org/Emily_Alvarado_(politician)",
               "https://senatedemocrats.wa.gov/alvarado/"]),
        claim("ea2", "emily-alvarado", "biblical_marriage", 2, False,
              "Has publicly committed to always defending LGBTQ rights and voted as a House member for legislation advancing transgender access to healthcare for youth (SB 5599, 2023) — rejecting the rubric's standard of opposing promotion of transgender ideology in law and policy.",
              ["https://senatedemocrats.wa.gov/alvarado/2025/02/21/from-the-desk-of-your-new-state-senator-2/",
               "https://ballotpedia.org/Emily_Alvarado_(politician)"]),
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
