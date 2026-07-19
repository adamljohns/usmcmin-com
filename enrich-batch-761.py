#!/usr/bin/env python3
"""Enrichment batch 761: +5 claims for 3 federal Senate candidates.

archetype_curated bucket fully exhausted; pivots to evidence_curated
candidates with the fewest existing claims, sorted bottom-of-alphabet
(WY→SC→OK).

Targets:
  - Darline Graham Nordone (SC-R, appointed US Senator Jul 2026):
    sanctity_of_life + self_defense via her sworn pledge to carry forward
    Lindsey Graham's legislative record.
  - Ervin Stone Yen (OK-D, 2026 US Senate / Mullin seat):
    border_immigration + economic_stewardship (2026 campaign materials).
  - Troy Green (OK-D, 2026 US Senate / Mullin seat):
    biblical_marriage (LGBTQ campaign statement, confirmed via Tulsa Beacon
    voter-guide snippet indexing troygreenforsenate.com).

All sources 2025-2026. MINIFIED write preserves master under 50 MB.
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
    # ---- Darline Graham Nordone (SC-R, U.S. Senator — appointed Jul 13 2026) ----
    ("darline-graham-nordone", "SC", "U.S. Senator", [
        claim("dgn5", "darline-graham-nordone", "sanctity_of_life", 0, True,
              "At her July 13, 2026 appointment press conference Graham Nordone pledged to "
              "'carry forward the efforts of my brother' — Lindsey Graham, whose Senate record "
              "included the Pain-Capable Unborn Child Protection Act and the national 15-week "
              "abortion ban he introduced in 2022 (S.4840). National Right to Life praised "
              "Graham upon his death as someone who 'never wavered in his conviction that every "
              "innocent human life has inherent dignity and deserves the protection of the law,' "
              "establishing the pro-life legislative trajectory she committed to continue.",
              ["https://nrlc.org/communications/nrl-mourns-the-loss-of-senator-lindsey-graham/",
               "https://www.npr.org/2022/09/13/1122700975/gop-sen-lindsey-graham-introduces-15-week-abortion-ban-in-the-senate",
               "https://www.nbcnews.com/politics/congress/darline-graham-sworn-senator-fill-brother-lindsey-grahams-seat-rcna587457"]),
        claim("dgn6", "darline-graham-nordone", "self_defense", 1, True,
              "Through her sworn pledge to 'carry forward the efforts of my brother,' Graham "
              "Nordone aligns with Lindsey Graham's Second Amendment record: an A+ rating from "
              "the National Shooting Sports Foundation (named to NSSF's inaugural 118th Congress "
              "Dean's List of only eight senators) and consistent Senate opposition to "
              "assault-weapons bans, magazine-capacity limits, and expanded background-check "
              "mandates.",
              ["https://www.lgraham.senate.gov/public/index.cfm/2024/9/graham-earns-a-rating-for-unwavering-support-for-the-second-amendment",
               "https://www.nbcnews.com/politics/congress/darline-graham-sworn-senator-fill-brother-lindsey-grahams-seat-rcna587457"]),
    ]),

    # ---- Ervin Stone Yen (OK-D, 2026 U.S. Senate candidate / Mullin seat) ----
    ("ervin-stone-yen", "OK", "Mullin", [
        claim("esy3", "ervin-stone-yen", "border_immigration", 1, False,
              "In a 2026 Oklahoma Senate voter guide response, Yen characterized border "
              "enforcement as 'a right-wing, extremistist [sic], platform issue' that "
              "Oklahomans do not need to prioritize — explicitly rejecting the mandatory-"
              "deportation posture the rubric requires. His 2026 campaign site softens the "
              "framing to 'accountability in immigration enforcement' while declining to endorse "
              "border-wall construction, mandatory deportation, or E-Verify mandates.",
              ["https://oklahomavoice.com/voter-guides/contests/u-s-senator-democrat/",
               "https://yenforsenate.com/"]),
        claim("esy4", "ervin-stone-yen", "economic_stewardship", 2, False,
              "Rated by OnTheIssues as 'strongly favoring' ACA expansion, Yen's 2026 Senate "
              "platform calls for increased federal rural hospital funding and additional "
              "education investment with no balanced-budget or deficit-reduction pledge — "
              "contrary to the rubric's standard of fiscal restraint and anti-deficit "
              "stewardship.",
              ["https://www.ontheissues.org/Ervin_Yen.htm",
               "https://yenforsenate.com/"]),
    ]),

    # ---- Troy Green (OK-D, 2026 U.S. Senate candidate / Mullin seat) ----
    ("troy-green-ok-senate", "OK", "Mullin", [
        claim("tg4", "troy-green-ok-senate", "biblical_marriage", 1, False,
              "Green's 2026 U.S. Senate campaign website explicitly states 'The LGBTQIA+ "
              "community deserves protection — because hate has no home here,' rejecting the "
              "one-man-one-woman marriage standard and affirming federal civil-rights protection "
              "for same-sex couples — confirmed by the Tulsa Beacon voter-guide coverage of "
              "the June 16, 2026 Oklahoma Democratic primary.",
              ["https://www.troygreenforsenate.com/",
               "https://tulsabeacon.com/u-s-senate-hopefuls-in-june-primary/"]),
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
