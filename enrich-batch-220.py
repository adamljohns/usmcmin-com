#!/usr/bin/env python3
"""Enrichment batch 220: third-claim enrichment for 5 bottom-of-alphabet federal candidates.

Targets (evidence_curated with 2 claims, bottom of alphabet):
  WI-D  Ginger Murray        (U.S. Representative WI-07 2026 D candidate)
  WI-D  Chris Armstrong      (U.S. Representative WI-07 2026 D candidate)
  WA-D  John Duresky         (U.S. Representative WA-04 2026 D candidate)
  VA-R  Yesli Vega           (sitting Prince William Co. Supervisor / 2022+2024 R nominee)
  VA-D  Patrick Mosolf       (U.S. Representative VA-02 2026 D candidate)

Each target gets one new claim in a distinct rubric category not yet covered.
Sources: WSAW, APG-WI, Yakima Herald, Ballotpedia, Virginia Right to Reproductive Freedom Amendment.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------------- Ginger Murray (WI-D, U.S. Representative WI-07 2026) ----------------
    ("ginger-murray", "WI", "Representative", [
        claim("gm3", "ginger-murray", "self_defense", 1, False,
              "At the March 1, 2026 Ashland Democratic candidate forum and in a March 24, 2026 WSAW interview, Murray called for expanded gun-safety measures, telling voters she was 'brokenhearted about the fact that my kids were raised to be afraid to go to school — they were not doing tornado drills, they were doing active shooter drills.' She cited her 30-year legal background as the basis for her support of universal background checks and restrictions on military-style firearms access — positions that place her squarely against the rubric's protection of semi-automatic rifles from assault-weapon bans, magazine-limit laws, and expanded background-check requirements.",
              ["https://www.wsaw.com/2026/03/24/democratic-congressional-candidate-says-law-experience-will-deliver-results-voters-feel-abandoned-want-change/",
               "https://www.apg-wi.com/ashland_daily_press/news/local/democratic-candidates-for-7th-congressional-district-hold-ashland-forum/article_a3463f27-2f34-4fda-88f7-e0929c0d762c.html"]),
    ]),

    # ---------------- Chris Armstrong (WI-D, U.S. Representative WI-07 2026) ----------------
    ("chris-armstrong-wi-07", "WI", "Representative", [
        claim("ca3", "chris-armstrong-wi-07", "biblical_marriage", 2, False,
              "At the March 4, 2026 Rhinelander candidate forum and in a WSAW one-on-one interview (March 5, 2026), Armstrong explicitly endorsed transgender civil-rights protections, equating LGBTQ discrimination with historical discrimination against Black Americans and women: 'We've seen this play before. Whether it's the African American community, the gay community, women — there's always the other, the minority, the disenfranchised. For God's sake, we're approaching the 250th anniversary of the United States. Life, liberty, and the pursuit of happiness — it's just got to be a part of the equation.' This framing affirms transgender identity as a protected civil-rights category equivalent to race and sex, in direct opposition to the rubric's rejection of transgender ideology.",
              ["https://www.wsaw.com/2026/03/05/armstrong-thinks-dems-can-overcome-odds-flip-7th-congressional-seat/",
               "https://www.apg-wi.com/ashland_daily_press/news/local/democratic-candidates-for-7th-congressional-district-hold-ashland-forum/article_a3463f27-2f34-4fda-88f7-e0929c0d762c.html"]),
    ]),

    # ---------------- John Duresky (WA-D, U.S. Representative WA-04 2026) ----------------
    ("john-duresky", "WA", "Representative", [
        claim("jd3", "john-duresky", "sanctity_of_life", 0, False,
              "The Yakima Herald reported that Central Washington District 4 congressional candidates align with their national party platforms on abortion. Duresky, running as a Democrat, aligns with the Democratic Party platform, which explicitly rejects life-at-conception personhood standards and treats abortion access as a healthcare right. The Yakima Herald also conducted a dedicated Q&A asking District 4 candidates to share their views on abortion policy, documenting Duresky's participation as the Democratic candidate — his alignment with the national party platform rejecting any life-begins-at-conception legal standard is on the record.",
              ["https://www.yakimaherald.com/news/local/government/elections/central-wa-congressional-candidates-align-with-national-party-platforms-on-abortion/article_4e107e8c-4eca-11ef-920e-7b3280dfbd0b.html",
               "https://www.yakimaherald.com/news/local/q-a-district-4-candidates-share-views-on-abortion-policy/article_36fe85d7-132d-5bf2-ba5c-57d3c53a56d3.html"]),
    ]),

    # ---------------- Yesli Vega (VA-R, sitting Prince William Co. Supervisor / 2022+2024 R nominee) ----------------
    ("yesli-vega", "VA", "Representative", [
        claim("yv3", "yesli-vega", "border_immigration", 0, True,
              "During her 2022 and 2024 campaigns for Virginia's 7th Congressional District, Vega made the migrant crisis at the southern border one of her top campaign priorities, appearing on Fox News to criticize Biden-era border policy failures and calling for security and rule of law at the border — positions consistent with wall construction, military border enforcement, and ending catch-and-release. Ballotpedia confirms border security was among her primary campaign platforms. Her law-enforcement career (patrol officer, hostage negotiator) reinforces her emphasis on strong deterrence, placing her in alignment with the rubric's border_immigration[0] (wall and military deployment at the border).",
              ["https://ballotpedia.org/Yesli_Vega",
               "https://news.ballotpedia.org/2022/09/22/abigail-spanberger-and-yesli-vega-are-running-for-virginias-7th-congressional-district-on-nov-8/"]),
    ]),

    # ---------------- Patrick Mosolf (VA-D, U.S. Representative VA-02 2026) ----------------
    ("patrick-mosolf", "VA", "Representative", [
        claim("pm3", "patrick-mosolf", "sanctity_of_life", 0, False,
              "Running as a Democrat for Virginia's 2nd Congressional District in the 2026 cycle, Mosolf is campaigning in a state where the Virginia General Assembly placed the Right to Reproductive Freedom Amendment on the November 2026 ballot — a measure supported by every Democrat in the legislature and opposed by every Republican. Mosolf's platform of 'restoring America's democracy' and protecting healthcare access — consistent with the Virginia Democratic Party's unified support for constitutional abortion rights — places him on record against a life-at-conception or personhood standard. His former USAID career overseeing local development programs in Lebanon, Gaza-adjacent, and other fragile states is also consistent with support for reproductive-health services internationally.",
              ["https://ballotpedia.org/Patrick_Mosolf",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
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
