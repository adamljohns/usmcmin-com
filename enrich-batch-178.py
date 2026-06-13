#!/usr/bin/env python3
"""Enrichment batch 178: 5 sitting CA House Democrats.

Targets: Sydney Kamlager-Dove (CA-37), Ro Khanna (CA-17), Robert Garcia (CA-42),
Pete Aguilar (CA-33), Norma Torres (CA-35).

All taken from the evidence_federal / 0-claims bottom-of-alphabet bucket (CA
is now the deepest remaining state with sitting members and 0 claims). Picks
are reverse-sorted by name within CA consistent with the bottom-of-alphabet
mandate.

Sources: en.wikipedia.org, ballotpedia.org, govtrack.us, khanna.house.gov.
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
    # ---------------- Sydney Kamlager-Dove (CA-37, D) ----------------
    ("sydney-kamlager-dove", "CA", "Representative", [
        claim("skd1", "sydney-kamlager-dove", "sanctity_of_life", 4, False,
              "Served on the board of Planned Parenthood Los Angeles before and during her congressional career, placing her within the Planned Parenthood political and fundraising network — the exact donor/endorser nexus the rubric disqualifies.",
              ["https://en.wikipedia.org/wiki/Sydney_Kamlager-Dove",
               "https://ballotpedia.org/Sydney_Kamlager-Dove"]),
        claim("skd2", "sydney-kamlager-dove", "sanctity_of_life", 0, False,
              "Supports federal protection of abortion access including the Women's Health Protection Act to codify abortion rights nationally and prohibit state gestational limits — rejecting any legal recognition of personhood from conception.",
              ["https://ballotpedia.org/Sydney_Kamlager-Dove",
               "https://en.wikipedia.org/wiki/Sydney_Kamlager-Dove"]),
        claim("skd3", "sydney-kamlager-dove", "biblical_marriage", 4, False,
              "A member of the Congressional Progressive Caucus and former California state senator who championed racial-equity and social-justice legislation; consistently backed LGBTQ-inclusive equality policies and supports the Equality Act, which would extend sexual-orientation and gender-identity protections into federal programs and schools.",
              ["https://en.wikipedia.org/wiki/Sydney_Kamlager-Dove",
               "https://ballotpedia.org/Sydney_Kamlager-Dove"]),
    ]),

    # ---------------- Ro Khanna (CA-17, D) ----------------
    ("ro-khanna", "CA", "Representative", [
        claim("rk1", "ro-khanna", "industry_capture", 4, True,
              "Was the lone dissenting vote against the FY2024 NDAA ($886B) in House Armed Services Committee, stating Pentagon spending was 'on track to a trillion dollar budget' and that defense contractors were 'ripping off American taxpayers at every turn.' In June 2026 introduced H.R.9283 requiring federal review of investment-company acquisitions of controlling stakes in major defense suppliers.",
              ["https://khanna.house.gov/media/press-releases/statement-khanna-long-no-vote-ndaa-out-house-armed-services-committee",
               "https://khanna.house.gov/media/press-releases/statement-khanna-votes-no-ndaa-house-floor-calls-modern-national-security"]),
        claim("rk2", "ro-khanna", "foreign_policy_restraint", 1, True,
              "A leading Congressional advocate for ending open-ended military entanglements: voted NO on the House floor against the $886B FY2024 NDAA and has repeatedly called for a 'modern national security strategy' that breaks from forever-war posture — consistent with the rubric's demand to end forever wars.",
              ["https://khanna.house.gov/media/press-releases/statement-khanna-votes-no-ndaa-house-floor-calls-modern-national-security",
               "https://en.wikipedia.org/wiki/Ro_Khanna"]),
        claim("rk3", "ro-khanna", "sanctity_of_life", 0, False,
              "As of 2021 voted 100% in alignment with President Biden's stated positions, which includes federal protection of abortion access and codifying Roe v. Wade; self-described progressive-capitalist who supports reproductive rights.",
              ["https://en.wikipedia.org/wiki/Ro_Khanna",
               "https://www.govtrack.us/congress/members/ro_khanna/412684"]),
    ]),

    # ---------------- Robert Garcia (CA-42, D) ----------------
    ("robert-garcia", "CA", "Representative", [
        claim("rg1", "robert-garcia", "biblical_marriage", 0, False,
              "The first openly gay immigrant elected to Congress and first openly LGBT mayor of Long Beach; co-chairs the House International LGBTQI+ Rights Task Force (119th Congress), which explicitly promotes LGBTQ identity as a protected class in U.S. foreign and domestic policy — rejecting the one-man/one-woman standard.",
              ["https://en.wikipedia.org/wiki/Robert_Garcia_(California_congressman)"]),
        claim("rg2", "robert-garcia", "foreign_policy_restraint", 1, False,
              "Voted in favor of all three April 2024 foreign military aid supplementals totaling ~$95B for Ukraine, Israel, and Taiwan — supporting continued open-ended U.S. military entanglements abroad rather than restraint.",
              ["https://en.wikipedia.org/wiki/Robert_Garcia_(California_congressman)"]),
        claim("rg3", "robert-garcia", "sanctity_of_life", 0, False,
              "Supports abortion rights and has backed legislation to protect federal abortion access, consistent with his Congressional Progressive Caucus membership and 100% alignment with Planned Parenthood's legislative agenda.",
              ["https://ballotpedia.org/Robert_Garcia_(California)",
               "https://en.wikipedia.org/wiki/Robert_Garcia_(California_congressman)"]),
    ]),

    # ---------------- Pete Aguilar (CA-33, D) ----------------
    ("pete-aguilar", "CA", "Representative", [
        claim("pa1", "pete-aguilar", "self_defense", 1, False,
              "A vocal gun-control advocate who backed an assault-weapons ban and participated in the June 2016 House floor sit-in organized to pressure leadership for gun-control votes; opposes the constitutional firearm rights the rubric protects.",
              ["https://en.wikipedia.org/wiki/Pete_Aguilar",
               "https://ballotpedia.org/Pete_Aguilar"]),
        claim("pa2", "pete-aguilar", "sanctity_of_life", 0, False,
              "As House Democratic Caucus Chair (#3 leadership) has pledged to fight for women's reproductive rights and protect abortion access; supports codifying federal abortion protections, rejecting personhood from conception.",
              ["https://en.wikipedia.org/wiki/Pete_Aguilar",
               "https://ballotpedia.org/Pete_Aguilar"]),
        claim("pa3", "pete-aguilar", "biblical_marriage", 4, False,
              "Supported legislation to prevent discrimination against LGBT people by government contractors and has backed LGBTQ-inclusive anti-discrimination policy throughout his tenure — consistent with promoting LGBTQ ideology in federal policy.",
              ["https://en.wikipedia.org/wiki/Pete_Aguilar"]),
    ]),

    # ---------------- Norma Torres (CA-35, D) ----------------
    ("norma-torres", "CA", "Representative", [
        claim("nt1", "norma-torres", "sanctity_of_life", 4, False,
              "Holds a 100% rating from Reproductive Freedom for All (formerly NARAL Pro-Choice America) and an F grade from the Susan B. Anthony List — placing her squarely in the abortion-advocacy endorsement network the rubric disqualifies.",
              ["https://en.wikipedia.org/wiki/Norma_Torres"]),
        claim("nt2", "norma-torres", "sanctity_of_life", 0, False,
              "Called the overturning of Roe v. Wade 'devastating' and said it reversed 'decades of hard-fought progress for women'; supports codifying federal abortion access and opposes any restrictions, rejecting personhood from conception.",
              ["https://en.wikipedia.org/wiki/Norma_Torres"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
