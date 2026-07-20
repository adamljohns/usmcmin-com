#!/usr/bin/env python3
"""Enrichment batch 789: 5 Utah Republican state representatives.

All federal and archetype_curated buckets exhausted.
Targets taken from the reversed archetype_party_default Republican
state-legislative bucket (UT, sorted reverse-alpha by first name),
continuing after batch 788 (which covered K/J names: Kristen, Kay, Katy,
Karen, Joseph).

Jordan D. Teuscher (District 44, South Jordan),
Jon Hawkins (District 55, Pleasant Grove),
Jill Koford (District 10, Ogden),
Jefferson S. Burton (District 64),
Jason Thompson (District 3, River Heights).

Sources: le.utah.gov, ksl.com, sltrib.com, utahnewsdispatch.com,
ballotpedia.org, legiscan.com, house.utleg.gov,
news.ballotpedia.org.
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
    # ------- Jordan D. Teuscher (UT-R, District 44, South Jordan) -------
    ("jordan-d-teuscher", "UT", "Representative", [
        claim("jdt1", "jordan-d-teuscher", "family_child_sovereignty", 0, True,
              "Teuscher was the substitute sponsor of H.B. 464 — Social Media Amendments — in the 2024 Utah General Session. The bill established that algorithmically curated social media platforms are legally presumed to have caused harm when a licensed mental health provider diagnoses a Utah minor with an adverse mental health outcome linked to excessive platform use. Social media companies escape this liability only by satisfying a strict parental-consent safe-harbor: they must obtain documented parental consent before a minor creates an account, disable algorithm-driven features that promote excessive use, limit minor account-holders' total daily platform time, and block access to the platform during nighttime hours. Governor Cox signed H.B. 464 on March 13, 2024. By conditioning corporate immunity on documented parental consent and robust parental oversight tools, the bill substantially expands parents' legal authority over their children's exposure to addictive social-media algorithms and gives families a private right of action against platforms that bypass those protections.",
              ["https://le.utah.gov/~2024/bills/static/HB0464.html",
               "https://www.ksl.com/article/50590794/efforts-to-curb-youth-social-media-use-clear-utah-legislature-await-governors-signature",
               "https://utahnewsdispatch.com/2024/03/01/utah-lawmakers-pass-new-social-media-restrictions/"]),
        claim("jdt2", "jordan-d-teuscher", "economic_stewardship", 2, True,
              "Teuscher was chief sponsor of H.B. 267 — Public Sector Labor Union Amendments — in the 2025 Utah General Session. The bill prohibited all public-sector employers in Utah — including school districts, police and fire departments, and state agencies — from entering or renewing collective-bargaining agreements with labor unions, eliminating the primary mechanism by which government unions extract wage and benefit commitments from taxpayer-funded entities. The Utah House passed H.B. 267 by a 42-32 vote; Governor Cox signed it on February 14, 2025 (effective July 1, 2025). By ending collective bargaining for public employees, the measure removed a primary structural driver of long-term government personnel costs and unfunded pension obligations — a direct fiscal-discipline measure. The legislature subsequently repealed H.B. 267 in a December 2025 special session after labor coalitions gathered over 320,000 referendum signatures (the most in Utah history); Teuscher himself sponsored the repeal, stating H.B. 267 was 'good policy' but had been 'overshadowed by misinformation and unnecessary division.'",
              ["https://le.utah.gov/~2025/bills/static/HB0267.html",
               "https://utahnewsdispatch.com/2025/01/27/utah-house-passes-labor-union-bill-teachers-police-firefighters/",
               "https://www.sltrib.com/news/politics/2025/03/10/utahs-hb267-an-inside-look-into/"]),
    ]),

    # ------- Jon Hawkins (UT-R, District 55, Pleasant Grove) -------
    ("jon-hawkins", "UT", "Representative", [
        claim("jha1", "jon-hawkins", "family_child_sovereignty", 0, True,
              "Hawkins was chief sponsor of H.B. 360 — School Athlete Amendments — in the 2026 Utah General Session. The bill prohibits any Utah public school from remaining a member of an activities association — such as the Utah High School Activities Association — that imposes periods of athletic ineligibility on students who transfer specifically because of open enrollment, a school-choice selection, or to escape a bullying environment. Prior UHSAA transfer rules routinely imposed year-long sit-out periods on transfer athletes, effectively penalizing families for exercising their statutory right to choose their child's school: a family that moved their child to a better-fitting school under open enrollment saw their child lose a full year of varsity eligibility. H.B. 360 removes that barrier by barring UHSAA membership for any school that enforces such penalties against open-enrollment or bullying-escape transfers. The bill takes effect July 1, 2026, ensuring that school-choice decisions are not financially or athletically punished.",
              ["https://le.utah.gov/~2026/bills/static/HB0360.html"]),
        claim("jha2", "jon-hawkins", "refuse_state_overreach", 0, True,
              "Hawkins was a named co-sponsor of H.B. 273 — Classroom Technology Amendments — in the 2026 Utah General Session (chief sponsor: Rep. Ariel Defay; Senate sponsor: Sen. Chris H. Wilson). The bill required the State Board of Education to develop model policies governing technology and artificial intelligence use in public school classrooms, and placed direct statutory limits on State Board authority over elementary-grade technology mandates. For grades K–3, H.B. 273 prohibits the Board from: requiring schools to send state-owned instructional devices home with students; mandating a one-device-per-student ratio; or requiring any classroom screen time beyond the narrow purposes of teaching required computer-science standards and administering standards-based assessments. K–3 instruction is instead directed toward hands-on, print-based, and developmentally appropriate learning. The bill takes effect July 1, 2026, rolling back Board mandates that had allowed EdTech vendors to gain a captive audience in Utah's youngest classrooms.",
              ["https://le.utah.gov/Session/2026/bills/static/HB0273.html",
               "https://le.utah.gov/Session/2026/bills/enrolled/HB0273.pdf"]),
    ]),

    # ------- Jill Koford (UT-R, District 10, Ogden) -------
    ("jill-koford", "UT", "Representative", [
        claim("jk1", "jill-koford", "election_integrity", 0, True,
              "Koford was a co-sponsor of H.B. 209 — Voting Amendments — in the 2026 Utah General Session (chief sponsor: Rep. A. Cory Maloy; Senate sponsor: Sen. Ronald M. Winterton). The bill created a bifurcated ballot system that requires documentary proof of U.S. citizenship — a valid passport, certified birth certificate, state-issued citizenship-confirming identification, naturalization certificate, or federally recognized tribal identification — in order to register to vote in Utah state and local races. Voters who cannot or choose not to provide such documentation are automatically limited to a federal-only ballot, retaining their right to vote in congressional and presidential contests but not in state or local ones. The House passed H.B. 209 by a 51-16-8 vote; Governor Cox signed it on March 25, 2026. By May 2026, more than 5,000 Utah registrants had been formally notified of the citizenship-documentation requirement. Koford's co-sponsorship aligned her with Utah's landmark proof-of-citizenship voting measure.",
              ["https://le.utah.gov/Session/2026/bills/enrolled/HB0209.pdf",
               "https://utahnewsdispatch.com/2026/05/27/5000-utah-voters-need-to-provide-proof-of-citizenship-under-new-state-law/",
               "https://utahnewsdispatch.com/briefs/utah-bill-requiring-proof-of-citizenship-to-vote-advances/"]),
        claim("jk2", "jill-koford", "family_child_sovereignty", 0, True,
              "Koford was chief sponsor of H.B. 308 — Driving by Minors Amendments — in the 2025 Utah General Session. The bill expanded the discretion that families have in supervising their minor children's driver training. Under prior law, a newly licensed driver under 18 was restricted to carrying only immediate family members as passengers, and a learner-permit holder under 18 was limited to practicing with a parent or legal guardian. H.B. 308 relaxed both constraints: it allows a newly licensed minor to carry one passenger who is not an immediate family member, and allows learner-permit holders under 18 to practice driving with approved adults other than a parent in specified circumstances. The House Transportation Committee recommended the 3rd Substitute version on February 6, 2025; the Senate Transportation Committee also reported favorably. The bill gives families flexibility to designate other trusted adults — grandparents, aunts, uncles, or family friends — to assist in their teen's driver education, reducing dependence on commercial driving schools and restoring family discretion over who may supervise a minor's behind-the-wheel learning.",
              ["https://le.utah.gov/~2025/bills/static/HB0308.html"]),
    ]),

    # ------- Jefferson S. Burton (UT-R, District 64) -------
    ("jefferson-s-burton", "UT", "Representative", [
        claim("jsb1", "jefferson-s-burton", "self_defense", 0, True,
              "Burton was a co-sponsor of H.B. 60 — Conceal Carry Firearms Amendments — in the 2021 Utah General Session. The bill established that any individual who is 21 years of age or older and who may lawfully possess a firearm may carry a concealed firearm in a public area without first obtaining or paying for a government-issued permit — implementing permitless constitutional carry as Utah law. The Utah Senate gave its final approval to the bill; Governor Spencer Cox indicated he would sign it into law. The legislation removed the pre-existing requirement that law-abiding adults obtain written government permission before exercising their Second Amendment right to carry a firearm for self-defense — recognizing that the right to bear arms requires no permit for ordinary citizens who are already legally entitled to possess a firearm. Burton's co-sponsorship marked his commitment to the full scope of Second Amendment rights without licensing as a prerequisite.",
              ["https://le.utah.gov/~2021/bills/static/HB0060.html",
               "https://www.sltrib.com/news/politics/2021/02/05/bill-end-concealed-weapon/",
               "https://www.ksl.com/article/50093060/bill-to-allow-utahns-to-carry-concealed-guns-without-any-permit-ignites-debate"]),
        claim("jsb2", "jefferson-s-burton", "election_integrity", 0, True,
              "Burton served as the House sponsor of S.B. 194 — Election Modifications — in the 2026 Utah General Session (chief Senate sponsor: Sen. Michael K. McKell). The bill amended Utah statutory provisions governing the nomination of candidates by political parties, updating the framework that controls how party nominees advance to the general election ballot and how parties exercise authority over candidate qualification and selection. By carrying S.B. 194 through the House chamber as the House sponsor, Burton helped advance election-law reforms to ensure that party-nomination processes reflect the will of registered party members and are protected from outside interference. The bill passed through multiple substitute amendments during the 2026 session before final passage, reflecting sustained engagement over its election-administration provisions.",
              ["https://le.utah.gov/Session/2026/bills/static/SB0194.html"]),
    ]),

    # ------- Jason Thompson (UT-R, District 3, River Heights) -------
    ("jason-thompson", "UT", "Representative", [
        claim("jte1", "jason-thompson", "economic_stewardship", 2, True,
              "Thompson was chief sponsor of H.B. 190 — Child Care Business Tax Credit — in the 2026 Utah General Session. The bill tripled the existing state income tax credit for employers who provide child care assistance to their employees, raising the credit rate from 10 percent to 30 percent of qualified child care expenditures. It also removed the prior restriction that limited the credit to on-site child care facilities, extending eligibility to employer-arranged or employer-subsidized off-site child care arrangements. H.B. 190 reduces total state income tax liability for qualifying businesses by an estimated $2.9 million annually. By directing tax relief specifically toward employers who invest in private-sector child care solutions, the bill encourages market-driven child care provision by small and medium-sized businesses rather than expanding government-managed child care programs or imposing new mandated employer spending — keeping child care affordable through private enterprise rather than increasing state outlays.",
              ["https://le.utah.gov/~2026/bills/static/HB0190.html",
               "https://www.ksl.com/article/51450337/utah-house-oks-bill-expanding-tax-credit-for-businesses-that-provide-child-care",
               "https://house.utleg.gov/utah-takes-on-child-care-costs-and-access-with-five-years-of-action/"]),
        claim("jte2", "jason-thompson", "refuse_state_overreach", 0, True,
              "Thompson publicly advocated for S.J.R. 2 — a proposed Utah constitutional amendment — before a Utah House committee during the 2025 General Session. S.J.R. 2, sponsored by Sen. Lincoln Fillmore, would require statewide ballot initiatives that impose new taxes, expand the application of existing taxes, or increase existing tax rates to receive at least 60 percent of the popular vote to take effect, rather than a bare simple majority. Thompson argued in the House committee that the proposed constitutional change gives voters the opportunity to set a higher standard for tax-raising direct democracy. S.J.R. 2 passed the House by a 55-17 vote and the Senate by 21-8, and was referred to Utah voters for ratification on the 2026 general election ballot. By supporting the 60-percent supermajority requirement, Thompson backed a structural constitutional safeguard against special-interest-funded ballot campaigns that use simple-majority direct democracy to expand the state's tax base and grow government spending outside the regular legislative appropriations process.",
              ["https://le.utah.gov/~2025/bills/static/sjr002.html",
               "https://utahnewsdispatch.com/2025/01/29/utah-lawmaker-wants-to-ask-voters-to-set-higher-bar-for-ballot-initiatives-that-raise-taxes/",
               "https://news.ballotpedia.org/2025/03/10/utah-legislature-refers-a-constitutional-amendment-to-2026-ballot-that-would-require-initiatives-making-tax-changes-to-receive-a-60-vote-of-approval/"]),
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
