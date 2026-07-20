#!/usr/bin/env python3
"""Enrichment batch 781: 5 Ohio Democratic state senators with 0 claims.

archetype_curated and archetype_party_default federal pools are exhausted;
this batch pivots to state-level officials from the bottom of the
reverse-alphabetical assignment (OH is next after the fully-depleted
WY → PA range). All five are Democrats with documented positions opposing
the God-First/America-First rubric across sanctity_of_life, biblical_marriage,
self_defense, and border_immigration categories.

Targets (archetype_party_default, 0 claims before this batch):
  Willis E. Blackshear Jr.  (OH-SD06, D, Dayton)
  William P. DeMora         (OH-SD25, D, Columbus)
  Paula Hicks-Hudson        (OH-SD11, D, Toledo, former mayor)
  Nickie J. Antonio         (OH-SD23, D, Lakewood, Senate Minority Leader)
  Kent Smith                (OH-SD21, D, Euclid, Senate Minority Whip)

All claims cite ≥1 reliable source (ohiosenate.gov, en.wikipedia.org,
ballotpedia.org, Dayton Daily News, Statehouse News Bureau, NBC4i,
The Buckeye Flame, HRC).

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
    # --- Willis E. Blackshear Jr. (OH-SD06, D, Dayton) ---
    ("willis-e-blackshear-jr", "OH", "State Senator", [
        claim("web1", "willis-e-blackshear-jr", "sanctity_of_life", 0, False,
              "After Ohio voters passed Issue 1 (the November 2023 constitutional amendment enshrining "
              "abortion rights through viability), then-Rep. Blackshear affirmed it was 'reflective of "
              "where Ohio stands' and 'the people have spoken.' In his 2024 state-senate campaign "
              "Ballotpedia candidate survey he listed blocking 'dangerous GOP policies like banning "
              "abortion' as a top priority — explicitly rejecting any legal recognition of personhood "
              "from conception.",
              ["https://ballotpedia.org/Willis_Blackshear_Jr.",
               "https://daytondailynews.com/local/issue-1-local-politicians-activists-react-to-abortion-rights-win/DFHQ3BA7CNE3TABFIMZZEC2GCA"]),
        claim("web2", "willis-e-blackshear-jr", "biblical_marriage", 4, False,
              "In his 2024 Ballotpedia candidate-connection survey, Blackshear pledged to fight against "
              "'discriminating against LGBTQ Ohioans,' treating LGBTQ non-discrimination as a core "
              "platform priority alongside abortion access — in direct opposition to the rubric's "
              "standard against government promotion of LGBTQ ideology in schools and policy.",
              ["https://ballotpedia.org/Willis_Blackshear_Jr.",
               "https://ohiosenate.gov/members/willis-e-blackshear-jr"]),
    ]),

    # --- William P. DeMora (OH-SD25, D, Columbus) ---
    ("william-p-demora", "OH", "State Senator", [
        claim("wpd1", "william-p-demora", "biblical_marriage", 2, False,
              "Voted against the Ohio Senate's January 2024 veto override of HB 68 (the Saving Ohio "
              "Adolescents from Experimentation Act, banning gender-transition care and transgender "
              "sports participation for minors). DeMora publicly stated that doctors, advocates, and "
              "even Governor DeWine made clear 'that if House Bill 68 passes, people will die,' calling "
              "the Republican majority's action unconscionable — rejecting the rubric's position that "
              "government should resist transgender ideology in law.",
              ["https://en.wikipedia.org/wiki/Bill_DeMora",
               "https://thebuckeyeflame.com/2024/01/24/ohio-senate-completes-override-of-gov-dewines-veto-of-hb-68/"]),
        claim("wpd2", "william-p-demora", "border_immigration", 2, False,
              "Voted against Ohio Senate Bill 172 (2025), which bars local governments from providing "
              "sanctuary-style protections against immigration-related arrests. DeMora argued on the "
              "Senate floor that the bill would cause racial profiling: 'How do you suspect someone's "
              "an illegal immigrant without violating the 14th Amendment and the Equal Protection "
              "Clause?' — opposing the rubric's support for anti-sanctuary enforcement.",
              ["https://www.daytondailynews.com/local/ohio-senate-oks-bill-blocking-local-protections-against-immigration-related-arrests/LZXE6AWUPRG5NBZ3LJSGI6GYMM/"]),
    ]),

    # --- Paula Hicks-Hudson (OH-SD11, D, Toledo) ---
    ("paula-hicks-hudson", "OH", "State Senator", [
        claim("phh1", "paula-hicks-hudson", "sanctity_of_life", 0, False,
              "Published an official Ohio Senate video titled 'Vote YES on Issue 1' in October 2023, "
              "actively campaigning for the constitutional amendment enshrining abortion rights through "
              "viability. Issue 1 passed 56.8% on November 7, 2023 and became part of the Ohio "
              "Constitution. Hicks-Hudson stated she would 'continue to lead the charge to ensure "
              "women have the freedom to make their own healthcare decisions' — explicitly rejecting "
              "any legal recognition of personhood from conception.",
              ["https://ohiosenate.gov/members/paula-hicks-hudson/video/senator-hicks-hudson-vote-yes-on-issue-1",
               "https://en.wikipedia.org/wiki/November_2023_Ohio_Issue_1"]),
        claim("phh2", "paula-hicks-hudson", "biblical_marriage", 2, False,
              "Voted against the January 2024 Ohio Senate veto override of HB 68 (Saving Ohio "
              "Adolescents from Experimentation Act) and published a statement titled 'Hicks-Hudson "
              "Condemns Anti-Trans Attacks,' calling the law 'government overreach — invading the "
              "privacy of individuals and sanctity of parental decisions' and stating it was 'passed "
              "with absolutely no consideration by the majority for the lives that it will adversely "
              "impact' — rejecting the rubric's opposition to transgender ideology in policy.",
              ["https://ohiosenate.gov/members/paula-hicks-hudson/news/hicks-hudson-condemns-anti-trans-attacks",
               "https://thebuckeyeflame.com/2024/01/24/ohio-senate-completes-override-of-gov-dewines-veto-of-hb-68/"]),
    ]),

    # --- Nickie J. Antonio (OH-SD23, D, Lakewood, Senate Minority Leader) ---
    ("nickie-j-antonio", "OH", "State Senator", [
        claim("nja1", "nickie-j-antonio", "biblical_marriage", 4, False,
              "Ohio's first openly gay state senator and current Senate Minority Leader, Antonio has "
              "introduced the Ohio Fairness Act in every General Assembly since 2011 — legislation "
              "that would extend LGBTQ nondiscrimination protections to housing, employment, and "
              "public accommodations. The most recent version, SB 132 (136th GA, 2024), received its "
              "first Senate committee hearing in November 2024; Antonio testified: 'Ohio is one of 27 "
              "states without laws protecting individuals from discrimination based on sexual "
              "orientation or gender identity.' This directly opposes the rubric's standard against "
              "government-mandated promotion of LGBTQ ideology.",
              ["https://thebuckeyeflame.com/2024/11/13/fairness-act-first-hearing/",
               "https://www.hrc.org/press-releases/bipartisan-ohio-fairness-act-introduced-in-state-senate"]),
        claim("nja2", "nickie-j-antonio", "sanctity_of_life", 0, False,
              "As Ohio Senate Minority Leader, Antonio was the leading Democratic voice for Ohio Issue "
              "1 (the November 2023 constitutional amendment enshrining abortion rights through "
              "viability). After passage she defended viability as the proper standard and stated "
              "Ohioans affirm 'access to abortion and some kind of guardrails.' Antonio has 'fought "
              "against numerous initiatives to restrict abortion rights' since first joining the Ohio "
              "legislature in 2011 — explicitly rejecting any legal recognition of personhood from "
              "conception.",
              ["https://www.statenews.org/government-politics/2023-11-15/ohio-senate-leader-says-after-issue-1-vote-abortion-wont-be-back-on-the-ballot-soon",
               "https://en.wikipedia.org/wiki/Nickie_Antonio"]),
    ]),

    # --- Kent Smith (OH-SD21, D, Euclid, Senate Minority Whip) ---
    ("kent-smith", "OH", "State Senator", [
        claim("ks1", "kent-smith", "self_defense", 1, False,
              "Sponsored SB 307 (135th General Assembly, 2023-24) and its successor SB 235 (136th GA, "
              "2025-26) to ban bump stocks, trigger cranks, and any device that increases a "
              "semi-automatic weapon's rate of fire to simulate fully automatic fire. Smith argued: "
              "'If machine guns are illegal, something that turns something into a machine gun should "
              "also be illegal.' The bill was brought to committee in November 2024 and reintroduced in "
              "2025 — directly opposing the rubric's position against new firearm restrictions and "
              "weapon-accessory bans.",
              ["https://www.nbc4i.com/news/politics/ohio-democrats-push-for-bump-stock-ban/",
               "https://www.buckeyefirearms.org/firearms-bills-135th-general-assembly-2023-2024"]),
        claim("ks2", "kent-smith", "biblical_marriage", 2, False,
              "Voted against the Ohio Senate's January 2024 veto override of HB 68 (transgender care "
              "and sports ban for minors) and published a statement denouncing it as 'state-sponsored "
              "bullying of trans Ohioans' and 'systematic dehumanization of a population for political "
              "gain.' Smith stated his Republican colleagues 'played doctor without a medical license' "
              "and 'assaulted the Constitutional rights of vulnerable Ohioans' — explicitly rejecting "
              "the rubric's position that government should refuse to promote transgender ideology.",
              ["https://ohiosenate.gov/members/kent-smith/news/smith-denounces-senates-veto-override-of-hb-68",
               "https://en.wikipedia.org/wiki/Kent_Smith_(American_politician)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
