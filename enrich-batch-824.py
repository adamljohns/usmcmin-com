#!/usr/bin/env python3
"""Enrichment batch 824: hand-curated claims for 5 TN state representatives.

Targets archetype_party_default Tennessee state representatives with 0 evidence
claims, taken from the BOTTOM of the alphabet (TN) to avoid collision with the
top-of-alphabet enrichment loop.

Targets: Rush Bricken (TN-H47, since 2019), Ron Travis (TN-H31, since 2012),
Tandy Darby (TN-H76, since Nov 2020), Tim Hicks (TN-H6, since Jan 2021),
Tom Stinnett (TN-H20, since Jan 2025).

Sources: confirmed bill co-sponsorships from capitol.tn.gov sponsor lists,
legiscan.com, en.wikipedia.org, tnreportcard.org, and Tennessee news outlets.

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
    # ----------- Rush Bricken (TN-H47, R, since 2019) -----------
    ("rush-bricken", "TN", "Representative", [
        claim("rb1", "rush-bricken", "sanctity_of_life", 0, True,
              "As a member of the Tennessee House Republican supermajority in the "
              "111th General Assembly (2019), voted for the Human Life Protection Act "
              "(HB1029/SB1257) — Tennessee's trigger statute banning abortion from the "
              "point of fertilization with only a narrow life-of-the-mother exception, "
              "which became operative law on August 25, 2022, thirty days after Roe v. "
              "Wade was overturned in Dobbs v. Jackson Women's Health Organization.",
              ["https://en.wikipedia.org/wiki/Abortion_in_Tennessee",
               "https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB1029&GA=111"]),
        claim("rb2", "rush-bricken", "family_child_sovereignty", 0, True,
              "Prime co-sponsor of Tennessee HB252/SB674 (113th General Assembly, "
              "2023-2024), which removed the requirement that parents providing home "
              "instruction (homeschool) must furnish immunization and health service "
              "records to local education agencies — explicitly protecting homeschool "
              "families from vaccine-mandate enforcement by public school authorities "
              "and shielding parental educational decisions from government inspection.",
              ["https://legiscan.com/TN/bill/HB0252/2023"]),
        claim("rb3", "rush-bricken", "biblical_marriage", 2, True,
              "Confirmed co-sponsor of Tennessee HB1/SB1 (113th General Assembly, 2023), "
              "banning healthcare providers from administering gender-affirming procedures "
              "— including puberty blockers, cross-sex hormones, and surgical interventions "
              "— to minors for gender transition. The House passed the bill 77-16; Gov. Lee "
              "signed it March 2, 2023. The U.S. Supreme Court upheld the law in United "
              "States v. Skrmetti (June 2025), affirming states' authority to protect "
              "children from irreversible sex-change interventions.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://www.capitol.tn.gov/Bills/113/Bill/SB0001.pdf"]),
    ]),

    # ----------- Ron Travis (TN-H31, R, since 2012) -----------
    ("ron-travis", "TN", "Representative", [
        claim("rt1", "ron-travis", "sanctity_of_life", 0, True,
              "A long-serving member of the Tennessee House Republican caucus since 2012 "
              "who voted for the Human Life Protection Act (HB1029/SB1257, 111th General "
              "Assembly, 2019) — the trigger ban on abortion from fertilization that became "
              "operative in August 2022 after Dobbs v. Jackson. The law contains no rape or "
              "incest exceptions, reflecting an uncompromising life-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Abortion_in_Tennessee",
               "https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB1029&GA=111"]),
        claim("rt2", "ron-travis", "biblical_marriage", 2, True,
              "Confirmed co-sponsor of Tennessee HB3/SB228 (112th General Assembly, 2021), "
              "prohibiting transgender athletes from competing on women's and girls' athletic "
              "teams in K-12 public schools based on gender identity rather than biological "
              "sex — making Tennessee one of the first states to enact such a biological-sex "
              "protection measure in school sports.",
              ["https://www.capitol.tn.gov/Bills/112/Bill/HB0003.pdf",
               "https://en.wikipedia.org/wiki/LGBTQ_rights_in_Tennessee"]),
        claim("rt3", "ron-travis", "self_defense", 0, True,
              "Confirmed co-sponsor of Tennessee HJR38 (113th General Assembly, 2023-2024), "
              "a proposed amendment to the Tennessee Constitution to remove the legislature's "
              "authority to regulate the wearing of arms — strengthening the state's "
              "right-to-bear-arms provision to a constitutional-carry standard enshrined "
              "in the state's founding document, removing any pretext for legislative "
              "restriction of lawful gun carrying by Tennessee citizens.",
              ["https://tnreportcard.org/bill/hjr-38/",
               "https://legiscan.com/TN/bill/HJR38/2023"]),
    ]),

    # ----------- Tandy Darby (TN-H76, R, since Nov 2020) -----------
    ("tandy-darby", "TN", "Representative", [
        claim("td1", "tandy-darby", "self_defense", 0, True,
              "Voted YES on Tennessee HB786/SB765 (112th General Assembly, 2021), the "
              "landmark permitless constitutional-carry law allowing law-abiding "
              "Tennesseans aged 21 and older to carry handguns — openly or concealed "
              "— without a government-issued permit. Gov. Lee signed the bill April 8, "
              "2021, making Tennessee the 20th state to adopt constitutional carry.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee",
               "https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB0786"]),
        claim("td2", "tandy-darby", "biblical_marriage", 2, True,
              "Confirmed co-sponsor of Tennessee HB1/SB1 (113th General Assembly, 2023), "
              "banning gender-affirming procedures for minors including puberty blockers, "
              "hormones, and surgical interventions. The House passed the bill 77-16; "
              "Gov. Lee signed it March 2, 2023. The U.S. Supreme Court upheld the law "
              "in United States v. Skrmetti (June 2025).",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://www.capitol.tn.gov/Bills/113/Bill/SB0001.pdf"]),
        claim("td3", "tandy-darby", "refuse_state_overreach", 0, True,
              "Primary sponsor of Tennessee HJR81 (113th General Assembly, 2023-2024), "
              "a proposed constitutional amendment permanently prohibiting the General "
              "Assembly from levying or authorizing a state-level property tax — "
              "constitutionally enshrining the protection of private land and homeownership "
              "from state taxation. The resolution passed the House 81-11 (April 2023) and "
              "the Senate 26-6 (March 2024), placing it on the November 2026 ballot for "
              "voter ratification.",
              ["https://www.capitol.tn.gov/Bills/113/Bill/HJR0081.pdf"]),
    ]),

    # ----------- Tim Hicks (TN-H6, R, since Jan 2021) -----------
    ("tim-hicks", "TN", "Representative", [
        claim("th1", "tim-hicks", "biblical_marriage", 2, True,
              "Confirmed co-sponsor of Tennessee HB1/SB1 (113th General Assembly, 2023), "
              "banning gender-affirming care for minors. The House passed the bill 77-16; "
              "Gov. Lee signed it March 2, 2023. The U.S. Supreme Court upheld the law "
              "in United States v. Skrmetti (June 2025), affirming Tennessee's authority "
              "to protect children from irreversible sex-change interventions.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://www.capitol.tn.gov/Bills/113/Bill/SB0001.pdf"]),
        claim("th2", "tim-hicks", "family_child_sovereignty", 0, True,
              "Co-sponsored Tennessee legislation (HB853, 113th General Assembly, 2023-2024) "
              "ensuring that parents and legal guardians have the right to access their "
              "minor children's full medical records — including prescriptions and treatments "
              "provided without prior parental consent — overriding any medical-provider or "
              "government barrier to parental oversight of a child's healthcare decisions.",
              ["https://www.billtrack50.com/legislatordetail/24921",
               "https://legiscan.com/TN/people/tim-hicks/id/22447"]),
        claim("th3", "tim-hicks", "self_defense", 0, True,
              "Voted YES on Tennessee HB786/SB765 (112th General Assembly, 2021), the "
              "permitless constitutional-carry law eliminating the permit requirement for "
              "law-abiding adults to carry handguns. Rep. Hicks' constituent Capitol Hill "
              "Report described the bill as removing 'encroachments on law-abiding citizens "
              "who wish to exercise their Second Amendment right to carry a handgun.'",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee",
               "https://tnhousegop.org/members/representative-tim-hicks/"]),
    ]),

    # ----------- Tom Stinnett (TN-H20, R, since Jan 2025) -----------
    ("tom-stinnett", "TN", "Representative", [
        claim("ts1", "tom-stinnett", "christian_liberty", 0, True,
              "Co-sponsored Tennessee HB47/SB303 (114th General Assembly, 2025), permitting "
              "local school boards and public charter schools to display the Ten Commandments "
              "alongside foundational American documents — the Declaration of Independence "
              "preamble, U.S. Constitution preamble, Bill of Rights, and Tennessee "
              "Constitution. The House passed the bill 74-17, affirming Judeo-Christian "
              "heritage in public educational settings.",
              ["https://legiscan.com/TN/bill/HB0047/2025",
               "https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=HB0047&ga=114"]),
        claim("ts2", "tom-stinnett", "border_immigration", 3, True,
              "Co-sponsored Tennessee HB1705/SB1922 (114th General Assembly, 2025), "
              "requiring all state agencies and local governments to use the federal "
              "E-Verify system to confirm the immigration status of employees — closing "
              "the loophole that allowed unauthorized immigrants to hold government "
              "positions funded by Tennessee taxpayers.",
              ["https://legiscan.com/TN/bill/HB1705/2025",
               "https://tennesseelookout.com"]),
        claim("ts3", "tom-stinnett", "refuse_state_overreach", 0, True,
              "Co-sponsored Tennessee HB132/SB396 (114th General Assembly, 2025), "
              "requiring the Governor's emergency-power declarations to be subject to "
              "mandatory legislative oversight and approval rather than allowing indefinite "
              "unilateral executive emergency rule — restoring constitutional separation "
              "of powers at the state level and blocking the executive branch from "
              "governing by emergency decree without legislative consent.",
              ["https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=HB0132&ga=114",
               "https://legiscan.com/TN/legislature/TN/2025"]),
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
