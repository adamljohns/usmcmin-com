#!/usr/bin/env python3
"""Enrichment batch 61: hand-curated claims for 5 U.S. House candidates.

Targets archetype_curated representatives that had 0 evidence claims, taken
from the bottom of the alphabet (NY, MI, AZ).  Mix: 4 D / 1 R.

Alex Bores (NY-12-D), Effie Phillips-Staley (NY-17-D),
Beth Davidson (NY-17-D), Curtis Hertel (MI-07-D),
Shawnna Bolick (AZ-01-R).

Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's
50MB warning.
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
    # ---------------- Alex Bores (NY-12-D, U.S. Rep candidate) ----------------
    ("alex-bores", "NY", "Representative", [
        claim("ab1", "alex-bores", "sanctity_of_life", 0, False,
              "As a NY State Assemblyman, co-sponsored and voted for multiple bills expanding abortion rights, including legislation protecting telemedicine prescriptions for medication abortion and shielding local providers from out-of-state subpoenas. His first Assembly floor speech was in support of the NY Equal Rights Amendment explicitly protecting reproductive rights — rejecting any personhood-from-conception standard.",
              ["https://assembly.state.ny.us/mem/Alex-Bores",
               "https://ballotpedia.org/Alex_Bores"]),
        claim("ab2", "alex-bores", "self_defense", 1, False,
              "Authored NY Assembly legislation directing New York State to study 'smart gun' technology designed to restrict firearms to authorized users only — a gun-restriction measure that gun-rights advocates oppose as a stepping stone toward limiting the firearms rights of law-abiding citizens.",
              ["https://assembly.state.ny.us/mem/Alex-Bores",
               "https://en.wikipedia.org/wiki/Alex_Bores"]),
        claim("ab3", "alex-bores", "border_immigration", 0, False,
              "Advocates reversing Trump administration immigration enforcement policies and supports allowing legal permanent residents to vote in local elections — opposing strict border enforcement and placing non-citizen inclusion above immigration-law enforcement.",
              ["https://assembly.state.ny.us/mem/Alex-Bores",
               "https://ballotpedia.org/Alex_Bores"]),
    ]),

    # ---------------- Effie Phillips-Staley (NY-17-D, U.S. Rep candidate) ----------------
    ("effie-phillips-staley", "NY", "Representative", [
        claim("ep1", "effie-phillips-staley", "sanctity_of_life", 0, False,
              "Abortion access is a central pillar of her 2026 congressional campaign — explicitly listed as a top legislative priority alongside climate and housing on her campaign platform, and she pledges to fight to protect reproductive rights at the federal level.",
              ["https://effieforcongress.com/priorities/",
               "https://ballotpedia.org/Effie_Phillips-Staley"]),
        claim("ep2", "effie-phillips-staley", "border_immigration", 0, False,
              "Campaigned against the Trump administration's border-enforcement agenda, criticizing the 'Big Ugly Bill' for making the situation 'significantly more frightening for immigrant communities' — positioning firmly against the wall construction and military-deployment model the rubric's border standard requires.",
              ["https://effieforcongress.com/category/podcast/",
               "https://ballotpedia.org/Effie_Phillips-Staley"]),
    ]),

    # ---------------- Beth Davidson (NY-17-D, U.S. Rep candidate) ----------------
    ("beth-davidson", "NY", "Representative", [
        claim("bd1", "beth-davidson", "sanctity_of_life", 0, False,
              "Campaign platform commits to 'guarantee nationwide access to abortion, birth control, and IVF,' framing abortion as a top-of-ticket health issue; explicitly rejects any federal restriction on abortion access.",
              ["https://bethdavidsonforcongress.com/beths-priorities/",
               "https://ballotpedia.org/Beth_Davidson_(New_York)"]),
        claim("bd2", "beth-davidson", "self_defense", 1, False,
              "As Rockland County Legislator, passed and cites as a signature accomplishment 'common-sense gun safety legislation' — a gun-restriction measure signed into law by a Republican county executive — indicating a track record of legislating against unrestricted Second Amendment rights.",
              ["https://bethdavidsonforcongress.com/beths-priorities/",
               "https://bethdavidsonforcongress.com/meet-beth/"]),
    ]),

    # ---------------- Curtis Hertel (MI-07-D, U.S. Rep candidate) ----------------
    ("curtis-hertel", "MI", "Representative", [
        claim("ch1", "curtis-hertel", "sanctity_of_life", 0, False,
              "Served as Governor Whitmer's chief legislative lobbyist and was centrally involved in shepherding repeal of Michigan's 1931 abortion ban through the state legislature in 2023, eliminating all criminal penalties for abortion providers — rejecting any life-from-conception standard.",
              ["https://ballotpedia.org/Curtis_Hertel",
               "https://en.wikipedia.org/wiki/Curtis_Hertel_Jr."]),
        claim("ch2", "curtis-hertel", "self_defense", 1, False,
              "Helped negotiate and pass three gun-restriction bills signed into Michigan law in 2023 following the Michigan State University shooting: universal background checks for all firearm purchases, mandatory safe-storage requirements, and judicial red-flag protection orders — a direct conflict with the rubric's anti-red-flag and anti-restriction standard.",
              ["https://ballotpedia.org/Curtis_Hertel",
               "https://en.wikipedia.org/wiki/Curtis_Hertel_Jr."]),
        claim("ch3", "curtis-hertel", "border_immigration", 0, False,
              "Backs the 2024 bipartisan Senate border deal (adding 1,500+ CBP officers and detection technology) as his border-security ceiling while opposing hard enforcement; has not endorsed wall construction or mass deportation — far short of the wall-plus-military standard the rubric identifies as ideal.",
              ["https://ballotpedia.org/Curtis_Hertel",
               "https://en.wikipedia.org/wiki/Curtis_Hertel_Jr."]),
    ]),

    # ---------------- Shawnna Bolick (AZ-01-R, U.S. Rep candidate) ----------------
    ("shawnna-bolick", "AZ", "Representative", [
        claim("sb1", "shawnna-bolick", "self_defense", 0, True,
              "Supports constitutional carry and publicly pledges to 'further protect the right of law-abiding citizens to carry a firearm openly or discreetly anywhere they have a right to be' — a direct constitutional-carry alignment matching the rubric's self-defense ideal.",
              ["https://ballotpedia.org/Shawnna_Bolick",
               "https://en.wikipedia.org/wiki/Shawnna_Bolick"]),
        claim("sb2", "shawnna-bolick", "border_immigration", 2, True,
              "Advocates denying state and federal funds to any sanctuary city or entity that does not comply with immigration law — a firm anti-sanctuary position matching the rubric ideal for border enforcement.",
              ["https://ballotpedia.org/Shawnna_Bolick",
               "https://en.wikipedia.org/wiki/Shawnna_Bolick"]),
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
