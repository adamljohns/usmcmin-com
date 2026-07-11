#!/usr/bin/env python3
"""Enrichment batch 636: hand-curated claims for 2 Oklahoma State Senators.

Senators: Ally Seifried (SD-2), Avery Frix (SD-9).
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
    # --- Ally Seifried (OK SD-2, State Senator — in office since Nov 2022) ---
    ("ally-seifried", "OK", "State Senator", [
        claim("as1", "ally-seifried", "sanctity_of_life", 0, True,
              "Seifried voted YES on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to a person intending to use them to cause an unlawful abortion; the Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://oksenate.gov/press-releases/senate-gives-final-passage-bill-creating-crime-abortion-pill-trafficking",
               "https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM"]),
        claim("as2", "ally-seifried", "family_child_sovereignty", 0, True,
              "Seifried voted YES on SB 613 (2023), authored by Sen. Julie Daniels, banning gender-transition procedures for minors in Oklahoma — including puberty blockers, cross-sex hormone therapy, and surgical interventions — with civil enforcement and professional license revocation provisions; the Senate passed it 37-8 on April 27, 2023, and Gov. Stitt signed it May 1, 2023.",
              ["https://oksenate.gov/press-releases/senate-approves-bill-prohibiting-gender-transition-procedures-minors",
               "https://legiscan.com/OK/bill/SB613/2023"]),
        claim("as3", "ally-seifried", "christian_liberty", 0, True,
              "Seifried voted YES on SB 658 (2025), prohibiting the Oklahoma Department of Human Services from excluding foster or adoptive parent candidates based solely on their deeply-held religious or moral beliefs about sexual orientation or gender identity; the Senate passed it 38-7 and Gov. Stitt signed it effective November 1, 2025.",
              ["https://oksenate.gov/press-releases/bill-recruit-foster-parents-becomes-law",
               "https://ocpathink.org/post/independent-journalism/oklahoma-senate-approves-protections-for-christian-foster-parents"]),
    ]),

    # --- Avery Frix (OK SD-9, State Senator — in office since Nov 2024; former House member) ---
    ("avery-frix", "OK", "State Senator", [
        claim("af1", "avery-frix", "sanctity_of_life", 0, True,
              "Frix was a named Senate co-author of SB 456 (2025), the Abolition of Abortion Act, which would have extended 14th Amendment equal protection to unborn children and classified abortion as homicide; the bill also co-authored by Sen. Dusty Deevers gained historic legislative support before failing in committee 6-2. Frix also voted YES on HB 1168 (2026) making abortion-drug trafficking a felony (37-10 Senate vote, Gov. Stitt signed May 5, 2026).",
              ["https://oksenate.gov/press-releases/deevers-introduces-slate-legislation-restore-moral-sanity-oklahoma",
               "https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM"]),
        claim("af2", "avery-frix", "family_child_sovereignty", 0, True,
              "Frix voted YES on HB 3586 (2026), the Right to Raise Act, prohibiting DHS and courts from denying foster or adoptive placement to parents based on their refusal to affirm a child's claimed gender identity contrary to biological sex, and clarifying that declining to use opposite-sex pronouns or support gender transition is not child abuse or neglect; the Senate passed it 39-7 and Gov. Stitt signed it.",
              ["https://ocpathink.org/post/independent-journalism/legislature-passes-bill-shielding-oklahoma-parents-who-decline-transgender-affirmation",
               "https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB3586_VOTES.HTM"]),
        claim("af3", "avery-frix", "border_immigration", 0, True,
              "Frix authored SB 868 (2025), the Prohibition on Sanctuary Policies for Illegal Immigration Act, which would prohibit sanctuary city policies in Oklahoma, require all county correctional facilities to enter immigration detainer agreements with federal agencies, and mandate state law enforcement cooperation with federal immigration enforcement; the bill advanced through the Senate Judiciary Committee.",
              ["https://oksenate.gov/press-releases/senate-advances-frix-bill-prohibiting-sanctuary-cities",
               "https://www.oklegislature.gov/BillInfo.aspx?Bill=sb868&Session=2500"]),
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
