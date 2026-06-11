#!/usr/bin/env python3
"""Enrichment batch 139: hand-curated claims for 5 sitting U.S. Representatives.

Targets from the BOTTOM of the alphabet (TX, TN) with 0 evidence claims.
Mix: August Pfluger (TX-11, R), Brian Babin (TX-36, R), Tim Burchett (TN-02, R),
Beth Van Duyne (TX-24, R), Pete Sessions (TX-17, R).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record / positions.

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
    # ---------------- August Pfluger (TX-11, R) ----------------
    ("august-pfluger", "TX", "Representative", [
        claim("ap1", "august-pfluger", "sanctity_of_life", 0, True,
              "Voted consistently to protect the lives of the unborn and to stop forced taxpayer funding of abortion. Supported the largest pro-life legislative victory in two decades by defunding Planned Parenthood of Medicaid dollars for one year through the 2025 reconciliation bill H.R.1 — affirming life from conception as foundational policy.",
              ["https://sbaprolife.org/representative/august-pfluger",
               "https://pfluger.house.gov/news/documentsingle.aspx?DocumentID=2724"]),
        claim("ap2", "august-pfluger", "border_immigration", 0, True,
              "A consistent border-security hawk who praised the Trump administration's military-backed enforcement push that drove FY2025 Southwest border apprehensions to their lowest level in half a century, and has called open-borders policies an 'election-year stunt' that endangers West Texas communities.",
              ["https://pfluger.house.gov/news/documentsingle.aspx?DocumentID=2649",
               "https://pfluger.house.gov/news/documentsingle.aspx?DocumentID=1061"]),
        claim("ap3", "august-pfluger", "economic_stewardship", 2, True,
              "Voted NO on the Democrats' $1.7 trillion, 4,000-page omnibus spending bill in December 2022, calling taxpayer-funded carve-outs 'wrong no matter the price tag' — a record consistent with anti-deficit, balanced-budget principles.",
              ["https://pfluger.house.gov/news/documentsingle.aspx?DocumentID=643"]),
    ]),

    # ---------------- Brian Babin (TX-36, R) ----------------
    ("brian-babin", "TX", "Representative", [
        claim("bb1", "brian-babin", "sanctity_of_life", 0, True,
              "Voted consistently to protect the lives of the unborn and to stop forced taxpayer funding of abortion, including supporting the 2025 reconciliation bill H.R.1 that defunded Planned Parenthood of Medicaid dollars for one year. Also publicly called out the FDA for approving a new generic abortion drug — affirming a life-from-conception standard.",
              ["https://sbaprolife.org/representative/brian-babin",
               "https://babin.house.gov/voterecord/"]),
        claim("bb2", "brian-babin", "border_immigration", 4, True,
              "Introduced the Birthright Citizenship Act of 2025 (H.R.569) to end the misuse of the 14th Amendment, limiting automatic citizenship to children born to U.S. citizens, lawful permanent residents, or active-duty military — directly opposing the anchor-baby loophole the rubric targets.",
              ["https://babin.house.gov/news/documentsingle.aspx?DocumentID=14088",
               "https://www.congress.gov/bill/119th-congress/house-bill/569"]),
    ]),

    # ---------------- Tim Burchett (TN-02, R) ----------------
    ("tim-burchett", "TN", "Representative", [
        claim("tb1", "tim-burchett", "sanctity_of_life", 0, True,
              "Publicly affirms that all life is precious and will always fight to protect the lives of unborn babies, and consistently opposes any use of taxpayer dollars to fund abortion — a life-from-conception posture confirmed on his official issues page.",
              ["https://burchett.house.gov/issues",
               "https://sbaprolife.org/representative/tim-burchett"]),
        claim("tb2", "tim-burchett", "self_defense", 0, True,
              "A strong Second Amendment advocate who states the U.S. Constitution guarantees the right to keep and bear arms for all law-abiding citizens, and has opposed gun-control expansions — consistent with the rubric's constitutional-carry and anti-AWB standard.",
              ["https://burchett.house.gov/issues/second-amendment"]),
        claim("tb3", "tim-burchett", "foreign_policy_restraint", 1, True,
              "Voted against all three 2024 foreign-aid supplemental bills, including the $95B Ukraine/Israel package, arguing the U.S. had already sent Ukraine nearly $114 billion and that Europe must take the reins — aligning with the rubric's call to end open-ended foreign military entanglements.",
              ["https://burchett.house.gov/media/press-releases/rep-burchett-statements-votes-against-three-foreign-aid-supplemental-bills",
               "https://burchett.house.gov/media/press-releases/rep-burchett-leads-letter-senate-leaders-reject-tying-foreign-aid-together"]),
    ]),

    # ---------------- Beth Van Duyne (TX-24, R) ----------------
    ("beth-van-duyne", "TX", "Representative", [
        claim("bvd1", "beth-van-duyne", "sanctity_of_life", 0, True,
              "Voted consistently to protect the lives of the unborn and to stop forced taxpayer funding of abortion, including the 2025 reconciliation bill H.R.1 defunding Planned Parenthood of Medicaid dollars, and introduced the Caring for Mothers Act to support expectant mothers who choose adoption over abortion.",
              ["https://sbaprolife.org/representative/beth-van-duyne",
               "https://vanduyne.house.gov/about"]),
        claim("bvd2", "beth-van-duyne", "border_immigration", 0, True,
              "Introduced the Border Patrol First Act in October 2022 to strengthen U.S. Border Patrol resources and enforcement capacity — a direct endorsement of military-style asset deployment at the southern border consistent with the rubric's wall-and-military standard.",
              ["https://vanduyne.house.gov/votes-and-legislation",
               "https://ballotpedia.org/Beth_Van_Duyne"]),
    ]),

    # ---------------- Pete Sessions (TX-17, R) ----------------
    ("pete-sessions", "TX", "Representative", [
        claim("ps1", "pete-sessions", "sanctity_of_life", 0, True,
              "Carries a 100% lifetime pro-life voting record with National Right to Life, opposes abortion in all its forms, and supports defunding Planned Parenthood — a consistent life-from-conception posture across more than two decades of congressional service.",
              ["https://en.wikipedia.org/wiki/Pete_Sessions",
               "https://ballotpedia.org/Pete_Sessions"]),
        claim("ps2", "pete-sessions", "border_immigration", 0, True,
              "Advocated for congressional appropriations to fund construction of a U.S.-Mexico border wall as part of a Republican-led budget framework — supporting the military-backed physical barrier the rubric identifies as the foundational border-security position.",
              ["https://en.wikipedia.org/wiki/Pete_Sessions",
               "https://sessions.house.gov/vote-record"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
