#!/usr/bin/env python3
"""Enrichment batch 695: cited claims for 5 Utah State Representatives.

All federal and archetype_party_default federal buckets are exhausted (694 batches);
pivoting to UT State Representatives from the bottom of the alphabet (UT).

Targets (5):
  Nicholeen P. Peck (UT - State Representative, District 28, Tooele County)
  Nelson T. Abbott (UT - State Representative, District 57, Orem)
  Norman K. Thurston (UT - State Representative, District 62, Provo)
  Scott H. Chew (UT - State Representative, District 68, Uintah Basin)
  Paul A. Cutler (UT - State Representative, District 18, Davis County)

Sources: le.utah.gov, house.utleg.gov, ballotpedia.org, utahnewsdispatch.com,
         ksl.com, sltrib.com, abc4.com, peck4utah.com, nelsonabbott.com,
         votepaulcutler.com, justfacts.votesmart.org, legiscan.com,
         progressreport.betterutah.org, termlimits.com, utahwaterrights.blogspot.com

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB limit.
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
    # -------------- Nicholeen P. Peck (UT - State Representative, District 28) --------------
    ("nicholeen-p-peck", "UT", "Representative", [
        claim("np1", "nicholeen-p-peck", "sanctity_of_life", 0, True,
              "Peck sponsored HB 233 (2025), which banned entities that perform elective abortions "
              "— including Planned Parenthood educators — from providing health instruction or "
              "materials in Utah public schools. The bill passed the House 51-14 and Senate 18-8 "
              "along party lines and was signed into law. She also sponsored HB 315 (2026), "
              "requiring schools to show fetal development videos (including Live Action's 'Baby "
              "Olivia' animated video) during 5th/6th-grade health classes. Her campaign pledge "
              "states she 'advocates for the protection of life at ALL STAGES of life from the "
              "very old to the very young.'",
              ["https://utahnewsdispatch.com/2025/02/21/utah-house-passes-bill-ban-planned-parenthood-educators-from-schools/",
               "https://www.ksl.com/article/51455046/utah-lawmakers-work-to-mandate-fetal-development-videos-in-schools",
               "https://le.utah.gov/~2025/bills/static/HB0233.html",
               "https://peck4utah.com/my-pledge/"]),
        claim("np2", "nicholeen-p-peck", "family_child_sovereignty", 0, True,
              "Peck sponsored HB 209 (2025), the Homeschool Amendments act, which removed a "
              "statutory affidavit requirement imposed on homeschooling parents — a requirement "
              "that had been used by some school districts to conduct background checks on "
              "homeschooling families. The bill was signed into law. Peck is an advocate for "
              "UHOPE (Utah Home-education Organizations for Parental Empowerment) and addressed "
              "the organization at its launch. Her campaign pledge states 'children are born to "
              "their parents, not to society' and she commits to 'protect the sovereign, most "
              "basic unit of society, the family, against government intrusion or overreach.'",
              ["https://www.sltrib.com/news/2025/02/22/utah-bill-that-would-adjust/",
               "https://le.utah.gov/~2025/bills/static/HB0209.html",
               "https://peck4utah.com/my-pledge/"]),
        claim("np3", "nicholeen-p-peck", "biblical_marriage", 2, True,
              "Peck sponsored HB 250 (2025), which prohibited employers and school districts from "
              "disciplining teachers who, in good faith or due to sincere personal moral or "
              "religious beliefs, use a student's biological sex pronouns or birth name rather "
              "than preferred pronouns — protecting conscience rights against compelled transgender "
              "ideology affirmation. She also sponsored HB 521 (2025), prohibiting the use of "
              "any public funds, including Medicaid, for gender-transition treatments or surgeries "
              "for any patient.",
              ["https://www.abc4.com/news/politics/utah-lawmakers-transgender-bills-2025/",
               "https://le.utah.gov/~2025/bills/static/HB0250.html",
               "https://le.utah.gov/~2025/bills/static/HB0521.html",
               "https://www.sltrib.com/news/politics/2025/02/18/utah-lawmaker-moves-restrict/"]),
    ]),

    # -------------- Nelson T. Abbott (UT - State Representative, District 57) --------------
    ("nelson-t-abbott", "UT", "Representative", [
        claim("na1", "nelson-t-abbott", "self_defense", 0, True,
              "Abbott co-sponsored HB 60 (2021), Utah's constitutional carry bill, which allows "
              "any person 21 or older who may lawfully possess a firearm to carry concealed in "
              "public without a government permit. The bill was signed into law by Governor "
              "Spencer Cox, making Utah one of the first states to enact permitless concealed "
              "carry. Abbott's campaign website states: 'I will be an active voice for the "
              "Second Amendment.'",
              ["https://le.utah.gov/~2021/bills/static/HB0060.html",
               "https://utahcarrylaws.com/hb60-conceal-carry-firearms-amendments/",
               "https://kutv.com/news/utah-legislature-2021/governor-signs-permit-less-concealed-carry-bill-into-law",
               "https://www.nelsonabbott.com/"]),
        claim("na2", "nelson-t-abbott", "sanctity_of_life", 0, True,
              "Abbott's campaign website explicitly states: 'I will be an active voice for the "
              "Second Amendment and the Right to Life.' As a member of the House Judiciary "
              "Committee, he voted YES in committee on HB 467 (2023), the Abortion Changes "
              "bill that delicensed Utah abortion clinics (barring new licenses after May 2, "
              "2023 and operations after January 1, 2024) and tightened the trigger-ban "
              "exceptions to cover only life-threatening physical conditions — the strongest "
              "practical abortion restriction available under existing Utah law.",
              ["https://www.nelsonabbott.com/",
               "https://progressreport.betterutah.org/legislators/rep-nelson-t-abbott/",
               "https://le.utah.gov/~2023/bills/static/HB0467.html"]),
        claim("na3", "nelson-t-abbott", "family_child_sovereignty", 0, True,
              "Abbott's campaign platform explicitly opposes federal intervention in education "
              "and affirms parental authority: 'each parent has the right to provide their "
              "children the best education, and parents, teachers and local school boards should "
              "be the major drivers on education, not big government.' He states he is 'opposed "
              "to federal intervention in education and will fight to protect parents' roles in "
              "providing the best education possible for their children.'",
              ["https://www.nelsonabbott.com/",
               "https://justfacts.votesmart.org/candidate/biography/192472/nelson-abbott"]),
    ]),

    # -------------- Norman K. Thurston (UT - State Representative, District 62) --------------
    ("norman-k-thurston", "UT", "Representative", [
        claim("nt1", "norman-k-thurston", "self_defense", 1, True,
              "Thurston was the chief House sponsor of HB 67 (2016), 'Weapons on Public "
              "Transportation,' which decriminalized the peaceful possession of a concealed "
              "firearm on public transit — changing what had previously been treated as a "
              "criminal offense to lawful conduct for permit-eligible individuals. The bill "
              "removed a felony-level trap that otherwise applied to law-abiding concealed "
              "carry holders who used public transportation.",
              ["https://le.utah.gov/~2016/bills/static/HB0067.html",
               "https://legiscan.com/UT/text/HB0067/id/1369704",
               "https://kslnewsradio.com/1902051/gunwatch-gun-bills-need-know-theyll-impact"]),
        claim("nt2", "norman-k-thurston", "sanctity_of_life", 0, True,
              "Thurston voted YES on HB 467 (2023), the Abortion Changes bill, which delicensed "
              "Utah abortion clinics, barred new clinic licenses after May 2, 2023, required "
              "abortions to take place in hospitals after January 1, 2024, and tightened the "
              "trigger-ban exceptions to cover only life-threatening physical conditions — "
              "restricting rape and incest exceptions to pregnancies under 18 weeks. The bill "
              "passed the House 56-14.",
              ["https://progressreport.betterutah.org/bills/2023/hb-467/",
               "https://le.utah.gov/~2023/bills/static/HB0467.html"]),
    ]),

    # -------------- Scott H. Chew (UT - State Representative, District 68) --------------
    ("scott-h-chew", "UT", "Representative", [
        claim("sc1", "scott-h-chew", "economic_stewardship", 2, True,
              "Chew sponsored SB 159 (2016, Severance Tax Exemption Extension) and SB 134 "
              "(Oil and Gas Conservation Account Amendments), legislation that extended tax "
              "relief for oil and gas producers in Utah's Uintah Basin — reducing the government "
              "tax burden on energy producers and keeping more revenue in the private sector. "
              "Chew is a fourth-generation rancher and energy-district representative whose "
              "career reflects consistent resistance to tax increases on productive industries.",
              ["https://justfacts.votesmart.org/candidate/biography/151551/scott-chew",
               "https://house.utleg.gov/rep/CHEWSH/",
               "https://ballotpedia.org/Scott_H._Chew"]),
        claim("sc2", "scott-h-chew", "refuse_state_overreach", 0, True,
              "Chew sponsored HB 63 (2026, Livestock Watering Amendments), signed into law, "
              "which created a formal legal framework allowing ranchers to register historic "
              "livestock water rights on privately owned land and on land where they hold "
              "grazing permits. The law protects established ranching water uses from bureaucratic "
              "challenge and gives Utah ranchers a clear legal title to water they have used "
              "for generations — pushing back against regulatory encroachment on agricultural "
              "property rights.",
              ["https://le.utah.gov/~2026/bills/static/HB0063.html",
               "http://utahwaterrights.blogspot.com/2026/04/2026-legislation-water-bills-that-passed.html",
               "https://house.utleg.gov/rep/CHEWSH/"]),
    ]),

    # -------------- Paul A. Cutler (UT - State Representative, District 18) --------------
    ("paul-a-cutler", "UT", "Representative", [
        claim("pc1", "paul-a-cutler", "christian_liberty", 0, True,
              "Cutler's official campaign platform states: 'we must rigorously guard religious "
              "liberties, relentlessly encourage freedom, and fiercely protect the rights of "
              "each individual' and he pledges to 'fight for personal liberty and religious "
              "freedoms.' In the same platform he commits to 'fight against overreach and "
              "mandates, keeping decisions local whenever possible.'",
              ["https://votepaulcutler.com/"]),
        claim("pc2", "paul-a-cutler", "family_child_sovereignty", 0, True,
              "Cutler's campaign platform states: 'Parents have the right and responsibility "
              "to be involved as a stakeholder in curriculum and education decisions and to "
              "make the best education related choices for their children.' He also worked on "
              "2023 education funding legislation and supports Utah's school-choice scholarship "
              "program (Utah Fits All), arguing that accreditation mandates on private schools "
              "represent government overstep 'into private school spaces.'",
              ["https://votepaulcutler.com/",
               "https://votepaulcutler.com/f/2023-week-1-newsletter",
               "https://www.deseret.com/utah/2026/02/17/utah-fits-all-modifications/"]),
        claim("pc3", "paul-a-cutler", "refuse_state_overreach", 0, True,
              "Cutler signed the U.S. Term Limits Convention pledge, committing to limit the "
              "power of career politicians. He sponsored HB 450 (2026, Data Privacy Amendments), "
              "which passed the House 66-1 and Senate 28-0 and was signed by Governor Cox on "
              "March 19, 2026. The law protects private individuals' home addresses from public "
              "records disclosure — shielding citizens and donors from government-enabled "
              "exposure. Campaign: 'state government should work WITH, NOT AGAINST, our local "
              "county, cities, and school district.'",
              ["https://www.termlimits.com/paul-cutler-supports-term-limits/",
               "https://le.utah.gov/~2026/bills/static/HB0450.html",
               "https://www.deseret.com/opinion/2026/05/24/data-privacy-law-helps-prevent-political-violence/",
               "https://votepaulcutler.com/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing slug collisions."""
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
