#!/usr/bin/env python3
"""Enrichment batch 190: hand-curated claims for 5 sitting CA U.S. Representatives.

Targets evidence_federal representatives with 0 claims (bottom-of-alphabet
bucket exhausted for senators; fallback to representatives). All are sitting
Democratic members with public voting records. 2-3 claims each spanning
distinct rubric categories, sourced from official .gov, Wikipedia, GovTrack,
and Ballotpedia.

Targets: Mark DeSaulnier (CA-10-D), Juan Vargas (CA-52-D),
         Josh Harder (CA-09-D), Ami Bera (CA-06-D), John Garamendi (CA-08-D).

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
    # ---------------- Mark DeSaulnier (CA-10, D, US Representative) ----------------
    ("mark-desaulnier", "CA", "Representative", [
        claim("md1", "mark-desaulnier", "sanctity_of_life", 0, False,
              "Consistently pro-choice and holds an F grade from SBA Pro-Life America. Called the Supreme Court's 2022 Dobbs v. Jackson decision 'an assault on the freedom of all women and an attack on equality,' and supports federal legislation to codify abortion access nationwide — rejecting any recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Mark_DeSaulnier",
               "https://ballotpedia.org/Mark_DeSaulnier"]),
        claim("md2", "mark-desaulnier", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (H.R. 8404) in July 2022 and the Senate-amended version in December 2022, which codified federal recognition of same-sex marriage and repealed the Defense of Marriage Act — rejecting the one-man/one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://desaulnier.house.gov/legislation"]),
        claim("md3", "mark-desaulnier", "self_defense", 1, False,
              "A gun-control advocate who, as a California State Senator, authored AB 2235 requiring biometric safety features on all new handguns sold in California; in Congress he has consistently supported federal gun-safety legislation, including background-check expansions and weapon restrictions that oppose the rubric's position against new firearms regulations.",
              ["https://ballotpedia.org/Mark_DeSaulnier",
               "https://desaulnier.house.gov/legislation"]),
    ]),

    # ---------------- Juan Vargas (CA-52, D, US Representative) ----------------
    ("juan-vargas", "CA", "Representative", [
        claim("jv1", "juan-vargas", "sanctity_of_life", 0, False,
              "Holds a 100% rating from Reproductive Freedom for All (successor to NARAL) and an F from SBA Pro-Life America. Condemned the Dobbs decision as 'fundamentally wrong and extremely disappointing, impacting millions of women across the country,' and supports codifying abortion rights into federal law — rejecting personhood from conception.",
              ["https://en.wikipedia.org/wiki/Juan_Vargas",
               "https://ballotpedia.org/Juan_Vargas"]),
        claim("jv2", "juan-vargas", "biblical_marriage", 0, False,
              "A member of the House Equality Caucus who voted for the Respect for Marriage Act in 2022, federally codifying same-sex marriage and repealing the Defense of Marriage Act; his official issues page states he is 'committed to ensuring respect, dignity, and safety for the LGBTQ+ community' — rejecting the one-man/one-woman marriage standard.",
              ["https://vargas.house.gov/issues/protecting-rights-and-freedoms",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
        claim("jv3", "juan-vargas", "border_immigration", 1, False,
              "In February 2025 Vargas joined a protest against the Trump administration's immigration enforcement campaign, standing alongside Cardinal Robert McElroy and other religious leaders to oppose mass deportation operations — opposing mandatory deportation of illegal aliens.",
              ["https://en.wikipedia.org/wiki/Juan_Vargas",
               "https://ballotpedia.org/Juan_Vargas"]),
    ]),

    # ---------------- Josh Harder (CA-09, D, US Representative) ----------------
    ("josh-harder", "CA", "Representative", [
        claim("jh1", "josh-harder", "sanctity_of_life", 0, False,
              "Supports legal abortion rights and has advocated for protecting abortion access at the federal level, opposing any personhood-from-conception standard or ban on abortion procedures.",
              ["https://en.wikipedia.org/wiki/Josh_Harder",
               "https://ballotpedia.org/Josh_Harder"]),
        claim("jh2", "josh-harder", "self_defense", 1, False,
              "Voted for the Protecting Our Kids Act (H.R. 7910, 2022), a gun-safety package including assault-style weapon restrictions, enhanced background checks, and safe-storage mandates — supporting the class of firearm regulations the rubric opposes.",
              ["https://harder.house.gov/media/press-releases/harder-votes-to-pass-commonsense-gun-safety-bill",
               "https://ballotpedia.org/Josh_Harder"]),
        claim("jh3", "josh-harder", "border_immigration", 1, True,
              "One of 46 House Democrats to cross the aisle and vote for the Laken Riley Act (S. 5, signed into law January 29, 2025), which requires DHS to detain — without bond — non-citizens arrested for, charged with, or admitting to crimes including theft, burglary, and assault on law enforcement. His vote aligned with the rubric's support for mandatory immigration enforcement.",
              ["https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://www.govtrack.us/congress/votes/119-2025/h23"]),
    ]),

    # ---------------- Ami Bera (CA-06, D, US Representative) ----------------
    ("ami-bera", "CA", "Representative", [
        claim("ab1", "ami-bera", "sanctity_of_life", 0, False,
              "Identifies as pro-choice and condemned the 2022 Dobbs decision as 'a blow to women's rights and reproductive health care.' Supports federal legislation to protect abortion access and has opposed any congressional effort to restrict abortion at the federal level — rejecting personhood from conception.",
              ["https://en.wikipedia.org/wiki/Ami_Bera",
               "https://ballotpedia.org/Ami_Bera"]),
        claim("ab2", "ami-bera", "self_defense", 1, False,
              "Voted for the Protecting Our Kids Act (H.R. 7910) in 2022, a bipartisan gun-safety bill that included restrictions on semi-automatic firearms, enhanced background checks, and other limitations — measures the rubric treats as impermissible infringements on Second Amendment rights.",
              ["https://bera.house.gov/news/press-releases/rep-bera-votes-for-bipartisan-commonsense-gun-violence-prevention-legislation",
               "https://ballotpedia.org/Ami_Bera"]),
        claim("ab3", "ami-bera", "border_immigration", 0, False,
              "Denounced a Republican border-security bill as 'partisan' while calling for alternative solutions, opposing the wall-and-military-enforcement posture the rubric favors; he has resisted strict border-enforcement legislation framed as one-sided.",
              ["https://bera.house.gov/news/documentsingle.aspx?DocumentID=399564",
               "https://ballotpedia.org/Ami_Bera"]),
    ]),

    # ---------------- John Garamendi (CA-08, D, US Representative) ----------------
    ("john-garamendi", "CA", "Representative", [
        claim("jg1", "john-garamendi", "sanctity_of_life", 0, False,
              "Supports abortion access as a 'fundamental human right to bodily autonomy,' calling the Dobbs decision 'devastating.' He backs federal legislation to restore and codify nationwide abortion access, rejecting personhood from conception.",
              ["https://en.wikipedia.org/wiki/John_Garamendi",
               "https://ballotpedia.org/John_Garamendi"]),
        claim("jg2", "john-garamendi", "border_immigration", 1, False,
              "Co-introduced the Freeze ICE Act (with Rep. Lizzie Fletcher and nine colleagues) to stop rapid recruitment of unvetted personnel at Immigration and Customs Enforcement; additionally voted NO on the FY2026 Homeland Security Appropriations Act funding DHS and ICE enforcement operations — opposing mandatory immigration enforcement the rubric favors.",
              ["https://garamendi.house.gov/media/press-releases",
               "https://ballotpedia.org/John_Garamendi"]),
        claim("jg3", "john-garamendi", "foreign_policy_restraint", 1, False,
              "Voted for and applauded passage of the April 2024 $95 billion Ukraine, Israel, and Pacific allies foreign-security package, stating it was 'vital' for the U.S. to 'stand by the brave people of Ukraine in their fight for freedom and democracy' — supporting open-ended foreign military commitments the rubric opposes.",
              ["https://garamendi.house.gov/media/press-releases/garamendi-releases-statement-passage-national-security-bills-ukraine-israel",
               "https://en.wikipedia.org/wiki/John_Garamendi"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
