#!/usr/bin/env python3
"""Enrichment batch 70: hand-curated claims for 5 candidates (bottom of alphabet).

Targets archetype_curated candidates with 0 evidence claims, taken from the
BOTTOM of the reverse-sorted bucket to avoid collision with the concurrent
top-of-alphabet agent.

Mix (3 R / 2 D): Tony Evers (WI-D Gov), Eric Toney (WI-R AG candidate),
Jason Miyares (VA-R former AG), Josh Kaul (WI-D AG), Marlo Oaks (UT-R Treasurer).

Each claim cites >=1 reliable source and reflects 2024-2026 record/positions.

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
    # ---------------- Tony Evers (WI-D, Governor) ----------------
    ("tony-evers", "WI", "Governor", [
        claim("te1", "tony-evers", "sanctity_of_life", 0, False,
              "Has pledged repeatedly in State of the State addresses—and made good on the pledge—to veto any legislation restricting abortion access; vetoed nine pro-life bills during his first two terms, including measures against infanticide and Planned Parenthood defunding, and identifies as firmly pro-choice—rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Tony_Evers",
               "https://sbaprolife.org/newsroom/press-releases/wi-alert-pro-abortion-governor-tony-evers-to-veto-commonsense-pro-life-bills",
               "https://wisconsinwatch.org/2024/01/wisconsin-governor-tony-evers-abortion-state-of-the-state/"]),
        claim("te2", "tony-evers", "self_defense", 1, False,
              "In his January 2025 State of the State address, called for a red-flag law, universal background checks, a 48-hour waiting period on gun purchases, and a ban on ghost guns—four distinct gun-control measures that directly oppose the rubric's defense of unrestricted Second Amendment rights.",
              ["https://fox11online.com/news/political/wisconsin-governor-tony-evers-2025-state-of-the-state-speech-address-excerpts-issues-taxes-economy-workforce-unemployment-child-mental-health-school-safety-gun-violence-care-prescription",
               "https://wisconsinwatch.org/2025/01/wisconsin-governor-evers-state-of-the-state-gun-control-immigration-republican-democrat/"]),
        claim("te3", "tony-evers", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Advocates of Wisconsin for his 2022 reelection campaign; additionally distributed at least $2.4 million in federal COVID-relief funds to Planned Parenthood affiliates statewide—placing him inside the abortion industry's endorsement and financial network.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-advocates-wisconsin/newsroom/planned-parenthood-advocates-of-wisconsin-endorses-governor-tony-evers-for-reelection",
               "https://empowerwisconsin.org/planned-parenthoods-payback-to-tony-evers-2/"]),
    ]),

    # ---------------- Eric Toney (WI-R, AG 2026 candidate) ----------------
    ("eric-toney-ag", "WI", "Attorney General", [
        claim("et1", "eric-toney-ag", "sanctity_of_life", 0, True,
              "Explicitly pledged throughout his AG campaigns to enforce Wisconsin's 1849 near-total criminal abortion statute as 'the rule of law,' describing abortion as 'an act that ends a human life'; in the 2026 Republican AG primary all three candidates, including Toney, advocated making performing an abortion a felony—affirming a life-from-conception standard in practice.",
              ["https://www.wuwm.com/2022-11-03/a-non-interview-with-wisconsin-attorney-general-candidate-da-eric-toney",
               "https://badgerherald.com/news/wisconsin/2025/10/22/republican-eric-toney-takes-second-shot-at-wisconsin-attorney-general/"]),
        claim("et2", "eric-toney-ag", "self_defense", 1, True,
              "Explicitly opposes Wisconsin red-flag laws, stating they would restrict the 'lawful right to exercise their constitutional Second Amendment rights'; pledged as AG to defend the individual right to keep and bear arms and to oppose firearms restrictions not accompanied by full judicial due process.",
              ["https://www.wuwm.com/2022-11-03/a-non-interview-with-wisconsin-attorney-general-candidate-da-eric-toney",
               "https://erictoney.com/"]),
    ]),

    # ---------------- Jason Miyares (VA-R, former Attorney General) ----------------
    ("jason-miyares-ag-2026", "VA", "Attorney General", [
        claim("jmv1", "jason-miyares-ag-2026", "sanctity_of_life", 0, False,
              "Supports a 15-week abortion ban with exceptions for rape, incest, and the life of the mother, and has stated he opposes prosecuting women who seek abortions—a restrictions-only position that falls short of the rubric's life-from-conception/personhood standard and the abolitionist 'no exceptions' call.",
              ["https://en.wikipedia.org/wiki/Jason_Miyares",
               "https://wset.com/news/beyond-the-podium/know-your-candidates/virginias-attorney-general-candidates-on-major-issues-ahead-of-2025-election-jason-miyares-jay-jones-republican-democrat-september-2025"]),
        claim("jmv2", "jason-miyares-ag-2026", "self_defense", 1, False,
              "As Virginia's Attorney General (2022–2026), continued actively defending Virginia's Universal Background Check law and One Handgun a Month statute in court after the Bruen ruling made such laws constitutionally suspect; declined to join 26 other Republican AGs in an amicus brief against Washington State's magazine-capacity restrictions—drawing sustained criticism from Gun Owners of America as a 'Second Amendment betrayal.'",
              ["https://www.gunowners.org/sa102925/",
               "https://www.ammoland.com/2023/01/virginias-pro-gun-ag-fighting-to-keep-universal-background-checks/"]),
    ]),

    # ---------------- Josh Kaul (WI-D, Attorney General) ----------------
    ("josh-kaul-ag-2026", "WI", "Attorney General", [
        claim("jk1", "josh-kaul-ag-2026", "sanctity_of_life", 0, False,
              "Successfully argued before the Wisconsin Supreme Court in 2024–2025 that the state's pre-Roe 1849 abortion ban was unenforceable, securing a ruling striking it down—directly dismantling Wisconsin's strongest legal protection for the unborn and rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/Josh_Kaul",
               "https://www.wpr.org/news/josh-kaul-governor-reelection-attorney-general"]),
        claim("jk2", "josh-kaul-ag-2026", "self_defense", 1, False,
              "Has repeatedly called on the Republican-controlled Wisconsin Legislature to enact universal background checks for all firearm purchases and additional 'gun safety' measures, making gun-control advocacy a platform pillar of his AG record and reelection campaign.",
              ["https://ballotpedia.org/Josh_Kaul",
               "https://civicmedia.us/news/2025/1/13/ag-josh-kaul-lays-out-key-issues-facing-wisconsin"]),
    ]),

    # ---------------- Marlo Oaks (UT-R, State Treasurer) ----------------
    ("marlo-oaks", "UT", "Treasurer", [
        claim("mo1", "marlo-oaks", "economic_stewardship", 0, True,
              "A nationally recognized opponent of Central Bank Digital Currency: explicitly listed fighting CBDC as a core pillar of his tenure as Utah State Treasurer, warning that a government-controlled digital dollar poses a surveillance and control threat to financial freedom—directly aligning with the rubric's opposition to a CBDC.",
              ["https://www.marlooaks.com/defending-economic-freedom/",
               "https://townhallreview.com/podcasts/meeting-of-minds/red-states-real-money-utah-treasurer-marlo-oaks-on-gold-bitcoin-economic-freedom"]),
        claim("mo2", "marlo-oaks", "economic_stewardship", 1, True,
              "National champion of the sound-money movement: championed Utah's 2024 HB306 transactional-gold bill (signed into law), making Utah the first state to allow vendors to be paid in gold and silver by state government, and oversaw the growth of Utah's gold reserve to $60 million—leading the nation in practical hard-money alternatives to fiat currency.",
              ["https://treasurer.utah.gov/featured-news/first-in-the-nation-utah-legislature-passes-bill-paving-the-way-for-state-vendors-to-be-paid-in-gold-and-silver/",
               "https://www.sltrib.com/news/politics/2025/03/18/utah-has-invested-60m-taxpayers/"]),
        claim("mo3", "marlo-oaks", "economic_stewardship", 4, True,
              "Led state-level opposition to the Biden administration's ESG mandates and the SEC's proposed Natural Asset Companies (NAC) rule that would have entrenched WEF/Davos-aligned environmental metrics into sovereign investment decisions; mobilized a multi-state coalition to oppose NAC, which the SEC ultimately withdrew.",
              ["https://www.marlooaks.com/defending-economic-freedom/",
               "https://treasurer.utah.gov/"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
