#!/usr/bin/env python3
"""Enrichment batch 691: 3 cited claims each for 5 WA/VA federal candidates.

Targets from the bottom of the alphabet (WA, VA) — evidence_curated candidates
with 5 existing claims — adding 3 new claims each in previously uncovered rubric
categories. All claims cite verifiable public-record or candidate-questionnaire
sources (iVoterGuide, Ballotpedia, govtrack.us, local news, campaign websites).

Candidates:
  Joe Kent (WA-03, R)       — 2022/2024 R nominee, Army Special Forces veteran
  Carmen Goers (WA-08, R)   — 2024 R nominee, 2026 candidate, commercial banker
  Yesli Vega (VA-07, R)     — 2022 R nominee, Prince William Co. Supervisor
  Jerrod Sessler (WA-04, R) — 2026 R candidate, Navy veteran, NASCAR driver
  Darius Mayfield (VA-07, R) — 2026 R candidate, small businessman

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
    # -------------- Joe Kent (WA-03, R) --------------
    ("joe-kent", "WA", "WA-03", [
        claim("jk-bm2", "joe-kent", "biblical_marriage", 2, True,
              "On his 2022 and 2024 iVoterGuide candidate questionnaires, Kent stated he would "
              "'require that our public schools defend girls' sports and spaces from biological men,' "
              "opposing biological males competing in women's athletics or entering girls' locker "
              "rooms and other female-only spaces. He also wrote: 'We have removed God from "
              "classrooms and replaced Him with pride flags. There is an attempt to completely "
              "destroy our native values and we must preserve them by teaching students about our "
              "nation's founding principles and protecting students' and teachers' right to pray "
              "in schools.' He consistently opposed gender ideology in schools and public "
              "institutions as a top legislative priority.",
              ["https://ivoterguide.com/candidate/59650/race/2690/election/984",
               "https://ballotpedia.org/Joe_Kent_(Washington)"]),
        claim("jk-ei0", "joe-kent", "election_integrity", 0, True,
              "On his 2022 iVoterGuide questionnaire, Kent wrote: 'Everyone must be required to "
              "provide a photo ID and proof of citizenship before they vote. People should vote "
              "in person on paper ballots that are hand counted under the observation of all "
              "parties involved. Election officials should be able to establish a chain of custody "
              "for all ballots.' He also stated during the 2022 campaign that investigating the "
              "2020 general election and enacting new election integrity laws were among his top "
              "legislative priorities, and publicly raised concerns about Washington State's "
              "all-mail voting system allowing a window for irregularities.",
              ["https://ivoterguide.com/candidate/59650/race/2690/election/984",
               "https://ballotpedia.org/Joe_Kent_(Washington)"]),
        claim("jk-cl0", "joe-kent", "christian_liberty", 0, True,
              "On his 2022 iVoterGuide questionnaire, Kent wrote: 'I am a strong believer in "
              "religious freedom and think everyone's right to worship as they please should be "
              "protected. Religious liberty is at risk in the United States and deserves the "
              "highest level of protection in the law. We also must acknowledge that we are a "
              "nation of Judeo-Christian values and the children in our nation should be taught "
              "these values from a young age.' He also publicly opposed all COVID-19 vaccine "
              "mandates as violations of individual liberty, stating in a Fox News interview that "
              "mandates were 'taking away a lot of people's individual choice' and calling for "
              "legislation to make vaccine mandates illegal.",
              ["https://ivoterguide.com/candidate/59650/race/2690/election/984",
               "https://www.foxnews.com/politics/gop-congressional-candidate-joe-kent-vaccine-mandates"]),
    ]),

    # -------------- Carmen Goers (WA-08, R) --------------
    ("carmen-goers", "WA", "WA-08", [
        claim("cg-ei0", "carmen-goers", "election_integrity", 0, True,
              "On her 2024 iVoterGuide candidate questionnaire, Goers stated: 'Identification is "
              "required to maintain the integrity of our election process and ensure that only "
              "eligible Americans vote.' She supports photo ID requirements as a necessary safeguard "
              "for election integrity and ensuring that votes are cast only by eligible citizens.",
              ["https://ivoterguide.com/candidate/68720/race/2695/election/1247"]),
        claim("cg-cl0", "carmen-goers", "christian_liberty", 0, True,
              "On her 2024 iVoterGuide questionnaire, Goers identified as 'a Christian since my "
              "early teen years, with spiritual beliefs and values rooted in the teachings of the "
              "Bible and the life and ministry of Jesus Christ.' When asked whether individuals "
              "and businesses should be required to provide services even if it would violate their "
              "moral and/or religious beliefs, she answered No — affirming that faith-based "
              "conscientious objection deserves legal protection against compelled-service mandates. "
              "She also stated her core values include 'love, faith, hope, forgiveness, humility, "
              "service, integrity, peace, justice, and the sanctity of life.'",
              ["https://ivoterguide.com/candidate/68720/race/2695/election/1247"]),
        claim("cg-sd0", "carmen-goers", "self_defense", 0, False,
              "On her 2024 iVoterGuide questionnaire, Goers stated: 'The Second Amendment "
              "guarantees the right to bear arms; however, the Supreme Court has upheld that "
              "reasonable regulations are permissible, such as background checks and restrictions "
              "on felons and individuals with mental illness. I concur with these restrictions.' "
              "This position endorses background-check requirements as constitutional, falling "
              "short of the constitutional-carry standard that holds the right to bear arms "
              "shall not be infringed by preconditions such as registration or licensing.",
              ["https://ivoterguide.com/candidate/68720/race/2695/election/1247"]),
    ]),

    # -------------- Yesli Vega (VA-07, R) --------------
    ("yesli-vega", "VA", "VA-07", [
        claim("yv-bm0", "yesli-vega", "biblical_marriage", 0, True,
              "At a 2022 candidate forum, Vega stated: 'As a Christian, I support the traditional "
              "definition of marriage.' As a Prince William County Supervisor, she voted NO on "
              "amending county code to comply with Virginia's Values Act (which extended "
              "non-discrimination protections to LGBTQ residents) in June 2020, was one of only "
              "two supervisors to oppose the measure in a 5-2 board vote, and declined to support "
              "the board's 2020, 2021, and 2022 LGBTQ Pride Month proclamations — a consistent "
              "record of opposing government recognition of same-sex relationships and LGBTQ "
              "identity as protected legal categories.",
              ["https://vademocrats.org/news/yesli-vega-ted-cruz-want-to-see-same-sex-marriage-overturned/",
               "https://www.princewilliamtimes.com/news/supervisors-split-on-adding-lgbtq-protections-to-county-code/article_22aa76a4-baf8-11ea-8662-0f519f2c51e3.html"]),
        claim("yv-fc0", "yesli-vega", "family_child_sovereignty", 0, True,
              "Vega made parental rights over children's education and identity a central 2022 "
              "campaign theme. Co-campaigning with Tulsi Gabbard on an explicit parental-rights "
              "platform, she declared: 'I'm sick and tired of a government that is telling me "
              "how to lead my life, how to spend my money, and most importantly, how to raise "
              "my children!' She supported Gov. Youngkin's policy requiring parental notification "
              "when schools discuss children's gender identity, stating it 'gives parents in the "
              "know as to what is happening with their children.' She also publicly opposed CRT "
              "in public schools and stated 'Education doesn't start at school, it starts at "
              "home,' urging parents to advocate at school board meetings.",
              ["https://www.theepochtimes.com/us/tulsi-gabbard-joins-virginia-republican-challenger-on-campaign-trail-for-parental-rights-government-accountability-4814508",
               "https://wusa9.com/amp/article/news/politics/elections/yesli-vega-campaign-priorities-ahead-of-2022-midterm-election-virginia-7th-congressional-district/65-18354246-5e25-4c83-b116-1c929f44ea51"]),
        claim("yv-fp1", "yesli-vega", "foreign_policy_restraint", 1, True,
              "Appearing on the John Fredericks Show during the 2022 campaign, Vega stated that "
              "U.S. assistance to Ukraine 'has to end' — one of the clearest anti-Ukraine-aid "
              "positions taken by a Virginia congressional candidate that cycle. She co-campaigned "
              "with Tulsi Gabbard, an outspoken critic of U.S. military aid to Ukraine and of "
              "NATO expansion. Vega also used general anti-foreign-spending framing: 'We keep "
              "printing money that we don't have and sending money to all of these places when "
              "we have a great need here,' framing overseas commitments as incompatible with "
              "domestic priorities.",
              ["https://vademocrats.org/news/yesli-vega-to-campaign-with-putin-sympathizer-noted-homophobe-tulsi-gabbard/",
               "https://www.theepochtimes.com/us/tulsi-gabbard-joins-virginia-republican-challenger-on-campaign-trail-for-parental-rights-government-accountability-4814508"]),
    ]),

    # -------------- Jerrod Sessler (WA-04, R) --------------
    ("jerrod-sessler", "WA", "WA-04", [
        claim("js-bm2", "jerrod-sessler", "biblical_marriage", 2, True,
              "On his 2022 iVoterGuide questionnaire, Sessler wrote: 'Children are the most "
              "vulnerable members of society and must be protected from abuse, including gender "
              "ideology, grooming, and bodily mutilation.' He stated opposition to biological "
              "males participating in women's sports or occupying biological women's spaces "
              "including bathrooms, locker rooms, and shelters, and called for never using "
              "taxpayer funds to provide gender-transition services. He stated his intent to "
              "'ban CRT mythology and gender ideology fantasies in our school systems' if "
              "elected. A self-described 'Bible-believing Christian' whose 'faith in Jesus "
              "Christ has formed his opinions and values,' he has endorsed Trump, the House "
              "Freedom Caucus, and Gen. Michael Flynn.",
              ["https://ivoterguide.com/candidate/59654/race/2691/election/899",
               "https://ivoterguide.com/candidate/59654/race/2691/election/1247"]),
        claim("js-fc0", "jerrod-sessler", "family_child_sovereignty", 0, True,
              "On his 2022 iVoterGuide questionnaire, Sessler stated he supports school choice "
              "including 'voucher programs, tax credits, charter schools, private schools, and "
              "home schools,' and supports eliminating the U.S. Department of Education and "
              "returning educational control to states and communities. He has campaigned "
              "consistently on parental rights alongside election integrity and border security "
              "as his three core issues, and called for banning CRT and gender ideology from "
              "public school curricula as a legislative priority if elected.",
              ["https://ivoterguide.com/candidate/59654/race/2691/election/899",
               "https://sengov.com/candidates/jerrod-sessler-for-congress-in-2026/"]),
        claim("js-fp1", "jerrod-sessler", "foreign_policy_restraint", 1, True,
              "Sessler criticized Rep. Newhouse directly for voting for Ukraine military aid, "
              "framing it as prioritizing Ukraine's defense over the border-crime and fentanyl "
              "crisis at home. In a 2024 campaign video he stated the U.S. should 'refuse to "
              "involve ourselves in the pointless endless wars that the despotic elite globalists "
              "are pushing for in order to undermine American sovereignty,' and called for "
              "restricting U.S. involvement to training assistance only, not fighting other "
              "countries' wars. He further stated any foreign aid should be 'collateralized' "
              "rather than given as open-ended grants, and was described as 'isolationist' by "
              "Jewish Insider due to his stance on Ukraine and NATO commitments.",
              ["https://www.yoursourceone.com/south_sound/columbia_basin/newhouse-vote-for-ukraine-aid-draws-criticism-from-challenger-jerrod-sessler/article_bb0b15f0-9bbb-11ee-ad10-1789c2fad109.html",
               "https://jewishinsider.com/2024/10/jerrod-sessler-dan-newhouse-washington-gop-washington/"]),
    ]),

    # -------------- Darius Mayfield (VA-07, R) --------------
    ("darius-mayfield", "VA", "VA-07", [
        claim("dm-bm0", "darius-mayfield", "biblical_marriage", 0, True,
              "On his NJ-12 iVoterGuide candidate questionnaires (2022 and 2024 cycles), Mayfield "
              "stated: 'Marriage is a God-ordained, sacred and legal union of one man and one "
              "woman. No government has the authority to alter this definition.' He also stated "
              "opposition to federal or state taxpayer funding for abortion providers including "
              "Planned Parenthood. These positions, self-reported during his prior congressional "
              "campaigns in New Jersey, reflect the worldview he carries into the 2026 VA-07 race.",
              ["https://ivoterguide.com/candidate/66350/race/6829/election/1112",
               "https://ivoterguide.com/candidate/66350/race/6829/election/949"]),
        claim("dm-ei0", "darius-mayfield", "election_integrity", 0, True,
              "On his NJ-12 iVoterGuide questionnaire, Mayfield stated: 'I support voter photo "
              "ID.' He also expressed skepticism about the 2020 election outcome in a "
              "since-deleted tweet, writing that Biden had won 'the FEWEST amount of counties "
              "of ANY President EVER but received the MOST votes ever,' calling the reported "
              "result implausible — a posture of 2020 election skepticism consistent with "
              "his pro-election-integrity platform carried into the 2026 VA-07 race.",
              ["https://ivoterguide.com/candidate/66350/race/6829/election/1112",
               "https://newjerseyglobe.com/congress/trump-republican-wants-to-take-on-watson-coleman/"]),
        claim("dm-cl0", "darius-mayfield", "christian_liberty", 0, True,
              "On his NJ-12 iVoterGuide questionnaire, Mayfield stated: 'Religious liberty is "
              "at risk in the United States and deserves the highest level of protection in the "
              "law.' He affirmed that individuals' and businesses' right of religious conscience "
              "should protect them from government-compelled participation in activities that "
              "violate their moral or religious beliefs — a position consistent with strong "
              "free-exercise protections for faith-based objections to government mandates.",
              ["https://ivoterguide.com/candidate/66350/race/6829/election/1112"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
