#!/usr/bin/env python3
"""Enrichment batch 638: hand-curated claims for 2 Oklahoma State Senators.

Senators: Darrell Weaver (SD-24), David Bullard (SD-6).
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
    # --- Darrell Weaver (OK SD-24, State Senator — former Bureau of Narcotics director) ---
    ("darrell-weaver", "OK", "State Senator", [
        claim("dw1", "darrell-weaver", "sanctity_of_life", 0, True,
              "Weaver was a named co-author of HB 4327 (2022), Oklahoma's civil-enforcement abortion ban prohibiting abortion from the moment of fertilization with a private right of action (Texas-model) against providers; the Senate passed it 35-10 on April 28, 2022, and Gov. Stitt signed it May 25, 2022.",
              ["https://oksenate.gov/press-releases/full-senate-approves-legislation-giving-greater-protection-lives-unborn-babies",
               "https://legiscan.com/OK/text/HB4327/id/2587278"]),
        claim("dw2", "darrell-weaver", "biblical_marriage", 2, True,
              "Weaver was a named co-author of SB 2 (2022), the Save Women's Sports Act, prohibiting biologically male athletes from competing on school athletic teams designated for females at any Oklahoma K-12 school or university; the Senate passed it 37-7 and Gov. Stitt signed it March 30, 2022.",
              ["https://oksenate.gov/press-releases/senate-supports-science-measures-affirming-biological-sex-birth-and-its-importance",
               "https://legiscan.com/OK/bill/SB2/2022"]),
        claim("dw3", "darrell-weaver", "public_justice", 0, True,
              "Weaver was the prime author of SB 1280 (2024), adding the crime of mixing fentanyl into other substances to Oklahoma statutes carrying penalties of 7 years to life imprisonment and fines up to $50,000+; the Senate passed it 44-0 on February 15, 2024. Weaver drew on his background as former director of the Oklahoma Bureau of Narcotics in authoring the bill.",
              ["https://oksenate.gov/press-releases/senator-weavers-bill-combat-fentanyl-manufacturing-unanimously-passes-senate-public",
               "https://www.kswo.com/2024/03/16/oklahoma-senate-passes-bill-strengthening-punishments-against-manufacturing-fentanyl/"]),
    ]),

    # --- David Bullard (OK SD-6, State Senator — SE Oklahoma) ---
    ("david-bullard", "OK", "State Senator", [
        claim("db1", "david-bullard", "sanctity_of_life", 0, True,
              "Bullard was the Senate prime author of HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly traffic abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them for an unlawful abortion; Bullard called it 'the most important legislation we've passed all session.' The Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking",
               "https://okcfox.com/news/local/gov-stitt-signs-hb-1168-making-abortion-pill-trafficking-a-felony-in-oklahoma"]),
        claim("db2", "david-bullard", "border_immigration", 0, True,
              "Bullard was the prime author of SB 212 (2023), prohibiting non-U.S. citizens from owning Oklahoma land directly or through business entities or trusts, and requiring an affidavit on every recorded deed; the Senate passed it 40-6 and the governor signed it into law.",
              ["https://oksenate.gov/press-releases/bill-stop-illegal-purchases-oklahoma-land-heads-governor",
               "https://oksenate.gov/press-releases/senate-votes-strengthen-law-against-illegal-foreign-ownership-oklahoma-land"]),
        claim("db3", "david-bullard", "family_child_sovereignty", 0, True,
              "Bullard co-authored SB 613 (2023), banning gender-transition procedures for minors in Oklahoma — including puberty blockers, cross-sex hormones, and surgical interventions — with civil enforcement and license revocation provisions; the Senate passed it 37-8 on April 27, 2023, and Gov. Stitt signed it May 1, 2023. Bullard also issued a public statement praising the federal ruling upholding the law.",
              ["https://oksenate.gov/press-releases/senate-approves-bill-prohibiting-gender-transition-procedures-minors",
               "https://oksenate.gov/press-releases/sen-bullard-statement-federal-ruling-affirming-sb-613"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
