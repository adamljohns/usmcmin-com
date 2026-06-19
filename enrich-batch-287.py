#!/usr/bin/env python3
"""Enrichment batch 287: hand-curated claims for 4 federal House candidates.

Targets: active evidence_federal candidates with 0 claims from the bottom
of the alphabet (NY, MD, KY).  All sitting federal senator/rep slots are
exhausted; this batch draws from 2026 challenger / open-seat candidates
with documented 2026 campaign positions.

Candidates (4 total, all D):
  Mike Sacks         (NY-17 D, Lawler challenger)
  Arthur Ellis       (MD-05 D, Hoyer open-seat)
  Patrick Timmins    (NY-12 D, Nadler open-seat)
  Melissa Strange    (KY-04 D, Massie challenger – D nominee)

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's
50 MB warning.
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
    # ---------- Mike Sacks (NY-17, D – Lawler challenger) ----------
    ("mike-sacks-ny-17", "NY", "Representative", [
        claim("ms1", "mike-sacks-ny-17", "sanctity_of_life", 0, False,
              "Declares 'Abortion is healthcare' on his campaign platform and calls for codifying Roe v. Wade into federal law, restoring reproductive freedom, and protecting bodily autonomy — rejecting any life-at-conception personhood standard.",
              ["https://thehill.com/homenews/5240419-comedian-mike-sacks-campaign/",
               "https://www.mikesacksforcongress.com/"]),
        claim("ms2", "mike-sacks-ny-17", "self_defense", 1, False,
              "Campaign platform calls to 'break the NRA's hold and choose lives over profits,' explicitly opposing the gun-rights lobby and backing gun-safety restrictions — the inverse of the rubric's defense of unrestricted Second Amendment rights.",
              ["https://thehill.com/homenews/5240419-comedian-mike-sacks-campaign/",
               "https://www.mikesacksforcongress.com/"]),
        claim("ms3", "mike-sacks-ny-17", "border_immigration", 1, False,
              "Supports 'a roadmap to citizenship' for undocumented immigrants and advocates treating 'asylum seekers with dignity' — opposing mandatory deportation and endorsing a pathway-to-legalization approach.",
              ["https://www.mikesacksforcongress.com/"]),
    ]),

    # ---------- Arthur Ellis (MD-05, D – Hoyer open-seat) ----------
    ("arthur-ellis", "MD", "Representative", [
        claim("ae1", "arthur-ellis", "self_defense", 0, False,
              "Co-sponsored Maryland's Gun Safety Act of 2023 (SB 1), which restricts the carrying of firearms in sensitive places including churches, government buildings, stadiums, and schools; the bill passed the Senate 31–16 and was signed into law — opposing the constitutional-carry standard.",
              ["https://legiscan.com/MD/bill/SB1/2023",
               "https://trackbill.com/bill/maryland-senate-bill-1-criminal-law-wearing-carrying-or-transporting-firearms-restrictions-gun-safety-act-of-2023/2301527/"]),
        claim("ae2", "arthur-ellis", "border_immigration", 1, False,
              "Congressional campaign platform calls for 'humane immigration reform,' opposing mass deportation and emphasizing technology-assisted pathways for immigrants navigating the system — contrary to the rubric's mandatory-deportation standard.",
              ["https://arthurellisforcongress.com/",
               "https://marylandmatters.org/2026/02/03/5th-district-gets-crowded-ferguson-wont-say-the-d-word-ellis-ai-trek-continues-in-political-notes/"]),
    ]),

    # ---------- Patrick Timmins (NY-12, D – Nadler open-seat) ----------
    ("patrick-timmins", "NY", "Representative", [
        claim("pt1", "patrick-timmins", "border_immigration", 1, False,
              "Proposed a 'Democratic Blue Card' granting legal status and a pathway to citizenship for undocumented immigrants who have lived in the U.S. for 10 or more years without legal trouble — opposing mandatory deportation and the rubric's enforcement-first standard.",
              ["https://www.westsiderag.com/2026/03/23/a-wsr-conversation-with-candidate-patrick-timmins-in-the-race-to-represent-the-uws-in-congress",
               "https://timminsforcongress.com/"]),
        claim("pt2", "patrick-timmins", "self_defense", 1, False,
              "As a career Bronx DA prosecutor turned congressional candidate, calls for stopping 'guns coming from gun-friendly states' via stricter interstate firearms enforcement and routing illegal-gun prosecutions to federal courts — supporting restrictions on firearm access rather than the rubric's anti-registry/anti-ban posture.",
              ["https://www.westsiderag.com/2026/03/23/a-wsr-conversation-with-candidate-patrick-timmins-in-the-race-to-represent-the-uws-in-congress"]),
    ]),

    # ---------- Melissa Strange (KY-04, D – D nominee vs Gallrein) ----------
    ("melissa-strange", "KY", "Representative", [
        claim("mst1", "melissa-strange", "sanctity_of_life", 0, False,
              "States explicitly that 'personal medical decisions should remain between patients and their healthcare providers — not politicians' and pledges to protect abortion access at the federal level, safeguarding comprehensive reproductive healthcare including birth control and maternal care — rejecting any life-at-conception personhood standard.",
              ["https://www.ballotready.org/people/melissa-claire-stange",
               "https://www.branch.vote/races/2026-kentucky-primary-election-ky-state-us-representative-ky-congressional-4-d/candidates/melissa-claire-strange"]),
        claim("mst2", "melissa-strange", "sanctity_of_life", 2, False,
              "Explicitly supports IVF access, calling for fertility treatments to remain 'accessible and affordable for all' — opposing any restrictions that would treat embryo discard during IVF as a legal violation, in direct contrast to the rubric's anti-IVF-discard position.",
              ["https://www.ballotready.org/people/melissa-claire-stange",
               "https://www.branch.vote/races/2026-kentucky-primary-election-ky-state-us-representative-ky-congressional-4-d/candidates/melissa-claire-strange"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
