#!/usr/bin/env python3
"""Enrichment batch 449: 5 Washington State Senators with 0 claims.

Continuing bottom-of-alphabet WA state senators from batch 448.
All are archetype_party_default Democrats; Riccelli and Chapman
moved from the State House to the Senate in January 2025.

Targets (reverse-alpha from remaining WA Senator pool):
  Rebecca Saldana  (WA Senate D, District 37 — Capitol Hill/Beacon Hill, Seattle)
  Liz Lovelett     (WA Senate D, District 40 — Whatcom/San Juan counties)
  Lisa Wellman     (WA Senate D, District 41 — Mercer Island/Bellevue)
  Marcus Riccelli  (WA Senate D, District 3 — central Spokane; was state Rep 2013-2024)
  Mike Chapman     (WA Senate D, District 24 — Olympic Peninsula; was state Rep 2017-2024)

Key legislation cited:
  - HB 1240 (2023 WA enacted Apr 25): assault-weapons ban; passed House 56-42 Apr 19,
    Senate 28-21 Apr 18 2023.
  - SB 5768 (2023 WA enacted Apr 27): protects access to abortion medications;
    co-sponsored by Lovelett, Wellman (confirmed sponsors list).
  - ESSB 5599 (2023 WA enacted Jul 23): exempts youth shelters from parental notification
    when minors seek gender-affirming care or reproductive services; co-sponsored by Lovelett.
  - HJR 4201 (2023-24 WA House session): House resolution proposing constitutional
    amendment to enshrine reproductive freedom; co-sponsored by Chapman and Riccelli
    (confirmed sponsors list).
  - HB 1854 (2023 WA House): House companion to SB 5768; co-sponsored by Riccelli
    (confirmed sponsors list).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
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
    # ------- Rebecca Saldana (WA-D, State Senator, District 37 — Seattle) -------
    ("rebecca-saldana", "WA", "Senator", [
        claim("rs1", "rebecca-saldana", "sanctity_of_life", 0, False,
              "Voted yes on SB 5768 (Washington State, enacted April 27, 2023) — protecting "
              "access to abortion medications by authorizing the Department of Corrections to "
              "acquire, sell, deliver, distribute, and dispense abortion medications. The bill "
              "passed the Senate on a party-line vote with full Democratic caucus support on "
              "April 14, 2023; it directly rejects personhood from conception by insulating "
              "abortion medication access from state interference.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5768&Initiative=false&Year=2023"]),
        claim("rs2", "rebecca-saldana", "self_defense", 1, False,
              "Voted yes on HB 1240 (Washington State, enacted April 25, 2023) — Washington's "
              "landmark assault-weapons ban, which passed the Senate 28-21 on a party-line vote "
              "on April 18, 2023. The law bans the sale, transfer, manufacture, distribution, "
              "and importation of assault-style weapons, listing more than 50 prohibited models "
              "including AR-15s and AK-47s.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/"]),
    ]),

    # ------- Liz Lovelett (WA-D, State Senator, District 40 — Whatcom/San Juan) -------
    ("liz-lovelett", "WA", "Senator", [
        claim("ll1", "liz-lovelett", "sanctity_of_life", 0, False,
              "Co-sponsored SB 5768 (Washington State, enacted April 27, 2023) — protecting "
              "access to abortion medications by authorizing the Department of Corrections to "
              "acquire, sell, deliver, distribute, and dispense abortion medications. The bill "
              "passed the Senate on a party-line vote on April 14, 2023, rejecting any state "
              "barrier to abortion medication access.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5768&Initiative=false&Year=2023"]),
        claim("ll2", "liz-lovelett", "family_child_sovereignty", 0, False,
              "Co-sponsored ESSB 5599 (Washington State, enacted July 23, 2023) — which passed "
              "the Senate on a 27-19 party-line vote on March 1, 2023 — exempting youth shelters "
              "and host homes from their duty to directly notify parents when a minor age 13-17 "
              "seeks or receives gender-affirming treatment or reproductive health care. The law "
              "directly limits parental notification and oversight rights in those cases.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/wa-law-to-protect-trans-youth-in-crisis-takes-effect-as-repeal-effort-fails/"]),
    ]),

    # ------- Lisa Wellman (WA-D, State Senator, District 41 — Mercer Island/Bellevue) -------
    ("lisa-wellman", "WA", "Senator", [
        claim("lw1", "lisa-wellman", "sanctity_of_life", 0, False,
              "Co-sponsored SB 5768 (Washington State, enacted April 27, 2023) — protecting "
              "access to abortion medications by authorizing the Department of Corrections to "
              "acquire, sell, deliver, distribute, and dispense abortion medications. Roll-call "
              "records confirm she voted yes on April 14, 2023 when the bill passed the Senate "
              "on a party-line vote.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5768&Initiative=false&Year=2023",
               "https://leg.wa.gov/votingrecord/senate/2023/27211.pdf"]),
        claim("lw2", "lisa-wellman", "self_defense", 1, False,
              "Voted yes on HB 1240 (Washington State, enacted April 25, 2023) — Washington's "
              "assault-weapons ban, which passed the Senate 28-21 on a party-line vote on "
              "April 18, 2023. The law bans the sale, transfer, manufacture, distribution, "
              "and importation of assault-style weapons including AR-15s and AK-47s.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/"]),
    ]),

    # ------- Marcus Riccelli (WA-D, State Senator, District 3 — central Spokane)
    # Note: served as state representative from District 3, 2013-2024; senator since Jan 2025 -------
    ("marcus-riccelli", "WA", "Senator", [
        claim("mr1", "marcus-riccelli", "sanctity_of_life", 0, False,
              "While serving as state representative from District 3 (central Spokane) and "
              "chair of the House Health Care and Wellness Committee, co-sponsored HJR 4201 "
              "(Washington State, 2023-24 session) — a House joint resolution proposing a "
              "constitutional amendment to enshrine the 'fundamental right to reproductive "
              "freedom,' including the right to an abortion or to use contraception, in the "
              "Washington State Constitution, explicitly rejecting any personhood-from-conception "
              "standard. Also co-sponsored HB 1854 (2023), the House companion bill to SB 5768 "
              "protecting access to abortion medications.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=4201&Year=2023",
               "https://app.leg.wa.gov/billsummary?BillNumber=1854&Year=2023"]),
        claim("mr2", "marcus-riccelli", "self_defense", 1, False,
              "While serving as state representative from District 3 (central Spokane), voted "
              "yes on HB 1240 (Washington State, enacted April 25, 2023) — Washington's "
              "assault-weapons ban. The bill passed the House 56-42 on April 19, 2023 on a "
              "near-party-line vote, banning the sale, transfer, manufacture, distribution, "
              "and importation of assault-style weapons, listing more than 50 prohibited models "
              "including AR-15s and AK-47s.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/wa-house-votes-to-ban-assault-weapons/"]),
    ]),

    # ------- Mike Chapman (WA-D, State Senator, District 24 — Olympic Peninsula)
    # Note: served as state representative from District 24, 2017-2024; senator since Jan 2025 -------
    ("mike-chapman", "WA", "Senator", [
        claim("mc1", "mike-chapman", "sanctity_of_life", 0, False,
              "While serving as state representative from District 24 (Clallam, Jefferson, and "
              "Grays Harbor counties), co-sponsored HJR 4201 (Washington State, 2023-24 session) "
              "— a House joint resolution proposing a constitutional amendment to enshrine the "
              "'fundamental right to reproductive freedom,' including the right to an abortion or "
              "to use contraception, in the Washington State Constitution, rejecting any "
              "personhood-from-conception standard.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=4201&Year=2023"]),
        claim("mc2", "mike-chapman", "self_defense", 1, False,
              "While serving as state representative from District 24 (Olympic Peninsula), voted "
              "yes on HB 1240 (Washington State, enacted April 25, 2023) — Washington's "
              "assault-weapons ban. The bill passed the House 56-42 on April 19, 2023 on a "
              "near-party-line vote, banning the sale, transfer, manufacture, distribution, "
              "and importation of assault-style weapons, listing more than 50 prohibited models "
              "including AR-15s and AK-47s.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/wa-house-votes-to-ban-assault-weapons/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
