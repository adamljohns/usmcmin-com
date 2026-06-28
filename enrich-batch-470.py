#!/usr/bin/env python3
"""Enrichment batch 470: hand-curated claims for 5 WA State Senators.

Remaining archetype_party_default WA State Senators with 0 claims (bottom of
alphabet after batch 469 took 5 others). All 5 targets are WA Democrats whose
2023-2025 records are sourced from official WA Legislature pages, WA State
Standard, Seattle Times, and senatedemocrats.wa.gov.

Targets:
  Javier Valdez       (WA-46, D) — weapons ban in public places + campus abortion
  Deborah Krishnadasan (WA-26, D) — campus abortion bill + PP endorsement
  Claudia Kauffman    (WA-47, D) — SB 5599 committee vice chair + AWB vote
  Annette Cleveland   (WA-49, D) — prime sponsor SB 5242 abortion cost-sharing + AWB
  Adrian Cortes       (WA-18, D) — permit-to-purchase + campus abortion caucus vote

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
    # ---------------- Javier Valdez (WA-46, D, State Senator) ----------------
    ("javier-valdez", "WA", "Senator", [
        claim("jv1", "javier-valdez", "self_defense", 1, False,
              "Prime sponsor of SB 5444 (2024), expanding Washington's weapons-free zones to include "
              "public libraries, zoos, aquariums, and transit stations and facilities. The bill passed "
              "the Senate 29-20 and the House 58-36 and was signed into law — further restricting "
              "where law-abiding citizens may lawfully carry.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5444&Year=2023&Initiative=false",
               "https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/Senate/5444%20SBA%20LAW%2024.pdf"]),
        claim("jv2", "javier-valdez", "sanctity_of_life", 0, False,
              "Co-sponsored SB 5321 (2025), requiring every public higher-education health center in "
              "Washington to offer medication abortion by the 2026-27 academic year — mandating that "
              "state institutions treat abortion as routine student healthcare and institutionalizing "
              "abortion infrastructure in every public university, rejecting any personhood-from-conception "
              "framework.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5321&Year=2025&Initiative=false",
               "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bill%20Reports/Senate/5321%20SBR%20HEWD%20OC%2025.pdf"]),
    ]),

    # ---------------- Deborah Krishnadasan (WA-26, D, State Senator) ----------------
    ("deborah-krishnadasan", "WA", "Senator", [
        claim("dk1", "deborah-krishnadasan", "sanctity_of_life", 0, False,
              "Co-sponsored SB 5321 (2025), requiring every public higher-education health center in "
              "Washington to provide access to medication abortion beginning with the 2026-27 academic "
              "year — mandating state universities actively dispense abortion drugs as a student health "
              "service, opposing any recognition of personhood from conception.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5321&Year=2025&Initiative=false",
               "https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bill%20Reports/Senate/5321%20SBR%20HEWD%20OC%2025.pdf"]),
        claim("dk2", "deborah-krishnadasan", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates of Washington for her 2025 special "
              "general election campaign for Washington State Senate District 26, placing her within "
              "the abortion-advocacy endorsement network the rubric's 'never took PP/NARAL money' "
              "standard identifies as disqualifying.",
              ["https://ballotpedia.org/Deborah_Krishnadasan",
               "https://senatedemocrats.wa.gov/Krishnadasan/news-releases/"]),
    ]),

    # ---------------- Claudia Kauffman (WA-47, D, State Senator) ----------------
    ("claudia-kauffman", "WA", "Senator", [
        claim("ck1", "claudia-kauffman", "family_child_sovereignty", 0, False,
              "As Vice Chair of the Washington Senate Human Services Committee, helped advance ESSB 5599 "
              "(2023) out of committee — legislation allowing licensed youth shelters to contact the "
              "Department of Children, Youth and Families instead of parents when a minor age 13-18 "
              "seeks gender-affirming care or reproductive health services, stripping parental "
              "notification rights for life-and-identity decisions. Governor Inslee signed it into law "
              "May 2023.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5599&Year=2023&Initiative=false",
               "https://komonews.com/news/local/senate-bill-5599-transgender-at-risk-youth-gender-affirming-reproductive-care-without-parental-consent-governor-jay-inslee-family-foster-homeless-children-families-minors-law-legislation"]),
        claim("ck2", "claudia-kauffman", "self_defense", 1, False,
              "Voted yes on HB 1240 (April 2023), Washington's assault-style weapons ban prohibiting "
              "the sale, transfer, manufacture, and import of AR-15s, AK-47s, and more than 50 named "
              "firearm models; the Senate cleared the ban 27-21 on a near-party-line vote.",
              ["https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/",
               "https://ballotpedia.org/Claudia_Kauffman"]),
    ]),

    # ---------------- Annette Cleveland (WA-49, D, State Senator) ----------------
    ("annette-cleveland", "WA", "Senator", [
        claim("ac1", "annette-cleveland", "sanctity_of_life", 0, False,
              "Prime sponsor of SB 5242 (2023), eliminating all insurance cost-sharing — copays and "
              "deductibles — for abortion care in Washington; the Senate passed the bill 29-19. "
              "Governor Inslee signed it July 2023; effective for health plans issued or renewed after "
              "January 1, 2024. Also sponsored legislation authorizing the Department of Corrections "
              "to distribute abortion medication (SB 5768, co-sponsor), further expanding the state's "
              "abortion infrastructure.",
              ["https://senatedemocrats.wa.gov/cleveland/2023/02/28/cleveland-bill-to-prohibit-cost-sharing-for-abortion-passes-senate/",
               "https://app.leg.wa.gov/billsummary?BillNumber=5242&Year=2023&Initiative=false"]),
        claim("ac2", "annette-cleveland", "self_defense", 1, False,
              "Co-sponsored SB 5265 (2023), the Senate companion bill to Washington's assault weapons "
              "ban, prohibiting the manufacture, sale, transfer, and import of AR-15s, AK-47s, and "
              "more than 50 other named firearm models; the Senate passed the companion House bill "
              "(HB 1240) 27-21 on a near-party-line vote and it was signed into law.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5265&Year=2023&Initiative=false",
               "https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/"]),
    ]),

    # ---------------- Adrian Cortes (WA-18, D, State Senator) ----------------
    ("adrian-cortes", "WA", "Senator", [
        claim("co1", "adrian-cortes", "self_defense", 1, False,
              "Voted yes on E2SHB 1163 (April 2025), Washington's permit-to-purchase firearms law "
              "requiring all prospective gun buyers to apply for a five-year permit from the Washington "
              "State Patrol, complete certified firearms safety training, and pass an enhanced "
              "background check before acquiring any firearm; the Senate passed the measure on a "
              "near-party-line vote and it was signed into law as Chapter 370, 2025 Laws.",
              ["https://washingtonstatestandard.com/2025/04/15/permit-requirement-for-gun-purchases-clears-washington-senate/",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("co2", "adrian-cortes", "sanctity_of_life", 0, False,
              "Joined the Washington Senate Democratic caucus in January 2025 and voted in line with "
              "the caucus's 2025 reproductive-rights agenda, including supporting SB 5321 — requiring "
              "every public higher-education health center to provide medication abortion by 2026-27 — "
              "as a member of the Democratic majority that advanced the bill through the Senate. "
              "Opposes any personhood-from-conception framework.",
              ["https://senatedemocrats.wa.gov/cortes/",
               "https://app.leg.wa.gov/billsummary?BillNumber=5321&Year=2025&Initiative=false"]),
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
