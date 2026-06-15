#!/usr/bin/env python3
"""Enrichment batch 231: third-claim enrichment for 5 federal Senate candidates.

Targets evidence_curated U.S. Senate candidates (2 claims each) from the
bottom of the alphabet: NH, MT, MN, IL, IA.  Each claim adds a distinct
rubric category not already covered by the candidate's prior two claims.

Candidates: Karishma Manzur (NH-D), Lee Calhoun (MT-R), Adam Schwarze (MN-R),
Jeannie Evans (IL-R), Joshua Smith (IA-R).
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


TARGETS = [
    # ---------- Karishma Manzur (NH-D, U.S. Senator 2026) ----------
    ("karishma-manzur", "NH", "Senator", [
        claim("km3", "karishma-manzur", "sanctity_of_life", 0, False,
              "Campaigns on ensuring abortion access is 'safe, legal, and accessible' as a core healthcare right; explicitly supports bodily autonomy and transgender healthcare access; opposes any federal limit on reproductive choice — rejecting the life-at-conception/personhood standard the rubric requires.",
              ["https://www.karishmaforsenate.com/our-priorities",
               "https://www.nhpr.org/nh-news/2025-08-20/nh-senate-race-democratic-primary-2026-karishma-manzur-chris-pappas"]),
    ]),

    # ---------- Lee Calhoun (MT-R, U.S. Senator 2026) ----------
    ("lee-calhoun", "MT", "Senator", [
        claim("lc3", "lee-calhoun", "sanctity_of_life", 0, True,
              "Stated publicly that 'human life deserves legal protection from conception until natural death' — directly affirming the life-at-conception/personhood standard at the core of the rubric's first life question, a position he maintains alongside his otherwise heterodox economic platform.",
              ["https://ivoterguide.com/candidate/91417/race/27491/election/1419",
               "https://projects.montanafreepress.org/election-guide-2026/candidates/lee-calhoun/"]),
    ]),

    # ---------- Adam Schwarze (MN-R, U.S. Senator 2026) ----------
    ("adam-schwarze", "MN", "Senator", [
        claim("as3", "adam-schwarze", "sanctity_of_life", 0, True,
              "Holds 'strict anti-abortion beliefs' and campaigns as 'uncompromising' on life; repeatedly attacked primary rival Michele Tafoya for describing herself as 'pro-choice,' making the pro-life contrast a central driver of his grassroots support and his eventual GOP endorsement in May 2026.",
              ["https://www.startribune.com/adam-schwarze-wins-republican-gop-minnesota-senate-endorsement-michele-tafoya-primary/601845122",
               "https://www.startribune.com/adam-schwarze-built-momentum-with-gop-activists-now-rivals-are-trying-to-stop-him/601837058"]),
    ]),

    # ---------- Jeannie Evans (IL-R, U.S. Senator 2026, lost March primary) ----------
    ("jeannie-evans-il-senate", "IL", "Senator", [
        claim("je3", "jeannie-evans-il-senate", "sanctity_of_life", 0, False,
              "Declined to advocate for a federal personhood standard, stating she would not support a national abortion ban and would leave the decision to individual states — a position that falls short of the rubric's explicit life-at-conception/personhood requirement.",
              ["https://www.kwqc.com/2026/02/12/illinois-gop-senate-candidates-take-stage-first-major-debate/",
               "https://will.illinois.edu/21stshow/story/gop-senate-candidate-jeannie-evans"]),
    ]),

    # ---------- Joshua Smith (IA-R, U.S. Senator 2026) ----------
    ("joshua-smith-ia-senate", "IA", "Senator", [
        claim("js3", "joshua-smith-ia-senate", "self_defense", 1, True,
              "Pledged to 'author bills aimed at ending all federal gun laws from the U.S. Senate' — encompassing the repeal of assault-weapons restrictions, red-flag frameworks, magazine-capacity limits, and background-check regimes, positioning himself as the most expansive pro-Second Amendment candidate in the Iowa race.",
              ["https://www.yahoo.com/news/meet-joshua-smith-republican-former-112546667.html",
               "https://joshuasmith4senate.com/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
