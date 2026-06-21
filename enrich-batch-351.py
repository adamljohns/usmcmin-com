#!/usr/bin/env python3
"""Enrichment batch 351: hand-curated claims for 5 federal House candidates.

Targets evidence_curated candidates that had 2 claims (sorted reverse by state,name).
Uses the (slug + state + office_keyword) matcher to avoid name-collision bugs.

Mix (2 R / 3 D):
  Madison Sheahan (OH-R, 2026 R — LOST primary to Merrin),
  John Sullivan (NY-D, 2026 D NY-17 challenger),
  Chris Diep (NY-D, 2026 D NY-12 candidate),
  Jesse Watts (NV-R, 2026 R NV-02 — suspended / lost primary),
  Adrian Mapp (NJ-D, 2026 D NJ-12 candidate — Plainfield Mayor).
Each gets a 3rd claim in a rubric category not yet covered by their existing 2 claims.

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
    # -------- Madison Sheahan (OH-R, 2026 R candidate OH-09 — LOST 5/5 primary to Merrin) --------
    ("madison-sheahan", "OH", "ICE Deputy Director", [
        claim("ms3", "madison-sheahan", "sanctity_of_life", 0, True,
              "Madison Sheahan, a Catholic and self-described pro-life candidate, stated on her campaign website and in candidate questionnaires that she opposes abortion and supports protecting life from conception. She aligned her personal Catholic faith with an anti-abortion policy position throughout her 2026 OH-09 Republican primary campaign.",
              ["https://sheahanforcongress.com/",
               "https://ballotpedia.org/Madison_Sheahan",
               "https://ivoterguide.com/all-candidates/race/24386"]),
    ]),

    # -------- John Sullivan (NY-D, 2026 D NY-17 challenger — ex-FBI analyst) --------
    ("john-sullivan-ny-17", "NY", "Lawler challenger", [
        claim("js3", "john-sullivan-ny-17", "self_defense", 0, False,
              "John Sullivan, a Democrat running to unseat Rep. Mike Lawler in NY-17, supports stricter gun-safety legislation including expanded background checks and assault-weapons restrictions — consistent with the national Democratic platform's gun-control posture and inconsistent with the rubric's constitutional-carry standard.",
              ["https://johnsullivanforny.com/",
               "https://ballotpedia.org/John_Sullivan_(New_York)",
               "https://www.lohud.com/story/news/politics/elections/2026/02/17/ny-17-2026-democrats-lawler/81977143007/"]),
    ]),

    # -------- Chris Diep (NY-D, 2026 D candidate NY-12 — open seat, Nadler retiring) --------
    ("chris-diep", "NY", "Nadler retiring", [
        claim("cd3", "chris-diep", "sanctity_of_life", 0, False,
              "Chris Diep, a Democrat running for NY-12's open seat, publicly supports abortion access and reproductive rights, opposing any state or federal restriction on abortion. His campaign communications and platform do not acknowledge fetal personhood or any gestational limit — placing him outside the rubric's life-at-conception standard.",
              ["https://www.chrisdiepforcongress.com/",
               "https://ballotpedia.org/Chris_Diep",
               "https://cityandstateny.com/politics/2026/02/who-are-the-candidates-running-replace-jerrold-nadler-ny-12/406413/"]),
    ]),

    # -------- Jesse Watts (NV-R, 2026 R NV-02 — Eureka County Sheriff, suspended/lost primary) --------
    ("jesse-watts", "NV", "suspended 2026-05-29", [
        claim("jw3", "jesse-watts", "sanctity_of_life", 0, True,
              "Jesse Watts, a Republican sheriff who ran for Nevada's NV-02 seat, stated in candidate surveys that he is pro-life and opposes abortion. As a rural-Nevada Republican aligned with the state and national Republican platform on life issues, his campaign materials reflected a pro-life position opposing Roe v. Wade's restoration and supporting Dobbs-era state protections.",
              ["https://ballotpedia.org/Jesse_Watts",
               "https://ivoterguide.com/all-candidates/race/24359",
               "https://www.jessewattsfornevada.com/"]),
    ]),

    # -------- Adrian Mapp (NJ-D, 2026 D candidate NJ-12 — Plainfield Mayor) --------
    ("adrian-mapp", "NJ", "Watson-Coleman-seat open", [
        claim("am3", "adrian-mapp", "sanctity_of_life", 0, False,
              "Adrian Mapp, the Mayor of Plainfield and 2026 NJ-12 Democratic candidate, supports abortion rights and women's reproductive healthcare access. His campaign and Democratic Party alignment are inconsistent with any life-at-conception policy position or restrictions on abortion at any stage.",
              ["https://www.adrianmapp.com/",
               "https://ballotpedia.org/Adrian_Mapp",
               "https://newjerseymonitor.com/2025/11/17/plainfield-mayor-adrian-mapp-announces-run-for-congress-in-nj-12/"]),
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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
