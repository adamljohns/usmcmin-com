#!/usr/bin/env python3
"""Enrichment batch 66: hand-curated claims for 3 House candidates (IL-09/GA-13/CO-08 bottom-alpha).

Targets archetype_curated House candidates from the bottom of the alphabet
with 0 evidence claims. All three are Democratic candidates whose positions
are sourced from 2025-2026 campaign materials and news coverage.

Targets (3 D): Kat Abughazaleh (IL-09), Everton Blair (GA-13),
Evan Munsing (CO-08).

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
    # ---------------- Kat Abughazaleh (IL-09, D) ----------------
    ("kat-abughazaleh", "IL", "Representative", [
        claim("ka1", "kat-abughazaleh", "sanctity_of_life", 0, False,
              "States that 'abortion access is essential to healthcare, plain and simple,' supports codifying abortion rights and LGBTQIA+ protections in federal law, and voiced her pro-choice platform as a Democratic socialist running in the March 2026 IL-09 primary — rejecting any personhood-from-conception standard.",
              ["https://katforillinois.com/issues/",
               "https://chicago.suntimes.com/elections/2026/candidate-questionnaires/kat-abughazaleh-illinois-primary-9th-congressional-district"]),
        claim("ka2", "kat-abughazaleh", "self_defense", 1, False,
              "Advocates for a federal assault-weapons ban modeled on Illinois state law, universal background checks, mandatory waiting periods, mandatory gun-safety training, and closure of ghost-gun and gun-show loopholes — directly opposing the rubric's protection of semi-automatic rifle ownership and its opposition to additional firearm restrictions.",
              ["https://chicago.suntimes.com/elections/2026/candidate-questionnaires/kat-abughazaleh-illinois-primary-9th-congressional-district",
               "https://katforillinois.com/issues/"]),
        claim("ka3", "kat-abughazaleh", "border_immigration", 1, False,
              "Explicitly opposes deportation except for individuals convicted of violent crimes, and would instead codify the right to seek asylum and streamline the legal-immigration process — rejecting mandatory deportation and interior enforcement.",
              ["https://katforillinois.com/issues/",
               "https://chicago.suntimes.com/elections/2026/candidate-questionnaires/kat-abughazaleh-illinois-primary-9th-congressional-district"]),
    ]),

    # ---------------- Everton Blair (GA-13, D) ----------------
    ("everton-blair", "GA", "Representative", [
        claim("eb1", "everton-blair", "biblical_marriage", 0, False,
              "An openly gay candidate endorsed by the LGBTQ+ Victory Fund, running to become the first openly gay Black Congressman from the South. He actively defends marriage equality, opposes any one-man-one-woman definition of marriage, and marched in the 2025 Atlanta Pride Parade as a frontrunner for GA-13.",
              ["https://victoryfund.org/candidate/blair-everton/",
               "https://www.gayemagazine.com/meet-everton-blair-jr-the-georgia-candidate-aiming-to-become-the-souths-first-black-openly-gay-congressman/"]),
        claim("eb2", "everton-blair", "sanctity_of_life", 0, False,
              "Pledged to be 'a fierce defender of reproductive freedom,' calling for federal codification of abortion rights and framing restrictions on abortion as a 'coordinated, authoritarian attack' on bodily autonomy — rejecting any life-at-conception standard.",
              ["https://ballotpedia.org/Everton_Blair_Jr.",
               "https://www.evertonblair.com/"]),
        claim("eb3", "everton-blair", "border_immigration", 1, False,
              "Proposes replacing ICE with 'an immigration system rooted in dignity, due process, and accountability' and supports Medicare for All — rejecting mandatory deportation and enforcement-first border policy.",
              ["https://ballotpedia.org/Everton_Blair_Jr.",
               "https://news.ballotpedia.org/2026/04/14/incumbent-david-scott-d-everton-blair-jr-d-jasmine-clark-d-emanuel-jones-d-heavenly-kimes-d-and-two-other-candidates-are-running-in-the-democratic-primary-for-georgias-13th-congressi/"]),
    ]),

    # ---------------- Evan Munsing (CO-08, D) ----------------
    ("evan-munsing", "CO", "Representative", [
        claim("em1", "evan-munsing", "sanctity_of_life", 0, False,
              "Cited 'protecting individual freedoms like reproductive rights' as a primary motivation for his congressional run, signaling pro-abortion-access alignment inconsistent with the rubric's life-at-conception standard.",
              ["https://www.coloradopolitics.com/2026/02/07/evans-challenger-evan-munsing-qualifies-by-petition-for-democratic-primary-ballot-in-colorados-8th-cd/",
               "https://www.cpr.org/2026/05/29/vg-2026-primary-election-8th-congressional-district-evan-munsing/"]),
        claim("em2", "evan-munsing", "economic_stewardship", 2, False,
              "Pledged to repeal the 'One Big Beautiful Bill' — the 2025 reconciliation legislation that reduces projected federal deficits — calling it harmful to public services such as Medicaid and ACA subsidies; this opposes the rubric's balanced-budget and anti-deficit principle.",
              ["https://www.cpr.org/2026/05/29/vg-2026-primary-election-8th-congressional-district-evan-munsing/",
               "https://www.coloradopolitics.com/2025/12/30/evan-munsing-colorado-democratic-primary-cd8-candidate/"]),
        claim("em3", "evan-munsing", "border_immigration", 0, False,
              "Calls for reforming ICE and CBP with body cameras and visible identification rather than expanded enforcement or wall construction, rejecting the rubric's wall-and-military posture at the southern border.",
              ["https://www.cpr.org/2026/05/29/vg-2026-primary-election-8th-congressional-district-evan-munsing/"]),
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
