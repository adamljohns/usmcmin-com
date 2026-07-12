#!/usr/bin/env python3
"""Enrichment batch 698: cited claims for 5 Wisconsin State Assembly Members.

Continuing the pivot to state legislators from the bottom of the alphabet (WI).
All archetype_curated federal buckets exhausted; targets are archetype_party_default
with 0 claims from the bottom of the reversed-alphabet WI Assembly list.

Targets (5, all D, WI):
  Francesca Hong     (WI AD-76, Madison area) — 2026 D gubernatorial candidate
  Deb Andraca        (WI AD-23, Whitefish Bay / North Shore suburbs)
  Darrin Madison     (WI AD-10, Milwaukee North/West Side) — Democratic Socialist
  Clinton Anderson   (WI AD-45, Beloit / Rock County)
  Christine Sinicki  (WI AD-20, Milwaukee South Side) — 14-term veteran

Sources: docs.legis.wisconsin.gov, legis.wisconsin.gov, legiscan.com,
         wispolitics.com, aclu-wi.org, channel3000.com, fastdemocracy.com,
         plannedparenthoodaction.org, wisconsinexaminer.com, francescahong.com,
         ballotpedia.org, wpr.org, wsaw.com

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
    # -------------- Francesca Hong (WI AD-76, Madison area) — 2026 D Gov candidate --------------
    ("francesca-hong-wi-76", "WI", "Assembly", [
        claim("fh1", "francesca-hong-wi-76", "sanctity_of_life", 0, False,
              "Hong voted NO on AB 975 (14-week abortion ban) on January 25, 2024 — one of all "
              "35 Assembly Democrats opposing the bill in a 53-46 passage. She also co-introduced "
              "AB 355 (July 8, 2025) to repeal Wisconsin's 1849 criminal abortion ban (§940.04) "
              "entirely and enshrine abortion as a fundamental 'right to bodily autonomy.' In her "
              "2026 gubernatorial campaign she is running on a platform of adding abortion access "
              "to the Wisconsin state constitution — rejecting any recognition of personhood from "
              "conception.",
              ["https://docs.legis.wisconsin.gov/2023/related/votes/assembly/av0150",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://pbswisconsin.org/news-item/abortion-laws-and-wisconsins-2026-candidates-for-governor/"]),
        claim("fh2", "francesca-hong-wi-76", "self_defense", 1, False,
              "Hong co-introduced AB 368 (July 27, 2023), a Democrat-led gun-control omnibus "
              "requiring universal background checks for all firearm transfers, including private "
              "sales. On her 2026 governor campaign platform she explicitly supports red-flag "
              "laws, expanded background checks, safe-storage mandates, and banning "
              "3D-printed guns — directly opposing the rubric's defense of unrestricted "
              "Second Amendment rights.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/reg/asm/bill/ab368",
               "https://fastdemocracy.com/bill-search/wi/2023-2024/bills/WIB00012062/",
               "https://francescahong.com/policy/"]),
        claim("fh3", "francesca-hong-wi-76", "biblical_marriage", 2, False,
              "Hong co-introduced AJR 20 (March 24, 2023) and AJR 31 (April 23, 2025) proclaiming "
              "Wisconsin's annual Transgender Day of Visibility, as well as AJR 79 (2025) "
              "recognizing June as LGBTQ Pride Month. She voted NO on all three anti-transgender "
              "Assembly bills (AB 377, AB 378, AB 465) when they passed 63-35 on strict party "
              "lines on October 12, 2023 — bills that barred gender-affirming medical care for "
              "minors and transgender athletes from female sports.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ajr31",
               "https://docs.legis.wisconsin.gov/2023/related/proposals/ajr20",
               "https://wisconsinexaminer.com/2023/10/13/transgender-restrictions-pass-assembly-with-gop-votes-get-hearing-in-senate/"]),
    ]),

    # -------------- Deb Andraca (WI AD-23, Whitefish Bay / North Shore Milwaukee suburbs) --------------
    ("deb-andraca-wi-23", "WI", "Assembly", [
        claim("da1", "deb-andraca-wi-23", "sanctity_of_life", 0, False,
              "Andraca voted NO on AB 975 (14-week abortion ban) on January 25, 2024, as part of "
              "all 35 Assembly Democrats opposing the bill (53-46 passage, vetoed by Gov. Evers). "
              "She co-introduced AB 355 (July 8, 2025) to repeal Wisconsin's 1849 criminal "
              "abortion ban — rejecting any legal protection for the unborn from conception. "
              "Planned Parenthood Advocates of Wisconsin tracks her district (AD-23) among those "
              "opposing abortion restrictions.",
              ["https://docs.legis.wisconsin.gov/2023/related/votes/assembly/av0150",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://www.plannedparenthoodaction.org/planned-parenthood-advocates-wisconsin/issues/14-week-abortion-ban"]),
        claim("da2", "deb-andraca-wi-23", "self_defense", 1, False,
              "Andraca co-introduced AB 368 (July 27, 2023), the Democrat gun-control omnibus "
              "requiring universal background checks for all firearm transfers including private "
              "sales. Before entering the Assembly she served as a Milwaukee-area volunteer leader "
              "for Moms Demand Action for Gun Sense in America, placing her squarely inside the "
              "gun-restriction advocacy network that opposes the rubric's defense of unrestricted "
              "Second Amendment rights.",
              ["https://docs.legis.wisconsin.gov/document/proposaltext/2023/REG/AB368.pdf",
               "https://fastdemocracy.com/bill-search/wi/2023-2024/bills/WIB00012062/",
               "https://legis.wisconsin.gov/assembly/23/andraca/about-the-team/meet-deb/"]),
        claim("da3", "deb-andraca-wi-23", "family_child_sovereignty", 0, False,
              "Andraca voted NO on AB 510 (Parent Bill of Rights) on January 18, 2024, when it "
              "passed 62-35. The bill would have required parental consent before school staff "
              "could address a student by a chosen name or pronouns differing from their birth "
              "certificate, and would have required advance parental notice before any lesson on "
              "gender identity or sexual orientation. She also co-introduced AJR 20 (March 2023) "
              "and AJR 79 (2025) affirming transgender visibility and LGBTQ Pride — opposing "
              "parental oversight of gender ideology in schools.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr79",
               "https://docs.legis.wisconsin.gov/2023/related/proposals/ajr20",
               "https://wisconsinexaminer.com/2024/01/19/assembly-passes-parental-rights-firearm-tracking-ban-and-universal-credentialing-bills/"]),
    ]),

    # -------------- Darrin Madison (WI AD-10, Milwaukee North/West Side) — Democratic Socialist --------------
    ("darrin-madison-wi-10", "WI", "Assembly", [
        claim("dm1", "darrin-madison-wi-10", "sanctity_of_life", 0, False,
              "Madison co-introduced AB 355 (July 8, 2025) to repeal Wisconsin's 1849 criminal "
              "abortion ban and codify abortion as a fundamental right to 'bodily autonomy.' "
              "He voted NO on AB 975 (14-week abortion ban, January 25, 2024, 53-46) as part of "
              "all 35 Assembly Democrats. First elected in 2022 as a Democratic Socialist, "
              "abortion access is a stated legislative priority, rejecting any recognition of "
              "personhood from conception.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://docs.legis.wisconsin.gov/2023/related/votes/assembly/av0150"]),
        claim("dm2", "darrin-madison-wi-10", "biblical_marriage", 2, False,
              "Madison co-introduced AJR 20 (March 2023), AJR 31 (April 2025), and AJR 123 "
              "(December 2025) proclaiming Wisconsin's Transgender Days of Visibility and "
              "Remembrance. In 2025 he publicly stated he 'rejects legislative Republicans' "
              "attacks on trans Wisconsinites.' He voted NO on all three anti-transgender bills "
              "(AB 377, AB 378, AB 465) when they passed 63-35 on strict party lines on "
              "October 12, 2023.",
              ["https://www.wispolitics.com/2025/rep-madison-rejects-legislative-republicans-attacks-on-trans-wisconsinites/",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ajr31",
               "https://wisconsinexaminer.com/2023/10/13/transgender-restrictions-pass-assembly-with-gop-votes-get-hearing-in-senate/"]),
        claim("dm3", "darrin-madison-wi-10", "self_defense", 1, False,
              "Madison co-introduced AB 368 (July 27, 2023), the Democrat gun-control omnibus "
              "requiring universal background checks for all firearm transfers. On his campaign "
              "platform he advocates that owning a gun should require a government-issued license "
              "including a background check, mandatory safety training, and demonstrated "
              "competency — going beyond background checks to full licensing requirements, "
              "directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://docs.legis.wisconsin.gov/document/proposaltext/2023/REG/AB368.pdf",
               "https://www.darrinmadison.com/platform",
               "https://fastdemocracy.com/bill-search/wi/2023-2024/bills/WIB00012062/"]),
    ]),

    # -------------- Clinton Anderson (WI AD-45, Beloit / Rock County) --------------
    ("clinton-anderson-wi-45", "WI", "Assembly", [
        claim("ca1", "clinton-anderson-wi-45", "sanctity_of_life", 0, False,
              "Anderson voted NO on AB 975 (14-week abortion ban, January 25, 2024, 53-46) as "
              "part of all 35 Assembly Democrats. He co-introduced AB 355 (July 8, 2025) to "
              "repeal Wisconsin's 1849 criminal abortion ban and has been endorsed by Planned "
              "Parenthood as a candidate, placing him within the abortion-rights network that "
              "rejects legal protection for the unborn from conception.",
              ["https://docs.legis.wisconsin.gov/2023/related/votes/assembly/av0150",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/votes/AB975/2023"]),
        claim("ca2", "clinton-anderson-wi-45", "self_defense", 1, False,
              "Anderson co-introduced AB 368 (July 27, 2023), the Democrat gun-control omnibus "
              "requiring universal background checks for all firearm transfers, including private "
              "sales. He is listed as a 'Moms Demand Action Gun Sense Candidate,' reflecting "
              "active endorsement from the national gun-restriction advocacy organization — "
              "directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://docs.legis.wisconsin.gov/document/proposaltext/2023/REG/AB368.pdf",
               "https://fastdemocracy.com/bill-search/wi/2023-2024/bills/WIB00012062/",
               "https://ballotpedia.org/Clinton_Anderson"]),
        claim("ca3", "clinton-anderson-wi-45", "biblical_marriage", 2, False,
              "Anderson co-introduced AJR 20 (March 24, 2023), AJR 31 (April 23, 2025), and "
              "AJR 79 (2025) proclaiming Wisconsin's Transgender Day of Visibility and LGBTQ "
              "Pride Month. He also co-authored AB 1212 (2023-24 session), which eliminated "
              "publication requirements for legal name changes sought to affirm gender identity. "
              "He voted NO on all three anti-transgender Assembly bills (AB 377, AB 378, "
              "AB 465) on October 12, 2023.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ajr20",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ajr31",
               "https://docs.legis.wisconsin.gov/2025/proposals/ajr79"]),
    ]),

    # -------------- Christine Sinicki (WI AD-20, Milwaukee South Side) — 14-term veteran --------------
    ("christine-sinicki-wi-20", "WI", "Assembly", [
        claim("cs1", "christine-sinicki-wi-20", "sanctity_of_life", 0, False,
              "Sinicki voted NO on AB 975 (14-week abortion ban, January 25, 2024, 53-46). She "
              "co-introduced AB 355 (July 8, 2025) to repeal Wisconsin's 1849 criminal abortion "
              "ban. In her 14 terms she has been repeatedly endorsed by Planned Parenthood "
              "Advocates of Wisconsin and has authored legislation removing abortion-related "
              "restrictions throughout her tenure — rejecting any recognition of personhood "
              "from conception.",
              ["https://docs.legis.wisconsin.gov/2023/related/votes/assembly/av0150",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://www.plannedparenthoodaction.org/planned-parenthood-advocates-wisconsin/issues/14-week-abortion-ban"]),
        claim("cs2", "christine-sinicki-wi-20", "self_defense", 1, False,
              "Sinicki co-introduced AB 368 (July 27, 2023), the Democrat gun-control omnibus "
              "requiring universal background checks for all firearm transfers, including private "
              "sales. The Wisconsin Firearms Coalition characterized the bill as a 'red flag gun "
              "confiscation' measure. She also voted against the Republican gun-expansion package "
              "in January 2024 that would have lowered the concealed-carry age to 18 and expanded "
              "interstate carry recognition — consistently opposing the rubric's defense of "
              "unrestricted Second Amendment rights.",
              ["https://docs.legis.wisconsin.gov/document/proposaltext/2023/REG/AB368.pdf",
               "https://www.channel3000.com/news/wisconsin-democrats-re-introduce-red-flag-background-check-bills-aimed-at-reducing-gun-violence/article_e99a7838-0972-11ee-bcc3-e3418a22f435.html",
               "https://fastdemocracy.com/bill-search/wi/2023-2024/bills/WIB00012062/"]),
        claim("cs3", "christine-sinicki-wi-20", "biblical_marriage", 2, False,
              "Sinicki co-introduced AJR 20 (March 2023) and AJR 31 (April 2025) proclaiming "
              "Wisconsin's Transgender Day of Visibility. She voted NO on all three "
              "anti-transgender Assembly bills (AB 377, AB 378, AB 465) when they passed 63-35 "
              "on strict party lines on October 12, 2023 — bills banning gender-affirming care "
              "for minors and transgender athletes from female sports. She also voted NO on "
              "AB 510 (Parent Bill of Rights, January 18, 2024, 62-35), which would have "
              "barred school staff from using a student's chosen pronouns without parental "
              "consent.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ajr31",
               "https://docs.legis.wisconsin.gov/2023/related/proposals/ajr20",
               "https://wisconsinexaminer.com/2023/10/13/transgender-restrictions-pass-assembly-with-gop-votes-get-hearing-in-senate/",
               "https://wisconsinexaminer.com/2024/01/19/assembly-passes-parental-rights-firearm-tracking-ban-and-universal-credentialing-bills/"]),
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
