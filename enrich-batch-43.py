#!/usr/bin/env python3
"""Enrichment batch 43: bottom-of-alphabet House candidates (NC/NV/MT).

Targets (4 R candidates, 11 claims total):
  Laurie Buckhout (NC-01, R) — 2026 R nominee, SBA-endorsed, pro-gun, anti-open-borders
  Drew Johnson   (NV-03, R)  — 2024 NV-03 nominee, NV Firearms Coalition, anti-deficit
  Al Olszewski   (MT-01, R)  — former MT state senator, life-at-conception, NRA A-rating
  Aaron Flint    (MT-01, R)  — 2026 R primary winner, anti-gun-control, anti-trans-athletes
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
    # -------- Laurie Buckhout (NC-01, R) --------
    ("laurie-buckhout", "NC", "NC-01", [
        claim("lb1", "laurie-buckhout", "sanctity_of_life", 0, True,
              "Endorsed for Congress 2026 by SBA Pro-Life America's Candidate Fund, which stated she 'stands with the people for the voiceless,' confirming a pro-life-from-conception posture.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-pro-life-americas-candidate-fund-endorses-laurie-buckhout-for-congress-in-nc-01",
               "https://sbaprolife.org/candidate/laurie-buckhout"]),
        claim("lb2", "laurie-buckhout", "self_defense", 1, True,
              "As a 'committed constitutional conservative,' her 2026 campaign lists opposing restrictions on firearms as a core policy priority, rejecting bans, waiting periods, and similar limitations on the right to keep and bear arms.",
              ["https://ballotpedia.org/Laurie_Buckhout"]),
        claim("lb3", "laurie-buckhout", "border_immigration", 0, True,
              "Campaign website declares 'Our nation is under siege by millions of illegal immigrants' due to 'Biden-Harris Administration's open border policies' and calls for a fully secured border and end to illegal crossings — aligning with the rubric's wall-and-enforcement standard.",
              ["https://ballotpedia.org/Laurie_Buckhout"]),
    ]),

    # -------- Drew Johnson (NV-03, R) --------
    ("drew-johnson", "NV", "NV-03", [
        claim("dj1", "drew-johnson", "self_defense", 0, True,
              "Earned the endorsement of the Nevada Firearms Coalition for his 'unwavering commitment to the Second Amendment' during his 2024 NV-03 campaign; pledged to 'always defend your right to keep and bear arms' as a member of Congress.",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/215541/drew-johnson",
               "https://ballotpedia.org/Drew_Johnson"]),
        claim("dj2", "drew-johnson", "border_immigration", 1, True,
              "Stated 'Open borders are a security threat that invites deadly drugs and human trafficking'; supports mandatory deportation through increased federal-local law-enforcement cooperation to identify and remove illegal immigrants.",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/215541/drew-johnson"]),
        claim("dj3", "drew-johnson", "economic_stewardship", 2, True,
              "A professional government-waste watchdog who campaigned on cutting wasteful foreign aid, reforming entitlements, and slashing excessive discretionary spending to reduce the federal deficit — directly matching the rubric's anti-deficit posture.",
              ["https://ballotpedia.org/Drew_Johnson",
               "https://en.wikipedia.org/wiki/Drew_Johnson"]),
    ]),

    # -------- Al Olszewski (MT-01, R) --------
    ("al-olszewski", "MT", "MT-01", [
        claim("ao1", "al-olszewski", "sanctity_of_life", 0, True,
              "Stated unequivocally 'Life begins at conception' and 'I will always protect life from conception to natural death' in the Montana Free Press 2022 election guide and across multiple campaigns (2018 Senate, 2020 governor, 2022 and 2026 House).",
              ["https://apps.montanafreepress.org/election-guide-2022/al-olszewski/",
               "https://www.ontheissues.org/Social/Albert_Olszewski_Abortion.htm"]),
        claim("ao2", "al-olszewski", "sanctity_of_life", 1, True,
              "As a Montana state senator, authored and carried multiple pro-life bills including HB 479 ('Montana's Unborn Child Pain and Suffering Prevention Act') and SB 282 (prohibiting abortions after 24 weeks, with violations a felony), prioritizing legislative abolition over incremental restrictions.",
              ["https://www.ontheissues.org/Social/Albert_Olszewski_Abortion.htm",
               "https://www.havredailynews.com/story/2019/08/30/opinion/olszewski-not-gianforte-is-the-pro-life-candidate-for-governor/525175.html"]),
        claim("ao3", "al-olszewski", "self_defense", 0, True,
              "Stated 'The Second Amendment is very clear. Our right to keep and bear arms shall not be infringed upon' and advocates constitutional carry (no-permit carry); earned an 'A' rating from both the NRA and the Montana Shooting Sports Association.",
              ["https://apps.montanafreepress.org/election-guide-2022/al-olszewski/",
               "https://www.ontheissues.org/states/MT_Gun_Control.htm"]),
    ]),

    # -------- Aaron Flint (MT-01, R) --------
    ("aaron-flint", "MT", "MT-01", [
        claim("af1", "aaron-flint", "self_defense", 1, True,
              "In his 2026 MT-01 primary campaign declared 'The gun grabbing socialists are on the march in Western Montana' and pledged to stop them — opposing red-flag laws, assault-weapons bans, and any magazine or registry restrictions.",
              ["https://montanafreepress.org/2026/04/13/in-montanas-western-district-aaron-flint-is-the-talked-up-candidate-for-congress/"]),
        claim("af2", "aaron-flint", "biblical_marriage", 2, True,
              "Made transgender athletes a recurring talking point in his 2026 MT-01 campaign, opposing biological males in women's sports and rejecting transgender ideology in public policy — in line with the rubric's opposition to LGBTQ ideological promotion.",
              ["https://montanafreepress.org/2026/04/13/in-montanas-western-district-aaron-flint-is-the-talked-up-candidate-for-congress/",
               "https://dailymontanan.com/2026/03/05/montanas-trump-flints-montana-talks-a-look-into-congressional-candidates-views/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions across states."""
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

    # Minified write — preserve the no-whitespace master to stay under GitHub's 50MB limit.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
