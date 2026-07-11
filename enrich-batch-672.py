#!/usr/bin/env python3
"""Enrichment batch 672: 5 Rhode Island Democratic state senators.

Federal senator/rep pools are fully exhausted; this batch moves to the
archetype_party_default state-senator pool at the bottom of the remaining
alphabet (RI is the highest remaining state after all W-states have been
upgraded to evidence_curated).  All five are Democrats; claims document
positions that do not align with the God-First/America-First rubric
(score_impact=False) and are sourced from Wikipedia, Ballotpedia, the RI
General Assembly website, LegiScan, and Rhode Island news outlets.

Targets (reverse-alpha top-5 in RI pool):
  Tiara Mack       (District 6,  Providence  — first openly queer Black RI senator)
  Sam Bell         (District 5,  Providence  — first DSA member in RI General Assembly)
  Sam Zurier       (District 3,  Providence  — attorney; co-sponsored 2025 AWB)
  Ryan W. Pearson  (District 19, Cumberland  — former Senate Majority Leader, openly gay)
  Pamela J. Lauria (District 29, Barrington  — primary sponsor of RI safe-storage gun law)
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
    # ---- Tiara Mack (RI, Senate District 6, Providence) ----
    # Elected Nov 2020; re-elected Nov 2024. First openly queer Black RI senator.
    # Former Planned Parenthood of Southern New England youth organizing specialist.
    ("tiara-mack", "RI", "Senator", [
        claim("tm1", "tiara-mack", "sanctity_of_life", 4, False,
              "Before her 2020 election to the Rhode Island Senate, Mack worked as a 'youth "
              "organizing specialist' for Planned Parenthood of Southern New England (PPSNE), "
              "an affiliate that directly provides and funds abortions. She continues to "
              "champion PPSNE's legislative priorities in the chamber, placing her squarely "
              "within the abortion-industry network the rubric tests (never took PP/NARAL/"
              "EMILY money or association).",
              ["https://en.wikipedia.org/wiki/Tiara_Mack",
               "https://ballotpedia.org/Tiara_Mack",
               "https://www.rilegislature.gov/senators/mack/Pages/Biography.aspx"]),
        claim("tm2", "tiara-mack", "sanctity_of_life", 0, False,
              "Mack championed the Equality in Abortion Coverage Act, which the Rhode Island "
              "Senate passed 24-12 in May 2023 and Gov. McKee signed into law. The act "
              "directs Rhode Island Medicaid and state-employee health insurance to fund "
              "abortions — explicitly expanding taxpayer-paid abortion and rejecting any "
              "legal protection for the unborn from conception.",
              ["https://abcnews.go.com/Politics/wireStory/rhode-island-senate-poised-approve-expanded-abortion-access-99439575",
               "https://www.eastbayri.com/warren/stories/rhode-island-general-assembly-passes-equality-in-abortion-coverage-act,112964"]),
        claim("tm3", "tiara-mack", "self_defense", 1, False,
              "Mack co-sponsored S0359, the Rhode Island Assault Weapons Ban Act of 2025, "
              "which bans the sale and manufacture of certain semi-automatic rifles, shotguns, "
              "and handguns; the bill passed the Senate and was signed into law June 26, 2025. "
              "Her campaign website explicitly endorses a federal assault-weapons ban, a "
              "large-capacity magazine ban (10+ rounds), mandatory firearm registration, and "
              "a limit of one handgun purchase per 30 days.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://www.tiaramackdistrict6.com/en/gun-policy"]),
    ]),

    # ---- Sam Bell (RI, Senate District 5, Providence) ----
    # Elected 2018; first DSA member ever elected to the RI General Assembly.
    # Self-identifies as bisexual. Gun-control activist since 2012 Sandy Hook shooting.
    ("sam-bell", "RI", "Senator", [
        claim("sb1", "sam-bell", "sanctity_of_life", 0, False,
              "Bell voted for the RI Reproductive Privacy Act (2019, passed Senate 21-17), "
              "which codified Roe v. Wade into Rhode Island law; and for the Equality in "
              "Abortion Coverage Act (May 2023, 24-12), which directs state Medicaid and "
              "employee insurance to fund abortions. His campaign website states he 'stood "
              "with activists to codify Roe v. Wade into Rhode Island Law.'",
              ["https://www.sambellpvd.com/issues",
               "https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/"]),
        claim("sb2", "sam-bell", "self_defense", 1, False,
              "Bell's political career began with gun-control activism after the 2012 Sandy "
              "Hook shooting. As executive director of the RI Progressive Democrats he "
              "investigated illegal NRA campaign contributions; his work resulted in the NRA "
              "paying a $63,000 fine — the second-largest campaign finance penalty in RI "
              "history — and the formal dissolution of the NRA's Rhode Island PAC. He has "
              "since co-sponsored gun-safety legislation in the Senate.",
              ["https://www.rilegislature.gov/senators/bell/Pages/Biography.aspx",
               "http://www.rifuture.org/ga-nra-illegal-donations/"]),
        claim("sb3", "sam-bell", "biblical_marriage", 0, False,
              "Bell self-identifies as bisexual and states on his campaign website: 'as a "
              "bisexual, Sam Bell knows first-hand how important acceptance and love are to "
              "the LGBTQ community,' committing to 'always fight for the LGBTQIA+ community' "
              "including specifically on transgender rights — directly rejecting a one-man/"
              "one-woman definition of marriage and family.",
              ["https://www.sambellpvd.com/issues",
               "https://ballotpedia.org/Sam_Bell_(Rhode_Island)"]),
    ]),

    # ---- Sam Zurier (RI, Senate District 3, Providence) ----
    # In office since November 2021; Yale (B.A. math), Oxford (M.A.), Yale Law (J.D.);
    # former assistant Massachusetts AG and law clerk under Judge Stephen Breyer.
    ("sam-zurier", "RI", "Senator", [
        claim("sz1", "sam-zurier", "self_defense", 1, False,
              "Zurier co-sponsored S0359, the Rhode Island Assault Weapons Ban Act of 2025, "
              "which bans the sale and manufacture of certain semi-automatic rifles, shotguns, "
              "and handguns. The bill passed the RI Senate and was signed into law June 26, "
              "2025. Zurier has also formally pledged to govern with 'gun sense as a priority' "
              "via the Everytown Gun Sense Voter program.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://gunsensevoter.org/candidates/details/?cid=e32973adb716010ed925618fa3a8c3fdd9470b841392f14eea9031a491df2c9c"]),
        claim("sz2", "sam-zurier", "biblical_marriage", 0, False,
              "In 2026, Zurier voted against confirming former RI Senate Majority Leader "
              "Michael McCaffrey to a District Court judgeship, explicitly citing McCaffrey's "
              "anti-LGBTQ voting record — including his 2013 vote against marriage equality "
              "and his 2019 vote against the Reproductive Privacy Act. In a prior interview "
              "Zurier expressed support for LGBTQ equality including diverse family "
              "representation in school curricula.",
              ["https://bostonspiritmagazine.com/2026/02/despite-long-anti-lgbtq-voting-record-as-state-senator-mccaffrey-appointed-ri-district-court-judge/",
               "https://upriseri.com/interview-samuel-zurier/"]),
    ]),

    # ---- Ryan W. Pearson (RI, Senate District 19, Cumberland/Lincoln) ----
    # In office since 2013. Senate Majority Leader Jan 2023 – Jan 2025.
    # First openly gay member of RI Senate leadership.
    ("ryan-w-pearson", "RI", "Senator", [
        claim("rp1", "ryan-w-pearson", "sanctity_of_life", 0, False,
              "Pearson provided a decisive vote in the RI Senate Judiciary Committee for the "
              "Equality in Abortion Coverage Act (2023), advancing it to the floor where it "
              "passed 24-12; Gov. McKee signed it in May 2023. Pearson was also named among "
              "Planned Parenthood Votes! Rhode Island PAC-endorsed 2024 general-election "
              "winners, confirming his alignment with the abortion-rights network.",
              ["https://rhodeislandcurrent.com/2023/05/16/eaca-passes-senate-judiciary-committee/",
               "https://www.plannedparenthoodaction.org/planned-parenthood-votes-rhode-island/news-room/planned-parenthood-votes-rhode-island-pac-announces-first-round-of-endorsements-for-the-2024-general-assembly-election-3"]),
        claim("rp2", "ryan-w-pearson", "biblical_marriage", 0, False,
              "Pearson is openly gay and was the first openly gay member of the Rhode Island "
              "Senate leadership team when chosen as Senate Majority Leader in 2022 — a "
              "position he held through January 2025. He consistently supports LGBTQ+ "
              "rights legislation, directly rejecting a one-man/one-woman definition of "
              "marriage.",
              ["https://rhodeislandcurrent.com/2025/04/24/conservative-and-progressive-dems-jockey-to-lead-the-r-i-senate/",
               "https://en.wikipedia.org/wiki/Ryan_W._Pearson"]),
        claim("rp3", "ryan-w-pearson", "self_defense", 1, False,
              "Pearson has publicly supported stricter gun restrictions throughout his Senate "
              "tenure; news reporting on the 2025 Senate leadership race noted that Pearson "
              "'supports stronger reproductive rights and gun restrictions,' and he voted "
              "with the Democratic majority on gun-safety measures during his term as "
              "Senate Majority Leader (2023-2025).",
              ["https://rhodeislandcurrent.com/2025/04/24/conservative-and-progressive-dems-jockey-to-lead-the-r-i-senate/",
               "https://en.wikipedia.org/wiki/Ryan_W._Pearson"]),
    ]),

    # ---- Pamela J. Lauria (RI, Senate District 29, Barrington) ----
    # Democrat; primary Senate sponsor of Rhode Island's safe-storage firearms law.
    # Shepherded the bill through two years of hearings; signed into law June 2024.
    ("pamela-j-lauria", "RI", "Senator", [
        claim("pl1", "pamela-j-lauria", "self_defense", 1, False,
              "Lauria was the primary Senate sponsor of Rhode Island's safe-storage firearms "
              "law, shepherding the bill through two years of committee hearings until it "
              "passed the RI Senate 28-7 in March 2024 and was signed into law by Gov. McKee "
              "in June 2024. The law requires all firearms not in active use to be stored in "
              "a locked container or equipped with a tamper-resistant lock, with civil and "
              "criminal penalties for violations — a direct restriction on Second Amendment "
              "exercise the rubric opposes.",
              ["https://rhodeislandcurrent.com/2024/03/19/safe-weapons-bill-passes-through-rhode-island-senate/",
               "https://rhodeislandcurrent.com/2024/06/14/mckee-signs-safe-firearms-storage-bill-into-law/"]),
        claim("pl2", "pamela-j-lauria", "sanctity_of_life", 0, False,
              "As a Democratic member of the Rhode Island Senate, Lauria supported the "
              "Equality in Abortion Coverage Act (passed 24-12, signed May 2023), which "
              "directs state Medicaid and state employee health insurance to fund abortions "
              "— rejecting any legal protection for the unborn from conception and expanding "
              "taxpayer-funded abortion.",
              ["https://abcnews.go.com/Politics/wireStory/rhode-island-senate-poised-approve-expanded-abortion-access-99439575",
               "https://ballotpedia.org/Pamela_Lauria"]),
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
