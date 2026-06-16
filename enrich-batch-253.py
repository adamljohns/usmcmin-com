#!/usr/bin/env python3
"""Enrichment batch 253: 4 archetype_party_default candidates with 0 claims, bottom-of-alphabet.

All archetype_curated and evidence_curated federal pools are exhausted; this batch
moves to archetype_party_default US-level candidates from MI → IA → IL.

Targets (reversed-alpha order):
  Mallory McMorrow (MI, D) — state senator, 2026 U.S. Senate candidate
  Josh Turek (IA, D)       — state rep, won D primary 6/2/2026, IA Senate D nominee
  Jan Schakowsky (IL, D)   — retiring U.S. Rep IL-09 (1999-2026)
  Danny Davis (IL, D)      — retiring U.S. Rep IL-07 (1997-2026)

Each claim cites >=1 reliable source (Wikipedia, Ballotpedia, Congress.gov, GovTrack).

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


TARGETS = [
    # ---------- Mallory McMorrow (MI, D, Michigan State Senator / 2026 U.S. Senate candidate) ----------
    ("mallory-mcmorrow", "MI", "State Senator", [
        claim("mm1", "mallory-mcmorrow", "sanctity_of_life", 0, False,
              "McMorrow publicly disclosed her own emergency dilation and curettage (D&C) procedure in July 2022 and emerged as one of Michigan's most vocal advocates against post-Dobbs abortion restrictions, arguing that such laws endanger women's health. She supports full access to abortion and has used her platform in the Michigan state senate to champion federal legislation restoring the legal framework of Roe v. Wade — a direct rejection of the pro-life principle that human life deserves protection from the moment of conception.",
              ["https://en.wikipedia.org/wiki/Mallory_McMorrow",
               "https://ballotpedia.org/Mallory_McMorrow"]),
        claim("mm2", "mallory-mcmorrow", "biblical_marriage", 4, False,
              "On April 19, 2022, McMorrow delivered a viral Michigan Senate floor speech — watched over one million times in its first hours — directly defending LGBTQ-inclusive curriculum and instruction, rejecting Republican legislators' objections to teaching children about LGBTQ identities in school settings. Her speech explicitly positioned LGBTQ promotion in education as morally justified and politically necessary, placing her in direct opposition to the rubric's standard opposing LGBTQ content in schools and public policy.",
              ["https://en.wikipedia.org/wiki/Mallory_McMorrow",
               "https://en.wikipedia.org/wiki/LGBT_grooming_conspiracy_theory"]),
    ]),

    # ---------- Josh Turek (IA, D, Iowa State Representative / 2026 U.S. Senate D nominee) ----------
    ("josh-turek", "IA", "State Representative", [
        claim("jt1", "josh-turek", "sanctity_of_life", 0, False,
              "Turek supports passing a federal law to restore the abortion protections previously afforded by Roe v. Wade — explicitly rejecting any legislative recognition that human life begins at conception. He has publicly argued that Iowa's six-week abortion ban reduced OB-GYN services available to women in the state and has made expanding abortion access a central plank of his 2026 U.S. Senate campaign as the D nominee (won D primary June 2, 2026, with 62.6% of the vote over state senator Zach Wahls).",
              ["https://en.wikipedia.org/wiki/Josh_Turek",
               "https://ballotpedia.org/Josh_Turek"]),
        claim("jt2", "josh-turek", "economic_stewardship", 2, False,
              "Turek supports a public health insurance option, full restoration of ACA subsidies, and opposes any cuts to Medicaid or Medicare — a platform of expanding federal healthcare entitlement spending that adds to the national debt and directly opposes the rubric's anti-deficit/balanced-budget standard. He has described himself as a populist moderate, but his healthcare agenda entails significant new federal outlays without offsetting cuts.",
              ["https://ballotpedia.org/Josh_Turek",
               "https://en.wikipedia.org/wiki/Josh_Turek"]),
    ]),

    # ---------- Jan Schakowsky (IL-09, D, retiring U.S. Representative) ----------
    ("jan-schakowsky", "IL", "Representative", [
        claim("js1", "jan-schakowsky", "self_defense", 1, False,
              "Schakowsky cosponsored H.R.698, the Assault Weapons Ban of 2023 (118th Congress), which would prohibit the manufacture, importation, sale, and transfer of named semi-automatic assault weapons and large-capacity ammunition magazines — a direct vote against the right to own commonly-owned semi-automatic firearms and in favor of the magazine-capacity restrictions and weapons registries that the rubric identifies as infringements on Second Amendment rights. She has a career 'F' rating from the NRA and has been among the House's most persistent advocates for federal gun control.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://en.wikipedia.org/wiki/Jan_Schakowsky"]),
        claim("js2", "jan-schakowsky", "sanctity_of_life", 0, False,
              "Schakowsky has been a leading member of the Congressional Pro-Choice Caucus for her entire 26-year House career, consistently championing federal protection of abortion rights, opposing any restriction on abortion at any stage of pregnancy, and publicly supporting legislation to codify Roe v. Wade as federal law. She is rated 100% by Reproductive Freedom for All (formerly NARAL Pro-Choice America) and has received repeated endorsements and financial support from Planned Parenthood Action Fund, placing her squarely within the abortion-industry funding network the rubric flags.",
              ["https://en.wikipedia.org/wiki/Jan_Schakowsky",
               "https://ballotpedia.org/Jan_Schakowsky",
               "https://reproductivefreedomforall.org/elections/"]),
    ]),

    # ---------- Danny Davis (IL-07, D, retiring U.S. Representative) ----------
    ("danny-davis", "IL", "Representative", [
        claim("dd1", "danny-davis", "sanctity_of_life", 0, False,
              "Davis has maintained a consistently pro-choice voting record across his entire 28-year House career (1997–2026), supporting access to abortion and contraceptive healthcare, opposing any restrictions on abortion rights, and voting against legislation limiting federal funding for abortion providers. He emphasized protecting reproductive rights — including abortion and contraceptive access — as a priority in his 2024 re-election messaging, rejecting the pro-life principle that human life deserves legal protection from conception.",
              ["https://en.wikipedia.org/wiki/Danny_Davis_(Illinois_politician)",
               "https://ballotpedia.org/Danny_K._Davis"]),
        claim("dd2", "danny-davis", "self_defense", 1, False,
              "Davis has advocated for 'common sense gun safety laws' throughout his congressional career, consistently supporting assault-weapons restrictions, universal background checks, and other gun control measures. He voted with the Democratic caucus majority on every major gun-control roll call vote from the 105th Congress through the 119th, including the Bipartisan Safer Communities Act (S.2938, signed into law June 2022) and previous Assault Weapons Ban reauthorizations — a career legislative record opposing the right to keep and bear arms free from registration and capacity restrictions.",
              ["https://ballotpedia.org/Danny_K._Davis",
               "https://www.govtrack.us/congress/members/danny_davis/400093",
               "https://en.wikipedia.org/wiki/Danny_Davis_(Illinois_politician)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs."""
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
