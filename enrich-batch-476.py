#!/usr/bin/env python3
"""Enrichment batch 476: hand-curated claims for 5 Virginia House of Delegates members.

archetype_curated and evidence_federal federal-senator/representative buckets are now
fully enriched.  This batch pivots to evidence_state VA House of Delegates members with
0 claims — the next available bottom-of-alphabet (VA) tier.

Targets (all VA, bottom-of-alpha after WY/WV/WI/WA):
  Andrew Rice     (VA-R, HoD-98)  — Republican prosecutor, March 2026 special election
  Alex Askew      (VA-D, HoD-95)  — Democrat, Hampton Roads
  Alfonso Lopez   (VA-D, HoD-3)   — Democrat, Northern Virginia; immigration/environment
  Amy Laufer      (VA-D, HoD-55)  — Democrat, Fredericksburg area; reproductive-rights advocate
  Adele McClure   (VA-D, HoD-2)   — Democrat, Northern Virginia; gun-restriction sponsor

Key sourced events:
  • HJR 1 (Right to Reproductive Freedom constitutional amendment) passed VA House 51-48
    on 14 Jan 2025 on a strict party-line vote — all 51 Democrats yes, all Republicans no.
    (VPM, 2025-01-15)
  • HJR 9 (Marriage Equality constitutional amendment) passed VA House 58-35 on 14 Jan 2025
    — all 51 Democrats plus 7 Republicans in favor.  (VPM, 2025-01-15)

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the master
under GitHub's 50MB warning.
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
    # ---------------- Andrew Rice (VA-R, HoD-District 98) ----------------
    ("andrew-rice", "VA", "District 98", [
        claim("ar1", "andrew-rice", "sanctity_of_life", 0, True,
              "Rice ran and won as a Republican in Virginia Beach's solidly conservative 98th district (62.5% in the March 2026 special election). The Virginia House voted 51-48 on a strict party-line split on HJR 1 — the Right to Reproductive Freedom constitutional amendment — in January 2025, with all Republicans voting no. Rice's Republican candidacy and overwhelming margin in a Virginia Beach district places him firmly in the pro-life wing that unanimously opposed this abortion-expansion measure.",
              ["https://en.wikipedia.org/wiki/Andrew_Rice_(Virginia_politician)",
               "https://www.wavy.com/news/local-news/virginia-beach/republican-andrew-rice-wins-house-district-98-special-election-over-democrat-cheryl-smith/",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality"]),
        claim("ar2", "andrew-rice", "self_defense", 1, True,
              "A 15-year veteran prosecutor who campaigned on protecting neighborhoods, holding violent criminals accountable, and supporting law enforcement. Virginia Republicans in the 2024-2026 General Assembly sessions unanimously opposed Democratic gun-control bills expanding background checks, locking-device mandates, and firearm restrictions. Rice's Republican Party affiliation and strong margin in a pro-Second-Amendment Virginia Beach coastal district aligns with the rubric's opposition to new firearm purchase restrictions and registries.",
              ["https://ballotpedia.org/Andrew_Rice",
               "https://en.wikipedia.org/wiki/Andrew_Rice_(Virginia_politician)"]),
    ]),

    # ---------------- Alex Askew (VA-D, HoD-District 95) ----------------
    ("alex-askew", "VA", "District 95", [
        claim("aa1", "alex-askew", "sanctity_of_life", 0, False,
              "On 14 January 2025, the Virginia House of Delegates passed HJR 1 — the Right to Reproductive Freedom constitutional amendment — by 51-48 on a strict party-line vote. Askew, a Democrat representing Hampton Roads' District 95 who consistently votes with his caucus (per VPAP voting records), voted yes, endorsing a state-constitutional right to abortion through all stages of pregnancy and explicitly foreclosing any life-from-conception protection in Virginia law.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Alex_Askew",
               "https://www.vpap.org/legislators/250404-alex-askew/"]),
        claim("aa2", "alex-askew", "biblical_marriage", 1, False,
              "On 14 January 2025, the Virginia House passed HJR 9 — the Marriage Equality constitutional amendment — by 58-35, with all 51 House Democrats (including Askew) in favor. The amendment would permanently enshrine same-sex marriage in Virginia's constitution, directly rejecting the one-man-one-woman definition the rubric requires.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://www.vpap.org/legislators/250404-alex-askew/"]),
    ]),

    # ---------------- Alfonso Lopez (VA-D, HoD-District 3) ----------------
    ("alfonso-lopez", "VA", "District 3", [
        claim("al1", "alfonso-lopez", "border_immigration", 1, False,
              "Lopez spent years championing in-state college tuition for undocumented immigrants in Virginia, modeling his bills after the federal DREAM Act. In 2020 that legislation finally passed into law (HB 1547), granting taxpayer-subsidized tuition access to individuals residing in the country illegally. Lopez celebrated this as a marquee achievement. This posture — granting public benefits to unlawful residents — directly conflicts with the rubric's mandatory-deportation and enforcement standards.",
              ["https://en.wikipedia.org/wiki/Alfonso_H._Lopez",
               "https://ballotpedia.org/Alfonso_Lopez"]),
        claim("al2", "alfonso-lopez", "sanctity_of_life", 0, False,
              "As House Democratic Whip (2016-2022) and a long-serving progressive from Northern Virginia's Arlington/Alexandria suburbs, Lopez voted for HJR 1 — the Right to Reproductive Freedom constitutional amendment — when it passed the Virginia House 51-48 on a strict party-line vote on 14 January 2025. The amendment would entrench a sweeping constitutional right to abortion at all stages of pregnancy, rejecting any personhood-from-conception standard.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://en.wikipedia.org/wiki/Alfonso_H._Lopez"]),
    ]),

    # ---------------- Amy Laufer (VA-D, HoD-District 55) ----------------
    ("amy-laufer", "VA", "District 55", [
        claim("alauf1", "amy-laufer", "sanctity_of_life", 0, False,
              "Laufer is a vocal reproductive-rights advocate who publicly called on Governor Glenn Youngkin to enshrine contraception protections into Virginia law. On 14 January 2025, she voted for HJR 1 — the Right to Reproductive Freedom constitutional amendment — which passed 51-48 on a party-line vote with all 51 Democrats in favor. The amendment would create a state-constitutional right to abortion through all stages of pregnancy, precluding any life-from-conception recognition.",
              ["https://ballotpedia.org/Amy_Laufer",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality"]),
        claim("alauf2", "amy-laufer", "biblical_marriage", 1, False,
              "Laufer voted for HJR 9 — the Marriage Equality constitutional amendment — when it passed the Virginia House 58-35 on 14 January 2025, with all 51 House Democrats in favor. The amendment would write same-sex marriage permanently into Virginia's state constitution, directly rejecting the one-man-one-woman definition the rubric requires.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Amy_Laufer"]),
    ]),

    # ---------------- Adele McClure (VA-D, HoD-District 2) ----------------
    ("adele-mcclure", "VA", "District 2", [
        claim("amc1", "adele-mcclure", "self_defense", 1, False,
              "McClure sponsored legislation in the Virginia General Assembly to prohibit the purchase, possession, or transportation of firearms by persons convicted of assault and battery of a family or household member or intimate partner — a new class of misdemeanor-based firearm restriction. The bill was vetoed by Governor Youngkin. Her effort to expand the categories of persons stripped of gun rights and her stated aim of 'preventing gun violence' directly conflict with the rubric's opposition to new firearm purchase restrictions.",
              ["https://ballotpedia.org/Adele_McClure",
               "https://law.lis.virginia.gov/vacode/title18.2/chapter7/section18.2-308.1:8/",
               "https://www.vpap.org/legislators/437427-adele-mcclure/"]),
        claim("amc2", "adele-mcclure", "sanctity_of_life", 0, False,
              "McClure voted for HJR 1 — the Right to Reproductive Freedom constitutional amendment — when it passed the Virginia House 51-48 on 14 January 2025 on a strict party-line vote, with all 51 Democrats in favor. Her support for this measure, combined with her broader progressive legislative agenda, confirms her rejection of any life-from-conception standard in Virginia law.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://ballotpedia.org/Adele_McClure"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
