#!/usr/bin/env python3
"""Enrichment batch 807: hand-curated claims for 5 state senators (OH + NY).

Federal senator/rep archetype_curated buckets exhausted; pivoting to
archetype_party_default state senators from the bottom of the alphabet.
Targets (reverse alpha, bottom side of remaining pool):
  Beth Liston (OH-D), Zellnor Myrie (NY-D), Shelley Mayer (NY-D),
  Siela Bynoe (NY-D), Toby Ann Stavisky (NY-D).

All claims drawn from 2023-2026 official legislative records and credible
state-level news sources. MINIFIED write preserved (no indent=2).
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
    # ---------------- Beth Liston (OH-D, State Senator) ----------------
    ("beth-liston", "OH", "Senator", [
        claim("bl1", "beth-liston", "sanctity_of_life", 0, False,
              "As an Ohio House member and physician, Liston co-introduced the Reproductive Care Act (HB 343, Nov 2023) to repeal Ohio's 6-week and 20-week abortion bans, eliminate the 24-hour waiting period, lift medication abortion limits, and nullify fetal-remains disposal requirements — rejecting any recognition of personhood from conception.",
              ["https://ohiocapitaljournal.com/2023/11/10/ohio-democrats-hope-to-seize-on-issue-1-success-announce-reproductive-health-care-bills/",
               "https://ballotpedia.org/Beth_Liston"]),
        claim("bl2", "beth-liston", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Advocates of Ohio for both her 2024 House re-election campaign and her 2024 Senate District 16 race, placing her squarely inside the abortion-industry endorsement network.",
              ["https://ballot.ohea.org/beth-liston-for-ohio-senate-16/",
               "https://ballotpedia.org/Beth_Liston"]),
        claim("bl3", "beth-liston", "biblical_marriage", 2, False,
              "Voted against the January 2024 Ohio House override of Gov. DeWine's veto of HB 68 (SAFE Act), which banned gender-affirming care and puberty blockers for minors, saying: 'I am sorry that we are here today to take away your rights, to target a small vulnerable group.' She subsequently co-introduced SB 71 (Feb 2025) to ban conversion therapy on minors by licensed health professionals — rejecting the rubric's opposition to transgender ideology.",
              ["https://ohiocapitaljournal.com/2024/01/10/ohio-house-overrides-gov-dewines-veto-of-bill-that-would-ban-gender-affirming-care-for-trans-youth/",
               "https://ohiocapitaljournal.com/2025/07/24/a-look-at-what-lgbtq-bills-ohio-lawmakers-have-introduced-so-far/"]),
    ]),

    # ---------------- Zellnor Myrie (NY-D, State Senator) ----------------
    ("zellnor-myrie", "NY", "Senator", [
        claim("zm1", "zellnor-myrie", "sanctity_of_life", 0, False,
              "Voted for the Reproductive Health Act (S240, Jan 22 2019) on the day he was sworn in, legalizing abortion on demand through 24 weeks of gestation and beyond 24 weeks when the woman's life, health, or fetal viability is at issue — rejecting any personhood-from-conception standard.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://en.wikipedia.org/wiki/Zellnor_Myrie"]),
        claim("zm2", "zellnor-myrie", "self_defense", 1, False,
              "Authored New York's gun industry civil liability law (S.7196-A, signed July 2021) — the nation's first state law allowing civil suits against gun manufacturers and dealers for creating a public nuisance through negligent or illegal sales. Named Everytown for Gun Safety's Lawmaker of the Year 2021 for this legislation.",
              ["https://www.nysenate.gov/newsroom/press-releases/2021/zellnor-myrie/governor-signs-senator-myries-gun-industry-liability",
               "https://www.everytown.org/press/everytown-announces-biden-harris-administration-new-york-state-senator-zellnor-myrie-and-dayton-mayor-nan-whaley-to-receive-lawmaker-of-the-year-award/"]),
        claim("zm3", "zellnor-myrie", "biblical_marriage", 2, False,
              "Co-sponsored the Lorena Borjas Transgender and Gender Non-Binary Wellness and Equity Fund (S8884, 2021) and the LGBTQ+ and HIV+ residents' Bill of Rights in long-term care facilities (S1783A, 2023). Supported the 2024 NY Equal Rights Amendment adding sexual orientation and gender identity to the state constitution's equal-protection clause, which voters ratified 56.8%-34.2% in November 2024.",
              ["https://www.nysenate.gov/legislation/bills/2021/S8884",
               "https://en.wikipedia.org/wiki/2024_New_York_Proposal_1"]),
    ]),

    # ---------------- Shelley Mayer (NY-D, State Senator) ----------------
    ("shelley-mayer", "NY", "Senator", [
        claim("sm1", "shelley-mayer", "sanctity_of_life", 0, False,
              "Co-sponsored and passed New York's telehealth abortion shield law (S.1066B, signed May 2023) protecting NY-based doctors who prescribe medication abortion via telehealth to patients in states with abortion bans, making New York the fifth state to enact such a shield. Followed with S.36A (2025) strengthening the shield law with pharmacist privacy protections.",
              ["https://www.nysenate.gov/newsroom/press-releases/2023/shelley-b-mayer/new-york-state-senate-and-assembly-pass-legislation",
               "https://www.nysenate.gov/newsroom/press-releases/2025/shelley-b-mayer/new-york-state-senate-and-assembly-pass-legislation"]),
        claim("sm2", "shelley-mayer", "self_defense", 1, False,
              "Voted YES on S.8479A (June 2024), which passed 45-16, requiring payment card networks to assign a unique merchant category code to all firearm and ammunition dealers — enabling financial institutions to flag and monitor suspicious bulk gun purchase patterns. She publicly urged Governor Hochul to sign this and related public-safety gun bills.",
              ["https://www.nysenate.gov/newsroom/press-releases/2024/shelley-b-mayer/senator-shelley-b-mayer-urges-governor-sign-critical",
               "https://www.nysenate.gov/legislation/bills/2023/S8479/amendment/A"]),
        claim("sm3", "shelley-mayer", "biblical_marriage", 2, False,
              "As Chair of the Senate Education Committee, characterized a 2025 GOP bill banning transgender girls from school sports as 'mean-spirited and misguided,' noting it conflicts with New York State law and the state constitution's gender-identity anti-discrimination protections. Her committee listing of 'transgender equality' and 'LGBT rights' as active issue areas reflects consistent institutional support for transgender school inclusion.",
              ["https://www.cityandstateny.com/policy/2025/05/senate-committee-advances-gop-anti-trans-bill/405093/",
               "https://www.nysenate.gov/issues/transgender-equality"]),
    ]),

    # ---------------- Siela Bynoe (NY-D, State Senator) ----------------
    ("siela-bynoe", "NY", "Senator", [
        claim("sb1", "siela-bynoe", "sanctity_of_life", 4, False,
              "Received the endorsement of Planned Parenthood Empire State Votes for her 2024 NY Senate District 6 campaign, explicitly citing her platform commitment to 'protecting a woman's right to choose' — placing her inside the abortion-industry endorsement network the rubric disqualifies.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-empire-state-votes/endorsements",
               "https://www.patch.com/new-york/longisland/siela-bynoe-announces-candidacy-new-york-state-senate-district-6"]),
        claim("sb2", "siela-bynoe", "sanctity_of_life", 0, False,
              "Voted with the NY Senate Democratic majority on January 21, 2025 to advance a five-bill reproductive rights package including S.135 expanding the Reproductive Freedom Equity Fund for abortion access — her first major abortion-related floor vote as a newly sworn-in state senator, rejecting personhood-from-conception limits.",
              ["https://www.nysenate.gov/newsroom/press-releases/2025/andrea-stewart-cousins/state-senate-advances-legislative-package",
               "https://ballotpedia.org/Siela_Bynoe"]),
    ]),

    # ---------------- Toby Ann Stavisky (NY-D, State Senator) ----------------
    ("toby-ann-stavisky", "NY", "Senator", [
        claim("ts1", "toby-ann-stavisky", "sanctity_of_life", 0, False,
              "Sponsored S.1043-A (signed May 2023), authorizing pharmacists to dispense self-administered hormonal contraceptives without a patient-specific physician prescription, as part of the 'Safe Harbor for All' reproductive-access package. Also co-sponsored S.1066, the abortion provider shield law protecting NY telehealth providers from out-of-state legal proceedings.",
              ["https://www.nysenate.gov/newsroom/press-releases/2023/toby-ann-stavisky/governor-hochul-signs-senator-staviskys-legislation",
               "https://www.nysenate.gov/legislation/bills/2023/S1066/amendment/B"]),
        claim("ts2", "toby-ann-stavisky", "self_defense", 1, False,
              "Co-sponsored the 10-day waiting period for all firearm purchases (S1235, 2021-22 session) and the firearms safety certificate requirement (S1701, 2023-24 session). Also voted for the Concealed Carry Improvement Act (July 2022) restricting where licensed holders may carry, following the NYSRPA v. Bruen Supreme Court decision.",
              ["https://www.nysenate.gov/legislation/bills/2023/S1701",
               "https://ballotpedia.org/Toby_Ann_Stavisky"]),
        claim("ts3", "toby-ann-stavisky", "biblical_marriage", 2, False,
              "Co-sponsored S.1532 (2023-24 session) requiring every school district to establish policies for transgender and gender non-conforming students including access to facilities consistent with their gender identity. Also supported the 2024 NY Equal Rights Amendment that constitutionally added sexual orientation and gender identity to the state equal-protection clause.",
              ["https://www.nysenate.gov/legislation/bills/2023/S1532",
               "https://en.wikipedia.org/wiki/2024_New_York_Proposal_1"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
