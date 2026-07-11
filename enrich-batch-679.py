#!/usr/bin/env python3
"""Enrichment batch 679: hand-curated claims for 5 PA state senators.

archetype_curated federal bucket exhausted; continuing archetype_party_default
state senators from bottom of alphabet (PA Democrats — reverse-alpha top of
remaining bucket). All five co-sponsored SB200 (2025 assault weapons ban);
claims span self_defense, sanctity_of_life, border_immigration,
family_child_sovereignty, and economic_stewardship.

Targets (from top of reverse-alpha 0-claim list):
  Wayne D. Fontana      (PA SD 42, Pittsburgh/Allegheny — D, Dem Chair Law & Justice)
  Vincent J. Hughes     (PA SD 7, Philadelphia/Montgomery — D, Senate Dem Appropriations Chair)
  Timothy P. Kearney    (PA SD 26, Delaware County — D, Min. Chair Institutional Sustainability)
  Steven J. Santarsiero (PA SD 10, Bucks County — D, Secretary Senate Dem Caucus)
  Patty Kim             (PA SD 15, Dauphin County — D, Min. Chair Local Government)
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
    # ---------- Wayne D. Fontana (PA SD 42, Pittsburgh/Allegheny County — D,
    #            Dem Chair Law & Justice; in office since June 2005 special election) ----------
    ("wayne-d-fontana", "PA", "State Senator", [
        claim("wdf1", "wayne-d-fontana", "self_defense", 1, False,
              "A longstanding gun-control legislator: prime Senate sponsor of SB 134 "
              "(2021-22 session), the Pennsylvania Extreme Risk Protection Order Act "
              "(red-flag law), which Republicans blocked from a floor vote via a unanimous "
              "discharge-petition veto on June 13, 2022; prime sponsor of SB 48 (2023-24, "
              "closing 3D-printed firearm loopholes) and SB 49 (2023-24, defining 80% "
              "receivers as firearms under the Uniform Firearm Act); and co-sponsored "
              "SB200 (2025-26), banning the manufacture, sale, and transfer of assault "
              "weapons and large-capacity magazines statewide. Stated in 2026: 'The "
              "Republicans' refusal to help us address the gun-violence epidemic is shameful.'",
              ["https://www.palegis.us/legislation/bills/2025/sb200",
               "https://www.senatorfontana.com/legislation/2023-24",
               "https://pasenate.com/senate-democrats-call-for-vote-on-pa-red-flag-law-gop-votes-no/"]),
        claim("wdf2", "wayne-d-fontana", "family_child_sovereignty", 0, False,
              "Voted NO on SB 7 (October 24, 2023), which gave parents the right to opt "
              "their child out of school-assigned books containing sexually explicit content; "
              "the bill passed the Senate 29-21 (28 Republicans + 1 Democrat yes; all "
              "remaining 21 Democrats no). Fontana is confirmed in the October 24 roll call "
              "as one of the 21 Democrats voting no — the full NO list includes Brewster, "
              "Cappelletti, Collett, Comitta, Costa, Dillon, Flynn, Fontana, Haywood, "
              "Hughes, Kane, Kearney, Miller, Muth, Santarsiero, Saval, Schwank, Street, "
              "Tartaglione, Williams (A.), Williams (L.).",
              ["https://legiscan.com/PA/bill/SB7/2023",
               "https://www.the74million.org/article/pa-senate-passes-explicit-content-bill-after-debating-whether-its-a-book-ban/",
               "https://www.pasenategop.com/news/senate-passes-bill-to-settle-issue-of-sexually-explicit-content-in-school/"]),
    ]),

    # ---------- Vincent J. Hughes (PA SD 7, Philadelphia/Montgomery County — D,
    #            Senate Dem Appropriations Chair; in office since Nov 1994 special election) ----------
    ("vincent-j-hughes", "PA", "State Senator", [
        claim("vh1", "vincent-j-hughes", "self_defense", 1, False,
              "Co-sponsored SB200 (introduced June 3, 2025), the Pennsylvania Assault Weapons "
              "and Large Capacity Magazine Ban, which would prohibit the manufacture, sale, and "
              "transfer of assault weapons and magazines holding more than 10 rounds statewide "
              "and establish a Firearms and Ammunition Buyback Program. Hughes is one of 15 "
              "Democratic co-sponsors alongside Senators Santarsiero, Kearney, Kim, Costa, "
              "Haywood, Fontana, and others; the bill was referred to the Senate Judiciary "
              "Committee.",
              ["https://www.palegis.us/legislation/bills/2025/sb200"]),
        claim("vh2", "vincent-j-hughes", "economic_stewardship", 2, False,
              "As Senate Democratic Appropriations Chair, championed the $50.09 billion "
              "Pennsylvania FY2025–26 General Appropriation Act (SB 160), which the Senate "
              "passed 40–9 on November 12, 2025 after a 135-day budget impasse. Hughes "
              "hailed the spending plan as delivering ‘affordability,’ citing new "
              "programs including a Working Pennsylvanian Tax Credit, increased school funding, "
              "childcare workforce retention payments, and direct care worker support — "
              "consistent with his career-long advocacy for government spending expansion over "
              "deficit discipline.",
              ["https://pasenate.com/senator-vincent-hughes-on-the-senate-passage-of-pennsylvanias-25-26-budget-we-delivered-on-affordability/",
               "https://penncapital-star.com/government-politics/135-days-late-50-1-billion-pennsylvania-budget-earns-bipartisan-support/"]),
    ]),

    # ---------- Timothy P. Kearney (PA SD 26, Delaware County — D,
    #            Min. Chair Institutional Sustainability; in office since Nov 2018) ----------
    ("timothy-p-kearney", "PA", "State Senator", [
        claim("tk1", "timothy-p-kearney", "self_defense", 1, False,
              "Co-sponsored SB262 (2025–26), establishing extreme risk protection orders "
              "(a red-flag law framework allowing courts to temporarily remove firearms from "
              "individuals deemed a risk to themselves or others), referred to Senate Judiciary "
              "on February 20, 2025; and co-sponsored SB200 (introduced June 3, 2025), banning "
              "the manufacture, sale, and transfer of assault weapons and large-capacity magazines "
              "statewide and establishing a Firearms and Ammunition Buyback Program. Kearney is "
              "among the 15 Democratic co-sponsors of SB200 alongside Senators Santarsiero, "
              "Hughes, Kim, Haywood, Costa, Fontana, and others.",
              ["https://www.palegis.us/legislation/bills/2025/sb262",
               "https://www.palegis.us/legislation/bills/2025/sb200"]),
        claim("tk2", "timothy-p-kearney", "border_immigration", 2, False,
              "Prime sponsor in the ‘ICE Out of Pennsylvania’ legislative package "
              "unveiled at a State Capitol rally on June 9, 2026. The suite spans multiple bills "
              "including SB1071 (requiring ICE and law enforcement to wear identification during "
              "enforcement operations), SB1125 (requiring school districts to implement "
              "immigration-enforcement response procedures), and SB1193 (prohibiting ICE arrests "
              "within 1,000 feet of courthouses and Commonwealth-owned facilities without a "
              "judicial warrant). Kearney also issued a statement condemning ICE operations and "
              "calling for state action to protect constitutional rights.",
              ["https://www.senatorkearney.com/pennsylvania-state-senators-call-for-ice-out-of-pennsylvania/",
               "https://whyy.org/articles/pennsylvania-democrats-ice-out-legislation-rally-senate/"]),
    ]),

    # ---------- Steven J. Santarsiero (PA SD 10, Bucks County — D,
    #            Secretary Senate Dem Caucus; in office since Nov 2018) ----------
    ("steven-j-santarsiero", "PA", "State Senator", [
        claim("ss1", "steven-j-santarsiero", "self_defense", 1, False,
              "Named first-listed co-prime sponsor of SB200 (introduced June 3, 2025), which "
              "amends Title 18 of the Pennsylvania Consolidated Statutes to ban the manufacture, "
              "sale, and transfer of assault weapons and large-capacity magazines statewide and "
              "establishes a Firearms and Ammunition Buyback Program. Santarsiero’s lead "
              "role on SB200 continues a history of gun control advocacy, including his claim "
              "to have authored Pennsylvania’s prior gun safety law while serving in the "
              "PA House (2008–2016).",
              ["https://www.palegis.us/legislation/bills/2025/sb200"]),
        claim("ss2", "steven-j-santarsiero", "sanctity_of_life", 0, False,
              "Self-described ‘outspoken defender of women’s reproductive rights’ "
              "who publicly committed to fighting any attempt to undermine them. Ahead of the "
              "July 8, 2022 Senate vote on SB106 — a constitutional amendment package "
              "declaring no state constitutional right to taxpayer-funded abortion or any "
              "abortion-related right — Santarsiero stated ‘There will be a "
              "reaction’; the measure passed 28–22 on a largely party-line vote with "
              "Senate Democrats in opposition. His Senate website carries a press release "
              "reaffirming his commitment to protecting women’s reproductive rights.",
              ["https://pasenate.com/senator-santarsiero-reaffirms-commitment-to-protecting-womens-reproductive-rights/",
               "https://www.inquirer.com/politics/pennsylvania/pa-senate-constitutional-amendments-abortion-elections-voting-20220708.html"]),
    ]),

    # ---------- Patty Kim (PA SD 15, Dauphin County/Harrisburg — D,
    #            Min. Chair Local Government; in Senate since Jan 2025, PA House 2013-2024) ----------
    ("patty-kim", "PA", "State Senator", [
        claim("pk1", "patty-kim", "self_defense", 1, False,
              "As a PA House member, voted YES on HB 777 (the Ghost Guns Act), which passed "
              "104–97 on March 27, 2024, banning the sale or purchase of firearms without "
              "serial numbers (privately made firearms) and requiring background checks for such "
              "transactions; Kim is listed as a co-sponsor of HB 777. As a state senator, "
              "co-sponsored SB 769 (introduced May 22, 2025), requiring safe storage of firearms "
              "when not in use with penalties for violations; the bill was referred to the Senate "
              "Judiciary Committee.",
              ["https://penncapital-star.com/government-politics/pa-house-passes-bill-banning-ghost-gun-parts/",
               "https://legiscan.com/PA/bill/HB777/2023",
               "https://www.palegis.us/legislation/bills/2025/sb769"]),
        claim("pk2", "patty-kim", "sanctity_of_life", 0, False,
              "States a ‘100% pro-choice voting record’ publicly on her campaign "
              "website and BallotReady profile. During her twelve years in the PA House "
              "(2013–2024), she opposed abortion restrictions including HB 321 and Senate "
              "Bill 3, positions that reject any state recognition of fetal personhood from "
              "conception. First elected to the PA Senate in November 2024 representing "
              "SD 15 (Dauphin County, Harrisburg area).",
              ["https://www.ballotready.org/people/patty-h-kim-681d060f-7c19-4416-92fc-8f63a833ab76",
               "https://pattykimforpa.com/vote/"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
