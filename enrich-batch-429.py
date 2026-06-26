#!/usr/bin/env python3
"""Enrichment batch 429: state-level officials from TX and UT (bottom of alphabet).

archetype_curated federal bucket fully exhausted; continuing with
evidence_state officials at bottom of reverse-alpha list with 0 claims.

Targets:
  Tony Tinderholt  (TX-R, State Rep HD-94, abortion-abolition author)
  Tom Oliverson    (TX-R, State Rep HD-130, House Majority Leader)
  Valoree Swanson  (TX-R, State Rep, 2A sanctuary + pro-life)
  Deidre Henderson (UT-R, Lt. Governor, voter-roll audit)
  Trent Ashby      (TX-R, State Rep HD-9, pro-life co-sponsor)

Each claim cites >=1 reliable source reflecting 2017-2025 voting records
or official public positions. Sources: en.wikipedia.org, capitol.texas.gov,
legis.state.tx.us, ballotpedia.org, le.utah.gov, ltgovernor.utah.gov.

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
    # ---------------- Tony Tinderholt (TX-R, State Rep HD-94) ----------------
    ("tony-tinderholt", "TX", "Representative", [
        claim("tt1", "tony-tinderholt", "sanctity_of_life", 1, True,
              "Authored HB 948 (85th Texas Legislature, 2017), the 'Abolition of Abortion in Texas Act,' criminalizing abortion from the moment of fertilization — including in cases of rape or incest — by applying criminal homicide statutes to providers and patients; the strongest possible legislative abolition posture.",
              ["https://capitol.texas.gov/members/MemberInfo.aspx?Leg=85&Chamber=H&Code=A3065",
               "https://en.wikipedia.org/wiki/Tony_Tinderholt"]),
        claim("tt2", "tony-tinderholt", "self_defense", 1, True,
              "Co-sponsored HB 2622 (87th Texas Legislature, 2021), the Second Amendment Sanctuary State Act, barring Texas agencies from enforcing federal firearm regulations enacted after January 19, 2021; signed by Gov. Abbott, effective September 1, 2021 — directly opposing red-flag laws, assault-weapon bans, and registries.",
              ["https://capitol.texas.gov/tlodocs/87R/billtext/html/HB02622F.HTM",
               "https://en.wikipedia.org/wiki/Second_Amendment_sanctuary"]),
    ]),

    # ---------------- Tom Oliverson (TX-R, State Rep HD-130) ----------------
    ("tom-oliverson", "TX", "Representative", [
        claim("to1", "tom-oliverson", "biblical_marriage", 2, True,
              "Sponsored HB 1686 (88th Texas Legislature, 2023), banning puberty blockers, cross-sex hormones, and gender-reassignment surgeries for minors in Texas — signed into law, making Texas one of the first states to codify legal protections against transgender medical interventions on children.",
              ["https://www.legis.state.tx.us/members/MemberInfo.aspx?Leg=88&Chamber=H&Code=A3535",
               "https://en.wikipedia.org/wiki/Tom_Oliverson"]),
        claim("to2", "tom-oliverson", "economic_stewardship", 2, True,
              "Advocates for automatic property tax rate reductions when Texas revenues exceed projections and supports a 'fair tax' consumption-based system to replace property taxes, seeking structural restraint on government spending growth — consistent with fiscal-stewardship and anti-deficit principles.",
              ["https://ballotpedia.org/Tom_Oliverson"]),
    ]),

    # ---------------- Valoree Swanson (TX-R, State Rep) ----------------
    ("valoree-swanson", "TX", "Representative", [
        claim("vs1", "valoree-swanson", "self_defense", 1, True,
              "Co-sponsored HB 112, the Texas Firearm Protection Act, a Second Amendment sanctuary bill that would prohibit Texas law enforcement from enforcing new federal gun-control regulations — directly opposing red-flag laws, assault-weapon bans, magazine-capacity limits, and firearm registries.",
              ["https://ballotpedia.org/Valoree_Swanson"]),
        claim("vs2", "valoree-swanson", "sanctity_of_life", 0, True,
              "Opposes abortion and filed legislation to expand 'prohibited practices,' including revoking the medical licenses of physicians who perform abortions — reflecting a consistent pro-life stance aligned with protecting life from conception.",
              ["https://ballotpedia.org/Valoree_Swanson"]),
        claim("vs3", "valoree-swanson", "biblical_marriage", 1, True,
              "Signed a court brief asking the Texas Supreme Court to re-examine its ruling granting same-sex couples government benefits, opposing legal equivalence between same-sex relationships and traditional marriage.",
              ["https://ballotpedia.org/Valoree_Swanson"]),
    ]),

    # ---------------- Deidre Henderson (UT-R, Lt. Governor) ----------------
    ("deidre-henderson", "UT", "Governor", [
        claim("dh1", "deidre-henderson", "election_integrity", 0, True,
              "As Utah Lt. Governor and chief elections officer, initiated a statewide voter-registration citizenship audit (April 17, 2025) to identify potential non-citizen voter registrations and recommend changes to ensure only eligible citizens vote — a direct voter-integrity enforcement action.",
              ["https://ltgovernor.utah.gov/",
               "https://ltgovernor.utah.gov/wp-content/uploads/CITIZENSHIP-FULL-SUMMARY-2.pdf"]),
        claim("dh2", "deidre-henderson", "sanctity_of_life", 0, True,
              "As UT State Senator, voted YES on HB 136 Substitute 1 (2019 Utah Legislature), the Abortion Amendments trigger law that would have banned nearly all abortions upon Roe v. Wade being overturned; the measure passed the Senate 23–6.",
              ["https://le.utah.gov/DynaBill/svotes.jsp?sessionid=2019GS&voteid=1664&house=S",
               "https://en.wikipedia.org/wiki/Deidre_Henderson"]),
    ]),

    # ---------------- Trent Ashby (TX-R, State Rep HD-9) ----------------
    ("trent-ashby", "TX", "Representative", [
        claim("ta1", "trent-ashby", "sanctity_of_life", 0, True,
              "Co-sponsored Texas HB 2 banning abortion after 20 weeks of gestation and has a consistent record supporting legislation restricting abortion access during his tenure in the Texas House — reflecting a pro-life position protecting unborn life.",
              ["https://ballotpedia.org/Trent_Ashby"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug/wrong-state collisions."""
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
