#!/usr/bin/env python3
"""Push foreign-influence findings DOWN INTO the specific category-question
that the money compromises, so the impact is visible in the per-category
score (not just the total).

Mapping:
  - aipac money    → america_first[3] = False (q4 literally names AIPAC)
  - china money    → america_first[3] = False (q4 covers "foreign-linked
                                               PACs" and "foreign governments")
  - soros funding  → life[3] = False (Soros-funded DAs protect abortion
                                       provider access by declining
                                       prosecution; q4 = "rejects any public
                                       funding, subsidies, or legal protections
                                       for abortion providers or procedures")

We also stamp an `answer_footnote` on the affected cell so a visitor can
click through and see why the answer was flipped.

This script is idempotent: it only flips True → False (never the reverse),
and it records what it flipped in profile.category_overrides so we can
audit the chain.
"""
import json
import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"

# (adjustment_key, category_id, question_index)
LOBBY_TO_QUESTION = [
    ("aipac", "america_first", 3),
    ("china", "america_first", 3),
    ("soros", "life", 3),
]


def main():
    scorecard = json.loads(SCORECARD.read_text())
    today = date.today().isoformat()

    counts = {key: {"flipped": 0, "already_false": 0, "no_category": 0}
              for key, _, _ in LOBBY_TO_QUESTION}

    for c in scorecard["candidates"]:
        adj = (c.get("profile") or {}).get("score_adjustments") or {}
        if not adj:
            continue
        scores = c.get("scores") or {}
        for key, cat_id, q_idx in LOBBY_TO_QUESTION:
            if key not in adj:
                continue
            # CRITICAL: only flip the question to False when the adjustment
            # is a PENALTY (delta < 0 = candidate actually took the money).
            # Verified-zero candidates earn a +7 bonus and their answer to
            # the foreign-lobby question should stay True (they passed).
            delta = adj[key].get("delta", 0) or 0
            if delta >= 0:
                continue
            cat_arr = scores.get(cat_id)
            if not cat_arr or q_idx >= len(cat_arr):
                counts[key]["no_category"] += 1
                continue
            current = cat_arr[q_idx]
            if current is False:
                counts[key]["already_false"] += 1
                continue
            cat_arr[q_idx] = False
            counts[key]["flipped"] += 1

            # Record the override so we can audit/undo if needed.
            overrides = c.setdefault("profile", {}).setdefault("category_overrides", {})
            ck = f"{cat_id}.q{q_idx + 1}"
            overrides[ck] = {
                "from": current,
                "to": False,
                "reason": (
                    f"Auto-flipped by foreign-influence adjustment: "
                    f"profile.score_adjustments.{key} is set, which is direct evidence "
                    f"of the failure described by {cat_id} q{q_idx + 1}."
                ),
                "adjustment_key": key,
                "applied_on": today,
            }

            # Stamp an answer-footnote pointing to the existing adjustment-source
            # list so the per-cell evidence trail is intact.
            sources = (adj[key].get("sources") or [])[:3]
            if sources:
                fn_id = f"fn-cat-flip-{key}-{cat_id}-{q_idx + 1}"
                footnotes = c.setdefault("footnotes", {})
                if fn_id not in footnotes:
                    label_map = {
                        "aipac": "AIPAC / pro-Israel lobby donations",
                        "china": "CCP-linked / United Front-affiliated donations",
                        "soros": "Open Society / Soros-funded prosecutor network",
                    }
                    footnotes[fn_id] = {
                        "title": label_map.get(key, key.upper()),
                        "type": "evidence",
                        "summary": (
                            f"This candidate has documented foreign-influence "
                            f"funding logged under profile.score_adjustments.{key}. "
                            f"The question '{cat_id} q{q_idx + 1}' is therefore marked "
                            f"False — the candidate's own donor record is direct "
                            f"evidence of the failure described by the question."
                        ),
                        "sources": sources,
                    }
                answer_fns = c.setdefault("answer_footnotes", {})
                cell_key = f"{cat_id}_{q_idx}"
                cell_fns = answer_fns.setdefault(cell_key, [])
                if fn_id not in cell_fns:
                    cell_fns.append(fn_id)

    SCORECARD.write_text(json.dumps(scorecard, indent=2))

    print("Foreign-influence findings pushed into category-question answers:")
    for key, cat_id, q_idx in LOBBY_TO_QUESTION:
        c = counts[key]
        print(f"  {key:<6} → {cat_id} q{q_idx + 1}: "
              f"flipped {c['flipped']}, already False {c['already_false']}, "
              f"no category {c['no_category']}")


if __name__ == "__main__":
    main()
