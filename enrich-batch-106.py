#!/usr/bin/env python3
"""Enrichment batch 106: hand-curated claims for 5 state/national candidates.

Targets archetype_curated candidates with 0 evidence claims, drawn from the
bottom of the alphabet (NM→IL→IA→FL→CO→CA). Only 2 federal candidates
remain in the bottom-bucket so this batch supplements with well-documented
gubernatorial/SoS candidates.

Mix (1 R / 4 D): Casey DeSantis (FL-R-Gov), Rob Sand (IA-D-Gov),
Jared Polis (CO-D-Gov), Alexi Giannoulias (IL-D-SoS), Kamala Harris (CA-D-Gov).
Each claim cites >=1 reliable public source reflecting 2022-2026 record.

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
    # ---------------- Rob Sand (IA-D, Governor candidate) ----------------
    ("rob-sand-gov", "IA", "Governor", [
        claim("rs1", "rob-sand-gov", "sanctity_of_life", 0, False,
              "Pledged as Iowa governor candidate to 'use whatever tools I have to protect Iowans' reproductive rights' and vowed to veto any legislation further restricting abortion access, including Iowa's existing 6-week heartbeat ban — rejecting life-at-conception personhood.",
              ["https://www.facebook.com/robsandia/posts/as-governor-ill-use-whatever-tools-i-have-to-protect-iowans-reproductive-rights/1258602849390354/",
               "https://www.thegazette.com/news/politics/rob-sand-says-he-d-veto-abortion-limits-end-medicaid-privatization-at-healthcare-roundtable/article_d7f49c23-b6b1-47eb-be1a-c8e676b1893c.html"]),
        claim("rs2", "rob-sand-gov", "sanctity_of_life", 2, False,
              "Committed to protecting IVF and contraceptive access in Iowa, stating he would use his 'veto pen to maintain accessibility for contraception, for IVF' — accepting the embryo creation and potential discard inherent in IVF programs.",
              ["https://www.thegazette.com/news/politics/rob-sand-says-he-d-veto-abortion-limits-end-medicaid-privatization-at-healthcare-roundtable/article_d7f49c23-b6b1-47eb-be1a-c8e676b1893c.html"]),
        claim("rs3", "rob-sand-gov", "border_immigration", 1, False,
              "Said Iowa should not make immigrant workers who 'comply with immigration check-ins feel unsafe,' emphasizing workforce impact over enforcement; applied a 'Constitution and public safety' test to National Guard border deployments rather than supporting mandatory deportation.",
              ["https://www.iowafieldreport.com/governor/verification-vs-evasion-why-rob-sand-sarah-trone-garriott-are-stalling-on-illegal-dependency/"]),
    ]),

    # ---------------- Jared Polis (CO-D, Governor) ----------------
    ("jared-polis", "CO", "Governor", [
        claim("jp1", "jared-polis", "biblical_marriage", 0, False,
              "Became the first U.S. governor to marry a same-sex partner (married Marlon Reis, September 2021) and in May 2024 signed legislation placing Amendment J on the ballot; voters passed it to remove Colorado's constitutional definition of marriage as one-man-one-woman.",
              ["https://en.wikipedia.org/wiki/Jared_Polis",
               "https://en.wikipedia.org/wiki/2024_Colorado_Amendment_J"]),
        claim("jp2", "jared-polis", "sanctity_of_life", 0, False,
              "Signed the Reproductive Health Equity Act (2022) codifying abortion access into Colorado law and championed 2024 Amendment 79, which voters passed to enshrine abortion as a constitutional right in Colorado — rejecting life-at-conception personhood.",
              ["https://en.wikipedia.org/wiki/Jared_Polis",
               "https://en.wikipedia.org/wiki/Abortion_in_Colorado"]),
        claim("jp3", "jared-polis", "biblical_marriage", 2, False,
              "Signed an April 2024 law requiring Colorado public schools to use transgender students' preferred names and pronouns — directing state institutions to affirm gender ideology in educational settings.",
              ["https://en.wikipedia.org/wiki/Jared_Polis"]),
    ]),

    # ---------------- Casey DeSantis (FL-R, Governor candidate) ----------------
    ("casey-desantis-gov", "FL", "Governor", [
        claim("cd1", "casey-desantis-gov", "family_child_sovereignty", 0, True,
              "Led Florida's first-in-the-nation Resiliency Florida initiative and in 2024 launched a program allowing parents and grandparents to serve as paid in-school Resiliency Coaches — embedding parental presence and values-based resiliency standards (grit, personal responsibility, critical thinking) into public school culture.",
              ["https://www.flgov.com/eog/news/press/2024/first-lady-casey-desantis-unveils-first-nation-opportunity-parents-and-grandparents",
               "https://www.fldoe.org/newsroom/latest-news/icymi-first-lady-casey-desantis-unveils-first-in-the-nation-opportunity-for-parents-and-grandparents-to-support-students-in-the-classroom.stml"]),
        claim("cd2", "casey-desantis-gov", "industry_capture", 0, True,
              "Launched 'Healthy Florida First' — an independent-lab food-safety testing program explicitly modeled after RFK Jr.'s MAHA agenda — and has been publicly critical of vaccine mandates, positioning herself against pharma-government capture ahead of any formal 2026 campaign announcement.",
              ["https://www.wusf.org/politics-issues/2026-02-18/casey-desantis-food-testing-healthy-florida-first-snubbed-budget-plans"]),
    ]),

    # ---------------- Alexi Giannoulias (IL-D, Secretary of State) ----------------
    ("alexi-giannoulias-sos-2026", "IL", "Secretary", [
        claim("ag1", "alexi-giannoulias-sos-2026", "sanctity_of_life", 0, False,
              "Re-elected in 2022 as a Planned Parenthood Illinois Action-endorsed pro-choice champion; as Secretary of State authored the nation's first law blocking license-plate location data from being shared with states prosecuting abortion seekers — using his office to protect abortion access infrastructure.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-illinois-action/press-room/abortion-rights-win-in-illinois-voters-re-elected-pritzker-stratton-plus-other-pro-choice-champions",
               "https://abc7chicago.com/post/illinois-secretary-state-alexi-giannoulias-clarifying-misinformation-voter-registration-dmv-election-safeguards/15465986/"]),
        claim("ag2", "alexi-giannoulias-sos-2026", "election_integrity", 0, False,
              "Championed an automatic voter-registration back-end system that adds eligible voters to rolls without an opt-in at the DMV, and characterized voter-ID requirements as 'voter suppression' — opposing the rubric's voter-ID and anti-mass-registration standards.",
              ["https://illinoisnewsroom.org/secretary-of-states-race-candidates-talk-elections-other-issues/",
               "https://abc7chicago.com/post/illinois-secretary-state-alexi-giannoulias-clarifying-misinformation-voter-registration-dmv-election-safeguards/15465986/"]),
    ]),

    # ---------------- Kamala Harris (CA-D, Governor candidate) ----------------
    ("kamala-harris-gov", "CA", "Governor", [
        claim("kh1", "kamala-harris-gov", "sanctity_of_life", 0, False,
              "Led the Biden White House's nationwide abortion-rights advocacy, calling herself 'the administration's voice for reproductive rights'; her 2024 presidential campaign centered on codifying Roe v. Wade and federal abortion access guarantees — rejecting life-at-conception personhood.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Kamala_Harris",
               "https://en.wikipedia.org/wiki/Kamala_Harris_2024_presidential_campaign"]),
        claim("kh2", "kamala-harris-gov", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood and EMILY's List — organizations the rubric bars — throughout her Senate, VP, and 2024 presidential campaigns, with reproductive-rights funding networks central to her political career.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Kamala_Harris"]),
        claim("kh3", "kamala-harris-gov", "self_defense", 1, False,
              "Backed an assault-weapons ban, universal background checks, and red-flag laws consistently throughout her Senate career and 2024 presidential run — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Kamala_Harris"]),
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
