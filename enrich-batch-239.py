#!/usr/bin/env python3
"""Enrichment batch 239: hand-curated claims for 5 federal House members.

Targets archetype_party_default U.S. Representatives with 0 claims, taken
from the BOTTOM of the alphabet (NM×2, NJ×3) to avoid collision with the
top-of-alphabet enrichment loop.

Mix (0 R / 5 D): Gabriel Vasquez (NM-D), Melanie Stansbury (NM-D),
Rob Menendez (NJ-D), LaMonica McIver (NJ-D), Josh Gottheimer (NJ-D).
Each claim cites >=1 reliable source and reflects 2021-2026 voting record /
public positions.

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
    # ---------------- Gabriel Vasquez (NM-02, D) ----------------
    ("gabriel-vasquez", "NM", "US House", [
        claim("gv1", "gabriel-vasquez", "sanctity_of_life", 0, False,
              "A cosponsor of the Women's Health Protection Act, which would codify a federal statutory right to abortion and preempt state pro-life laws, explicitly rejecting any legal recognition of personhood or life from conception.",
              ["https://vasquez.house.gov/issues/rights",
               "https://en.wikipedia.org/wiki/Gabe_Vasquez"]),
        claim("gv2", "gabriel-vasquez", "self_defense", 1, False,
              "Supports the Bipartisan Background Checks Act, a federal assault weapons ban, and Ethan's Law mandating safe storage of firearms — a package of restrictions the rubric opposes as infringing on Second Amendment rights without disarming criminals.",
              ["https://vasquez.house.gov/issues/rights",
               "https://ballotpedia.org/Gabriel_Vasquez"]),
    ]),

    # ---------------- Melanie Stansbury (NM-01, D) ----------------
    ("melanie-stansbury", "NM", "US House", [
        claim("ms1", "melanie-stansbury", "sanctity_of_life", 0, False,
              "Endorsed by pro-abortion groups including Voteprochoice and runs in the Congressional Progressive Caucus, consistently supporting abortion access and opposing any legislation that would recognize fetal personhood from the moment of conception.",
              ["https://ballotpedia.org/Melanie_Ann_Stansbury",
               "https://en.wikipedia.org/wiki/Melanie_Stansbury"]),
        claim("ms2", "melanie-stansbury", "self_defense", 1, False,
              "Pledged support for a federal assault weapons ban in her 2021 candidate questionnaire and, as a member of the Congressional Progressive Caucus, backs comprehensive gun-control legislation — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Melanie_Ann_Stansbury",
               "https://www.govtrack.us/congress/members/melanie_stansbury/456861"]),
    ]),

    # ---------------- Rob Menendez (NJ-08, D) ----------------
    ("rob-menendez", "NJ", "US House", [
        claim("rm1", "rob-menendez", "sanctity_of_life", 0, False,
              "Consistently pro-choice with a 0% rating from SBA Pro-Life America; opposes any legal recognition of personhood from conception and has made protection of abortion access a defining plank of his legislative agenda.",
              ["https://sbaprolife.org/representative/robert-menendez-jr",
               "https://en.wikipedia.org/wiki/Rob_Menendez"]),
        claim("rm2", "rob-menendez", "sanctity_of_life", 4, False,
              "Carries a 100% score from Reproductive Freedom for All (successor to NARAL Pro-Choice America), placing him squarely within the abortion-industry endorsement network the rubric considers disqualifying.",
              ["https://reproductivefreedomforall.org/lawmaker/rob-menendez/",
               "https://ballotpedia.org/Rob_Menendez_(New_Jersey)"]),
    ]),

    # ---------------- LaMonica McIver (NJ-10, D) ----------------
    ("lamonica-mciver", "NJ", "US House", [
        claim("lm1", "lamonica-mciver", "sanctity_of_life", 0, False,
              "Firmly opposes the Supreme Court's Dobbs decision and is 'committed to safeguarding the rights of patients and providers as they make decisions about abortion, IVF, and contraception' — rejecting any framework that recognizes life or personhood from conception.",
              ["https://mciver.house.gov/issue/reproductive-justice",
               "https://ballotpedia.org/LaMonica_McIver"]),
        claim("lm2", "lamonica-mciver", "border_immigration", 1, False,
              "Publicly called for abolishing ICE in a February 4, 2026 CNN interview, placing her in direct opposition to the rubric's demand for mandatory deportation and robust interior enforcement.",
              ["https://ballotpedia.org/LaMonica_McIver",
               "https://www.govtrack.us/congress/members/lamonica_mciver/456962"]),
    ]),

    # ---------------- Josh Gottheimer (NJ-05, D) ----------------
    ("josh-gottheimer", "NJ", "US House", [
        claim("jg1", "josh-gottheimer", "self_defense", 1, False,
              "Helped pass the Bipartisan Safer Communities Act (2022) — the first major federal gun legislation in decades — which expands background checks for buyers under 21, closes the 'boyfriend loophole,' and funds state red-flag law programs; also led 100+ House Democrats urging Speaker Johnson to bring additional gun-control legislation to the floor.",
              ["https://gottheimer.house.gov/posts/release-gottheimer-helps-pass-bipartisan-gun-safety-bill-applauds-bipartisan-efforts-now-signed-into-law",
               "https://gottheimer.house.gov/posts/release-gottheimer-100-house-democrats-call-on-speaker-johnson-to-work-together-address-gun-violence"]),
        claim("jg2", "josh-gottheimer", "sanctity_of_life", 0, False,
              "Introduced the Protecting Personal, Private Medical Decisions Act (2024) to shield federal access to mifepristone (the chemical abortion pill), cosponsored the Women's Health Protection Act to codify a federal right to abortion, and condemned the Dobbs ruling — consistently rejecting any recognition of personhood from conception.",
              ["https://gottheimer.house.gov/posts/release-gottheimer-announces-new-legislation-to-protect-access-to-mifepristone-stop-far-right-extremist-war-on-womens-healthcare",
               "https://en.wikipedia.org/wiki/Josh_Gottheimer"]),
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
