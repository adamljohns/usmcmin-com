#!/usr/bin/env python3
"""Enrichment batch 596: hand-curated claims for 5 Oregon Democratic state senators.

Targets archetype_party_default OR state senators with 0 claims, continuing
from batch 595 (which covered 5 OR Republican senators). This batch covers the
next 5 in reverse-alpha order: Wlnsvey Campos, Sara Gelser Blouin, Rob Wagner,
Mark Meek, Lisa Reynolds — all Democrats.

Each claim cites >=1 reliable source and reflects documented 2023-2025
voting record / public positions.

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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------------- Wlnsvey Campos (OR-D, State Senator SD-18, Aloha) ----------------
    ("wlnsvey-campos", "OR", "Senator", [
        claim("wc1", "wlnsvey-campos", "sanctity_of_life", 0, False,
              "Voted YES on HB 2002 (June 15, 2023, 17-3), which declares 'every individual has a fundamental right' to 'pregnancy termination services' and mandates state Medicaid coverage for abortion — rejecting any recognition of fetal personhood or life-at-conception protections. Campos represents Senate District 18 (Aloha, Washington County) and took office January 9, 2023. She explicitly lists 'abortion and reproductive health care' as a core policy priority.",
              ["https://fastdemocracy.com/bill-search/or/2023/bills/ORB00017712/",
               "https://www.opb.org/article/2023/05/04/oregon-politics-republican-walkout-boycott-senate-salem-reproductive-health-care-abortion-gender/",
               "https://ballotpedia.org/Wlnsvey_Campos"]),
        claim("wc2", "wlnsvey-campos", "biblical_marriage", 2, False,
              "The same HB 2002 vote (17-3, June 15, 2023) mandated that all Oregon health benefit plans cover 'gender-affirming treatment' for individuals of all ages and added new civil-rights protections for people seeking gender-affirming care — Campos voted YES, endorsing state-required transgender hormone therapy and surgery coverage as a benefit and institutionalizing transgender ideology in Oregon health policy.",
              ["https://www.opb.org/article/2023/05/04/oregon-politics-republican-walkout-boycott-senate-salem-reproductive-health-care-abortion-gender/",
               "https://fastdemocracy.com/bill-search/or/2023/bills/ORB00017712/"]),
        claim("wc3", "wlnsvey-campos", "family_child_sovereignty", 0, False,
              "HB 2002, which Campos voted for, includes a provision allowing Oregon minors younger than 15 to access gender-affirming and reproductive healthcare without parental knowledge or consent in certain circumstances — directly undermining parental authority over minors' medical decisions and contra the rubric's requirement of parental rights and anti-CPS/state-overreach protections.",
              ["https://www.opb.org/article/2023/05/04/oregon-politics-republican-walkout-boycott-senate-salem-reproductive-health-care-abortion-gender/",
               "https://olis.oregonlegislature.gov/liz/2023R1/Measures/Overview/HB2002"]),
    ]),

    # ---------------- Sara Gelser Blouin (OR-D, State Senator SD-8, Corvallis area) ----------------
    ("sara-gelser-blouin", "OR", "Senator", [
        claim("sgb1", "sara-gelser-blouin", "sanctity_of_life", 0, False,
              "Describes herself as 'proudly pro-choice' who 'will always defend women's access to reproductive health care services' and voted YES on HB 2002 (June 15, 2023, 17-3), the law declaring abortion a fundamental right in Oregon. Gelser Blouin has represented District 8 (Corvallis, Albany, and parts of Linn, Benton, and Marion Counties) since 2015 and scores 4% on the Oregon Freedom Index, reflecting a consistently progressive/anti-restraint voting record.",
              ["https://saragelser.com/",
               "https://freedomindex.us/legislator/9901/session/256/report/179",
               "https://ballotpedia.org/Sara_Gelser_Blouin"]),
        claim("sgb2", "sara-gelser-blouin", "biblical_marriage", 4, False,
              "Identifies as a 'longtime supporter of equal rights for LGBT Oregonians' and consistently champions LGBTQ nondiscrimination protections in state government programs, schools, and publicly funded services. As chair of the Senate Human Services Committee she has embedded LGBTQ-affirming frameworks into Oregon foster care, mental health, and social-services policy — promoting LGBTQ ideology in state institutions.",
              ["https://saragelser.com/",
               "https://en.wikipedia.org/wiki/Sara_Gelser_Blouin"]),
        claim("sgb3", "sara-gelser-blouin", "economic_stewardship", 2, False,
              "Carries a 4% Freedom Index score in the Oregon Senate — among the lowest in the chamber — reflecting consistent opposition to limited-government, fiscal-restraint legislation. As a long-serving member and chair of the Senate Human Services Committee she has championed sustained expansions of state welfare, foster care, behavioral-health, and Medicaid budgets, prioritizing spending growth over balanced-budget discipline.",
              ["https://freedomindex.us/legislator/9901/session/256/report/179",
               "https://en.wikipedia.org/wiki/Sara_Gelser_Blouin"]),
    ]),

    # ---------------- Rob Wagner (OR-D, State Senator SD-19, Senate President) ----------------
    ("rob-wagner", "OR", "Senator", [
        claim("rw1", "rob-wagner", "sanctity_of_life", 0, False,
              "As Oregon Senate President, publicly and repeatedly refused to remove HB 2002 from the floor calendar during the historic 6-week Republican walkout of 2023 — the walkout's primary demand — stating: 'I'm not going to pull bills just because other senators don't want to vote on them.' HB 2002 declares a fundamental right to abortion and mandates state Medicaid funding for pregnancy termination services; it was signed into law July 13, 2023 under Wagner's sustained leadership.",
              ["https://www.kgw.com/article/news/local/the-story/oregon-senate-president-rob-wagner-republican-walkout-interview/283-465491f6-c447-4e30-9310-685d11ece772",
               "https://www.kptv.com/2023/07/13/kotek-signs-controversial-abortion-ghost-gun-bills-into-law/",
               "https://en.wikipedia.org/wiki/Rob_Wagner_(politician)"]),
        claim("rw2", "rob-wagner", "biblical_marriage", 2, False,
              "Held firm on HB 2002's mandate requiring Oregon health plans to cover gender-affirming care — including transgender hormone therapy and surgery for all ages — rejecting Republican demands to strip those provisions during the 2023 walkout standoff. As Senate President, he shepherded HB 2002 to final passage (17-3, June 15, 2023), institutionalizing gender-affirming care coverage statewide and rejecting the rubric's opposition to transgender ideology in public policy.",
              ["https://www.opb.org/article/2023/05/03/republican-walk-out-oregon-senate-abortion-guns-gender-affirming-care/",
               "https://oregoncapitalchronicle.com/2023/05/03/oregon-senate-republicans-independent-stage-walkout-as-divisive-bills-await-votes/"]),
        claim("rw3", "rob-wagner", "economic_stewardship", 2, False,
              "Spent a decade as a staff executive at American Federation of Teachers – Oregon (AFT-Oregon), the statewide teachers' union, before entering elected office. His political career is grounded in organized labor's advocacy for expanded public employee compensation, collective bargaining, and state education spending — a posture consistently opposing fiscal restraint and balanced-budget governance.",
              ["https://en.wikipedia.org/wiki/Rob_Wagner_(politician)",
               "https://ballotpedia.org/Rob_Wagner"]),
    ]),

    # ---------------- Mark Meek (OR-D, State Senator SD-20, N. Clackamas) ----------------
    ("mark-meek", "OR", "Senator", [
        claim("mm1", "mark-meek", "sanctity_of_life", 0, False,
              "Voted YES on HB 2002 (June 15, 2023, 17-3) declaring a fundamental right to abortion in Oregon. His campaign materials explicitly describe him as 'fighting against a ban on abortion, protecting access to birth control, and defending a woman's right to choose.' Meek represents Senate District 20 (northern Clackamas County), having transitioned from the Oregon House (District 40) to the Senate in January 2023.",
              ["https://fastdemocracy.com/bill-search/or/2023/bills/ORB00017712/",
               "https://ballotpedia.org/Mark_Meek",
               "https://votemarkmeek.com/"]),
        claim("mm2", "mark-meek", "biblical_marriage", 2, False,
              "Voted YES on HB 2002 (June 15, 2023), which mandated gender-affirming care coverage in Oregon health insurance plans and extended state-funded gender-affirming and reproductive services access to minors under 15 without parental consent. By casting that vote, Meek endorsed Oregon's policy institutionalizing transgender medical care as a required benefit and waiving parental consent for minors' gender care.",
              ["https://olis.oregonlegislature.gov/liz/2023R1/Measures/Overview/HB2002",
               "https://fastdemocracy.com/bill-search/or/2023/bills/ORB00017712/"]),
        claim("mm3", "mark-meek", "economic_stewardship", 2, False,
              "Endorsed by SEIU Oregon State Council (Service Employees International Union), reflecting alignment with organized labor's priorities of expanded public employee benefits, state spending on social services, and opposing fiscal-restraint measures — inconsistent with the rubric's balanced-budget and anti-deficit standards.",
              ["https://seiu-oregon.org/legislator/mark-meek/",
               "https://ballotpedia.org/Mark_Meek"]),
    ]),

    # ---------------- Lisa Reynolds (OR-D, State Senator SD-17, Portland/Cedar Mill) ----------------
    ("lisa-reynolds", "OR", "Senator", [
        claim("lr1", "lisa-reynolds", "self_defense", 1, False,
              "As Moms Demand Action for Gun Sense's volunteer state legislative lead for two years, trained over 400 Moms Demand Action volunteers on how to lobby Oregon legislators for gun-control bills, and traveled the state teaching 100+ medical providers how to counsel patients on 'safe gun storage.' Helped pass Oregon firearms-restriction legislation and is described as 'a fierce advocate for gun violence prevention,' opposing the rubric's protection of broad Second Amendment rights.",
              ["https://www.lisafororegon.com/",
               "https://en.wikipedia.org/wiki/Lisa_Reynolds"]),
        claim("lr2", "lisa-reynolds", "sanctity_of_life", 0, False,
              "A pediatrician who served as a front-line provider of reproductive health care and publicly stated her provider role gave her 'moral clarity on the need for' HB 2002 (signed July 13, 2023), which declared abortion a fundamental right in Oregon and mandated Medicaid coverage for pregnancy termination services. Appointed to Oregon Senate District 17 (Downtown Portland, Cedar Mill, Bethany) in November 2024 after serving in the Oregon House since 2019.",
              ["https://www.lisafororegon.com/",
               "https://multco.us/news/multnomah-and-washington-county-commissioners-appoint-representative-lisa-reynolds-oregon-senate"]),
        claim("lr3", "lisa-reynolds", "biblical_marriage", 2, False,
              "Also provided gender-affirming medical care as a front-line practitioner and publicly championed HB 2002's gender-affirming care mandate — stating she 'will never stop fighting to protect patients and providers from government intrusion in care decisions.' Actively opposes any restriction on transgender medical care for minors or adults, rejecting the rubric's call to refuse transgender ideology in public policy.",
              ["https://www.lisafororegon.com/",
               "https://en.wikipedia.org/wiki/Lisa_Reynolds"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
