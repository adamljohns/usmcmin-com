#!/usr/bin/env python3
"""Enrichment batch 331: add 3rd claim for 5 evidence_curated federal candidates.

Targets evidence_curated U.S. House candidates with 2 claims from the
bottom of the alphabet (KY, IL, FL). Adds one claim each in a category
distinct from their existing two.

Mix: Melissa Strange (KY-D), Jan Schakowsky (IL-D retiring),
Danny Davis (IL-D retiring), Daniel Webster (FL-R retiring),
Daniel Biss (IL-D 2026 nominee IL-09).

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
    # ---------------- Melissa Strange (KY-D, KY-04) ----------------
    ("melissa-strange", "KY", "KY-04", [
        claim("mst3", "melissa-strange", "self_defense", 1, False,
              "Gun Sense Voter (the electoral program of Everytown for Gun Safety / Moms Demand Action) lists Strange as a 2026 Gun Sense Candidate for KY-04, reflecting her stated support for expanded background checks and red-flag laws — positions that oppose the rubric's standard of unrestricted constitutional carry and opposition to red-flag legislation.",
              ["https://gunsensevoter.org/candidates/"]),
    ]),

    # ---------------- Jan Schakowsky (IL-D, retiring US Rep) ----------------
    ("jan-schakowsky", "IL", "Representative", [
        claim("js3", "jan-schakowsky", "border_immigration", 0, False,
              "Schakowsky voted NAY on H.R. 2 (118th Cong.), the Secure the Border Act of 2023 (House Roll Call 209, May 11, 2023), which mandated DHS resume border-wall construction, reinstated Remain-in-Mexico protocols, and tightened asylum eligibility. The bill passed 219–213 on party lines; all House Democrats, including Schakowsky, opposed it.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://schakowsky.house.gov/issues/reform"]),
    ]),

    # ---------------- Danny Davis (IL-D, retiring US Rep IL-07) ----------------
    ("danny-davis", "IL", "IL-07", [
        claim("dd3", "danny-davis", "biblical_marriage", 1, False,
              "Davis co-sponsored H.R. 8404 (Respect for Marriage Act, 117th Cong.) and voted YEA on final House passage (Roll Call 513, Dec. 8, 2022), which repealed the Defense of Marriage Act and permanently enshrined federal recognition of same-sex marriages in statute — opposing the rubric's one-man-one-woman marriage standard.",
              ["https://www.govtrack.us/congress/votes/117-2022/h513",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
    ]),

    # ---------------- Daniel Webster (FL-R, retiring US Rep FL-11) ----------------
    ("daniel-webster", "FL", "Representative", [
        claim("dw3", "daniel-webster", "border_immigration", 0, True,
              "Webster voted YEA on H.R. 2 (118th Cong., Roll Call 209, May 11, 2023), the Secure the Border Act, and cosponsored two of its constituent provisions. The bill mandated DHS resume southern-border-wall construction, reinstated Remain-in-Mexico protocols, and tightened asylum eligibility — aligning with the rubric's demand for border enforcement and wall completion.",
              ["https://webster.house.gov/2023/5/webster-votes-to-pass-legislation-to-secure-the-southern-border",
               "https://www.govtrack.us/congress/votes/118-2023/h209"]),
    ]),

    # ---------------- Daniel Biss (IL-D, 2026 nominee IL-09) ----------------
    ("daniel-biss", "IL", "IL-09", [
        claim("db3", "daniel-biss", "self_defense", 1, False,
              "On his 2026 IL-09 campaign website, Biss explicitly called for repealing the Second Amendment, arguing it 'has been grossly corrupted' and should be repealed to 'empower all levels of government to impose reasonable gun safety laws without constitutional threat,' and endorsed a federal assault-weapons ban — directly opposing the rubric's defense of constitutional carry and opposition to assault-weapons bans.",
              ["https://www.danielbiss.com/issues/protecting-civil-rights-and-civil-liberties-for-all"]),
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
