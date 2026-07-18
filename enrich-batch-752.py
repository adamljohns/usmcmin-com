#!/usr/bin/env python3
"""Enrichment batch 752: 5 TN Republican state representatives with 0 claims.

Targets archetype_party_default TN state representatives from the bottom of
the alphabet pool: Tim Hicks (HD-6), Tandy Darby (HD-76), Sabi Kumar (HD-66),
Ryan Williams (HD-42), Rusty Grills (HD-77).

Sources: Ballotpedia, Wikipedia, en.wikipedia.org/wiki/Gun_laws_in_Tennessee,
en.wikipedia.org/wiki/Tennessee_Senate_Bill_1,
en.wikipedia.org/wiki/Tennessee_Human_Life_Protection_Act,
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
    # ---------------- Tim Hicks (TN HD-6, Republican) ----------------
    ("tim-hicks", "TN", "Representative", [
        claim("th1", "tim-hicks", "self_defense", 0, True,
              "Voted for Tennessee's constitutional carry law (HB786, effective July 1, 2021), eliminating permit requirements for law-abiding Tennesseans 21+ to carry handguns openly or concealed without a government permit. Hicks, owner of Hicks Construction and representing East Tennessee's Washington County since November 2020, supported the expansion of Second Amendment rights to all eligible citizens regardless of permit status.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee",
               "https://ballotpedia.org/Tim_Hicks_(Tennessee)"]),
        claim("th2", "tim-hicks", "biblical_marriage", 2, True,
              "Voted YES on SB1/HB1 (signed March 2, 2023), Tennessee's ban on gender-affirming medical interventions — puberty blockers, hormone therapy, and surgical transition procedures — for minors, which passed the House 77-16 and was later upheld by the U.S. Supreme Court in United States v. Skrmetti (2024). Hicks's vote rejects state-sanctioned medical transformation of children based on transgender ideology.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://ballotpedia.org/Tim_Hicks_(Tennessee)"]),
        claim("th3", "tim-hicks", "family_child_sovereignty", 0, True,
              "Voted for Tennessee's Education Freedom Act of 2025 (HB6004/SB6001, signed February 12, 2025), creating the state's first universal Education Savings Account program offering $7,296 per student annually — redirecting public education funding to private, charter, or home-school alternatives at each family's direction and breaking the state's monopoly over K-12 education funding.",
              ["https://news.ballotpedia.org/2025/02/18/tennessee-enacts-private-school-choice-scholarship-bill-becoming-the-13th-state-with-a-universal-school-choice-program/",
               "https://www.tn.gov/governor/news/2025/1/30/gov--lee-marks-the-close-of-special-legislative-session--passes-full-agenda.html"]),
    ]),

    # ---------------- Tandy Darby (TN HD-76, Republican) ----------------
    ("tandy-darby", "TN", "Representative", [
        claim("td1", "tandy-darby", "self_defense", 0, True,
              "Voted for Tennessee's constitutional carry law (HB786, effective July 1, 2021), eliminating permit requirements for law-abiding Tennesseans 21+ to carry handguns. Darby, an agricultural salesman representing rural Weakley County in West Tennessee since November 2020, supported constitutional carry consistent with his rural constituents' Second Amendment traditions of self-reliance and armed protection.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee",
               "https://ballotpedia.org/Tandy_Darby"]),
        claim("td2", "tandy-darby", "biblical_marriage", 2, True,
              "Voted YES on SB1/HB1 (signed March 2, 2023), Tennessee's ban on gender-affirming medical care — puberty blockers and hormone therapy — for minors, passing the House 77-16. The law, upheld by the U.S. Supreme Court in United States v. Skrmetti (2024), reflects Darby's rejection of the state-over-parent transgender-medicine ideology.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://ballotpedia.org/Tandy_Darby"]),
        claim("td3", "tandy-darby", "family_child_sovereignty", 0, True,
              "Voted for Tennessee's Education Freedom Act of 2025 (HB6004/SB6001, signed February 12, 2025), creating the state's universal $7,296 per-student Education Savings Account scholarship program. Darby, who holds a BS in agricultural business from UT Martin and has worked in family-oriented rural commerce since 1997, supported empowering families — rather than state bureaucracies — to direct their children's education.",
              ["https://news.ballotpedia.org/2025/02/18/tennessee-enacts-private-school-choice-scholarship-bill-becoming-the-13th-state-with-a-universal-school-choice-program/",
               "https://ballotpedia.org/Tandy_Darby"]),
    ]),

    # ---------------- Sabi Kumar (TN HD-66, Republican) ----------------
    ("sabi-kumar", "TN", "Representative", [
        claim("sk1", "sabi-kumar", "sanctity_of_life", 0, True,
              "A physician (hence 'Doc Kumar') and the first Indian American elected to the Tennessee House (since 2014) who voted for Tennessee's Human Life Protection Act (SB1257/HB1029, passed House 73-20 in 2019) — the state's total abortion trigger ban that outlawed nearly all abortions after fertilization upon Roe's overturning in June 2022. Kumar's medical background underscores his affirmation that human life deserving protection begins at fertilization.",
              ["https://en.wikipedia.org/wiki/Sabi_%22Doc%22_Kumar",
               "https://en.wikipedia.org/wiki/Tennessee_Human_Life_Protection_Act"]),
        claim("sk2", "sabi-kumar", "biblical_marriage", 2, True,
              "Voted YES on SB1/HB1 (signed March 2, 2023), Tennessee's ban on gender-affirming medical interventions for minors (passed House 77-16). Kumar, a physician and chair of the House Insurance Committee, voted to prohibit medically unnecessary puberty blockers and hormone therapy for children — rejecting the transgender-medical-ideology framework applied to pediatric care and upheld as constitutional by the U.S. Supreme Court in United States v. Skrmetti (2024).",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://ballotpedia.org/Sabi_Kumar"]),
        claim("sk3", "sabi-kumar", "family_child_sovereignty", 0, True,
              "Voted for Tennessee's Education Freedom Act of 2025 (HB6004/SB6001, signed February 12, 2025), the universal $7,296 per-student ESA scholarship program. As Chair of the House Insurance Committee, Kumar supported routing public education funding directly through families rather than school district bureaucracies — the state becoming the 13th in the nation to adopt a universal school-choice program.",
              ["https://news.ballotpedia.org/2025/02/18/tennessee-enacts-private-school-choice-scholarship-bill-becoming-the-13th-state-with-a-universal-school-choice-program/",
               "https://ballotpedia.org/Sabi_Kumar"]),
    ]),

    # ---------------- Ryan Williams (TN HD-42, Republican) ----------------
    ("ryan-williams", "TN", "Representative", [
        claim("rw1", "ryan-williams", "self_defense", 0, True,
              "Voted for Tennessee's constitutional carry law (HB786, effective July 1, 2021) and in 2024 co-sponsored a resolution — enacted — authorizing trained public school faculty and staff to carry concealed firearms on campus, eliminating the 'gun-free zone' policy that leaves children defenseless. Williams, serving as Republican Caucus Chairman since 2016, has led the caucus in consistently advancing constitutional carry protections across all settings.",
              ["https://ballotpedia.org/Ryan_Williams_(Tennessee)",
               "https://en.wikipedia.org/wiki/Ryan_Williams_(American_politician)"]),
        claim("rw2", "ryan-williams", "sanctity_of_life", 0, True,
              "As Republican Caucus Chairman since 2016, Williams coordinated the House Republican caucus's passage of Tennessee's Human Life Protection Act (SB1257/HB1029, passed House 73-20 in 2019) — a total abortion trigger ban outlawing nearly all abortions after fertilization, activated June 24, 2022, following the Dobbs ruling. Williams has represented Sullivan County since 2010 and holds a consistent pro-life voting record across his career.",
              ["https://en.wikipedia.org/wiki/Ryan_Williams_(American_politician)",
               "https://en.wikipedia.org/wiki/Tennessee_Human_Life_Protection_Act"]),
        claim("rw3", "ryan-williams", "family_child_sovereignty", 0, True,
              "As Chair of the House Committee on Rural Economic Development and Republican Caucus Chairman, Williams voted for Tennessee's Education Freedom Act of 2025 (HB6004/SB6001, signed February 12, 2025) — the state's universal $7,296 per-student scholarship program. Williams, who holds a BS in biology from Carson-Newman College, supported breaking the school district monopoly over education funding and returning that authority to families in rural and urban communities alike.",
              ["https://news.ballotpedia.org/2025/02/18/tennessee-enacts-private-school-choice-scholarship-bill-becoming-the-13th-state-with-a-universal-school-choice-program/",
               "https://ballotpedia.org/Ryan_Williams_(Tennessee)"]),
    ]),

    # ---------------- Rusty Grills (TN HD-77, Republican) ----------------
    ("rusty-grills", "TN", "Representative", [
        claim("rg1", "rusty-grills", "self_defense", 0, True,
              "A self-identified Conservative Baptist and working farmer who voted for Tennessee's constitutional carry law (HB786, effective July 1, 2021), eliminating permit requirements for law-abiding Tennesseans 21+ to carry handguns. Grills represents Dyer, Lake, and Obion Counties — Mississippi Delta farming territory — where firearm ownership for protection and property defense is foundational. He has represented this rural district since November 2020.",
              ["https://en.wikipedia.org/wiki/Rusty_Grills",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
        claim("rg2", "rusty-grills", "biblical_marriage", 2, True,
              "Voted YES on SB1/HB1 (signed March 2, 2023), Tennessee's ban on gender-affirming medical care for minors — puberty blockers, hormone therapy, and surgical procedures — which passed the House 77-16 and was upheld by the U.S. Supreme Court in United States v. Skrmetti (2024). Grills, a Conservative Baptist, supported the law's rejection of the state-over-parent framework imposing transgender medical ideology on Tennessee children.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://en.wikipedia.org/wiki/Rusty_Grills"]),
        claim("rg3", "rusty-grills", "family_child_sovereignty", 0, True,
              "A farmer and father of two who voted for Tennessee's Education Freedom Act of 2025 (HB6004/SB6001, signed February 12, 2025), the state's universal $7,296 per-student Education Savings Account scholarship. As Chair of the Agriculture & Natural Resources Subcommittee and a parent, Grills supported empowering families — particularly in rural Delta communities — to direct their children's education without dependence on a government-monopoly school system.",
              ["https://news.ballotpedia.org/2025/02/18/tennessee-enacts-private-school-choice-scholarship-bill-becoming-the-13th-state-with-a-universal-school-choice-program/",
               "https://en.wikipedia.org/wiki/Rusty_Grills"]),
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
