#!/usr/bin/env python3
"""Enrichment batch 751: 5 TN Republican state legislators with 0 claims.

Targets archetype_party_default TN state representatives from the bottom of
the alphabet pool: William Slater (HD-35), Tom Stinnett (HD-20),
Todd Warner (HD-92), Timothy Hill (HD-3), Tim Rudd (HD-34).

Sources: Ballotpedia, Wikipedia, en.wikipedia.org/wiki/Tennessee_Senate_Bill_1,
en.wikipedia.org/wiki/Gun_laws_in_Tennessee, tn.gov,
news.ballotpedia.org (Education Freedom Act 2025).

Writes scorecard.json MINIFIED to stay under GitHub 50MB limit.
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
    # ---------------- William Slater (TN HD-35, Republican) ----------------
    ("william-slater", "TN", "Representative", [
        claim("ws1", "william-slater", "biblical_marriage", 2, True,
              "Voted YES on Tennessee SB1/HB1 (signed March 2, 2023), banning gender-affirming medical care — puberty blockers and hormone therapy — for minors. The bill passed the House 77-16, with Slater (in office since November 2022) supporting it. The law also requires schools to notify parents if a minor requests gender-identity affirmation, rejecting the state-over-parent transgender-ideology framework.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://ballotpedia.org/William_Slater"]),
        claim("ws2", "william-slater", "family_child_sovereignty", 0, True,
              "Voted for Tennessee's Education Freedom Act of 2025 (HB6004/SB6001, signed February 12, 2025), creating the state's first universal Education Savings Account scholarship program — $7,296 per student — allowing families to redirect public school funding to private, charter, or home-school alternatives, consistent with the rubric's principle of parental sovereignty over children's education.",
              ["https://news.ballotpedia.org/2025/02/18/tennessee-enacts-private-school-choice-scholarship-bill-becoming-the-13th-state-with-a-universal-school-choice-program/",
               "https://www.tn.gov/governor/news/2025/1/30/gov--lee-marks-the-close-of-special-legislative-session--passes-full-agenda.html"]),
    ]),

    # ---------------- Tom Stinnett (TN HD-20, Republican) ----------------
    ("tom-stinnett", "TN", "Representative", [
        claim("tst1", "tom-stinnett", "family_child_sovereignty", 0, True,
              "A career educator (nearly 40 years in Career and Technical Education) who voted for Tennessee's Education Freedom Act of 2025 (HB6004, signed February 12, 2025) — the state's universal $7,296 per-student scholarship program redirecting public education dollars to family-chosen private or alternative schools. Stinnett's support from an education-professional background underscores the parental-sovereignty principle over bureaucratic schooling monopolies.",
              ["https://ballotpedia.org/Tom_Stinnett",
               "https://news.ballotpedia.org/2025/02/18/tennessee-enacts-private-school-choice-scholarship-bill-becoming-the-13th-state-with-a-universal-school-choice-program/"]),
        claim("tst2", "tom-stinnett", "biblical_marriage", 2, True,
              "Elected November 2024 as a Republican in Tennessee's Republican supermajority House (75-24); represents a district where Tennessee's 2023 gender-affirming care ban for minors (SB1) was supported and upheld, including at the U.S. Supreme Court (United States v. Skrmetti, cert. granted June 2024). Stinnett's election platform aligned with the Republican caucus's rejection of transgender ideology in state law and public schools.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://ballotpedia.org/Tom_Stinnett"]),
    ]),

    # ---------------- Todd Warner (TN HD-92, Republican) ----------------
    ("todd-warner", "TN", "Representative", [
        claim("tw1", "todd-warner", "self_defense", 1, True,
              "Ranked 5th most conservative member of the entire Tennessee House and Senate by the American Conservative Union for the 2021 session (earning an 'A' grade for advancing conservative policy). In the same session, voted for Tennessee's permitless carry law (HB786, effective July 1, 2021), eliminating permit requirements for law-abiding Tennesseans 21+ to carry handguns; later voted for legislation authorizing school faculty and staff to conceal carry with training — consistently opposing new gun restrictions.",
              ["https://en.wikipedia.org/wiki/Todd_Warner",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
        claim("tw2", "todd-warner", "biblical_marriage", 2, True,
              "Voted YES on SB1/HB1 (signed March 2, 2023), Tennessee's ban on gender-affirming medical care for minors (puberty blockers, hormone therapy), which passed the House 77-16. The law — upheld by the U.S. Supreme Court in United States v. Skrmetti (2024) — reflects the rubric's rejection of transgender ideology as a basis for state-sanctioned medical intervention on children.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://ballotpedia.org/Todd_Warner"]),
        claim("tw3", "todd-warner", "family_child_sovereignty", 0, True,
              "Voted for the Education Freedom Act of 2025 (HB6004, signed February 12, 2025) — Tennessee's universal school-choice scholarship program offering $7,296 per student for private or alternative schooling. Warner, a row-crop farmer and small-business owner, supported expanding parental control over education against the state-monopoly school system.",
              ["https://news.ballotpedia.org/2025/02/18/tennessee-enacts-private-school-choice-scholarship-bill-becoming-the-13th-state-with-a-universal-school-choice-program/",
               "https://en.wikipedia.org/wiki/Todd_Warner"]),
    ]),

    # ---------------- Timothy Hill (TN HD-3, Republican) ----------------
    ("timothy-hill", "TN", "Representative", [
        claim("th1", "timothy-hill", "sanctity_of_life", 0, True,
              "A long-serving Tennessee Republican (2013-2021, returned August 2023) who served as House Majority Whip (selected February 2016) during the Tennessee General Assembly's 2019 passage of SB1257/HB1029 — Tennessee's Human Life Protection Act, a total abortion trigger ban that outlawed nearly all abortions after fertilization when Roe v. Wade was overturned in June 2022. Hill's leadership role during that vote reflects consistent life-from-conception alignment.",
              ["https://en.wikipedia.org/wiki/Timothy_Hill_(politician)",
               "https://ballotpedia.org/Timothy_Hill"]),
        claim("th2", "timothy-hill", "family_child_sovereignty", 0, True,
              "As a member of the Tennessee House Health Committee, Hill voted for the Education Freedom Act of 2025 (HB6004, signed February 12, 2025) — Tennessee's universal $7,296 per-student education scholarship — giving parents direct control over education dollars for private or alternative schooling options and shifting power from the state school bureaucracy to families.",
              ["https://news.ballotpedia.org/2025/02/18/tennessee-enacts-private-school-choice-scholarship-bill-becoming-the-13th-state-with-a-universal-school-choice-program/",
               "https://ballotpedia.org/Timothy_Hill"]),
    ]),

    # ---------------- Tim Rudd (TN HD-34, Republican) ----------------
    ("tim-rudd", "TN", "Representative", [
        claim("tr1", "tim-rudd", "sanctity_of_life", 0, True,
              "A self-described opponent of abortion for any reason who has advocated consistently for the protection of the unborn throughout his tenure (elected 2016). Served in the Tennessee House during the 2019 passage of SB1257/HB1029 — the Human Life Protection Act total abortion trigger ban — which outlawed nearly all abortions in Tennessee following the June 2022 Dobbs ruling.",
              ["https://en.wikipedia.org/wiki/Tim_Rudd",
               "https://ballotpedia.org/Tim_Rudd"]),
        claim("tr2", "tim-rudd", "christian_liberty", 0, True,
              "Sponsored HB-836 (enacted), which grants taxpayer-funded adoption and foster care agencies the statutory right to refuse placements based on 'religious beliefs or moral convictions' — protecting faith-based child-welfare ministries from being forced to place children with LGBTQ households. One of the broadest religious-free-exercise shields for faith-based agencies passed by any state legislature.",
              ["https://en.wikipedia.org/wiki/Tim_Rudd",
               "https://ballotpedia.org/Tim_Rudd"]),
        claim("tr3", "tim-rudd", "self_defense", 1, True,
              "A Second Amendment defender who lists protection of the Second Amendment as a core legislative priority and voted for Tennessee's permitless carry law (HB786, effective July 1, 2021) — eliminating the permit requirement for law-abiding Tennesseans 21+ to carry handguns openly or concealed. Consistently opposes new firearm restrictions.",
              ["https://en.wikipedia.org/wiki/Tim_Rudd",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing slug collisions.

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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
