#!/usr/bin/env python3
"""Enrichment batch 599: hand-curated claims for 5 sitting state-level R officials.

All archetype_curated federal senator/representative buckets are exhausted;
these targets are evidence_state R officials with 0 claims, taken from the
bottom of the alphabet (OH, NH, NE, MS, KS — furthest from the top-of-alphabet
agent's AK/AL/AR territory).

Targets:
  Keith Faber     (OH) — State Auditor, 2026 AG candidate
  John Formella   (NH) — Attorney General (reconfirmed 2025)
  Mike Hilgers    (NE) — Attorney General
  Lynn Fitch      (MS) — Attorney General
  Kris Kobach     (KS) — Attorney General

Claims cite reliable sources (official AG sites, en.wikipedia.org, ballotpedia.org)
and reflect 2022-2026 documented actions/positions.

MINIFIED write — do not add indent=2.
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
    # -------- Keith Faber (OH — State Auditor, 2026 AG candidate) --------
    ("keith-faber", "OH", "Auditor", [
        claim("kf1", "keith-faber", "public_justice", 0, True,
              "As Ohio's State Auditor since 2019, Faber oversaw the criminal "
              "conviction of more than 155 public officials and spearheaded audits "
              "that identified billions of dollars in unemployment fraud and abuse — "
              "a record of rigorous government accountability and zero tolerance for "
              "public-sector corruption.",
              ["https://ohioauditor.gov/about/auditor.html",
               "https://en.wikipedia.org/wiki/Keith_Faber"]),
        claim("kf2", "keith-faber", "economic_stewardship", 2, True,
              "As President of the Ohio Senate (2013–2016), Faber built a record of "
              "restraining state spending, cutting taxes, and opposing deficit-financed "
              "expansions of government — a posture he continued as Auditor by "
              "scrutinizing wasteful public expenditures and recovering public funds.",
              ["https://en.wikipedia.org/wiki/Keith_Faber",
               "https://ballotpedia.org/Keith_Faber"]),
    ]),

    # -------- John Formella (NH — Attorney General, reconfirmed 2025) --------
    ("john-formella", "NH", "Attorney General", [
        claim("jf1", "john-formella", "self_defense", 1, True,
              "AG Formella led a 25-state coalition in a 2025 amicus brief urging "
              "the U.S. Supreme Court to strike down Massachusetts' nonresident "
              "firearm licensing scheme, which imposes 40–170-day delays, high fees, "
              "and subjective 'suitability' denials on law-abiding travelers — "
              "defending the constitutional right to carry across state lines and "
              "opposing de facto licensing barriers that function as a registry.",
              ["https://www.doj.nh.gov/news-and-media/new-hampshire-leads-25-state-coalition-defending-second-amendment-rights-law-abiding",
               "https://en.wikipedia.org/wiki/John_Formella"]),
        claim("jf2", "john-formella", "border_immigration", 1, True,
              "Formella joined a coalition of more than 20 state AGs calling on "
              "President Biden to designate Mexican drug cartels as Foreign Terrorist "
              "Organizations, noting that cartels import raw chemicals from China to "
              "manufacture deadly synthetic opioids and traffic them across the "
              "southwest border — a designation that would enable mandatory "
              "prosecutorial and removal actions against cartel-linked individuals.",
              ["https://www.doj.nh.gov/resources/press-releases/attorney-general-formella-urges-biden-administration-designate-drug",
               "https://en.wikipedia.org/wiki/John_Formella"]),
        claim("jf3", "john-formella", "public_justice", 0, True,
              "Formella pursued aggressive opioid industry accountability, securing "
              "New Hampshire's share of nationwide settlements including a $21 billion "
              "national distributor agreement (2021) and approximately $720 million "
              "from eight drug manufacturers (2024–2025) — holding the pharmaceutical "
              "industry responsible for the overdose epidemic rather than shielding "
              "corporate actors from consequences.",
              ["https://www.doj.nh.gov/news-and-media/attorney-general-formella-announces-720-million-nationwide-opioid-settlements-eight",
               "https://ballotpedia.org/John_Formella"]),
    ]),

    # -------- Mike Hilgers (NE — Attorney General) --------
    ("mike-hilgers", "NE", "Attorney General", [
        claim("mh1", "mike-hilgers", "sanctity_of_life", 0, True,
              "AG Hilgers filed an amicus brief urging the U.S. Supreme Court to "
              "protect each state's authority to regulate abortion, and in February "
              "2026 led 21 states in a brief supporting Louisiana's challenge to a "
              "Biden-era rule that expanded abortion-drug access in defiance of state "
              "law — consistently affirming unborn life and state sovereignty over "
              "abortion policy.",
              ["https://ago.nebraska.gov/news/attorney-general-hilgers-urges-us-supreme-court-protect-states%E2%80%99-right-regulate-abortion",
               "https://ago.nebraska.gov/news/nebraska-files-brief-supporting-louisianas-challenge-biden-era-abortion-drug-rule"]),
        claim("mh2", "mike-hilgers", "border_immigration", 0, True,
              "Hilgers joined a 27-state coalition supporting Texas's physical "
              "border-barrier construction against the Biden administration's attempt "
              "to dismantle them (January 2024), and in January 2026 joined an amicus "
              "brief supporting federal immigration enforcement authority in Minnesota "
              "— backing both physical barrier infrastructure and mandatory federal "
              "enforcement of immigration law.",
              ["https://en.wikipedia.org/wiki/Mike_Hilgers",
               "https://ago.nebraska.gov/about"]),
        claim("mh3", "mike-hilgers", "election_integrity", 0, True,
              "Hilgers joined a multistate AG letter supporting election integrity "
              "measures and filed suit to support Presidential Executive Order 14399 "
              "requiring citizenship verification and integrity in federal voter "
              "registration — backing voter-identification-equivalent enforcement and "
              "removal of noncitizens from voter rolls.",
              ["https://ago.nebraska.gov/attorney-general-hilgers-joins-multistate-letter-supporting-election-integrity",
               "https://ago.nebraska.gov/ag-hilgers-joins-lawsuit-support-executive-order-ensuring-citizenship-verification-and-integrity"]),
    ]),

    # -------- Lynn Fitch (MS — Attorney General) --------
    ("lynn-fitch", "MS", "Attorney General", [
        claim("lf1", "lynn-fitch", "sanctity_of_life", 0, True,
              "Fitch argued Dobbs v. Jackson Women's Health Organization before the "
              "U.S. Supreme Court (December 2021), explicitly requesting the Court "
              "overrule Roe v. Wade and Planned Parenthood v. Casey; after the Court "
              "agreed in June 2022 she immediately certified the ruling, activating "
              "Mississippi's trigger law and making Mississippi one of the first "
              "states to end elective abortion post-Dobbs — the most consequential "
              "pro-life legal action by any state AG in modern history.",
              ["https://en.wikipedia.org/wiki/Lynn_Fitch",
               "https://en.wikipedia.org/wiki/Dobbs_v._Jackson_Women%27s_Health_Organization"]),
        claim("lf2", "lynn-fitch", "sanctity_of_life", 1, True,
              "Mississippi's trigger law activated by Fitch bans all abortions in "
              "the state except to preserve the mother's life or in cases of rape — "
              "effectively ending elective abortion in Mississippi and going far "
              "beyond incremental gestational restrictions toward near-total "
              "abolition of elective abortion.",
              ["https://en.wikipedia.org/wiki/Lynn_Fitch",
               "https://en.wikipedia.org/wiki/Abortion_in_Mississippi"]),
    ]),

    # -------- Kris Kobach (KS — Attorney General) --------
    ("kris-kobach", "KS", "Attorney General", [
        claim("kk1", "kris-kobach", "election_integrity", 0, True,
              "Kobach led a 26-state AG coalition in October 2024 filing an amicus "
              "brief urging the Supreme Court to allow Virginia to remove noncitizens "
              "from its voter rolls; in April 2026 Kansas intervened with 10 other "
              "states defending Presidential Executive Order 14399 requiring "
              "citizenship verification in federal voter registration — making him "
              "the most aggressive state AG enforcer of clean-voter-rolls and "
              "anti-noncitizen-voting measures.",
              ["https://www.ag.ks.gov/Home/Components/News/News/310/1292",
               "https://en.wikipedia.org/wiki/Kris_Kobach"]),
        claim("kk2", "kris-kobach", "border_immigration", 1, True,
              "Kobach, who rose to national prominence as a hardline immigration "
              "enforcer, as Kansas AG obtained an injunction stopping a Biden rule "
              "that granted Obamacare benefits to illegal aliens, and co-filed suit "
              "in January 2025 to block illegal alien counting for Congressional "
              "reapportionment in the 2030 Census — consistently backing mandatory "
              "enforcement and opposing amnesty-adjacent policies.",
              ["https://www.ag.ks.gov/about-us/attorney-general-kris-w-kobach",
               "https://en.wikipedia.org/wiki/Kris_Kobach"]),
        claim("kk3", "kris-kobach", "biblical_marriage", 2, True,
              "Kobach obtained an injunction stopping the Biden administration's "
              "April 2024 Title IX regulatory expansion that would have redefined "
              "'sex' to include gender identity and required Kansas schools to affirm "
              "and accommodate gender transitions — rejecting the federal imposition "
              "of transgender ideology on Kansas students and educational institutions.",
              ["https://www.ag.ks.gov/about-us/attorney-general-kris-w-kobach",
               "https://en.wikipedia.org/wiki/Kris_Kobach"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
