#!/usr/bin/env python3
"""Enrichment batch 63: hand-curated claims for 5 federal House/Senate candidates.

Targets archetype_curated candidates from the BOTTOM of the alphabet bucket
(NY → IL → CO → AZ → CA) that had 0 evidence claims. Uses the
(slug + state + office_keyword) matcher to avoid collisions.

Mix (0 R / 5 D): La Shawn Ford (IL-07), Laura Fine (IL-09),
Yadira Caraveo (CO-08), Kirsten Engel (AZ-06), Scott Wiener (CA-11).
Each claim cites >=1 reliable source and reflects 2019-2025 voting
record / public positions.

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
    # ---------------- La Shawn Ford (IL-07, D, state rep → US House) ----------------
    ("la-shawn-ford", "IL", "representative", [
        claim("lf1", "la-shawn-ford", "self_defense", 1, False,
              "Ford chairs the Illinois House Firearm Public Awareness Task Force and has backed gun-restriction legislation throughout his tenure as a state representative. He supported the 2023 Protect Illinois Communities Act (PICA, SB 2226), which banned assault-style weapons and high-capacity magazines statewide — directly opposing the rubric's protection of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/La_Shawn_K._Ford",
               "https://www.ilga.gov/legislation/billstatus.asp?DocNum=2226&GAID=16&DocTypeID=SB&LegID=134879&SessionID=110&GA=102"]),
        claim("lf2", "la-shawn-ford", "sanctity_of_life", 0, False,
              "As an Illinois House Democrat since 2007, Ford voted YES on the 2019 Reproductive Health Act (HB 2495), which removed personhood language from Illinois law and established abortion as a fundamental right — rejecting any legal recognition of life from conception.",
              ["https://ballotpedia.org/La_Shawn_K._Ford",
               "https://www.ilga.gov/legislation/billstatus.asp?DocNum=2495&GAID=15&DocTypeID=HB&LegID=117984&SessionID=108&GA=101"]),
    ]),

    # ---------------- Laura Fine (IL-09, D, state senator → US House) ----------------
    ("laura-fine", "IL", "representative", [
        claim("lfn1", "laura-fine", "sanctity_of_life", 0, False,
              "Fine was a key advocate who helped pass the Illinois Reproductive Health Act (HB 2495, 2019), which removed personhood language from state law and established abortion as a fundamental right — rejecting life-from-conception protections.",
              ["https://ballotpedia.org/Laura_Fine",
               "https://www.ilga.gov/legislation/billstatus.asp?DocNum=2495&GAID=15&DocTypeID=HB&LegID=117984&SessionID=108&GA=101"]),
        claim("lfn2", "laura-fine", "self_defense", 1, False,
              "Fine fought for an Illinois assault weapons ban and sponsored legislation closing gun-purchase loopholes for domestic abusers; she also voted YES on the 2023 Protect Illinois Communities Act (PICA, SB 2226), which banned assault-style weapons and high-capacity magazines statewide.",
              ["https://ballotpedia.org/Laura_Fine",
               "https://www.ilga.gov/legislation/billstatus.asp?DocNum=2226&GAID=16&DocTypeID=SB&LegID=134879&SessionID=110&GA=102"]),
        claim("lfn3", "laura-fine", "border_immigration", 1, False,
              "Fine publicly called for abolishing ICE, referring to its agents as 'Trump's private army,' and introduced legislation in the Illinois Senate to bar ICE agents from becoming local law enforcement officers — rejecting the rubric's mandatory-deportation standard.",
              ["https://ballotpedia.org/Laura_Fine"]),
    ]),

    # ---------------- Yadira Caraveo (CO-08, D, former US Rep) ----------------
    ("yadira-caraveo", "CO", "representative", [
        claim("yc1", "yadira-caraveo", "sanctity_of_life", 0, False,
              "Caraveo ran for Congress explicitly to 'protect a woman's freedom to choose,' and received endorsements from EMILY's List and Planned Parenthood Action Fund — a platform and funding network that rejects any legal recognition of fetal personhood from conception.",
              ["https://en.wikipedia.org/wiki/Yadira_Caraveo",
               "https://ballotpedia.org/Yadira_Caraveo"]),
        claim("yc2", "yadira-caraveo", "self_defense", 1, False,
              "Caraveo was endorsed by the Giffords gun-safety PAC for her 2024 re-election campaign, and as a Colorado state representative she sponsored extreme-risk-protection-order (red-flag) legislation restricting firearm access — opposing the rubric's standard of no red-flag laws or assault-weapons bans.",
              ["https://giffords.org/candidates/yadira-caraveo/",
               "https://ballotpedia.org/Yadira_Caraveo"]),
        claim("yc3", "yadira-caraveo", "border_immigration", 0, False,
              "Caraveo voted NO on H.R. 2, the Secure the Border Act (118th Congress, May 2023), which would have funded border-wall construction and tightened asylum restrictions — opposing the rubric's wall-and-military-enforcement-first posture.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.govtrack.us/congress/members/yadira_caraveo/456887"]),
    ]),

    # ---------------- Kirsten Engel (AZ-06, D) ----------------
    ("kirsten-engel", "AZ", "representative", [
        claim("ke1", "kirsten-engel", "sanctity_of_life", 0, False,
              "Engel has stated she 'fought to protect reproductive rights' in the Arizona legislature and ran her 2022 and 2024 congressional campaigns on an abortion-access platform, opposing any restrictions based on fetal personhood from conception.",
              ["https://ballotpedia.org/Kirsten_Engel",
               "https://en.wikipedia.org/wiki/Kirsten_Engel"]),
        claim("ke2", "kirsten-engel", "border_immigration", 0, False,
              "Engel characterized the U.S.-Mexico border situation as 'a humanitarian crisis' and called for asylum-reform rather than wall construction or military enforcement — rejecting the rubric's wall-first, enforcement-first border posture.",
              ["https://ballotpedia.org/Kirsten_Engel"]),
        claim("ke3", "kirsten-engel", "biblical_marriage", 2, False,
              "As an Arizona state legislator (2017–2021) and congressional candidate, Engel opposed Republican efforts to restrict gender-affirming care and supported LGBTQ anti-discrimination protections, rejecting the rubric's standard of refusing to affirm transgender ideology in law and policy.",
              ["https://ballotpedia.org/Kirsten_Engel",
               "https://en.wikipedia.org/wiki/Kirsten_Engel"]),
    ]),

    # ---------------- Scott Wiener (CA-11, D, CA state senator → US House) ----------------
    ("scott-wiener-ca-11", "CA", "representative", [
        claim("sw1", "scott-wiener-ca-11", "biblical_marriage", 2, False,
              "Wiener authored California SB 107 (2022), making California the first 'transgender-minor sanctuary state' — barring enforcement of out-of-state laws restricting gender-affirming care for minors. Signed into law September 2022 and took effect January 2023.",
              ["https://en.wikipedia.org/wiki/California_Senate_Bill_107",
               "https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202120220SB107"]),
        claim("sw2", "scott-wiener-ca-11", "sanctity_of_life", 0, False,
              "As Chair of the California Legislative LGBTQ Caucus and a San Francisco Democrat, Wiener has consistently supported abortion-rights legislation and been endorsed by reproductive-rights organizations; he has voted YES on every major California abortion-access expansion bill since joining the State Senate in 2016.",
              ["https://ballotpedia.org/Scott_Wiener",
               "https://en.wikipedia.org/wiki/Scott_Wiener"]),
        claim("sw3", "scott-wiener-ca-11", "self_defense", 1, False,
              "Wiener has consistently backed California's assault-weapons bans, magazine-capacity limits, and background-check expansions as a California state senator from San Francisco; he holds an A rating from the Giffords Law Center and has opposed every effort to loosen California's strict gun laws.",
              ["https://ballotpedia.org/Scott_Wiener",
               "https://justfacts.votesmart.org/candidate/key-votes/129655/scott-wiener/"]),
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
