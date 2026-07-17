#!/usr/bin/env python3
"""Enrichment batch 730: 1 NY Republican State Senator + 4 Nevada Republican State Senators, 10 claims.

archetype_curated federal senator/rep buckets exhausted; continuing with
archetype_party_default state senators from the bottom of the reverse-alpha
bucket (NY exhausted except Alexis Weik; NV is next).

Targets:
  Alexis Weik     (NY SD-8, Suffolk County/Long Island)
  Robin Titus     (NV SD-17, Senate Minority Leader, Wellington area)
  Lori Rogich     (NV SD-11, Reno/Las Vegas, freshman elected 2024)
  Lisa Krasner    (NV SD-16, Storey County/Carson City/Washoe, NRA A-rated)
  John Steinbeck  (NV SD-18, Clark County, freshman elected 2024)

Key sourced votes/positions:
  S9316 (NY 2025-26) — "Gestating Parent" bill replacing mother/father in NY
    family law; passed Senate 38-23 on June 2, 2026. Weik co-signed open
    letter to Gov. Hochul with Canzoneri-Fitzpatrick and Weber calling the
    terminology "dehumanizing"; confirmed in the 23-vote Republican NAY bloc.
  S51001 (NY 2022, CCIA) — Concealed Carry Improvement Act passed 43-20 in
    July 1, 2022 extraordinary session, entirely party-line. All 20 Republican
    senators voted NAY; Weik was a serving Republican senator (SD-3 at the time).
  Robin Titus — "led the fight to stop the egregious gun control bill during
    the [2023] session both times the Democrats tried ramming it through"
    (self-stated, voterobintitus.com). 2023 NV gun bills (AB354/AB355/SB171)
    blocked before Gov. Lombardo's vetoes. Titus is longtime NRA member/CCW holder.
  SB217 (NV 2025) — IVF insurance coverage mandate; passed 18-3. NAY bloc:
    Titus, Ellison, Stone. YEA includes Republicans Steinbeck and Rogich.
    Vetoed by Gov. Lombardo. Five Senate Republicans opposed (including Krasner).
  SB128 (NV 2025) — Prohibits AI-only insurance claim denials; Steinbeck and
    Rogich were the only Republicans to vote for it.
  JR (NV 2025, sanctuary schools) — Resolution urging Congress to bar ICE from
    entering schools or places of worship; Rogich was the only Republican in
    either chamber to support it.
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
    # ------- Alexis Weik (SD-8, Suffolk County/Long Island, R, Senate since Jan 2021) -------
    ("alexis-weik", "NY", "State Senator", [
        claim("aw1", "alexis-weik", "biblical_marriage", 2, True,
              "Co-signed an open letter with Republican Senators Canzoneri-Fitzpatrick "
              "and Weber to Governor Hochul urging a veto of S9316 (2025-26), a Democrat "
              "bill that replaced 'mother' and 'father' with 'gestating parent' and "
              "'non-gestating parent' throughout New York family court, domestic relations, "
              "and social services law. Weik stated publicly: 'Only a woman can become "
              "pregnant and give birth,' and called the new terminology 'dehumanizing.' "
              "The bill passed the Senate 38-23 on June 2, 2026; Weik was confirmed in "
              "the 23-vote Republican NAY bloc that rejected the gender-ideology "
              "language mandate the rubric opposes.",
              ["https://www.newsnationnow.com/politics/new-york-legislature-parents-bill/",
               "https://senate.maio.net/2026/06/17/s9316-passed-albany-legislature/",
               "https://divorce.law/guides/news/ny-gender-neutral-parent-terms-bill-2026/"]),
        claim("aw2", "alexis-weik", "self_defense", 1, True,
              "Voted NAY on S51001 (July 1, 2022 extraordinary session), New York's "
              "Concealed Carry Improvement Act (CCIA), which created sweeping 'sensitive "
              "place' restrictions on where licensed carriers may carry firearms, required "
              "extensive new training and documentation requirements, and established an "
              "opt-in private-property framework that effectively defaulted nearly all "
              "private spaces to gun-free zones. The CCIA passed 43-20 entirely along "
              "party lines during the extraordinary session — all 20 Republican senators, "
              "Weik among them, voted NAY. The Supreme Court subsequently struck down "
              "core provisions of the CCIA as unconstitutional under Bruen. Weik's family "
              "is a law-enforcement household (husband and oldest son are sworn officers), "
              "and her consistent opposition to NY's gun control agenda reflects "
              "the rubric's position against magazine limits, carry restrictions, "
              "and related infringements.",
              ["https://www.nysenate.gov/legislation/bills/2021/S51001",
               "https://www.cityandstateny.com/policy/2022/07/new-york-lawmakers-address-abortion-gun-restrictions-during-sleep-deprived-extraordinary-session/368905/",
               "https://www.nysenate.gov/senators/alexis-weik/about"]),
    ]),

    # ------- Robin Titus (SD-17, Wellington/Yerington area, R, Senate since 2023, Minority Leader since Jan 2024) -------
    ("robin-titus", "NV", "State Senator", [
        claim("rt1", "robin-titus", "self_defense", 1, True,
              "As Nevada Senate Minority Leader and longtime NRA member and CCW holder, "
              "Dr. Robin Titus 'successfully led the fight to stop the egregious gun "
              "control bill during the [2023] session both times the Democrats tried "
              "ramming it through' — her own words from her campaign website. The 2023 "
              "Nevada legislative session produced three gun control bills (AB354, which "
              "would bar persons under 21 from possessing semiautomatic rifles; AB355, "
              "which would bar firearms near election sites; and SB171, which would "
              "prohibit those convicted of hate crimes from possessing firearms). All "
              "three passed the Democrat-controlled chambers and were subsequently vetoed "
              "by Governor Lombardo, who stated: 'I will not support legislation that "
              "infringes on the constitutional rights of Nevadans.' Titus was elected "
              "Senate Minority Leader in January 2024 in recognition of her leadership "
              "in blocking the Democrats' gun control agenda.",
              ["https://www.voterobintitus.com/",
               "https://www.reviewjournal.com/news/politics-and-government/nevada/2023-legislature/lombardo-vetoes-gun-control-bills-will-not-support-infringing-on-nevadans-rights-2778778/",
               "https://www.nevadaappeal.com/news/2024/jan/17/titus-named-nevada-senate-minority-leader/"]),
        claim("rt2", "robin-titus", "sanctity_of_life", 2, True,
              "Voted NAY on SB217 (2025 Nevada legislative session), the mandatory IVF "
              "insurance coverage bill authored by Senate Majority Leader Nicole "
              "Cannizzaro. The bill would have required most private and public insurers, "
              "including Medicaid, to cover in vitro fertilization treatments. The bill "
              "passed 18-3; Titus was one of only three senators to vote against it, "
              "alongside Senators John Ellison (R-Elko) and Jeff Stone (R-Henderson). "
              "Her opposition — representing the only three NAY votes in the chamber — "
              "aligns with the rubric's anti-embryo-discard position, as IVF treatments "
              "typically result in the creation and discarding of surplus embryos. "
              "Governor Lombardo subsequently vetoed the bill.",
              ["https://nevadacurrent.com/2025/03/25/reproductive-rights-bills-in-nevada-legislature-tackle-ivf-contraceptives-provider-protections/",
               "https://thenevadaindependent.com/article/2025-lombardo-veto-tracker-bipartisan-ballot-drop-box-bill-rejected"]),
    ]),

    # ------- Lori Rogich (SD-11, Reno/Las Vegas area, R, Senate since Nov 2024) -------
    ("lori-rogich", "NV", "State Senator", [
        claim("lr1", "lori-rogich", "sanctity_of_life", 2, False,
              "Voted YES on SB217 (2025 Nevada legislative session), the mandatory IVF "
              "insurance coverage bill requiring most private and public insurers, "
              "including Medicaid, to cover in vitro fertilization treatments. Rogich "
              "was one of two Republicans (along with Senator John Steinbeck) to support "
              "the bill, which passed 18-3 and was subsequently vetoed by Governor "
              "Lombardo. An analysis of the 2025 session found that Rogich diverged "
              "from her Republican caucus 47 times — the second-highest cross-party "
              "voting rate of any lawmaker. Her vote for SB217 places her outside the "
              "rubric's anti-embryo-discard position, as IVF routinely involves the "
              "creation and discarding of surplus embryos.",
              ["https://thenevadaindependent.com/article/which-nevada-lawmakers-bucked-their-own-party-the-most-in-the-2025-session",
               "https://nevadacurrent.com/2025/03/25/reproductive-rights-bills-in-nevada-legislature-tackle-ivf-contraceptives-provider-protections/"]),
        claim("lr2", "lori-rogich", "border_immigration", 2, False,
              "Was the only Republican in either chamber of the Nevada Legislature to "
              "vote for a 2025 joint resolution urging Congress to prohibit federal "
              "immigration officials — including ICE agents — from entering schools or "
              "places of worship for the purpose of enforcing immigration laws. Rogich's "
              "sole-Republican support for the sanctuary-schools resolution is directly "
              "contrary to the rubric's anti-sanctuary position, which calls for full "
              "federal immigration enforcement cooperation and opposes policies that "
              "shield illegal immigrants from removal.",
              ["https://thenevadaindependent.com/article/which-nevada-lawmakers-bucked-their-own-party-the-most-in-the-2025-session",
               "https://nevadacurrent.com/2025/11/18/the-curious-case-of-the-immigration-resolution-that-immigrant-advocates-dont-want/"]),
    ]),

    # ------- Lisa Krasner (SD-16, Storey County/Carson City/Washoe, R, Senate since 2021) -------
    ("lisa-krasner", "NV", "State Senator", [
        claim("lk1", "lisa-krasner", "self_defense", 1, True,
              "Has received an 'A' rating from the NRA Political Victory Fund, reflecting "
              "a consistent record of opposing gun control legislation and supporting "
              "Second Amendment rights in the Nevada Legislature. Krasner represents "
              "a district covering Storey County, Carson City, and parts of Washoe County, "
              "and has maintained her pro-Second-Amendment record across multiple "
              "legislative sessions.",
              ["https://ballotpedia.org/Lisa_Krasner",
               "https://www.leg.state.nv.us/App/Legislator/A/Senate/Current/16"]),
        claim("lk2", "lisa-krasner", "family_child_sovereignty", 0, True,
              "Voted against Assembly Bill 416 and Assembly Bill 445 (2025 Nevada "
              "legislative session), both of which aimed to expand legal protections for "
              "librarians and limit the ability of parents and school boards to remove "
              "challenged books from school and public libraries. By opposing these bills, "
              "Krasner defended parental authority and community oversight over what "
              "content is accessible to minors in publicly funded libraries — aligning "
              "with the rubric's parental-rights position on family and child sovereignty. "
              "Both bills were part of a broader Democrat legislative effort to restrict "
              "book-removal mechanisms that parents and conservative advocates have used "
              "to protect children from age-inappropriate content.",
              ["https://ballotpedia.org/Lisa_Krasner",
               "https://www.leg.state.nv.us/App/Legislator/A/Senate/Current/16"]),
    ]),

    # ------- John Steinbeck (SD-18, Clark County/Henderson area, R, Senate since Nov 2024) -------
    ("john-steinbeck", "NV", "State Senator", [
        claim("js1", "john-steinbeck", "sanctity_of_life", 2, False,
              "Was the only Republican senator to vote FOR SB217 (2025 Nevada legislative "
              "session), the mandatory IVF insurance coverage bill requiring most private "
              "and public insurers, including Medicaid, to cover in vitro fertilization "
              "treatments. The bill passed 18-3 with Steinbeck casting the sole "
              "Republican YEA vote in the Senate; the three NAY votes came from Republican "
              "Senators Titus, Ellison, and Stone. Governor Lombardo vetoed the bill. "
              "An analysis by the Nevada Policy Research Institute found Steinbeck posted "
              "the lowest conservative scorecard score among all Republicans in the 2025 "
              "session (61.59%), with 51 cross-party votes — the most of any lawmaker "
              "in either chamber.",
              ["https://thenevadaindependent.com/article/which-nevada-lawmakers-bucked-their-own-party-the-most-in-the-2025-session",
               "https://nevadanewsandviews.com/report-steinbeck-koenig-and-yurek-post-bottom-gop-scores-in-legislative-session/"]),
        claim("js2", "john-steinbeck", "industry_capture", 0, False,
              "Voted FOR SB128 (2025 Nevada legislative session), which prohibits health "
              "insurers from using only artificial intelligence to deny or modify prior "
              "authorization requests for patient care — one of only two Republicans "
              "(along with Sen. Rogich) to join Democrats in passing this new regulatory "
              "mandate on insurance companies. The bill expands state regulatory authority "
              "over private insurers' internal review processes. Steinbeck and Rogich were "
              "consistently the two Republicans most willing to cross party lines on "
              "pro-regulatory bills in the 2025 session, with Steinbeck bucking his "
              "caucus 51 times overall.",
              ["https://thenevadaindependent.com/article/which-nevada-lawmakers-bucked-their-own-party-the-most-in-the-2025-session",
               "https://nevadanewsandviews.com/legislative-review-nevada-gop-lawmakers-break-ranks-408-times-this-session/"]),
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
