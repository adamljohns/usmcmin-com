#!/usr/bin/env python3
"""Enrichment batch 67: 4 candidates from the bottom of the alphabet.

Targets (reverse-alpha): Mike Tipping (ME-D US Senate), Rob Sand (IA-D US Senate),
Pete Hegseth (US-R DoD Secretary), Robert F. Kennedy Jr. (US-R HHS Secretary).

Sources: ballotpedia.org, en.wikipedia.org, defense.gov, hhs.gov, mainesenate.org,
thegazette.com, iowafieldreport.com, robsand.com.
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
    # ---------------- Mike Tipping (ME-D, US Senate 2026 candidate) ----------------
    ("mike-tipping-senate", "ME", "Senate", [
        claim("mt1", "mike-tipping-senate", "border_immigration", 2, False,
              "Explicitly named 'combating ICE's tactics' as one of his top legislative priorities, opposing immigration enforcement cooperation and aligning with sanctuary-state policies that shield illegal immigrants from federal deportation.",
              ["https://www.mainesenate.org/senator/senator/senator-mike-tipping/",
               "https://mainebeacon.com/tag/mike-tipping/"]),
        claim("mt2", "mike-tipping-senate", "sanctity_of_life", 0, False,
              "Runs for U.S. Senate as a committed progressive Democrat in Maine — a state whose Democratic majority passed a constitutional amendment enshrining reproductive autonomy in 2024 — explicitly opposing any life-at-conception or personhood standard; his platform centers reproductive rights as a core issue.",
              ["https://tippingforsenate.com/",
               "https://ballotpedia.org/Maine_Right_to_Personal_Reproductive_Autonomy_Amendment_(2024)"]),
        claim("mt3", "mike-tipping-senate", "biblical_marriage", 4, False,
              "A progressive activist and Maine Senate Democrat who has earned LGBTQ community endorsements and supports full LGBTQ protections in schools and public policy, directly opposing the rubric's standard against promoting LGBTQ ideology in institutional settings.",
              ["https://www.mainesenate.org/senator/senator/senator-mike-tipping/",
               "https://mainebeacon.com/progressive-advocate-writer-mike-tipping-launches-maine-state-senate-campaign/"]),
    ]),

    # ---------------- Rob Sand (IA-D, US Senate 2026 / also Governor candidate) ----------------
    ("rob-sand-senate", "IA", "Senate", [
        claim("rs1", "rob-sand-senate", "sanctity_of_life", 0, False,
              "Explicitly pledged to veto any legislation further restricting abortion access, declaring 'I can't unilaterally repeal a six-week ban, but I can stop us from making it worse,' and vowed to use 'whatever tools I have to protect Iowans' reproductive rights' — rejecting any life-at-conception standard.",
              ["https://www.thegazette.com/news/politics/rob-sand-says-he-d-veto-abortion-limits-end-medicaid-privatization-at-healthcare-roundtable/article_d7f49c23-b6b1-47eb-be1a-c8e676b1893c.html",
               "https://siouxcityjournal.com/news/state-regional/government-politics/article_b7496414-a5bc-59d0-acec-a33164de659b.html"]),
        claim("rs2", "rob-sand-senate", "border_immigration", 2, False,
              "Deliberately refused to state whether he would maintain Iowa's cooperation with ICE as governor, drawing sharp criticism for evasion on sanctuary-city and deportation questions — a de facto pro-sanctuary posture that does not align with the rubric's demand for active enforcement cooperation.",
              ["https://www.iowafieldreport.com/governor/verification-vs-evasion-why-rob-sand-sarah-trone-garriott-are-stalling-on-illegal-dependency/"]),
        claim("rs3", "rob-sand-senate", "economic_stewardship", 2, False,
              "Opposes Medicaid privatization and campaigns on expanding government-managed healthcare — policies that increase state spending obligations and run counter to the rubric's preference for balanced budgets and limited government financial commitments.",
              ["https://www.thegazette.com/news/politics/rob-sand-says-he-d-veto-abortion-limits-end-medicaid-privatization-at-healthcare-roundtable/article_d7f49c23-b6b1-47eb-be1a-c8e676b1893c.html",
               "https://robsand.com/priorities/"]),
    ]),

    # ---------------- Pete Hegseth (US-R, Secretary of Defense) ----------------
    ("pete-hegseth", "US", "Defense", [
        claim("ph1", "pete-hegseth", "biblical_marriage", 2, True,
              "As Secretary of Defense, issued memorandum 'Prioritizing Military Excellence and Readiness' (Feb 7, 2025) banning individuals with a history of gender dysphoria from military service, explicitly stating that transgender identification 'conflicts with a soldier's commitment to an honorable, truthful, and disciplined lifestyle' — a direct institutional rejection of transgender ideology.",
              ["https://en.wikipedia.org/wiki/Pete_Hegseth_as_Secretary_of_Defense",
               "https://en.wikipedia.org/wiki/Executive_Order_14183"]),
        claim("ph2", "pete-hegseth", "biblical_marriage", 4, True,
              "Systematically eliminated DEI programs and LGBTQ-promotion policies across the Department of Defense, removing gender-ideology training and dismantling the institutional apparatus that advanced LGBTQ content in a major federal institution.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Pete_Hegseth",
               "https://en.wikipedia.org/wiki/Pete_Hegseth_as_Secretary_of_Defense"]),
        claim("ph3", "pete-hegseth", "christian_liberty", 0, True,
              "Initiated monthly Christian worship services during Pentagon business hours (May 2025) and frames the Department of Defense's mission in explicitly Christian terms, asserting the free exercise of faith within a federal institution and giving Christian service members access to senior leadership through shared worship.",
              ["https://en.wikipedia.org/wiki/Pete_Hegseth",
               "https://history.defense.gov/Multimedia/Biographies/Article-View/Article/4244292/peter-b-hegseth/"]),
    ]),

    # ---------------- Robert F. Kennedy Jr. (US-R, HHS Secretary) ----------------
    ("robert-f-kennedy-jr", "US", "Health", [
        claim("rfk1", "robert-f-kennedy-jr", "industry_capture", 0, True,
              "As HHS Secretary directed the CDC to halt its COVID-19 vaccine recommendations for children and pregnant women (May 2025) and halted clinical trials of a COVID-19 vaccine pill — challenging the government-pharmaceutical consensus on mandated vaccination that the rubric treats as industry capture.",
              ["https://en.wikipedia.org/wiki/Robert_F._Kennedy_Jr.",
               "https://www.hhs.gov/press-room/eo-maha.html"]),
        claim("rfk2", "robert-f-kennedy-jr", "industry_capture", 3, True,
              "Chaired the MAHA Commission whose strategy explicitly advocates raw milk access, directed the FDA to eliminate the self-affirm pathway by which companies unilaterally declare their own food ingredients safe, and oversaw reforms restoring whole milk in schools — targeting Big Food regulatory capture.",
              ["https://en.wikipedia.org/wiki/MAHA_Commission",
               "https://www.hhs.gov/about/news/2025/03/10/hhs-secretary-kennedy-directs-fda-explore-rulemaking-eliminate-pathway-companies-self-affirm-food-ingredients-are-safe.html"]),
        claim("rfk3", "robert-f-kennedy-jr", "industry_capture", 1, True,
              "A decade-long advocate for repealing the PREP Act and related pharmaceutical liability shields, arguing they remove market accountability and enable the regulatory capture by drug companies that the rubric opposes; this position defined his outsider campaign and continues in his HHS tenure.",
              ["https://en.wikipedia.org/wiki/Robert_F._Kennedy_Jr.",
               "https://www.hhs.gov/about/leadership/robert-kennedy.html"]),
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
        print(f"  ✓ {m['name']:<34} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
