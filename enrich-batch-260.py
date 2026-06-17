#!/usr/bin/env python3
"""Enrichment batch 260: hand-curated claims for 5 federal candidates.

archetype_curated bucket exhausted; targets pulled from evidence_federal 0-claim pool,
bottom-of-alphabet: Herb Conaway (NJ-03-D), Nellie Pou (NJ-09-D), Mac Deford (SC-01-D),
Sam Forstag (MT-01-D), Pablo Jose Hernandez Rivera (PR-PPD, Resident Commissioner).
All claims sourced 2024-2026; all score False (do not align with rubric ideals).

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
    # ---------------- Herb Conaway (NJ-03, D, sitting U.S. Rep since Jan 2025) ----------------
    ("herb-conaway", "NJ", "NJ-03", [
        claim("hc1", "herb-conaway", "sanctity_of_life", 0, False,
              "As a New Jersey assemblyman (1998-2025), Conaway co-sponsored Assembly Bill 4848 (the Reproductive Freedom Act) and A3975 (protecting nondisclosure of abortion-patient information) — actively advancing abortion-access law and rejecting any legal protection of unborn life from conception.",
              ["https://www.herbforcongress.com/issues",
               "https://en.wikipedia.org/wiki/Herb_Conaway"]),
        claim("hc2", "herb-conaway", "self_defense", 1, False,
              "Endorsed by Everytown for Gun Safety Action Fund and Giffords PAC Courage to Fight Gun Violence, both organizations that champion red-flag laws, assault-style-weapons bans, and magazine-capacity limits — placing Conaway squarely against the rubric's defense of unrestricted Second Amendment rights.",
              ["https://legisletter.org/legislator/herb-conaway-C001136",
               "https://www.herbforcongress.com/issues"]),
        claim("hc3", "herb-conaway", "border_immigration", 2, False,
              "Stated that DHS 'has done absolutely nothing to rein in their reckless and poorly trained ICE agents' and framed federal immigration enforcement as making 'communities more dangerous' — opposing the strict interior-enforcement posture the rubric affirms.",
              ["https://conaway.house.gov/media"]),
    ]),

    # ---------------- Nellie Pou (NJ-09, D, sitting U.S. Rep since Jan 2025) ----------------
    ("nellie-pou", "NJ", "NJ-09", [
        claim("np1", "nellie-pou", "sanctity_of_life", 4, False,
              "Endorsed and actively supported by EMILY's List, the leading organization that exclusively recruits and funds pro-abortion women candidates — placing Pou inside the abortion-industry endorsement-and-money network the rubric tracks.",
              ["https://emilyslist.org/candidate/nellie-pou/",
               "https://en.wikipedia.org/wiki/Nellie_Pou"]),
        claim("np2", "nellie-pou", "sanctity_of_life", 0, False,
              "Publicly pledges to fight against 'anti-abortion extremists' and 'stand up for reproductive freedoms,' rejecting any legal recognition of unborn personhood from conception.",
              ["https://en.wikipedia.org/wiki/Nellie_Pou"]),
        claim("np3", "nellie-pou", "biblical_marriage", 0, False,
              "Criticized a colleague's opposition to same-sex marriage legislation as part of a 'war on women,' signaling consistent support for redefining marriage beyond the one-man-one-woman definition the rubric holds.",
              ["https://www.insidernj.com/pou-jumps-webber-sherrill-fight-decries-webbers-record-war-women/"]),
    ]),

    # ---------------- Mac Deford (SC-01, D, June 23 2026 runoff) ----------------
    ("mac-deford", "SC", "SC-01", [
        claim("md1", "mac-deford", "sanctity_of_life", 0, False,
              "Ran a 2026 campaign ad sharing a personal story and pledging explicitly to 'defend reproductive rights,' calling specifically for codifying Roe v. Wade into federal law — rejecting personhood-from-conception protection for the unborn.",
              ["https://abcnews4.com/news/local/mac-deford-shares-personal-story-in-new-campaign-ad-pledges-to-defend-reproductive-rights-abortion-democrat-republican-wciv-abc-news-4-2024",
               "https://defordforcongress.com/"]),
        claim("md2", "mac-deford", "self_defense", 1, False,
              "Supports universal background checks and red-flag laws that temporarily seize firearms from individuals deemed at risk — measures that conflict with the rubric's defense of unrestricted Second Amendment rights and opposition to red-flag confiscation.",
              ["https://abcnews4.com/news/local/coast-guard-veteran-mac-deford-prioritizes-constituent-access-and-transparency-in-2026-run-south-carolina-1st-congressional-district-wciv-abc-news-4-10-2-2025",
               "https://www.live5news.com/2025/08/22/we-palmetto-meet-candidate-mac-deford-sc01/"]),
    ]),

    # ---------------- Sam Forstag (MT-01, D, 2026 D NOMINEE) ----------------
    ("sam-forstag", "MT", "MT-01", [
        claim("sf1", "sam-forstag", "sanctity_of_life", 0, False,
              "Pledges to codify Roe v. Wade as federal law, expand funding for family-planning providers, and reverse Ryan Zinke's Medicaid restrictions on reproductive healthcare coverage — opposing personhood at conception.",
              ["https://samformontana.com/policies/",
               "https://projects.montanafreepress.org/election-guide-2026/candidates/sam-forstag/"]),
        claim("sf2", "sam-forstag", "border_immigration", 1, False,
              "Opposes mandatory deportation, calling for 'a real, achievable pathway' to legal status for undocumented immigrants and supports limiting local law-enforcement cooperation with federal ICE — rejecting the mass-deportation enforcement posture the rubric affirms.",
              ["https://samformontana.com/policies/",
               "https://www.mtpr.org/montana-news/2026-03-31/sam-forstag-interview"]),
    ]),

    # ---------------- Pablo Jose Hernandez Rivera (PR, PPD, sitting Resident Commissioner) ----------------
    ("pablo-jose-hernandez-rivera", "PR", "Commissioner", [
        claim("pjhr1", "pablo-jose-hernandez-rivera", "border_immigration", 1, False,
              "Co-pressed DHS in January 2025 to halt ICE operations he characterized as 'wrongful detentions' of documented individuals in Puerto Rico, and delivered a floor speech denouncing 'three blows of betrayal' against immigrant communities — opposing mandatory-deportation enforcement.",
              ["https://hernandez.house.gov/media/press-releases/hernandez-espaillat-press-dhs-ices-wrongful-detention-documented-individuals",
               "https://hernandez.house.gov/media/press-releases/resident-commissioner-pablo-jose-hernandez-denounces-puerto-rico-governments"]),
        claim("pjhr2", "pablo-jose-hernandez-rivera", "border_immigration", 2, False,
              "Publicly denounced Puerto Rico government cooperation with ICE enforcement operations as a betrayal of immigrant communities and a violation of civil rights — aligning with sanctuary-style non-cooperation that the rubric opposes.",
              ["https://hernandez.house.gov/media/press-releases/comisionado-residente-pablo-jose-hernandez-rivera-denuncia-la-traicion-del",
               "https://en.wikipedia.org/wiki/Pablo_Hern%C3%A1ndez_Rivera"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
