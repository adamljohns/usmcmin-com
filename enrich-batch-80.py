#!/usr/bin/env python3
"""Enrichment batch 80: hand-curated claims for 5 state candidates (bottom of alphabet).

Targets archetype_curated candidates with 0 evidence claims, taken from the
BOTTOM of the alphabet (TN, TX, SC, NE, NV) to avoid collision with the
top-of-alphabet loop.

Mix (4 R / 1 R-mixed): Tre Hargett (TN-R, Secretary of State),
           Glenn Hegar (TX-R, Comptroller),
           Pamela Evette (SC-R, Lt Gov / 2026 Gov candidate),
           Jim Pillen (NE-R, Governor),
           Joe Lombardo (NV-R, Governor — mixed record, negative scores on gun/life).
Each claim cites >=1 reliable source and reflects documented 2019-2026 positions.

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
    # ---------------- Tre Hargett (TN-R, Tennessee Secretary of State) ----------------
    ("tre-hargett", "TN", "Secretary of State", [
        claim("th1", "tre-hargett", "election_integrity", 0, True,
              "Under Hargett, Tennessee has ranked #1 in election integrity by the Heritage Foundation for four consecutive years. The state requires a valid government-issued photo ID to vote — college student IDs and private-organization IDs are explicitly rejected — and uses a polling-place-first model that resists mass mail-in voting.",
              ["https://sos.tn.gov/press-releases/tennessee-secretary-of-state-and-general-assemblys-efforts-to-make-it-easy-to-vote",
               "https://ballotpedia.org/Tre_Hargett"]),
        claim("th2", "tre-hargett", "border_immigration", 0, True,
              "In 2025, Hargett's office used the enhanced federal SAVE (Systematic Alien Verification for Entitlements) program to identify 42 individuals suspected of being non-U.S. citizens who voted in Tennessee elections and referred their names to the FBI for investigation — an active use of executive authority to enforce the citizen-only voting principle against illegal alien voting.",
              ["https://sos.tn.gov/press-releases/tennessee-secretary-of-state-tre-hargett-protecting-the-vote-in-tennessee-uses",
               "https://ballotpedia.org/Tre_Hargett"]),
    ]),

    # ---------------- Glenn Hegar (TX-R, Texas Comptroller) ----------------
    ("glenn-hegar-2026", "TX", "Comptroller", [
        claim("gh1", "glenn-hegar-2026", "economic_stewardship", 4, True,
              "As Texas Comptroller, Hegar administered the 2021 state law requiring Texas pension and school funds to divest from financial companies that boycott the fossil-fuel industry. In 2022 he sent letters to more than 100 of the world's largest financial firms demanding they disclose whether they restrict business with energy companies, then blacklisted BlackRock and nine other firms — calling ESG 'an opaque and perverse system' that uses financial clout to 'push a social and political agenda.'",
              ["https://en.wikipedia.org/wiki/Glenn_Hegar",
               "https://ballotpedia.org/Glenn_Hegar"]),
        claim("gh2", "glenn-hegar-2026", "sanctity_of_life", 0, True,
              "Texas Right to Life awarded Hegar its 'Perfectly Pro-Life Award,' reflecting a consistent record opposing abortion throughout his service in the Texas state legislature and as Comptroller.",
              ["https://glennhegar.com/issues/pro-life/",
               "https://ballotpedia.org/Glenn_Hegar"]),
        claim("gh3", "glenn-hegar-2026", "economic_stewardship", 1, True,
              "Hegar has repeatedly called for sound-money discipline in state finances, opposing unfunded spending commitments, and his Comptroller office maintained the state's biennial revenue forecasts as a firewall against deficit budgeting — a posture consistent with the rubric's preference for fiscal restraint over inflationary government borrowing.",
              ["https://en.wikipedia.org/wiki/Glenn_Hegar",
               "https://ballotpedia.org/Glenn_Hegar"]),
    ]),

    # ---------------- Pamela Evette (SC-R, Lieutenant Governor / 2026 Gov candidate) ----------------
    ("pamela-evette-ltgov-2026", "SC", "Lieutenant Governor", [
        claim("pe1", "pamela-evette-ltgov-2026", "self_defense", 0, True,
              "Evette supported the signing of South Carolina's Constitutional Carry law, which allows law-abiding South Carolinians to carry a firearm without a government-issued permit. She has pledged as a gubernatorial candidate to defend Second Amendment rights from any further restriction.",
              ["https://pamelaevette.com/issues/",
               "https://ballotpedia.org/Pamela_Evette"]),
        claim("pe2", "pamela-evette-ltgov-2026", "sanctity_of_life", 0, True,
              "Evette stood with Governor McMaster to defend South Carolina's Fetal Heartbeat law, one of the most protective pro-life statutes in the country, banning most abortions after cardiac activity is detected. Running for governor in 2026, she has pledged to ban taxpayer-funded abortions and never back down to the pro-abortion lobby.",
              ["https://pamelaevette.com/issues/protect-life-and-family-values/",
               "https://ballotpedia.org/Pamela_Evette"]),
        claim("pe3", "pamela-evette-ltgov-2026", "border_immigration", 2, True,
              "Evette has pledged that 'South Carolina will never become a sanctuary state' under her administration, calling for active partnership with the Trump administration to enforce immigration laws, deport illegal immigrants, and protect South Carolina communities from cartel-driven crime.",
              ["https://pamelaevette.com/issues/",
               "https://en.wikipedia.org/wiki/Pamela_Evette"]),
    ]),

    # ---------------- Jim Pillen (NE-R, Governor) ----------------
    ("jim-pillen-gov-2026", "NE", "Governor", [
        claim("jp1", "jim-pillen-gov-2026", "sanctity_of_life", 0, True,
              "On May 22, 2023, Governor Pillen signed LB 574, banning most abortions in Nebraska after 12 weeks of pregnancy. In November 2024, Nebraska voters approved Initiative 434, a constitutional amendment enshrining the 12-week limit — defeating a competing initiative (Initiative 439) that would have restored abortion until fetal viability. Pillen campaigned explicitly on opposing abortion.",
              ["https://en.wikipedia.org/wiki/Jim_Pillen",
               "https://ballotpedia.org/Jim_Pillen"]),
        claim("jp2", "jim-pillen-gov-2026", "self_defense", 0, True,
              "Under Pillen's administration, Nebraska's permitless constitutional carry law took effect on September 2, 2023, eliminating the state requirement for a concealed-carry permit and recognizing the right of law-abiding citizens to bear arms without government permission.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Nebraska",
               "https://en.wikipedia.org/wiki/Jim_Pillen"]),
        claim("jp3", "jim-pillen-gov-2026", "border_immigration", 1, True,
              "In August 2025, Governor Pillen joined U.S. Secretary of Homeland Security Kristi Noem to announce 'Cornhusker Clink,' a new immigration detention facility in McCook, Nebraska — a direct state-level partnership with federal deportation efforts reflecting a mandatory-enforcement posture on illegal immigration.",
              ["https://en.wikipedia.org/wiki/Jim_Pillen",
               "https://ballotpedia.org/Jim_Pillen"]),
    ]),

    # ---------------- Joe Lombardo (NV-R, Governor — mixed/negative record) ----------------
    ("joe-lombardo", "NV", "Governor", [
        claim("jl1", "joe-lombardo", "self_defense", 1, False,
              "As Clark County Sheriff, Lombardo publicly supported a high-capacity magazine ban and backed universal background checks on gun purchases — two policies the rubric explicitly opposes. As governor he has not moved to repeal or nullify Nevada's gun-control statutes.",
              ["https://en.wikipedia.org/wiki/Joe_Lombardo",
               "https://ballotpedia.org/Joe_Lombardo"]),
        claim("jl2", "joe-lombardo", "sanctity_of_life", 0, False,
              "Lombardo signed legislation protecting access to abortion services in Nevada — one of only three Republican governors to do so as of May 2023 — and has not moved to restrict Nevada's existing law allowing abortion on demand through 24 weeks, placing him outside the rubric's life-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Joe_Lombardo",
               "https://ballotpedia.org/Joe_Lombardo"]),
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
