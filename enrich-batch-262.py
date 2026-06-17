#!/usr/bin/env python3
"""Enrichment batch 262: second-wave claims for 5 sitting US senators.

archetype_curated bucket exhausted; targets are evidence_curated sitting
US senators with only 4 claims, pulled from bottom of alphabet:
Cynthia Lummis (WY-R), Mike Lee (UT-R), Patty Murray (WA-D),
Maria Cantwell (WA-D), Ted Cruz (TX-R). Each new claim spans a distinct
rubric category not yet covered for that senator. All claims sourced
2021-2026 from official .gov / congress.gov / govtrack.us / wikipedia.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ---------------- Cynthia Lummis (WY-R, US Senator) ----------------
    ("cynthia-lummis", "WY", "Senator", [
        claim("cl4", "cynthia-lummis", "election_integrity", 0, True,
              "Lummis was among the 11 Republican senators who co-signed the January 2, 2021 joint statement led by Cruz and Johnson demanding a 10-day Emergency Electoral Commission to audit the 2020 election results in six disputed states. She then voted against certifying Pennsylvania's electoral votes on January 7, 2021 — one of only 7 senators to do so — stating she had 'serious concerns about election integrity, especially in Pennsylvania.'",
              ["https://www.lummis.senate.gov/press-releases/statement-from-senator-cynthia-lummis-on-electoral-college-certification-vote/",
               "https://www.cruz.senate.gov/?p=press_release&id=5541",
               "https://en.wikipedia.org/wiki/Cynthia_Lummis"]),
        claim("cl5", "cynthia-lummis", "self_defense", 1, True,
              "Lummis has consistently sponsored legislation to restore and protect Second Amendment rights rather than restrict them: she introduced the SAME Act (Second Amendment Mandates Equality Act) to reinstate the right of 18-to-20-year-olds to purchase handguns from federally licensed dealers, and she led a bill to 'Preserve Second Amendment Rights for Law-Abiding Wyoming Citizens' that required federal law to give due consideration to lawful self-defense in any firearms rulemaking — opposing the magazine-limit, registry, and red-flag framework the rubric rejects.",
              ["https://www.lummis.senate.gov/press-releases/lummis-leads-bill-to-preserve-second-amendment-rights-for-law-abiding-wyoming-citizens/",
               "https://www.lummis.senate.gov/press-releases/lummis-introduces-same-act-to-restore-18-year-olds-constitutional-right-to-purchase-handgun/",
               "https://en.wikipedia.org/wiki/Cynthia_Lummis"]),
    ]),

    # ---------------- Mike Lee (UT-R, US Senator) ----------------
    ("mike-lee", "UT", "Senator", [
        claim("ml1", "mike-lee", "sanctity_of_life", 0, True,
              "In January 2024 Senator Lee introduced a four-bill pro-life legislative package — the Abortion is not Health Care Act, the Protecting Life in Health Savings Accounts Act, the Protecting Life in Foreign Assistance Act, and the GUARD Act (Guaranteeing the Unborn Access to Respect and Dignity), which establishes personhood protections for unborn children under federal law from the moment of fertilization. He reprised the same package in January 2025 for the March for Life, stating life begins at conception and federal law must reflect that principle.",
              ["https://www.lee.senate.gov/2024/1/senator-lee-introduces-four-bills-to-protect-the-unborn",
               "https://www.lee.senate.gov/2025/1/lee-introduces-pro-life-legislation-for-march-for-life",
               "https://www.lee.senate.gov/public/index.cfm/protecting-life"]),
        claim("ml2", "mike-lee", "self_defense", 0, True,
              "In March 2026 Senator Lee introduced the National Constitutional Carry Act, federal legislation to guarantee that any person legally permitted to possess a firearm may carry it — openly or concealed — in any U.S. state without obtaining a government-issued permit, eliminating state-level permit requirements for all lawful gun owners nationwide. This directly fulfills the rubric's constitutional-carry ideal.",
              ["https://www.lee.senate.gov/2026/3/lee-introduces-national-constitutional-carry-act",
               "https://www.lee.senate.gov/public/index.cfm/protect-2a"]),
    ]),

    # ---------------- Patty Murray (WA-D, US Senator) ----------------
    ("patty-murray", "WA", "Senator", [
        claim("pm1", "patty-murray", "economic_stewardship", 2, False,
              "As Chair of the Senate Appropriations Committee (2023-2024), Murray shepherded the $1.66 trillion FY2024 omnibus government-funding package — the largest single-year discretionary spending bill in U.S. history at the time — and secured over $513 million in earmarked community-project spending for Washington State. She has consistently opposed balanced-budget proposals and any cuts to domestic discretionary programs, stating her priority is investing in communities rather than reducing the deficit, running counter to the rubric's balanced-budget ideal.",
              ["https://www.murray.senate.gov/senator-murray-secures-over-513-million-for-key-infrastructure-environmental-and-social-projects-and-priorities-in-draft-appropriations-bills/",
               "https://www.appropriations.senate.gov/news/majority/senate-approves-final-fy24-funding-package-in-overwhelming-74-24-vote",
               "https://ballotpedia.org/Patty_Murray"]),
        claim("pm2", "patty-murray", "border_immigration", 0, False,
              "Murray has consistently opposed physical border-barrier construction and military-style enforcement: her official immigration page calls for 'comprehensive immigration reform' that offers 'a fair pathway to citizenship for the more than 11 million undocumented immigrants living in America, including Dreamers, farmworkers, and those with Temporary Protected Status' — explicitly rejecting the wall-and-military-deployment enforcement framework the rubric endorses. In 2024 she used her Appropriations chairmanship to release a national-security supplemental stripped of the border-enforcement provisions Republicans had demanded.",
              ["https://www.murray.senate.gov/immigration/",
               "https://www.appropriations.senate.gov/news/majority/with-republicans-planning-to-block-bipartisan-supplemental-with-border-policy-changes-they-demanded-murray-releases-supplemental-without-border-provisions",
               "https://ballotpedia.org/Patty_Murray"]),
    ]),

    # ---------------- Maria Cantwell (WA-D, US Senator) ----------------
    ("maria-cantwell", "WA", "Senator", [
        claim("mc1", "maria-cantwell", "self_defense", 1, False,
              "Cantwell voted 'Yea' on the Bipartisan Safer Communities Act (S.2938, Senate vote #242, June 23, 2022), which passed 65-33 and was signed into law. She issued a press statement praising its provisions, specifically calling out 'creating grants to help states implement crisis intervention programs like red flag laws, enhancing background checks for individuals under 21, and closing the boyfriend loophole so any domestic violence abuser cannot possess or purchase a firearm' — endorsing red-flag-law funding and new firearms purchase restrictions that the rubric opposes.",
              ["https://www.cantwell.senate.gov/news/press-releases/cantwell-statement-on-passage-of-historic-bipartisan-gun-safety-bill",
               "https://www.govtrack.us/congress/votes/117-2022/s242",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
        claim("mc2", "maria-cantwell", "economic_stewardship", 2, False,
              "Cantwell has opposed Republican-sponsored budget cuts as fiscally reckless while consistently supporting expanded federal spending packages: she voted against the GOP's Continuing Resolution that cut $280 million from NIH, slashed the Army Corps of Engineers budget by 44 percent, and reduced USDA Agriculture Research Services by $57 million — stating those cuts were unacceptable — and has championed large multi-year appropriations packages to fund technology research, clean energy, and infrastructure, prioritizing program growth over deficit reduction.",
              ["https://www.cantwell.senate.gov/news/press-releases/cantwell-statement-on-voting-against-gops-continuing-resolution-bill",
               "https://ballotpedia.org/Maria_Cantwell",
               "https://www.govtrack.us/congress/members/maria_cantwell/300018/report-card/2024"]),
    ]),

    # ---------------- Ted Cruz (TX-R, U.S. Senator) ----------------
    ("ted-cruz", "TX", "Senator", [
        claim("tc1", "ted-cruz", "election_integrity", 0, True,
              "Cruz led the group of 11 Republican senators who on January 2, 2021 issued a joint statement demanding a 10-day Emergency Electoral Commission to audit the 2020 presidential election in six disputed states, citing allegations of fraud and irregularities 'that exceed any in our lifetimes.' He objected to Arizona's electoral votes on January 6-7, 2021, forcing a roll-call vote in the Senate. He subsequently opposed the Electoral Count Reform Act of 2022, arguing it unconstitutionally reduced Congress's ability to reject fraudulent electoral-vote submissions.",
              ["https://www.cruz.senate.gov/?p=press_release&id=5541",
               "https://www.cruz.senate.gov/newsroom/press-releases/sen-cruz-we-have-an-obligation-to-the-constitution-to-ensure-that-this-election-was-lawful",
               "https://www.cruz.senate.gov/newsroom/press-releases/sen-cruz-opposes-electoral-count-reform-act-for-reducing-congressional-ability-to-address-voter-fraud"]),
        claim("tc2", "ted-cruz", "biblical_marriage", 0, True,
              "Cruz voted against the Respect for Marriage Act (RFMA) when it passed the Senate in November 2022 (61-36) and again in December 2022 (61-36 final passage), which codified federal recognition of same-sex and interracial marriages. He issued a press statement explaining his opposition, and together with Senator Mike Lee co-sponsored the State Marriage Defense Act to preserve each state's right to define marriage as one man and one woman — maintaining the one-man-one-woman definition the rubric endorses.",
              ["https://www.cruz.senate.gov/newsroom/press-releases/cruz-statement-on-vote-against-so-called-respect-for-marriage-act",
               "https://www.cruz.senate.gov/newsroom/press-releases/sens-cruz-and-lee-introduce-state-marriage-defense-act",
               "https://en.wikipedia.org/wiki/Political_positions_of_Ted_Cruz"]),
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
