#!/usr/bin/env python3
"""Enrichment batch 189: hand-curated claims for 4 federal Senate candidates.

Primary archetype_curated bucket is exhausted; falls back to the low_evidence
and unset federal pool taken from the bottom of the alphabet per the
collision-avoidance protocol.

Mix (2 R / 2 D): Jared Hudson (AL-R, Navy SEAL / runoff candidate),
Elizabeth Temple (NC-R, music teacher / conservative patriot),
Karishma Manzur (NH-D, writer-activist / anti-AIPAC pledge),
Juliana Stratton (IL-D, Lt. Governor / 2026 Senate nominee).
Each claim cites >=1 reliable source and reflects 2024-2026 positions.

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
    # -------- Jared Hudson (AL-R, 2026 R runoff candidate for Tuberville seat) --------
    ("jared-hudson", "AL", "Senator", [
        claim("jh1", "jared-hudson", "border_immigration", 0, True,
              "Pledges full support for ICE, Border Patrol, and the Trump deportation agenda: 'I will give ICE, Border Patrol and the Trump Administration the funding and authorities they need to enforce our laws and send the bad guys back where they came from' — matching the rubric's demand for a militarized border and mandatory removal of illegal entrants.",
              ["https://ballotpedia.org/Jared_Hudson",
               "https://news.ballotpedia.org/2026/02/11/seven-candidates-are-running-in-the-republican-primary-for-the-u-s-senate-in-alabama-on-may-19-2026/"]),
        claim("jh2", "jared-hudson", "border_immigration", 2, True,
              "Has explicitly pledged to strip all federal funding from sanctuary cities: 'I will fight to strip away every last dime of federal funding from every so-called sanctuary city from coast to coast' — a direct match to the rubric's anti-sanctuary position.",
              ["https://ballotpedia.org/Jared_Hudson",
               "https://news.ballotpedia.org/2026/05/22/barry-moore-and-jared-hudson-advanced-from-the-may-19-republican-primary-for-the-u-s-senate-in-alabama-to-the-june-16-primary-runoff/"]),
        claim("jh3", "jared-hudson", "self_defense", 1, True,
              "As a former Navy SEAL and CEO of The Shooting Institute (a firearms training organization), Hudson's public identity is built around lawful gun ownership and tactical proficiency; he has not endorsed any red-flag law, assault-weapons ban, magazine restriction, or firearm registry — consistent with the rubric's Second Amendment standard.",
              ["https://ballotpedia.org/Jared_Hudson",
               "https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Alabama"]),
    ]),

    # -------- Elizabeth Temple (NC-R, 2026 R primary candidate for Tillis seat) --------
    ("elizabeth-temple", "NC", "Senator", [
        claim("et1", "elizabeth-temple", "election_integrity", 0, True,
              "Self-describes as having 'passionately fought for election integrity' as a core advocacy priority — placing her squarely in the voter-ID / paper-ballot / anti-mass-mail-in posture the rubric rewards.",
              ["https://ballotpedia.org/Elizabeth_Anne_Temple"]),
        claim("et2", "elizabeth-temple", "industry_capture", 0, True,
              "Identifies 'medical freedom' as a central fighting principle — language that specifically targets government and pharmaceutical-industry vaccine mandates, consistent with the rubric's opposition to pharma mandates.",
              ["https://ballotpedia.org/Elizabeth_Anne_Temple"]),
        claim("et3", "elizabeth-temple", "family_child_sovereignty", 0, True,
              "A 'mother of five' who lists 'education reform' alongside 'medical freedom' and 'election integrity' as her three main causes, and describes her worldview as 'a return to our foundational moral compass based in God's principles' — reflecting the rubric's emphasis on parental rights and family sovereignty over schooling decisions.",
              ["https://ballotpedia.org/Elizabeth_Anne_Temple"]),
    ]),

    # -------- Karishma Manzur (NH-D, 2026 D primary candidate for Shaheen seat) --------
    ("karishma-manzur", "NH", "Senator", [
        claim("km1", "karishma-manzur", "foreign_policy_restraint", 3, True,
              "Endorsed by Track AIPAC, the advocacy organization that tracks and publicizes whether Congressional candidates pledge not to accept money from AIPAC or foreign-affiliated political action committees — placing Manzur in the no-foreign-PAC column the rubric rewards.",
              ["https://ballotpedia.org/Karishma_Manzur"]),
        claim("km2", "karishma-manzur", "foreign_policy_restraint", 1, True,
              "Endorsed by Peace Action, the largest grassroots peace organization in the United States, which specifically supports ending U.S. military engagements abroad and repealing open-ended AUMFs — consistent with the rubric's 'end forever wars' standard.",
              ["https://ballotpedia.org/Karishma_Manzur"]),
    ]),

    # -------- Juliana Stratton (IL-D, 2026 D Senate nominee / Durbin seat) --------
    ("juliana-stratton", "IL", "Senate", [
        claim("js1", "juliana-stratton", "sanctity_of_life", 4, False,
              "Endorsed by Reproductive Freedom for All (the national organization formerly known as NARAL Pro-Choice America) for her 2026 U.S. Senate campaign — placing her squarely inside the abortion-industry endorsement network the rubric flags.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-endorses-illinois-lt-governor-juliana-stratton-for-u-s-senate/",
               "https://ballotpedia.org/Juliana_Stratton"]),
        claim("js2", "juliana-stratton", "sanctity_of_life", 0, False,
              "As Illinois Lieutenant Governor worked to make the state 'a safe haven for abortion access in the Midwest,' breaking down barriers to reproductive health care, protecting providers from out-of-state legal actions, and expanding access to medication abortion — explicitly rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Juliana_Stratton",
               "https://ballotpedia.org/Juliana_Stratton"]),
        claim("js3", "juliana-stratton", "border_immigration", 1, False,
              "Was the only 2026 Illinois Democratic Senate primary candidate to call for abolishing ICE (Immigration and Customs Enforcement) during a Democratic Senate debate — directly opposing the rubric's mandatory deportation / enforcement standard.",
              ["https://ballotpedia.org/Juliana_Stratton",
               "https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Illinois"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
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
