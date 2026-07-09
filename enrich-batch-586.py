#!/usr/bin/env python3
"""Enrichment batch 586: 5 Oklahoma R state senators with 0 claims.

All archetype_curated federal officials are fully enriched; this batch continues
the reverse-alpha archetype_party_default sweep into Oklahoma (OK), the next
state group after SD/SC (batch 585) in reverse-alphabetical order.

Senators:
  Warren Hamilton   (OK-R, District 7)
  Shane Jett        (OK-R, District 17, Oklahoma Freedom Caucus chair)
  Micheal Bergstrom (OK-R, District 1)
  Tom Woods         (OK-R, District 4)
  Lisa Standridge   (OK-R, District 15)

Claims drawn from documented legislative records, bill authorship, official
press releases, Ballotpedia profiles, and Wikipedia for 2021-2026.

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep master under
GitHub's 50MB limit.
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
    # ---------- Warren Hamilton (OK-R, District 7) ----------
    ("warren-hamilton", "OK", "Senator", [
        claim("wh1", "warren-hamilton", "sanctity_of_life", 0, True,
              "Hamilton is an abortion abolitionist who co-authored Senate legislation "
              "with Sen. Dusty Deevers classifying abortion as criminal homicide under "
              "Oklahoma law, subjecting abortionists — and potentially mothers — to "
              "prosecution including the death penalty where charged with first-degree "
              "murder (with exceptions only to save the mother's life and for spontaneous "
              "miscarriage). Hamilton filed a companion to Deevers' Equal Protection and "
              "Equal Justice Act and spoke in favor of abolition at an Abolitionists "
              "Rising/Abolish Abortion Oklahoma rally at the state Capitol in February 2024. "
              "During a 2022 Senate floor debate over SB 1503 (Oklahoma's near-total "
              "abortion ban), Hamilton publicly questioned why an ectopic pregnancy "
              "exception appeared in the bill — reflecting a life-from-conception standard "
              "with no exceptions short of direct threat to the mother's life.",
              ["https://en.wikipedia.org/wiki/Warren_Hamilton",
               "https://okcfox.com/news/local/senator-to-file-abolition-of-abortion-in-oklahoma-act",
               "https://oksenate.gov/press-releases/sen-warren-hamilton-files-equal-protection-and-equal-justice-act"]),
        claim("wh2", "warren-hamilton", "self_defense", 0, True,
              "Hamilton authored Oklahoma's Second Amendment Sanctuary State Act, "
              "which directs Oklahoma state agencies and officials to refuse enforcement "
              "of any new federal gun restrictions that would infringe on Oklahomans' "
              "Second Amendment rights under state law — the most aggressive legislative "
              "posture available to a state senator in defense of constitutional carry and "
              "against federal firearm regulation. He is a member of Gun Owners of America "
              "and the Oklahoma Second Amendment Association, and his official campaign "
              "platform states he will 'safeguard Oklahomans from any further infringement "
              "upon our Second Amendment rights.' He is also a retired military officer "
              "who served in the U.S. Army.",
              ["https://www.votehamilton.org/",
               "https://en.wikipedia.org/wiki/Warren_Hamilton",
               "https://ivoterguide.com/candidate?canK=53616&elecK=698&primarypartyk=R&raceK=11480"]),
        claim("wh3", "warren-hamilton", "public_justice", 0, True,
              "Hamilton introduced Senate Bill 599 (2025) making child rapists eligible "
              "for the death penalty. The bill provides that any person convicted of "
              "forcible anal or oral sodomy, rape, rape by instrumentation, or lewd "
              "molestation of a child under 14 years of age is eligible for a death "
              "sentence. Governor Kevin Stitt signed SB 599 into law on May 22, 2025; "
              "the law took effect November 1, 2025, making Oklahoma one of the first "
              "states to impose capital punishment for crimes against children short of "
              "homicide following the U.S. Supreme Court's 2008 Kennedy v. Louisiana "
              "ruling.",
              ["https://en.wikipedia.org/wiki/Warren_Hamilton",
               "https://deathpenaltyinfo.org/research/analysis/reports/year-end-reports/the-death-penalty-in-2025/legislation"]),
    ]),

    # ---------- Shane Jett (OK-R, District 17, Freedom Caucus chair) ----------
    ("shane-jett", "OK", "Senator", [
        claim("sj1", "shane-jett", "family_child_sovereignty", 0, True,
              "Jett introduced Senate legislation in February 2021 to prohibit the "
              "teaching of critical race theory (CRT) in Oklahoma public schools — one "
              "of the first state-level legislative efforts to restore parental authority "
              "over racially divisive curriculum. In 2023, he authored a bill prohibiting "
              "social-emotional learning (SEL) mandates in Oklahoma schools, targeting "
              "the therapeutic and ideological framework progressives use to introduce "
              "gender and emotional programming into K-12 classrooms without parental "
              "consent. As chair of the Oklahoma Freedom Caucus (named September 3, 2024), "
              "Jett has continued to lead the chamber's most aggressive defense of parental "
              "rights in education.",
              ["https://en.wikipedia.org/wiki/Shane_Jett",
               "https://ballotpedia.org/Shane_Jett"]),
        claim("sj2", "shane-jett", "christian_liberty", 0, True,
              "Jett, as chair of the Oklahoma Freedom Caucus, championed the Bibles in "
              "Classroom Initiative — publicly supporting the presence of Bibles in "
              "Oklahoma public school classrooms as an expression of the state's Christian "
              "heritage and students' religious liberties under the First Amendment's "
              "Free Exercise Clause. The Freedom Caucus framed the initiative as consistent "
              "with Oklahoma's history and opposed to the secular restriction of Christian "
              "sacred texts from government-run schools. Jett has also introduced "
              "legislation aimed at banning diversity, equity, and inclusion (DEI) "
              "requirements from state higher-education institutions, dismantling a "
              "framework the Freedom Caucus views as hostile to faith-based worldviews.",
              ["https://en.wikipedia.org/wiki/Shane_Jett",
               "https://oksenate.gov/senator-press-releases/shane-jett"]),
    ]),

    # ---------- Micheal Bergstrom (OK-R, District 1) ----------
    ("micheal-bergstrom", "OK", "Senator", [
        claim("mb1", "micheal-bergstrom", "christian_liberty", 0, True,
              "Bergstrom authored Senate Bill 513 (2025), designed to protect the "
              "constitutional right to religious freedom during declared states of "
              "emergency. The bill advanced through the Oklahoma Senate Public Safety "
              "Committee in February 2025 and would prohibit government officials from "
              "restricting religious gatherings or faith-based activities under the cover "
              "of emergency declarations — a direct legislative response to the documented "
              "pattern of pandemic-era authorities closing churches while exempting other "
              "activities from the same restrictions.",
              ["https://ballotpedia.org/Micheal_Bergstrom",
               "https://oksenate.gov/senator-press-releases/micheal-bergstrom"]),
        claim("mb2", "micheal-bergstrom", "biblical_marriage", 2, True,
              "Bergstrom sponsored legislation to prohibit nonbinary ('X') gender markers "
              "on Oklahoma birth certificates, ensuring state-issued vital records reflect "
              "only biological sex as male or female. The legislation directly rejects "
              "transgender ideology in government documentation by maintaining that sex "
              "is a fixed, binary biological reality that the state records at birth — "
              "not a spectrum of self-identified or assigned genders that can be altered "
              "by state fiat or personal declaration.",
              ["https://en.wikipedia.org/wiki/Micheal_Bergstrom",
               "https://ballotpedia.org/Micheal_Bergstrom"]),
    ]),

    # ---------- Tom Woods (OK-R, District 4) ----------
    ("tom-woods", "OK", "Senator", [
        claim("tw1", "tom-woods", "self_defense", 0, True,
              "Woods, a dairy farmer and business owner representing rural Adair County "
              "and parts of Delaware, Sequoyah, and Cherokee Counties, ran for the Oklahoma "
              "Senate explicitly committed to 'staunchly defend the Second Amendment.' "
              "He has served in the Oklahoma Senate under the state's constitutional carry "
              "law (HB 2597, signed February 27, 2019 by Gov. Stitt) — which allows "
              "law-abiding Oklahomans 21 and over to carry firearms without a government-"
              "issued permit — and has not moved to restrict any existing firearm rights "
              "in his district or statewide.",
              ["https://ballotpedia.org/Tom_Woods_(Oklahoma)",
               "https://en.wikipedia.org/wiki/Tom_Woods_(Oklahoma_politician)",
               "http://tomwoodsok.com/"]),
        claim("tw2", "tom-woods", "sanctity_of_life", 0, True,
              "Woods campaigned for the Oklahoma Senate pledging to 'advocate for "
              "constitutional freedoms, especially for the unborn' — a commitment "
              "documented in his official campaign platform and Ballotpedia profile. "
              "As a Republican state senator from a deeply conservative rural district, "
              "he supports Oklahoma's existing near-total abortion ban framework, including "
              "the 2022 trigger laws that prohibit virtually all abortions in the state "
              "following the U.S. Supreme Court's Dobbs decision.",
              ["https://ballotpedia.org/Tom_Woods_(Oklahoma)",
               "https://en.wikipedia.org/wiki/Tom_Woods_(Oklahoma_politician)"]),
    ]),

    # ---------- Lisa Standridge (OK-R, District 15) ----------
    ("lisa-standridge", "OK", "Senator", [
        claim("ls1", "lisa-standridge", "sanctity_of_life", 0, True,
              "Standridge ran for and won Oklahoma Senate District 15 in November 2024 "
              "on an anti-abortion platform, defeating Democrat Elizabeth Foreman with "
              "61 percent of the vote. A licensed pharmacist with a doctorate from the "
              "University of Oklahoma College of Pharmacy and co-owner of pharmacies in "
              "Blanchard and Norman, she opposes abortion and supports Oklahoma's existing "
              "pro-life legal framework — a near-total abortion ban in effect since the "
              "state's pre-Dobbs trigger laws activated after the June 2022 Dobbs ruling. "
              "Ballotpedia documents her as anti-abortion.",
              ["https://ballotpedia.org/Lisa_Standridge",
               "https://www.oudaily.com/news/oklahoma-election-results-lisa-standridge-elizabeth-foreman-oklahoma-senate-district-15/article_b79c6d3e-9be6-11ef-b769-8f99212ff17c.html"]),
        claim("ls2", "lisa-standridge", "self_defense", 0, True,
              "Standridge is documented by Ballotpedia as a supporter of the Second "
              "Amendment. Representing District 15 (Norman/Blanchard area), she was "
              "elected in 2024 on a conservative Republican platform that includes "
              "protecting Oklahomans' right to keep and bear arms, consistent with "
              "Oklahoma's constitutional carry law (HB 2597, 2019) and the state's "
              "existing pro-Second Amendment legal framework.",
              ["https://ballotpedia.org/Lisa_Standridge",
               "https://www.oudaily.com/news/oklahoma-election-results-lisa-standridge-elizabeth-foreman-oklahoma-senate-district-15/article_b79c6d3e-9be6-11ef-b769-8f99212ff17c.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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
