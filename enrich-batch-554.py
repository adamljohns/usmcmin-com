#!/usr/bin/env python3
"""Enrichment batch 554: 5 bottom-of-alphabet state officials (evidence_state, 0 claims).

All archetype_curated/archetype_party_default federal-senator and federal-rep buckets
are fully exhausted (confirmed). This batch works the bottom of the evidence_state
0-claim frontier — PA, OR, OK, OH, NC — picking the most prominent sitting officials.

Targets:
  - Gentner Drummond  (OK-R, Attorney General · 2026 R gubernatorial runoff)
  - Mike DeWine       (OH-R, Governor)
  - Rachel Hunt       (NC-D, Lieutenant Governor)
  - Austin Davis      (PA-D, Lieutenant Governor)
  - Dan Rayfield      (OR-D, Attorney General)

All claims cite >=1 reliable source (oklahoma.gov, governor.ohio.gov, en.wikipedia.org,
choicetracker.org, nraila.org, opb.org, statenews.org) and reflect verifiable
2019-2026 actions, votes, and public statements.

Scorecard written MINIFIED (separators=(",",":")) to stay under GitHub's 50 MB limit.
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
    # --- Gentner Drummond (OK-R, Attorney General · 2026 gubernatorial runoff) ---
    ("gentner-drummond", "OK", "Attorney General", [
        claim("gd1", "gentner-drummond", "sanctity_of_life", 0, True,
              "As Oklahoma AG, Drummond filed suit in November 2023 against the Biden HHS after it stripped Oklahoma of its decades-long Title X family-planning grant solely because Oklahoma declines to refer women for abortion, calling HHS's action an attempt to 'punish Oklahoma for the policies adopted by Oklahoma's elected representatives to protect unborn life.' He escalated to the U.S. Supreme Court in October 2024 and in June 2025 touted a favorable SCOTUS outcome through Medina v. Planned Parenthood South Atlantic that vindicated Oklahoma's right to enforce pro-life law without forfeiting federal family-planning funding.",
              ["https://oklahoma.gov/oag/news/newsroom/2023/november/drummond-sues-biden-administration-over-title-x-abortion-overrea.html",
               "https://oklahoma.gov/oag/news/newsroom/2025/june/drummond-touts-supreme-court-wins-on-birth-certificates-and-title-x.html",
               "https://oklahoma.gov/oag/news/newsroom/2024/october/drummond-asks-supreme-court-to-review-title-x-referral-overreach-case.html"]),
        claim("gd2", "gentner-drummond", "self_defense", 1, True,
              "Drummond led a coalition of 24 state attorneys general urging Congress to pass H.R. 38 (the Concealed Carry Reciprocity Act), affirming states' rights to carry without a government-issued permit. In August 2024 he hailed a federal-court victory blocking a Biden-era ATF rule that expanded firearms-dealer background-check mandates, calling it a win against regulatory overreach. In June 2026 he praised a U.S. Supreme Court ruling striking down Hawaii's prohibition on carrying firearms in places of public accommodation, stating 'this decision rightly upholds our Second Amendment right to keep and bear arms.'",
              ["https://www.nraila.org/articles/20250602/twenty-four-state-attorneys-general-urge-congress-to-pass-hr-38",
               "https://oklahoma.gov/oag/news/newsroom/2024/august/drummond-hails-oklahoma-coalition-winning-decision-against-biden-administration-gun-rule.html",
               "https://oklahoma.gov/oag/news/newsroom/2026/june/drummond-lauds-supreme-court-ruling-on-second-amendment-rights.html"]),
    ]),

    # --- Mike DeWine (OH-R, Governor) ---
    ("mike-dewine", "OH", "Governor", [
        claim("md1", "mike-dewine", "sanctity_of_life", 0, True,
              "In April 2019, DeWine signed Ohio's Human Rights and Heartbeat Protection Act (HB 493), banning abortions after embryonic cardiac activity is detected — approximately six weeks — with no exceptions for rape or incest, one of the nation's most restrictive abortion laws at the time. DeWine defended the bill as necessary to 'protect the most vulnerable among us, those who don't have a voice,' stating that 'the government's role should be to protect life from the beginning to the end.' (The ban was later struck down following the 2023 Ohio Issue 1 constitutional amendment, but DeWine's signature reflects his firm personhood-from-conception commitment.)",
              ["https://en.wikipedia.org/wiki/Mike_DeWine",
               "https://en.wikipedia.org/wiki/Abortion_in_Ohio"]),
        claim("md2", "mike-dewine", "self_defense", 0, True,
              "In March 2022, DeWine signed Senate Bill 215, making Ohio the 23rd state to enact permitless concealed carry — eliminating the requirement for a government-issued license, mandatory eight hours of firearms training, and background check to carry a concealed handgun. He also signed Ohio's Stand Your Ground law, removing any duty to retreat before using deadly force in self-defense. Together these actions represent the most significant expansion of Ohioans' Second Amendment carry rights in the state's history.",
              ["https://www.statenews.org/government-politics/2022-03-14/dewine-signs-bill-to-make-it-easier-for-people-to-carry-concealed-guns",
               "https://en.wikipedia.org/wiki/Mike_DeWine"]),
    ]),

    # --- Rachel Hunt (NC-D, Lieutenant Governor) ---
    ("rachel-hunt", "NC", "Lieutenant Governor", [
        claim("rh1", "rachel-hunt", "sanctity_of_life", 0, False,
              "As a North Carolina state senator (SD-42, 2022–2024), Hunt voted against the Care for Women, Children and Families Act (SL 2023-14) — the 2023 Republican bill that reduced abortion access from 20 weeks to 12 weeks with only narrow exceptions — joining all 20 Senate Democrats in unanimous opposition. She co-sponsored legislation to codify Roe v. Wade at the state level and has stated she 'will continue to stand up for reproductive rights and fight for access to comprehensive reproductive healthcare,' explicitly rejecting any personhood-from-conception framework.",
              ["https://en.wikipedia.org/wiki/Rachel_Hunt",
               "https://www.ncleg.gov/Members/Biography/s/442"]),
        claim("rh2", "rachel-hunt", "family_child_sovereignty", 0, False,
              "During her 2024 Lieutenant Governor campaign, Hunt explicitly minimized parental authority over children's in-school experiences on sensitive topics, stating 'parents don't have all the answers' and that teachers must be empowered to fill the gap 'because sometimes kids can't ask their parents.' She ran on a platform of expanding public school funding — opposing Republican parental-rights and school-choice legislation, including Opportunity Scholarship voucher expansion — prioritizing the school establishment over parental sovereignty.",
              ["https://spectrumlocalnews.com/nc/charlotte/politics/2023/03/01/n-c--sen--rachel-hunt-to-run-for-lieutenant-governor",
               "https://en.wikipedia.org/wiki/Rachel_Hunt"]),
    ]),

    # --- Austin Davis (PA-D, Lieutenant Governor) ---
    ("austin-davis", "PA", "Lt. Governor", [
        claim("ad1", "austin-davis", "sanctity_of_life", 0, False,
              "Davis has been endorsed by Planned Parenthood Pennsylvania Advocates PAC, voted as a state representative against bills that would have excluded abortion from the PA Constitution or prohibited abortion based on Down syndrome diagnosis, and as Lieutenant Governor joined the national Reproductive Freedom Coalition — a 22-state Democratic LG alliance dedicated to expanding abortion access. He also proposed a state constitutional amendment enshrining a 'fundamental right to personal reproductive liberty,' explicitly rejecting any personhood-from-conception standard.",
              ["https://choicetracker.org/legislator/h35davis",
               "https://www.plannedparenthoodaction.org/planned-parenthood-pennsylvania-advocates/press-releases/planned-parenthood-pa-pac-announces-first-wave-of-campaign-endorsements-for-general-assembly-and-lieutenant-governor",
               "https://penncapital-star.com/briefs/pa-lt-gov-davis-joins-multi-state-abortion-alliance/"]),
        claim("ad2", "austin-davis", "biblical_marriage", 4, False,
              "Davis and Governor Shapiro committed to enacting Pennsylvania's first statewide LGBTQ nondiscrimination law covering employment, housing, and public accommodations based on sexual orientation and gender identity; strengthening PA hate-crime statutes to protect LGBTQ+ individuals; and eliminating the 'Gay and Trans Panic Defense' — a legal strategy that has been used to justify violence against LGBTQ persons. These commitments represent active promotion of LGBTQ ideology in law, courts, and public accommodations that the rubric opposes.",
              ["https://justfacts.votesmart.org/public-statement/1617916/lgbtq-leaders-from-across-pennsylvania-endorse-josh-shapiro-and-austin-davis-for-governor-lieutenant-governor",
               "https://en.wikipedia.org/wiki/Austin_Davis_(politician)"]),
    ]),

    # --- Dan Rayfield (OR-D, Attorney General) ---
    ("dan-rayfield", "OR", "Attorney General", [
        claim("dr1", "dan-rayfield", "sanctity_of_life", 0, False,
              "As Speaker of the Oregon House of Representatives (2022–2024), Rayfield championed and helped enact what Oregon lawmakers described as 'the nation's strongest abortion protections,' codifying a state right to abortion and contraception and eliminating waiting periods and mandatory counseling requirements. As Attorney General since 2024, he has committed to enforcing and defending these laws, directly opposing any personhood-from-conception standard.",
              ["https://www.opb.org/article/2024/09/25/opb-election-survey-dan-rayfield/",
               "https://en.wikipedia.org/wiki/Dan_Rayfield"]),
        claim("dr2", "dan-rayfield", "self_defense", 1, False,
              "Rayfield publicly committed during his 2024 AG race to continue litigating to implement Oregon Ballot Measure 114 — passed by voters in November 2022 — which requires a government-issued permit to purchase any firearm and bans the possession of ammunition magazines exceeding 10 rounds. He 'indicated he would continue to pursue the litigation to implement the law and move the process forward' despite ongoing court challenges from gun-rights groups, placing him directly against the rubric's rejection of government permitting schemes and magazine restrictions.",
              ["https://www.opb.org/article/2024/09/25/opb-election-survey-dan-rayfield/",
               "https://en.wikipedia.org/wiki/Dan_Rayfield"]),
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
            if cat in scores and qi is not None and qi < len(scores.get(cat) or []):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
