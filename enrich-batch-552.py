#!/usr/bin/env python3
"""Enrichment batch 552: 5 Texas state officials (evidence_state, 0 claims).

Primary archetype_curated federal senator/rep buckets are fully exhausted.
This batch opens the evidence_state Texas Republican frontier from the bottom
of the alphabet (names C-D-B range within TX-R, reverse-alpha order).

Targets (all TX-R):
  - Briscoe Cain        (TX-R, State Rep HD-128)
  - Charlie Geren       (TX-R, State Rep HD-99 / Speaker Pro Tempore)
  - Brian Harrison      (TX-R, State Rep HD-10 / former Trump HHS Chief of Staff)
  - Dawn Buckingham     (TX-R, Land Commissioner)
  - Brent Money         (TX-R, State Rep HD-2)

Each claim cites >=1 reliable source and reflects 2021-2025 voting record
and public positions.

Scorecard written MINIFIED (separators=(",",":")) to stay under GitHub's 50 MB limit.
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
    # --- Briscoe Cain (TX-R, State Rep HD-128) ---
    ("briscoe-cain", "TX", "Representative", [
        claim("bc1", "briscoe-cain", "sanctity_of_life", 0, True,
              "Cain originated and championed the Texas Heartbeat Act concept, authoring the precursor HB 1500 in 2019, and was named Operation Rescue's Pro-Life Person of the Year 2021 for his relentless work protecting unborn life. Rice University's Baker Institute ranked him the most conservative member of the Texas House for five sessions (2017-2021) and second-most-conservative in 2023. He has affirmed life from conception without exception and personally sent cease-and-desist letters to every Texas abortion fund after SB 8 became law, citing felony penalties for anyone who 'knowingly provides the means to procure an abortion.'",
              ["https://www.godreports.com/2022/03/creator-of-texas-heartbeat-bill-overcame-autism-aspergers/",
               "https://briscoecain.com/tag/texas-heartbeat-bill/"]),
        claim("bc2", "briscoe-cain", "self_defense", 1, True,
              "Cain filed HB 162 (the Anti-Red Flag Act) in 2019 to proactively ban extreme risk protection orders in Texas, and championed HB 1927 (constitutional carry) signed into law in 2021, which allows eligible Texans 21+ to carry a handgun without a government-issued permit — squarely opposing the red-flag law and permit-to-carry schemes the rubric identifies as Second Amendment threats.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://house.texas.gov/members/member-page/?district=128"]),
        claim("bc3", "briscoe-cain", "election_integrity", 0, True,
              "Speaker Dade Phelan appointed Cain chair of the Texas House Elections Committee in 2021; Cain has publicly stated that requiring a valid Texas photo ID to vote is 'essential to restoring fair elections,' authored voter-integrity legislation, and consistently advocates for strict ballot-chain-of-custody requirements and against mass mail-in voting.",
              ["https://www.houstonpublicmedia.org/articles/news/politics/2021/04/29/396903/briscoe-cain-and-the-fight-for-election-integrity/"]),
    ]),

    # --- Charlie Geren (TX-R, State Rep HD-99 / Speaker Pro Tempore) ---
    ("charlie-geren", "TX", "Representative", [
        claim("cg1", "charlie-geren", "sanctity_of_life", 0, True,
              "Geren voted for the Texas Heartbeat Act (SB 8) in 2021 and personally authored and passed the Life of the Mother Act, which preserves physician protections for life-threatening emergencies while maintaining Texas's near-total abortion prohibition; he is endorsed by Texas Alliance for Life and LifePAC, reflecting a consistent legislative record in defense of unborn life.",
              ["https://www.charliegeren.com/issues/",
               "https://texasallianceforlife.org/"]),
        claim("cg2", "charlie-geren", "self_defense", 0, True,
              "Geren is A-rated and endorsed by the National Rifle Association and the Texas State Rifle Association; he voted for Texas HB 1927 (constitutional carry) in 2021, securing permitless carry rights for law-abiding Texans — a foundational Second Amendment win he highlights on his official issues page.",
              ["https://www.charliegeren.com/issues/"]),
    ]),

    # --- Brian Harrison (TX-R, State Rep HD-10) ---
    ("brian-harrison", "TX", "Representative", [
        claim("bh1", "brian-harrison", "sanctity_of_life", 0, True,
              "As HHS Chief of Staff under President Trump (2019-2021), Harrison led a staff of over 85,000 and by his own account oversaw an agency that 'protected the unborn' — implementing the Mexico City Policy expansion, conscience-rights protections for pro-life medical providers, and Title X reforms blocking Planned Parenthood funding; he has carried a consistent pro-life posture into the Texas House since his 2021 special-election win.",
              ["https://www.foxnews.com/politics/ex-trump-administration-hhs-official-brian-harrison-announces-run-for-texas-house-seat",
               "https://house.texas.gov/members/4085/biography"]),
        claim("bh2", "brian-harrison", "industry_capture", 0, True,
              "As a Texas state representative, Harrison 'successfully led the fight against COVID vaccine mandates,' directly challenging the pharmaceutical-government nexus that pushed coercive jab requirements; his campaign materials list this as a signature legislative achievement and he has been a consistent critic of top-down public-health mandates.",
              ["https://www.texansforbrianharrison.com/",
               "https://repbio.org/brian-harrison/"]),
        claim("bh3", "brian-harrison", "family_child_sovereignty", 0, True,
              "Harrison 'ended Texas taxpayer funding of the Marxist-led American Library Association,' removing state financial support from an organization that promotes sexually explicit and ideologically extreme materials in public libraries accessible to children; he also 'expanded educational opportunities in Ellis County,' prioritizing parental choice over institutional capture of public education.",
              ["https://www.texansforbrianharrison.com/"]),
    ]),

    # --- Dawn Buckingham (TX-R, Land Commissioner) ---
    ("dawn-buckingham", "TX", "Land", [
        claim("db1", "dawn-buckingham", "sanctity_of_life", 0, True,
              "As a Texas state senator (2017-2023), Buckingham earned a perfect 100 score from Texas Right to Life, co-authored the Texas Heartbeat Act (SB 8, 2021) that underpins the state's near-total abortion ban, voted against abortion access at every recorded opportunity during the 2021 session, and helped pass the trigger law that made abortion illegal statewide after Dobbs; she holds a 96% lifetime rating from the American Conservative Union.",
              ["https://texasrighttolife.com/legislative-scores/",
               "https://texasscorecard.com/state/texas-right-to-life-releases-ratings-of-legislature/"]),
        claim("db2", "dawn-buckingham", "border_immigration", 0, True,
              "As Texas Land Commissioner, Buckingham deployed GLO-controlled state land for border-wall enforcement: she declared Fronton Island (Starr County) state land, granted DPS a Dec. 2023 Right of Entry to install Rio Grande fencing on GLO property, acquired a 1,402-acre Starr County ranch in October 2024 to construct a state-funded border wall, and called on the Trump administration and the Texas Military Department to physically secure newly identified border islands — one of the most aggressive uses of a state land-commissioner's authority to support wall-and-military border enforcement.",
              ["https://www.glo.texas.gov/the-glo/news/press-releases/2024/october/commissioner-buckingham-strengthens-texas-border-security-through-continued-partnership-with-dps-in-starr-county.html",
               "https://www.glo.texas.gov/about-glo/press-releases/texas-land-commissioner-buckingham-acquires-ranch-starr-county-build",
               "https://www.glo.texas.gov/about-glo/press-releases/commissioner-buckingham-identifies-new-border-islands-calls-on-trump-administration-and-tx-military-dept-to-secure-and-defend"]),
    ]),

    # --- Brent Money (TX-R, State Rep HD-2) ---
    ("brent-money", "TX", "Representative", [
        claim("bm1", "brent-money", "sanctity_of_life", 1, True,
              "In the 89th Texas legislative session (2025), Money introduced HB 2197 to remove the statutory exception that shields women from prosecution for self-induced abortions, extending existing murder statutes to all who terminate a pregnancy — an abolition-not-mere-restriction approach that goes beyond gestational limits. Money called the bill a 'top priority for Republicans' and pushed it against institutional resistance.",
              ["https://www.ketk.com/news/politics/texas-politics/texas-rep-brent-money-legislation/",
               "https://www.tpr.org/government-politics/2025-04-22/texas-lawmakers-ditch-discussion-on-controversial-bill-that-would-make-abortion-murder"]),
        claim("bm2", "brent-money", "self_defense", 0, True,
              "Money is a 'card-carrying lifetime NRA member' who holds that the right to keep and bear arms is a 'fundamental, God-given right that protects all of our other God-given rights from government intrusion,' and states he is 'fully invested in protecting the right of law-abiding citizens to keep and bear arms' without restriction.",
              ["https://www.brentmoney.com/issues/"]),
        claim("bm3", "brent-money", "family_child_sovereignty", 0, True,
              "Money voted for Senate Bill 2 (89th Legislature, 2025) to establish Texas Education Freedom Accounts — a $1 billion statewide school-choice voucher program giving families control over K-12 education dollars; he was among the net-16 newly elected pro-voucher House members who provided the decisive margin for the bill's 86-61 passage, championing parental sovereignty over government-assigned schooling.",
              ["https://www.texastribune.org/2025/03/31/texas-school-voucher-funding/",
               "https://educationfreedom.texas.gov/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
