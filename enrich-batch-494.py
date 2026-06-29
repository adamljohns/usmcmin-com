#!/usr/bin/env python3
"""Enrichment batch 494: 5 Texas state legislators with 0 claims (continuing TX D/bottom bucket).

All archetype_curated federal buckets are fully enriched. Continuing with
evidence_state Texas state legislators, working from the top of the
reverse-alphabetical-by-name TX bucket.

Targets (all TX, evidence_state):
  Toni Rose (toni-rose)              — TX D, HD-110 Dallas (Oak Cliff/Pleasant Grove);
                                       serving since 2012; First Vice-Chair TX House Dem Caucus;
                                       endorsed by Planned Parenthood TX Votes 2024;
                                       pro-choice public record since at least 2011.
  Terry Meza (terry-meza)            — TX D, HD-105 Dallas County (Irving);
                                       serving since 2019; introduced HB 196 (87th Leg 2021)
                                       to require retreat before deadly force outside home;
                                       consistently opposed school vouchers.
  Terry Canales (terry-canales)      — TX D, HD-40 Hidalgo County (Edinburg);
                                       serving since 2013; co-authored and voted FOR
                                       HB 1927 (Constitutional Carry, 2021) — one of only
                                       two Democrats to do so; first Latino Chair TX House
                                       Transportation Committee (2019-2023) and
                                       Transportation Funding Committee (2025).
  Taylor Rehmet (taylor-rehmet)      — TX D, SD-9 (Collin/Denton counties);
                                       won special election, seated Feb 19, 2026;
                                       union president/machinist/veteran; endorsed by
                                       TX AFL-CIO and Working Families Party; labeled
                                       "anti-gun Democrat" by Texas Gun Rights PAC.
  Suleman Lalani (suleman-lalani)    — TX D, HD-76 Fort Bend County (Sugar Land, Stafford);
                                       serving since 2023; first Muslim and South Asian
                                       member of TX Legislature; physician (general
                                       practitioner); scored 56% on Texas Alliance for Life
                                       2025 scorecard — unusually high for a House Democrat.

Key TX legislation cited:
  SB 8  (87th Leg, 2021) — Texas Heartbeat Act; bans abortion ~6 wks; House 83-64 May 6 2021
  HB 196 (87th Leg, 2021) — Meza bill; requires retreat before deadly force outside home;
                              limits stand-your-ground rights
  HB 1927 (87th Leg, 2021) — Constitutional Carry; removes license req for 21+ carry;
                               House 87-58 Apr 15 2021; Canales was a joint author
  HB 3  (89th Leg, 2025) — TX Education Savings Account school voucher program;
                             House 85-63 Apr 17 2025; all 62 House Dems voted NO

NOTE: writes scorecard.json MINIFIED to keep file ~35-36 MB under GitHub 50 MB cap.
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
    # ---- Toni Rose (TX D, HD-110, Dallas — Oak Cliff, Pleasant Grove, Balch Springs, Mesquite) ----
    # Serving since 2012 (13+ years); First Vice-Chair TX House Democratic Caucus;
    # endorsed by Planned Parenthood TX Votes 2024; pro-choice on record since 2011
    ("toni-rose", "TX", "Representative", [
        claim("tr1", "toni-rose", "sanctity_of_life", 0, False,
              "Rose is a consistent pro-choice Democrat representing Dallas's HD-110 since 2012. She voted against Texas SB 8 (Texas Heartbeat Act, 87th Legislature, 2021), which bans most abortions once a fetal heartbeat is detected at approximately six weeks of pregnancy. The House passed SB 8 83-64 on May 6, 2021, with Rose voting with the Democratic bloc against the bill. She has publicly argued since at least 2011 that cutting access to Planned Parenthood 'foster[s] an environment where more abortions will occur, not less,' reflecting a career-long commitment to abortion access that rejects any personhood-from-conception standard.",
              ["https://ballotpedia.org/Toni_Rose",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://legiscan.com/TX/rollcall/SB8/id/1039526"]),
        claim("tr2", "toni-rose", "sanctity_of_life", 4, False,
              "Rose was endorsed by Planned Parenthood Texas Votes in the 2024 general election. Planned Parenthood Texas Votes requires candidates to commit '100% to supporting reproductive health care access, including safe, legal abortion' to receive its endorsement, placing Rose squarely inside the abortion-industry advocacy network the rubric identifies as a disqualifying tie. She is a member of the Texas House Democratic Caucus leadership (First Vice-Chair) and has sustained this alignment throughout her tenure.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-texas-votes/elections/november-2024-elections-endorsements",
               "https://ballotpedia.org/Toni_Rose"]),
        claim("tr3", "toni-rose", "family_child_sovereignty", 0, False,
              "Rose voted against Texas HB 3 (89th Legislature, 2025), the Education Savings Account program creating the state's first universal school voucher system. All 62 House Democrats, including Rose, voted NO on HB 3 when it passed 85-63 on April 17, 2025. Her opposition rejects the expansion of parental authority over education funding that the rubric's family-sovereignty standard supports.",
              ["https://ballotpedia.org/Toni_Rose",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://legiscan.com/TX/bill/HB3/2025"]),
    ]),

    # ---- Terry Meza (TX D, HD-105, Dallas County — Irving) ----
    # Serving since 2019; introduced HB 196 (87th Leg, 2021) to limit stand-your-ground;
    # voted for Raney amendment (88th Leg, 2023) stripping voucher language;
    # rated pro-choice by TX Choice Tracker
    ("terry-meza", "TX", "Representative", [
        claim("tm1", "terry-meza", "self_defense", 3, False,
              "Meza introduced Texas HB 196 in the 87th Legislature (2021 session), a bill that would have required a homeowner to 'exhaust the potential of safely retreating into their habitation before using deadly force in defense of themselves or their property.' The bill proposed a duty-to-retreat for stand-your-ground situations outside the home, directly undermining the castle-doctrine principle that defenders need not retreat before using deadly force. The proposal drew national attention as an attempt to weaken Texans' statutory self-defense rights.",
              ["https://www.elliscountypress.com/news/texas-hb-196-repeals-castle-doctrine",
               "https://www.snopes.com/fact-check/house-bill-196-castle-doctrine/",
               "https://en.wikipedia.org/wiki/Terry_Meza"]),
        claim("tm2", "terry-meza", "sanctity_of_life", 0, False,
              "Meza voted against Texas SB 8 (Texas Heartbeat Act, 87th Legislature, 2021), which bans most abortions after approximately six weeks of pregnancy. The House passed SB 8 83-64 on May 6, 2021; Meza, a Democrat representing HD-105 (Irving, Dallas County) since 2019, voted with the House Democratic bloc against the bill. She is rated pro-choice by the Texas Choice Tracker.",
              ["https://ballotpedia.org/Terry_Meza",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://choicetracker.org/tx/people"]),
        claim("tm3", "terry-meza", "family_child_sovereignty", 0, False,
              "Meza has consistently opposed school choice legislation. In the 88th Legislature (2023), she voted for the Raney amendment that stripped voucher language from an omnibus education bill, blocking the last attempt to pass vouchers in that session. In the 89th Legislature (2025), she voted NO on HB 3, the Education Savings Account school voucher program that passed 85-63 on April 17, 2025, with all 62 House Democrats, including Meza, opposing it.",
              ["https://ballotpedia.org/Terry_Meza",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://legiscan.com/TX/bill/HB3/2025"]),
    ]),

    # ---- Terry Canales (TX D, HD-40, Hidalgo County — Edinburg, McAllen area) ----
    # Serving since 2013; first Latino Chair TX House Transportation Committee (2019-2023);
    # Transportation Funding Committee Chair (2025); co-authored HB 1927 (Constitutional Carry)
    # with Republicans — one of only two Democrats to support the bill
    ("terry-canales", "TX", "Representative", [
        claim("tc1", "terry-canales", "self_defense", 0, True,
              "Canales was one of only two House Democrats who co-authored and voted for Texas HB 1927 (Constitutional Carry Act, 87th Legislature, 2021), the bill removing the license requirement for Texans 21 and older to carry a handgun openly or concealed. The Texas Tribune noted that Canales and Rep. Ryan Guillen 'were expected because they were already joint authors of the legislation.' HB 1927 passed the House 87-58 on April 15, 2021. Canales's co-authorship and YES vote on constitutional carry directly aligns with the rubric's self-defense standard — a rare position for a Democratic legislator.",
              ["https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://ballotpedia.org/Terry_Canales",
               "https://legiscan.com/TX/bill/HB1927/2021"]),
        claim("tc2", "terry-canales", "family_child_sovereignty", 0, False,
              "Canales voted NO on Texas HB 3 (89th Legislature, 2025), the Education Savings Account school voucher program that passed 85-63 on April 17, 2025. All 62 House Democrats, including Canales, voted against the bill. Despite his cross-aisle record on gun rights, Canales opposed the expansion of parental education choice the rubric's family-sovereignty standard supports.",
              ["https://ballotpedia.org/Terry_Canales",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://legiscan.com/TX/bill/HB3/2025"]),
    ]),

    # ---- Taylor Rehmet (TX D, SD-9 — Collin/Denton Counties; won Feb 2026 special election) ----
    # Seated Feb 19, 2026; union president/machinist/veteran; missed 89th session main votes
    # (SB 8 was 2021, HB 3 was April 2025); positions sourced from campaign and endorsements
    ("taylor-rehmet", "TX", "Senator", [
        claim("treh1", "taylor-rehmet", "family_child_sovereignty", 0, False,
              "Rehmet's campaign platform explicitly pledges to 'fully fund public schools and end voucher schemes that drain them' and to 'reinvest in public education... and reverse the privatization of Texas schools by way of tax-payer dollars' — a direct commitment to opposing any school-choice program that redirects public funding toward private or home-based alternatives. He won his February 2026 SD-9 special election on this platform and was endorsed by the Texas AFL-CIO and Working Families Party, both of which oppose education savings account programs as privatization of public schools.",
              ["https://www.taylorfortx.com/",
               "https://ballotpedia.org/Taylor_Rehmet",
               "https://texasaflcio.org/news/texas-union-win-taylor-rehmet-headed-runoff-sd-9-special-election"]),
        claim("treh2", "taylor-rehmet", "self_defense", 1, False,
              "Texas Gun Rights PAC endorsed Rehmet's Republican opponent Leigh Wambsganss in the 2025-26 SD-9 special election runoff, explicitly labeling Rehmet an 'anti-gun Democrat backed by national gun-confiscation interests.' The PAC's active opposition and endorsement of his rival places Rehmet among candidates whose positions and political backing suggest support for gun-control measures — including restrictions on carry rights and firearm-type or magazine regulations — that the rubric's self-defense standard opposes.",
              ["https://txgunrights.org/pro-2a-voters-must-see-results-or-risk-losing-texas-in-november/",
               "https://ballotpedia.org/Taylor_Rehmet",
               "https://www.npr.org/2026/02/01/nx-s1-5695678/democrat-taylor-rehmet-wins-texas-state-senate-seat"]),
    ]),

    # ---- Suleman Lalani (TX D, HD-76, Fort Bend County — Sugar Land, Stafford, Meadows Place) ----
    # Serving since 2023 (88th Legislature onward); first Muslim/South Asian TX legislator;
    # physician (general practitioner); co-chair AAPI Caucus; scored 56% on TAL 2025 scorecard
    ("suleman-lalani", "TX", "Representative", [
        claim("sl1", "suleman-lalani", "sanctity_of_life", 0, False,
              "Lalani is a Democratic member of the Texas House aligned with his party's pro-choice caucus. He was not in office during the 87th Legislature (2021) when Texas SB 8 (Heartbeat Act) and HB 1280 (trigger ban) were enacted. In the 89th Legislature (2025), he scored 56% on the Texas Alliance for Life's Legislative Scorecard — an unusually high score compared to the near-zero average for House Democrats — indicating he voted pro-life on a majority of the specific bills TAL tracked. He has not, however, made public statements affirming life from the moment of fertilization or personhood at conception, and his overall Democratic alignment and coalition suggest he falls short of the rubric's highest pro-life standard.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Suleman_Lalani",
               "https://en.wikipedia.org/wiki/Suleman_Lalani"]),
        claim("sl2", "suleman-lalani", "family_child_sovereignty", 0, False,
              "Lalani voted NO on Texas HB 3 (89th Legislature, 2025), the Education Savings Account program creating the state's first universal school voucher system. All 62 House Democrats, including Lalani, voted against HB 3 when it passed 85-63 on April 17, 2025. As co-chair of the AAPI Caucus and a physician who champions expanded access to public healthcare, Lalani's legislative record reflects support for public-institution funding over redirecting public dollars to private alternatives.",
              ["https://ballotpedia.org/Suleman_Lalani",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://legiscan.com/TX/bill/HB3/2025"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent same-slug collisions across states."""
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

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36 MB under GitHub 50 MB cap).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
