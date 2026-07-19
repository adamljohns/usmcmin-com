#!/usr/bin/env python3
"""Enrichment batch 759: 3rd claim for 4 bottom-of-alpha active federal candidates.

Targets: Paige Loud (ME-02 D), Harry Dunn (MD-05 D), Wala Blegay (MD-05 D),
Rushern Baker (MD-05 D). Each had 2 claims; this batch adds one claim in a
distinct rubric category for each. archetype_curated 0-claim federal pool is
fully depleted — these are evidence_curated 2-claim candidates receiving their
completion claim.

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
    # -------- Paige Loud (ME-02, D) — open Golden seat --------
    ("paige-loud", "ME", "ME-02", [
        claim("pl3", "paige-loud", "sanctity_of_life", 0, False,
              "Supports federal codification of abortion access, stating 'fundamental rights must be the letter of the law' as her rationale. Maine Public's April 2026 voter profile quotes her advocacy for 'access to abortion, birth control, quality prenatal and postnatal care,' and she pledged to defend abortion rights throughout the June 2026 ME-02 Democratic primary — rejecting any personhood-from-conception standard.",
              ["https://www.mainepublic.org/politics/2026-04-19/your-vote-2026-profile-paige-loud-democrat-for-2nd-district",
               "https://www.mainepublic.org/politics/2026-06-03/democrats-in-maines-2nd-congressional-district-primary-trade-jabs-over-abortion"]),
    ]),

    # -------- Harry Dunn (MD-05, D) — open Hoyer seat --------
    ("harry-dunn-md-05", "MD", "MD-05", [
        claim("hd3", "harry-dunn-md-05", "sanctity_of_life", 0, False,
              "His campaign website states: 'We must codify protections for reproductive freedom at the federal level. Reproductive health care is between a doctor and a patient. Politicians need to stay out of the doctor's office.' He also explicitly supports protecting IVF access, rejecting any personhood-from-conception standard.",
              ["https://harrydunnformd.com/issues/"]),
    ]),

    # -------- Wala Blegay (MD-05, D) — open Hoyer seat --------
    ("wala-blegay", "MD", "MD-05", [
        claim("wb3", "wala-blegay", "border_immigration", 2, False,
              "In a May 2026 TANTV interview, Blegay stated 'local governments should refuse cooperation with ICE detainers unless a judicial warrant is presented' — a sanctuary model she said Prince George's County already embraces. She sponsored county legislation to block private immigration detention facilities and called ICE enforcement 'harassing people who have been here a long time,' opposing the rubric's anti-sanctuary position.",
              ["https://www.tantvnews.com/wala-blegay-tantv-interview-gaza-ai-ice-data-centers-md05-2026/"]),
    ]),

    # -------- Rushern Baker (MD-05, D) — open Hoyer seat --------
    ("rushern-baker", "MD", "MD-05", [
        claim("rb3", "rushern-baker", "biblical_marriage", 1, False,
              "While serving as Prince George's County Executive, Baker publicly endorsed same-sex marriage legalization in Maryland ahead of the 2012 state referendum — rejecting the one-man-one-woman marriage definition. He is listed among LGBTQ 'allies on the ballot' in 2026 Maryland primary coverage by the Washington Blade.",
              ["https://en.wikipedia.org/wiki/Rushern_Baker",
               "https://www.washingtonblade.com/2026/06/18/queer-candidates-allies-on-the-ballot-in-md-primary/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
