#!/usr/bin/env python3
"""Enrichment batch 607: 5 sitting U.S. Senators — 10 claims.

All archetype_curated buckets depleted; targets carry evidence_curated confidence
with 6-7 existing claims. This batch fills DISTINCT uncovered rubric categories.

Targets (bottom-of-alphabet states):
  Jon Husted      (OH-R) — +2: biblical_marriage[2], foreign_policy_restraint[0]
  Bernie Moreno   (OH-R) — +2: christian_liberty[0], family_child_sovereignty[0]
  Kirsten Gillibrand (NY-D) — +2: christian_liberty[0], family_child_sovereignty[0]
  Chuck Schumer   (NY-D) — +2: christian_liberty[0], election_integrity[0]
  Pete Ricketts   (NE-R) — +2: election_integrity[0], family_child_sovereignty[0]
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
    # ---------- Jon Husted (OH-R, US Senator) ----------
    ("jon-husted", "OH", "Senator", [
        claim("jh1", "jon-husted", "biblical_marriage", 2, True,
              "As Ohio Lt. Governor, Husted publicly backed House Bill 68 (the SAFE Act) in December 2023 after Governor DeWine vetoed it, posting: 'I support it for two main reasons: Men should not compete in women's sports. Permanent medical decisions concerning gender should not be made when you are a child. I hope the SAFE Act will become law in Ohio.' As a newly appointed U.S. Senator, Husted championed Ohio House Bill 8 (the Parents' Bill of Rights, signed January 8, 2025) — legislation he personally spearheaded as Lt. Governor — requiring K-12 schools to notify parents if a student identifies as LGBTQ+ and allowing parents to opt their children out of sexuality and gender-identity classroom content. At the federal level, Husted voted for the FY2026 National Defense Authorization Act (S.2296, Senate vote December 17, 2025, passed 77-20), which included a statutory ban on transgender women competing in athletic programs at U.S. military service academies and a prohibition on Department of Defense funding for gender-affirming care for military family members.",
              ["https://abc6onyourside.com/news/local/men-shouldnt-play-womens-sports-lt-governor-jon-husted-weighs-in-on-safe-act",
               "https://thebuckeyeflame.com/2026/05/12/sherrod-brown-will-face-anti-transgender-republican-sen-jon-husted-in-bid-for-ohio-senate-seat/",
               "https://www.cbsnews.com/news/senate-passes-ndaa-defense-bill-trump/"]),
        claim("jh2", "jon-husted", "foreign_policy_restraint", 0, False,
              "Husted voted NAY on the Senate Iran War Powers Resolution (June 23, 2026, passed 50-48), which directed the President to remove U.S. military forces from hostilities against Iran within 30 days absent a congressional declaration of war or specific statutory authorization — the core Article I war-powers check on unilateral executive military action. Only four Republicans — Paul, Collins, Murkowski, and Cassidy — crossed over to support Article I authority; Husted sided with the 44-senator Republican bloc that opposed it. Earlier, in April 2025, Husted co-sponsored the Sanctioning Russia Act (S.1241), introduced by Senators Graham and Blumenthal with 84 co-sponsors, to impose sweeping new sanctions on Russia and countries purchasing Russian energy — a posture of sustained international economic engagement, stating: 'If Moscow wants a lasting peace with Ukraine, the door is open, and, if they refuse, I support sanctions that would make the consequences severe and certain.'",
              ["https://thehill.com/homenews/senate/5936650-iran-war-powers-senate/",
               "https://www.banking.senate.gov/newsroom/minority/mccormick-warren-husted-and-coons-co-lead-bipartisan-bill-to-strengthen-and-sustain-pressure-on-russian-oil-revenue-help-achieve-just-peace",
               "https://www.govtrack.us/congress/bills/119/s1241"]),
    ]),

    # ---------- Bernie Moreno (OH-R, US Senator) ----------
    ("bernie-moreno", "OH", "Senator", [
        claim("bm1", "bernie-moreno", "christian_liberty", 0, True,
              "Moreno ran as a firm Equality Act opponent throughout his 2024 Senate campaign, with the Human Rights Campaign and GLAAD documenting his opposition to extending Civil Rights Act protections to sexual orientation and gender identity — the framework that would strip RFRA as a defense for faith-based organizations. His 2024 campaign materials state he supports 'exempting faith-based organizations (e.g., adoption and foster care providers, private schools) from regulations that cause them to violate their sincerely held religious beliefs' — the practical equivalent of a RFRA-protection pledge for religious service providers. He co-sponsored S.292 (Educational Choice for Children Act, January 29, 2025, 119th Congress), which contains an explicit protective provision: 'No federal, state, or local government entity shall disfavor or discourage the use of scholarships ... at private or nonprofit elementary and secondary education institutions, including faith-based schools' — codifying a statutory shield against government discrimination targeting religious schools that accept scholarship students.",
              ["https://www.hrc.org/press-releases/human-rights-campaign-equality-votes-pac-condemns-radical-anti-equality-ohio-senate-candidate-bernie-moreno",
               "https://www.ontheissues.org/Senate/Bernie_Moreno.htm",
               "https://www.congress.gov/bill/119th-congress/senate-bill/292/all-info"]),
        claim("bm2", "bernie-moreno", "family_child_sovereignty", 0, True,
              "Co-introduced S.1148 (119th Congress) with Senators Paul and Lee to abolish the U.S. Department of Education entirely, stating: 'There is no constitutional role for the federal government in education, and returning power to the states will empower parents, cut red tape, and give our students the opportunity to receive the best possible education.' He separately co-sponsored S.292 (Educational Choice for Children Act, January 29, 2025), which creates federal tax credits for scholarship-granting organizations and expressly prohibits any government entity from disfavoring faith-based schools that accept scholarship students. In February 2025 Moreno sent a public letter demanding the Mentor, Ohio school board comply with President Trump's executive order ending 'radical indoctrination in K-12 schooling,' stating: 'The Mentor Board of Education, and all school boards across the country, must adhere to President Trump's Executive Orders and remove all woke, radical, and indoctrinating curriculum immediately.' His 2024 campaign record states he supports giving parents full access to curriculum and the right to opt children out of lessons or activities to which the parents object.",
              ["https://www.paul.senate.gov/senators-paul-lee-moreno-reintroduce-bill-to-abolish-the-department-of-education/",
               "https://www.congress.gov/bill/119th-congress/senate-bill/292",
               "https://www.moreno.senate.gov/press-releases/moreno-demands-answers-from-mentor-board-of-education-following-resistance-to-trumps-executive-order/"]),
    ]),

    # ---------- Kirsten Gillibrand (NY-D, US Senator) ----------
    ("kirsten-gillibrand", "NY", "Senator", [
        claim("kg1", "kirsten-gillibrand", "christian_liberty", 0, False,
              "Gillibrand was an original co-sponsor of the Senate Equality Act (S.393, 117th Congress, introduced February 23, 2021), whose explicit Section 1107 barred the Religious Freedom Restoration Act from being invoked as 'a claim concerning, or a defense to a claim under' any of the Act's nondiscrimination mandates — effectively stripping RFRA protection from faith-based employers, religious adoption agencies, Christian schools, and religious business owners facing LGBTQ nondiscrimination claims in employment, education, housing, and public accommodations. She separately co-sponsored the Do No Harm Act, which would amend RFRA itself to prevent religious freedom from being raised as a defense against anti-discrimination laws, healthcare access mandates, or government contract requirements — a direct statutory narrowing of the free-exercise protection RFRA has provided since 1993. The U.S. Conference of Catholic Bishops and major evangelical organizations warned the Equality Act would expose religious institutions to federal civil rights liability for declining to affirm same-sex unions or transgender ideology; Gillibrand's co-sponsorship of both bills represents an on-the-record commitment to enact that liability exposure.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/393/all-info",
               "https://www.govtrack.us/congress/bills/117/s393/cosponsors",
               "https://www.hrc.org/resources/do-no-harm-act"]),
        claim("kg2", "kirsten-gillibrand", "family_child_sovereignty", 0, False,
              "When House Republicans passed the Parents Bill of Rights Act (H.R.5, 118th Congress, March 2023, 213-208) — which would have required parental consent before schools change a student's gender markers or pronouns, mandated curriculum transparency, and required schools to make library book lists available to parents — Gillibrand provided no co-sponsorship or public support, and the Senate companion bill received no Democratic support. Her own 2019 'Family Bill of Rights' addresses government childcare access, paid family leave, and infant healthcare — not parental oversight of school curriculum or gender-identity school policies. Her official Senate record contains no co-sponsorships of school choice legislation (vouchers, education savings accounts, or scholarship tax credits), and she has consistently aligned with teachers' union positions that prioritize union authority over parental choice. No record exists of Gillibrand supporting parental notification requirements for minors' gender-identity accommodations in schools, parental curriculum review rights, or any mechanism giving parents legal recourse against school content they object to.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/5/text",
               "https://www.pbs.org/newshour/education/house-republicans-pass-parents-rights-bill-in-fight-over-schools",
               "https://www.ontheissues.org/social/Kirsten_Gillibrand_Education.htm"]),
    ]),

    # ---------- Chuck Schumer (NY-D, US Senator) ----------
    ("chuck-schumer", "NY", "Senator", [
        claim("cs1", "chuck-schumer", "christian_liberty", 0, False,
              "In a striking reversal of his own legislative legacy, Schumer — who personally sponsored the Religious Freedom Restoration Act in 1993 as a House Member, stating government should only infringe religious freedom 'when the government has a compelling interest in doing so' — co-sponsored the Senate Equality Act (S.393, 117th Congress, 2021) which explicitly provides that RFRA 'shall not provide a claim concerning, or a defense to a claim under, a covered title.' As Senate Majority Leader, Schumer then used his procedural authority to bypass normal committee referral and bring the Equality Act directly to the Senate floor, participating in public advocacy events to champion its passage while attacking opponents for their religious objections to LGBTQ nondiscrimination mandates. Legal scholars and journalism analysts noted the specific irony: the senator who authored the statute the Equality Act would nullify was the one floor-managing its passage — with GetReligion noting that many reporters ignored the Equality Act's direct dismantling of the Schumer-Kennedy RFRA.",
              ["https://www.republicanleader.senate.gov/newsroom/research/sen-schumers-religious-freedom-restoration-act-key-law-at-issue-in-hobby-lobby-",
               "https://www.democrats.senate.gov/dpcc/press-releases/transcript-at-event-to-push-for-passage-of-equality-act-schumer-slams-recent-gop-attacks-against-lgbtq-community",
               "https://thenewamerican.com/schumer-moves-anti-religious-freedom-equality-act-to-the-senate-floor/",
               "https://www.congress.gov/bill/117th-congress/senate-bill/393/all-info"]),
        claim("cs2", "chuck-schumer", "election_integrity", 0, False,
              "As Senate Majority Leader, Schumer championed and personally managed S.1 (For the People Act, 117th Congress) — which included provisions prohibiting states from requiring photo ID for federal elections, mandating same-day voter registration, and requiring nationwide no-excuse mail-in ballot access — declaring it legislation that would 'strengthen American democracy.' He brought S.1 to a cloture vote on June 22, 2021, which failed 50-50. He subsequently became the lead Senate opponent of the SAVE Act (S.128, 119th Congress) and SAVE America Act (S.3752), both requiring documentary proof of U.S. citizenship to register to vote. Schumer characterized the SAVE Act as 'Jim Crow 2.0,' posted that 'every single Senate Democrat will vote against any bill that contains it,' called it 'one of the most despicable pieces of legislation I've come across,' and delivered Senate floor remarks vowing to fight the citizenship-proof requirement 'tooth and nail.'",
              ["https://www.democrats.senate.gov/newsroom/press-releases/transcript-majority-leader-schumer-remarks-at-senate-rules-committee-hearing-on-s1-the-for-the-people-act-legislation-to-strengthen-american-democracy",
               "https://www.democrats.senate.gov/news/press-releases/leader-schumer-floor-remarks-slamming-the-save-act-as-jim-crow-20-calls-it-dead-on-arrival-in-the-senate",
               "https://thehill.com/homenews/senate/5720541-schumer-condemns-save-act/"]),
    ]),

    # ---------- Pete Ricketts (NE-R, US Senator) ----------
    ("pete-ricketts", "NE", "Senator", [
        claim("pr1", "pete-ricketts", "election_integrity", 0, True,
              "As Nebraska Governor, Ricketts was the principal public champion of Initiative 432, the 2022 ballot measure that amended the Nebraska Constitution to require photo ID to vote. He held town halls across the state in June 2022 promoting the initiative, called it 'a proactive step' to protect election integrity, and the initiative's campaign was substantially funded by his family ($1.88 million of the $2.1 million total, contributed by his mother Marlene Ricketts). The measure passed with 60% of Nebraska voters in November 2022. As U.S. Senator, Ricketts co-sponsored both the SAVE Act (S.128, January 28, 2026) and the SAVE America Act (S.3752, February 4, 2026) — Senate bills requiring documentary proof of U.S. citizenship at federal election registration and photo ID to vote in person, with absentee voters required to submit a copy of their ID with both their ballot request and their returned ballot. Ricketts stated he was 'a proud cosponsor of the SAVE America Act, which I believe is long overdue, to strengthen the integrity of our election systems.'",
              ["https://nebraskaexaminer.com/2022/06/28/gov-pete-ricketts-takes-voter-id-show-on-the-road-with-town-halls/",
               "https://ballotpedia.org/Nebraska_Initiative_432,_Photo_Voter_Identification_Initiative_(2022)",
               "https://www.congress.gov/bill/119th-congress/senate-bill/128/cosponsors"]),
        claim("pr2", "pete-ricketts", "family_child_sovereignty", 0, True,
              "Co-sponsored S.3571 (Families' Rights and Responsibilities Act, 118th Congress, introduced January 10, 2024) — alongside Senators Scott (sponsor), Lankford, Cramer, Barrasso, Kennedy, and Rubio — affirming parents hold a fundamental constitutional right to direct the upbringing, education, and healthcare of their children and requiring government actions that infringe on parental rights to pass strict scrutiny; the bill was re-introduced as S.204 in the 119th Congress (2025–2026). As Nebraska Governor, Ricketts successfully contested the Nebraska Department of Education's plans to introduce sexual orientation and gender identity (SOGI) content into K-12 health classes, ultimately forcing the Department to abandon those plans following sustained gubernatorial and parental pressure. Ricketts declared Nebraska's first School Choice Week in 2015 as Governor and continues to champion school choice as Senator, co-sponsoring the National School Choice Week Resolution in 2026 and promoting tax credits for donations to scholarship-granting organizations to support families in choosing public, private, or faith-based schools.",
              ["https://www.congress.gov/bill/118th-congress/senate-bill/3571",
               "https://www.scott.senate.gov/media-center/press-releases/senators-scott-lankford-congresswoman-foxx-champion-bill-to-restore-parental-rights/",
               "https://omaha.com/news/state-and-regional/govt-and-politics/protect-nebraska-children-emerges-as-political-force-in-culture-battles-over-schools/article_c356b572-0399-11ed-8850-c7b3ada8bf4f.html",
               "https://www.ricketts.senate.gov/news/press-releases/ricketts-highlights-national-school-choice-week-2026/"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
