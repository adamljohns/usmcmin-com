#!/usr/bin/env python3
"""Enrichment batch 283: hand-curated claims for 4 federal House candidates.

Targets evidence_federal candidates with 0 claims, drawn from the BOTTOM of
the alphabet (TX, NY, MN, MO) to avoid collision with the top-of-alphabet
enrichment agent.

Mix (0 R / 4 D): Carlos Quintanilla (TX-33-D, cross-party pro-life),
Nina Schwalbe (NY-12-D), Kelly Morrison (MN-03-D, sitting Rep.),
Matthew Levine (MO-06-D).

Each claim cites >=1 reliable source and reflects 2024-2026 public
positions, iVoterGuide survey responses, and official House.gov press
releases.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---- Carlos Quintanilla (TX-33, D) — cross-party pro-life Democrat ----
    ("carlos-quintanilla", "TX", "Representative", [
        claim("cq1", "carlos-quintanilla", "sanctity_of_life", 0, True,
              "Via iVoterGuide candidate survey, stated: 'Human life begins at conception and deserves legal protection at every stage until natural death' — an unambiguous affirmation of personhood from conception, a rare pro-life position for a Democratic candidate.",
              ["https://ivoterguide.com/candidate/23489/race/6591/election/791",
               "https://ballotpedia.org/Carlos_Quintanilla_(Texas)"]),
        claim("cq2", "carlos-quintanilla", "sanctity_of_life", 4, True,
              "Via iVoterGuide survey: 'Abortion providers, including Planned Parenthood, should not receive taxpayer funds or grants from federal, state, or local governments' — explicitly opposing any taxpayer subsidy of the abortion industry.",
              ["https://ivoterguide.com/candidate/23489/race/6591/election/791",
               "https://ballotpedia.org/Carlos_Quintanilla_(Texas)"]),
        claim("cq3", "carlos-quintanilla", "biblical_marriage", 0, True,
              "Via iVoterGuide survey: 'Governments should not discriminate against individuals, organizations or small businesses because of their belief that marriage is only a union of one man and one woman' — affirming the one-man-one-woman definition and defending religious-liberty protections for those who hold it.",
              ["https://ivoterguide.com/candidate/23489/race/6591/election/791"]),
    ]),

    # ---- Nina Schwalbe (NY-12, D) — progressive public-health Democrat ----
    ("nina-schwalbe", "NY", "Representative", [
        claim("ns1", "nina-schwalbe", "sanctity_of_life", 0, False,
              "Campaigns on passing a federal law to override state abortion bans and guarantee nationwide access to abortion care — rejecting any recognition of unborn personhood from conception.",
              ["https://www.ninafornyc.com/policy",
               "https://patch.com/new-york/upper-west-side-nyc/election-q-meet-ny-12-candidate-nina-schwalbe"]),
        claim("ns2", "nina-schwalbe", "biblical_marriage", 2, False,
              "Backs federal protection of gender-affirming care for transgender individuals, citing the American Psychological Association's endorsement of such interventions as 'evidence-based and medically necessary' — affirming transgender ideology in law and policy.",
              ["https://www.ninafornyc.com/policy"]),
        claim("ns3", "nina-schwalbe", "biblical_marriage", 4, False,
              "Champions the BE HEARD in the Workplace Act to extend LGBTQ discrimination protections in schools and public accommodations — codifying LGBTQ ideology into federal education and public-accommodation law.",
              ["https://www.ninafornyc.com/policy"]),
    ]),

    # ---- Kelly Morrison (MN-03, D) — sitting U.S. Representative ----
    ("kelly-morrison", "MN", "House", [
        claim("km1", "kelly-morrison", "sanctity_of_life", 0, False,
              "A pro-choice OB-GYN who ran on reproductive rights, led Minnesota's legislative effort to pass a comprehensive package protecting abortion access, was endorsed by a former CEO of Planned Parenthood North Central States, and publicly opposed Republican legislation she called a 'backdoor abortion ban' — rejecting any life-from-conception protection.",
              ["https://en.wikipedia.org/wiki/Kelly_Morrison",
               "https://morrison.house.gov/about"]),
        claim("km2", "kelly-morrison", "self_defense", 1, False,
              "Called on the House floor to ban assault weapons, bump stocks, and high-capacity magazine sales; convened a gun violence prevention town hall; and serves on the House Gun Violence Prevention Task Force — directly opposing Second Amendment protections against bans and magazine restrictions.",
              ["https://morrison.house.gov/media/press-releases/us-rep-kelly-morrison-reads-letters-minnesotans-calling-gun-control-house"]),
        claim("km3", "kelly-morrison", "border_immigration", 1, False,
              "Publicly demanded a block on additional ICE and Customs and Border Patrol funding, stating: 'We cannot give one more penny to ICE as long as this lawless agency is violating Americans' Constitutional rights, blatantly racially profiling, brutalizing people, terrorizing our communities, traumatizing our children, and killing people' — opposing border-enforcement funding and mandatory deportation.",
              ["https://morrison.house.gov/media/press-releases/us-rep-kelly-morrison-stands-minnesotans-ahead-vote-dhs-funding"]),
    ]),

    # ---- Matthew Levine (MO-06, D) — Democratic primary candidate ----
    ("matthew-levine-mo-06", "MO", "Representative", [
        claim("ml1", "matthew-levine-mo-06", "sanctity_of_life", 0, False,
              "Campaign platform explicitly lists 'women's healthcare and reproductive care' as a priority and opposes any government cuts to those services — signaling support for abortion access consistent with mainstream Democratic positions in the 2026 cycle.",
              ["https://www.levine4congress.com/"]),
        claim("ml2", "matthew-levine-mo-06", "economic_stewardship", 2, False,
              "Campaigns on expanding public investment in jobs, education, and infrastructure, and opposes Republican cuts to Medicare and Medicaid — prioritizing expanded federal social spending over deficit reduction and balanced-budget principles.",
              ["https://www.levine4congress.com/"]),
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
