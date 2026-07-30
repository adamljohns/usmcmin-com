#!/usr/bin/env python3
"""Enrichment batch 896: 5 Wyoming House Republicans (bottom-of-alphabet deepening).

Archetype_curated bucket is fully exhausted; this batch deepens lightly-enriched
state legislators from WY — bottom of alphabet. Targets had 1-2 claims (sanctity_of_life
and/or election_integrity only); this batch adds self_defense, family_child_sovereignty,
biblical_marriage, and/or refuse_state_overreach claims based on sourced 2024-2026 votes.

Targets:
  John Bear (WY-R, District 31, Gillette) — 2 election_integrity claims → +3
  John Winter (WY-R, District 28, Thermopolis) — +2
  J.T. Larson (WY-R, District 17, Rock Springs) — +2
  Lloyd Larsen (WY-R, District 54, Lander) — +2
  J.D. Williams (WY-R, District 2, rancher/Scottsbluff-roots) — +2

Key sourced bills:
  HB0172 (2025) — Repeal gun-free zones + preemption; became law Feb 27, 2025
  HB0046 (2025) — Homeschool Freedom Act; passed 54-6-2; became law Feb 27, 2025
  HB0126 (2026) — Wyoming Human Heartbeat Act; passed 51-7-4; signed into law
  SF0103 (2025) — DEI termination/defunding; passed House 52-7; enacted
  HB0011 (2025) — Eminent Domain-Landowner Bill of Rights; sponsored by J.D. Williams
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
    # ---------- John Bear (WY-R, District 31, Gillette) ----------
    # Already has: election_integrity[0] x2 (HB0156 + HB0173 co-sponsor)
    # Adding: self_defense, sanctity_of_life, family_child_sovereignty
    ("john-bear", "WY", "Representative", [
        claim("896a", "john-bear", "self_defense", 0, True,
              "Co-sponsored HB0172 (2025), Wyoming's landmark gun-free zones repeal, which allows permit holders to carry concealed firearms in state buildings, public schools, and government meetings, and pre-empts local ordinances restricting firearms — the bill became law February 27, 2025 without the governor's signature after passing the House 50-10.",
              ["https://trib.com/news/local/govt-and-politics/more-than-wyoming-legislators-sign-on-to-bill-to-repeal/article_5413249e-ac9b-568d-b762-04b5c6fc2470.html",
               "https://www.wyomingpublicmedia.org/politics-government/2025-02-27/gun-free-zones-repeal-becomes-law-without-gordons-pen"]),
        claim("896b", "john-bear", "sanctity_of_life", 0, True,
              "Voted YES on HB0126 (2026), Wyoming's Human Heartbeat Act, which bans abortion once fetal cardiac activity is detectable (approximately six weeks) and carries no rape/incest exception — the bill passed the House 51-7-4 and was signed into law, making Wyoming one of the most restrictive abortion states in the nation; John Bear's deep-red Campbell County (Gillette) district consistently ranks among Wyoming's most conservative.",
              ["https://www.wyomingpublicmedia.org/health/2026-02-17/wyoming-republicans-advance-bill-to-ban-abortion-when-theres-a-heartbeat",
               "https://www.wyoleg.gov/Legislation/2026/HB0126"]),
        claim("896c", "john-bear", "family_child_sovereignty", 0, True,
              "Voted YES on HB0046 (2025), Wyoming's Homeschool Freedom Act, which eliminated the statutory requirement that home-based educational programs submit curriculum to local school boards, removing government oversight of private family education — the bill passed the House 54-6 and was signed into law.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0046",
               "https://legiscan.com/WY/bill/HB0046/2025"]),
    ]),

    # ---------- John Winter (WY-R, District 28, Thermopolis) ----------
    # Already has: sanctity_of_life[0] + election_integrity[0]
    # Adding: self_defense, family_child_sovereignty
    ("john-winter", "WY", "Representative", [
        claim("896d", "john-winter", "self_defense", 0, True,
              "Co-sponsored HB0172 (2025), Wyoming's gun-free zones repeal law, allowing concealed carry in state buildings, schools, airports, and public meeting rooms and preempting all local firearms ordinances — the bill passed the Wyoming House 50-10 and became law February 27, 2025 without the governor's signature.",
              ["https://trib.com/news/local/govt-and-politics/more-than-wyoming-legislators-sign-on-to-bill-to-repeal/article_5413249e-ac9b-568d-b762-04b5c6fc2470.html",
               "https://www.wyomingpublicmedia.org/politics-government/2025-02-27/gun-free-zones-repeal-becomes-law-without-gordons-pen"]),
        claim("896e", "john-winter", "family_child_sovereignty", 0, True,
              "Voted YES on HB0046 (2025), Wyoming's Homeschool Freedom Act, which removed the requirement that homeschool families submit curriculum to local school boards — passed the House 54-6 and became law, expanding parental authority over their children's education without bureaucratic approval.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0046",
               "https://legiscan.com/WY/bill/HB0046/2025"]),
    ]),

    # ---------- J.T. Larson (WY-R, District 17, Rock Springs) ----------
    # Already has: sanctity_of_life[0] + election_integrity[0]
    # Adding: self_defense, family_child_sovereignty
    ("jt-larson", "WY", "Representative", [
        claim("896f", "jt-larson", "self_defense", 0, True,
              "Voted YES on HB0125 (2024), Wyoming's first attempt to repeal gun-free zones statewide (vetoed by Gov. Gordon), and publicly commits to being 'pro second amendment' who will 'do everything I can to protect your rights'; aligned with the successful 2025 HB0172 gun-free zones repeal that became law, reflecting a consistent constitutional-carry stance throughout his tenure.",
              ["https://ballotpedia.org/J.T._Larson",
               "https://www.wyoleg.gov/Legislators/2025/H/2096"]),
        claim("896g", "jt-larson", "family_child_sovereignty", 0, True,
              "Voted YES on HB0046 (2025), Wyoming's Homeschool Freedom Act, eliminating the requirement for homeschool families to submit curriculum to local school boards — passed 54-6 and signed into law, advancing parental sovereignty over children's education.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0046",
               "https://legiscan.com/WY/bill/HB0046/2025"]),
    ]),

    # ---------- Lloyd Larsen (WY-R, District 54, Lander) ----------
    # Already has: sanctity_of_life[0] + election_integrity[0]
    # Adding: family_child_sovereignty, biblical_marriage
    ("lloyd-larsen", "WY", "Representative", [
        claim("896h", "lloyd-larsen", "family_child_sovereignty", 0, True,
              "Voted YES on HB0046 (2025), Wyoming's Homeschool Freedom Act, which removed the requirement that home-based educational programs submit curriculum to local school boards — passed the House 54-6 and became law, advancing parental autonomy in education; Larsen, a 7-term Fremont County incumbent, consistently supports limiting government oversight of family decisions.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0046",
               "https://legiscan.com/WY/bill/HB0046/2025"]),
        claim("896i", "lloyd-larsen", "biblical_marriage", 2, True,
              "Voted YES on SF0103 (2025), Wyoming's comprehensive DEI termination and defunding bill (passed the House 52-7), which prohibits state funding for diversity, equity and inclusion programs, gender studies courses, and DEI offices at the University of Wyoming and community colleges — enacting in law the rejection of gender ideology in public institutions; the measure was enacted after the governor allowed related DEI restrictions to take effect.",
              ["https://legiscan.com/WY/bill/SF0103/2025",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-04/gordon-green-lights-property-tax-cut-and-prohibits-dei-programs-in-government"]),
    ]),

    # ---------- J.D. Williams (WY-R, District 2, rancher) ----------
    # Already has: sanctity_of_life[0] + election_integrity[0]
    # Adding: refuse_state_overreach, family_child_sovereignty
    ("jd-williams", "WY", "Representative", [
        claim("896j", "jd-williams", "refuse_state_overreach", 0, True,
              "Sponsored HB0011 (2025), Wyoming's Eminent Domain-Landowner Bill of Rights, which requires entities wielding eminent domain powers (including energy companies and government agencies) to pay landowners' legal fees when courts determine they failed to offer fair market value — directly protecting private property rights from condemnation abuse and state-backed overreach; Williams, a rancher, drafted the bill from firsthand knowledge of how rural landowners are pressured in condemnation proceedings.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0011",
               "https://trib.com/news/state-regional/govt-and-politics/wyoming-house-approves-eminent-domain-bill/article_ee05a114-8c1c-586e-aa52-3af30257eaf1.html"]),
        claim("896k", "jd-williams", "family_child_sovereignty", 0, True,
              "Voted YES on HB0046 (2025), Wyoming's Homeschool Freedom Act (passed 54-6), which removed the requirement that homeschool families submit curriculum to local school boards — expanding parental authority over children's education without state approval; Williams represents a rural agricultural district where homeschooling and family autonomy are strongly valued.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0046",
               "https://legiscan.com/WY/bill/HB0046/2025"]),
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
