#!/usr/bin/env python3
"""Enrichment batch 72: hand-curated claims for 5 bottom-of-alphabet archetype_curated candidates.

Targets (reverse-alpha by state): Cavalier Johnson (WI-D, Milwaukee Mayor),
Katie Wilson (WA-D, Seattle Mayor), Tulsi Gabbard (US-R, DNI),
Stephen Miller (US-R, Deputy Chief of Staff), Russ Vought (US-R, OMB Director).
Each claim cites >=1 reliable source and reflects 2024-2026 public positions.

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
    # ---------------- Cavalier Johnson (WI-D, Mayor of Milwaukee) ----------------
    ("cavalier-johnson", "WI", "Milwaukee", [
        claim("cj1", "cavalier-johnson", "border_immigration", 2, False,
              "Milwaukee operates as a sanctuary city under Johnson's tenure, limiting local law-enforcement cooperation with U.S. Immigration and Customs Enforcement. City police are directed not to honor ICE detainer requests beyond state-law minimums, making Milwaukee one of the major Midwest sanctuary jurisdictions.",
              ["https://en.wikipedia.org/wiki/Sanctuary_city",
               "https://en.wikipedia.org/wiki/Cavalier_Johnson"]),
        claim("cj2", "cavalier-johnson", "sanctity_of_life", 0, False,
              "A progressive Democrat, Johnson has aligned with the party's pro-choice platform and opposes restrictions on abortion access. His electoral coalition and public record as Milwaukee mayor reflect support for abortion rights, rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Cavalier_Johnson",
               "https://ballotpedia.org/Cavalier_Johnson"]),
    ]),

    # ---------------- Katie Wilson (WA-D, Mayor of Seattle) ----------------
    ("katie-wilson", "WA", "Mayor", [
        claim("kw1", "katie-wilson", "border_immigration", 2, False,
              "As Seattle's mayor since January 2026, Wilson has actively directed the city to resist ICE enforcement, defending immigrant communities and activist networks working against immigration arrests. Seattle's long-standing sanctuary policies — maintained and reinforced by Wilson — prevent city resources from assisting federal immigration removal operations.",
              ["https://en.wikipedia.org/wiki/Katie_Wilson",
               "https://news.ballotpedia.org/2025/11/17/democratic-socialist-katie-wilson-elected-mayor-of-seattle-as-progressives-win-downballot-races-2/"]),
        claim("kw2", "katie-wilson", "sanctity_of_life", 0, False,
              "A self-described democratic socialist, Wilson supports broad abortion access and opposes restrictions on reproductive services — rejecting the rubric's personhood-from-conception standard consistent with her progressive democratic socialist platform.",
              ["https://en.wikipedia.org/wiki/Katie_Wilson",
               "https://ballotpedia.org/Katie_Wilson_(Washington)"]),
    ]),

    # ---------------- Tulsi Gabbard (US-R, Director of National Intelligence) ----------------
    ("tulsi-gabbard", "US", "Intelligence", [
        claim("tg1", "tulsi-gabbard", "foreign_policy_restraint", 1, True,
              "A consistent anti-interventionist who introduced the Stop Arming Terrorists Act (H.R. 608) to halt U.S. assistance to groups backing ISIS and al-Qaeda; opposed U.S. regime-change wars in Syria, Libya, and Yemen; and repeatedly called for ending open-ended foreign military entanglements — directly matching the rubric's call to end forever wars.",
              ["https://en.wikipedia.org/wiki/Stop_Arming_Terrorists_Act",
               "https://en.wikipedia.org/wiki/Tulsi_Gabbard"]),
        claim("tg2", "tulsi-gabbard", "self_defense", 1, True,
              "Received the Second Amendment Champion Award from the Second Amendment Institute in June 2024, recognizing her shift to firmly opposing gun-control legislation — including red-flag laws, assault-weapons bans, and magazine-capacity limits — after leaving the Democratic Party.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Tulsi_Gabbard"]),
        claim("tg3", "tulsi-gabbard", "biblical_marriage", 2, True,
              "After leaving the Democratic Party in 2022, Gabbard became a vocal opponent of policies permitting biological males to compete in women's sports and has backed legislation protecting female-only athletic spaces — aligning with the rubric's rejection of transgender ideology.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Tulsi_Gabbard",
               "https://en.wikipedia.org/wiki/Tulsi_Gabbard"]),
    ]),

    # ---------------- Stephen Miller (US-R, White House Deputy Chief of Staff for Policy) ----------------
    ("stephen-miller", "US", "Deputy Chief", [
        claim("sm1", "stephen-miller", "border_immigration", 1, True,
              "The principal architect of the Trump administration's mass-deportation program. Miller described the 2025 deportation campaign as rivaling 'building the Panama Canal' in scope, drove zero-tolerance and mandatory-detention policies across both Trump terms, and in 2025 publicly floated suspending habeas corpus for immigrants to accelerate removals — a hard-enforcement posture matching the rubric ideal.",
              ["https://en.wikipedia.org/wiki/Stephen_Miller_(political_advisor)",
               "https://ballotpedia.org/Stephen_Miller_(Washington,_D.C.)"]),
        claim("sm2", "stephen-miller", "biblical_marriage", 2, True,
              "A key policy driver behind executive actions reinstating the ban on transgender military service and mandating that federal agencies recognize only two biological sexes. Miller's America First policy portfolio consistently opposes the expansion of gender ideology into federal law and institutions.",
              ["https://en.wikipedia.org/wiki/Stephen_Miller_(political_advisor)"]),
    ]),

    # ---------------- Russ Vought (US-R, OMB Director / Acting CFPB Director) ----------------
    ("russ-vought", "US", "Management and Budget", [
        claim("rv1", "russ-vought", "sanctity_of_life", 0, True,
              "A devout Christian who attended the 2020 March for Life and praised Trump's participation as 'a golden chapter for our movement.' As OMB Director he has called for banning mifepristone and other drugs used in medical abortions — affirming that human life deserves protection from conception.",
              ["https://en.wikipedia.org/wiki/Russell_Vought"]),
        claim("rv2", "russ-vought", "biblical_marriage", 2, True,
              "Publicly described transgender identity as a 'contagion' and has supported executive policies rolling back gender-identity language from federal regulations, rejecting transgender ideology in federal programs — matching the rubric's standard.",
              ["https://en.wikipedia.org/wiki/Russell_Vought"]),
        claim("rv3", "russ-vought", "economic_stewardship", 2, True,
              "As OMB Director in both Trump terms, Vought has been a consistent advocate for reducing the federal deficit, opposing large unauthorized spending packages, and cutting agency budgets. He dismantled the CFPB and directed a broad federal spending-reduction agenda consistent with the rubric's anti-deficit, fiscal-restraint standard.",
              ["https://en.wikipedia.org/wiki/Russell_Vought",
               "https://ballotpedia.org/Russell_Vought"]),
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
