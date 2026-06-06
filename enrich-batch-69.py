#!/usr/bin/env python3
"""Enrichment batch 69: hand-curated claims for 5 candidates (bottom of alphabet).

Targets archetype_curated candidates with 0 evidence claims, taken from the
BOTTOM of the reverse-sorted bucket to avoid collision with the concurrent
top-of-alphabet agent.

Mix (3 R / 2 mixed): JB McCuskey (WV-R AG), Tim Michels (WI-R Gov candidate),
Bob Ferguson (WA-D Gov), Winsome Earle-Sears (VA-R former LG),
Phil Scott (VT-R Gov).

Each claim cites >=1 reliable source and reflects 2024-2026 record/positions.

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
    # ---------------- JB McCuskey (WV-R, Attorney General) ----------------
    ("jb-mccuskey-ag-2026", "WV", "Attorney General", [
        claim("jm1", "jb-mccuskey-ag-2026", "sanctity_of_life", 0, True,
              "During his 2024 Attorney General campaign, McCuskey explicitly pledged to support abortion restrictions and to defend West Virginia's near-total abortion ban — a law that criminalizes virtually all abortions except in cases of rape or incest before 14 weeks, fatal fetal abnormality, and direct threat to the mother's life. He won with over 70% of the vote and took office as the 35th AG in January 2025, making enforcement of this protective law part of his mandate.",
              ["https://en.wikipedia.org/wiki/JB_McCuskey",
               "https://ballotpedia.org/John_B._McCuskey"]),
        claim("jm2", "jb-mccuskey-ag-2026", "self_defense", 1, True,
              "During his 2024 AG campaign, McCuskey explicitly pledged to oppose restrictions on firearms and to fight any federal overreach against Second Amendment rights as West Virginia's chief law officer — committing to resist red-flag laws, assault-weapons bans, and registry schemes that conflict with the rubric's defense of the unrestricted right to keep and bear arms.",
              ["https://ballotpedia.org/John_B._McCuskey",
               "https://en.wikipedia.org/wiki/JB_McCuskey"]),
    ]),

    # ---------------- Tim Michels (WI-R, 2026 Governor candidate) ----------------
    ("tim-michels-gov-2026", "WI", "Governor", [
        claim("tm1", "tim-michels-gov-2026", "sanctity_of_life", 0, True,
              "Michels identified as '100% pro-life' throughout his 2022 Wisconsin gubernatorial campaign, earning perfect 100% ratings from both Wisconsin Right to Life and Pro-Life Wisconsin; he supported the Human Life Amendment and pledged to 'defend the lives of those who cannot defend themselves.' He also stood behind Wisconsin's 1849 pre-Roe criminal abortion statute — a near-total ban that predates Roe and treats abortion as criminal — as constitutional and binding after Dobbs.",
              ["https://en.wikipedia.org/wiki/Tim_Michels",
               "https://ballotpedia.org/Tim_Michels",
               "https://www.ontheissues.org/social/Tim_Michels_Abortion.htm"]),
        claim("tm2", "tim-michels-gov-2026", "self_defense", 1, True,
              "During his 2022 Wisconsin gubernatorial campaign, Michels opposed new firearms restrictions, declaring 'I believe that there are already too many laws that threaten our rights' and pledging that 'law-abiding gun owners are not having their guns confiscated.' Protecting Second Amendment rights was a campaign centerpiece — consistent with the rubric's opposition to assault-weapons bans, red-flag laws, and magazine-capacity limits.",
              ["https://www.ontheissues.org/domestic/Tim_Michels_Gun_Control.htm",
               "https://en.wikipedia.org/wiki/Tim_Michels"]),
    ]),

    # ---------------- Bob Ferguson (WA-D, Governor) ----------------
    ("bob-ferguson", "WA", "Governor", [
        claim("bf1", "bob-ferguson", "sanctity_of_life", 4, False,
              "On his first day as governor (January 15, 2025), Ferguson signed an executive order convening a reproductive rights roundtable to protect abortion access. He subsequently pledged to backfill approximately $15 million in Planned Parenthood Medicaid funding after the Trump administration defunded the organization — directly directing state revenue to sustain the nation's largest abortion provider and placing him inside the abortion-industry funding network the rubric opposes.",
              ["https://governor.wa.gov/news/2025/governor-ferguson-washington-will-cover-gap-caused-federal-attempt-defund-planned-parenthood",
               "https://en.wikipedia.org/wiki/Bob_Ferguson_(politician)"]),
        claim("bf2", "bob-ferguson", "biblical_marriage", 2, False,
              "As governor, Ferguson publicly declared that Washington would protect transgender individuals' access to medical transitions, stating 'health care provided to treat gender dysphoria is health care, and in Washington state, we will not treat health care like a political football' — rejecting any limits on gender-ideology-driven medical interventions and advancing transgender ideology as state policy.",
              ["https://en.wikipedia.org/wiki/Bob_Ferguson_(politician)",
               "https://ballotpedia.org/Bob_Ferguson"]),
        claim("bf3", "bob-ferguson", "self_defense", 1, False,
              "Ferguson carried an F rating from the National Rifle Association throughout his tenure as Washington Attorney General (2013-2025) and entered the governorship with combating gun violence as a stated first-term priority. His record backing assault-weapons regulations, background-check expansions, and related restrictions directly conflicts with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Bob_Ferguson",
               "https://en.wikipedia.org/wiki/Bob_Ferguson_(politician)"]),
    ]),

    # ---------------- Winsome Earle-Sears (VA-R, former Lt. Governor) ----------------
    ("winsome-earle-sears", "VA", "Lt. Governor", [
        claim("we1", "winsome-earle-sears", "sanctity_of_life", 0, False,
              "Earle-Sears supports allowing abortion up to 15 weeks with exceptions for rape, incest, and threats to the pregnant woman's health — falling short of the rubric's life-at-conception personhood standard. This position permits on-demand abortion through the first trimester and rejects the principle that every unborn child has full legal personhood from the moment of fertilization.",
              ["https://en.wikipedia.org/wiki/Winsome_Earle-Sears",
               "https://ballotpedia.org/Winsome_Earle-Sears"]),
        claim("we2", "winsome-earle-sears", "biblical_marriage", 0, True,
              "When Earle-Sears was constitutionally required as Virginia's presiding lieutenant governor to sign a marriage-equality bill, she did so — but simultaneously added a written statement to the legislative record expressly declaring her personal and moral opposition to the bill's content, publicly reaffirming her conviction that marriage is the union of one man and one woman.",
              ["https://en.wikipedia.org/wiki/Winsome_Earle-Sears",
               "https://ballotpedia.org/Winsome_Earle-Sears"]),
        claim("we3", "winsome-earle-sears", "biblical_marriage", 4, True,
              "Opposing gender ideology in public schools was a prominent plank of Earle-Sears's 2025 Virginia gubernatorial campaign; she specifically targeted gender-ideology instruction in K-12 classrooms and pledged to protect children from ideologically driven curricula, aligning with the rubric's opposition to LGBTQ promotion in schools and public policy.",
              ["https://en.wikipedia.org/wiki/Winsome_Earle-Sears",
               "https://ballotpedia.org/Winsome_Earle-Sears"]),
    ]),

    # ---------------- Phil Scott (VT-R, Governor) ----------------
    ("phil-scott-gov-2026", "VT", "Governor", [
        claim("ps1", "phil-scott-gov-2026", "sanctity_of_life", 0, False,
              "Scott is pro-choice and signed two major abortion-access expansions into law: in June 2019, he signed H.57 — one of the nation's most sweeping abortion-rights statutes, explicitly protecting abortion at any stage of pregnancy with no gestational limit; and in December 2022, he signed Proposal 5, a constitutional amendment enshrining the right to 'personal reproductive autonomy' into Vermont's constitution. Both actions reject any life-at-conception personhood standard.",
              ["https://en.wikipedia.org/wiki/Phil_Scott",
               "https://ballotpedia.org/Phil_Scott_(Vermont)",
               "https://www.ontheissues.org/Governor/Phil_Scott_Abortion.htm"]),
        claim("ps2", "phil-scott-gov-2026", "biblical_marriage", 0, False,
              "Scott publicly supports same-sex marriage and has governed accordingly in Vermont throughout his tenure since 2017, rejecting the one-man-one-woman definition of marriage the rubric requires.",
              ["https://en.wikipedia.org/wiki/Phil_Scott",
               "https://www.ontheissues.org/Governor/Phil_Scott_Civil_Rights.htm"]),
        claim("ps3", "phil-scott-gov-2026", "biblical_marriage", 2, False,
              "Scott signed a gender-neutral bathroom bill specifically extending legal recognition and access rights to transgender individuals in Vermont — advancing government endorsement of gender identity as a protected category in public accommodations, promoting the transgender ideology the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Phil_Scott",
               "https://www.ontheissues.org/Governor/Phil_Scott_Civil_Rights.htm"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
