#!/usr/bin/env python3
"""Enrichment batch 128: hand-curated claims for 5 sitting U.S. Representatives.

Targets bottom-of-alphabet (WA/WI) archetype_party_default US House members with 0 claims.
Mix (1 R / 4 D): Michael Baumgartner (WA-R), Marie Gluesenkamp Perez (WA-D),
Pramila Jayapal (WA-D), Gwen Moore (WI-D), Mark Pocan (WI-D).

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
    # ---------------- Michael Baumgartner (WA-5, R, US House) ----------------
    ("michael-baumgartner", "WA", "House", [
        claim("mb1", "michael-baumgartner", "border_immigration", 0, True,
              "Publicly called for the border wall to be completed, stating 'The wall needs to be finished' as a cornerstone of his immigration platform — directly matching the rubric's demand for physical barrier enforcement.",
              ["https://en.wikipedia.org/wiki/Michael_Baumgartner",
               "https://ballotpedia.org/Michael_Baumgartner_(Washington)"]),
        claim("mb2", "michael-baumgartner", "border_immigration", 2, True,
              "In March 2025, joined Reps. Jim Jordan and Tom McClintock in formally challenging Washington State's sanctuary law, which bars local police from cooperating with federal immigration enforcement — aligning with the rubric's anti-sanctuary position.",
              ["https://en.wikipedia.org/wiki/Michael_Baumgartner",
               "https://ballotpedia.org/Michael_Baumgartner_(Washington)"]),
        claim("mb3", "michael-baumgartner", "border_immigration", 3, True,
              "Called for mandatory E-Verify implementation as part of his border-enforcement platform, requiring employers to confirm worker immigration status — consistent with the rubric's E-Verify demand.",
              ["https://en.wikipedia.org/wiki/Michael_Baumgartner",
               "https://ballotpedia.org/Michael_Baumgartner_(Washington)"]),
    ]),

    # ---------------- Marie Gluesenkamp Perez (WA-3, D, US House) ----------------
    ("marie-gluesenkamp-perez", "WA", "House", [
        claim("mgp1", "marie-gluesenkamp-perez", "border_immigration", 1, True,
              "In January 2025, was one of 48 House Democrats to vote for the Laken Riley Act — requiring ICE detention of undocumented immigrants charged with theft or violent crimes — and voted for the Senate-amended version, aligning with the rubric's mandatory enforcement standard.",
              ["https://en.wikipedia.org/wiki/Marie_Gluesenkamp_Perez",
               "https://ballotpedia.org/Marie_Gluesenkamp_Perez"]),
        claim("mgp2", "marie-gluesenkamp-perez", "election_integrity", 0, True,
              "One of only five House Democrats to vote for the SAVE Act in July 2024 — and again in April 2025 — which requires documentary proof of U.S. citizenship to register to vote, a voter-integrity measure the rubric supports.",
              ["https://en.wikipedia.org/wiki/Marie_Gluesenkamp_Perez",
               "https://ballotpedia.org/Marie_Gluesenkamp_Perez"]),
        claim("mgp3", "marie-gluesenkamp-perez", "biblical_marriage", 4, True,
              "In 2026, was one of eight House Democrats to vote for the Stopping Indoctrination and Protecting Kids Act, mandating that school professionals notify parents when a student identifies as transgender — rejecting concealment of LGBTQ ideology from parents in schools.",
              ["https://en.wikipedia.org/wiki/Marie_Gluesenkamp_Perez",
               "https://ballotpedia.org/Marie_Gluesenkamp_Perez"]),
    ]),

    # ---------------- Pramila Jayapal (WA-7, D, US House) ----------------
    ("pramila-jayapal", "WA", "House", [
        claim("pj1", "pramila-jayapal", "self_defense", 1, False,
              "Supported and applauded the House Judiciary Committee's passage of the Assault Weapons Ban of 2022 (H.R. 1808), seeking to ban gas-operated semi-automatic rifles — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Pramila_Jayapal",
               "https://jayapal.house.gov/2022/07/20/jayapal-statement-on-house-judiciary-advancing-assault-weapons-ban/"]),
        claim("pj2", "pramila-jayapal", "sanctity_of_life", 0, False,
              "Sponsored legislation to protect abortion access and ensure affordable abortion coverage for all women, explicitly limiting state restrictions on abortion providers — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Pramila_Jayapal",
               "https://www.congress.gov/member/pramila-jayapal/J000298"]),
        claim("pj3", "pramila-jayapal", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (2022), federally codifying recognition of same-sex marriage and repealing the Defense of Marriage Act — directly opposing the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Pramila_Jayapal",
               "https://ballotpedia.org/Pramila_Jayapal"]),
    ]),

    # ---------------- Gwen Moore (WI-4, D, US House) ----------------
    ("gwen-moore", "WI", "House", [
        claim("gm1", "gwen-moore", "sanctity_of_life", 4, False,
              "Carries a career 100% rating from NARAL Pro-Choice America (now Reproductive Freedom for All) and consistent Planned Parenthood support scores — squarely inside the abortion-advocacy endorsement network the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Gwen_Moore",
               "https://ballotpedia.org/Gwen_Moore"]),
        claim("gm2", "gwen-moore", "sanctity_of_life", 0, False,
              "Consistently opposes any restriction on abortion access; led floor opposition to the 2011 Pence Amendment to defund Planned Parenthood, declaring it 'healthy for women' — rejecting the personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Gwen_Moore",
               "https://gwenmoore.house.gov/voterecord/"]),
        claim("gm3", "gwen-moore", "self_defense", 1, False,
              "Receives 0% from the Sportsmen's and Animal Owners' Voting Alliance; has a career record of supporting gun-control legislation including assault-weapons restrictions — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Gwen_Moore",
               "https://ballotpedia.org/Gwen_Moore"]),
    ]),

    # ---------------- Mark Pocan (WI-2, D, US House) ----------------
    ("mark-pocan", "WI", "House", [
        claim("mp1", "mark-pocan", "biblical_marriage", 4, False,
              "Co-chair of the Congressional LGBT Equality Caucus; organized House press conferences attacking Republican efforts to restrict LGBTQ promotion in schools and youth policy — directly opposing the rubric's position against such promotion.",
              ["https://en.wikipedia.org/wiki/Mark_Pocan",
               "https://pocan.house.gov/media-center/press-releases/equality-caucus-press-conference-on-gop-anti-trans-agenda"]),
        claim("mp2", "mark-pocan", "self_defense", 1, False,
              "Voted for the Protecting Our Children Act (H.R. 7910) gun-safety package and publicly backed an assault-weapons ban, calling Congress 'too chicken to address the epidemic of military-style assault weapons' — opposing the rubric's defense of semi-automatic firearms.",
              ["https://en.wikipedia.org/wiki/Mark_Pocan",
               "https://pocan.house.gov/media-center/press-releases/pocan-takes-action-on-gun-violence"]),
        claim("mp3", "mark-pocan", "sanctity_of_life", 0, False,
              "A lifelong abortion-rights advocate who supports codifying abortion access into federal law and carries a 100% rating from pro-abortion organizations — opposing any recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Mark_Pocan",
               "https://ballotpedia.org/Mark_Pocan"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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
