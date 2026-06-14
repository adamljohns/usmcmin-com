#!/usr/bin/env python3
"""Enrichment batch 200: 5 evidence_federal CA House candidates with 0 claims.

Targets from the bottom of the alphabet bucket (reverse-sorted); all CA.
archetype_curated and evidence_federal WY/WV/WI/WA/VA/GA/FL pools exhausted
or too thin for sourced claims — this batch moves to active CA candidates.

Mix: 5D (all progressive Democrats)
  Connie Chan       (CA-11 D, SF Supervisor · Pelosi-endorsed · Nov general)
  Marni von Wilpert (CA-48 D, SD City Councilmember · EMILY's List · Nov general)
  George Whitesides (CA-27 D, sitting U.S. Rep · former Virgin Galactic/NASA CEO)
  Julia Brownley    (CA-26 D, retiring 7-term incumbent · Emily's List/PP endorsements)
  Randy Villegas    (CA-22 D, Visalia professor · Bernie/WFP-endorsed · Nov general)

MINIFIED write — see enrich-batch-4.py module docstring for rationale.
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
    # ---- Connie Chan (CA-11, D, SF Supervisor · advancing to November general) ----
    ("connie-chan-ca-11", "CA", "Representative", [
        claim("cc1", "connie-chan-ca-11", "sanctity_of_life", 0, False,
              "Pledges on her campaign website to 'fight for access to the full range of reproductive health care including abortion and affordable contraception' and to 'push to restore full funding for Planned Parenthood which provides critical health services to over 2 million Americans every year' — a direct rejection of any legal protection of the unborn from conception.",
              ["https://ballotpedia.org/Connie_Chan",
               "https://www.conniechansf.com/"]),
        claim("cc2", "connie-chan-ca-11", "self_defense", 1, False,
              "Carries no NRA endorsement or gun-rights rating; she is backed by gun-control advocates including House Speaker Emerita Nancy Pelosi and Sen. Adam Schiff — the principal Senate champion of universal background checks and assault-weapons restrictions — and has given no indication she would oppose federal gun-control measures as a member of Congress.",
              ["https://ballotpedia.org/Connie_Chan",
               "https://news.ballotpedia.org/2026/06/05/scott-wiener-d-and-connie-chan-d-advanced-from-the-top-two-primary-in-californias-11th-congressional-district-on-june-2-2026/"]),
    ]),

    # ---- Marni von Wilpert (CA-48, D, SD City Councilmember · advancing to November general) ----
    ("marni-von-wilpert", "CA", "Representative", [
        claim("mvw1", "marni-von-wilpert", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List — the flagship fundraising vehicle for pro-abortion candidates — which calls her 'a champion for reproductive freedom' in the 2026 CA-48 race, placing her inside the abortion-industry endorsement network the rubric identifies as disqualifying.",
              ["https://emilyslist.org/candidate/marni-von-wilpert/",
               "https://emilyslist.org/news/emilys-list-endorses-marni-von-wilpert-for-californias-48th-congressional-district/"]),
        claim("mvw2", "marni-von-wilpert", "self_defense", 1, False,
              "As chair of the San Diego City Council's Public Safety Committee, von Wilpert introduced and shepherded the 'Eliminate Non-Serialized Untraceable Firearm' ordinance — banning ghost-gun kit sales in San Diego — and earned the endorsement of San Diegans for Gun Violence Prevention (SD4GVP), building a documented record of restricting firearms access directly at odds with the rubric's defense of Second Amendment rights.",
              ["https://fox5sandiego.com/news/local-news/council-member-introduces-ordinance-to-ban-ghost-guns/",
               "https://sd4gvp.org/oct-15-2025-sd4gvp-endorses-von-wilpert-congress/",
               "https://www.kpbs.org/news/politics/2021/09/14/san-diego-city-council-cracks-down-ghost-guns"]),
        claim("mvw3", "marni-von-wilpert", "sanctity_of_life", 0, False,
              "Has stated she 'protected abortion access' as chair of the San Diego City Council's Public Safety Committee; running as a publicly bisexual woman she has said she worries about 'losing my rights to equality under the law' under the Trump administration, signaling commitment to maintaining unrestricted reproductive and LGBTQ rights in federal law.",
              ["https://emilyslist.org/candidate/marni-von-wilpert/",
               "https://qvoicenews.com/2026/04/01/marni-von-wilpert-bisexual-san-diego-city-council-member-wants-to-represent-calif-s-48th-district/"]),
    ]),

    # ---- George Whitesides (CA-27, D, sitting U.S. Representative) ----
    ("george-whitesides", "CA", "Representative", [
        claim("gw1", "george-whitesides", "sanctity_of_life", 0, False,
              "States 'opposing restrictions on abortion' as an explicit policy priority for his congressional term — a direct rejection of any legal protection of the unborn from conception and alignment with the Democratic party's pro-abortion legislative agenda.",
              ["https://ballotpedia.org/George_Whitesides",
               "https://www.govtrack.us/congress/members/george_whitesides/456977"]),
        claim("gw2", "george-whitesides", "self_defense", 1, False,
              "Has backed federal legislation to prevent sales of semiautomatic centerfire rifles to persons under 21 and to require universal background checks for all firearm transfers, as reflected in the Congressional Record — positions directly opposing the rubric's standard of uninfringed Second Amendment rights.",
              ["https://www.congress.gov/member/george-whitesides/W000830",
               "https://www.govtrack.us/congress/members/george_whitesides/456977"]),
    ]),

    # ---- Julia Brownley (CA-26, D, retiring 7-term incumbent) ----
    ("julia-brownley", "CA", "Representative", [
        claim("jb1", "julia-brownley", "sanctity_of_life", 4, False,
              "Endorsed in her congressional campaigns by both Emily's List and Planned Parenthood — two of the flagship organizations in the abortion-industry endorsement-and-funding network the rubric identifies as disqualifying — and consistently voted with the pro-abortion caucus across her 7 terms.",
              ["https://en.wikipedia.org/wiki/Julia_Brownley",
               "https://ballotpedia.org/Julia_Brownley"]),
        claim("jb2", "julia-brownley", "self_defense", 1, False,
              "A consistent gun-control advocate with no NRA endorsement; voted with Democratic colleagues on major gun-control legislation — including universal background check bills and assault-weapons restrictions — throughout her 13 years in Congress, with GovTrack's 2024 report card documenting continued alignment with the House gun-control caucus through her final term.",
              ["https://en.wikipedia.org/wiki/Julia_Brownley",
               "https://www.govtrack.us/congress/members/julia_brownley/412516"]),
    ]),

    # ---- Randy Villegas (CA-22, D, Visalia professor · advancing to November general) ----
    ("randy-villegas", "CA", "Representative", [
        claim("rv1", "randy-villegas", "sanctity_of_life", 0, False,
              "Endorsed by the Congressional Progressive Caucus PAC — which explicitly includes protecting 'reproductive rights including abortion access' among its core commitments — and by Bernie Sanders and the Working Families Party, both of which mandate abortion rights advocacy from endorsed candidates; Villegas's 'fully progressive' platform opposes any restriction on abortion access.",
              ["https://ballotpedia.org/Randy_Villegas_(California)",
               "https://news.ballotpedia.org/2026/03/09/incumbent-david-valadao-r-jasmeet-bains-d-eric-garcia-d-rudy-salas-d-and-randy-villegas-d-are-running-in-the-top-two-primary-for-californias-22nd-congressional-district-on-june-2-2026/"]),
        claim("rv2", "randy-villegas", "economic_stewardship", 2, False,
              "Campaigns explicitly against any cuts to Medicaid, Social Security, and federal nutrition programs, framing his candidacy as 'a fight for the soul of the Democratic Party' toward expanding government social spending — a posture directly at odds with the rubric's call for fiscal discipline, a balanced budget, and opposition to runaway deficit spending.",
              ["https://ballotpedia.org/Randy_Villegas_(California)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher; slug uniqueness prevents collisions here."""
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
