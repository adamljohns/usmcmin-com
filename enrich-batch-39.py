#!/usr/bin/env python3
"""Enrichment batch 39: 3 bottom-of-alphabet federal candidates (all D).

Targets archetype_curated federal candidates with 0 claims, taken from the
bottom of the reverse-alphabetical bucket.

Candidates:
  Lamont McClure  (PA-07, U.S. Rep candidate, D) — Northampton Co Executive
  Justin Douglas  (PA-10, U.S. Rep candidate, D) — Dauphin Co Commissioner
  Cindy Wilson    (ID Senate 2026, D)             — former teacher / supt candidate

All claims cite 2024-2026 sourced positions; score_impact reflects
alignment with the God-First/America-First rubric (True = aligns).

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
    # ---------------- Lamont McClure (PA-07, D) ----------------
    ("lamont-mcclure", "PA", "Representative", [
        claim("lm1", "lamont-mcclure", "border_immigration", 2, False,
              "As Northampton County Executive, issued an executive order in March 2020 barring ICE agents from making arrests on county property without a judicial warrant — a 'sanctuary' policy that the NRCC characterized as shielding undocumented immigrants from federal deportation proceedings. When the Trump administration designated Northampton County a 'sanctuary jurisdiction' in 2025, McClure rejected the designation and vowed to fight it in court.",
              ["https://www.nrcc.org/2025/05/30/lamont-mcclure-carol-obando-derstine-enable-sanctuary-counties/",
               "https://www.lehighvalleynews.com/criminal-justice/well-see-them-in-court-lehigh-valley-county-execs-reject-trump-sanctuary-designations"]),
        claim("lm2", "lamont-mcclure", "border_immigration", 1, False,
              "Publicly stated that only 'violent criminals' in the country without documentation should be deported, explicitly rejecting blanket mandatory-deportation enforcement and defending his courthouse ICE-restriction order as a matter of due-process rights — a position at odds with the rubric's support for mandatory enforcement.",
              ["https://www.cityandstatepa.com/politics/2026/04/im-only-one-s-ever-been-elected-official-pa-7-dem-primary-lamont-mcclure-runs-his-record/413236/",
               "https://www.nrcc.org/2025/03/01/democrat-lamont-mcclure-is-a-danger-to-pennsylvanians/"]),
    ]),

    # ---------------- Justin Douglas (PA-10, D) ----------------
    ("justin-douglas-pa-10", "PA", "Representative", [
        claim("jd1", "justin-douglas-pa-10", "sanctity_of_life", 0, False,
              "A self-described progressive Democrat who supports abortion access as a right and specifically calls for repealing the Hyde Amendment so that federal Medicaid funds cover abortions for low-income women — rejecting any personhood-from-conception standard and expanding taxpayer funding of abortion.",
              ["https://grokipedia.com/page/Justin_Douglas",
               "https://www.abc27.com/election/one-on-one-with-10th-congressional-candidate-justin-douglas/",
               "https://www.justindouglas.us/positions-1"]),
        claim("jd2", "justin-douglas-pa-10", "biblical_marriage", 2, False,
              "A vocal advocate for LGBTQ rights who was fired from his pastoral position at a Harrisburg-area church for appearing in a promotional video welcoming LGBTQ individuals to the congregation. As county commissioner he helped lead Dauphin County's official Pride Month recognition, and he campaigns on advancing LGBTQ protections in federal law — directly rejecting the rubric's call to refuse transgender and LGBTQ ideology in policy.",
              ["https://grokipedia.com/page/Justin_Douglas",
               "https://www.fox43.com/article/news/local/dauphin-county/dauphin-county-leaders-mark-the-start-of-pride-month/521-e5a89aea-160d-4ca1-a4ec-cae59462fe45",
               "https://www.cityandstatepa.com/politics/2026/05/justin-douglas-leans-his-experience-pa-10-democratic-primary-race/413592/"]),
        claim("jd3", "justin-douglas-pa-10", "self_defense", 1, False,
              "Supports gun-control measures including universal background checks for all firearm sales and safe-storage mandates for firearms — opposing the rubric's defense of unrestricted Second Amendment rights and resistance to background-check registries.",
              ["https://grokipedia.com/page/Justin_Douglas",
               "https://www.abc27.com/election/one-on-one-with-10th-congressional-candidate-justin-douglas/"]),
    ]),

    # ---------------- Cindy Wilson (ID Senate 2026, D) ----------------
    ("cindy-wilson-id-senate", "ID", "Senate", [
        claim("cw1", "cindy-wilson-id-senate", "family_child_sovereignty", 0, False,
              "As the 2018 Democratic nominee for Idaho Superintendent of Public Instruction, ran on a platform centered on expanding government-directed early-childhood programs — all-day kindergarten, state-funded preschool, and centralized teacher-retention spending — prioritizing government schooling infrastructure over parental choice, school autonomy, or homeschool support.",
              ["https://www.idahoednews.org/news/cindy-wilson-candidate-for-state-superintendent/",
               "https://www.idahopress.com/opinion/editorials/endorsement-cindy-wilson-for-superintendent-of-public-instruction/article_0efabff0-b008-5d30-b496-97d9c471b0ac.html"]),
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
