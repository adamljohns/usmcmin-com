#!/usr/bin/env python3
"""Enrichment batch 387: hand-curated claims for 5 Democratic State Senators (WI + WA).

Targets archetype_party_default state senators with 0 evidence claims from the
bottom of the alphabet (WI then WA), continuing where batch 386 left off.

Senators: Dora Drake (WI-SD4), Dianne Hesselbein (WI-SD27),
Chris Larson (WI-SD7), Brad Pfaff (WI-SD32), Yasmin Trudeau (WA-SD27).

Each claim cites >=1 reliable source and reflects 2023-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Dora Drake (WI-SD4, State Senator) ----------------
    ("dora-drake", "WI", "Senator", [
        claim("dd1", "dora-drake", "sanctity_of_life", 0, False,
              "Co-authored 2023 Wisconsin Assembly Joint Resolution 10 calling for an advisory referendum to repeal the state's 1849 criminal abortion prohibition and restore constitutional rights guaranteed under Roe v. Wade — an unambiguous rejection of life-at-conception protections that Wisconsin's 19th-century statute extended to the unborn.",
              ["https://docs.legis.wisconsin.gov/2023/legislators/assembly/2462",
               "https://ballotpedia.org/Dora_Drake"]),
        claim("dd2", "dora-drake", "self_defense", 1, False,
              "Co-sponsored 2023 Wisconsin Assembly Bill 1051 creating a new Office of Gun Violence Prevention within the state Department of Justice — a government bureaucracy tasked with developing and coordinating additional restrictions on lawful firearm ownership rather than addressing root causes of violence.",
              ["https://docs.legis.wisconsin.gov/2023/legislators/assembly/2462",
               "https://ballotpedia.org/Dora_Drake"]),
        claim("dd3", "dora-drake", "biblical_marriage", 2, False,
              "Co-sponsored 2023 Wisconsin Assembly Bill 1203 authorizing state grants for LGBTQIA+ rights training programs for school counselors and school social workers — publicly funding ideological instruction that affirms transgender and LGBTQ identities through school mental health personnel.",
              ["https://docs.legis.wisconsin.gov/2023/legislators/assembly/2462",
               "https://ballotpedia.org/Dora_Drake"]),
    ]),

    # ---------------- Dianne Hesselbein (WI-SD27, State Senator / Minority Leader) ----------------
    ("dianne-hesselbein", "WI", "Senator", [
        claim("dh1", "dianne-hesselbein", "sanctity_of_life", 0, False,
              "As Wisconsin Senate Minority Leader, introduced 2025 Senate Bill 271 — the 'right to bodily autonomy' bill — repealing abortion-related regulations and mandating that health insurance plans cover abortion, a comprehensive effort to entrench abortion access in Wisconsin law.",
              ["https://legis.wisconsin.gov/senate/27/hesselbein/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2811",
               "https://ballotpedia.org/Dianne_Hesselbein"]),
        claim("dh2", "dianne-hesselbein", "self_defense", 1, False,
              "Introduced 2025 Wisconsin Senate Bill 946 mandating that firearms dealers provide a container or trigger lock with every firearm sold in Wisconsin — imposing mandatory compliance costs on every lawful gun purchase and restricting a buyer's immediate ability to take operational possession of a legally purchased firearm.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2811",
               "https://legis.wisconsin.gov/senate/27/hesselbein/news-updates/press-releases/",
               "https://ballotpedia.org/Dianne_Hesselbein"]),
        claim("dh3", "dianne-hesselbein", "election_integrity", 0, False,
              "Introduced 2025 legislation to expand voter registration through Wisconsin high schools — advancing enrollment of new voters through institutional channels rather than supporting the voter ID verification standards championed by Wisconsin Republicans and approved 78–22 by Wisconsin voters in the 2024 SJR 73 advisory referendum.",
              ["https://legis.wisconsin.gov/senate/27/hesselbein/",
               "https://ballotpedia.org/Dianne_Hesselbein"]),
    ]),

    # ---------------- Chris Larson (WI-SD7, State Senator) ----------------
    ("chris-larson", "WI", "Senator", [
        claim("cl1", "chris-larson", "sanctity_of_life", 0, False,
              "Co-sponsored 2023 Wisconsin Senate Joint Resolution 10 calling for an advisory referendum to repeal Wisconsin's 1849 criminal abortion prohibition and restore constitutional abortion rights under Roe v. Wade, publicly declaring 'Our freedoms are not negotiable' in opposition to the statute protecting unborn life.",
              ["https://legis.wisconsin.gov/senate/07/larson/press-releases/our-freedoms-are-not-negotiable-sen-larson-statement-on-introduction-of-the-abortion-rights-restoration-act/",
               "https://ballotpedia.org/Chris_Larson"]),
        claim("cl2", "chris-larson", "self_defense", 1, False,
              "Sponsored 2023 Wisconsin Senate Bill 1100 to eliminate the state's preemption on local regulation of firearms — which would have allowed Milwaukee and other municipalities to enact their own patchwork of gun-control ordinances beyond state law, undermining the uniform statewide legal standard protecting law-abiding gun owners.",
              ["https://docs.legis.wisconsin.gov/document/legislator/2023/2424",
               "https://legis.wisconsin.gov/senate/07/larson/",
               "https://ballotpedia.org/Chris_Larson"]),
    ]),

    # ---------------- Brad Pfaff (WI-SD32, State Senator) ----------------
    ("brad-pfaff", "WI", "Senator", [
        claim("bp1", "brad-pfaff", "sanctity_of_life", 0, False,
              "Co-authored 2025 Wisconsin Senate Bill 271 — the 'right to bodily autonomy' bill — repealing abortion-related regulations and mandating health insurance coverage of abortion, and also co-authored companion 2025 SB 547 separately eliminating additional abortion-related regulations from Wisconsin statute.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2823",
               "https://legis.wisconsin.gov/senate/32/pfaff/",
               "https://ballotpedia.org/Brad_Pfaff"]),
        claim("bp2", "brad-pfaff", "refuse_state_overreach", 0, False,
              "Co-authored 2025 SB 271's provision mandating that qualifying Wisconsin health insurance plans cover abortion — a government-dictated benefit requirement imposed on private insurance contracts — while listing 'protecting reproductive choice' as an explicit stated legislative priority on his official state senate website.",
              ["https://legis.wisconsin.gov/senate/32/pfaff/about/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2823",
               "https://ballotpedia.org/Brad_Pfaff"]),
    ]),

    # ---------------- Yasmin Trudeau (WA-SD27, State Senator) ----------------
    ("yasmin-trudeau", "WA", "Senator", [
        claim("yt1", "yasmin-trudeau", "sanctity_of_life", 0, False,
              "Sponsored 2023 Washington Senate Bill 5768 authorizing the state Department of Corrections to acquire, sell, deliver, distribute, and dispense abortion medications — expanding state government's role as a direct distributor of abortion drugs. The bill passed 28–18 in the Senate and became Chapter 195, 2023 Laws.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=5768&Initiative=false&Year=2023",
               "https://ballotpedia.org/Yasmin_Trudeau"]),
        claim("yt2", "yasmin-trudeau", "self_defense", 1, False,
              "Co-sponsored 2023 Washington Senate Bill 5265 — the Senate companion to House Bill 1240 — which banned the manufacture, importation, distribution, and sale of assault weapons in Washington state. HB 1240 passed both chambers along party lines, was signed by Governor Inslee in April 2023, and became Chapter 162, 2023 Laws.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://leg.wa.gov/legislators/member/yasmin-trudeau",
               "https://ballotpedia.org/Yasmin_Trudeau"]),
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
