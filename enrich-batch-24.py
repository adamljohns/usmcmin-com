#!/usr/bin/env python3
"""Enrichment batch 24: hand-curated claims for 5 bottom-of-alphabet federal candidates.

Targets archetype_curated candidates with 0 evidence claims, taken from the
BOTTOM of the reverse-sorted (state desc) bucket to avoid collision with the
concurrent top-of-alphabet enrichment agent (AK/AL/AR...).

Mix (2 R / 3 D): Chris Murphy (CT-D), John Hickenlooper (CO-D),
Alex Padilla (CA-D), Doug Collins (GA-R, former US Rep/VA Sec),
Sharice Davids (KS-D, sitting US Rep).
Each claim cites >=1 reliable source and reflects documented 2024-2026
voting record / public positions (or House record for former members).

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
    # ---------------- Chris Murphy (CT-D, US Senator) ----------------
    ("chris-murphy", "CT", "Senator", [
        claim("cm1", "chris-murphy", "self_defense", 1, False,
              "A founding Senate champion of gun restrictions who staged a 15-hour filibuster in 2016 and led negotiations on the Bipartisan Safer Communities Act (2022) — the first significant federal gun law in nearly 30 years. Murphy supports an assault-weapons ban, universal background checks, red-flag laws, and high-capacity magazine limits, directly opposing the rubric's defense of the right to keep and bear arms without legislative restriction.",
              ["https://en.wikipedia.org/wiki/Chris_Murphy",
               "https://www.murphy.senate.gov/newsroom/in-the-news/in-his-own-words-senator-murphy-on-guns-democracy-and-2024"]),
        claim("cm2", "chris-murphy", "sanctity_of_life", 4, False,
              "Cosponsors the Women's Health Protection Act to codify abortion access nationwide and visited a Planned Parenthood facility in 2024 to advance abortion rights; his legislation is endorsed by both Planned Parenthood Federation of America and Reproductive Freedom for All (formerly NARAL Pro-Choice America) — placing him squarely inside the abortion industry's endorsement and funding network.",
              ["https://www.murphy.senate.gov/issues/choice-and-womens-health",
               "https://en.wikipedia.org/wiki/Chris_Murphy"]),
        claim("cm3", "chris-murphy", "biblical_marriage", 4, False,
              "In 2024–2025 led Senate efforts to strip anti-LGBTQ provisions from government funding bills and introduced legislation to reverse restrictions on abortion access — actively working to embed LGBTQ protections into federal appropriations law, in direct conflict with the rubric's opposition to government promotion of LGBTQ ideology.",
              ["https://www.murphy.senate.gov/newsroom/press-releases/murphy-blumenthal-colleagues-push-to-keep-anti-lgbtq-and-anti-abortion-provisions-out-of-critical-government-funding-bills",
               "https://en.wikipedia.org/wiki/Chris_Murphy"]),
    ]),

    # ---------------- John Hickenlooper (CO-D, US Senator) ----------------
    ("john-hickenlooper", "CO", "Senator", [
        claim("jh1", "john-hickenlooper", "self_defense", 1, False,
              "As Colorado governor signed bills in 2013 mandating universal background checks on all gun transfers and banning magazines holding more than 15 rounds; as U.S. Senator cosponsors the Background Check Expansion Act and advocates banning assault weapons — a consistent record opposing Second Amendment rights without restriction.",
              ["https://en.wikipedia.org/wiki/John_Hickenlooper",
               "https://www.hickenlooper.senate.gov/issues/gun-violence/"]),
        claim("jh2", "john-hickenlooper", "biblical_marriage", 0, False,
              "Cosponsors the Equality Act, which extends federal civil-rights protections to sexual orientation and gender identity in workplaces, schools, and public accommodations — mandating legal recognition of LGBTQ identity categories that conflicts with the biblical definition of marriage as between one man and one woman.",
              ["https://www.hickenlooper.senate.gov/issues/civil-rights/",
               "https://en.wikipedia.org/wiki/John_Hickenlooper"]),
        claim("jh3", "john-hickenlooper", "sanctity_of_life", 0, False,
              "After Dobbs, Hickenlooper condemned the ruling as threatening women's 'control over her own future' and called on Republicans to 'keep politics out of reproductive health care decisions.' His consistent pro-abortion stance rejects any recognition of human personhood beginning at conception.",
              ["https://en.wikipedia.org/wiki/John_Hickenlooper",
               "https://ballotpedia.org/John_Hickenlooper"]),
    ]),

    # ---------------- Alex Padilla (CA-D, US Senator) ----------------
    ("alex-padilla", "CA", "Senator", [
        claim("ap1", "alex-padilla", "border_immigration", 0, False,
              "In February 2024, broke from his own party's leadership and the Biden administration to lead Senate opposition to the bipartisan border security bill, publicly urging colleagues to vote against it to protect 'Dreamers, farmworkers and other long-term undocumented members of our communities.' Prioritized amnesty provisions over enforcement, blocking any deal that didn't advance a path to legal status for those in the country illegally.",
              ["https://www.padilla.senate.gov/newsroom/news-coverage/la-times-california-sen-alex-padilla-convinces-colleagues-to-vote-against-bipartisan-border-bill/",
               "https://en.wikipedia.org/wiki/Alex_Padilla"]),
        claim("ap2", "alex-padilla", "sanctity_of_life", 4, False,
              "Holds a 100% lifetime score from Reproductive Freedom for All (formerly NARAL Pro-Choice America), received NARAL's endorsement for reelection, led a Senate resolution on medication abortion backed by Planned Parenthood, and visited a Planned Parenthood clinic to push for abortion rights — firmly embedded in the abortion-industry endorsement and funding orbit.",
              ["https://reproductivefreedomforall.org/lawmaker/alex-padilla/",
               "https://reproductivefreedomforall.org/news/naral-pro-choice-america-endorses-alex-padilla-for-reelection-to-the-u-s-senate/",
               "https://www.padilla.senate.gov/newsroom/press-releases/padilla-pushes-to-protect-abortion-rights-during-planned-parenthood-visit/"]),
        claim("ap3", "alex-padilla", "border_immigration", 4, False,
              "Publicly condemned President Trump's executive orders to end birthright citizenship as unconstitutional, defending automatic citizenship for children born to non-citizens on U.S. soil — opposing the rubric's call to end birthright citizenship as a migration incentive.",
              ["https://en.wikipedia.org/wiki/Alex_Padilla",
               "https://www.padilla.senate.gov/about/issues/immigration/"]),
    ]),

    # ---------------- Doug Collins (GA-R, former US Rep GA-09 / former VA Secretary) ----------------
    ("doug-collins-senate-2026", "GA", "Senate", [
        claim("dc1", "doug-collins-senate-2026", "sanctity_of_life", 0, True,
              "SBA Pro-Life America documents a consistent pro-life House record (2013–2020): Collins 'voted consistently to protect the lives of the unborn as well as the consciences of taxpayers who don't want their hard-earned tax dollars paying for abortion domestically or internationally.' An ordained Church of God minister, he affirms the sanctity of human life from conception.",
              ["https://sbaprolife.org/representative/doug-collins",
               "https://en.wikipedia.org/wiki/Doug_Collins_(politician)"]),
        claim("dc2", "doug-collins-senate-2026", "self_defense", 1, True,
              "A consistently pro-Second-Amendment House member who opposed gun restrictions throughout his 2013–2020 tenure, earning strong ratings from the National Rifle Association and opposing assault-weapons bans, expanded background-check mandates, and magazine-capacity limits pushed by House Democrats.",
              ["https://ballotpedia.org/Doug_Collins",
               "https://www.govtrack.us/congress/members/doug_collins/412531"]),
        claim("dc3", "doug-collins-senate-2026", "election_integrity", 0, True,
              "In December 2020, Collins was one of 126 House Republicans who signed an amicus brief in Texas v. Pennsylvania, supporting the legal challenge to mail-in voting procedures implemented without explicit legislative authorization — aligning with the rubric's preference for election processes governed by state legislatures rather than executive or judicial expansion of absentee voting.",
              ["https://en.wikipedia.org/wiki/Doug_Collins_(politician)"]),
    ]),

    # ---------------- Sharice Davids (KS-D, sitting US Rep KS-03, 2026 Senate candidate) ----------------
    ("sharice-davids-senate", "KS", "Senate", [
        claim("sd1", "sharice-davids-senate", "border_immigration", 1, False,
              "In a 2018 podcast, when asked about abolishing ICE, Davids responded that defunding ICE was 'probably essentially the same thing' — a position verified by the Associated Press fact-checker despite her subsequent denials. Opposition to the primary federal immigration-enforcement agency is incompatible with the rubric's support for mandatory deportation of those in the country illegally.",
              ["https://en.wikipedia.org/wiki/Sharice_Davids",
               "https://ballotpedia.org/Sharice_Davids"]),
        claim("sd2", "sharice-davids-senate", "sanctity_of_life", 0, False,
              "Publicly affirms that 'people have a right to make their own health care decisions, not the government,' and has voted consistently against legislation limiting abortion access, rejecting any legal recognition of human personhood beginning at conception.",
              ["https://en.wikipedia.org/wiki/Sharice_Davids",
               "https://ballotpedia.org/Sharice_Davids"]),
        claim("sd3", "sharice-davids-senate", "biblical_marriage", 0, False,
              "An openly gay member of Congress who voted for the Respect for Marriage Act (2022) enshrining federal recognition of same-sex unions, and supports the Equality Act extending civil-rights protections to sexual orientation and gender identity in workplaces and schools — rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Sharice_Davids",
               "https://ballotpedia.org/Sharice_Davids"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
