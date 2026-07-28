#!/usr/bin/env python3
"""Correction for batch 867: fix two factual errors.

1. Paul Sherrell ps1: The "hang them" quote was about execution methods for
   death-row inmates (HB 1245, Feb 28 2023), NOT abortion providers. Replace
   with verified pro-life position from Southern Standard Oct 2022 interview.

2. Rick Scarbrough rs1/rs2/rs3: Scarbrough entered the legislature January 2025
   (first term; previously Clinton Police Chief for 16 years). Bills cited
   (HB786 April 2021, HB1 triggered June 2022, SAFE Act March 2023) all
   predated his service. Replace with his actual 2025-2026 legislative record.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()

# Claims to remove (by id)
REMOVE_IDS = {
    # Scarbrough — bills passed before his Jan 2025 first term
    "rick-scarbrough-sanctity_of_life-0-rs1",
    "rick-scarbrough-self_defense-1-rs2",
    "rick-scarbrough-biblical_marriage-2-rs3",
    # Sherrell — wrong context (execution methods bill, not abortion)
    "paul-sherrell-sanctity_of_life-1-ps1",
}

# Replacement claims (same helper format as batch-4)
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


REPLACEMENTS = {
    "rick-scarbrough": [
        # Documented from his actual 2025-2026 legislative record
        claim("rs1b", "rick-scarbrough", "border_immigration", 0, True,
              "Primary sponsor of HB 1707/SB 1952 (114th GA, 2025-2026), requiring all Tennessee "
              "courts to cooperate with DHS/ICE in federal immigration enforcement; judges who "
              "obstruct ICE detainer requests can be referred to the Board of Judicial Conduct and "
              "face removal from office. The House passed the bill in April 2026.",
              ["https://tennesseelookout.com/2026/04/03/tennessee-house-approves-bill-to-discipline-judges-who-obstruct-ice/",
               "https://wapp.capitol.tn.gov/apps/billsearch/BillSummaryPublic.aspx?BillNumber=HB1707&GA=114"]),
        claim("rs2b", "rick-scarbrough", "sanctity_of_life", 0, True,
              "Publicly identifies as 'boldly pro-life' on his campaign website, stating he 'believes "
              "all life is precious and should be protected.' Supports exceptions only to prevent the "
              "death of the mother. First-term legislator (January 2025) running on a fully pro-life "
              "platform.",
              ["https://ivoterguide.com/",
               "https://ballotpedia.org/Rick_Scarbrough_(Tennessee)"]),
    ],
    "paul-sherrell": [
        # Corrected: actual pro-life position from Southern Standard interview
        claim("ps1b", "paul-sherrell", "sanctity_of_life", 1, True,
              "In an October 2022 Southern Standard interview, Sherrell stated: 'Let's go back to "
              "what the Bible says. Life starts at conception… Abortion is bad because it kills a "
              "baby that can't defend itself.' He supports Tennessee's total abortion prohibition "
              "rather than partial restrictions, a posture consistent with the rubric's abolition "
              "(not restriction) standard.",
              ["https://www.southernstandard.com/top-stories/local-headlines/uselton-sherrell-directly-opposed-abortion/",
               "https://en.wikipedia.org/wiki/Abortion_in_Tennessee"]),
    ],
}


def main():
    scorecard = json.loads(SCORECARD.read_text())
    fixed = 0
    removed_total = 0
    added_total = 0

    for c in scorecard["candidates"]:
        slug = c.get("slug", "")
        existing = c.get("claims") or []

        # Remove bad claims
        before = len(existing)
        existing = [cl for cl in existing if cl.get("id") not in REMOVE_IDS]
        removed = before - len(existing)

        # Add replacements
        added = 0
        if slug in REPLACEMENTS:
            existing_ids = {cl.get("id") for cl in existing}
            for new_cl in REPLACEMENTS[slug]:
                if new_cl["id"] not in existing_ids:
                    existing.append(new_cl)
                    added += 1
                    # Update score for this category/qi
                    scores = c.get("scores") or {}
                    cat, qi, si = new_cl["category"], new_cl["question_idx"], new_cl["score_impact"]
                    if cat in scores and qi < len(scores[cat]):
                        scores[cat][qi] = si

        if removed or added:
            c["claims"] = existing
            prof = c.setdefault("profile", {}) or {}
            if not isinstance(prof, dict):
                prof = {}
                c["profile"] = prof
            prof["confidence"] = "evidence_curated"
            prof["last_curated"] = TODAY
            fixed += 1
            removed_total += removed
            added_total += added
            print(f"  ✓ {c.get('name','?'):<30} ({c.get('state','?')}) "
                  f"removed={removed} added={added} total_claims={len(existing)}")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print(f"\nFixed {fixed} candidates: removed {removed_total} bad claims, added {added_total} corrected claims")


if __name__ == "__main__":
    main()
