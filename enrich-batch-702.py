#!/usr/bin/env python3
"""Enrichment batch 702: 5 Texas State Representatives (evidence_state → evidence_curated).

archetype_curated federal bucket is exhausted; targets taken from evidence_state
candidates at the bottom of the alphabet (TX). All five are sitting House Democrats
whose 2021-2025 voting records oppose the rubric on life, Second Amendment,
gender ideology, and parental rights.

Candidates: Mary Ann Perez (HD-144), Jon Rosenthal (HD-135), Jolanda Jones (HD-147),
Josey Garcia (HD-124), John Bucy III (HD-136).
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
    # --- Mary Ann Perez (TX D HD-144) ---
    ("mary-ann-perez", "TX", "State Representative", [
        claim("map1", "mary-ann-perez", "sanctity_of_life", 0, False,
              "Voted NO on SB 8 (87th Legislature, 2021) — the Texas Heartbeat Act banning abortion after detection of fetal cardiac activity at ~6 weeks. The bill passed 83–64; Perez was among the 64 opposing members, confirming rejection of life-at-conception protections. She is endorsed by Planned Parenthood Texas Votes.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://choicetracker.org/tx/people/mary-ann-perez/"]),
        claim("map2", "mary-ann-perez", "self_defense", 0, False,
              "Voted NO on HB 1927 (87th Legislature, 2021) — the Texas Firearms Carry Act restoring constitutional/permitless carry of handguns for eligible adults. The bill passed 87–58; Perez opposed expanding the right to carry without a government-issued license, reflecting opposition to constitutional carry.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://freedomindex.us/legislator/11142"]),
        claim("map3", "mary-ann-perez", "family_child_sovereignty", 0, False,
              "Voted NO on HB 900 (88th Legislature, 2023) — the READER Act requiring book vendors to rate materials for sexually explicit content and prohibiting such content in school libraries. The bill passed 95–52; Perez opposed the measure to shield children from explicit school library materials.",
              ["https://thetexan.news/house-democrats-divided-on-bill-to-remove-explicit-books-from-school-libraries/",
               "https://capitol.texas.gov/BillLookup/History.aspx?LegSess=88R&Bill=HB900"]),
    ]),

    # --- Jon Rosenthal (TX D HD-135) ---
    ("jon-rosenthal", "TX", "State Representative", [
        claim("jr1", "jon-rosenthal", "sanctity_of_life", 0, False,
              "Voted NO on SB 8 (87th Legislature, 2021) — the Texas Heartbeat Act prohibiting abortion after ~6 weeks of pregnancy. The bill passed 83–64; Rosenthal, endorsed by Planned Parenthood, opposed the measure and the life-at-conception standard it reflects. Texas Alliance for Life rated him 45% in 2025.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://choicetracker.org/tx/people/jon-rosenthal/88342528"]),
        claim("jr2", "jon-rosenthal", "self_defense", 0, False,
              "The NRA-ILA explicitly named Rosenthal for voting against nine of twelve pro-Second Amendment laws that took effect September 1, 2021, including HB 1927 (constitutional/permitless carry). He holds an F rating from the Texas State Rifle Association and is endorsed by Gun Sense Voter.",
              ["https://www.nraila.org/articles/20210901/a-dozen-new-pro-second-amendment-laws-take-effect-today-your-state-representative-jon-rosenthal-voted-against-nine-of-them",
               "https://capitol.texas.gov/billlookup/History.aspx?LegSess=87R&Bill=HB1927"]),
        claim("jr3", "jon-rosenthal", "biblical_marriage", 2, False,
              "Voted NO on SB 14 (88th Legislature, 2023) banning puberty blockers and cross-sex hormones for minors, and NO on HB 229 (89th Legislature, 2025) defining sex as strictly biological for state records. He was named a 2025 Houston Pride Grand Marshal, reflecting active promotion of transgender ideology.",
              ["https://www.texastribune.org/2023/05/12/texas-trans-kids-health-care-ban/",
               "https://en.wikipedia.org/wiki/Texas_House_Bill_229"]),
    ]),

    # --- Jolanda Jones (TX D HD-147) ---
    ("jolanda-jones", "TX", "State Representative", [
        claim("jj1", "jolanda-jones", "sanctity_of_life", 0, False,
              "A vocal abortion-rights advocate who declared during 2025 Texas House debate: 'I will never stop working to restore abortion rights to make sure women — not politicians — make their own healthcare decisions.' She rejects any state protection of unborn life and opposes all abortion restrictions.",
              ["https://www.texastribune.org/2025/04/11/texas-abortion-law-lethal-fetal-anomalies/"]),
        claim("jj2", "jolanda-jones", "biblical_marriage", 2, False,
              "Texas's first openly lesbian Black state representative; testified against HB 1686 (2023) — the House companion to SB 14 — in committee, invoking personal LGBTQ identity to oppose the ban on gender-affirming procedures for minors. Voted NO on SB 14 (88th Legislature, 2023), which passed 87–56.",
              ["https://www.texastribune.org/2023/03/24/texas-legislature-transgender-health-care/",
               "https://capitol.texas.gov/BillLookup/History.aspx?Bill=SB14&LegSess=88R"]),
        claim("jj3", "jolanda-jones", "family_child_sovereignty", 0, False,
              "Voted FOR the Herrero amendment (April 6, 2023) blocking state funds from private-school vouchers, opposing all school-choice legislation and placing government control over schooling above parental sovereignty. Rated by ATPE (Texas teachers union) for consistent anti-school-choice votes.",
              ["https://teachthevote.atpe.org/Candidates/Jolanda-Jones"]),
    ]),

    # --- Josey Garcia (TX D HD-124) ---
    ("josey-garcia", "TX", "State Representative", [
        claim("jg1", "josey-garcia", "biblical_marriage", 2, False,
              "Voted NO on SB 14 (88th Legislature, 2023) banning puberty blockers and cross-sex hormones for minors. As an openly bisexual lawmaker (Air Force veteran, Bexar County) she was not among the four Democrats who crossed party lines, as confirmed by Texas Tribune and KXAN coverage of the 87–56 final vote.",
              ["https://www.texastribune.org/2023/05/12/texas-trans-kids-health-care-ban/",
               "https://www.kxan.com/news/texas-politics/texas-democrat-faces-censure-primary-challenger-after-vote-on-health-care-ban-for-transgender-minors/"]),
        claim("jg2", "josey-garcia", "sanctity_of_life", 0, False,
              "Voted NO on SB 33 (89th Legislature, 2025) prohibiting cities from using taxpayer funds to finance abortion-related travel. The bill passed 89–57 with only 2 Democrat crossover votes; Garcia, representing San Antonio/Bexar County — the city specifically targeted by the bill — voted against restricting taxpayer-subsidized abortion access.",
              ["https://www.lifenews.com/2025/05/22/texas-house-votes-to-stop-san-antonio-from-funding-abortion-travel-with-tax-dollars/",
               "https://legiscan.com/TX/bill/SB33/2025"]),
        claim("jg3", "josey-garcia", "family_child_sovereignty", 0, False,
              "Publicly stated she was 'proud to have joined the bipartisan majority to defeat school vouchers' (88th Legislature, 2023) and voted NO on SB 2 (89th Legislature, 2025), the $10,000-per-student Education Savings Account program that passed 85–63. She consistently prioritizes government school systems over parental school choice.",
              ["https://sanantonioreport.org/profile/josey-garcia/",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
    ]),

    # --- John Bucy III (TX D HD-136) ---
    ("john-bucy-iii", "TX", "State Representative", [
        claim("jb1", "john-bucy-iii", "sanctity_of_life", 0, False,
              "Voted NO on SB 8 (87th Legislature, 2021) — the Texas Heartbeat Act; Texas Choice Tracker records additional votes against a medication abortion ban and a bill imposing criminal penalties on providers. Received a 43% rating from Texas Alliance for Life on the 89th Legislature (2025) scorecard, voting against the majority of pro-life measures.",
              ["https://choicetracker.org/tx/people/john-bucy-iii/88408064",
               "https://www.texasallianceforlife.org/89th-texas-lege-scorecard/"]),
        claim("jb2", "john-bucy-iii", "biblical_marriage", 2, False,
              "Voted NO on SB 14 (88th Legislature, 2023) banning gender-affirming medical interventions for minors (confirmed by iVoterGuide). Received a 0% rating from Texas Values Action on their 2023 Faith & Family Scorecard, indicating uniform opposition to legislation protecting children from gender ideology in schools and medical settings.",
              ["https://ivoterguide.com/candidate/23737/race/6701/election/1214",
               "https://txvaluesaction.org/legislator/john-bucy-iii/"]),
        claim("jb3", "john-bucy-iii", "self_defense", 0, False,
              "Maintains an explicit 'Gun Violence Prevention' priority page on his campaign website and votes against Second Amendment expansions in the Texas Legislature. Aligned with gun-control advocacy groups and opposed constitutional carry legislation.",
              ["https://bucyfortexas.com/priorities/gun-violence-prevention/",
               "https://legiscan.com/TX/bill/HB1927/2021"]),
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
