#!/usr/bin/env python3
"""Enrichment batch 191: hand-curated claims for 5 sitting U.S. Representatives.

Targets sitting federal House members from the bottom of the alphabet with
0 evidence claims (PA and OR delegation — all Democrat).

Candidates: Chris Deluzio (PA-D), Brendan Boyle (PA-D), Val Hoyle (OR-D),
Suzanne Bonamici (OR-D), Maxine Dexter (OR-D).
Each claim cites >=1 reliable source and reflects 2024-2026 positions/record.

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
    # ---------------- Chris Deluzio (PA-17, D) ----------------
    ("chris-deluzio", "PA", "Representative", [
        claim("cd1", "chris-deluzio", "self_defense", 1, False,
              "A vocal gun-control advocate: co-introduced legislation to ban firearms at polling places ahead of the 2024 election and celebrated $8.5 million in federal funding for extreme-risk protection order (red-flag) programs under the Bipartisan Safer Communities Act — directly opposing constitutional-carry and anti-red-flag positions.",
              ["https://deluzio.house.gov/media/press-releases/ahead-2024-election-pa-congressman-chris-deluzio-and-colleagues-introduce-bill-protect-voters-and-election-workers-from-gun-related-intimidation-at-americas-polls",
               "https://deluzio.house.gov/media/press-releases/deluzio-celebrates-85-million-gun-violence-prevention-and-crisis-intervention",
               "https://giffords.org/candidates/chris-deluzio/"]),
        claim("cd2", "chris-deluzio", "sanctity_of_life", 0, False,
              "Identifies as pro-choice and calls abortion access 'a basic human right,' opposing any government restriction on reproductive decisions after Dobbs — rejecting personhood from conception.",
              ["https://ballotpedia.org/Chris_Deluzio",
               "https://en.wikipedia.org/wiki/Chris_Deluzio"]),
    ]),

    # ---------------- Brendan Boyle (PA-2, D) ----------------
    ("brendan-boyle", "PA", "Representative", [
        claim("bb1", "brendan-boyle", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act (2021) to codify unlimited federal abortion access up to viability; SBA Pro-Life America assigns him a lifetime score of 0% on pro-life votes — a full reversal from his Notre Dame Democrats-for-Life presidency and 2008 pro-life questionnaire answers.",
              ["https://sbaprolife.org/representative/brendan-boyle",
               "https://en.wikipedia.org/wiki/Brendan_Boyle"]),
        claim("bb2", "brendan-boyle", "border_immigration", 1, True,
              "One of only 48 House Democrats to cross party lines and vote YES on the Laken Riley Act (H.R. 29, Jan. 7, 2025), which mandates detention of undocumented immigrants charged with theft, burglary, or violent crimes — a step toward mandatory deportation enforcement.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://en.wikipedia.org/wiki/Brendan_Boyle"]),
    ]),

    # ---------------- Val Hoyle (OR-4, D) ----------------
    ("val-hoyle", "OR", "Representative", [
        claim("vh1", "val-hoyle", "sanctity_of_life", 0, False,
              "Strongly pro-choice: pledges on her official congressional website to 'restore the national protections of Roe v. Wade' and to oppose any national ban on abortion, contraceptives, or IVF — rejecting personhood from conception.",
              ["https://hoyle.house.gov/issues/reproductive-rights",
               "https://oregoncapitalchronicle.com/2024/09/04/u-s-rep-hoyle-hammers-republican-challenger-despain-on-abortion-stance/"]),
        claim("vh2", "val-hoyle", "self_defense", 1, False,
              "A gun-safety advocate and member of the Congressional Progressive Caucus who ran on a platform of 'common-sense gun safety' legislation, supporting universal background checks and stricter firearm restrictions — opposing constitutional-carry and the rubric's anti-red-flag standard.",
              ["https://ballotpedia.org/Val_Hoyle",
               "https://www.valhoyle.com/issues/"]),
    ]),

    # ---------------- Suzanne Bonamici (OR-1, D) ----------------
    ("suzanne-bonamici", "OR", "Representative", [
        claim("sb1", "suzanne-bonamici", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act in July 2022 and again in December 2022 (final passage), codifying federal recognition of same-sex marriage; issued a statement that 'everyone should be able to marry who they love' — rejecting the one-man-one-woman definition.",
              ["https://bonamici.house.gov/media/press-releases/bonamici-helps-house-pass-respect-marriage-act-bill-heads-presidents-desk",
               "https://www.govtrack.us/congress/bills/117/hr8404"]),
        claim("sb2", "suzanne-bonamici", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act of 2023 (H.R. 12) to federally protect abortion access; SBA Pro-Life America gives her a 0% lifetime pro-life score, and she voted against the Born-Alive Abortion Survivors Protection Act.",
              ["https://sbaprolife.org/representative/suzanne-bonamici",
               "https://www.congress.gov/bill/118th-congress/house-bill/12"]),
    ]),

    # ---------------- Maxine Dexter (OR-3, D) ----------------
    ("maxine-dexter", "OR", "Representative", [
        claim("md1", "maxine-dexter", "sanctity_of_life", 0, False,
              "Led the expansion of abortion rights in the Oregon state legislature before coming to Congress; has set preserving and expanding abortion access as a top congressional priority — rejecting personhood from conception.",
              ["https://ballotpedia.org/Maxine_Dexter",
               "https://oregoncapitalchronicle.com/2025/01/02/u-s-rep-elect-dexter-sets-long-term-goals-for-congress-on-health-care-environment/"]),
        claim("md2", "maxine-dexter", "self_defense", 1, False,
              "Backed stricter gun laws in the Oregon House, including safe gun storage requirements and a ban on undetectable ghost guns; supports enacting federal gun control as a U.S. Representative.",
              ["https://ballotpedia.org/Maxine_Dexter",
               "https://dexter.house.gov/about"]),
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
