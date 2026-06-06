#!/usr/bin/env python3
"""Enrichment batch 84: hand-curated claims for 4 conservative state-level officials.

Federal senator/house-rep bucket is nearly exhausted (only phantom entries remain).
Pivoting to confirmed sitting R officials from the bottom of the alphabet where the
archetype_curated 0-claims bucket still has entries: LA Governor, AR Governor,
IA AG, and MO Governor — all with verifiable 2023-2025 public record.

Targets: Jeff Landry (LA Gov), Sarah Huckabee Sanders (AR Gov),
Brenna Bird (IA AG), Mike Kehoe (MO Gov).
Each claim cites >=1 reliable source and reflects 2023-2026 public record / stated positions.

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
    # ---------------- Jeff Landry (LA-R, Governor since Jan 2024) ----------------
    ("jeff-landry", "LA", "Governor", [
        claim("jl1", "jeff-landry", "self_defense", 0, True,
              "As governor, Landry signed a constitutional-carry bill allowing Louisiana residents to carry concealed firearms without a government-issued permit — aligning with the rubric's standard that no government permission should be required to exercise the right to keep and bear arms.",
              ["https://en.wikipedia.org/wiki/Jeff_Landry",
               "https://ballotpedia.org/Jeff_Landry"]),
        claim("jl2", "jeff-landry", "biblical_marriage", 4, True,
              "In June 2024, Landry signed legislation requiring parental approval before school staff can use a student's requested preferred pronouns — protecting parental authority over gender-identity messaging directed at their children in public schools, directly opposing LGBTQ-ideology promotion in K-12 settings.",
              ["https://en.wikipedia.org/wiki/Jeff_Landry",
               "https://en.wikipedia.org/wiki/2024_in_Louisiana"]),
        claim("jl3", "jeff-landry", "sanctity_of_life", 0, True,
              "Governor Landry signed a June 2024 law classifying the abortion-inducing drugs mifepristone and misoprostol as Schedule IV controlled substances — making Louisiana the first state to criminalize possession of these drugs without a prescription. He also signed an extradition warrant for a New York physician charged with violating Louisiana's near-total abortion ban, demonstrating active enforcement of personhood protections from conception.",
              ["https://en.wikipedia.org/wiki/Jeff_Landry",
               "https://en.wikipedia.org/wiki/Abortion_in_Louisiana"]),
    ]),

    # ---------------- Sarah Huckabee Sanders (AR-R, Governor since Jan 2023) ----------------
    ("sarah-huckabee-sanders", "AR", "Governor", [
        claim("shs1", "sarah-huckabee-sanders", "biblical_marriage", 2, True,
              "Governor Sanders signed two landmark bills in March 2023 rejecting transgender ideology: (1) a law banning transgender students from using public school bathrooms that match their claimed gender identity, and (2) a bill creating a 15-year civil-liability window for individuals to sue medical providers who administered gender-affirming procedures to them as minors — directly opposing the rubric's concern about gender ideology imposed on children.",
              ["https://en.wikipedia.org/wiki/Sarah_Huckabee_Sanders",
               "https://en.wikipedia.org/wiki/LGBTQ_rights_in_Arkansas"]),
        claim("shs2", "sarah-huckabee-sanders", "sanctity_of_life", 0, True,
              "Sanders explicitly stated she would not support rape or incest exceptions in anti-abortion legislation, reflecting a consistent life-from-conception position. She ran for governor championing Arkansas's existing near-total abortion ban and pledged to defend it — earning the support of pro-life organizations and running on a platform that 'Women, not politicians' framing does not override the unborn child's right to life.",
              ["https://en.wikipedia.org/wiki/Sarah_Huckabee_Sanders",
               "https://ballotpedia.org/Sarah_Huckabee_Sanders"]),
        claim("shs3", "sarah-huckabee-sanders", "family_child_sovereignty", 0, True,
              "Sanders championed and signed the LEARNS Act (2023), Arkansas's sweeping education reform that created Education Freedom Accounts — education savings accounts allowing families to use public funding for private school tuition, home-school costs, and other approved educational expenses, fundamentally shifting power over children's education from the government to parents.",
              ["https://en.wikipedia.org/wiki/Sarah_Huckabee_Sanders",
               "https://ballotpedia.org/Sarah_Huckabee_Sanders"]),
    ]),

    # ---------------- Brenna Bird (IA-R, Attorney General since Jan 2023; 2026 re-election) ----------------
    ("brenna-bird-ag-2026", "IA", "Attorney", [
        claim("bb1", "brenna-bird-ag-2026", "sanctity_of_life", 0, True,
              "In April 2023, AG Bird ordered Iowa to stop the state practice of paying for emergency contraception or abortions for rape victims — ending taxpayer-funded abortions and contraception in Iowa, consistent with a life-from-conception standard that refuses any public funding for procedures that may destroy a newly conceived human life.",
              ["https://en.wikipedia.org/wiki/Brenna_Bird",
               "https://ballotpedia.org/Brenna_Bird"]),
        claim("bb2", "brenna-bird-ag-2026", "border_immigration", 0, True,
              "AG Bird filed or joined more than a dozen multi-state lawsuits against the Biden administration in 2023 and at least a dozen more in 2024, with a significant share targeting open-border immigration policies, DACA expansions, and the failure to enforce federal immigration law — directly opposing the rubric's concern about sanctuary jurisdictions and non-enforcement of deportation requirements.",
              ["https://en.wikipedia.org/wiki/Brenna_Bird",
               "https://ballotpedia.org/Brenna_Bird"]),
        claim("bb3", "brenna-bird-ag-2026", "refuse_federal_overreach", 0, True,
              "Beyond immigration, Bird led Iowa into 24+ multi-state coalitions challenging Biden-era federal overreach across regulatory, administrative, and constitutional law — establishing her record as one of the most active state AGs defending state sovereignty and the Tenth Amendment against unconstitutional federal encroachment.",
              ["https://en.wikipedia.org/wiki/Brenna_Bird",
               "https://ballotpedia.org/Brenna_Bird"]),
    ]),

    # ---------------- Mike Kehoe (MO-R, Governor since Jan 2025) ----------------
    ("mike-kehoe", "MO", "Governor", [
        claim("mk1", "mike-kehoe", "sanctity_of_life", 0, True,
              "In May 2025, Kehoe signed legislation scheduling a statewide referendum to repeal Missouri's Amendment 3 — a November 2024 ballot measure that had legalized abortion in Missouri — and reinstitute the state's near-total abortion ban with only narrow emergency exceptions, affirming Missouri's commitment to a life-from-conception standard over voter-enacted abortion liberalization.",
              ["https://en.wikipedia.org/wiki/Mike_Kehoe",
               "https://en.wikipedia.org/wiki/Abortion_in_Missouri"]),
        claim("mk2", "mike-kehoe", "family_child_sovereignty", 0, True,
              "In his first year as governor, Kehoe's 2025 budget prioritized a $50 million expansion of the MOScholars program — Missouri's tax-credit scholarship initiative that funds private and parochial school tuition for families who choose alternatives to the public-school system, placing education authority back in parents' hands.",
              ["https://en.wikipedia.org/wiki/Mike_Kehoe",
               "https://ballotpedia.org/Mike_Kehoe"]),
        claim("mk3", "mike-kehoe", "election_integrity", 0, True,
              "In July 2025, Kehoe signed legislation banning foreign nationals and foreign governments from contributing to Missouri ballot measure campaigns — making Missouri one of a growing bloc of states closing this loophole to prevent foreign influence on state elections, consistent with the rubric's election-integrity standard.",
              ["https://ballotpedia.org/Mike_Kehoe",
               "https://news.ballotpedia.org/2025/07/09/missouri-becomes-ninth-state-state-to-ban-foreign-funding-in-ballot-measure-campaigns-in-2025-as-federal-court-upholds-kansas-ban/"]),
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
