#!/usr/bin/env python3
"""Enrichment batch 746: corrects two factual errors from batch 745.

Batch 745 attributed votes on HB 218 (2022) and SB 202 (2021) to
Jason Dickerson and Derek Mallow, neither of whom was in office at
the time of those votes:

  Jason Dickerson (SD-21, Cherokee Co.) — took office October 14, 2025,
    after winning the SD-21 special election runoff (61.5%) on Sept 23, 2025.
    No vote record on any major bill yet.

  Derek Mallow (SD-2, Savannah/Chatham Co.) — took office January 9, 2023
    (first elected November 2022). Was not present for HB 218 (2022) or
    SB 202 (2021).

This batch:
  1. Removes the two wrong claims for each senator (4 total).
  2. Replaces them with accurate evidence-based claims.

For Dickerson: uses his documented campaign platform statements (the only
available record), since he was sworn in October 2025 and has not yet voted
on any major social-issue legislation.

For Mallow: uses his confirmed 2023-session vote on SB 140 (transgender
youth care ban — Mallow voted YES on Motion to Table, i.e., voted to kill
the bill), and his documented public opposition to SB 202 effects via his
statement on Bryan County voter challenges and his vote against SB 189.

Sources: Georgia Recorder, GPB News, Georgia Senate Press Office,
ballotpedia.org, tribuneledgernews.com, georgiarecorder.com.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()

# Claim IDs introduced by batch 745 that are factually wrong and must be removed.
WRONG_IDS = {
    "jason-dickerson-self_defense-0-jd1",     # Falsely attributed HB 218 (2022) vote
    "jason-dickerson-election_integrity-0-jd2", # Falsely attributed SB 202 (2021) vote
    "derek-mallow-self_defense-0-dm1",          # Falsely attributed HB 218 (2022) vote
    "derek-mallow-election_integrity-0-dm2",    # Falsely attributed SB 202 (2021) vote
}


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


# Replacement claims — each replaces one or more removed wrong claims.
# (slug, state, office_keyword, claims-to-add, scores-to-reset)
# scores-to-reset: list of (category, q_idx, value) to explicitly set after
# removing claims that previously set them.
CORRECTIONS = [
    # ---- Jason Dickerson (GA SD-21, Cherokee Co., took office Oct 2025) ----
    ("jason-dickerson", "GA", "Senator", [
        claim("jd1c", "jason-dickerson", "sanctity_of_life", 0, True,
              "Ran for Georgia SD-21 in the September 2025 special election on an explicitly pro-life platform: his campaign website pledged he 'will fight to protect life' and framed the race around a 'family first agenda' rooted in 'faith and service.' Dickerson won the runoff 61.5% against Democrat Debra Shigley, filling the seat of Sen. Brandon Beach (appointed U.S. Treasurer by President Trump). He has been in office since October 14, 2025 and has not yet voted on a major abortion bill.",
              ["https://ballotpedia.org/Jason_Dickerson_(Georgia)",
               "https://www.tribuneledgernews.com/local_news/jason-dickerson-announces-run-for-georgia-senate/article_6a27b899-881a-4a5c-8b8b-a7ceb05a4b3f.html",
               "https://georgiarecorder.com/2025/09/23/live-results-georgia-voters-settle-state-senate-runoff-that-has-drawn-national-attention/"]),
        claim("jd2c", "jason-dickerson", "self_defense", 0, True,
              "Declared Second Amendment advocacy as a cornerstone of his October 2025 campaign for Georgia SD-21, pledging to 'defend our Second Amendment gun rights' as part of protecting 'our conservative way of life.' Dickerson won the seat in a closely-watched September 2025 runoff. He took office October 14, 2025 and does not yet have a voting record on gun legislation.",
              ["https://ballotpedia.org/Jason_Dickerson_(Georgia)",
               "https://www.tribuneledgernews.com/local_news/jason-dickerson-announces-run-for-georgia-senate/article_6a27b899-881a-4a5c-8b8b-a7ceb05a4b3f.html"]),
        claim("jd3c", "jason-dickerson", "election_integrity", 0, True,
              "Pledged to 'secure our border and elections' as a central campaign commitment in his 2025 SD-21 race, running on a platform emphasizing election security alongside fiscal conservatism and family values. He has been in office since October 14, 2025 and has not yet voted on a major election-integrity bill.",
              ["https://ballotpedia.org/Jason_Dickerson_(Georgia)",
               "https://georgiarecorder.com/2025/09/23/live-results-georgia-voters-settle-state-senate-runoff-that-has-drawn-national-attention/"]),
    ], []),  # no score overrides needed; jd2c and jd3c re-set same values already written by wrong claims

    # ---- Derek Mallow (GA SD-2, Savannah, took office Jan 2023) ----
    ("derek-mallow", "GA", "Senator", [
        claim("dm1c", "derek-mallow", "biblical_marriage", 2, False,
              "Voted YES on the March 21, 2023 Motion to Table Georgia SB 140 (Vulnerable Child Protection Act) — effectively voting to kill the bill that banned gender-affirming hormone therapy and surgery for minors under 18; the motion failed (the bill passed 31-21 along party lines) but Mallow's YES vote placed him on record opposing restrictions on transgender care for minors, contradicting the rubric's rejection of transgender ideology.",
              ["https://www.gpb.org/news/2023/03/21/lawmakers-emotions-run-high-senate-approves-bill-restricting-gender-affirming-care",
               "https://georgiarecorder.com/2023/03/22/georgia-legislature-sends-bill-to-limit-transgender-care-for-minors-to-governor/",
               "https://ballotpedia.org/Derek_Mallow"]),
        claim("dm2c", "derek-mallow", "election_integrity", 0, False,
              "Publicly condemned Georgia SB 202 (Election Integrity Act of 2021) and voted against SB 189 (2023 voter-registration challenge expansion), stating: 'The voter challenges happening in Bryan County today are a direct result of Senate Bill 202 and Senate Bill 189 and I warned about these consequences when I spoke against SB 189.' Mallow has been a consistent opponent of the post-2020 election-security framework in Georgia, rejecting the rubric's support for voter-ID requirements and secure election administration.",
              ["https://senatepress.net/sen-derek-mallow-statement-on-bryan-county-hearing-on-voter-challenges.html",
               "https://ballotpedia.org/Derek_Mallow",
               "https://en.wikipedia.org/wiki/Georgia_Election_Integrity_Act_of_2021"]),
    ], [("self_defense", 0, False)]),  # batch 745 wrongly set self_defense[0]=False; keep False (correct for D)
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
            continue
        return c
    return None


def main():
    scorecard = json.loads(SCORECARD.read_text())
    total_removed = 0
    total_added = 0

    # Step 1: global removal pass for all wrong claims
    for c in scorecard["candidates"]:
        existing = c.get("claims") or []
        before = len(existing)
        c["claims"] = [cl for cl in existing if cl.get("id") not in WRONG_IDS]
        removed = before - len(c["claims"])
        if removed:
            total_removed += removed
            print(f"  - Removed {removed} wrong claim(s) from {c['name']} ({c.get('state')})")

    # Step 2: add correct replacement claims
    for slug, state, office_keyword, new_claims, score_overrides in CORRECTIONS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  ✗ NOT FOUND: slug={slug} state={state}")
            continue
        existing = m.get("claims") or []
        existing_ids = {cl.get("id") for cl in existing}
        to_add = [cl for cl in new_claims if cl["id"] not in existing_ids]
        existing.extend(to_add)
        m["claims"] = existing

        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY

        scores = m.get("scores") or {}
        for cl in to_add:
            cat, qi, si = cl["category"], cl["question_idx"], cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        for cat, qi, val in score_overrides:
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = val

        total_added += len(to_add)
        print(f"  + {m['name']:<26} ({state}) +{len(to_add)} corrected claims")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: removed {total_removed} wrong claims, added {total_added} corrected claims")


if __name__ == "__main__":
    main()
