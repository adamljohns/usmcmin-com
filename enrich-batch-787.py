#!/usr/bin/env python3
"""Enrichment batch 787: 5 Utah Republican state representatives.

All federal and archetype_curated buckets are exhausted.
Targets taken from the bottom of the reversed archetype_party_default
Republican state-legislative bucket (UT, sorted reverse-alpha by name).

Matt MacPherson (District 26), Mark A. Strong (District 47),
Logan Monson (District 69), Lisa Shepherd (District 61),
Leah Hansen (District 51).

Sources: le.utah.gov, en.wikipedia.org, ksltv.com, sltrib.com,
utahpolicy.com, house.utleg.gov, kpcw.org, utahnewsdispatch.com,
ballotpedia.org, conventionofstates.com, ksl.com.
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
    # ------- Matt MacPherson (UT-R, District 26, West Valley City) -------
    ("matt-macpherson", "UT", "Representative", [
        claim("mm1", "matt-macpherson", "self_defense", 1, True,
              "MacPherson was chief sponsor of H.B. 195 — Firearm Retention Amendments — in the 2025 Utah General Session (Senate Sponsor: Daniel McCay). The bill prohibits a plea-in-abeyance from including a condition that a defendant forfeit their firearms unless the underlying offense itself restricts firearm possession, and requires law enforcement to return seized firearms to any individual who is not legally restricted from possessing them. The House passed it 72-0 on February 11, 2025; Governor Cox signed it effective May 7, 2025. The bill directly opposes the use of criminal-justice process as a backdoor mechanism to strip non-restricted Utahns of their lawfully held firearms.",
              ["https://le.utah.gov/~2025/bills/static/HB0195.html",
               "https://ballotpedia.org/Matt_MacPherson"]),
        claim("mm2", "matt-macpherson", "family_child_sovereignty", 3, True,
              "MacPherson was chief sponsor of H.B. 477 — School Trespass Amendments — in the 2025 Utah General Session. The bill narrowed the definition of school property covered by criminal trespass to school buildings and added an explicit protection: public comments made during a school board meeting that comply with time, place, manner, and relevance restrictions cannot be the basis for a criminal trespass charge on grounds of 'intent to cause annoyance.' Governor Cox signed it on March 27, 2025 (effective May 7, 2025). The bill prevents school boards from weaponizing trespass law to silence or criminalize parents who speak out at public school board meetings.",
              ["https://le.utah.gov/~2025/bills/static/HB0477.html",
               "https://utahpolicy.com/news-release/76246-matt-macpherson-launches-re-election-campaign-for-utah-house-district-26"]),
    ]),

    # ------- Mark A. Strong (UT-R, District 47, Bluffdale) -------
    ("mark-a-strong", "UT", "Representative", [
        claim("ms1", "mark-a-strong", "public_justice", 0, True,
              "Strong sponsored H.B. 127 — 'Ashley's Law' — during the 2025 Utah General Session, adding a mandatory 15-years-to-life sentencing provision for rape, object rape, and forcible sodomy when committed against any incapacitated adult, defined as a person 14 or older with a physical, intellectual, neurological, or cognitive disability that prevents them from understanding, resisting, or reporting the assault. The bill passed the Utah House on February 3, 2025 and the Senate on March 5, 2025; Governor Cox signed it effective May 7, 2025.",
              ["https://le.utah.gov/~2025/bills/static/HB0127.html",
               "https://ksltv.com/local-news/ashleys-law/756670/"]),
        claim("ms2", "mark-a-strong", "election_integrity", 0, True,
              "Strong sponsored H.B. 92 — Voting Amendments — in the 2024 Utah General Session, which would have ended Utah's automatic universal vote-by-mail system: instead of all active voters automatically receiving mail ballots, voters would need to affirmatively opt in, and counties would be required to maintain at least one in-person voting center per 5,000 active non-mail voters. Strong also sponsored HCR005 (2023) — Concurrent Resolution Opposing Federal Legislative Efforts to Strip States of Authority to Regulate Congressional Elections — which the Utah House passed on February 23, 2023. Both actions document sustained opposition to centralized mass-mail-in election administration and a commitment to preserving state election integrity authority.",
              ["https://le.utah.gov/~2024/bills/static/HB0092.html",
               "https://le.utah.gov/~2023/bills/static/HCR005.html"]),
    ]),

    # ------- Logan Monson (UT-R, District 69, Blanding / San Juan County) -------
    ("logan-monson", "UT", "Representative", [
        claim("lm1", "logan-monson", "family_child_sovereignty", 0, True,
              "Monson voted YES (House passed 48-19, third reading, February 11, 2025) on H.B. 281 — Health Curriculum and Procedures Amendments — which requires Utah schools to obtain informed parental consent before providing school-based health services, including mental health therapy, to students, and allows parents to designate specific topics that school counselors may not discuss with their children. Signed by the Governor on March 26, 2025 (effective July 1, 2025), the bill established that parents — not public schools or government health agencies — hold primary authority over their children's health care and therapeutic exposure.",
              ["https://le.utah.gov/~2025/bills/static/HB0281.html",
               "https://ballotpedia.org/Logan_Monson"]),
        claim("lm2", "logan-monson", "public_justice", 0, True,
              "Monson was prime sponsor of H.B. 540 — Judicial Transparency — during the 2026 Utah General Session, co-carried with Sen. Brady Brammer. The bill: (1) required the Utah Judicial Council to create a single free publicly searchable portal for all public court records; and (2) for the first time compelled judges and court commissioners to file annual financial and conflict-of-interest disclosure statements identical to the standards already required of every other elected Utah official — covering board positions, investments, non-investment income, real estate, and spouses' employment. Signed by the Governor on March 25, 2026. The bill also prompted the Utah Supreme Court to adopt a new rule barring retired appellate judges from appearing before their former court for two years post-retirement.",
              ["https://le.utah.gov/~2026/bills/static/HB0540.html",
               "https://house.utleg.gov/utahs-2026-judicial-reforms-more-transparency-more-judges-and-greater-accountability/"]),
    ]),

    # ------- Lisa Shepherd (UT-R, District 61, southwest Orem / west Provo) -------
    ("lisa-shepherd", "UT", "Representative", [
        claim("ls1", "lisa-shepherd", "border_immigration", 3, True,
              "Shepherd was chief sponsor of H.B. 386 — Immigration Amendments — in the 2026 Utah General Session (Senate Sponsor: Paige Nelson). The bill required USHE institutions to verify lawful presence before providing out-of-state tuition waivers or scholarships, prohibited illegal immigrants from accessing in-state tuition rates, certain state home-loan programs, and professional licensing, and repealed the Utah Guest Worker Program and related employee-verification provisions. The House passed H.B. 386 39-33 on February 27, 2026, though the Senate ultimately struck the enacting clause. Shepherd's authorship documents her position that state benefits, employment programs, and professional licenses must be conditioned on lawful immigration status.",
              ["https://le.utah.gov/Session/2026/bills/static/HB0386.html",
               "https://www.ksl.com/article/51455044/utahns-first-or-eroding-the-utah-way-house-oks-measure-cracking-down-on-illegal-immigration"]),
        claim("ls2", "lisa-shepherd", "election_integrity", 0, True,
              "Shepherd co-sponsored H.B. 209 — Voting Amendments — in the 2026 Utah General Session (Chief Sponsor: Rep. A. Cory Maloy). The bill created a bifurcated ballot system requiring documentary proof of U.S. citizenship — a passport, birth certificate, state-issued citizenship-confirming ID, naturalization certificate, or tribal ID — to register to vote in state and local elections; voters unable to provide documentation are limited to federal-race ballots only. The House passed it 51-16-8 on March 5, 2026; Governor Cox signed it on March 25, 2026. By May 2026, over 5,000 Utah voters had been notified of the new requirement.",
              ["https://le.utah.gov/~2026/bills/static/HB0209.html",
               "https://utahnewsdispatch.com/2026/05/27/5000-utah-voters-need-to-provide-proof-of-citizenship-under-new-state-law/"]),
    ]),

    # ------- Leah Hansen (UT-R, District 51, Utah County, appointed Aug 13 2025) -------
    ("leah-hansen", "UT", "Representative", [
        claim("lh1", "leah-hansen", "family_child_sovereignty", 0, True,
              "Before her appointment to the Utah House in August 2025, Hansen testified publicly in support of SCR002 — 'Concurrent Resolution Encouraging Practices that Promote Child Independence' — during the 2025 Utah General Session, sponsored by Sen. Lincoln Fillmore. The resolution encouraged schools and parents to restore unstructured, independent, free-range experiences to children, pushing back against over-programmed and hyper-supervised childhood environments promoted by government institutions. The Senate Education Committee advanced it unanimously. Hansen's public advocacy, documented on her Wikipedia page, reflects her conviction that families — not government institutions — should direct child development.",
              ["https://le.utah.gov/~2025/bills/static/SCR002.html",
               "https://en.wikipedia.org/wiki/Leah_Hansen"]),
        claim("lh2", "leah-hansen", "biblical_marriage", 4, True,
              "Hansen publicly supported H.B. 261 — Equal Opportunity Initiatives — in January 2024, sponsored by Rep. Katy Hall. The legislation prohibited DEI offices in all Utah public colleges, universities, K-12 schools, and government agencies from engaging in 'differential treatment or preference' based on race, sex, sexual orientation, religion, or gender identity; DEI programs were required to transform into general 'student success centers' open to all. The House passed HB261 60-14; Governor Cox signed it on January 31, 2024 (effective July 1, 2024). Hansen's documented advocacy for the bill opposes government-mandated promotion of LGBTQ ideology and race-based preferences in public education and state institutions.",
              ["https://le.utah.gov/~2024/bills/static/HB0261.html",
               "https://www.sltrib.com/news/education/2024/01/31/utahs-gov-cox-signs-anti-dei-bill/",
               "https://en.wikipedia.org/wiki/Leah_Hansen"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher: returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
