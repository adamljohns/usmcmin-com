#!/usr/bin/env python3
"""Enrichment batch 471: hand-curated claims for 5 WA State Representatives.

Remaining archetype_party_default WA State Representatives with 0 claims (top 5
reverse-alpha from bucket of 76 after batch 470 exhausted WA State Senators).
All 5 targets are WA Democrats whose 2023-2025 records are sourced from official
WA Legislature pages, Lynnwood Times, Spokesman-Review, and housedemocrats.wa.gov.

Targets:
  Timm Ormsby      (WA-3,  D) — HB 1240 co-sponsor/vote + Abortion Access Project letter
  Strom Peterson   (WA-21, D) — HB 1240 primary sponsor + HB 1469 shield law vote
  Tarra Simmons    (WA-23, D) — HB 1240 co-sponsor + HB 1263 gender-affirming care
  Steve Tharinger  (WA-24, D) — HB 1163 permit-to-purchase + HB 1469 reproductive shield
  Steve Bergquist  (WA-11, D) — HB 1240 co-sponsor + Planned Parenthood endorsement

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
    # ---------------- Timm Ormsby (WA-3, D, State Representative) ----------------
    ("timm-ormsby", "WA", "Representative", [
        claim("to1", "timm-ormsby", "self_defense", 1, False,
              "Co-sponsored and voted for HB 1240 (April 2023), Washington's assault-style "
              "weapons ban prohibiting the manufacture, importation, distribution, and sale of "
              "AR-15s, AK-47s, and more than 50 named semi-automatic rifle models. The "
              "Spokesman-Review explicitly reported that Ormsby voted in favor on the 56-42 final "
              "House concurrence vote; Governor Inslee signed the ban into law on April 25, 2023.",
              ["https://www.spokesman.com/stories/2023/mar/08/state-house-passes-bills-to-ban-assault-weapons-an/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023&Initiative=false"]),
        claim("to2", "timm-ormsby", "sanctity_of_life", 4, False,
              "Signed a letter to Washington state legislative leadership calling for restoration "
              "of funding for the Abortion Access Project, a program that channels state "
              "appropriations through Planned Parenthood's clinical operations. The letter was "
              "circulated in September 2025, placing Ormsby within the Planned "
              "Parenthood-aligned legislative network.",
              ["https://www.spokesman.com/stories/2025/sep/09/state-lawmakers-call-for-legislature-to-restore-fu/"]),
    ]),

    # ---------------- Strom Peterson (WA-21, D, State Representative) ----------------
    ("strom-peterson", "WA", "Representative", [
        claim("sp1", "strom-peterson", "self_defense", 1, False,
              "Primary sponsor of HB 1240 (2023), Washington's landmark assault-style weapons ban "
              "prohibiting the manufacture, importation, distribution, and sale of AR-15s, AK-47s, "
              "and more than 50 other named semi-automatic rifle models. Peterson carried the bill "
              "from introduction through its 55-42 House passage on March 8, 2023, Senate "
              "concurrence, and final signing by Governor Inslee on April 25, 2023 — making "
              "Washington the 10th state to ban assault-weapon sales.",
              ["https://lynnwoodtimes.com/2023/03/09/assault-weapons-230309/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023&Initiative=false"]),
        claim("sp2", "strom-peterson", "biblical_marriage", 2, False,
              "Voted for HB 1469 (2023), Washington's Reproductive and Gender-Affirming Care "
              "Shield Law, which explicitly protects individuals and providers involved in "
              "gender-affirming care from out-of-state civil or criminal liability and prohibits "
              "Washington law enforcement from assisting such prosecutions. The House passed the "
              "measure 56-42 on a near-party-line vote; Governor Inslee signed it on April 27, "
              "2023. The law institutionalizes gender-affirming treatment as a protected medical "
              "category under state law.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1469&Year=2023&Initiative=false",
               "https://www.axios.com/2023/04/27/abortion-shield-law-washington"]),
    ]),

    # ---------------- Tarra Simmons (WA-23, D, State Representative) ----------------
    ("tarra-simmons", "WA", "Representative", [
        claim("ts1", "tarra-simmons", "self_defense", 1, False,
              "Co-sponsored HB 1240 (2023), Washington's assault-style weapons ban prohibiting the "
              "manufacture, importation, distribution, and sale of AR-15s, AK-47s, and more than "
              "50 named semi-automatic rifle models; the House passed the bill 55-42, and it was "
              "signed into law on April 25, 2023.",
              ["https://wa-law.org/bill/2023-24/hb/1240/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023&Initiative=false"]),
        claim("ts2", "tarra-simmons", "biblical_marriage", 2, False,
              "Supported HB 1263 (2023), the Keep Our Care Act, which prohibits hospital mergers "
              "or acquisitions that would reduce patient access to services including "
              "gender-affirming care; the bill prevents Washington hospital consolidations from "
              "eliminating transgender care services as a condition of deal approval. Simmons "
              "highlighted the bill in her February 2023 district legislative update as a key "
              "priority for reproductive and gender-affirming care access.",
              ["https://housedemocrats.wa.gov/simmons/2023/02/09/23rd-district-legislative-news-protecting-reproductive-care-rental-stability-and-derelict-vessel-appeals/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1263&Year=2023&Initiative=false"]),
    ]),

    # ---------------- Steve Tharinger (WA-24, D, State Representative) ----------------
    ("steve-tharinger", "WA", "Representative", [
        claim("st1", "steve-tharinger", "self_defense", 1, False,
              "Co-sponsored HB 1163 (2025), Washington's permit-to-purchase firearms law requiring "
              "all prospective gun buyers to apply for a five-year permit from the Washington State "
              "Patrol, complete certified firearms safety training, and pass an enhanced background "
              "check before acquiring any firearm; enacted as Chapter 370, 2025 Laws, with an "
              "effective date of May 1, 2027.",
              ["https://app.leg.wa.gov/BillSummary/?BillNumber=1163&Year=2025",
               "https://sportsmensalliance.org/news/washington-legislature-passes-funds-permit-to-purchase-firearms/"]),
        claim("st2", "steve-tharinger", "sanctity_of_life", 0, False,
              "Among the original House sponsors of ESHB 1469 (2023), Washington's Reproductive "
              "and Gender-Affirming Care Shield Law, which prohibits Washington law enforcement "
              "from cooperating with out-of-state efforts to prosecute individuals for receiving "
              "or providing abortions lawful in Washington, and treats abortion as a protected "
              "health service; signed by Governor Inslee on April 27, 2023.",
              ["https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/Senate/1469-S.E%20SBR%20WM%20OC%2023.pdf",
               "https://app.leg.wa.gov/billsummary?BillNumber=1469&Year=2023&Initiative=false"]),
    ]),

    # ---------------- Steve Bergquist (WA-11, D, State Representative) ----------------
    ("steve-bergquist", "WA", "Representative", [
        claim("sb1", "steve-bergquist", "self_defense", 1, False,
              "Co-sponsored and voted for HB 1240 (2023), Washington's assault-style weapons ban "
              "prohibiting the manufacture, importation, distribution, and sale of AR-15s, AK-47s, "
              "and more than 50 named semi-automatic rifle models; the House passed the bill 55-42, "
              "and it was signed into law on April 25, 2023.",
              ["https://www.billtrack50.com/billdetail/1516004",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023&Initiative=false"]),
        claim("sb2", "steve-bergquist", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Alliance Advocates of Washington for his 2024 general "
              "election campaign, placing him within the abortion-industry endorsement network the "
              "rubric's 'never took PP/NARAL/EMILY money' standard identifies as disqualifying.",
              ["https://progressivevotersguide.com/washington/2024/general/steve-bergquist",
               "https://housedemocrats.wa.gov/bergquist/"]),
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
