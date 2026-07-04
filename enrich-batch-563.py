#!/usr/bin/env python3
"""Enrichment batch 563: 5 WA State Representatives, 11 claims.

Targets archetype_party_default state legislators from Washington (WA) —
continuing bottom-of-alphabet after batch 562. All federal archetype_curated
slots are exhausted; this batch continues with WA state-level officials.

Candidates (all WA, D, 'State Representative'):
  My-Linh Thai          (WA-41, Bellevue)
  Monica Jurado Stonier (WA-49, Vancouver)
  Mia Gregerson         (WA-30, Federal Way)
  Melanie Morgan        (WA-29, Tacoma)
  Mary Fosse            (WA-38, Marysville)
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
    # -------- My-Linh Thai (WA-41, D, State Representative) --------
    ("my-linh-thai", "WA", "State Representative", [
        claim("mlt1", "my-linh-thai", "sanctity_of_life", 0, False,
              "A co-sponsor of HB 2182 (2025-26), which expands state distribution of mifepristone by authorizing licensed health providers statewide to obtain abortion medications from Washington's Department of Corrections — circumventing potential federal supply restrictions. The bill also broadens prescriber eligibility for abortion medications and was introduced at the request of the Women's Commission.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=2182&Year=2025&Initiative=false",
               "https://legiscan.com/WA/drafts/HB2182/2025",
               "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/House%20Bills/2182.pdf"]),
        claim("mlt2", "my-linh-thai", "self_defense", 1, False,
              "Voted in favor of HB 1163 (2025), requiring Washington residents to obtain a government-issued permit before purchasing any firearm, with mandatory live-fire training and creation of a state registry of firearm purchasers. The NRA described the bill as 'an illegal government registry of firearm owners.' Signed by Gov. Ferguson; effective May 1, 2027.",
              ["https://legiscan.com/WA/rollcall/HB1163/id/1502231",
               "https://app.leg.wa.gov/billsummary?BillNumber=1163&Year=2025",
               "https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate"]),
    ]),

    # -------- Monica Jurado Stonier (WA-49, D, State Representative) --------
    ("monica-jurado-stonier", "WA", "State Representative", [
        claim("mjs1", "monica-jurado-stonier", "family_child_sovereignty", 0, False,
              "The prime sponsor — and, as House Majority Floor Leader, the principal legislative driver — of HB 1296 (2025), the Democratic overhaul of Washington's citizen-passed Parents' Bill of Rights (Initiative 2081). The bill removed parental notification rights over children's gender-related medical decisions in schools and restricted parental access to student health records. It passed 59-39 on a strict party-line vote; signed by Gov. Ferguson on May 20, 2025.",
              ["https://legiscan.com/WA/sponsors/HB1296/2025",
               "https://housedemocrats.wa.gov/stonier/2025/05/27/new-law-strengthens-student-rights-and-parental-involvement-in-public-schools/",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/"]),
        claim("mjs2", "monica-jurado-stonier", "self_defense", 1, False,
              "Voted in favor of HB 1163 (2025), requiring Washington residents to obtain a government-issued permit before purchasing any firearm, mandating live-fire training and creating a state registry of purchasers — opposed by the NRA as 'an illegal government registry of firearm owners.' Signed by Gov. Ferguson; effective May 1, 2027.",
              ["https://legiscan.com/WA/rollcall/HB1163/id/1502231",
               "https://app.leg.wa.gov/billsummary?BillNumber=1163&Year=2025",
               "https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate"]),
    ]),

    # -------- Mia Gregerson (WA-30, D, State Representative) --------
    ("mia-gregerson", "WA", "State Representative", [
        claim("mg1", "mia-gregerson", "self_defense", 1, False,
              "A co-sponsor of HB 1163 (2025), requiring Washington residents to obtain a government-issued permit before purchasing any firearm, with mandatory live-fire training and creation of a state database of purchasers. The NRA described the bill as 'an illegal government registry of firearm owners.' Signed by Gov. Ferguson; effective May 1, 2027.",
              ["https://legiscan.com/WA/sponsors/HB1163/2025",
               "https://app.leg.wa.gov/billsummary?BillNumber=1163&Year=2025",
               "https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate"]),
        claim("mg2", "mia-gregerson", "sanctity_of_life", 0, False,
              "The primary sponsor of HJR 4201 in the 2023 Washington legislative session — a proposed constitutional amendment to enshrine 'reproductive freedom' (abortion and contraception access) as a fundamental right in the Washington State Constitution, making abortion rights irrevocable by future legislatures. Gregerson described expanding abortion rights as an 'emerging priority' for her caucus.",
              ["https://housedemocrats.wa.gov/gregerson/2023/01/17/legislative-update-emerging-priorities-this-session-reproductive-freedom-addressing-workforce-and-housing-shortages/",
               "https://app.leg.wa.gov/billsummary?BillNumber=4201&Chamber=House&Year=2023"]),
    ]),

    # -------- Melanie Morgan (WA-29, D, State Representative) --------
    ("melanie-morgan", "WA", "State Representative", [
        claim("mm1", "melanie-morgan", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates of Washington in the 2024 election cycle, an organization that explicitly requires endorsed candidates to support abortion access — placing her within the abortion-industry advocacy network.",
              ["https://ballotpedia.org/Melanie_Morgan",
               "https://progressivevotersguide.com/washington/2024/primary/melanie-morgan"]),
        claim("mm2", "melanie-morgan", "family_child_sovereignty", 0, False,
              "Voted in favor of HB 1296 (2025), the Democratic overhaul of Washington's citizen-passed Parents' Bill of Rights (Initiative 2081), removing parental notification rights over children's gender-related medical decisions in schools and restricting parental access to student health records. The bill passed 59-39 (all 98 House members voting) along a strict party line; signed by Gov. Ferguson May 20, 2025.",
              ["https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://legiscan.com/WA/rollcall/HB1296/id/1478198"]),
    ]),

    # -------- Mary Fosse (WA-38, D, State Representative) --------
    ("mary-fosse", "WA", "State Representative", [
        claim("mf1", "mary-fosse", "self_defense", 1, False,
              "A co-sponsor of HB 1163 (2025), requiring Washington residents to obtain a government-issued permit before purchasing any firearm, with mandatory live-fire training and creation of a state database of purchasers. The NRA described the bill as 'an illegal government registry of firearm owners.' Signed by Gov. Ferguson; effective May 1, 2027.",
              ["https://legiscan.com/WA/sponsors/HB1163/2025",
               "https://app.leg.wa.gov/billsummary?BillNumber=1163&Year=2025",
               "https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate"]),
        claim("mf2", "mary-fosse", "family_child_sovereignty", 0, False,
              "A co-sponsor of HB 1296 (2025), the Democratic overhaul of Washington's citizen-passed Parents' Bill of Rights (Initiative 2081), removing parental notification rights over children's gender-related medical decisions in schools and restricting parental access to student health records. The bill passed 59-39 along party lines; signed by Gov. Ferguson May 20, 2025.",
              ["https://legiscan.com/WA/sponsors/HB1296/2025",
               "https://app.leg.wa.gov/billsummary?BillNumber=1296&Year=2025",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/"]),
        claim("mf3", "mary-fosse", "sanctity_of_life", 0, False,
              "A co-sponsor of HB 1854 (2023-24 session), which authorized Washington's Department of Corrections to acquire, hold, and distribute mifepristone (abortion medication) to licensed health providers statewide — enabling the state to stockpile and supply abortion drugs after Governor Inslee directed DOC to purchase a three-year supply of mifepristone.",
              ["https://legiscan.com/WA/text/HB1854/id/2770293",
               "https://app.leg.wa.gov/billsummary?BillNumber=1854&Year=2023"]),
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
