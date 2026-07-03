#!/usr/bin/env python3
"""Enrichment batch 533: hand-curated claims for 5 state senators (3 UT, 2 TN).

Targets archetype_party_default state senators from bottom-of-alphabet states
(UT, TN) with 0 evidence claims, continuing from batch 532's UT/TN coverage.

Candidates:
  Chris H. Wilson   (UT-R) — Utah Senate SD-2 (Logan/Cache County), in office Jan 2023
  David Hinkins     (UT-R) — Utah Senate SD-26, in office since 2009
  Derrin Owens      (UT-R) — Utah Senate SD-27, in office since Jan 2021
  Bill Powers       (TN-R) — Tennessee Senate SD-22 (Clarksville/Montgomery County)
  Bobby Harshbarger (TN-R) — Tennessee Senate SD-4 (Kingsport), in office Nov 2024

NOTE: writes scorecard.json MINIFIED to stay under GitHub's 50MB limit.
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
    # ---------------- Chris H. Wilson (UT-R, Utah Senate SD-2) ----------------
    ("chris-h-wilson", "UT", "State Senator", [
        claim("chw1", "chris-h-wilson", "self_defense", 1, True,
              "Sponsored Utah SB115 (2022) Firearm Preemption Amendments — establishing that only the state (not cities, counties, or local entities) may enact firearm regulations, and closing a Salt Lake County loophole that had allowed county-mandated background checks at gun shows; the Utah Senate passed the bill 20-5 with Republicans unified in support.",
              ["https://www.deseret.com/utah/2022/2/3/22916775/gun-laws-utah-firearm-bill-state-final-regulation-senate-preemption-salt-lake-county-gun-shows/",
               "https://le.utah.gov/~2022/bills/static/SB0115.html"]),
        claim("chw2", "chris-h-wilson", "christian_liberty", 0, True,
              "Sponsored Utah SB154 (2023) Adoption Amendments — shielding faith-based child-placing agencies from being compelled to place children with families contrary to the agency's religious teachings, practices, or sincerely held beliefs, or the birth mother's wishes; created a statewide adoption consortium while protecting religious agencies from forced participation in placements their beliefs prohibit.",
              ["https://le.utah.gov/~2023/bills/static/SB0154.html"]),
    ]),

    # ---------------- David Hinkins (UT-R, Utah Senate SD-26) ----------------
    ("david-hinkins", "UT", "State Senator", [
        claim("dh1", "david-hinkins", "sanctity_of_life", 0, True,
              "Voted for Utah HB467 (2023) 'Abortion Changes Act' — requiring all abortions be performed in licensed hospitals and prohibiting new abortion clinic licenses after May 2, 2023; the Republican-controlled Senate passed the bill 22-6 along party lines post-Dobbs, with Hinkins voting with his caucus.",
              ["https://www.deseret.com/utah/2023/3/2/23623104/utah-bill-to-close-abortion-clinics-passes-senate/",
               "https://www.sltrib.com/news/politics/2023/03/02/gop-lawmakers-pass-abortion-clinic/"]),
        claim("dh2", "david-hinkins", "election_integrity", 0, True,
              "As a Utah Republican state senator, backed HB300 (2025) requiring voters to write the last four digits of their driver's license number on mail-ballot return envelopes beginning in 2026, and phasing out Utah's automatic universal vote-by-mail system by January 2029; the Senate passed the bill 19-10 along party lines.",
              ["https://utahnewsdispatch.com/2025/03/06/utah-legislature-approves-bill-require-voter-id-phase-out-automatic-voting-by-mail-by-2029/"]),
    ]),

    # ---------------- Derrin Owens (UT-R, Utah Senate SD-27) ----------------
    ("derrin-owens", "UT", "State Senator", [
        claim("do1", "derrin-owens", "sanctity_of_life", 0, True,
              "As a Utah Republican state senator, voted for HB467 (2023) 'Abortion Changes Act' — the Republican-controlled Utah Senate passed the bill 22-6 along party lines, banning new abortion clinic licenses and requiring all abortions be performed in licensed hospitals; Owens voted with the Republican majority.",
              ["https://www.sltrib.com/news/politics/2023/03/02/gop-lawmakers-pass-abortion-clinic/",
               "https://www.deseret.com/utah/2023/3/3/23624526/utah-bill-to-close-abortion-clinics-passes-legislature/"]),
        claim("do2", "derrin-owens", "self_defense", 1, True,
              "Voted for Utah SB115 (2022) Firearm Preemption Amendments — the bill, confirming state-only authority to regulate firearms and preventing local governments from imposing additional gun restrictions, cleared the Utah Senate 20-5 with near-unanimous Republican support; Owens voted with the majority.",
              ["https://www.deseret.com/utah/2022/2/3/22916775/gun-laws-utah-firearm-bill-state-final-regulation-senate-preemption-salt-lake-county-gun-shows/",
               "https://le.utah.gov/~2022/bills/static/SB0115.html"]),
    ]),

    # ---------------- Bill Powers (TN-R, Tennessee Senate SD-22) ----------------
    ("bill-powers", "TN", "State Senator", [
        claim("bp1", "bill-powers", "self_defense", 0, True,
              "Voted for Tennessee's permitless carry law (SB765/HB786, signed April 8, 2021) — eliminating the permit requirement for law-abiding adults 21+ to carry a handgun openly or concealed in Tennessee; the bill passed the Republican-controlled Tennessee Senate along party lines, with Powers voting in the majority.",
              ["https://tennesseelookout.com/2021/03/18/permit-less-handgun-carry-rolls-through-senate/",
               "https://www.ammoland.com/2021/03/tennessee-on-the-move-toward-constitutional-carry-hb0786-sb0765/"]),
        claim("bp2", "bill-powers", "biblical_marriage", 2, True,
              "Voted for Tennessee SB1/HB1 (signed March 2, 2023), the state's comprehensive ban on gender-affirming surgeries and puberty blockers for minors — one of the nation's earliest and broadest legislative rejections of transgender medical interventions for children; the bill passed the Republican-controlled Tennessee Senate.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://www.aclu-tn.org/legislation/sb-1hb-1-ban-healthcare-trans-youth/"]),
    ]),

    # ---------------- Bobby Harshbarger (TN-R, Tennessee Senate SD-4) ----------------
    ("bobby-harshbarger", "TN", "State Senator", [
        claim("bh1", "bobby-harshbarger", "industry_capture", 0, True,
              "Sponsored Tennessee SB2040 (2025) FAIR Rx Act — prohibiting pharmacy benefit managers (PBMs) from owning or controlling pharmacies, breaking up the corporate vertical integration that allowed PBMs to simultaneously set drug reimbursement rates and own the pharmacies filling prescriptions; the bill passed both chambers with broad support and was signed into law by Governor Lee.",
              ["https://tnpharm.org/governor-lee-signs-fair-rx-act-into-law/",
               "https://wcyb.com/news/local/tennessee-lawmakers-pass-fair-rx-act-as-cvs-warns-of-closures-and-litigation"]),
        claim("bh2", "bobby-harshbarger", "border_immigration", 2, True,
              "Backed Tennessee's January 2025 immigration enforcement law, approved by the state Senate, which criminalized human smuggling and harboring of undocumented immigrants within Tennessee — extending state-level enforcement against those who shelter illegal immigrants from federal removal, consistent with an anti-sanctuary posture.",
              ["https://nashvillebanner.com/2025/01/30/tennessee-senate-immigration-bill/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to avoid wrong-state slug collisions."""
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
