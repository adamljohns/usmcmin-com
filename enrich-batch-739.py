#!/usr/bin/env python3
"""Enrichment batch 739: hand-curated claims for 4 NJ Republican state senators.

Continuing from batch 738 (Parker Space, Mike Testa, Vincent Polistina,
Joseph Pennacchio). archetype_curated federal pool fully exhausted; continuing
with archetype_party_default R state senators from NJ (11 remaining after batch 738).

Targets (reverse-alpha by name within NJ):
  Robert W. Singer (NJ-30), Kristin Corrado (NJ-40),
  Doug Steinhardt (NJ-23), Jon Bramnick (NJ-21).

Sources: njleg.state.nj.us, newjerseymonitor.com, insidernj.com, senatenj.com,
en.wikipedia.org, ballotpedia.org, ivoterguide.com, pub.njleg.state.nj.us.
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
    # ---------------- Robert W. Singer (NJ-30, State Senator) ----------------
    ("robert-w-singer", "NJ", "Senator", [
        claim("rs1", "robert-w-singer", "sanctity_of_life", 0, True,
              "Voted no on NJ S49 (Freedom of Reproductive Choice Act, January 2022), joining fellow Republican state senators in rejecting the bill that removed nearly all remaining statutory protections for the unborn and codified abortion-on-demand into New Jersey state law. Singer, who has represented the conservative Ocean-Monmouth corridor since 1994, maintains a consistently pro-life posture in one of the nation's most permissive abortion states.",
              ["https://newjerseymonitor.com/2022/01/10/abortion-rights-bill-clears-legislature/",
               "https://www.insidernj.com/press-release/senate-approves-weinberg-greenstein-sweeney-freedom-reproductive-choice-act/"]),
        claim("rs2", "robert-w-singer", "economic_stewardship", 2, True,
              "As Senate Republican Conference Leader (2018–present) and the senior ranking Republican on the Health, Human Services and Senior Citizens Committee — New Jersey's longest-serving state senator — Singer has a consistent record of opposing large budget expansions and advancing cost-containment legislation. His telehealth cost-protection bill, which passed the full Senate, reduces out-of-pocket patient costs rather than piling on government-mandated coverage requirements that raise premiums.",
              ["https://www.senatenj.com/m/newsflash/home/detail/1219",
               "https://www.njleg.state.nj.us/legislative-roster/93/senator-singer"]),
    ]),

    # ---------------- Kristin Corrado (NJ-40, State Senator) ----------------
    ("kristin-corrado", "NJ", "Senator", [
        claim("kc1", "kristin-corrado", "sanctity_of_life", 0, True,
              "On iVoterGuide, Senator Corrado stated: 'Human life begins at conception and deserves legal protection at every stage until natural death' — a personhood-from-conception position. She backed that conviction with her vote: she voted no on NJ S49 (Freedom of Reproductive Choice Act, January 2022), opposing the legislation that codified abortion-on-demand into state law over all Republican objections.",
              ["https://ivoterguide.com/candidate?canK=51869&elecK=694&primarypartyk=R&raceK=6803",
               "https://newjerseymonitor.com/2022/01/10/abortion-rights-bill-clears-legislature/"]),
        claim("kc2", "kristin-corrado", "family_child_sovereignty", 0, True,
              "Introduced the 'Parents Bill of Rights Act' (with Sen. Anthony Bucco) to give parents substantially more information about what their children will be taught and to expand their ability to opt out of any lesson — not just the narrow statutory carve-outs that previously existed. As Ranking Republican on the Senate Judiciary Committee, Corrado has also pressed back on legislative attempts to erode parental authority over minors' medical decisions.",
              ["https://www.insidernj.com/press-release/corrado-bucco-introduce-parents-bill-of-rights-act-for-education/",
               "https://ballotpedia.org/Kristin_Corrado"]),
    ]),

    # ---------------- Doug Steinhardt (NJ-23, State Senator) ----------------
    ("doug-steinhardt", "NJ", "Senator", [
        claim("ds1", "doug-steinhardt", "sanctity_of_life", 0, True,
              "Described himself as pro-life upon being sworn in as the 23rd District state senator in December 2022, placing him squarely against New Jersey's permissive abortion regime. As former chairman of the NJ Republican State Committee (2017–2020), Steinhardt championed a conservative platform of fiscal responsibility, parental rights, and the defense of unborn life in a state where Democrats have pushed abortion access to near-absolute levels.",
              ["https://www.insidernj.com/press-release/steinhardt-sworn-in-as-state-senator-for-new-jerseys-23rd-legislative-district/",
               "https://ballotpedia.org/Doug_Steinhardt"]),
        claim("ds2", "doug-steinhardt", "self_defense", 1, True,
              "A Lifetime Member of the National Rifle Association who has publicly described himself as 'a strong advocate for the rights of law-abiding citizens to defend themselves.' In New Jersey — where magazine-capacity limits, semi-automatic rifle restrictions, and onerous carry-permit requirements constitute some of the heaviest civilian disarmament burdens in the nation — Steinhardt's NRA Lifetime membership and pro-gun record represent a principled stand against the state's restrictive firearms framework.",
              ["https://www.insidernj.com/press-release/steinhardt-sworn-in-as-state-senator-for-new-jerseys-23rd-legislative-district/",
               "https://www.senatenj.com/169/Doug-Steinhardt---District-23"]),
    ]),

    # ---------------- Jon Bramnick (NJ-21, State Senator) ----------------
    ("jon-bramnick", "NJ", "Senator", [
        claim("jb1", "jon-bramnick", "sanctity_of_life", 0, False,
              "A self-described 'pro-choice Republican' who abstained on NJ S49 (Freedom of Reproductive Choice Act, January 2022) — saying the bill 'went too far' while making clear he supports abortion access. By 2024, during his Republican gubernatorial primary campaign, Bramnick explicitly embraced the 'pro-choice Republican' label, rejecting the life-at-conception standard the RESOLUTE rubric requires.",
              ["https://en.wikipedia.org/wiki/Jon_Bramnick",
               "https://ballotpedia.org/Jon_Bramnick"]),
        claim("jb2", "jon-bramnick", "economic_stewardship", 2, True,
              "Supports a constitutional amendment to cap annual New Jersey state budget increases at 2 percent — a structural guard against deficit spending in the nation's most heavily taxed state. Bramnick also helped eliminate the estate tax and backed senior and veteran tax relief, citing billions in tax cuts since he joined the Assembly in 2004.",
              ["https://en.wikipedia.org/wiki/Jon_Bramnick",
               "https://ballotpedia.org/Jon_Bramnick"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
