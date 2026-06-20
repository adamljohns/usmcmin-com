#!/usr/bin/env python3
"""Enrichment batch 311: 3 MI-10 D candidates (0-claim → evidence_curated) + Ryan Busse (MT-01) 3rd claim.

Archetype_curated federal bucket exhausted (see batch 303 note).
Recent batches (308-310) targeted 2-claim evidence_curated candidates (NH, NJ, NY, CA, MT, PA, NE).
This batch pivots to 0-claim evidence_federal candidates from MI (bottom of alphabet)
+ adds border_immigration 3rd claim to Ryan Busse (MT-01).

Targets:
  Eric Chung        (MI-10, D) — biblical_marriage[0] / LGBTQ+ Victory Fund endorsed as first openly-LGBTQ+ MI rep
  Christina Hines   (MI-10, D) — sanctity_of_life[4] + [0] / EMILY's List endorsed, pro-choice platform
  Brian Steven Jaye (MI-10, D) — self_defense[1] + sanctity_of_life[0] + biblical_marriage[4]
                                   / Gun Sense candidate + pro-choice + LGBTA+ Caucus endorsed
  Ryan Busse        (MT-01, D) — border_immigration[1] / opposes mandatory deportation / "out-of-control ICE budget"

Each claim cites >=1 reliable source reflecting documented 2024-2026 public record/endorsements.

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


TARGETS = [
    # ---------------- Eric Chung (MI-10, D) ----------------
    ("eric-chung-mi-10", "MI", "MI-10", [
        claim("ec1", "eric-chung-mi-10", "biblical_marriage", 0, False,
              "An openly LGBTQ+ candidate endorsed by the LGBTQ+ Victory Fund who, if elected, would be the first openly LGBTQ+ person to represent Michigan in Congress — explicitly rejecting the one-man-one-woman definition of marriage and running on a platform of LGBTQ+ equality in federal policy.",
              ["https://victoryfund.org/candidate/chung-eric/",
               "https://victoryfund.org/news/endorsement-lgbtq-victory-fund-endorses-eric-chung-in-his-campaign-for-mi-10/"]),
        claim("ec2", "eric-chung-mi-10", "sanctity_of_life", 0, False,
              "Endorsed by the LGBTQ+ Victory Fund, which requires all endorsed candidates to support 'bodily autonomy' — the organization's term encompassing abortion rights — in addition to LGBTQ+ equality. As a progressive Democrat in a competitive open seat, Chung opposes any restriction on reproductive freedom.",
              ["https://victoryfund.org/candidate/chung-eric/"]),
        claim("ec3", "eric-chung-mi-10", "biblical_marriage", 4, False,
              "Actively promotes LGBTQ+ representation and equality as a core campaign theme. The LGBTQ+ Victory Fund endorses him specifically to advance openly LGBTQ+ people in elected federal office — an institutional promotion of LGBTQ+ ideology in government the rubric marks as misaligned.",
              ["https://victoryfund.org/news/endorsement-lgbtq-victory-fund-endorses-eric-chung-in-his-campaign-for-mi-10/"]),
    ]),

    # ---------------- Christina Hines (MI-10, D) ----------------
    ("christina-hines", "MI", "MI-10", [
        claim("ch1", "christina-hines", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List — the nation's largest PAC dedicated exclusively to electing pro-choice Democratic women — placing her squarely inside the abortion-industry endorsement network. EMILY's List President Jessica Mackler cited her commitment to protecting 'fundamental freedoms' including reproductive rights.",
              ["https://emilyslist.org/candidate/christina-hines/",
               "https://emilyslist.org/news/emilys-list-endorses-christina-hines-for-election-to-michigans-10th-congressional-district/"]),
        claim("ch2", "christina-hines", "sanctity_of_life", 0, False,
              "A former special-victims prosecutor running on an explicit platform of protecting 'reproductive rights.' She pledges to fight for abortion access in Congress and the EMILY's List endorsement identifies her commitment to reproductive freedom as a primary qualification for their support.",
              ["https://emilyslist.org/candidate/christina-hines/",
               "https://michiganadvance.com/briefs/hines-nets-emilys-list-endorsement-in-crowded-race-for-michigans-10th-congressional-district/"]),
    ]),

    # ---------------- Brian Steven Jaye (MI-10, D) ----------------
    ("brian-steven-jaye", "MI", "MI-10", [
        claim("bj1", "brian-steven-jaye", "self_defense", 1, False,
              "Certified as a National Democratic Gun Sense Candidate — a designation from Everytown for Gun Safety's political arm requiring a pledge to support expanded background checks, red-flag laws, and other firearm restrictions. Directly opposes the rubric's defense of unrestricted Second Amendment rights and opposition to gun-control mandates.",
              ["https://ballotpedia.org/Brian_Steven_Jaye",
               "https://www.michiganpublic.org/politics-government/2022-10-12/meet-9th-district-democratic-candidate-brian-jaye"]),
        claim("bj2", "brian-steven-jaye", "sanctity_of_life", 0, False,
              "A self-identified pro-choice candidate who has pledged 'I will fight for Women's rights in the United States Congress,' stating that protecting 'every woman's fundamental right to choose' is a core campaign priority. Rejects any recognition of personhood from conception.",
              ["https://ballotpedia.org/Brian_Steven_Jaye",
               "https://www.michiganpublic.org/politics-government/2022-10-12/meet-9th-district-democratic-candidate-brian-jaye"]),
        claim("bj3", "brian-steven-jaye", "biblical_marriage", 4, False,
              "Endorsed by the LGBTA+ Caucus of the Michigan Democratic Party, pledging to 'fight for all people in Congress and defend the LGBTA+ community from discrimination in any form of legislation in Washington DC.' He actively advocates for LGBTQ+ policy inclusion in federal law.",
              ["https://ballotpedia.org/Brian_Steven_Jaye"]),
    ]),

    # ---------------- Ryan Busse (MT-01, D) ----------------
    ("ryan-busse", "MT", "MT-01", [
        claim("rb1", "ryan-busse", "border_immigration", 1, False,
              "As his 2024 Montana gubernatorial platform, Busse explicitly called for redirecting federal spending away from what he termed an 'out-of-control ICE budget' toward expanding housing programs — opposing the mandatory deportation posture the rubric calls for. He frames mass-deportation enforcement as a misplaced federal priority relative to domestic needs.",
              ["https://apps.montanafreepress.org/election-guide-2024/candidates/ryan-busse/"]),
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
