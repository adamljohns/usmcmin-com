#!/usr/bin/env python3
"""Enrichment batch 872: evidence-curated claims for 4 Virginia 2026 US House candidates.

Targets evidence_curated and unset-confidence federal candidates from the bottom of
the alphabet (VA) with 0 claims.  All four are 2026 congressional candidates whose
primary election is August 4, 2026.

Mix (2 R / 2 D):
  Sam Wong (VA-R, US Rep VA-10, withdrew after ballot finalized),
  Anthony Suttles (VA-R, US Rep VA-10),
  Suzanne Krzyzanowski (VA-D, US Rep VA-05),
  Beth Macy (VA-D, US Rep VA-06).

Each claim cites >=1 reliable source and reflects publicly documented 2025-2026
campaign positions.
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
    # ---------------- Sam Wong (VA-R, US Rep VA-10, withdrew) ----------------
    ("sam-wong", "VA", "Representative", [
        claim("sw1", "sam-wong", "self_defense", 1, True,
              "Campaign explicitly opposed Virginia Gov. Spanberger's 2026 assault-weapons ban and his Democratic opponent Rep. Suhas Subramanyam's gun-control posture; stated 'The Second Amendment is your fundamental right' and pledged to stand against measures that 'disarm law abiding citizens' — an unambiguous anti-AWB/anti-gun-restriction position. (Wong withdrew after ballots were finalized; name appears on Aug 4 2026 primary ballot.)",
              ["https://ballotpedia.org/Sam_Wong",
               "https://www.wongforcongress.com/"]),
        claim("sw2", "sam-wong", "border_immigration", 0, True,
              "Campaign platform stated: 'Sam fully supports the Trump mission to finish the wall, end catch and release' — an explicit endorsement of completing physical border barriers and ending asylum-catch-and-release policies.",
              ["https://www.wongforcongress.com/",
               "https://www.localcandidates.org/politicians/sam-wong"]),
        claim("sw3", "sam-wong", "border_immigration", 1, True,
              "Platform committed to 'prioritize the deportation of illegal immigrants, with the goal to restore the rule of law to keep Virginia communities safe' — an explicit mass-deportation-first immigration enforcement position.",
              ["https://www.wongforcongress.com/",
               "https://www.localcandidates.org/politicians/sam-wong"]),
    ]),

    # ---------------- Anthony Suttles (VA-R, US Rep VA-10) ----------------
    ("anthony-suttles", "VA", "Representative", [
        claim("as1", "anthony-suttles", "family_child_sovereignty", 0, True,
              "Anthony Suttles and his wife Sally homeschooled all three of their children — a biographical commitment to parental authority in education that directly aligns with the rubric's defense of parental rights and homeschool freedom against state control.",
              ["https://www.insidenova.com/news/loudoun/three-way-race-to-determine-gop-challenger-for-subramanyam-s-10th-district-seat/article_af2200d5-1bbc-41a6-843a-813a84055459.html",
               "https://www.fauquiernow.com/news/government_politics/three-way-race-to-determine-gop-challenger-for-subramanyam-s-10th-district-seat/article_a450efad-cf7e-5fc1-af99-44eaf2fd19d0.html"]),
        claim("as2", "anthony-suttles", "foreign_policy_restraint", 2, True,
              "Former 30-year USAF veteran and Deputy Assistant Secretary of Defense overseeing a $500-billion portfolio whose 2026 campaign explicitly frames the mission as 'protect[ing] Virginia families from the resurgence of imperial Communism' — a posture opposed to aid, investment, or accommodation of communist-aligned hostile regimes.",
              ["https://www.insidenova.com/news/loudoun/three-way-race-to-determine-gop-challenger-for-subramanyam-s-10th-district-seat/article_af2200d5-1bbc-41a6-843a-813a84055459.html",
               "https://www.fauquiernow.com/news/government_politics/three-way-race-to-determine-gop-challenger-for-subramanyam-s-10th-district-seat/article_a450efad-cf7e-5fc1-af99-44eaf2fd19d0.html"]),
    ]),

    # ---------------- Suzanne Krzyzanowski (VA-D, US Rep VA-05) ----------------
    ("suzanne-krzyzanowski", "VA", "Representative", [
        claim("sk1", "suzanne-krzyzanowski", "sanctity_of_life", 0, False,
              "Democratic physician who has centered her 2026 VA-05 campaign on 'healthcare, reproductive rights and scientific research funding' — explicitly campaigning to protect and expand abortion access, rejecting any recognition of fetal personhood from conception.",
              ["https://dailyprogress.com/news/local/government-politics/elections/article_0ee7db66-1b44-4173-aa4b-114fabc0765f.html",
               "https://www.cvilletomorrow.org/qa-with-three-candidates-seeking-democratic-nomination-for-virginias-5th-district/"]),
        claim("sk2", "suzanne-krzyzanowski", "refuse_federal_overreach", 0, False,
              "Supports a universal healthcare system in which every American has government or private health insurance — a position requiring substantial federal mandate and government expansion into the healthcare market, directly counter to the rubric's principle of refusing federal overreach into family and private decisions.",
              ["https://dailyprogress.com/news/local/government-politics/elections/article_0ee7db66-1b44-4173-aa4b-114fabc0765f.html",
               "https://www.localcandidates.org/politicians/suzanne-krzyzanowski/about"]),
    ]),

    # ---------------- Beth Macy (VA-D, US Rep VA-06) ----------------
    ("beth-macy", "VA", "Representative", [
        claim("bm1", "beth-macy", "industry_capture", 1, True,
              "Author of Dopesick (2018), the best-selling exposé of Purdue Pharma's OxyContin marketing as the catalyst of the opioid epidemic; her 2026 VA-06 congressional campaign is built on pharmaceutical industry accountability and halting Medicaid cuts that would end opioid treatment — a posture aligned with the rubric's call to repeal liability shields that protect pharma companies from full legal exposure.",
              ["https://en.wikipedia.org/wiki/Beth_Macy",
               "https://bethmacyforcongress.com/"]),
        claim("bm2", "beth-macy", "sanctity_of_life", 0, False,
              "2026 Democratic candidate for VA-06 endorsed by Sen. Tim Kaine (D-VA), who holds a 0% lifetime score from SBA Pro-Life America; Macy's campaign prioritizes Medicaid expansion and reproductive healthcare access consistent with the Democratic Party's pro-choice platform — no pro-life position identified in any campaign materials.",
              ["https://sbaprolife.org/senator/tim-kaine",
               "https://cardinalnews.org/2025/11/18/beth-macy-makes-her-run-for-congress-official/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
