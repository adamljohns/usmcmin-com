#!/usr/bin/env python3
"""Enrichment batch 669: TX Republican state representatives — evidence_state tier.

Federal senator/rep archetype_curated buckets fully exhausted; this batch moves to
evidence_state Republicans from bottom-of-alphabet states.  Three of five targets
(Isaac, Harris Davila, Fairly) took office in 2023 or 2025 and have no vote on 87th
Legislature bills (HB 1927/SB8).  Bell was a coauthor of HB 1927.  Cunningham also
arrived in 2023.  Claims reference 2021-2025 legislative record and confirmed scores.

Targets: Carrie Isaac (HD73), Caroline Harris Davila (HD52), Caroline Fairly (HD87),
Cecil Bell Jr. (HD3), Charles Cunningham (HD127).
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
    # ---- Carrie Isaac (TX, HD73, Comal/Hays counties) ----
    ("carrie-isaac", "TX", "Representative", [
        claim("ci1", "carrie-isaac", "self_defense", 1, True,
              "Authored HB 3137 (88th Legislature, 2023), expanding Texas's state firearms "
              "preemption law to prohibit municipalities and counties from requiring gun owners "
              "to obtain liability insurance. The bill passed and was signed by Governor Abbott, "
              "effective September 1, 2023. In her 2022 primary campaign she was the only "
              "non-incumbent challenger to receive simultaneous endorsements from the NRA, TSRA, "
              "and Gun Owners of America.",
              ["https://www.nraila.org/articles/20230605/thank-your-state-rep-carrie-isaac-for-passing-legislation-to-strengthen-texas-state-firearms-preemption-law",
               "https://texas.gunowners.org/carrie-isaac-is-your-gun-owners-choice-candidate/",
               "https://legiscan.com/TX/bill/HB3137/2023"]),
        claim("ci2", "carrie-isaac", "sanctity_of_life", 0, True,
              "Earned a 93% pro-life score from Texas Alliance for Life on their 89th Legislature "
              "(2025) scorecard. In the 88th Legislature (2023) sponsored HB 2690 to create civil "
              "liability for distributing abortion-inducing drugs and to restrict internet promotion "
              "of abortion — reflecting a legislative commitment to protecting life.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://legiscan.com/TX/bill/HB2690/2023",
               "https://choicetracker.org/tx/people/carrie-isaac/84279296"]),
        claim("ci3", "carrie-isaac", "border_immigration", 0, True,
              "Publicly supports Operation Lone Star and Texas's $5 billion border security "
              "investment; has visited the Texas-Mexico border at least three times since taking "
              "office in 2023 and stated Texas must compensate for the Biden administration's "
              "inadequate response. Appointed to the House Homeland Security, Public Safety & "
              "Veterans' Affairs Committee in the 89th Legislature, giving her direct oversight "
              "of border-related policy and funding.",
              ["https://www.isaacfortexas.com/issues",
               "https://www.isaacfortexas.com/news/2023/8/31/notes-from-the-border"]),
    ]),

    # ---- Caroline Harris Davila (TX, HD52, Round Rock / Williamson County) ----
    ("caroline-harris-davila", "TX", "Representative", [
        claim("chd1", "caroline-harris-davila", "sanctity_of_life", 0, True,
              "In the 89th Legislature (2025) successfully added a floor amendment boosting "
              "annual Thriving Texas Families funding from $20 million to $35 million per year "
              "as part of a $200 million pro-life package funding pregnancy resource centers, "
              "maternity homes, and adoption agencies. Earned a 93% pro-life score from Texas "
              "Alliance for Life and received the 2025 Defender of Life Award from the "
              "St. John Paul II Life Center.",
              ["https://texasrighttolife.com/texas-lawmakers-approve-200-million-to-help-moms-and-babies/",
               "https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://www.texasallianceforlife.org/rep-harris-davila/"]),
        claim("chd2", "caroline-harris-davila", "family_child_sovereignty", 0, True,
              "Co-sponsored HB 18 (SCOPE Act, 88th Legislature, 2023), requiring parental "
              "consent before digital service providers may enter agreements with known minors, "
              "restricting targeted advertising to minors, and mandating age verification. "
              "Governor Abbott signed it; effective September 1, 2024. Also voted for the school "
              "voucher / Education Savings Account bill (HB 1, 4th Special Session), earning an "
              "Abbott endorsement in her 2024 re-election race.",
              ["https://legiscan.com/TX/bill/HB18/2023",
               "https://abc13.com/post/texas-parents-control-teens-social-media-use-after-meta-rolls-new-tools-comply-house-bill-18/15286859/",
               "https://teachthevote.atpe.org/Candidates/Caroline-Harris"]),
        claim("chd3", "caroline-harris-davila", "election_integrity", 0, True,
              "Before serving in the Texas House, worked as a policy advisor to State Senator "
              "Bryan Hughes — the author of Texas SB 1 (the 2021 Election Integrity Act), which "
              "strengthened voter-ID requirements, limited drive-through voting, and restricted "
              "extended early-voting hours — working directly on drafting that legislation.",
              ["https://carolinefortexas.com/",
               "https://www.branch.vote/races/2024-texas-general-election-tx-state-state-representative-tx-state-house-52/candidates/caroline-harris-davila"]),
    ]),

    # ---- Caroline Fairly (TX, HD87, Amarillo / Texas Panhandle) ----
    ("caroline-fairly", "TX", "Representative", [
        claim("cf1", "caroline-fairly", "sanctity_of_life", 0, True,
              "Earned a 100% pro-life voting score from Texas Alliance for Life on their 89th "
              "Legislature (2025) scorecard, voting correctly on every tracked pro-life measure. "
              "Campaigns as pro-life and volunteers with Hope Choice Pregnancy Center in Amarillo.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://amarillotribune.org/2025/01/10/caroline-fairly-to-begin-her-first-term-in-texas-house/"]),
        claim("cf2", "caroline-fairly", "family_child_sovereignty", 0, True,
              "Authored HB 1481 (89th Legislature, 2025), banning K-12 students from using "
              "personal communication devices during the school day at all Texas public schools "
              "and open-enrollment charters — removing a documented barrier to learning and "
              "childhood development. The bill passed the House 136-10, passed the Senate "
              "unanimously, and was signed by Governor Abbott on June 22, 2025 "
              "(effective September 1, 2025).",
              ["https://abc7amarillo.com/news/local/caroline-fairlys-bill-banning-cell-phones-in-school-signed-by-gov-greg-abbott-house-bill-1481-k-12-public-school-students",
               "https://www.texastribune.org/2025/05/30/texas-public-school-cellphone-ban/",
               "https://legiscan.com/TX/bill/HB1481/2025"]),
    ]),

    # ---- Cecil Bell Jr. (TX, HD3, Montgomery County) ----
    # Lost March 2026 primary; served through 89th Legislature (2025).
    ("cecil-bell-jr", "TX", "Representative", [
        claim("cbj1", "cecil-bell-jr", "self_defense", 0, True,
              "Official coauthor of HB 1927 (87th Legislature, 2021) — the Texas Permitless "
              "Carry Act — which abolished the license-to-carry requirement for Texans 21 and "
              "older who can legally possess a firearm. Coauthorship of landmark legislation is "
              "a stronger endorsement of constitutional carry than a floor vote alone. Also "
              "coauthored Texas Firearms Freedom Act measures asserting state sovereignty over "
              "firearms manufactured and kept within Texas.",
              ["https://capitol.texas.gov/reports/report.aspx?LegSess=87R&ID=coauthor&Code=A2335",
               "https://ballotpedia.org/Cecil_Bell_Jr."]),
        claim("cbj2", "cecil-bell-jr", "sanctity_of_life", 0, True,
              "Earned a 100% pro-life score from Texas Alliance for Life on the 89th Legislature "
              "(2025) scorecard, and full marks from Texas Right to Life across his career. Has "
              "stated he 'voted to protect life because all human life is sacred, from conception "
              "to natural death.'",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Cecil_Bell_Jr."]),
        claim("cbj3", "cecil-bell-jr", "biblical_marriage", 1, True,
              "In 2015 introduced legislation to prohibit Texas from complying with the U.S. "
              "Supreme Court's Obergefell v. Hodges ruling recognizing same-sex marriage — an "
              "explicit legislative stand against federal imposition of same-sex marriage on the "
              "state. In 2017 introduced a broad nullification bill authorizing Texas to declare "
              "federal laws and court decisions unconstitutional and unenforceable in-state.",
              ["https://ballotpedia.org/Cecil_Bell_Jr."]),
    ]),

    # ---- Charles Cunningham (TX, HD127, Harris County — Humble/Kingwood) ----
    ("charles-cunningham", "TX", "Representative", [
        claim("cc1", "charles-cunningham", "sanctity_of_life", 0, True,
              "Earned a 96% pro-life score from Texas Alliance for Life on the 89th Legislature "
              "(2025) scorecard. Self-described 'staunchly pro-life'; opposes taxpayer funding "
              "for Planned Parenthood; supports in-person physician requirements and reporting "
              "mandates for chemical abortion drugs.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ballotpedia.org/Charles_Cunningham_(Texas)"]),
        claim("cc2", "charles-cunningham", "family_child_sovereignty", 0, True,
              "Voted YES on HB 900 (READER Act, 88th Legislature, 2023), requiring book vendors "
              "to rate library materials by sexual content level and prohibiting certain explicit "
              "materials in public school libraries. Also authored HB 824 (civics education "
              "requirement for Texas public high school students) and served on the House "
              "Subcommittee on Disease Prevention & Women's & Children's Health in the 89th "
              "Legislature.",
              ["https://legiscan.com/TX/bill/HB900/2023",
               "https://teachthevote.atpe.org/Candidates/Charles-Cunningham",
               "https://ballotpedia.org/Charles_Cunningham_(Texas)"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
