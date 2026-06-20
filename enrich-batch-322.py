#!/usr/bin/env python3
"""Enrichment batch 322: third claims for 5 evidence_curated 2026 federal candidates.

Primary archetype_curated-senator bucket exhausted; targets taken from bottom
of the evidence_curated-federal-2claim list (reverse-alpha by state: NJ, SC, FL, AZ, IA).

Candidates:
  Verlina Reynolds-Jackson (NJ-12, D) — border_immigration[q2]
  Max Diaz                 (SC-01, D) — border_immigration[q2]
  Anthony Sabatini         (FL-11, R) — sanctity_of_life[q4]
  Joseph Chaplik           (AZ-01, R) — self_defense[q0]
  Lanon Baccam             (IA-03, D) — border_immigration[q1]

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
    # --- Verlina Reynolds-Jackson (NJ-12, D) ---
    ("verlina-reynolds-jackson", "NJ", "Representative", [
        claim("vrj1", "verlina-reynolds-jackson", "border_immigration", 2, False,
              "During her 2026 NJ-12 campaign stated that ICE should be abolished and its funding reallocated to FEMA, rejecting enforcement-first immigration policy and any anti-sanctuary standard — a position that directly opposes the rubric's requirement for immigration-law enforcement cooperation.",
              ["https://www.dailyprincetonian.com/article/2026/03/princeton-news-broadfocus-verlina-reynolds-jackson-new-jersey-12-congressional-district",
               "https://ballotpedia.org/Verlina_Reynolds-Jackson"]),
    ]),

    # --- Max Diaz (SC-01, D) ---
    ("max-diaz-sc-01", "SC", "Representative", [
        claim("md1", "max-diaz-sc-01", "border_immigration", 2, False,
              "At a 2026 SC-01 primary candidate forum, offered the most extreme position on immigration among respondents: argued ICE should be dismantled entirely and its enforcement responsibilities reassigned to other agencies — a stance that directly rejects the anti-sanctuary and enforcement-first border policy the rubric requires.",
              ["https://yourislandnews.com/primary-2026-1st-district-candidates-share-competing-visions-for-lowcountry/",
               "https://ballotpedia.org/Max_Diaz"]),
    ]),

    # --- Anthony Sabatini (FL-11, R) ---
    ("anthony-sabatini-fl-11", "FL", "Representative", [
        claim("as1", "anthony-sabatini-fl-11", "sanctity_of_life", 4, True,
              "Described by iVoterGuide as 'Florida's most outspoken opponent of abortion'; sponsored the Heartbeat Bill (near-total ban at ~6 weeks gestation) in every Florida House session from 2018 through his final term, and explicitly stated that abortion providers including Planned Parenthood should receive no federal, state, or local government funding — a consistent record of refusing to participate in the abortion-industry funding network.",
              ["https://ivoterguide.com/candidate/41519/race/1298/election/922",
               "https://ballotpedia.org/Anthony_Sabatini"]),
    ]),

    # --- Joseph Chaplik (AZ-01, R) ---
    ("joseph-chaplik", "AZ", "Representative", [
        claim("jc1", "joseph-chaplik", "self_defense", 0, True,
              "Earned an A+ NRA rating during his Arizona House tenure and received endorsements from Gun Owners of America and the National Association for Gun Rights for his 2026 AZ-01 congressional bid; also voted for HB2111 (2021) prohibiting Arizona from enforcing federal firearms laws inconsistent with state law — a constitutional-carry-aligned, Second Amendment maximalist record.",
              ["https://azfreedomproject.com/joseph-chaplik-spotlight/",
               "https://en.wikipedia.org/wiki/Joseph_Chaplik",
               "https://ballotpedia.org/Joseph_Chaplik"]),
    ]),

    # --- Lanon Baccam (IA-03, D) ---
    ("lanon-baccam", "IA", "Representative", [
        claim("lb1", "lanon-baccam", "border_immigration", 1, False,
              "The son of Laotian refugees, Baccam explicitly rejected mandatory deportation as border policy; drew on his family's immigrant experience to argue against mass deportation while framing his preferred approach as 'bipartisan' — adding border patrol agents and fentanyl-detection technology at ports rather than the mandatory-deportation and enforcement-first model the rubric requires.",
              ["https://www.washingtonpost.com/nation/2024/10/24/iowa-congress-immigration-lanon-baccam/",
               "https://ballotpedia.org/Lanon_Baccam"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision across states."""
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
