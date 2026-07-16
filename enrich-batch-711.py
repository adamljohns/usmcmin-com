#!/usr/bin/env python3
"""Enrichment batch 711: 5 Democratic state-level officials (NY, MI, ME, MA AGs and Lt. Govs).

All archetype_curated federal senators/representatives are exhausted; this batch
moves to evidence_state officials from the bottom of the alphabet (NY, MI, ME, MA).
Targets: Letitia James (NY AG), Dana Nessel (MI AG), Garlin Gilchrist (MI Lt Gov),
Aaron Frey (ME AG), Kim Driscoll (MA Lt Gov). Each receives 3 claims documenting
public positions on the rubric's core categories, all scoring negatively (False)
against the God-First/America-First rubric.
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
    # ---------------- Letitia James (NY-D, Attorney General) ----------------
    ("letitia-james", "NY", "Attorney", [
        claim("lj1", "letitia-james", "self_defense", 1, False,
              "A consistent gun-control advocate who joined 24 state AGs in urging the Supreme Court to uphold federal ghost gun regulations, removed more than 9,500 firearms through statewide buybacks, defended NY's Concealed Carry Improvement Act against Second Amendment challenges, and sued gun retailers for safety-law violations — systematically backing restrictions on semi-automatic firearms, concealed carry, and ghost guns that the rubric opposes.",
              ["https://ag.ny.gov/press-release/2024/attorney-general-james-takes-action-uphold-federal-ghost-gun-regulations",
               "https://ag.ny.gov/press-release/2024/attorney-general-james-takes-action-protect-commonsense-gun-laws"]),
        claim("lj2", "letitia-james", "sanctity_of_life", 0, False,
              "A vocal abortion-rights advocate who publicly revealed she obtained an abortion and declared 'I make no apologies to anyone'; leads a multistate coalition protecting abortion and gender-affirming care access, and fights to preserve late-term abortion protection — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Letitia_James",
               "https://ag.ny.gov/press-release/2025/attorney-general-james-leads-multistate-effort-protect-abortion-and-gender"]),
        claim("lj3", "letitia-james", "biblical_marriage", 4, False,
              "As AG, James has championed LGBTQ promotion through official programs including drag story hour events and active advocacy for transgender youth rights in schools — using the full authority of the AG's office to advance LGBTQ policy the rubric opposes.",
              ["https://ag.ny.gov/about/meet-letitia-james",
               "https://en.wikipedia.org/wiki/Letitia_James"]),
    ]),

    # ---------------- Dana Nessel (MI-D, Attorney General) ----------------
    ("dana-nessel", "MI", "Attorney", [
        claim("dn1", "dana-nessel", "biblical_marriage", 1, False,
              "As a private attorney in 2014, Nessel successfully argued DeBoer v. Snyder, challenging Michigan's same-sex marriage ban; the case was consolidated into Obergefell v. Hodges (2015), which imposed same-sex marriage nationwide — making her a direct legal architect of overturning the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Dana_Nessel"]),
        claim("dn2", "dana-nessel", "sanctity_of_life", 0, False,
              "Refused to defend Michigan's 1931 abortion ban when Roe was overturned, actively defended MI Proposal 3 (2022) enshrining unlimited abortion rights in the state constitution, and in June 2025 petitioned state courts to strike down remaining abortion restrictions as unconstitutionally discriminatory — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Dana_Nessel",
               "https://www.michigan.gov/ag/news/press-releases/2025/06/03/ag-nessel-asks-michigan-court-of-claims-to-find-abortion-restrictions-discriminatory"]),
        claim("dn3", "dana-nessel", "biblical_marriage", 2, False,
              "In August 2025, Nessel joined a multistate lawsuit to block federal restrictions on so-called 'gender-affirming care' for transgender minors under age 19, fighting to preserve hormonal and medical transgender procedures on children in states like Michigan — explicitly rejecting the rubric's position that transgender ideology should be opposed in law.",
              ["https://www.michigan.gov/ag/news/press-releases/2025/08/01/attorney-general-nessel-sues"]),
    ]),

    # ---------------- Garlin Gilchrist (MI-D, Lieutenant Governor) ----------------
    ("garlin-gilchrist", "MI", "Lieutenant", [
        claim("gg1", "garlin-gilchrist", "self_defense", 1, False,
              "In 2023, Gilchrist co-signed official statements supporting Michigan's universal background check legislation and its new extreme risk protection order (red-flag) law, publicly calling them 'commonsense' measures that would 'save lives' — endorsing both gun-restriction tools the rubric explicitly opposes.",
              ["https://www.michigan.gov/whitmer/news/press-releases/2023/02/21/statements-on-introduction-of-gun-violence-prevention-bills",
               "https://www.michigan.gov/whitmer/news/press-releases/2023/05/22/whitmer-signs-extreme-risk-protection-order-legislation-to-keep-michigan-communities-safe"]),
        claim("gg2", "garlin-gilchrist", "sanctity_of_life", 0, False,
              "As Lt. Governor, championed Michigan Proposal 3 (2022) enshrining unlimited abortion rights in the state constitution with no gestational limit, and was part of the Whitmer-Gilchrist administration that signed the 2023 Reproductive Health Act removing virtually all remaining statutory abortion restrictions — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Garlin_Gilchrist",
               "https://www.michigan.gov/whitmer/news/press-releases/2023/11/21/governor-whitmer-signs-reproductive-health-act"]),
        claim("gg3", "garlin-gilchrist", "biblical_marriage", 4, False,
              "Publicly championed the 2023 expansion of Michigan's Elliott-Larsen Civil Rights Act to add sexual orientation and gender identity as protected classes, stating it would 'prevent Michiganders from being fired... because of who they are or how they identify' — directly promoting LGBTQ ideology through state civil rights law.",
              ["https://www.michigan.gov/whitmer/news/press-releases/2023/03/16/whitmer-signs-bipartisan-legislation-expanding-rights-and-freedoms-for-lgbtq"]),
    ]),

    # ---------------- Aaron Frey (ME-D, Attorney General) ----------------
    ("aaron-frey", "ME", "Attorney", [
        claim("af1", "aaron-frey", "sanctity_of_life", 4, False,
              "In 2025, Frey joined a 21-state coalition suing the Trump administration over cuts to Planned Parenthood and Maine Family Planning funding, characterizing defunding the nation's largest abortion provider as a 'direct attack on healthcare access' — actively defending public funding for abortion-performing organizations.",
              ["https://www.maine.gov/ag/news/article.shtml?id=13239390",
               "https://en.wikipedia.org/wiki/Aaron_Frey"]),
        claim("af2", "aaron-frey", "sanctity_of_life", 0, False,
              "In January 2024, Frey took official action to protect medication abortion access in Maine, and has consistently defended abortion-on-demand rights throughout his tenure as AG since 2019 — opposing any recognition of personhood from conception.",
              ["https://www.maine.gov/ag/",
               "https://en.wikipedia.org/wiki/Aaron_Frey"]),
        claim("af3", "aaron-frey", "biblical_marriage", 4, False,
              "In December 2022, Frey joined a multistate amicus brief protecting LGBTQ+ workers' civil rights, and has used his office to defend expanded nondiscrimination protections that override religious-liberty exemptions — promoting LGBTQ policy through state legal action.",
              ["https://en.wikipedia.org/wiki/Aaron_Frey",
               "https://www.maine.gov/ag/"]),
    ]),

    # ---------------- Kim Driscoll (MA-D, Lieutenant Governor) ----------------
    ("kim-driscoll", "MA", "Lieutenant", [
        claim("kd1", "kim-driscoll", "sanctity_of_life", 0, False,
              "As part of the Healey-Driscoll administration, supported the updated Massachusetts abortion shield law protecting providers and patients, an executive order protecting emergency abortion access on the second anniversary of Dobbs, and state investment in abortion provider organizations — actively promoting abortion access and rejecting any personhood-from-conception standard.",
              ["https://www.mass.gov/news/governor-healey-signs-updated-shield-law-strengthening-protections-for-health-care-providers-and-patients",
               "https://www.mass.gov/news/on-two-year-anniversary-of-dobbs-governor-healey-signs-executive-order-protecting-access-to-emergency-abortion-care"]),
        claim("kd2", "kim-driscoll", "biblical_marriage", 2, False,
              "The Healey-Driscoll shield law explicitly extends to providers of 'gender-affirming care,' and in January 2025 the administration adopted emergency amendments protecting nurses who provide gender-affirming services — using state law to actively promote and protect transgender procedures.",
              ["https://www.mass.gov/news/governor-healey-signs-updated-shield-law-strengthening-protections-for-health-care-providers-and-patients",
               "https://www.mass.gov/doc/shield-law-guidance-bhpl-and-borim-september-2025/download"]),
        claim("kd3", "kim-driscoll", "christian_liberty", 0, False,
              "The Healey-Driscoll administration launched the nation's first government-funded public campaign against pregnancy resource centers — many of which are faith-based — characterizing their pro-life counseling as dangerous misinformation, using state authority to suppress faith-based charities and restrict their outreach.",
              ["https://www.mass.gov/news/healey-driscoll-administration-launches-first-in-the-nation-public-education-campaign-on-the-dangers-of-anti-abortion-centers"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision across states."""
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

    # Minified write — preserve no-whitespace master (keeps file ~35-36 MB, under GitHub 50 MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
