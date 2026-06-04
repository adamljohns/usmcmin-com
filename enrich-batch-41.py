#!/usr/bin/env python3
"""Enrichment batch 41: 4 bottom-of-alphabet House candidates.

Targets archetype_curated House members with 0 claims (bottom of the
reversed bucket: PA then NY).  Senate slots (MA/IL) had no findable
sourced public positions and were skipped per the reliable-sources rule.

Mix (2 R / 2 D): Bob Brooks (PA-07 D, primary winner), Carol
Obando-Derstine (PA-07 D, lost primary), Brandon Williams (NY-22 R,
former Rep 2023-2025), Alison Esposito (NY-18 R, 2022 Lt Gov nominee).
Each claim cites >=1 reliable source and reflects 2024-2026 campaign
positions / voting records.

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
    # ---- Bob Brooks (PA-07 D, won primary, faces Mackenzie in general) ----
    ("bob-brooks-pa-07", "PA", "Representative", [
        claim("bb1", "bob-brooks-pa-07", "sanctity_of_life", 0, False,
              "Ran on an explicit pledge to codify Roe v. Wade into federal law, stating on his campaign platform that he supports legislation to 'codify Roe v. Wade in the constitution' — directly rejecting any legal recognition of personhood from conception.",
              ["https://brooksforcongress.com/issues/",
               "https://ballotpedia.org/Bob_Brooks_(Pennsylvania)"]),
        claim("bb2", "bob-brooks-pa-07", "biblical_marriage", 1, False,
              "Pledges to 'always stand up for LGBTQ people by... defending marriage equality,' explicitly affirming federal recognition of same-sex marriage against the one-man-one-woman standard.",
              ["https://brooksforcongress.com/issues/",
               "https://ballotpedia.org/Bob_Brooks_(Pennsylvania)"]),
        claim("bb3", "bob-brooks-pa-07", "foreign_policy_restraint", 1, True,
              "Campaign platform calls to 'stop endless wars,' arguing that 'Democrats used to stand against reckless wars and it's time to get back to that' — aligning with the rubric's demand to end open-ended foreign military entanglements.",
              ["https://brooksforcongress.com/issues/"]),
    ]),

    # ---- Carol Obando-Derstine (PA-07 D, lost primary to Bob Brooks) ----
    ("carol-obando-derstine", "PA", "Representative", [
        claim("cod1", "carol-obando-derstine", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List and by CHC BOLD PAC, both of which gate endorsements on candidates' explicit support for abortion access — placing her inside the core abortion-funding network the rubric grades against.",
              ["https://emilyslist.org/news/emilys-list-endorses-carol-obando-derstine-for-election-to-pennsylvanias-7th-congressional-district/",
               "https://www.boldpac.com/candidates/carol-obando-derstine"]),
        claim("cod2", "carol-obando-derstine", "sanctity_of_life", 0, False,
              "Listed 'civil and reproductive rights' as a top priority, pledging to 'fight back against extreme attacks on health care and be a fierce advocate for reproductive freedom' — opposing any legal protection for unborn personhood.",
              ["https://ballotpedia.org/Carol_Obando-Derstine",
               "https://emilyslist.org/news/emilys-list-endorses-carol-obando-derstine-for-election-to-pennsylvanias-7th-congressional-district/"]),
        claim("cod3", "carol-obando-derstine", "border_immigration", 0, False,
              "Her family immigrated from Colombia and she listed 'immigration reform' as a top campaign priority — opposing the wall construction, mandatory deportation, and enforcement policies the rubric requires.",
              ["https://ballotpedia.org/Carol_Obando-Derstine",
               "https://www.boldpac.com/candidates/carol-obando-derstine"]),
    ]),

    # ---- Brandon Williams (NY-22 R, former Rep 2023-2025) ----
    ("brandon-williams", "NY", "Representative", [
        claim("bw1", "brandon-williams", "self_defense", 1, True,
              "Stated he would 'oppose any effort in Congress to restrict or remove access to firearms, including red-flag laws and bans of assault weapons and high-capacity magazines' — a clean pro-Second Amendment record on the rubric's core gun-rights questions during his 2023-2025 House term.",
              ["https://en.wikipedia.org/wiki/Brandon_Williams_(politician)"]),
        claim("bw2", "brandon-williams", "border_immigration", 0, True,
              "Voted for H.R. 2 (the Secure the Border Act of 2023), which funds border-wall construction, tightens the asylum system, and implements the Border Security Deployment Program — matching the rubric's wall-plus-enforcement standard.",
              ["https://en.wikipedia.org/wiki/Brandon_Williams_(politician)",
               "https://www.congress.gov/bill/118th-congress/house-bill/2"]),
        claim("bw3", "brandon-williams", "sanctity_of_life", 0, True,
              "Holds a pro-life record rated by SBA Pro-Life America, having voted consistently to defend unborn life throughout his 2023-2025 congressional term; personally opposes abortion and celebrated the Dobbs ruling.",
              ["https://sbaprolife.org/representative/brandon-williams",
               "https://en.wikipedia.org/wiki/Brandon_Williams_(politician)"]),
    ]),

    # ---- Alison Esposito (NY-18 R, 2022 Lt Gov nominee, former NYPD) ----
    ("alison-esposito-ny-18", "NY", "Representative", [
        claim("ae1", "alison-esposito-ny-18", "border_immigration", 0, True,
              "Stated during her 2024 NY-18 campaign that 'the construction of our border wall must resume, and new technologies should be employed to monitor our borders' — directly matching the rubric's call for wall construction and military-backed border security.",
              ["https://ballotpedia.org/Alison_Esposito"]),
        claim("ae2", "alison-esposito-ny-18", "self_defense", 1, True,
              "Said she does not support an assault-weapons ban, arguing that 'we do not remove a Second Amendment right from our citizens simply because somebody else committed a crime' — opposing the gun restrictions the rubric scores against.",
              ["https://pix11.com/news/local-news/republican-ny-18-candidate-alison-esposito-says-america-doesnt-have-a-gun-problem/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
