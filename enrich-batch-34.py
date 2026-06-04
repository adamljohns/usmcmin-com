#!/usr/bin/env python3
"""Enrichment batch 34: hand-curated claims for 4 federal House candidates (bottom of alphabet bucket).

Targets archetype_curated federal House candidates from the TX bucket with 0 evidence claims.
Mix (1 R / 3 D): Jason Corley (TX-19-R), Michelle Vallejo (TX-15-D),
Jessica Cisneros (TX-28-D), Frederick D. Haynes III (TX-30-D).
Each claim cites >=1 reliable source and reflects 2024-2026 stated positions.

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
    # ---------------- Jason Corley (TX-19, R, House) ----------------
    ("jason-corley", "TX", "Representative", [
        claim("jc1", "jason-corley", "sanctity_of_life", 0, True,
              "Stated in a 2026 campaign interview that 'Abortion is NOT EVER necessary to save the life of a mother,' drawing a firm distinction between abortion and emergency medical procedures such as ectopic-pregnancy surgery — affirming a life-from-conception posture consistent with a personhood standard.",
              ["https://www.kacu.org/local-news/2026-02-25/jason-corley-hopes-to-switch-from-lubbock-county-commissioner-to-tx-19-congressman",
               "https://www.everythinglubbock.com/features/talking-points-features/lubbock-republican-primary-race/"]),
        claim("jc2", "jason-corley", "border_immigration", 0, True,
              "Pledged in his 2026 congressional campaign to entrench Trump's border enforcement so it outlasts the administration, stating 'Texas is ground zero for the border crisis and a secure nation requires a secure border.' Supports continued physical barriers and military-level border security.",
              ["https://www.kacu.org/local-news/2026-02-25/jason-corley-hopes-to-switch-from-lubbock-county-commissioner-to-tx-19-congressman",
               "https://ballotpedia.org/Jason_Corley_(Texas)"]),
        claim("jc3", "jason-corley", "economic_stewardship", 2, True,
              "As Lubbock County Commissioner, twice declined personal pay raises and redirected those funds to volunteer fire departments; ran for Congress on a platform of cutting government spending to lower the cost of living — a record of fiscal restraint matching the rubric's balanced-budget standard.",
              ["https://www.kacu.org/local-news/2026-02-25/jason-corley-hopes-to-switch-from-lubbock-county-commissioner-to-tx-19-congressman",
               "https://103kkcn.com/ixp/190/p/lubbock-commissioner-corley-campaign/"]),
    ]),

    # ---------------- Michelle Vallejo (TX-15, D, House) ----------------
    ("michelle-vallejo", "TX", "Representative", [
        claim("mv1", "michelle-vallejo", "sanctity_of_life", 0, False,
              "Openly supports abortion rights; ran in the 2022 primary backed by the Congressional Progressive Caucus (whose members include AOC, Ilhan Omar, and Rashida Tlaib), an organization that opposes any restriction on abortion — rejecting the rubric's life-from-conception standard.",
              ["https://www.texastribune.org/2022/08/24/tx15-vallejo-de-la-cruz-2022-midterm/",
               "https://ballotpedia.org/Michelle_Vallejo"]),
        claim("mv2", "michelle-vallejo", "self_defense", 1, False,
              "Stated 'common-sense gun safety measures can prevent gun violence in America and still respect the Second Amendment' and explicitly backed the bipartisan 2022 gun safety bill that funds red-flag laws and expands background checks — directly opposing the rubric's rejection of red-flag legislation.",
              ["https://www.nrcc.org/2022/08/17/michelle-vallejo-deletes-progressive-priorities-from-website/",
               "https://freebeacon.com/democrats/she-won-her-texas-primary-as-an-unabashed-liberal-now-michelle-vallejo-is-abandoning-her-far-left-policies/"]),
        claim("mv3", "michelle-vallejo", "border_immigration", 1, False,
              "Her 2022 campaign platform called for a 'pathway to citizenship for all 11 million undocumented Americans,' opposing mandatory deportation. She quietly deleted this language under political pressure before the general election, but the original position was documented by multiple outlets.",
              ["https://freebeacon.com/democrats/she-won-her-texas-primary-as-an-unabashed-liberal-now-michelle-vallejo-is-abandoning-her-far-left-policies/",
               "https://www.nrcc.org/2022/08/17/michelle-vallejo-deletes-progressive-priorities-from-website/"]),
    ]),

    # ---------------- Jessica Cisneros (TX-28, D, House) ----------------
    ("jessica-cisneros", "TX", "Representative", [
        claim("jci1", "jessica-cisneros", "sanctity_of_life", 4, False,
              "Received the Planned Parenthood Action Fund endorsement for her TX-28 primary campaigns; explicitly calls to repeal the Hyde Amendment and codify Roe v. Wade — placing her squarely inside the abortion-funding endorsement network the rubric flags.",
              ["https://www.commondreams.org/newswire/2021/11/23/planned-parenthood-action-fund-endorses-jessica-cisneros-tx-28",
               "https://en.wikipedia.org/wiki/Jessica_Cisneros"]),
        claim("jci2", "jessica-cisneros", "self_defense", 1, False,
              "Supports banning bump stocks, high-capacity magazines, and 'weapons of war' (semi-automatic rifles), and advocates for expanded universal background checks — opposing the rubric's protection of unrestricted Second Amendment rights.",
              ["https://livableworld.org/meet-the-candidates/house-candidates/jessica-cisneros-for-house-d-tx-28/",
               "https://jessicacisnerosforcongress.com/issues/"]),
        claim("jci3", "jessica-cisneros", "border_immigration", 1, False,
              "As an immigration removal-defense attorney, campaigns for an independent immigration court insulated from presidential enforcement priorities — opposing mandatory deportation and supporting judicial discretion over enforcement-first border policy.",
              ["https://jessicacisnerosforcongress.com/issues/",
               "https://en.wikipedia.org/wiki/Jessica_Cisneros"]),
    ]),

    # ---------------- Frederick D. Haynes III (TX-30, D, House) ----------------
    ("frederick-d-haynes-iii", "TX", "Representative", [
        claim("fdh1", "frederick-d-haynes-iii", "border_immigration", 2, False,
              "Launched his 2026 congressional campaign with abolishing ICE as a flagship pledge, stating at his kickoff event that dismantling U.S. Immigration and Customs Enforcement is a core priority — the inverse of the rubric's demand for robust interior immigration enforcement.",
              ["https://www.wfaa.com/article/news/politics/elections/dallas-pastor-frederick-haynes-house-campaign-abolish-ice/287-6fc619b6-c6ac-43e9-9dc0-a188ee138271",
               "https://www.keranews.org/politics/2026-01-12/frederick-haynes-friendship-west-baptist-congress-district-30-jasmine-crockett"]),
        claim("fdh2", "frederick-d-haynes-iii", "economic_stewardship", 2, False,
              "Advocates Medicare for All — a single-payer federal takeover of health insurance that estimates have placed in the multi-trillion-dollar range in added federal outlays — rejecting the rubric's balanced-budget and limited-government standards.",
              ["https://www.keranews.org/politics/2026-01-12/frederick-haynes-friendship-west-baptist-congress-district-30-jasmine-crockett",
               "https://www.cbsnews.com/texas/news/dr-frederick-haynes-iii-friendship-west-baptist-church-30th-congressional-district-jasmine-crockett/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs across states."""
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
