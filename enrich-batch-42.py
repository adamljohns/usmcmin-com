#!/usr/bin/env python3
"""Enrichment batch 42: 5 bottom-of-alphabet archetype_curated federal
candidates with 0 claims.

Targets (bottom of alpha, NC/NE/NV/NJ):
  Virginia Foxx (NC-5 R sitting U.S. Representative),
  Brinker Harding (NE-02 R Trump-endorsed 2026 nominee),
  Mark Robertson (NV-01 R 2024/2026 nominee),
  John Lee (NV-04 R 2026 candidate, former NLV mayor),
  Rajesh Mohan (NJ-03 R 2026 candidate, cardiologist).

2-3 claims per candidate spanning distinct rubric categories; all sourced
from official sites, govtrack, ballotpedia, or regional press.

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
    # ---- Virginia Foxx (NC-5, R, sitting U.S. Representative) ----
    ("virginia-foxx", "NC", "Representative", [
        claim("vf1", "virginia-foxx", "sanctity_of_life", 0, True,
              "On the 46th anniversary of Roe v. Wade, declared 'we remember the 60 million babies aborted in the U.S. since this lethal SCOTUS decision.' When asked whether any condition justified abortion she answered no — rejecting exceptions for rape, incest, or the health of the mother, consistent with a life-from-conception position.",
              ["https://en.wikipedia.org/wiki/Virginia_Foxx",
               "https://foxx.house.gov/issues/"]),
        claim("vf2", "virginia-foxx", "self_defense", 1, True,
              "Holds a career A-rating from the NRA. Her official issues page states 'Americans must have the ability to defend themselves and their loved ones.' Co-sponsored H.R. 367, the Hearing Protection Act of 2017, to remove suppressors from NFA restrictions — opposing registry-and-ban expansion of federal gun controls.",
              ["https://foxx.house.gov/issues/issue/?IssueID=106729",
               "https://en.wikipedia.org/wiki/Virginia_Foxx"]),
        claim("vf3", "virginia-foxx", "economic_stewardship", 2, True,
              "Has publicly stated 'we must continue to cut wasteful federal spending and redirect limited funds to federal priorities' — a consistent anti-deficit, balanced-budget posture maintained across her 20-year House tenure.",
              ["https://en.wikipedia.org/wiki/Virginia_Foxx",
               "https://foxx.house.gov/issues/"]),
    ]),

    # ---- Brinker Harding (NE-02, R, Trump-endorsed 2026 nominee) ----
    ("brinker-harding", "NE", "Representative", [
        claim("bh1", "brinker-harding", "border_immigration", 0, True,
              "His campaign platform calls to 'finish the wall and enforce immigration laws,' citing 10.3 million illegal border crossings under Biden as justification for completing physical barrier construction along the southern border.",
              ["https://www.brinkerharding.com/vision",
               "https://nebraskaexaminer.com/voter-guides/contests/2026-primary-u-s-house-district-2/"]),
        claim("bh2", "brinker-harding", "border_immigration", 1, True,
              "Explicitly pledges to 'deport criminal illegal immigrants' and to 'keep our communities safe' from migrant crime — committing to mandatory removal as a core immigration enforcement position.",
              ["https://www.brinkerharding.com/vision",
               "https://nebraskaexaminer.com/briefs/trump-gives-total-endorsement-to-brinker-harding-in-ne-02/"]),
        claim("bh3", "brinker-harding", "self_defense", 1, True,
              "Earned Trump's 'Total Endorsement,' whose endorsement letter explicitly highlights that Harding will 'Protect our always under siege Second Amendment.' Harding has not supported any new firearm restrictions during his tenure on the Omaha City Council.",
              ["https://nebraskaexaminer.com/briefs/trump-gives-total-endorsement-to-brinker-harding-in-ne-02/",
               "https://www.nrcc.org/2026/04/14/%F0%9F%9A%A8-president-trump-endorses-brinker-harding-for-congress/"]),
    ]),

    # ---- Mark Robertson (NV-01, R, 2024/2026 nominee) ----
    ("mark-robertson", "NV", "Representative", [
        claim("mr1", "mark-robertson", "border_immigration", 0, True,
              "Supports completing the border wall along the southern U.S. border, calls border security 'a matter of national security,' and endorses Trump's wall initiative. He would limit legal immigration to those who 'can sustain themselves without government assistance' and embrace 'our culture and language (English).'",
              ["https://thenevadaindependent.com/article/on-the-record-republican-congressional-district-1-candidate-mark-robertson",
               "https://ballotpedia.org/Mark_Robertson_(Nevada)"]),
        claim("mr2", "mark-robertson", "election_integrity", 0, True,
              "Backed Nevada's 2026 voter-ID ballot measure (Question 7), calling it a 'common-sense' election-security step — aligning with the rubric's voter-ID pillar of election integrity.",
              ["https://thenevadaindependent.com/article/dina-titus-mark-robertson-face-off-again-in-nevadas-1st-congressional-district",
               "https://mynews4.com/news/local/2026-midterm-election-what-questions-will-be-on-the-ballot"]),
        claim("mr3", "mark-robertson", "sanctity_of_life", 0, False,
              "Called federal abortion legislation 'unnecessary' given that Nevada law already permits abortion through 24 weeks, and explicitly stated he would not support any federal legislation to overturn Nevada voters' abortion preferences — rejecting a life-at-conception/personhood position at the federal level.",
              ["https://thenevadaindependent.com/article/on-the-record-republican-congressional-district-1-candidate-mark-robertson",
               "https://ballotpedia.org/Mark_Robertson_(Nevada)"]),
    ]),

    # ---- John Lee (NV-04, R, 2026 candidate) ----
    ("john-lee-nv-04", "NV", "Representative", [
        claim("jl1", "john-lee-nv-04", "sanctity_of_life", 0, True,
              "Favored a heartbeat bill (prohibiting abortion once a fetal heartbeat is detected at approximately 6 weeks) and voted against Nevada's Question 6 — the 2024 ballot measure to enshrine abortion rights up to viability in the state constitution — signaling a consistently pro-life legislative posture.",
              ["https://knpr.org/show/knprs-state-of-nevada/2024-10-15/for-nevadas-4th-congressional-district-lee-challenges-incumbent-horsford",
               "https://en.wikipedia.org/wiki/John_Lee_(Nevada_politician)"]),
        claim("jl2", "john-lee-nv-04", "border_immigration", 0, True,
              "Supports more border wall construction along the southern border, calling illegal immigration a drain on public resources and taxpayer dollars; border security is listed as a top federal priority on his campaign platform.",
              ["https://knpr.org/show/knprs-state-of-nevada/2024-10-15/for-nevadas-4th-congressional-district-lee-challenges-incumbent-horsford",
               "https://lasvegassun.com/news/2024/aug/04/gop-sees-lee-as-best-hope-to-pick-up-house-seat-in/"]),
        claim("jl3", "john-lee-nv-04", "economic_stewardship", 2, True,
              "As mayor of North Las Vegas, eliminated the city's long-term budget deficit from $156 million (2013) down to zero without raising taxes or fees on constituents — a documented fiscal record aligned with the rubric's anti-deficit standard.",
              ["https://lasvegassun.com/news/2024/aug/04/gop-sees-lee-as-best-hope-to-pick-up-house-seat-in/",
               "https://en.wikipedia.org/wiki/John_Lee_(Nevada_politician)"]),
    ]),

    # ---- Rajesh Mohan (NJ-03, R, 2026 candidate) ----
    ("rajesh-mohan-nj-03", "NJ", "Representative", [
        claim("rm1", "rajesh-mohan-nj-03", "border_immigration", 0, True,
              "'Border Security and Stop illegal immigration' is listed as a top campaign priority, and he has highlighted the need to secure the border and enforce immigration laws in multiple candidate forums in NJ-03.",
              ["https://mohanforuscongress.com/",
               "https://ballotpedia.org/Rajesh_Mohan"]),
        claim("rm2", "rajesh-mohan-nj-03", "industry_capture", 0, True,
              "As a quadruple-board-certified cardiologist, his signature healthcare plank is 'restoring the patient-doctor relationship by removing insurance companies and government out of the exam room' — opposing government and industry mandates over medical practice and patient care.",
              ["https://mohanforuscongress.com/",
               "https://americankahani.com/lead-stories/indian-american-cardiologist-rajesh-mohan-wins-republican-primary-in-new-jerseys-third-congressional-district/"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
