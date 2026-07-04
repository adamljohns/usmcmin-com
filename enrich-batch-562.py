#!/usr/bin/env python3
"""Enrichment batch 562: 5 WA State Representatives, 11 claims.

Targets archetype_party_default state legislators from Washington (WA) —
continuing bottom-of-alphabet after batch 561. All federal archetype_curated
slots are exhausted; this batch continues with WA state-level officials.

Candidates (all WA, D, 'State Representative'):
  Sharlett Mena    (WA-29, Tacoma)
  Osman Salahuddin (WA-48, Bellevue)
  Nicole Macri     (WA-43, Seattle)
  Natasha Hill     (WA-03, Spokane)
  Shaun Scott      (WA-43-Pos2, Seattle)
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
    # -------- Sharlett Mena (WA-29, D, State Representative) --------
    ("sharlett-mena", "WA", "State Representative", [
        claim("sm1", "sharlett-mena", "sanctity_of_life", 4, False,
              "Prior to taking office, Mena served as a board member of the Planned Parenthood Votes Washington Political Action Committee — a board seat that requires active advocacy for abortion access and alignment with Planned Parenthood's legislative agenda, placing her squarely within the abortion-industry network.",
              ["https://ballotpedia.org/Sharlett_Mena",
               "https://housedemocrats.wa.gov/mena/biography/"]),
        claim("sm2", "sharlett-mena", "self_defense", 1, False,
              "A co-sponsor of HB 1163 (2025), which requires Washington residents to obtain a government-issued permit before purchasing any firearm, mandating a live-fire training requirement and creating a state registry of firearm purchasers. The NRA described the bill as 'an illegal government registry of firearm owners.' Signed by Gov. Ferguson; effective May 1, 2027.",
              ["https://legiscan.com/WA/sponsors/HB1163/2025",
               "https://app.leg.wa.gov/billsummary?BillNumber=1163&Year=2025",
               "https://www.nrahlf.org/articles/2025/4/18/nra-alerts-gun-owners-as-washington-state-senate-passes-permit-to-purchase-bill/"]),
    ]),

    # -------- Osman Salahuddin (WA-48, D, State Representative) --------
    ("osman-salahuddin", "WA", "State Representative", [
        claim("os1", "osman-salahuddin", "sanctity_of_life", 4, False,
              "Received an endorsement from Planned Parenthood Alliance Advocates of Washington during his 2024 campaign, an organization that explicitly requires endorsed candidates to affirm support for abortion access — placing him within the abortion-industry network.",
              ["https://ballotpedia.org/Osman_Salahuddin"]),
        claim("os2", "osman-salahuddin", "self_defense", 1, False,
              "A co-sponsor of HB 1163 (2025), requiring a government-issued permit before purchasing any firearm, with mandatory live-fire training and a state database of purchasers. Also received a 2024 campaign endorsement from the Alliance for Gun Responsibility Victory Fund, a leading gun-control advocacy group. The NRA opposed the permit bill as 'an illegal government registry of firearm owners.'",
              ["https://legiscan.com/WA/sponsors/HB1163/2025",
               "https://app.leg.wa.gov/billsummary?BillNumber=1163&Year=2025",
               "https://ballotpedia.org/Osman_Salahuddin"]),
        claim("os3", "osman-salahuddin", "family_child_sovereignty", 0, False,
              "A co-sponsor of HB 1296 (2025), the Democratic overhaul of Washington's citizen-passed Parents' Bill of Rights (Initiative 2081), removing parental notification rights over gender-related student medical decisions in schools and stripping parental access to certain student health records. The bill passed 59-39 along party lines; signed by Gov. Ferguson May 20, 2025.",
              ["https://legiscan.com/WA/sponsors/HB1296/2025",
               "https://app.leg.wa.gov/billsummary?Year=2025&BillNumber=1296",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/"]),
    ]),

    # -------- Nicole Macri (WA-43, D, State Representative) --------
    ("nicole-macri", "WA", "State Representative", [
        claim("nm1", "nicole-macri", "biblical_marriage", 2, False,
              "Co-chairs the Washington State Legislative LGBTQ Caucus and serves as a legislative representative to the Washington State LGBTQ Commission — a body she helped create via sponsorship of SB 5356. Her stated 2023 legislative priorities include 'protecting transgender people' and she is a leading advocate for embedding LGBTQ ideology into public policy and law.",
              ["https://lgbtq.wa.gov/about-us/legislative-representatives",
               "https://housedemocrats.wa.gov/macri/2023/01/30/housing-reproductive-care-workforce-my-priorities-this-legislative-session/"]),
        claim("nm2", "nicole-macri", "sanctity_of_life", 0, False,
              "A co-sponsor of HB 1469 (2023), which shielded abortion providers and gender-affirming care practitioners from medical licensing board accountability for services rendered in Washington — including to out-of-state patients crossing state lines. The bill defines 'protected health care services' to include both abortion and gender-affirming treatment, and bars courts from issuing subpoenas tied to such services. Became Chapter 193, 2023 Laws; effective April 27, 2023.",
              ["https://legiscan.com/WA/bill/HB1469/2023",
               "https://wa-law.org/bill/2023-24/hb/1469/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1469&Initiative=false&Year=2023"]),
    ]),

    # -------- Natasha Hill (WA-03, D, State Representative) --------
    ("natasha-hill", "WA", "State Representative", [
        claim("nh1", "natasha-hill", "self_defense", 1, False,
              "A co-sponsor of HB 1163 (2025), requiring a government-issued permit before purchasing any firearm in Washington, with mandatory live-fire training and creation of a government database of firearm purchasers. The NRA characterized the bill as 'an illegal government registry of firearm owners.' Signed by Gov. Ferguson; effective May 1, 2027.",
              ["https://legiscan.com/WA/sponsors/HB1163/2025",
               "https://app.leg.wa.gov/billsummary?BillNumber=1163&Year=2025",
               "https://wa-law.org/bill/2025-26/hb/1163/1/"]),
        claim("nh2", "natasha-hill", "family_child_sovereignty", 0, False,
              "A co-sponsor of HB 1296 (2025), which overhauled Washington's citizen-passed Parents' Bill of Rights (Initiative 2081), removing parental notification rights over children's gender-related medical decisions in schools and restricting parental access to student health records. The bill passed 59-39 along party lines; signed May 20, 2025.",
              ["https://legiscan.com/WA/sponsors/HB1296/2025",
               "https://app.leg.wa.gov/billsummary?Year=2025&BillNumber=1296",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/"]),
    ]),

    # -------- Shaun Scott (WA-43-Pos2, D, State Representative) --------
    ("shaun-scott", "WA", "State Representative", [
        claim("ss1", "shaun-scott", "family_child_sovereignty", 0, False,
              "A co-sponsor of HB 1296 (2025), the Democratic rewrite of Washington's citizen-passed Parents' Bill of Rights (Initiative 2081), stripping parental notification rights over gender-related student medical decisions in schools. The bill passed 59-39 entirely on party lines; signed by Gov. Ferguson May 20, 2025.",
              ["https://legiscan.com/WA/sponsors/HB1296/2025",
               "https://app.leg.wa.gov/billsummary?Year=2025&BillNumber=1296",
               "https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/"]),
        claim("ss2", "shaun-scott", "economic_stewardship", 2, False,
              "The first socialist elected to the Washington State Legislature since 1912 and a member of the Democratic Socialists of America (DSA), Scott introduced the Well Washington Fund (Nov 2025) — a progressive payroll excise tax designed to expand state social programs in response to federal spending reductions under H.R. 1. His legislative agenda prioritizes growing government programs and redistributive taxation rather than balanced-budget fiscal restraint.",
              ["https://housedemocrats.wa.gov/blog/2025/12/04/rep-shaun-scott-unveils-well-washington-fund-a-progressive-payroll-excise-tax-to-protect-washington-families-from-trumps-austerity-budget/",
               "https://en.wikipedia.org/wiki/Shaun_Scott_(politician)"]),
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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
