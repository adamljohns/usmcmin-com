#!/usr/bin/env python3
"""Enrichment batch 284: hand-curated claims for 4 active 2026 House candidates.

All four are evidence_federal confidence with 0 claims. Drawn from the bottom
of the alphabet (NY, MO, ME, CA) to avoid collision with the top-of-alphabet
enrichment loop. 9 total claims across 4 candidates.

Targets: Blake Gendebien (NY-21 D), Josh Smead (MO-06 D),
         Matthew Dunlap (ME-02 D), Jasmeet Bains (CA-22 D).

Sources: WAMC/WRVO candidate profiles, Daily Gazette debate coverage,
         votesmead.com, KCUR, centralmaine.com, Maine Public, American Prospect.
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
    # ---------------- Blake Gendebien (NY-21, D) ----------------
    ("blake-gendebien", "NY", "NY-21", [
        claim("bg1", "blake-gendebien", "sanctity_of_life", 0, False,
              "Supports a woman's right to choose and opposes abortion bans, including bans that would prohibit abortion in cases of rape or when the life of the mother is at stake — rejecting any life-from-conception standard.",
              ["https://www.wrvo.org/2026-06-10/ny-21-candidate-profile-democrat-blake-gendebien",
               "https://www.wamc.org/news/2026-06-10/ny-21-candidate-profile-democrat-blake-gendebien"]),
        claim("bg2", "blake-gendebien", "self_defense", 0, False,
              "Calls himself a '2A supporter' but explicitly backs universal background checks and safe-storage mandates — regulatory expansions that fall outside the rubric's constitutional-carry, no-new-restrictions standard.",
              ["https://www.dailygazette.com/ade/cjfund/gendebien-amoriell-square-off-in-ny21-democratic-debate-divided-on-immigration/article_1fbd8887-1658-49af-9f41-f21d243e5f5b.html",
               "https://www.wrvo.org/2026-06-10/ny-21-candidate-profile-democrat-blake-gendebien"]),
        claim("bg3", "blake-gendebien", "border_immigration", 1, False,
              "Opposes mandatory deportation; supports a legal pathway to citizenship for those who entered the country illegally and advocates for lawful migrant-worker programs — directly at odds with the rubric's mandatory-deportation standard.",
              ["https://www.dailygazette.com/ade/cjfund/gendebien-amoriell-square-off-in-ny21-democratic-debate-divided-on-immigration/article_1fbd8887-1658-49af-9f41-f21d243e5f5b.html",
               "https://www.northcountrypublicradio.org/news/story/53573/20260616/ny-21-democratic-candidates-debate-ahead-of-june-23-primary"]),
    ]),

    # ---------------- Josh Smead (MO-06, D) ----------------
    ("josh-smead", "MO", "MO-06", [
        claim("js1", "josh-smead", "self_defense", 0, False,
              "States the 'Second Amendment is worth protecting while working to lower firearm deaths in America' — a regulatory-balance framing that stops short of constitutional carry and endorses gun-control legislation to reduce firearms deaths.",
              ["https://votesmead.com/",
               "https://www.kcur.org/politics-elections-and-government/2026-03-31/kansas-city-congressional-district-candidates-2026"]),
        claim("js2", "josh-smead", "border_immigration", 1, False,
              "Advocates immigration enforcement that is 'lawful, transparent, and centered on due process, with resources focused on courts instead of mass detention centers' — explicitly rejecting mandatory deportation and mass-detention enforcement.",
              ["https://votesmead.com/"]),
    ]),

    # ---------------- Matthew Dunlap (ME-02, D) ----------------
    ("matthew-dunlap", "ME", "ME-02", [
        claim("md1", "matthew-dunlap", "sanctity_of_life", 0, False,
              "States that 'the decision to terminate a pregnancy belongs to the woman faced with whatever circumstances affect her' and that 'safe access to reproductive health care should be a constitutional right'; supports codifying Roe v. Wade into federal law — rejecting any life-from-conception standard.",
              ["https://www.centralmaine.com/2025/12/08/matt-dunlap-hoping-to-replace-jared-golden-defends-abortion-record/",
               "https://www.mainepublic.org/politics/2026-04-19/your-vote-2026-profile-matt-dunlap-democrat-for-2nd-district"]),
        claim("md2", "matthew-dunlap", "sanctity_of_life", 4, False,
              "Holds an 83% rating from the Planned Parenthood Maine Action Fund, placing him within the PP/abortion-industry endorsement and funding network — failing the rubric's 'never took PP/NARAL/EMILY money' standard.",
              ["https://www.centralmaine.com/2025/12/08/matt-dunlap-hoping-to-replace-jared-golden-defends-abortion-record/",
               "https://www.mainepublic.org/politics/2026-06-03/democrats-in-maines-2nd-congressional-district-primary-trade-jabs-over-abortion"]),
    ]),

    # ---------------- Jasmeet Bains (CA-22, D) ----------------
    ("jasmeet-bains", "CA", "CA-22", [
        claim("jb1", "jasmeet-bains", "sanctity_of_life", 4, False,
              "Endorsed by the Planned Parenthood Action Fund (PP's political PAC), which entered the CA-22 Democratic primary specifically to back her — placing her squarely inside the abortion-industry endorsement-and-funding network the rubric disqualifies.",
              ["https://prospect.org/2026/05/15/planned-parenthood-congressional-primary-california-bains-valadao-villegas/",
               "https://ballotpedia.org/Jasmeet_Bains"]),
        claim("jb2", "jasmeet-bains", "sanctity_of_life", 0, False,
              "Pro-choice candidate whose Planned Parenthood endorsement and campaign platform confirm support for abortion rights and reproductive healthcare access — rejecting any life-from-conception or personhood-from-conception standard.",
              ["https://prospect.org/2026/05/15/planned-parenthood-congressional-primary-california-bains-valadao-villegas/",
               "https://www.kget.com/news/politics/your-local-elections/asm-dr-jasmeet-bains-announces-2026-run-for-congress-for-rep-david-valadaos-seat/"]),
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
