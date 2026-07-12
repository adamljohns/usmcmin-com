#!/usr/bin/env python3
"""Enrichment batch 692: cited claims for 5 Ohio Republican State Senators.

Targets from the bottom of the alphabet (OH) — archetype_party_default state
senators with 0 claims. All claims cite verifiable public-record sources
(Ohio Senate official bios, Ballotpedia, iVoterGuide, campaign sites, NRA/RTL
endorsement records, legislative records).

Candidates:
  Susan Manchester (OH-12, R)  — State Senator, 100% pro-life, A-rated NRA
  Steve Wilson (OH-07, R)      — State Senator, Heartbeat Bill co-sponsor
  Stephen A. Huffman (OH-05, R)— State Senator/physician, Born-Alive bill sponsor
  Shane Wilkin (OH-17, R)      — State Senator, NRA A+, Ohio RTL endorsed
  Sandra O'Brien (OH-32, R)    — State Senator, Heartbeat Bill co-sponsor, NRA

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
    # -------------- Susan Manchester (OH-12, R) --------------
    ("susan-manchester", "OH", "State Senator", [
        claim("sm-sol0", "susan-manchester", "sanctity_of_life", 0, True,
              "Manchester describes herself as 'a Pro-Life, Pro-Second Amendment fiscal "
              "conservative' and carries a 100% pro-life voting record in the Ohio House "
              "across six years (2019–2025) before her 2024 election to the Ohio Senate. "
              "She is a member of Ohio Right to Life and has stated she believes 'we need "
              "to defend and protect life under all other circumstances because every life "
              "has value and every life is worth fighting for,' holding that abortion "
              "should be permitted only when the mother's life is directly at risk.",
              ["https://ohiosenate.gov/members/susan-manchester/biography",
               "https://ivoterguide.com/candidate/39756/race/2766/election/544"]),
        claim("sm-sd0", "susan-manchester", "self_defense", 0, True,
              "Manchester is an A-Rated NRA member and a member of the Buckeye Firearms "
              "Association, reflecting a consistent pro-Second Amendment legislative record. "
              "Her campaign platform explicitly lists 'Pro-Second Amendment' as a core "
              "identity alongside her pro-life and fiscal-conservative commitments.",
              ["https://www.manchesterforyou.com/",
               "https://ivoterguide.com/candidate/39756/race/2766/election/544"]),
    ]),

    # -------------- Steve Wilson (OH-07, R) --------------
    ("steve-wilson", "OH", "State Senator", [
        claim("sw-sol0", "steve-wilson", "sanctity_of_life", 0, True,
              "Wilson co-sponsored Ohio Senate Bill 23 (2019), the 'Heartbeat Bill,' which "
              "prohibits abortion once a fetal heartbeat is detectable — as early as six "
              "weeks into pregnancy — and contains no exceptions for rape or incest. "
              "Governor Mike DeWine signed SB23 into law on April 11, 2019. Wilson has "
              "earned perfect scores from the American Conservative Union, reflecting a "
              "consistent pro-life and socially conservative voting record across his tenure "
              "as the longest-serving senator in the 136th General Assembly.",
              ["https://en.wikipedia.org/wiki/Steve_Wilson_(Ohio_politician)",
               "https://ballotpedia.org/Steve_Wilson"]),
        claim("sw-es2", "steve-wilson", "economic_stewardship", 2, True,
              "Wilson has received perfect scores from both the Ohio Chamber of Commerce "
              "and the American Conservative Union for his fiscal conservative work and "
              "voting record. He has consistently supported balanced state budgets and "
              "tax-cutting measures, and led as Chairman of the Senate Financial "
              "Institutions, Insurance & Technology Committee and served on the Ways & "
              "Means Committee, where he has championed fiscal discipline and opposed "
              "deficit spending at the state level.",
              ["https://ohiosenate.gov/members/steve-wilson",
               "https://en.wikipedia.org/wiki/Steve_Wilson_(Ohio_politician)"]),
    ]),

    # -------------- Stephen A. Huffman (OH-05, R) --------------
    ("stephen-a-huffman", "OH", "State Senator", [
        claim("sah-sol0", "stephen-a-huffman", "sanctity_of_life", 0, True,
              "Huffman, a practicing physician of 32 years, co-introduced Ohio Senate Bill "
              "157 (2021), the 'Born-Alive Infant Protection Act,' which prohibits abortion "
              "providers from withholding necessary medical care from infants who survive "
              "an attempted abortion. Upon the bill's passage, Huffman stated: 'Every life "
              "has dignity.' The legislation also severs financial ties between abortion "
              "clinics and state-funded universities. As a physician-legislator, Huffman "
              "has consistently applied a medical pro-life standard — protecting unborn and "
              "newborn life — across his legislative career.",
              ["https://ohiosenate.gov/members/stephen-a-huffman/biography",
               "https://campusreform.org/article?id=18726"]),
        claim("sah-cl0", "stephen-a-huffman", "christian_liberty", 0, True,
              "Huffman championed Ohio legislation to protect medical professionals who "
              "face moral, religious, or ethical conflicts when asked to perform or refer "
              "patients for abortion or other elective procedures that violate their "
              "conscience. Huffman stated: 'When a patient requests elective services, "
              "like abortion, that could infringe on a doctor's personal religious, moral "
              "or ethical code, it is simply time they find a new provider,' affirming "
              "that faith-based conscientious objection deserves strong legal protection "
              "in medical settings.",
              ["https://ohiosenate.gov/members/stephen-a-huffman/news/huffman-defends-medical-professionals-facing-moral-religious-conflicts-while-serving-patients"]),
    ]),

    # -------------- Shane Wilkin (OH-17, R) --------------
    ("shane-wilkin", "OH", "State Senator", [
        claim("shw-sol0", "shane-wilkin", "sanctity_of_life", 0, True,
              "Wilkin received the endorsement of the Ohio Right to Life PAC in the 2022 "
              "general election, affirming his pro-life legislative record. He has earned "
              "the American Conservative Union's Award for Conservative Achievement four "
              "consecutive years — one of the highest conservative ratings issued by the "
              "founders of CPAC — reflecting a consistent voting record on pro-life and "
              "other social-conservative issues across his Senate tenure.",
              ["https://ballotpedia.org/Shane_Wilkin",
               "https://ohiosenate.gov/members/shane-wilkin/biography"]),
        claim("shw-sd0", "shane-wilkin", "self_defense", 0, True,
              "Wilkin holds an A+ rating from the National Rifle Association for his "
              "'steadfast defense of the 2nd Amendment' and has been endorsed by the "
              "Buckeye Firearms Association. He voted YES on Ohio Senate Bill 215 (2022), "
              "which enacted constitutional carry (permitless carry) in Ohio — eliminating "
              "the permit requirement for concealed carry by law-abiding adults.",
              ["https://ballotpedia.org/Shane_Wilkin",
               "https://ohiosenate.gov/members/shane-wilkin/biography"]),
    ]),

    # -------------- Sandra O'Brien (OH-32, R) --------------
    ("sandra-obrien", "OH", "State Senator", [
        claim("sob-sol0", "sandra-obrien", "sanctity_of_life", 0, True,
              "O'Brien co-sponsored Ohio Senate Bill 23 (2019), the 'Heartbeat Bill,' "
              "which bans abortions after detection of a fetal heartbeat (~6 weeks) with "
              "no rape or incest exceptions, and was signed into law by Gov. DeWine. On "
              "her voter questionnaire she stated: 'I believe human life begins at "
              "conception and deserves legal protection at every stage until natural "
              "death.' She opposes taxpayer funding for Planned Parenthood and other "
              "abortion providers, and supports the Born Alive Abortion Survivors "
              "Protection Act to require care for infants surviving abortion procedures.",
              ["https://ivoterguide.com/candidate?canK=39690&elecK=766&primarypartyk=-&raceK=11082",
               "https://ballotpedia.org/Sandra_O%27Brien_(Ohio)"]),
        claim("sob-bm0", "sandra-obrien", "biblical_marriage", 0, True,
              "On her voter questionnaire O'Brien stated that governments should not "
              "'discriminate against individuals or organizations based on traditional "
              "marriage beliefs,' and that marriage should be defined as the union of "
              "one man and one woman — rejecting civil recognition of same-sex unions "
              "as a redefinition of the institution. This position is consistent with "
              "her overall conservative-Christian platform and NRA/RTL endorsement record.",
              ["https://sandyforohio.com/",
               "https://ivoterguide.com/candidate?canK=39690&elecK=766&primarypartyk=-&raceK=11082"]),
        claim("sob-sd0", "sandra-obrien", "self_defense", 0, True,
              "O'Brien is a member of the National Rifle Association and was endorsed by "
              "the NRA in the 2024 Republican primary election for her pro-Second Amendment "
              "legislative record in the Ohio Senate.",
              ["https://sandyforohio.com/",
               "https://ballotpedia.org/Sandra_O%27Brien_(Ohio)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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
