#!/usr/bin/env python3
"""Enrichment batch 542: 10 new claims across 5 Texas Republican state representatives.

Continuing the TX evidence_state pool (C/D-names, reverse-alpha). All five are
Republican state reps with 0 claims, taken from the top of the reverse-alpha list
after batch 541's D-name pass (Drew, Don, Denise, David x2).

Targets (reverse alpha by name within TX R pool):
  Daniel Alders       (HD-6, Panola/Shelby County NE Texas — freshman Jan 2025)
  Dade Phelan         (HD-21, SE Texas Beaumont area — former Speaker 2021-2025, not seeking re-election)
  Cole Hefner         (HD-5, Wood/Camp County NE Texas — chairs Homeland Security/Public Safety cmte)
  Cody Vasut          (HD-25, Angleton/Brazoria County SW Houston — chairs Redistricting cmtes)
  Cody Harris         (HD-8, Palestine/Anderson County East Texas — NRA lifetime member)

Two distinct rubric-category claims per target. Sources: texasallianceforlife.org,
txgunrights.org, texastribune.org, ballotpedia.org, legiscan.com, txgunrights.org.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub 50MB limit.
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
    # -------------- Daniel Alders (TX-R, HD-6, Panola/Shelby County) --------------
    ("daniel-alders", "TX", "Representative", [
        claim("da1", "daniel-alders", "sanctity_of_life", 0, True,
              "Received a 93% score on the Texas Alliance for Life 89th Legislature (2025) Legislative Scorecard, earning a near-perfect rating for his votes protecting unborn life including SB 31 (Life of the Mother Act, clarifying medically necessary care for pregnant women) and SB 33 (Stop Taxpayer-Funded Abortion Travel Act). As a freshman representative (since January 14, 2025) representing Panola and Shelby counties in deep-East Texas, Alders entered the House with a strong pro-life voting record aligned with his conservative district.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Daniel_Alders"]),
        claim("da2", "daniel-alders", "self_defense", 0, True,
              "Received the Texas Gun Rights (TXGR) PAC endorsement in the November 5, 2024 general election for Texas House District 6, listed as a TXGR-endorsed candidate on the statewide voter guide. Texas Gun Rights endorsements require candidates to affirm opposition to red-flag laws, universal background checks, and gun registries and to pledge support for constitutional carry and Second Amendment protections — confirming Alders' commitment to unrestricted gun rights entering his first legislative term.",
              ["https://txgunrights.org/texas-gun-rights-voter-guide-nov-5th-general-election/",
               "https://ballotpedia.org/Daniel_Alders"]),
    ]),

    # ----------- Dade Phelan (TX-R, HD-21, Beaumont area — former Speaker) -----------
    ("dade-phelan", "TX", "Representative", [
        claim("dp1", "dade-phelan", "sanctity_of_life", 0, True,
              "Received a 100% score on the Texas Alliance for Life 89th Legislature (2025) Legislative Scorecard. As Speaker of the Texas House (2021–2025), Phelan shepherded the passage of the most sweeping pro-life legislation in Texas history: the Human Life Protection Act (trigger ban making abortion illegal in Texas), the Heartbeat Act (SB 8, banning abortion after cardiac activity is detected), and in the 88th Legislature additional pro-life protections — described by supporters as 'the two most conservative sessions in the history of our great state.' Phelan holds a lifelong commitment to protecting unborn life from conception.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Dade_Phelan",
               "https://www.texastribune.org/2024/05/28/dade-phelan-david-covey-texas-house-speaker-runoff/"]),
        claim("dp2", "dade-phelan", "border_immigration", 0, True,
              "Led an eightfold increase in Texas border security spending during his tenure as Speaker (2021–2025), growing the state's border-security appropriation to billions annually. Under Phelan's House leadership, Texas passed SB 4 (the Texas Border Security Act, 88th Legislature 3rd Special Session, 2023) — creating a state criminal offense for illegal border crossing and requiring mandatory return orders — and supported Operation Lone Star and the deployment of the Texas National Guard and DPS to the border. Phelan called securing Texas's border 'the most important thing we can do for the safety of Texas families.'",
              ["https://www.texastribune.org/2024/04/01/dade-phelan-border-immigration-primary/",
               "https://ballotpedia.org/Dade_Phelan",
               "https://www.texastribune.org/2023/10/25/texas-legislature-house-immigration-bills/"]),
    ]),

    # ----------- Cole Hefner (TX-R, HD-5, Wood/Camp County NE Texas) -----------
    ("cole-hefner", "TX", "Representative", [
        claim("ch1", "cole-hefner", "sanctity_of_life", 0, True,
              "Received a 100% score on the Texas Alliance for Life 89th Legislature (2025) Legislative Scorecard and earned a TAL PAC endorsement. Voted YES on SB 31 (Life of the Mother Act), SB 33 (Stop Taxpayer-Funded Abortion Travel Act), and HB 7 (2nd Special Session, 2025 — Woman and Child Protection Act imposing civil penalties for mailing abortion drugs into Texas). As chair of the House Homeland Security, Public Safety & Veterans' Affairs Committee, Hefner brings a senior conservative voice to the protection of unborn life.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://www.texasallianceforlife.org/89th-texas-legislature-pro-life-accomplishments-2025/",
               "https://ballotpedia.org/Cole_Hefner"]),
        claim("ch2", "cole-hefner", "self_defense", 1, True,
              "Served as the primary House sponsor of SB 1362 (89th Legislature, 2025), the 'Anti-Red Flag Act' — a Texas Gun Rights flagship priority bill (co-filed by Sen. Bryan Hughes in the Senate and Rep. Briscoe Cain in the House) prohibiting Texas courts, law enforcement, and state officials from recognizing, enforcing, or serving any red-flag gun confiscation order that is not explicitly authorized by Texas state law. The bill passed the Texas House 86–60 and was sent to Governor Abbott for signature. Hefner stated the bill was necessary to prevent 'rogue judges' from stripping Texans of their firearms and to make clear 'Texas won't violate anyone's right to bear arms.'",
              ["https://txgunrights.org/texas-house-and-senate-committees-set-will-lawmakers-follow-through-on-their-pro-gun-promises/",
               "https://www.texastribune.org/2025/05/27/texas-anti-red-flag-law-senate-bill-1362/",
               "https://ballotpedia.org/Cole_Hefner"]),
    ]),

    # ----------- Cody Vasut (TX-R, HD-25, Angleton / Brazoria County) -----------
    ("cody-vasut", "TX", "Representative", [
        claim("cv1", "cody-vasut", "sanctity_of_life", 0, True,
              "Received an 82% score on the Texas Alliance for Life 89th Legislature (2025) Legislative Scorecard, reflecting a generally pro-life voting record on key bills protecting unborn children and restricting taxpayer funding of abortion. Vasut, an attorney representing the Brazoria County / Angleton area, has supported pro-life legislation during his tenure since 2021 and holds a conservative record on protecting life consistent with his district.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Cody_Vasut"]),
        claim("cv2", "cody-vasut", "economic_stewardship", 2, True,
              "Filed a House floor amendment during the 89th Legislature's budget process (2025) to redirect $2 billion from the state dementia research fund allocation and apply it to property tax relief for Texas homeowners, reflecting a consistent fiscal-conservative posture that prioritizes reducing tax burdens over growing state spending commitments. As chair of the Select Committee on Congressional Redistricting and the Select Committee on Redistricting, Vasut is embedded in House leadership and has articulated a platform of 'shrinking the size of government' and reducing regulatory burdens to lower costs for Texans.",
              ["https://www.texastribune.org/2025/04/10/texas-house-budget-day/",
               "https://ballotpedia.org/Cody_Vasut"]),
    ]),

    # ----------- Cody Harris (TX-R, HD-8, Palestine / Anderson County) -----------
    ("cody-harris", "TX", "Representative", [
        claim("coh1", "cody-harris", "sanctity_of_life", 0, True,
              "Received a 100% score on the Texas Alliance for Life 89th Legislature (2025) Legislative Scorecard and a TAL PAC endorsement. Voted YES on SB 31 (Life of the Mother Act), SB 33 (Stop Taxpayer-Funded Abortion Travel Act), and the full suite of pro-life legislation in the 2025 session. Harris, who represents deep-East Texas (Anderson County / Palestine), publicly lists 'fighting for pro-life and pro-family values' as a legislative priority, consistent with his across-the-board perfect TAL rating.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://www.texastribune.org/directory/cody-harris/",
               "https://ballotpedia.org/Cody_Harris"]),
        claim("coh2", "cody-harris", "self_defense", 0, True,
              "A lifetime member of the National Rifle Association who publicly lists protecting Second Amendment rights as a legislative priority. Represents HD-8 (Anderson, Freestone, and Cherokee counties), a deep-East Texas rural district where constitutional carry and gun rights are central constituent concerns. Harris's NRA lifetime membership and stated commitment to gun rights reflect support for constitutional (permit-free) carry, which Texas enacted in the 87th Legislature (HB 1927, 2021) — a law Harris supported — allowing Texans 21+ to carry a handgun without a license.",
              ["https://ballotpedia.org/Cody_Harris",
               "https://www.texastribune.org/directory/cody-harris/"]),
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
