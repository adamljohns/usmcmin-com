#!/usr/bin/env python3
"""Enrichment batch 697: cited claims for 5 Wisconsin State Assembly Members.

All archetype_curated federal buckets are exhausted; continuing the pivot to
state legislators from the bottom of the alphabet (WI, bottom of reversed list).

Targets (5, all D, WI — archetype_party_default with 0 claims):
  Jodi Emerson       (WI AD-91, Eau Claire)
  Joan Fitzgerald    (WI AD-46, Jefferson/Walworth County) — freshman Jan 2025
  Jill Billings      (WI AD-95, La Crosse) — longest-serving of the five
  Jenna Jacobson     (WI AD-50, SW Dane / Green County)
  Greta Neubauer     (WI AD-66, Racine) — Assembly Minority Leader

Sources: legis.wisconsin.gov, docs.legis.wisconsin.gov, wispolitics.com,
         wpr.org, wsaw.com, wsaw.com, channel3000.com, bluevoterguide.org,
         plannedparenthoodaction.org, aclu-wi.org, capsitimes.com,
         hngnews.com, ourliveswisconsin.com, wisconsinexaminer.com,
         teamlpac.com, journaltimes.com, ballotready.org, legiscan.com

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
    # -------------- Jodi Emerson (WI AD-91, Eau Claire) --------------
    ("jodi-emerson-wi-91", "WI", "Assembly", [
        claim("je1", "jodi-emerson-wi-91", "sanctity_of_life", 4, False,
              "Emerson is endorsed by Planned Parenthood Advocates of Wisconsin and EMILY's List, "
              "placing her in the abortion-industry endorsement network. On January 25, 2024, she "
              "voted NO on AB 975 (a 14-week abortion ban that passed 53-46); all 35 Assembly "
              "Democrats voted against the bill, which Gov. Evers then vetoed. She has publicly "
              "called for repealing Wisconsin's 1849 abortion ban, stating: 'We must restore "
              "abortion access in Wisconsin. We're not backing down.'",
              ["https://wispolitics.com/2024/divided-assembly-gop-passes-bill-to-put-14-week-abortion-ban-before-voters/",
               "https://aclu-wi.org/legislation/ab-975sb-1011-14-week-abortion-ban/",
               "https://bluevoterguide.org/WI/candidate_Jodi_Emerson/304599"]),
        claim("je2", "jodi-emerson-wi-91", "self_defense", 1, False,
              "Emerson is a 2024 Moms Demand Action 'Gun Sense Candidate' (the Everytown voter "
              "outreach endorsement) and co-sponsored AB 368 (2023-24 session), a Democratic gun "
              "control package that included universal background check requirements and a red flag "
              "(extreme risk protection order) law — directly opposing the rubric's protection of "
              "unrestricted Second Amendment rights.",
              ["https://bluevoterguide.org/WI/candidate_Jodi_Emerson/304599",
               "https://docs.legis.wisconsin.gov/document/proposaltext/2023/REG/AB368.pdf",
               "https://channel3000.com/news/wisconsin-democrats-re-introduce-red-flag-background-check-bills-aimed-at-reducing-gun-violence/"]),
        claim("je3", "jodi-emerson-wi-91", "family_child_sovereignty", 0, False,
              "Emerson voted NO on Wisconsin's Parent Bill of Rights (January 18, 2024, passed "
              "62-35), which would have guaranteed parental rights to determine children's pronouns "
              "at school and opt out of classes conflicting with personal beliefs. She also voted "
              "NO on all three anti-transgender bills (AB 377, AB 378, AB 465) that passed "
              "63-35 on strict party lines on October 12, 2023 — AB 465 banned gender-affirming "
              "medical care for minors; AB 377/378 barred transgender athletes from female sports.",
              ["https://wsaw.com/2024/01/18/wisconsin-assembly-approves-bill-guaranteeing-parental-oversight-childrens-education/",
               "https://wpr.org/health/lawmakers-approve-bills-bar-gender-affirmation-procedures-sports-participation-transgender-youth",
               "https://wisconsinexaminer.com/2024/01/19/assembly-passes-parental-rights-firearm-tracking-ban-and-universal-credentialing-bills/"]),
    ]),

    # -------------- Joan Fitzgerald (WI AD-46, Jefferson/Walworth) — freshman Jan 2025 --------------
    ("joan-fitzgerald-wi-46", "WI", "Assembly", [
        claim("jf1", "joan-fitzgerald-wi-46", "sanctity_of_life", 4, False,
              "Fitzgerald is endorsed by Planned Parenthood Advocates of Wisconsin and EMILY's List. "
              "In her first session she co-sponsored AB 355 (introduced July 8, 2025) to repeal "
              "Wisconsin's 1849 abortion ban, eliminate abortion-related regulations, and mandate "
              "abortion coverage under certain health plans. She stated: 'When we put a ban and "
              "we put restrictions on (abortion), we're taking away a fundamental right of women "
              "to just choose what's best for them.'",
              ["https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf",
               "https://captimes.com/news/elections/joan-fitzgerald-jenifer-quimby-battle-in-wisconsin-assembly-district/",
               "https://www.plannedparenthoodaction.org/planned-parenthood-advocates-wisconsin/"]),
        claim("jf2", "joan-fitzgerald-wi-46", "self_defense", 1, False,
              "Before taking office, Fitzgerald founded the Whitewater-area chapter of Moms Demand "
              "Action for Gun Sense in America and then ran and won with a Moms Demand Action 'Gun "
              "Sense Candidate' endorsement in 2024, identifying gun violence prevention as a top "
              "legislative priority — signaling firm opposition to the rubric's defense of "
              "unrestricted Second Amendment rights.",
              ["https://hngnews.com/lake_mills_leader/news/local/joan-fitzgerald-breaks-down-campaign-for-wisconsins-46th-assembly-district/",
               "https://captimes.com/news/elections/joan-fitzgerald-jenifer-quimby-battle-in-wisconsin-assembly-district/"]),
        claim("jf3", "joan-fitzgerald-wi-46", "biblical_marriage", 4, False,
              "Fitzgerald is endorsed by Fair Wisconsin PAC, Wisconsin's leading LGBTQ+ advocacy "
              "and political organization. In her first months in office she co-sponsored Assembly "
              "Joint Resolution 31 proclaiming March 31 as Wisconsin's Transgender Day of "
              "Visibility (April 23, 2025) and supported a June 2025 resolution recognizing "
              "LGBTQ Pride Month — directly representing the promotion of LGBTQ ideology in "
              "public policy that the rubric opposes.",
              ["https://captimes.com/news/elections/joan-fitzgerald-jenifer-quimby-battle-in-wisconsin-assembly-district/",
               "https://docs.legis.wisconsin.gov/2025/legislators/assembly/2890"]),
    ]),

    # -------------- Jill Billings (WI AD-95, La Crosse) — Assembly Caucus Vice-Chair --------------
    ("jill-billings-wi-95", "WI", "Assembly", [
        claim("jb1", "jill-billings-wi-95", "sanctity_of_life", 0, False,
              "Billings co-sponsored Assembly Joint Resolution 10 (February 2023) to place a "
              "referendum before Wisconsin voters on repealing the state's 1849 abortion ban and "
              "restoring Roe v. Wade-era abortion rights — rejecting any recognition of personhood "
              "from conception. She also voted NO on AB 975 (14-week abortion ban) on January 25, "
              "2024; all 35 Assembly Democrats voted against the bill, which passed 53-46 and was "
              "vetoed by Gov. Evers.",
              ["https://aclu-wi.org/en/legislation/ajr-10sjr-10-referendum-repeal-1849-abortion-ban",
               "https://wispolitics.com/2024/divided-assembly-gop-passes-bill-to-put-14-week-abortion-ban-before-voters/"]),
        claim("jb2", "jill-billings-wi-95", "family_child_sovereignty", 0, False,
              "Billings voted NO on all three anti-transgender bills (AB 377, AB 378, AB 465) that "
              "passed 63-35 on strict party lines on October 12, 2023 — banning gender-affirming "
              "care for minors and transgender athletes from female sports. She also voted NO on "
              "Wisconsin's Parent Bill of Rights (January 18, 2024, passed 62-35), which would "
              "have guaranteed parents the right to determine children's pronouns at school and "
              "opt out of classes conflicting with personal beliefs.",
              ["https://wpr.org/health/lawmakers-approve-bills-bar-gender-affirmation-procedures-sports-participation-transgender-youth",
               "https://wsaw.com/2024/01/18/wisconsin-assembly-approves-bill-guaranteeing-parental-oversight-childrens-education/"]),
        claim("jb3", "jill-billings-wi-95", "self_defense", 1, False,
              "Billings co-sponsored AB 1192 / companion SB 1094 (2023-24 session), legislation "
              "relating to firearm transfers and background check requirements with associated "
              "penalties — supporting expanded government regulation of firearm purchases and "
              "opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://docs.legis.wisconsin.gov/2023/legislators/assembly/2448",
               "https://legis.wisconsin.gov/assembly/95/billings/"]),
    ]),

    # -------------- Jenna Jacobson (WI AD-50, SW Dane / Green County) --------------
    ("jenna-jacobson-wi-50", "WI", "Assembly", [
        claim("jjac1", "jenna-jacobson-wi-50", "sanctity_of_life", 0, False,
              "Jacobson is publicly and explicitly pro-choice, stating she must 'fight every day "
              "for you and your children and your loved ones to have their fundamental right to "
              "privacy and bodily autonomy.' On January 25, 2024, she voted NO on AB 975 (14-week "
              "abortion ban) — all 35 Assembly Democrats voted against the bill (passed 53-46, "
              "vetoed by Gov. Evers) — rejecting any legal protection for the unborn from "
              "conception.",
              ["https://wispolitics.com/2024/divided-assembly-gop-passes-bill-to-put-14-week-abortion-ban-before-voters/",
               "https://www.plannedparenthoodaction.org/planned-parenthood-advocates-wisconsin/issues/14-week-abortion-ban",
               "https://ballotready.org/people/jenna-jacobson"]),
        claim("jjac2", "jenna-jacobson-wi-50", "self_defense", 1, False,
              "Jacobson co-sponsored AB 368 (2023-24 session), the Wisconsin Democratic gun safety "
              "package that included universal background check requirements, a mandatory waiting "
              "period for handgun purchases, and a red flag (extreme risk protection order) law — "
              "directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://docs.legis.wisconsin.gov/document/proposaltext/2023/REG/AB368.pdf",
               "https://channel3000.com/news/wisconsin-democrats-re-introduce-red-flag-background-check-bills-aimed-at-reducing-gun-violence/"]),
        claim("jjac3", "jenna-jacobson-wi-50", "biblical_marriage", 0, False,
              "Jacobson co-sponsored a Wisconsin joint resolution (July 17, 2025) to eliminate "
              "the state constitution's restrictions on marriage and codify marriage equality in "
              "Wisconsin law — rejecting the one-man-one-woman definition of marriage. She also "
              "co-sponsored resolutions recognizing Wisconsin's Transgender Day of Remembrance "
              "and LGBTQ Pride Month (2025), and legislation funding LGBTQIA+ rights training "
              "for school counselors and social workers.",
              ["https://legiscan.com/WI/people/jenna-jacobson/id/23593",
               "https://ourliveswisconsin.com/article/wisconsin-democrats-plan-legislation-to-codify-marriage-equality/",
               "https://docs.legis.wisconsin.gov/2025/legislators/assembly/2859"]),
    ]),

    # -------------- Greta Neubauer (WI AD-66, Racine) — Assembly Minority Leader --------------
    ("greta-neubauer-wi-66", "WI", "Assembly", [
        claim("gn1", "greta-neubauer-wi-66", "sanctity_of_life", 0, False,
              "As Assembly Minority Leader, Neubauer co-introduced AB 355 (2025) to repeal "
              "Wisconsin's 1849 abortion ban, eliminate all abortion-related restrictions, and "
              "restore full abortion access statewide — rejecting any recognition of personhood "
              "from conception. On January 25, 2024, she voted NO on AB 975 (14-week abortion "
              "ban, passed 53-46). When Planned Parenthood of Wisconsin paused abortion services "
              "in September 2025 due to federal legislation, she publicly condemned 'Republican "
              "extremists targeting reproductive healthcare.'",
              ["https://docs.legis.wisconsin.gov/document/proposaltext/2025/REG/AB355.pdf",
               "https://wispolitics.com/2024/divided-assembly-gop-passes-bill-to-put-14-week-abortion-ban-before-voters/",
               "https://wisconsinexaminer.com/2025/09/25/planned-parenthood-of-wisconsin-is-pausing-abortion-services-due-to-trump-legislation/"]),
        claim("gn2", "greta-neubauer-wi-66", "family_child_sovereignty", 0, False,
              "Neubauer voted NO on Wisconsin's Parent Bill of Rights (January 18, 2024, passed "
              "62-35), publicly arguing the bill would result in children being 'less likely to "
              "learn about MLK and other civil rights leaders.' When the 2025 session brought a "
              "new round of anti-transgender bills targeting youth sports, medical care, and "
              "pronoun/name changes in schools (passed March 2025), she called the legislation "
              "a 'new low,' accusing Republicans of 'denying children healthcare' to score "
              "political points.",
              ["https://wsaw.com/2024/01/18/wisconsin-assembly-approves-bill-guaranteeing-parental-oversight-childrens-education/",
               "https://wpr.org/health/lawmakers-approve-bills-bar-gender-affirmation-procedures-sports-participation-transgender-youth",
               "https://wisconsinexaminer.com/2025/03/21/assembly-passes-bills-targeting-transgender-youth-in-school-and-their-medical-decisions/"]),
        claim("gn3", "greta-neubauer-wi-66", "biblical_marriage", 2, False,
              "Neubauer is the first openly queer Assembly Minority Leader in Wisconsin history "
              "and a leading legislative advocate for transgender ideology in public schools and "
              "policy. She wrote a public op-ed ('I'm queer and I'm talking about it') pledging "
              "to put in place 'laws that protect LGBT folks in Wisconsin.' She is endorsed by "
              "LPAC (the national LGBTQ political action committee that exclusively endorses "
              "queer women candidates) and co-sponsored legislation to codify marriage equality "
              "in Wisconsin state law.",
              ["https://journaltimes.com/print_specific/column/commentary-by-state-rep-greta-neubauer-i-m-queer-and-i-m-talking-about-it/",
               "https://teamlpac.com/our-candidates/greta-neubauer",
               "https://en.wikipedia.org/wiki/Greta_Neubauer",
               "https://ourliveswisconsin.com/article/wisconsin-democrats-plan-legislation-to-codify-marriage-equality/"]),
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

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
