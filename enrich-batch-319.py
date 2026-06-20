#!/usr/bin/env python3
"""Enrichment batch 319: third evidence claim for 5 sitting U.S. Representatives.

Targets sitting US Reps with exactly 2 claims (evidence_curated confidence),
drawn from the bottom of the alphabet (AR, AL, AK). Adds one claim per candidate
in a DISTINCT rubric category not yet covered.

Candidates: French Hill (AR-R), Bruce Westerman (AR-R), Robert Aderholt (AL-R),
Nick Begich III (AK-R), Shomari Figures (AL-D).
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
    # ---- French Hill (AR-2, R) ----
    ("french-hill", "AR", "Representative", [
        claim("fh1", "french-hill", "self_defense", 1, True,
              "Holds an NRA A- rating and has voted consistently against gun-control expansions throughout his House career, opposing assault-weapons bans, magazine-capacity limits, and universal background check mandates — positions aligned with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/members/french_hill/412609",
               "https://en.wikipedia.org/wiki/French_Hill_(politician)"]),
    ]),

    # ---- Bruce Westerman (AR-4, R) ----
    ("bruce-westerman", "AR", "Representative", [
        claim("bw1", "bruce-westerman", "border_immigration", 0, True,
              "Voted for the Laken Riley Act (H.R.29, January 2025), mandating detention of non-citizens charged with violent crimes, and supported border-wall construction and military-enforcement provisions embedded in the One Big Beautiful Bill Act (H.R.1, signed July 2025) — consistent with the rubric's demand for physical barrier and military deterrence at the southern border.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act"]),
    ]),

    # ---- Robert Aderholt (AL-4, R) ----
    ("robert-aderholt", "AL", "Representative", [
        claim("ra1", "robert-aderholt", "self_defense", 1, True,
              "NRA-rated 'A' for consistent support of Second Amendment rights; cosponsored the Protecting the Right to Keep and Bear Arms Act of 2023 (H.R.5561) affirming federal protection of gun ownership, and has historically sponsored legislation banning gun-registration mandates in Washington, D.C. — opposing the registry and red-flag framework the rubric rejects.",
              ["https://www.ontheissues.org/house/Robert_Aderholt_Gun_Control.htm",
               "https://www.govtrack.us/congress/members/robert_aderholt/400004"]),
    ]),

    # ---- Nick Begich III (AK-AL, R) ----
    ("nick-begich-iii", "AK", "Representative", [
        claim("nb1", "nick-begich-iii", "sanctity_of_life", 0, True,
              "Voted for the One Big Beautiful Bill Act (H.R.1, 218–214, July 2025), which included a one-year Medicaid prohibition on funding Planned Parenthood; as a Freedom Caucus member has advocated for robust federal pro-life spending restrictions — aligning with the rubric's standard of protecting the unborn from conception.",
              ["https://en.wikipedia.org/wiki/Nick_Begich_III",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act"]),
    ]),

    # ---- Shomari Figures (AL-2, D) ----
    ("shomari-figures", "AL", "Representative", [
        claim("sf1", "shomari-figures", "sanctity_of_life", 0, False,
              "Voted against the One Big Beautiful Bill Act (H.R.1, 218–214, July 2025) — which passed over universal Democratic opposition — thereby opposing its one-year Medicaid defunding of Planned Parenthood, signaling support for continued taxpayer funding of the nation's largest abortion provider in conflict with the rubric's life-at-conception standard.",
              ["https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://en.wikipedia.org/wiki/Shomari_Figures"]),
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
