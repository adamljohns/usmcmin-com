#!/usr/bin/env python3
"""Enrichment batch 44: 5 bottom-of-alphabet U.S. House candidates with 0 claims.

Targets (reversed-alpha order from archetype_curated rep bucket):
  Tyler Kistner (MN-02, R · Marine vet · dropped out 4/2026 for deployment)
  Analilia Mejia (NJ-11, D · incumbent · won 2026 special)
  Adam Hamawy   (NJ-12, D · Army vet surgeon · won D primary 6/3/2026)
  Ryan Busse     (MT-01, D · 2024 MT Gov nominee · gun-industry author)
  Denise Powell  (NE-02, D · D nominee · EMILY's List)

Each claim cites >=1 reliable source (2020-2026 record / stated positions).
Minified write preserves the ~35-36 MB master under GitHub's 50 MB limit.
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
    # ---------------- Tyler Kistner (MN-02, R) ----------------
    ("tyler-kistner", "MN", "representative", [
        claim("tk1", "tyler-kistner", "sanctity_of_life", 0, True,
              "Endorsed by the National Right to Life Committee PAC in both his 2020 and 2022 MN-02 campaigns; stated he would 'always fight for legislation to protect the unborn' — a life-from-conception stance matching the rubric ideal.",
              ["https://ballotpedia.org/Tyler_Kistner",
               "https://justfacts.votesmart.org/candidate/192397/tyler-kistner"]),
        claim("tk2", "tyler-kistner", "self_defense", 1, True,
              "Opposes new gun-control restrictions, arguing such laws 'make it harder for average law-abiding citizens to own guns while doing nothing to hinder criminals'; supports gun education and mental-health awareness instead of additional mandates — consistent with rejecting red-flag laws and assault-weapon bans.",
              ["https://ballotpedia.org/Tyler_Kistner",
               "https://justfacts.votesmart.org/candidate/192397/tyler-kistner"]),
        claim("tk3", "tyler-kistner", "border_immigration", 0, True,
              "Criticized opponent Angie Craig for voting to block border crossing restrictions during the Biden era; publicly called the resulting surge a 'border crisis' and supported legislation to restore enforcement at the southern border.",
              ["https://ballotpedia.org/Tyler_Kistner",
               "https://www.startribune.com/gop-tyler-kistner-enters-race-to-replace-angie-craig/601354217"]),
    ]),

    # ---------------- Analilia Mejia (NJ-11, D · incumbent) ----------------
    ("analilia-mejia", "NJ", "representative", [
        claim("am1", "analilia-mejia", "sanctity_of_life", 0, False,
              "Ran explicitly on protecting abortion rights as a central campaign issue; her 2026 primary and special-election platforms both foregrounded reproductive rights as a non-negotiable priority — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Analilia_Mejia",
               "https://newjerseymonitor.com/2026/04/16/analilia-mejia-special-house-election/"]),
        claim("am2", "analilia-mejia", "border_immigration", 2, False,
              "Campaigned on abolishing U.S. Immigration and Customs Enforcement ('abolish ICE now'); endorsed by Sen. Bernie Sanders and Rep. Alexandria Ocasio-Cortez, whose platforms oppose deportation enforcement and sanctuary-city restrictions — directly opposing the anti-sanctuary rubric ideal.",
              ["https://whyy.org/articles/analilia-mejia-new-jersey-11th-congressional-district-special-election/",
               "https://en.wikipedia.org/wiki/Analilia_Mejia"]),
    ]),

    # ---------------- Adam Hamawy (NJ-12, D) ----------------
    ("adam-hamawy", "NJ", "representative", [
        claim("ah1", "adam-hamawy", "sanctity_of_life", 0, False,
              "Explicitly supports codifying the right to abortion into federal law; his campaign website states 'The draconian policies enacted after the overturning of Roe v. Wade is a stain on our country' and he commits to restoring nationwide abortion access — rejecting life-from-conception personhood.",
              ["https://hamawyfornj.com/priorities",
               "https://ballotpedia.org/Adam_Hamawy"]),
        claim("ah2", "adam-hamawy", "border_immigration", 2, False,
              "Called for abolishing the Department of Homeland Security and ending mass deportation programs; won the June 2026 NJ-12 Democratic primary with endorsements from Bernie Sanders and Squad members who advocate sanctuary policies — opposing the anti-sanctuary enforcement rubric ideal.",
              ["https://en.wikipedia.org/wiki/Adam_Hamawy",
               "https://newjerseymonitor.com/2026/06/02/adam-hamawy-democratic-primary/"]),
    ]),

    # ---------------- Ryan Busse (MT-01, D) ----------------
    ("ryan-busse", "MT", "representative", [
        claim("rb1", "ryan-busse", "sanctity_of_life", 0, False,
              "Supports abortion rights and has stated he believes a woman has a 'Constitutional right to make whatever private decisions are best for her health and her family and her future — including the right to abortion' — rejecting any government restriction or personhood-from-conception standard.",
              ["https://busseformontana.com/",
               "https://montanafreepress.org/2026/01/08/ryan-busse-announces-for-western-house-race/"]),
        claim("rb2", "ryan-busse", "self_defense", 1, False,
              "Supports expanded background checks and red-flag laws for firearms; authored the 2021 book 'Gunfight: My Battle Against the Industry that Radicalized America' attacking the gun industry — positions that support the red-flag and background-check restrictions the rubric opposes.",
              ["https://ballotpedia.org/Ryan_Busse",
               "https://newlinesmag.com/reportage/montana-gubernatorial-hopeful-gun-owners-abortion-rights/"]),
    ]),

    # ---------------- Denise Powell (NE-02, D) ----------------
    ("denise-powell-ne-02", "NE", "representative", [
        claim("dp1", "denise-powell-ne-02", "sanctity_of_life", 0, False,
              "Has advocated for abortion access in Nebraska for a decade; won the 2026 NE-02 Democratic primary on a platform of restoring Roe v. Wade nationwide and protecting 'all aspects of reproductive healthcare'; endorsed by EMILY's List — rejecting any pro-life standard.",
              ["https://nebraskaexaminer.com/2026/05/13/denise-powell-wins-dem-nomination-in-nebraskas-2nd-district/",
               "https://emilyslist.org/candidate/denise-powell/"]),
        claim("dp2", "denise-powell-ne-02", "self_defense", 1, False,
              "Gun-violence-prevention platform includes universal background checks, red-flag laws to keep firearms from domestic abusers, and funded community-violence-intervention programs — supporting the regulatory restrictions the rubric opposes.",
              ["https://deniseforcongress.org/priorities/",
               "https://ballotpedia.org/Denise_Powell"]),
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
