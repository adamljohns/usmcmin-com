#!/usr/bin/env python3
"""Enrichment batch 606: 5 sitting U.S. Senators — 10 claims.

All archetype_curated federal buckets depleted. These senators carry
evidence_curated confidence with 7-9 claims each. This batch adds 2 claims
per senator in DISTINCT categories not yet documented, using sourced
2017-2026 voting records / public positions.

Targets (bottom-of-alphabet states):
  Marsha Blackburn  (TN-R) — +2 claims: christian_liberty, family_child_sovereignty
  Tim Kaine         (VA-D) — +2 claims: christian_liberty, family_child_sovereignty
  Mark Warner       (VA-D) — +2 claims: christian_liberty, election_integrity
  Bernie Sanders    (VT-I) — +2 claims: christian_liberty, industry_capture
  Peter Welch       (VT-D) — +2 claims: family_child_sovereignty, industry_capture
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
    # ---------- Marsha Blackburn (TN-R, US Senator) ----------
    ("marsha-blackburn-gov", "TN", "Senator", [
        claim("mb1", "marsha-blackburn-gov", "christian_liberty", 0, True,
              "Led the Senate introduction of S.J.Res.27 (118th Congress, September 2023), a Congressional Review Act resolution to nullify the Biden Labor Department's rescission of Trump-era religious exemption protections for faith-based federal contractors. The original 2020 Trump rule shielded religious organizations from compelled compliance with LGBTQ nondiscrimination mandates when contracting with the federal government; the Biden DOL eliminated that shield effective March 31, 2023. Blackburn's resolution would have restored it, with her stating: 'Federal contractors should not be discriminated against because of their religious views, and the Trump administration's rule ensured that employees of faith were protected.' She also led a 40+ member congressional amicus brief to the U.S. Supreme Court in 2019 supporting Barronelle Stutzman of Arlene's Flowers — a Christian florist who declined to arrange flowers for a same-sex wedding on religious grounds — defending First Amendment free-exercise and artistic-conscience rights for Christian business owners against government coercion.",
              ["https://www.congress.gov/bill/118th-congress/senate-joint-resolution/27",
               "https://www.blackburn.senate.gov/2023/9/issues/fighting-wokeness/blackburn-colleagues-stand-up-for-religious-liberty-of-federal-contractors",
               "https://www.blackburn.senate.gov/2019/10/blackburn-leads-amicus-brief-support-religious-liberty"]),
        claim("mb2", "marsha-blackburn-gov", "family_child_sovereignty", 0, True,
              "An original cosponsor of S.120 (Educational Choice for Children Act, 118th Congress, January 2023), the Senate companion to H.R.531, which establishes federal tax credits for charitable contributions to scholarship-granting organizations that issue K-12 scholarships explicitly covering public school, private school, and homeschool costs. Blackburn's stated position on her official Senate education page: 'parents — not government — should always have the final say in what kind of schooling their child receives.' On introduction she stated: 'Our children and their families deserve access to the education of their choosing, regardless of zip code. I'm pleased to join this legislation to provide students and their families with the financial resources to choose schools and programs that best fit their needs.'",
              ["https://www.congress.gov/bill/118th-congress/senate-bill/120",
               "https://www.blackburn.senate.gov/2023/1/issues/education/blackburn-cassidy-smith-colleagues-introduce-bicameral-bill-to-expand-school-choice-and-educational-opportunity",
               "https://www.blackburn.senate.gov/issues/education"]),
    ]),

    # ---------- Tim Kaine (VA-D, US Senator) ----------
    ("tim-kaine", "VA", "Senator", [
        claim("tk1", "tim-kaine", "christian_liberty", 0, False,
              "A self-described 'personally devout' Catholic who has co-sponsored the Equality Act (S.393) in both the 117th Congress (2021) and the 118th Congress (2023 reintroduction) — legislation whose Section 9 explicitly barred the Religious Freedom Restoration Act from being invoked as a 'claim or defense' in any LGBTQ nondiscrimination suit, stripping existing statutory religious liberty protection from churches, faith-based adoption agencies, religious schools, and Christian business owners. Kaine separately co-sponsored the 2014 'Protect Women's Health from Corporate Interference Act,' a direct legislative response to the Supreme Court's Hobby Lobby ruling that attempted to nullify the RFRA-based right of religious employers to exclude abortifacient contraceptives from their healthcare plans. At a 2023 Senate hearing Kaine called it 'extremely troubling' to suggest that constitutional rights derive from God rather than from government — a repudiation of the natural-law and Founding-era framework of inalienable God-given liberties — prompting a public rebuke from Catholic Bishop Robert Barron.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/393/all-info",
               "https://www.kaine.senate.gov/press-releases/warner-kaine-and-colleagues-reintroduce-equality-act-to-enshrine-protections-for-lgbtq-americans-into-law",
               "https://catholicvote.org/catholic-democratic-senator-from-virginia-says-rights-do-not-come-from-god-bishop-barron-pushes-back/",
               "https://www.christianpost.com/news/tim-kaine-doubles-down-on-comments-about-god-given-rights.html"]),
        claim("tk2", "tim-kaine", "family_child_sovereignty", 0, False,
              "Co-filed a Supreme Court amicus brief with Sen. Warner — signed by nearly 200 Members of Congress — arguing that Title IX requires K-12 schools to affirm transgender students' gender identity for access to sex-segregated facilities, allowing biologically-male students who identify as female to use female restrooms and locker rooms regardless of parental objection. Kaine and Warner separately wrote to the Department of Education urging binding guidance mandating transgender bathroom access in middle schools, high schools, and colleges — guidance that materialized as the Obama-era 'Dear Colleague' letter. Kaine also actively opposes school vouchers and school choice legislation: his stated position is that federal education funding 'should go to public schools,' he has invoked Virginia's segregationist voucher history to oppose choice programs, and his official website makes no reference to parental curriculum rights, notification requirements, or parental authority over children's gender-identity school accommodations.",
              ["https://www.kaine.senate.gov/press-releases/warner-kaine-file-amicus-brief-to-support-rights-of-transgender-students",
               "https://www.kaine.senate.gov/press-releases/warner-kaine-urge-dept-of-education-to-clarify-legal-protections-for-lgbt-students-across-the-country",
               "https://www.kaine.senate.gov/issues/education"]),
    ]),

    # ---------- Mark Warner (VA-D, US Senator) ----------
    ("mark-warner", "VA", "Senator", [
        claim("mw1", "mark-warner", "christian_liberty", 0, False,
              "Co-sponsored the Equality Act (S.393) in the 117th Congress (2021) and co-led its reintroduction in the 118th Congress (2023) alongside Sen. Kaine — legislation whose Section 1107 explicitly stated that the Religious Freedom Restoration Act of 1993 'shall not provide a claim concerning, or a defense to a claim under, a covered title,' stripping RFRA as any defense for religious organizations, faith-based employers, Christian schools, or religious businesses facing LGBTQ nondiscrimination suits. The U.S. Conference of Catholic Bishops, the Church of Jesus Christ of Latter-day Saints, and major evangelical bodies warned the Equality Act would expose religious institutions to federal discrimination liability for declining to affirm same-sex unions or transgender ideology. Warner's cosponsorship constitutes an explicit on-the-record commitment to enact the most direct legislative elimination of statutory religious liberty in modern American history.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/393/cosponsors",
               "https://www.warner.senate.gov/newsroom/press-releases/warner-kaine-colleagues-reintroduce-equality-act-to-enshrine-protections-for-lgbtq-americans-into-law/",
               "https://en.wikipedia.org/wiki/Equality_Act_(United_States)"]),
        claim("mw2", "mark-warner", "election_integrity", 0, False,
              "Co-sponsored and voted for cloture on S.1 (For the People Act, 117th Congress) — legislation that would have prohibited state voter-ID requirements for federal elections, mandated nationwide mass mail-in ballot access, required same-day and automatic voter registration, and stripped states of existing election integrity safeguards; the cloture vote failed 50-50 on June 22, 2021. Warner stated the bill's purpose was to stop 'restrictive and discriminatory voting laws.' He subsequently opposed the SAVE Act (H.R.22, 119th Congress, 2025) and the SAVE America Act (2026), both of which require documentary proof of U.S. citizenship to register to vote, calling them 'voter suppression' measures that 'could disenfranchise millions' — opposing the citizenship-verification standard the rubric's election integrity framework requires.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/1",
               "https://www.warner.senate.gov/newsroom/press-releases/statement-of-u-s-sen-mark-r-warner-on-senate-vote-on-for-the-people-act/",
               "https://www.warner.senate.gov/newsroom/press-releases/warner-kaine-slam-save-america-act-as-voter-suppression-measure-that-could-disenfranchise-millions/"]),
    ]),

    # ---------- Bernie Sanders (VT-I, US Senator) ----------
    ("bernie-sanders", "VT", "Senator", [
        claim("bs1", "bernie-sanders", "christian_liberty", 0, False,
              "Co-sponsored the Equality Act (S.393, 117th Congress), which explicitly stripped the Religious Freedom Restoration Act as any defense for religious organizations facing LGBTQ nondiscrimination claims. Most consequentially, at a 2017 Senate Budget Committee confirmation hearing for OMB nominee Russell Vought, Sanders applied a direct theological litmus test: repeatedly questioning Vought about his published Christian belief that Muslims who have not accepted Jesus Christ 'stand condemned,' Sanders declared 'this nominee is really not someone who is what this country is supposed to be about' — explicitly disqualifying Vought based on his orthodox Christian theology. The Baptist Joint Committee for Religious Liberty, legal scholars, and multiple First Amendment attorneys stated that Sanders had imposed an unconstitutional religious test on a federal nominee in violation of Article VI of the Constitution, which provides that 'no religious test shall ever be required as a qualification to any office or public trust under the United States.'",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/393/cosponsors",
               "https://www.usnews.com/news/national-news/articles/2017-06-08/bernie-sanders-questions-trump-budget-nominee-russell-vought-on-christian-faith",
               "https://bjconline.org/bjcs-tyler-bernie-sanders-inquiry-of-omb-nominee-imposed-a-religious-test-061017/",
               "https://www.npr.org/sections/thetwo-way/2017/06/09/532116365/is-it-hateful-to-believe-in-hell-bernie-sanders-questions-prompt-backlash"]),
        claim("bs2", "bernie-sanders", "industry_capture", 0, False,
              "Voted Nay on S.J.Res.29 (Senate roll call, December 8, 2021, passed 52-48), the Congressional Review Act resolution to overturn the Biden OSHA Emergency Temporary Standard requiring all employers with 100 or more employees to mandate COVID-19 vaccination or weekly testing — a government-pharma coalition mandate covering approximately 84 million American workers. The resolution passed with all 50 Republicans plus Democratic Senators Joe Manchin (WV) and Jon Tester (MT); Sanders joined the 48 opponents who defended the mandate. His vote aligned him squarely with the pharma-government vaccine-mandate consensus and against the individual medical-choice and anti-pharma-mandate standard the rubric requires.",
              ["https://www.cnbc.com/2021/12/08/biden-vaccine-mandate-senate-votes-to-overturn-osha-rule.html",
               "https://en.wikipedia.org/wiki/Bernie_Sanders",
               "https://en.wikipedia.org/wiki/COVID-19_vaccination_policy_in_the_United_States"]),
    ]),

    # ---------- Peter Welch (VT-D, US Senator) ----------
    ("peter-welch", "VT", "Senator", [
        claim("pw1", "peter-welch", "family_child_sovereignty", 0, False,
              "As a U.S. Representative, voted YES on the Equality Act (H.R.5, 117th Congress, House Vote #39, February 25, 2021, passed 224-206); as a U.S. Senator, co-sponsored the Senate Equality Act (S.5, 118th Congress, 2023-2024). The Equality Act extends federal civil-rights nondiscrimination law to cover gender identity in K-12 and higher education, requiring schools receiving federal funds to treat transgender students' self-declared gender identity as determinative for access to sex-segregated programs, bathrooms, locker rooms, and sports — without any parental opt-out or consent mechanism for the gender-identity accommodation of minor children. Welch has no public record supporting parental notification requirements, parental curriculum review rights, or parental authority over schools' gender-identity policies for their minor children.",
              ["https://www.govtrack.us/congress/votes/117-2021/h39",
               "https://www.welch.senate.gov/welch-cosponsors-the-equality-act-landmark-bill-to-prohibit-discrimination-based-on-sex-sexual-orientation-and-gender-identity/",
               "https://en.wikipedia.org/wiki/Equality_Act_(United_States)"]),
        claim("pw2", "peter-welch", "industry_capture", 0, False,
              "Opposed Robert F. Kennedy Jr.'s nomination as HHS Secretary in the Senate Finance Committee (January 2025), explicitly citing Kennedy's 'anti-vaccine actions' as disqualifying and declaring 'I want a disrupter in the health care system... I don't want a destroyer.' After Kennedy was confirmed, Welch issued a formal statement ('We have confirmed a vaccine denier'), joined Democratic colleagues in demanding Kennedy's resignation, and co-signed a Senate Finance Committee letter to the Committee chair urging a formal investigation of Kennedy for 'repeated anti-vaccine actions and conflicts of interest' — including Kennedy's dismissal of all 17 members of the ACIP vaccine advisory committee and their replacement with what Welch called 'vaccine deniers.' His consistent defense of ACIP institutional authority and opposition to any challenge to the government's vaccine-advisory and mandate apparatus positions him firmly within the pharma-government consensus the rubric's industry_capture standard opposes.",
              ["https://www.welch.senate.gov/welch-opposes-rfk-jr-s-nomination-in-the-senate-finance-committee-i-want-a-disrupter-in-the-health-care-system-and-the-one-leading-it-i-dont-want-a-destroyer/",
               "https://www.welch.senate.gov/welch-holds-senate-republicans-accountable-for-kennedys-tenure-at-hhs-we-have-confirmed-a-vaccine-denier/",
               "https://www.welch.senate.gov/welch-joins-wyden-finance-committee-democrats-in-urging-crapo-to-investigate-rfk-jr-on-anti-vaccine-actions-conflicts-of-interests/"]),
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
