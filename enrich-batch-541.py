#!/usr/bin/env python3
"""Enrichment batch 541: 10 new claims across 5 Texas Republican state representatives.

Continuing the TX evidence_state pool (D-names, reverse-alpha). All archetype_curated
federal senators and representatives have been fully enriched; this batch picks up
where batch 540 left off in the evidence_state TX R member pool.

Targets (reverse alpha by name within TX):
  Drew Darby          (HD-72, San Angelo / West Texas — veteran member since 2007)
  Don McLaughlin      (HD-80, Uvalde / SW Texas border — freshman Jan 2025)
  Denise Villalobos   (HD-34, Corpus Christi / Nueces County — freshman Jan 2025)
  David Spiller       (HD-68, Jacksboro / North Texas — authored TX SB 4 / HB 4)
  David Lowe          (HD-91, Tarrant County / Fort Worth — freshman Jan 2025)

Two distinct rubric-category claims per target. Sources: texasallianceforlife.org,
txgunrights.org, ballotpedia.org, texastribune.org, legiscan.com, gov.texas.gov,
keranews.org, kut.org.

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
    # -------------- Drew Darby (TX-R, HD-72, San Angelo) --------------
    ("drew-darby", "TX", "Representative", [
        claim("dd1", "drew-darby", "sanctity_of_life", 0, True,
              "Earned a perfect 100% on the Texas Alliance for Life 89th Legislature (2025) scorecard, voting YES on SB 31 (Life of the Mother Act, clarifying that medically necessary care for pregnant women is permitted) and SB 33 (Stop Taxpayer-Funded Abortion Travel Act). His across-the-board pro-life record affirms protection of the unborn from conception.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Drew_Darby"]),
        claim("dd2", "drew-darby", "family_child_sovereignty", 0, True,
              "Voted YES on SB 2 (89th Legislature, April 2025), the Texas Education Savings Accounts Act creating a $1 billion program allowing families to use state funds for private school tuition, homeschooling, and educational materials. The bill passed the Texas House 85–63. Though Darby had opposed similar voucher proposals in 2023, he voted yes in 2025 after securing amendment protections, supporting the principle of parental control over children's education.",
              ["https://www.texastribune.org/2025/04/17/greg-abbott-school-vouchers-republicans-hardball/",
               "https://www.texastribune.org/2025/06/03/texas-san-angelo-rural-lawmakers-legislative-session-impact",
               "https://ballotpedia.org/Drew_Darby"]),
    ]),

    # ----------- Don McLaughlin (TX-R, HD-80, Uvalde / border district) -----------
    ("don-mclaughlin", "TX", "Representative", [
        claim("dm1", "don-mclaughlin", "sanctity_of_life", 0, True,
              "Received a 96% score on the Texas Alliance for Life 2025 Legislative Scorecard (89th Legislature), earning a formal TAL PAC endorsement. His near-perfect pro-life record covers votes on SB 31 (Life of the Mother Act) and SB 33 (ban on taxpayer-funded abortion travel), reflecting consistent protection of unborn life.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Don_McLaughlin"]),
        claim("dm2", "don-mclaughlin", "self_defense", 1, True,
              "Received the Texas Gun Rights (TXGR) endorsement in the November 2024 general election after completing their candidate survey. Explicitly opposes raising the legal purchase age for semi-automatic rifles from 18 to 21 — a position he maintained even as the representative from Uvalde, site of the 2022 Robb Elementary shooting. TXGR listed him among House Homeland Security committee members who 'vowed to fight for the Second Amendment,' opposing red-flag confiscation laws and new firearm restrictions.",
              ["https://txgunrights.org/texas-gun-rights-voter-guide-nov-5th-general-election/",
               "https://txgunrights.org/texas-house-and-senate-committees-set-will-lawmakers-follow-through-on-their-pro-gun-promises/",
               "https://ballotpedia.org/Don_McLaughlin"]),
    ]),

    # ----------- Denise Villalobos (TX-R, HD-34, Corpus Christi) -----------
    ("denise-villalobos", "TX", "Representative", [
        claim("dv1", "denise-villalobos", "sanctity_of_life", 0, True,
              "Earned a perfect 100% on the Texas Alliance for Life 89th Legislature (2025) scorecard and received their 2024 general-election endorsement. Voted YES on SB 31 (Life of the Mother Act), SB 33 (Stop Taxpayer-Funded Abortion Travel Act), and HB 7 (2nd Special Session, Woman and Child Protection Act — establishing civil penalties for abortion providers who illegally mail abortion-inducing drugs into Texas).",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://www.texasallianceforlife.org/89th-texas-legislature-pro-life-accomplishments-2025/",
               "https://ballotpedia.org/Denise_Villalobos"]),
        claim("dv2", "denise-villalobos", "public_justice", 0, True,
              "Primary House author of HB 2306 (89th Legislature, 2025), which eliminates parole eligibility for persons convicted of human trafficking when the victim is a child or a disabled individual. The bill passed the Texas House 140–0 (unanimous, bipartisan) and was signed into law by Governor Abbott on August 21, 2025, effective September 1, 2025. Prior to this law, convicted child traffickers could be paroled after serving as little as 12 years.",
              ["https://gov.texas.gov/news/post/governor-abbott-signs-anti-human-trafficking-bills-into-law-at-governors-mansion",
               "https://legiscan.com/TX/bill/HB2306/2025",
               "https://ballotpedia.org/Denise_Villalobos"]),
    ]),

    # ----------- David Spiller (TX-R, HD-68, Jacksboro / North Texas) -----------
    ("david-spiller", "TX", "Representative", [
        claim("ds1", "david-spiller", "border_immigration", 1, True,
              "Primary House author of HB 4 (88th Legislature, 3rd Special Session, October 2023), creating a Texas state criminal offense for improper entry from a foreign nation: a Class B misdemeanor for a first crossing, escalating to a state jail felony for repeat offenders and a second-degree felony (2–20 years) for those who refuse a lawful order to return. The bill passed the House 84–60 and its Senate companion SB 4 was signed into law; the 5th U.S. Circuit Court of Appeals lifted an injunction and allowed enforcement in 2026.",
              ["https://legiscan.com/TX/bill/HB4/2023/X3",
               "https://www.keranews.org/2023-10-26/texas-house-approves-sweeping-border-enforcement-bill-after-hours-of-intense-debate",
               "https://www.texastribune.org/2023/10/25/texas-legislature-house-immigration-bills/"]),
        claim("ds2", "david-spiller", "election_integrity", 0, True,
              "Filed HB 52 (88th Legislature, 2023) to restore felony-level penalties for illegal voting and impose civil penalties for Election Code violations, stating the higher penalties were needed 'to ensure that we have safe and secure elections.' The companion Senate bill (SB 2) passed the full Legislature and was signed into law, making illegal voting a second-degree felony in Texas effective September 1, 2023.",
              ["https://legiscan.com/TX/text/HB52/id/2612881",
               "https://www.texastribune.org/2023/04/27/texas-house-illegal-voting-felony-penalty/"]),
    ]),

    # ----------- David Lowe (TX-R, HD-91, Tarrant County / Fort Worth) -----------
    ("david-lowe", "TX", "Representative", [
        claim("dl1", "david-lowe", "self_defense", 1, True,
              "Received the Texas Gun Rights (TXGR) endorsement in the 2024 general election. Explicitly opposes red-flag laws, calling them 'the gateway to unconstitutional gun confiscation by the government,' and pledged after his election to 'help push the legislature to pass a Constitutional amendment to protect Texans from Red Flag laws.' Also advocates eliminating the License to Carry program entirely, stating 'you shouldn't need a license for your gun rights.'",
              ["https://txgunrights.org/breaking-down-gun-rights-victories-in-the-2024-republican-primary/",
               "https://ballotpedia.org/David_Lowe_(Texas)"]),
        claim("dl2", "david-lowe", "border_immigration", 2, True,
              "A named cosponsor of SB 8 (89th Legislature, 2025), which mandates that Texas county sheriffs in counties of 100,000+ residents enter into 287(g) agreements with U.S. Immigration and Customs Enforcement — deputizing local law enforcement to identify and apprehend undocumented immigrants and requiring counties to fund compliance through a state grant program. The bill was signed into law and took effect in late 2025.",
              ["https://www.texastribune.org/2025/04/01/texas-senate-bill-8-vote-287g-agreements-sheriffs-ice/",
               "https://www.texastribune.org/2025/06/01/texas-immigration-enforcement-sheriffs-287g-bill/",
               "https://capitol.texas.gov/billlookup/History.aspx?LegSess=89R&Bill=SB8"]),
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
