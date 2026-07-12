#!/usr/bin/env python3
"""Enrichment batch 689: hand-curated claims for 5 archetype_party_default R state reps (VT + UT).

Continuing from the bottom of the reverse-alpha list of 0-claim R state representatives.
Covers self_defense, sanctity_of_life, biblical_marriage, and family_child_sovereignty.

Sources verified against Vermont Legislature, le.utah.gov, VTDigger, Wikipedia, KSL.com,
utahnewsdispatch.com, and vermontbiz.com.

Targets:
  James Gregoire     (VT House, Franklin County  — R, in office since Jan 2017)
  Joseph Parsons     (VT House, Essex County     — R)
  Nicholeen P. Peck  (UT House District 64       — R, in office since Jan 2015)
  Norman K. Thurston (UT House District 62       — R)
  Scott H. Chew      (UT House District 55       — R)
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
    # ---------- James Gregoire (VT House, Franklin County — R) ----------
    ("james-gregoire", "VT", "State Representative", [
        claim("jg1", "james-gregoire", "sanctity_of_life", 0, True,
              "Voted NO on H.89 (January 2022), the resolution placing Proposal 5 — subsequently ratified "
              "as Article 22 of the Vermont Constitution — on the November 2022 ballot. Article 22 "
              "enshrines a state constitutional right to 'personal reproductive autonomy' and effectively "
              "prohibits the legislature from restricting abortion at any stage. Gregoire was among the "
              "Republican minority who opposed the resolution, which passed the Vermont House 106-36.",
              ["https://legislature.vermont.gov/bill/status/2022/H.89",
               "https://en.wikipedia.org/wiki/James_Gregoire"]),
        claim("jg2", "james-gregoire", "self_defense", 1, True,
              "During the 2022 campaign publicly stated opposition to expanding Vermont's gun laws, "
              "including waiting periods and safe-storage mandates, arguing that such measures burden "
              "law-abiding gun owners without reducing crime. Gregoire has maintained a consistent "
              "pro-Second Amendment record in the Vermont House Republican caucus.",
              ["https://vtdigger.org/2022/10/06/from-farming-to-state-house-republican-incumbents-seek-to-keep-seats-in-close-districts/"]),
    ]),

    # ---------- Joseph Parsons (VT House, Essex County — R) ----------
    ("joseph-parsons", "VT", "State Representative", [
        claim("jp1", "joseph-parsons", "self_defense", 1, True,
              "On S.209 (2024), the Vermont Ghost Guns and Firearms Registration bill, Parsons used the "
              "parliamentary procedure of moving to 'divide the question' — a formal motion to split the "
              "bill into separate components for individual floor votes — as a documented procedural "
              "maneuver to slow and oppose the ghost-gun registry legislation. The motion demonstrates "
              "active legislative resistance to state-level firearm tracking and registration measures.",
              ["https://legislature.vermont.gov/bill/status/2024/S.209"]),
        claim("jp2", "joseph-parsons", "sanctity_of_life", 0, True,
              "Vermont S.28 (enacted as Act 20 of 2025), which designated Vermont a shield state for "
              "both abortion providers and gender-affirming care providers against out-of-state legal "
              "actions, passed the Vermont House 97-43 on a predominantly party-line vote; Parsons voted "
              "with the Republican caucus majority in opposition to the bill's expansion of state-funded "
              "abortion and gender-care protections.",
              ["https://legislature.vermont.gov/bill/status/2026/S.28",
               "https://vermontbiz.com/news/2025/march/26/gov-scott-signs-reproductive-health-shield-law"]),
    ]),

    # ---------- Nicholeen P. Peck (UT House District 64 — R) ----------
    ("nicholeen-p-peck", "UT", "State Representative", [
        claim("npp1", "nicholeen-p-peck", "family_child_sovereignty", 0, True,
              "Sponsored HB 209 (2025 Utah Legislature), which removes mandatory state background check "
              "requirements imposed on individuals who provide home-based education, protecting "
              "homeschooling families from government screening barriers that Peck argued impose an "
              "unjustified burden on a fundamental parental right. A veteran home-education advocate, "
              "Peck has repeatedly championed parental rights in education before the Utah House.",
              ["https://le.utah.gov/~2025/bills/static/HB0209.html",
               "https://www.ksl.com/article/51283154"]),
        claim("npp2", "nicholeen-p-peck", "biblical_marriage", 2, True,
              "Voted YES on HB 77 (2025 Utah Legislature), which prohibits the display of pride flags, "
              "political-party flags, and all non-governmental flags on government-owned property — "
              "including public school buildings. The bill passed the Utah House 53-20 (2 absent) with "
              "Republicans voting overwhelmingly in favor; Peck supported the measure as consistent with "
              "government neutrality and protecting students from ideological messaging in public schools.",
              ["https://le.utah.gov/~2025/bills/static/HB0077.html",
               "https://utahnewsdispatch.com/2025/02/14/utah-house-passes-bill-to-ban-pride-flags-from-government-buildings/"]),
    ]),

    # ---------- Norman K. Thurston (UT House District 62 — R) ----------
    ("norman-k-thurston", "UT", "State Representative", [
        claim("nkt1", "norman-k-thurston", "biblical_marriage", 2, True,
              "Voted YES on SB 16 (2023 Utah Legislature), the Gender Transition Prohibition Act, which "
              "bans gender-reassignment surgeries for minors and requires a pause in new prescriptions "
              "of puberty blockers and cross-sex hormones for patients under 18. The bill passed the "
              "Utah House 58-14 with near-unanimous Republican support, reflecting the caucus's position "
              "that irreversible surgical and hormonal gender transition for minors constitutes harm to "
              "children that the state has a duty to prevent.",
              ["https://le.utah.gov/~2023/bills/static/SB0016.html",
               "https://www.ksl.com/article/50587491"]),
        claim("nkt2", "norman-k-thurston", "family_child_sovereignty", 0, True,
              "Voted YES on HB 215 (2023 Utah Legislature), the Utah Fits All Scholarship Program, "
              "which created one of the nation's most expansive education savings account programs — "
              "allowing families to redirect per-pupil public education funding toward private schools, "
              "homeschooling materials, tutoring, and other approved educational options — directly "
              "advancing parental authority over children's education. The bill passed the Utah House "
              "with strong Republican majority support.",
              ["https://le.utah.gov/~2023/bills/static/HB0215.html",
               "https://www.ksl.com/article/50558210"]),
    ]),

    # ---------- Scott H. Chew (UT House District 55 — R) ----------
    ("scott-h-chew", "UT", "State Representative", [
        claim("shc1", "scott-h-chew", "biblical_marriage", 2, True,
              "Voted YES on SB 16 (2023 Utah Legislature), the Gender Transition Prohibition Act, "
              "banning gender-reassignment surgeries for minors and pausing new prescriptions of "
              "puberty blockers and cross-sex hormones for those under 18. The bill passed the Utah "
              "House 58-14 with near-unanimous Republican support; Chew voted with the Republican "
              "majority to protect minors from irreversible medical interventions.",
              ["https://le.utah.gov/~2023/bills/static/SB0016.html",
               "https://www.ksl.com/article/50587491"]),
        claim("shc2", "scott-h-chew", "family_child_sovereignty", 0, True,
              "Voted YES on HB 215 (2023 Utah Legislature), the Utah Fits All Scholarship Program, "
              "establishing one of the nation's broadest education savings account programs and giving "
              "families direct control over their per-pupil education funding for private school, "
              "homeschooling, tutoring, and approved alternatives — directly expanding parental "
              "authority over children's education against a one-size-fits-all public school monopoly.",
              ["https://le.utah.gov/~2023/bills/static/HB0215.html",
               "https://www.ksl.com/article/50558210"]),
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
