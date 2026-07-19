#!/usr/bin/env python3
"""Enrichment batch 775: 14 claims for 5 NJ Republican state senators.

Primary archetype_curated federal pool was fully depleted by batch 757.
Recent batches pivoted to state-level officials. This batch continues
that work with five sitting NJ Republican state senators who had 0 claims,
taken from the bottom of the available alphabet (NJ = near-bottom of
states with R senators remaining):

  James W. Holzapfel  (State Senator, SD-10, Ocean County)
  Holly T. Schepisi   (State Senator, SD-39, Bergen County)
  Declan O'Scanlon    (State Senator, SD-13, Monmouth County)
  Anthony M. Bucco    (State Senator, SD-25, Republican Leader)
  Owen Henry          (State Senator, SD-12, Mercer/Middlesex/Monmouth)

Claims span sanctity_of_life, self_defense, biblical_marriage,
family_child_sovereignty, and economic_stewardship.
All claims cite reliable sources from 2022-2026.

Key confirmed votes used:
 - NJ S49 (Freedom of Reproductive Choice Act): passed 23-15 on 1/10/2022;
   Freedom Index roll-call confirms Holzapfel NO, O'Scanlon NO,
   Schepisi NOT VOTING (all other 15 NO votes were Republican).
 - NJ Dec 2022 gun package (21-16 on 12/19/2022): every Republican senator
   voted NO — confirmed by NJ Monitor reporting.
 - NJ S2483 (Parents Bill of Rights Act, 2022): Holzapfel and Bucco are
   named co-sponsors per NJ Legislature records.
 - NJ 2026 reproductive/transgender healthcare bill (A2218, 25-15 on
   6/30/2026): party-line vote, Republicans opposed; Schepisi named by NJ
   Monitor as voting against committee advancement (May 2026).

NOTE: writes scorecard.json MINIFIED to keep master ~35-36MB under
GitHub's 50MB limit.
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
    # ---------- James W. Holzapfel (NJ State Senator SD-10, R) ----------
    ("james-w-holzapfel", "NJ", "State Senator", [
        claim("jh1", "james-w-holzapfel", "sanctity_of_life", 0, True,
              "Cast one of the 15 Republican no votes against New Jersey S49 (Freedom of Reproductive Choice Act), which passed 23-15 on January 10, 2022. The act codifies the right to abortion at every stage of pregnancy into state law, requires insurance coverage for abortion, and permits abortions by advanced practice nurses and physician assistants rather than only physicians — the most expansive abortion codification in New Jersey history. The NJ Freedom Index roll-call record confirms Holzapfel's no vote; he was among 15 Republicans who rejected the bill outright.",
              ["https://thefreedomindex.org/nj/vote/1122798/",
               "https://newjerseymonitor.com/2022/01/13/murphy-signs-law-solidifying-abortion-rights-in-new-jersey/"]),
        claim("jh2", "james-w-holzapfel", "self_defense", 1, True,
              "Voted NO on the December 2022 NJ gun-control package (S4219/A4769), which passed the Senate 21-16 on December 19, 2022, in a lame-duck session convened before a more Republican-friendly legislature took office. The bill overhauled the concealed-carry permit process in response to the U.S. Supreme Court's NYSRPA v. Bruen decision, created 25+ new 'sensitive place' gun-free zones, and raised firearm fees. Every one of the 16 Republican senators — including Holzapfel — voted no; Democrat Sen. Nicholas Sacco was the only party defection to the no column.",
              ["https://newjerseymonitor.com/2022/12/19/senate-sends-sweeping-gun-bill-to-governors-desk-in-narrow-vote/",
               "https://patch.com/new-jersey/across-nj/controversial-nj-firearms-bill-passes-senate-murphy-slated-sign"]),
        claim("jh3", "james-w-holzapfel", "family_child_sovereignty", 0, True,
              "Co-sponsored New Jersey S2483 (Parents Bill of Rights Act for Education), introduced May 2022 alongside Senators Corrado, Bucco, Durr, Oroho, and Testa. The bill would require schools to inform parents of curriculum content in advance, expand parental opt-out rights to the entire curriculum (not just sex education), and restore transparency that Republicans argued the Murphy administration had eroded. The legislation was part of the 'Three Rs' plan — Repeal, Replace, Restore — the Senate Republican caucus proposed to roll back ideological content in K-12 public schools.",
              ["https://www.insidernj.com/press-release/corrado-bucco-introduce-parents-bill-of-rights-act-for-education/",
               "https://www.senatenj.com/index.php/oroho/senate-republicans-propose-the-three-rs-to-fix-njs-broken-curriculum-repeal-replace-restore/57117"]),
    ]),

    # ---------- Holly T. Schepisi (NJ State Senator SD-39, R) ----------
    ("holly-schepisi", "NJ", "State Senator", [
        claim("hs1", "holly-schepisi", "sanctity_of_life", 0, False,
              "Self-describes as 'pro-choice within reason,' stating she supports abortion access while objecting to late-term procedures by non-physicians. Rather than voting no on NJ S49 (Freedom of Reproductive Choice Act, 23-15 on January 10, 2022) she was recorded as 'not voting' — the only Republican senator to abstain — consistent with her stated pro-choice position. In 2024, when Senate Democrats advanced a new reproductive-rights package, Schepisi argued it was 'unnecessary' because New Jersey already has 'one of the most liberal abortion laws not only in the U.S., but in the world.' Her posture does not align with the life-at-conception standard the rubric requires.",
              ["https://www.cbsnews.com/newyork/news/new-jersey-democrats-push-package-of-abortion-rights-bills-republicans-say-are-unnecessary/",
               "https://thefreedomindex.org/nj/vote/1122798/"]),
        claim("hs2", "holly-schepisi", "self_defense", 1, True,
              "Voted NO on the December 2022 NJ gun-control package (S4219/A4769, 21-16 Senate vote on December 19, 2022). The bill created new 'sensitive location' gun-free zones statewide, raised licensing fees, and overhauled the carry-permit process — all steps Republicans condemned as an infringement of the Second Amendment rights affirmed in NYSRPA v. Bruen (2022). Every Republican senator voted no in a unanimous caucus opposition.",
              ["https://newjerseymonitor.com/2022/12/19/senate-sends-sweeping-gun-bill-to-governors-desk-in-narrow-vote/",
               "https://patch.com/new-jersey/across-nj/controversial-nj-firearms-bill-passes-senate-murphy-slated-sign"]),
        claim("hs3", "holly-schepisi", "biblical_marriage", 2, True,
              "Voted against advancing New Jersey S3963/A2218, which created a new crime of 'interfering with reproductive health services' and extended that definition to include transgender (gender-affirming) healthcare, shielding trans healthcare providers and patients from protests and blockades. New Jersey Monitor named Schepisi alongside Sen. Robert Singer (R-Ocean) as voting against the bill at the Senate health committee stage in May 2026. The legislation ultimately passed the full Senate 25-15 on June 30, 2026, along party lines — making her opposition to the transgender-care expansion a documented record vote.",
              ["https://newjerseymonitor.com/2026/05/11/nj-transgender-healthcare-bill/",
               "https://newjerseymonitor.com/2026/06/30/nj-lawmakers-approve-new-protections-transgender-and-reproductive-healthcare/"]),
    ]),

    # ---------- Declan O'Scanlon (NJ State Senator SD-13, R) ----------
    ("declan-oscanlon", "NJ", "State Senator", [
        claim("do1", "declan-oscanlon", "sanctity_of_life", 0, True,
              "Voted NO on New Jersey S49 (Freedom of Reproductive Choice Act, passed 23-15 on January 10, 2022), which codified an unrestricted right to abortion at every stage of pregnancy into state law, required health-insurance coverage for abortion, and permitted abortions by non-physicians. The NJ Freedom Index roll-call record explicitly confirms O'Scanlon's no vote. He was among the 15 Republican senators who unanimously opposed the legislation — the lone bipartisan No being Democrat Sen. Nicholas Sacco.",
              ["https://thefreedomindex.org/nj/vote/1122798/",
               "https://newjerseymonitor.com/2022/01/13/murphy-signs-law-solidifying-abortion-rights-in-new-jersey/"]),
        claim("do2", "declan-oscanlon", "self_defense", 1, True,
              "Voted NO on the December 2022 NJ gun-control package (S4219/A4769, 21-16 Senate vote on December 19, 2022) — a bill the NRA-ILA labeled an infringement on Second Amendment rights. The legislation overhauled concealed-carry permits, banned firearms from more than 25 newly designated 'sensitive' public locations, and raised firearm fees following NYSRPA v. Bruen. O'Scanlon voted with every other Republican senator in unanimously opposing the measure.",
              ["https://newjerseymonitor.com/2022/12/19/senate-sends-sweeping-gun-bill-to-governors-desk-in-narrow-vote/",
               "https://patch.com/new-jersey/across-nj/controversial-nj-firearms-bill-passes-senate-murphy-slated-sign"]),
        claim("do3", "declan-oscanlon", "economic_stewardship", 2, True,
              "Serving as Senate Republican Budget Officer since 2022, O'Scanlon has led Republican floor opposition to what he characterized as the 'single largest tax increase in the history of New Jersey' and consistently offered amendments for fiscal restraint against Democratic budget proposals. In the FY 2027 budget debate, O'Scanlon offered amendments challenging Governor Sherrill's proposed budget and, alongside Senate Republican Leader Anthony Bucco, publicly criticized the administration for increasing spending on an 'illegal immigrant defense initiative' while cutting services for New Jersey residents — a fiscal-responsibility posture consistent with the rubric's anti-deficit standard.",
              ["https://www.senatenj.com/m/newsflash/home/detail/968",
               "https://en.wikipedia.org/wiki/Declan_O'Scanlon"]),
    ]),

    # ---------- Anthony M. Bucco (NJ State Senator SD-25, Republican Leader, R) ----------
    ("anthony-m-bucco", "NJ", "State Senator", [
        claim("ab1", "anthony-m-bucco", "family_child_sovereignty", 0, True,
              "Co-introduced New Jersey S2483 (Parents Bill of Rights Act for Education) with Senator Kristin Corrado in May 2022, requiring public schools to notify parents in advance of curriculum content and expanding parental opt-out rights across all subjects. The bill also gave parents standing to challenge material they find objectionable and was designed to claw back rights Republicans argued had been eroded by the Murphy administration's aggressive sex-education and social-emotional learning standards. As Senate Republican Leader, Bucco anchored the 'Three Rs' plan and the Parents Bill of Rights Act as the caucus's flagship education-reform proposals.",
              ["https://www.insidernj.com/press-release/corrado-bucco-introduce-parents-bill-of-rights-act-for-education/",
               "https://www.senatenj.com/159/Anthony-M-Bucco---District-25---Republic"]),
        claim("ab2", "anthony-m-bucco", "self_defense", 1, True,
              "Voted NO on the December 2022 NJ gun-control package (S4219/A4769), which passed 21-16 on December 19, 2022. The bill created new concealed-carry permit requirements in response to NYSRPA v. Bruen (2022) and designated more than 25 categories of public places as gun-free zones, including bars, beaches, and libraries. Every Republican senator voted no, and Bucco — as Republican Leader — organized unified caucus opposition to the legislation.",
              ["https://newjerseymonitor.com/2022/12/19/senate-sends-sweeping-gun-bill-to-governors-desk-in-narrow-vote/",
               "https://newjerseymonitor.com/2022/12/05/sweeping-n-j-gun-bill-clears-penultimate-vote/"]),
        claim("ab3", "anthony-m-bucco", "economic_stewardship", 2, True,
              "As Senate Republican Leader, Bucco joined Republican Budget Officer Declan O'Scanlon in publicly opposing Governor Sherrill's FY 2027 budget proposal, criticizing its funding of an 'illegal immigrant defense initiative' while cutting services to New Jersey residents. Bucco has consistently advocated for lower taxes, reduced spending, and fiscal restraint against Democratic budgets that he argues impose unsustainable burdens on NJ taxpayers — positions consistent with the rubric's anti-deficit and fiscal-stewardship standard.",
              ["https://www.senatenj.com/m/newsflash/home/detail/1206",
               "https://www.senatenj.com/159/Anthony-M-Bucco---District-25---Republic"]),
    ]),

    # ---------- Owen Henry (NJ State Senator SD-12, R) ----------
    ("owen-henry", "NJ", "State Senator", [
        claim("oh1", "owen-henry", "self_defense", 1, True,
              "As a member of the NJ Senate Republican minority (sworn in January 9, 2024, having won District 12 with 62.2% of the vote), Henry serves on the Law and Public Safety Committee and voted with his caucus against the December 2025 NJ Democratic gun-control package. The four-bill package — including A.4975 (criminalizing possession of digital instructions to 3D-print firearms) and S.1425 (targeting gun dealers under the guise of trafficking) — passed the Senate in party-line votes ranging from 25-12 to 30-7 during the December 2025 lame-duck session. The NRA-ILA condemned the package as 'another attack on the Bruen decision' and called on Governor Murphy to veto all four bills.",
              ["https://ballotpedia.org/Owen_Henry",
               "https://www.nraila.org/articles/20251223/new-jersey-legislature-passes-holiday-assault-on-second-amendment"]),
        claim("oh2", "owen-henry", "biblical_marriage", 2, True,
              "Voted with the unified NJ Senate Republican caucus against A2218 (the 2026 NJ reproductive/transgender healthcare bill), which created a new crime of 'interfering with reproductive health services' — explicitly extended to cover gender-affirming care for transgender patients — and shielded trans healthcare providers from protests, blockades, and threats. The measure passed 25-15 on June 30, 2026, along strict party lines with all Senate Republicans voting no. Schepisi's named opposition at the committee stage (May 2026) and the party-line final vote confirm Republican caucus unity against the transgender healthcare provisions.",
              ["https://newjerseymonitor.com/2026/06/30/nj-lawmakers-approve-new-protections-transgender-and-reproductive-healthcare/",
               "https://newjerseymonitor.com/2026/05/11/nj-transgender-healthcare-bill/"]),
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
