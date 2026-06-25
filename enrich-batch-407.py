#!/usr/bin/env python3
"""Enrichment batch 407: 4 Wyoming state representatives with 0 claims.

Transitions pipeline from exhausted archetype_curated federal bucket to
archetype_party_default state legislators, starting from the bottom of the
alphabet (WY). All claims sourced from wyoleg.gov, Ballotpedia, WyoFile,
and Wyoming Public Media; reflect 2025-2026 legislative record.

Targets: Jeremy Haroldson (WY-House), Pepper Ottman (WY-House),
         Paul Hoeft (WY-House), John Bear (WY-House).

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
    # ---- Jeremy Haroldson (WY-House District 4, Speaker Pro Tempore, Freedom Caucus) ----
    ("jeremy-haroldson", "WY", "Representative", [
        claim("jh1", "jeremy-haroldson", "self_defense", 0, True,
              "Primary sponsor of HB0172 (Repeal gun-free zones and preemption amendments), which he introduced every session since 2022; the 2025 bill passed the Wyoming House and became law after Governor Gordon let it take effect without his signature, eliminating most public gun-free zones in Wyoming and broadly expanding where permitless constitutional carry applies.",
              ["https://wyofile.com/wyoming-gun-free-zones-repeal-easily-clears-house-heads-to-senate/",
               "https://www.wyomingpublicmedia.org/politics-government/2025-01-24/we-are-local-control-wyoming-house-forwards-repeal-on-all-gun-free-zones-to-senate"]),
        claim("jh2", "jeremy-haroldson", "election_integrity", 0, True,
              "As Speaker Pro Tempore and Wyoming Freedom Caucus leader, championed banning ballot drop boxes and eliminating electronic voting machines in favor of hand-countable paper ballots as top 2026 legislative priorities — directly aligning with the rubric's demand for secure, verifiable, fraud-resistant elections.",
              ["https://www.wyomingpublicmedia.org/politics-government/2026-01-15/wyoming-freedom-caucus-releases-2026-legislative-priorities-ahead-of-session",
               "https://wyofile.com/wyoming-freedom-caucus-aims-at-state-spending-voting-machines-and-the-judicial-branch-in-2026-priorities/"]),
        claim("jh3", "jeremy-haroldson", "christian_liberty", 0, True,
              "Serves simultaneously as lead pastor of Impact Ministries, an Assemblies of God Pentecostal congregation in Wheatland, WY, and as Wyoming House Speaker Pro Tempore; his Freedom Caucus explicitly commits to legislation guided by 'godly principles,' and his Wyoming Public Media profile documents how his pastoral vocation directly informs his legislative priorities.",
              ["https://www.wyomingpublicmedia.org/open-spaces/2025-07-21/how-one-wyoming-representatives-religious-and-political-jobs-intersect",
               "https://en.wikipedia.org/wiki/Jeremy_Haroldson"]),
    ]),

    # ---- Pepper Ottman (WY-House District 34, Chair Labor/Health/Social Services) ----
    ("pepper-ottman", "WY", "Representative", [
        claim("po1", "pepper-ottman", "sanctity_of_life", 0, True,
              "Primary sponsor of HB0186 (Baby Olivia Act, 2026 session), which mandates human development education in Wyoming public schools grades 5-12, including high-definition ultrasound video and instruction on fertilization and fetal development from conception — educationally affirming the personhood of the unborn from the moment of fertilization.",
              ["https://wyomingfamily.org/hb0186-baby-olivia-act-requiring-human-development-education/",
               "https://wyoleg.gov/Legislation/2026/HB0186"]),
        claim("po2", "pepper-ottman", "border_immigration", 2, True,
              "Primary sponsor of HB0116 (Driver's licenses — unauthorized alien restrictions, 2026 session), directing Wyoming law enforcement not to recognize out-of-state driver's licenses issued to undocumented immigrants — a direct anti-sanctuary-policy measure that refuses state-level facilitation of unlawful presence.",
              ["https://wyofile.com/wyoming-senators-skeptical-of-bill-banning-out-of-state-licenses-for-undocumented-immigrants/",
               "https://ballotpedia.org/Pepper_Ottman"]),
        claim("po3", "pepper-ottman", "christian_liberty", 0, True,
              "Sponsored HB0143 (Free speech for health care providers), a conscience-protection bill shielding health care workers' right to speak freely on matters of professional and moral conscience — a religious-liberty measure protecting providers from compelled speech or viewpoint discrimination in medical settings.",
              ["https://ballotpedia.org/Pepper_Ottman",
               "https://www.wyoleg.gov/Legislators/2025/H/2076"]),
    ]),

    # ---- Paul Hoeft (WY-House District 25, Church of Christ Elder, NRA Benefactor) ----
    ("paul-hoeft", "WY", "Representative", [
        claim("ph1", "paul-hoeft", "sanctity_of_life", 0, True,
              "Ran on an explicit Wyoming Right to Life platform and co-sponsored HB0186 (Baby Olivia Act, 2026) mandating fetal development education from fertilization in WY schools; Ballotpedia lists 'Wyoming Right to Life' as a primary campaign message, affirming life from conception as a core legislative priority.",
              ["https://ballotpedia.org/Paul_Hoeft",
               "https://wyoleg.gov/Legislation/2026/HB0186"]),
        claim("ph2", "paul-hoeft", "self_defense", 1, True,
              "A Benefactor Member of the National Rifle Association and ran on a Gun Owners of America platform; serves on Wyoming's State Shooting Complex Oversight Task Force and manages a sporting goods department at a ranch supply store — making Second Amendment rights both a professional and legislative cornerstone of his public service.",
              ["https://ballotpedia.org/Paul_Hoeft",
               "https://www.wyoleg.gov/Legislators/2025/H/2124"]),
        claim("ph3", "paul-hoeft", "christian_liberty", 0, True,
              "Serves as an Elder in the Church of Christ — a formal leadership role requiring doctrinal accountability in his tradition — and carries faith-grounded values into his legislative work, evidenced by his pro-life platform and co-sponsorship of the Baby Olivia Act.",
              ["https://ballotpedia.org/Paul_Hoeft"]),
    ]),

    # ---- John Bear (WY-House District 31, Gillette/Campbell County) ----
    ("john-bear", "WY", "Representative", [
        claim("jb1", "john-bear", "election_integrity", 0, True,
              "Co-sponsored HB0156 (2025 general session), which requires documentation for voter registration in Wyoming — tightening ballot access to verified citizens and aligning with the rubric's demand for secure, document-verified voter rolls.",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://ballotpedia.org/John_Bear_(Wyoming)"]),
        claim("jb2", "john-bear", "election_integrity", 0, True,
              "Co-sponsored HB0173 (Independent candidate requirements, 2025), amending Wyoming election statutes W.S. 22-5-301, 22-5-304, and 22-5-307 to tighten qualification standards for independent candidates — reinforcing the integrity and accountability of Wyoming's ballot-access framework.",
              ["https://wyoleg.gov/2025/Bills/HB0173.pdf",
               "https://ballotpedia.org/John_Bear_(Wyoming)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions across states.

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
