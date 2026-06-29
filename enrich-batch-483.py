#!/usr/bin/env python3
"""Enrichment batch 483: 5 Utah Republican state senators with 0 claims.

Targets archetype_party_default senators from UT — next bottom-of-alphabet
state after WY/WV/WI/WA/VA were exhausted. Senators: Wayne Harper, Todd Weiler,
Scott Sandall, Ronald Winterton, Mike McKell.
Claims drawn from 2023-2026 Utah legislative sessions, verified via
le.utah.gov, ksl.com, deseret.com, utahnewsdispatch.com, senate.utah.gov.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # -------- Wayne Harper (UT-R, State Senator, Senate President Pro Tempore) --------
    ("wayne-harper", "UT", "Senator", [
        claim("wh1", "wayne-harper", "election_integrity", 0, True,
              "Senate-sponsored SB164 (2025 General Session, 'Modifications to Election Law'), enrolled and signed into law. The bill requires poll watchers to observe the ballot-signature verification process for candidate petitions, mandates an audit of that verification, and requires election clerks to check additional signatures beyond the target threshold — strengthening ballot-integrity procedures.",
              ["https://le.utah.gov/Session/2025/bills/enrolled/SB0164.pdf",
               "https://trackbill.com/bill/utah-senate-bill-164-modifications-to-election-law/2631399/"]),
        claim("wh2", "wayne-harper", "economic_stewardship", 2, True,
              "A consistent champion of income tax cuts; co-sponsored the Utah Senate's $160M+ income tax reduction package and has supported limited-government fiscal restraint throughout his tenure. Elected Senate President Pro Tempore in January 2025.",
              ["https://senate.utah.gov/utah-senate-passes-more-than-160-million-income-tax-cut-for-utahns/"]),
    ]),

    # -------- Todd Weiler (UT-R, State Senator, District 8) --------
    ("todd-weiler", "UT", "Senator", [
        claim("tw1", "todd-weiler", "biblical_marriage", 2, True,
              "Sponsored SB100 (2023 General Session, 'School Gender Identity Policies'), signed by Governor Cox on February 16, 2023. The law requires schools to obtain parental consent before changing a student's official records to reflect a different name or pronoun related to gender identity, and prohibits schools from withholding that information from parents — rejecting gender-ideology directives that override parental authority and biological reality.",
              ["https://le.utah.gov/~2023/bills/static/SB0100.html",
               "https://www.kuer.org/politics-government/2023-01-31/heres-what-utah-sen-todd-weilers-bill-on-gender-identity-in-schools-actually-does"]),
        claim("tw2", "todd-weiler", "family_child_sovereignty", 0, True,
              "Authored Utah's entire legislative suite protecting children's digital environments: SB287 (2023, porn age-verification — signed into law), SB104 (2024, mandatory device content filters for minors), and SB142 (2025, 'App Store Accountability Act' — first-in-the-nation law requiring Apple and Google to verify user ages before app downloads and mandating parental consent for minor accounts, with $1,000 per-violation civil penalties, effective May 2026).",
              ["https://le.utah.gov/Session/2025/bills/enrolled/SB0142.pdf",
               "https://www.ksl.com/article/51284592/how-will-big-tech-comply-with-utahs-first-in-the-nation-child-protection-laws"]),
    ]),

    # -------- Scott Sandall (UT-R, State Senator, District 1) --------
    ("scott-sandall", "UT", "Senator", [
        claim("ss1", "scott-sandall", "self_defense", 0, True,
              "Senate-sponsored and championed HB133 (2025 General Session, 'Dangerous Weapons Amendments'), a firearms bill to remove criminal penalties for carrying loaded rifles or shotguns in a vehicle and clarify constitutional carry rights statewide; it passed the House before dying in a Senate committee. Sandall publicly stated his district is 'a constitutional carry, Second Amendment group, that wants to be able to freely carry.'",
              ["https://utahnewsdispatch.com/2025/01/27/changes-to-utah-gun-laws-gain-steam-in-legislature-including-letting-18-year-olds-open-carry/",
               "https://le.utah.gov/Session/2025/bills/introduced/HB0133.pdf"]),
        claim("ss2", "scott-sandall", "refuse_federal_overreach", 0, True,
              "Senate-sponsored HB421 (2025, 'Grazing Amendments'), requiring the Utah Division of Wildlife Resources to obtain local land use authority approval before acquiring grazing permits — placing a check on state and federal agency power over ranchers. A 3rd-generation farmer/rancher, Sandall consistently champions local control over land, water, and natural resource decisions against federal encroachment.",
              ["https://www.utahfarmbureau.org/Article/Five-Key-Bills-from-the-2025-Utah-Legislative-Session",
               "https://www.votescottsandall.com/"]),
    ]),

    # -------- Ronald Winterton (UT-R, State Senator, District 20) --------
    ("ronald-winterton", "UT", "Senator", [
        claim("rw1", "ronald-winterton", "refuse_federal_overreach", 0, True,
              "Chairs the Utah Federalism Commission, the legislature's dedicated body for promoting states' rights against federal overreach. Senate-sponsored SB149 (2025, 'Natural Resources Modifications'), reorganizing Utah's Public Lands Policy Coordinating Office that asserts RS 2477 highway rights and resists federal land-management encroachment — the bill passed the Senate 25–0 and advanced through the House.",
              ["https://fastdemocracy.com/bill-search/ut/2025/bills/UTB00012958/",
               "https://www.kpcw.org/wasatch-county/2022-03-17/senator-ron-winterton-runs-for-reelection"]),
        claim("rw2", "ronald-winterton", "economic_stewardship", 4, True,
              "Senate-sponsored HB201 (2025, 'Energy Resource Amendments'), signed into law effective May 7, 2025, modifying Public Service Commission evaluation of integrated resource plans to add definitions for baseload capacity — supporting reliable, affordable conventional energy over ESG-driven variable-only mandates. Winterton's stated governing priority is 'ensuring reliable, low-cost energy' for Utah families.",
              ["https://le.utah.gov/Session/2025/bills/enrolled/HB0201.pdf",
               "https://legiscan.com/UT/bill/HB0201/2025"]),
    ]),

    # -------- Mike McKell (UT-R, State Senator, District 25, Majority Assistant Whip) --------
    ("mike-mckell", "UT", "Senator", [
        claim("mm1", "mike-mckell", "family_child_sovereignty", 0, True,
              "Primary Senate sponsor of SB152 (2023, 'Social Media Regulation Act'), signed March 23, 2023 — making Utah the first state to require social media companies to verify ages of all users, mandate parental consent for minor account creation, give parents full account access and screen-time control, and restrict direct messaging to minor accounts.",
              ["https://www.ksl.com/article/50606907/social-media-restrictions-for-teens-signed-into-law-by-utah-governor",
               "https://senate.utah.gov/utah-leads-the-way-with-new-social-media-legislation/"]),
        claim("mm2", "mike-mckell", "public_justice", 0, True,
              "Senate co-sponsor of HB272 'Om's Law' (2024, 'Child Custody Proceedings Amendments'), signed April 10, 2024. The law directs family court judges to prioritize child safety in custody decisions, requires consideration of domestic violence and credible abuse allegations, and mandates specialized training for judges and court personnel — named for Om Moses Gandhi, a 16-year-old killed by his father in a custody dispute.",
              ["https://www.deseret.com/2024/1/31/24055593/domestic-violence-bills-utah-legislature/",
               "https://ksltv.com/ksl-investigates/utah-lawmakers-pass-oms-law-focused-on-child-safety-in-custody-decisions/627083/"]),
        claim("mm3", "mike-mckell", "election_integrity", 0, True,
              "Primary sponsor of SB194 (2026 General Session, 'Election Modifications'), which passed the legislature requiring county clerks to verify both voter signature AND last four digits of ID number on mail-in ballots — a dual-verification election-security reform strengthening mail-ballot integrity.",
              ["https://www.deseret.com/politics/2026/03/06/utah-legislature-reforms-vote-by-mail-but-rejects-election-oversight-overhaul/",
               "https://www.ksl.com/article/51438782/third-party-lawmakers-recent-election-prompts-new-bill-in-utah-legislature"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
