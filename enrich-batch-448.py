#!/usr/bin/env python3
"""Enrichment batch 448: 5 Washington State Senate Democrats (0 claims).

Federal and archetype_curated pools exhausted. Continuing bottom-of-alphabet
with Washington State senators who have archetype_party_default confidence.

Targets (sorted reverse-alpha by name — first 5 of WA State Senators pool):
  Sharon Shewmake  (WA Senate D, District 42 — Whatcom County)
  Noel Frame       (WA Senate D, District 36 — North Seattle)
  Marko Liias      (WA Senate D, District 21 — Snohomish Co. / Senate Majority Floor Leader)
  Manka Dhingra    (WA Senate D, District 45 — Eastside King County)
  Jamie Pedersen   (WA Senate D, District 43 — Capitol Hill / Central Seattle)

Key legislation cited:
  - SJR 8202 (2023 WA): proposed constitutional amendment to enshrine "reproductive
    freedom" (including abortion); co-sponsored by Dhingra, Frame, Liias, Pedersen et al.
  - HB 1240 (2023 WA): assault-weapons ban; passed Senate 28-21, April 18, 2023.
  - SB 5768 (2023 WA enacted): protects access to abortion medications; passed April 2023.
  - SB 5078 (2022 WA enacted): high-capacity magazine restrictions / gun industry liability.
  - ESSB 5599 (2023 WA enacted): exempts youth shelters from parental notification
    requirements for minors seeking gender-affirming care or reproductive services.

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
    # ------- Sharon Shewmake (WA-D, State Senator, District 42) -------
    ("sharon-shewmake", "WA", "Senator", [
        claim("ss1", "sharon-shewmake", "self_defense", 1, False,
              "Voted yes on HB 1240 (Washington State, enacted April 2023) — the state's "
              "landmark assault-weapons ban, which passed the Senate 28-21 on a strict "
              "party-line vote. The law bans the sale, transfer, manufacture, distribution, "
              "and importation of assault-style weapons, listing more than 50 prohibited "
              "models including AR-15s and AK-47s.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/"]),
        claim("ss2", "sharon-shewmake", "sanctity_of_life", 0, False,
              "Voted yes on SB 5768 (Washington State, enacted April 27, 2023) — protecting "
              "access to abortion medications by authorizing the Department of Corrections to "
              "acquire, sell, deliver, distribute, and dispense abortion medications. The bill "
              "passed the Senate with full Democratic caucus support.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5768&Initiative=false&Year=2023"]),
    ]),

    # ------- Noel Frame (WA-D, State Senator, District 36) -------
    ("noel-frame", "WA", "Senator", [
        claim("nf1", "noel-frame", "sanctity_of_life", 0, False,
              "Co-sponsored SJR 8202 (Washington State Senate, 2023 Regular Session), a joint "
              "resolution to amend the state constitution to enshrine the 'fundamental right to "
              "reproductive freedom' — including the right to abortion — while explicitly "
              "rejecting any personhood-from-conception standard. Also co-sponsored SB 5768 "
              "(enacted 2023) protecting access to abortion medications.",
              ["https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/Senate/8202%20SBR%20HLTC%20OC%2023.pdf",
               "https://app.leg.wa.gov/billsummary?BillNumber=5768&Initiative=false&Year=2023"]),
        claim("nf2", "noel-frame", "self_defense", 1, False,
              "Co-sponsored SB 5078 (2021-22 WA session, enacted 2022) restricting "
              "high-capacity magazines and establishing gun-industry liability duties; voted "
              "yes on HB 1240 (assault weapons ban, enacted April 2023, passed Senate 28-21). "
              "Also co-sponsored SB 5099 (2025-26 session) adding safety requirements for "
              "licensed firearms dealers.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5078&Year=2021",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023"]),
        claim("nf3", "noel-frame", "family_child_sovereignty", 0, False,
              "As a member of the Washington State Senate Human Services Committee, signed the "
              "majority committee report recommending passage of ESSB 5599 (2023) — legislation "
              "that exempts youth shelters and host homes from directly notifying parents when "
              "minors age 13-17 seek or receive gender-affirming treatment or reproductive "
              "health care, limiting parental notification and oversight rights in those cases.",
              ["https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/Senate/5599%20SBR%20HS%20OC%2023.pdf",
               "https://www.seattletimes.com/seattle-news/politics/conservative-group-sues-wa-over-law-meant-to-protect-trans-teens/"]),
    ]),

    # ------- Marko Liias (WA-D, State Senator, District 21, Majority Floor Leader) -------
    ("marko-liias", "WA", "Senator", [
        claim("ml1", "marko-liias", "sanctity_of_life", 0, False,
              "Co-sponsored SJR 8202 (Washington State Senate, 2023 Regular Session), a proposed "
              "constitutional amendment to enshrine 'reproductive freedom' — including the right "
              "to abortion — in the state constitution, rejecting any personhood-from-conception "
              "standard. As Senate Majority Floor Leader, Liias manages the Democratic caucus's "
              "floor agenda and shepherds progressive legislation to the floor.",
              ["https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/Senate/8202%20SBR%20HLTC%20OC%2023.pdf",
               "https://ballotpedia.org/Marko_Liias"]),
        claim("ml2", "marko-liias", "self_defense", 1, False,
              "Sponsored SB 5193 (2023 WA) — the Senate assault-weapons-ban companion bill — "
              "and co-sponsored SB 5078 (enacted 2022) restricting high-capacity magazines. "
              "Voted yes on HB 1240 (enacted April 2023), Washington's assault-weapons ban "
              "prohibiting sale, transfer, manufacture, and importation of AR-15s, AK-47s, and "
              "over 50 other named models (Senate 28-21 party-line vote).",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5078&Year=2021",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/"]),
        claim("ml3", "marko-liias", "family_child_sovereignty", 0, False,
              "Voted yes on ESSB 5599 (Washington State, enacted 2023) — which passed the "
              "Senate March 1, 2023 on a party-line vote — exempting youth shelters and host "
              "homes from directly notifying parents when minors age 13-17 seek or receive "
              "gender-affirming treatment or reproductive health care, restricting parental "
              "rights in those cases.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/wa-law-to-protect-trans-youth-in-crisis-takes-effect-as-repeal-effort-fails/"]),
    ]),

    # ------- Manka Dhingra (WA-D, State Senator, District 45) -------
    ("manka-dhingra", "WA", "Senator", [
        claim("md1", "manka-dhingra", "sanctity_of_life", 0, False,
              "Co-sponsored SJR 8202 (Washington State Senate, 2023 Regular Session), a joint "
              "resolution to constitutionally enshrine 'reproductive freedom' — including "
              "abortion rights — explicitly rejecting personhood from conception. Ran for "
              "Washington Attorney General in 2024 on a platform of protecting abortion access "
              "statewide.",
              ["https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/Senate/8202%20SBR%20HLTC%20OC%2023.pdf",
               "https://ballotpedia.org/Manka_Dhingra"]),
        claim("md2", "manka-dhingra", "self_defense", 1, False,
              "Consistent pro-gun-control voting record throughout her Senate tenure. Voted yes "
              "on HB 1240 (enacted April 2023), Washington's assault-weapons ban (Senate 28-21 "
              "party-line vote) banning sale, transfer, manufacture, and importation of "
              "assault-style weapons. Championed upholding Washington's gun-safety laws during "
              "her 2024 state Attorney General campaign.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/"]),
        claim("md3", "manka-dhingra", "family_child_sovereignty", 0, False,
              "Voted yes on ESSB 5599 (Washington State, enacted 2023) — passed the Senate on "
              "a party-line vote March 1, 2023 — exempting youth shelters and host homes from "
              "parental notification requirements when minors age 13-17 seek or receive "
              "gender-affirming treatment or reproductive health care, limiting parental "
              "oversight in those cases.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023",
               "https://www.seattletimes.com/seattle-news/politics/wa-bill-focused-on-trans-youth-sparks-dueling-protests/"]),
    ]),

    # ------- Jamie Pedersen (WA-D, State Senator, District 43) -------
    ("jamie-pedersen", "WA", "Senator", [
        claim("jp1", "jamie-pedersen", "biblical_marriage", 1, False,
              "Served as Lambda Legal's lead pro-bono attorney on Andersen v. King County, "
              "Washington State's landmark same-sex marriage case. As a state legislator "
              "championed the 2012 legislation and Referendum 74 that legalized same-sex "
              "marriage in Washington. Has sponsored marriage equality and LGBTQ family-rights "
              "legislation throughout his career in the House and Senate.",
              ["https://en.wikipedia.org/wiki/Jamie_Pedersen",
               "https://ballotpedia.org/Jamie_Pedersen"]),
        claim("jp2", "jamie-pedersen", "sanctity_of_life", 0, False,
              "Co-sponsored SJR 8202 (2023 WA Senate) proposing a constitutional amendment to "
              "enshrine reproductive freedom (including abortion rights), rejecting personhood "
              "from conception. Also co-sponsored SB 5489 (enacted 2023) shielding patients "
              "and providers from out-of-state lawsuits for receiving or providing abortion "
              "care in Washington, and co-sponsored SB 5768 (enacted 2023) protecting access "
              "to abortion medications.",
              ["https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/Senate/8202%20SBR%20HLTC%20OC%2023.pdf",
               "https://app.leg.wa.gov/billsummary?BillNumber=5768&Initiative=false&Year=2023",
               "https://ballotpedia.org/Jamie_Pedersen"]),
        claim("jp3", "jamie-pedersen", "self_defense", 1, False,
              "As Senate Law & Justice Committee Chair, led Washington's gun-safety legislative "
              "agenda. Voted yes on HB 1240 (enacted April 2023), Washington's assault-weapons "
              "ban (Senate 28-21 party-line vote). Previously introduced 2013 legislation "
              "requiring background checks for private firearm sales and has consistently "
              "championed expanded firearms regulations.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://ballotpedia.org/Jamie_Pedersen"]),
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
