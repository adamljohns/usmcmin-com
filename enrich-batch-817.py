#!/usr/bin/env python3
"""Enrichment batch 817: 5 Utah State Representatives (archetype_party_default → evidence_curated).

Targets from the bottom of the unenriched archetype_party_default bucket (WY-VA states exhausted;
UT is the next available state working backward from the alphabet):
David Shallenberger (UT-58), Colin W. Jack (UT-73), Clinton Okerlund (UT-42),
Christine F. Watkins (UT-67), Cheryl K. Acton (UT-38).
All are Utah House Republicans with 0 prior claims.
Research covers 2023-2026 legislative sessions with verifiable votes and sponsorships.
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


TARGETS = [
    # ---------- David Shallenberger (UT-58, R, first term Jan 2025) ----------
    ("david-shallenberger", "UT", "Representative", [
        claim("ds1", "david-shallenberger", "biblical_marriage", 2, True,
              "Primary sponsor of HB 404 (2026 General Session) — Sex-Designated Housing Amendments — amending Utah's Fair Housing Act to permit landlords of shared-accommodation housing (dorms, boarding houses) to designate units as single-sex based on biological sex at birth. Passed the House 50–20 on Feb. 10, 2026; signed by Governor Cox on March 23, 2026.",
              ["https://legiscan.com/UT/bill/HB0404/2026",
               "https://trackbill.com/bill/utah-house-bill-404-sex-designated-housing-amendments/2793738/"]),
        claim("ds2", "david-shallenberger", "election_integrity", 0, True,
              "Voted YES on HB 300 (2025 General Session) — Amendments to Election Law — requiring voters to include the last four digits of a government-issued ID on mail-in ballot envelopes starting in 2026, phasing out Utah's automatic vote-by-mail system by 2029 (voters must opt in), and mandating ballots be received by 8 p.m. on election night. Passed the House 56–15; signed by Governor Cox on March 26, 2025.",
              ["https://utahnewsdispatch.com/2025/03/06/utah-legislature-approves-bill-require-voter-id-phase-out-automatic-voting-by-mail-by-2029/"]),
        claim("ds3", "david-shallenberger", "family_child_sovereignty", 0, True,
              "Voted YES on HB 174 (2026 General Session) — Sex Characteristic Change Treatment Amendments — permanently banning puberty blockers and cross-sex hormones for transgender minors in Utah (converting the prior moratorium into a permanent prohibition). Passed the House 54–15 on Feb. 5, 2026; signed by Governor Cox.",
              ["https://utahnewsdispatch.com/2026/02/05/utah-house-passes-ban-transgender-treatments-for-minors/"]),
    ]),

    # ---------- Colin W. Jack (UT-73, R, chair Public Utilities & Energy Committee) ----------
    ("colin-w-jack", "UT", "Representative", [
        claim("cj1", "colin-w-jack", "refuse_federal_overreach", 0, True,
              "Primary sponsor of HB 374 (2024 General Session) — State Energy Policy Amendments — rewrote Utah's energy policy statute to explicitly resist EPA and federal overreach on energy permitting, prevent federally-incentivized early closure of coal plants, and direct state funds toward legal challenges of 'unreasonable' federal environmental regulations. Passed the House 63–9; signed by Governor Cox on March 21, 2024.",
              ["https://utahnewsdispatch.com/2024/02/20/bills-utah-energy-policy-coal/",
               "https://le.utah.gov/~2024/bills/static/HB0374.html"]),
        claim("cj2", "colin-w-jack", "self_defense", 0, True,
              "Voted YES on HB 219 (2023 General Session) — Federal Firearm Enforcement Limitation Act — establishing Utah as a Second Amendment Sanctuary state, prohibiting state and local agencies from spending public funds to assist federal gun regulations not mirrored in state law. Passed 60–3; signed into law. Publicly states: 'The right to keep and bear arms is protected in both the US Constitution and the Utah Constitution and will never be infringed by me.' Lifetime Member of the NRA.",
              ["https://www.stgeorgeutah.com/news/government-news/declaring-utah-a-2nd-amendment-sanctuary-state-among-these-gun-related-bills-moving-through-legislature/article_e1230bd4-74a1-5e38-bdc6-c739c72d5baf.html",
               "https://www.colinwjack.com/issues"]),
        claim("cj3", "colin-w-jack", "public_justice", 0, True,
              "Primary sponsor of HB 474 (2024 General Session) — Criminal Justice Amendments — strengthening Utah's pretrial detention framework: removed unsecured bond as a release option, authorized judges to weigh charge severity in pretrial decisions, created a new crime for violating pretrial release conditions, allowed sheriffs to detain probation/parole violators up to 24 hours, and stiffened distribution penalties for fentanyl, methamphetamine, heroin, and cocaine.",
              ["https://le.utah.gov/~2024/bills/hbillhtm/HB0474.htm"]),
    ]),

    # ---------- Clinton Okerlund (UT-42, R, first term Jan 2025, CFO background) ----------
    ("clinton-okerlund", "UT", "Representative", [
        claim("co1", "clinton-okerlund", "sanctity_of_life", 0, True,
              "Explicit pro-life campaign pledge: 'I firmly believe that life at every stage is precious and worth defending and will always vote Pro-Life and for policies that provide resources for adoption services and for the health and wellness of new mothers and babies.' (electclint.com/priorities, 2024 campaign).",
              ["https://www.electclint.com/priorities",
               "https://www.ballotready.org/people/clint-okerlund"],
              kind="statement"),
        claim("co2", "clinton-okerlund", "economic_stewardship", 2, True,
              "Chief sponsor of HB 490 (2025 General Session) — State Parks Modifications — requiring the Utah Division of State Parks to sustain operations primarily through fee revenue rather than general-fund appropriations, reducing reliance on tax subsidies and moving parks toward fiscal self-sufficiency. Passed the Utah Senate on March 6, 2025.",
              ["https://le.utah.gov/~2025/bills/static/HB0490.html"]),
        claim("co3", "clinton-okerlund", "public_justice", 0, True,
              "Chief sponsor of HB 341 (2026 General Session) — Animal Fighting Penalties — elevating cockfighting and animal fighting offenses from misdemeanors to felony-level charges, targeting organizers, promoters, and profiteers. Passed the Utah House 64–8 on Feb. 26, 2026.",
              ["https://fastdemocracy.com/bill-search/ut/2026/bills/UTB00014426/"]),
    ]),

    # ---------- Christine F. Watkins (UT-67, R, Carbon County; not seeking reelection 2026) ----------
    ("christine-f-watkins", "UT", "Representative", [
        claim("cw1", "christine-f-watkins", "biblical_marriage", 2, True,
              "Voted YES on HB 257 (2024 General Session) — Sex-based Designations for Privacy, Anti-bullying, and Women's Opportunities — barring individuals from using sex-designated bathrooms or locker rooms that do not match their biological sex. Made a public floor statement in support. Passed the House 52–17; signed by Governor Cox on Jan. 30, 2024.",
              ["https://www.deseret.com/2024/1/19/24044529/transgender-bathroom-bill-passes-utah-house/"]),
        claim("cw2", "christine-f-watkins", "refuse_federal_overreach", 0, True,
              "Chief sponsor of HB 410 (2024 General Session) — Utah San Rafael State Energy Lab — appropriating $2 million to purchase and $1 million annually to operate a state-controlled energy research lab in Emery County studying nuclear, solar, coal, and wind technologies. Created explicitly to resist federal EPA pressure on fossil fuels and protect rural Carbon/Emery County energy-sector jobs. Signed into law March 21, 2024.",
              ["https://utahnewsdispatch.com/2024/02/05/utah-may-buy-emery-county-energy-research-lab/"]),
        claim("cw3", "christine-f-watkins", "public_justice", 0, True,
              "Chief sponsor of HB 83 (2025 General Session) — Child Welfare Modifications — introduced in direct response to children's deaths where DCFS had been alerted but lacked authority to act quickly. The bill would have authorized DCFS to obtain warrants to enter a home in urgent situations and restricted withdrawal of children from school for homeschooling within three years of an active abuse investigation.",
              ["https://ksltv.com/local-news/lawmaker-demands-answers-from-dcfs-proposes-new-bill-to-help/666166/"]),
    ]),

    # ---------- Cheryl K. Acton (UT-38, R, West Jordan; not seeking reelection 2026) ----------
    ("cheryl-k-acton", "UT", "Representative", [
        claim("ca1", "cheryl-k-acton", "sanctity_of_life", 0, True,
              "Chief sponsor of HB 136 (2019 General Session) — Abortion Amendments — banning abortion after 18 weeks gestation. Blocked by a federal court until Dobbs (2022), after which Planned Parenthood's lawsuit was dismissed and the law became operative. One of the most consequential pro-life bills passed by the Utah legislature in recent decades.",
              ["https://www.ksl.com/article/46517954/utah-governor-signs-into-law-bill-to-ban-abortion-after-18-weeks"]),
        claim("ca2", "cheryl-k-acton", "biblical_marriage", 2, True,
              "Voted YES on HB 174 (2026 General Session) — Sex Characteristic Change Treatment Amendments — permanently banning puberty blockers and cross-sex hormones for transgender minors. Floor statement: 'I have a desire to protect children from irreversible harms. That's what this bill is about.' Passed 54–15 in the House; signed by Governor Cox on March 18, 2026.",
              ["https://utahnewsdispatch.com/2026/01/28/utah-bill-would-ban-transgender-care-for-minors/",
               "https://www.qsaltlake.com/news/2026/02/11/utah-hb174-passes-house/"]),
        claim("ca3", "cheryl-k-acton", "family_child_sovereignty", 0, True,
              "Chief sponsor of HB 303 (2025 General Session) — Public School Directory Sharing Amendments — requiring annual written parental consent before local education agencies may share student directory information with another school or LEA, and limiting data sharing to schools within a 50-mile radius. Passed the House 40–33.",
              ["https://legiscan.com/UT/research/HB0303/2025",
               "https://pf.utleg.gov/public-web/sessions/2025GS/fiscal-notes/HB0303.fn.pdf"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
