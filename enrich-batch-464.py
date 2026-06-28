#!/usr/bin/env python3
"""Enrichment batch 464: 5 Wisconsin State Assembly Democrats with 0 claims.

Primary archetype_curated federal-senator bucket is exhausted (all 100 sitting
U.S. Senators are now evidence_curated). Continuing fallback: archetype_party_default
state-level officials from the bottom of the alphabet.

Targets (sorted state desc, then name desc — next 5 after batch 463):
- Steve Doyle (WI-94, D)
- Shelia Stubbs (WI-78, D)
- Sequanna Taylor (WI-11, D)
- Ryan Spaude (WI-89, D)
- Ryan Clancy (WI-19, D)

2-3 distinct-category claims per candidate spanning sanctity_of_life,
biblical_marriage, self_defense, election_integrity, and public_justice rubric
categories. Sources: docs.legis.wisconsin.gov, legiscan.com, ballotpedia.org,
wpr.org, urbanmilwaukee.com, legis.wisconsin.gov.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = "2026-06-28"


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
    # ---------------- Steve Doyle (WI-94, D) ----------------
    ("steve-doyle-wi-94", "WI", "Assembly", [
        claim("sd1", "steve-doyle-wi-94", "sanctity_of_life", 0, False,
              "Co-introduced Wisconsin AB355 (July 8, 2025), the 'Right to Bodily Autonomy' bill that would enshrine abortion access at any stage of pregnancy in state law, eliminate existing abortion-related regulations, and require coverage of abortion under health care plans. Doyle voted pro-choice as a legislator despite describing himself as personally anti-abortion — the bill rejects any legal personhood from conception.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://ballotpedia.org/Steve_Doyle"]),
        claim("sd2", "steve-doyle-wi-94", "election_integrity", 0, False,
              "As a Wisconsin Assembly Democrat, Doyle belongs to the caucus that voted unanimously against the January 2025 voter-ID constitutional amendment (SJR2), which passed 54-45 on a strict party-line vote with all Democrats opposed — rejecting the rubric's voter-ID plank for election integrity. The amendment was subsequently ratified by Wisconsin voters in the April 2025 referendum.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://legiscan.com/WI/bill/SJR2/2025",
               "https://www.wpr.org/news/april-2025-election-voter-id-requirement-passes-wisconsin-constitution"]),
        claim("sd3", "steve-doyle-wi-94", "self_defense", 1, False,
              "Despite a prior NRA endorsement reflecting his rural district's gun culture, Doyle co-sponsored a universal background check bill in the Wisconsin Assembly — a firearm-transfer regulation the rubric marks against, as it expands government screening beyond what the Second Amendment community regards as constitutionally appropriate.",
              ["https://ballotpedia.org/Steve_Doyle",
               "https://progressivevotersguide.com/wisconsin/2024/general/steve-doyle"]),
    ]),

    # ---------------- Shelia Stubbs (WI-78, D) ----------------
    ("shelia-stubbs-wi-78", "WI", "Assembly", [
        claim("ss1", "shelia-stubbs-wi-78", "sanctity_of_life", 0, False,
              "A self-described 'champion' for abortion access who co-sponsored Wisconsin AB589 (October 2025, the Abortion Accessibility Act), which would remove criminal penalties, eliminate mandatory informed-consent requirements unique to abortion, and allow non-physician providers to perform abortions — dismantling every statutory limit the state maintained on the practice and rejecting any personhood-from-conception framework.",
              ["https://legiscan.com/WI/bill/AB589/2025",
               "https://www.aclu-wi.org/legislation/ab-589-sb-547-abortion-accessibility-act/",
               "https://ballotpedia.org/Shelia_Stubbs"]),
        claim("ss2", "shelia-stubbs-wi-78", "biblical_marriage", 0, False,
              "Sponsored Wisconsin Assembly Joint Resolution 76 (2025) to eliminate the state constitutional restriction defining marriage as only between a man and a woman — the definition the rubric identifies as the biblical standard. She also sponsored AJR79 (2025) recognizing June 2025 as LGBTQ Pride Month, actively promoting the ideological framework the rubric opposes.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/assembly/2869",
               "https://ballotpedia.org/Shelia_Stubbs",
               "https://legis.wisconsin.gov/assembly/78/stubbs"]),
        claim("ss3", "shelia-stubbs-wi-78", "self_defense", 1, False,
              "Serves as Co-Chair of the Wisconsin Coalition on Gun Safety and led the 2025 'Safe Summer' gun-control package, which includes reinstating a 48-hour waiting period for all firearm purchases, a red-flag (extreme risk protection order) law, a ban on ghost guns, and universal background checks — a comprehensive regulatory agenda directly opposed to the rubric's constitutional-carry and anti-restriction principles.",
              ["https://www.wispolitics.com/2025/wisconsin-gun-safety-coalition-co-chairs-rep-shelia-stubbs-rep-deb-andraca-sen-latonya-johnson-wisconsin-attorney-general-josh-kaul-senate-minority-leader-dianne-hesselbein-sen-chris-larson/",
               "https://legis.wisconsin.gov/assembly/78/stubbs/news-updates/press-releases/"]),
    ]),

    # ---------------- Sequanna Taylor (WI-11, D) ----------------
    ("sequanna-taylor-wi-11", "WI", "Assembly", [
        claim("qt1", "sequanna-taylor-wi-11", "sanctity_of_life", 0, False,
              "Co-sponsored Wisconsin AB355 (July 8, 2025) — the 'Right to Bodily Autonomy' bill that would legalize abortion at any stage of pregnancy, eliminate existing state abortion regulations, and mandate insurance coverage for abortion — rejecting any recognition of fetal personhood from conception. The bill drew 59 Democratic co-sponsors and passed no committee before failing in March 2026.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://ballotpedia.org/Sequanna_Taylor"]),
        claim("qt2", "sequanna-taylor-wi-11", "self_defense", 1, False,
              "Co-sponsored Wisconsin Assembly Bill 319 (2025), which would establish an extreme risk protection order (ERPO/red flag) process allowing courts to temporarily confiscate firearms from individuals deemed a danger — a gun-removal mechanism the rubric opposes as violating due-process and Second Amendment rights. Taylor also supported the broader gun-control package that included waiting periods and universal background checks.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/assembly/2880",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://www.everytown.org/press/after-republicans-prioritized-guns-over-safety-gun-sense-champions-introduce-life-saving-omnibus-package-to-protect-wisconsin-families-from-gun-violence/"]),
        claim("qt3", "sequanna-taylor-wi-11", "election_integrity", 0, False,
              "As a Wisconsin Assembly Democrat, Taylor belongs to the caucus that voted unanimously against the January 2025 voter-ID constitutional amendment (SJR2), which passed 54-45 on a strict party-line vote with all Democrats opposed — rejecting the rubric's voter-ID plank for election integrity.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://legiscan.com/WI/bill/SJR2/2025",
               "https://ballotpedia.org/Sequanna_Taylor"]),
    ]),

    # ---------------- Ryan Spaude (WI-89, D) ----------------
    ("ryan-spaude-wi-89", "WI", "Assembly", [
        claim("rs1", "ryan-spaude-wi-89", "sanctity_of_life", 0, False,
              "Co-introduced Wisconsin AB355 (July 8, 2025) — the 'Right to Bodily Autonomy' bill that would establish unrestricted abortion access at any stage of pregnancy as a fundamental right, eliminate state abortion regulations, and require abortion coverage under health plans. As a former assistant district attorney who ran on progressive values, Spaude was among the bill's primary Democratic sponsors.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://ballotpedia.org/Ryan_Spaude"]),
        claim("rs2", "ryan-spaude-wi-89", "self_defense", 1, False,
              "Co-introduced Wisconsin AB324 (July 8, 2025), which would reinstate a mandatory waiting period for the purchase of handguns, and AB325 (2025), relating to expanded regulation of firearm sales and transfers — gun-control measures the rubric opposes as restrictions on the right to keep and bear arms without restriction.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab324",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://www.billtrack50.com/billdetail/1900879"]),
        claim("rs3", "ryan-spaude-wi-89", "election_integrity", 0, False,
              "As a Wisconsin Assembly Democrat, Spaude belongs to the caucus that voted unanimously against the January 2025 voter-ID constitutional amendment (SJR2), which passed 54-45 on a strict party-line vote with all Democrats opposed — rejecting the rubric's voter-ID plank for election integrity.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://legiscan.com/WI/bill/SJR2/2025",
               "https://ballotpedia.org/Ryan_Spaude"]),
    ]),

    # ---------------- Ryan Clancy (WI-19, D) ----------------
    ("ryan-clancy-wi-19", "WI", "Assembly", [
        claim("rc1", "ryan-clancy-wi-19", "sanctity_of_life", 0, False,
              "Co-sponsored Wisconsin AB355 (July 8, 2025) — the 'Right to Bodily Autonomy' bill establishing unrestricted abortion access at any stage of pregnancy, eliminating existing state abortion regulations, and mandating insurance coverage for abortion — rejecting any personhood-from-conception standard. The bill had 59 Democratic co-sponsors before failing in March 2026.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025",
               "https://ballotpedia.org/Ryan_Clancy"]),
        claim("rc2", "ryan-clancy-wi-19", "public_justice", 0, False,
              "Introduced Wisconsin AB1193 (March 2026) to decriminalize prostitution and create a 'sex workers' bill of rights,' removing criminal penalties for commercial sex transactions. He also co-introduced Assembly Bill 510 (September 2025) allowing sex workers to report crimes without arrest — a systematic move to normalize the commercial sex trade the rubric categorizes under public moral order.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab1193",
               "https://legiscan.com/WI/bill/AB1193/2025",
               "https://urbanmilwaukee.com/pressrelease/rep-ryan-clancy-announces-legislation-providing-vital-protections-for-trafficking-survivors-sex-workers/"]),
        claim("rc3", "ryan-clancy-wi-19", "election_integrity", 0, False,
              "As a Wisconsin Assembly Democrat, Clancy belongs to the caucus that voted unanimously against the January 2025 voter-ID constitutional amendment (SJR2), which passed 54-45 on a strict party-line vote with all Democrats opposed — rejecting the rubric's voter-ID plank. He simultaneously introduced legislation to allow student IDs to qualify for voting, expanding the pool of acceptable identification beyond government-issued photo ID.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://legiscan.com/WI/bill/SJR2/2025",
               "https://ballotpedia.org/Ryan_Clancy"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to avoid name-collision bugs.

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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  OK {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
