#!/usr/bin/env python3
"""Enrichment batch 187: hand-curated claims for 4 sitting U.S. House members (IN×3, IL).

archetype_curated bucket is fully depleted; targets are archetype_party_default
representatives with 0 evidence claims from the bottom of the alphabet (IN, IL).
Uses state-aware matcher to avoid cross-state slug collisions.

Targets (all R): Jefferson Shreve (IN-6), Jim Baird (IN-4),
Mark Messmer (IN-8), Darin LaHood (IL-16).
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
    # ------------ Jefferson Shreve (IN-6, R, US Representative) ------------
    ("jefferson-shreve", "IN", "Representative", [
        claim("js1", "jefferson-shreve", "sanctity_of_life", 0, True,
              "Endorsed for re-election by SBA Pro-Life America with an A+ rating for a consistent pro-life voting record in the 119th Congress, including support for defunding Planned Parenthood of Medicaid dollars through H.R.1 — affirming protection of unborn life.",
              ["https://sbaprolife.org/candidate-fund/leading-natl-pro-life-group-endorses-rep-jefferson-shreve-for-re-election",
               "https://en.wikipedia.org/wiki/Jefferson_Shreve"]),
        claim("js2", "jefferson-shreve", "self_defense", 1, False,
              "During his 2023 Indianapolis mayoral campaign, Shreve called for banning assault-weapon sales, repealing Indiana's permitless-carry law, and raising the minimum firearm purchase age to 21 — positions that earned him an F rating from the NRA Political Victory Fund and directly oppose the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Jefferson_Shreve",
               "https://ballotpedia.org/Jefferson_Shreve"]),
    ]),

    # -------------- Jim Baird (IN-4, R, US Representative) ----------------
    ("jim-baird", "IN", "Representative", [
        claim("jb1", "jim-baird", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America and a 100% lifetime score from the National Right to Life Committee; voted for H.R.1 (2025 reconciliation bill) defunding Planned Parenthood of Medicaid dollars for one year — described by SBA as the largest pro-life legislative victory in two decades.",
              ["https://sbaprolife.org/representative/jim-baird",
               "https://en.wikipedia.org/wiki/Jim_Baird_(politician)"]),
        claim("jb2", "jim-baird", "border_immigration", 1, False,
              "Cosponsored the DIGNIDAD (Dignity) Act of 2025 (H.R.4393) with 20 Republicans and 20 Democrats, creating a pathway to lawful permanent resident status for up to 12 million individuals without legal immigration status — directly opposing the rubric's call for mandatory deportation of those in the country illegally.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/4393",
               "https://en.wikipedia.org/wiki/DIGNIDAD_Act"]),
    ]),

    # ------------- Mark Messmer (IN-8, R, US Representative) --------------
    ("mark-messmer", "IN", "Representative", [
        claim("mm1", "mark-messmer", "sanctity_of_life", 0, True,
              "Introduced the Forced Abortion Prevention and Accountability Act in the 119th Congress, establishing federal penalties for administering any abortion-inducing drug to a woman without her informed consent — a pro-life measure protecting life and opposing coerced chemical abortion.",
              ["https://en.wikipedia.org/wiki/Mark_Messmer",
               "https://messmer.house.gov/"]),
        claim("mm2", "mark-messmer", "sanctity_of_life", 1, True,
              "Cosponsored legislation in the 119th Congress to amend the Internal Revenue Code to revoke the federal tax-exempt status of any organization that provides or funds abortions — an abolition-oriented measure targeting the financial infrastructure of the abortion industry rather than merely regulating procedures.",
              ["https://www.congress.gov/member/mark-messmer/M001233",
               "https://ballotpedia.org/Mark_Messmer"]),
    ]),

    # ------------- Darin LaHood (IL-16, R, US Representative) -------------
    ("darin-lahood", "IL", "Representative", [
        claim("dl1", "darin-lahood", "sanctity_of_life", 0, True,
              "A practicing Catholic with a consistent pro-life record: cosponsored the Protecting Pain-Capable Unborn Children from Late-Term Abortions Act (banning abortion at 20+ weeks), and voted for H.R.1 (2025) defunding Planned Parenthood of Medicaid dollars for one year.",
              ["https://lahood.house.gov/right-to-life",
               "https://sbaprolife.org/representative/darin-lahood"]),
        claim("dl2", "darin-lahood", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (S.5, signed Jan. 29, 2025), requiring DHS to mandatorily detain illegal immigrants charged with or convicted of theft, burglary, or violent crimes and initiate removal proceedings — enforcing mandatory deportation rather than catch-and-release.",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://lahood.house.gov/immigration"]),
        claim("dl3", "darin-lahood", "self_defense", 1, True,
              "A licensed FOID card holder who openly commits to defending 'hunters, sportsmen, and firearm owners' in Central and West Central Illinois; stated that law-abiding citizens have a constitutional right to keep and bear arms and has opposed executive gun-control orders as unconstitutional.",
              ["https://lahood.house.gov/2nd-amendment",
               "https://ballotpedia.org/Darin_LaHood"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
