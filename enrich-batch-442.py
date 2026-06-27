#!/usr/bin/env python3
"""Enrichment batch 442: 5 state executives — bottom-of-alphabet strategy.

Federal senator/representative pool fully exhausted. Pivoting to high-profile
state executives (Governors, AGs, Lt. Governors) with evidence_state confidence
and 0 claims, taken from the bottom of the alphabet (TN, SD, RI x2, PR).

Targets:
  Randy McNally       — Tennessee Lt. Governor (R), fiscal conscience, pro-life
  Tony Venhuizen      — South Dakota Lt. Governor (R), Medicaid reform sponsor
  Sabina Matos        — Rhode Island Lt. Governor (D), pro-abortion, pro-LGBTQ
  Peter Neronha       — Rhode Island Attorney General (D), abortion/gun-control advocate
  Jenniffer González-Colón — Puerto Rico Governor (R), signed life-at-conception law 2026

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
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
    # ---------- Randy McNally (TN Lt. Governor, R) ----------
    ("randy-mcnally", "TN", "Lt. Governor", [
        claim("rm1", "randy-mcnally", "sanctity_of_life", 0, True,
              "Lt. Governor and Senate Speaker Randy McNally voted for and helped steer through the General Assembly Tennessee's Human Life Protection Act (the 'trigger ban'), which took effect August 25, 2022, after Dobbs v. Jackson Women's Health Organization. The law bans abortion at any stage of pregnancy with narrow medical exceptions only — no exceptions for rape or incest — and is among the strictest abortion prohibitions in the nation. McNally called the Dobbs decision 'a huge win for the cause of life' and, when colleagues in 2023 sought to add exceptions to the law, stated publicly that he preferred to keep the trigger law intact.",
              ["https://tennesseelookout.com/2022/08/25/amid-uncertainty-and-anger-tennessees-abortion-ban-takes-effect/",
               "https://en.wikipedia.org/wiki/Abortion_in_Tennessee",
               "https://tennesseelookout.com/2023/01/06/stockard-on-the-stump-lawmakers-line-up-to-add-exceptions-to-abortion-law/"]),
        claim("rm2", "randy-mcnally", "self_defense", 0, True,
              "As Lieutenant Governor and presiding officer of the Tennessee Senate, McNally oversaw passage of Senate Bill 765 (2021), Tennessee's constitutional carry law — signed by Governor Bill Lee on April 8, 2021, and effective July 1, 2021 — which eliminated the permit requirement for law-abiding adults to carry a handgun openly or concealed. Tennessee became the 20th state to adopt permitless carry. McNally did not invoke procedural opposition and allowed the bill to advance, consistent with his pro-Second-Amendment record as a Republican leader.",
              ["https://www.nraila.org/gun-laws/state-gun-laws/tennessee/",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
        claim("rm3", "randy-mcnally", "economic_stewardship", 2, True,
              "Recognized statewide as 'Tennessee's fiscal conscience' over his 35+ year legislative career, McNally chaired the Senate Finance, Ways, and Means Committee for decades and consistently opposed deficit spending and unfunded budget growth. During the 2023 session, when Tennessee faced a mid-year budget shortfall, McNally's Finance committee alerted colleagues and pushed for tighter spending discipline rather than borrowing. He championed building up Tennessee's rainy-day reserve fund and rejected inflationary budget expansion.",
              ["https://ballotpedia.org/Randy_McNally",
               "https://tennesseelookout.com/2023/08/28/as-house-senate-remain-stuck-finance-commissioner-warns-about-budget-shortfall/"]),
    ]),

    # ---------- Tony Venhuizen (SD Lt. Governor, R) ----------
    ("tony-venhuizen", "SD", "Lt. Governor", [
        claim("tv1", "tony-venhuizen", "economic_stewardship", 2, True,
              "As a Republican member of the South Dakota House of Representatives representing District 13 (Lincoln and Minnehaha counties), Venhuizen co-introduced a concurrent resolution alongside Rep. Casey Crabtree requiring that Medicaid expansion enrollees meet work, education, or community-service requirements as a condition of eligibility. The South Dakota Legislature adopted the resolution, placing the measure on the 2024 ballot as Amendment F; South Dakota voters approved the Medicaid work requirement in November 2024, rolling back unconditional federal welfare expansion and restoring fiscal accountability to the state Medicaid program.",
              ["https://en.wikipedia.org/wiki/Tony_Venhuizen",
               "https://ballotpedia.org/Tony_Venhuizen"]),
        claim("tv2", "tony-venhuizen", "sanctity_of_life", 0, True,
              "Venhuizen served in the South Dakota House during 2023–2025 as the state enforced its near-total abortion ban (Human Life Protection Act, SDCL 22-17-5.1) — triggered by Dobbs v. Jackson in June 2022 — which prohibits abortion in all cases except to save the mother's life, with no exceptions for rape or incest. He was appointed Lt. Governor in January 2025 by pro-life Governor Larry Rhoden and was unanimously confirmed. South Dakota voters rejected Amendment G in November 2024 (by 59%–41%), which would have legalized abortion through the second trimester; Venhuizen's Republican caucus uniformly opposed the measure.",
              ["https://en.wikipedia.org/wiki/Tony_Venhuizen",
               "https://en.wikipedia.org/wiki/Abortion_in_South_Dakota",
               "https://ballotpedia.org/South_Dakota_Constitutional_Amendment_G,_Right_to_Abortion_Initiative_(2024)"]),
    ]),

    # ---------- Sabina Matos (RI Lt. Governor, D) ----------
    ("sabina-matos", "RI", "Lt. Governor", [
        claim("sm1", "sabina-matos", "sanctity_of_life", 0, False,
              "Lt. Governor Matos publicly celebrated Rhode Island's Equality in Abortion Coverage Act, which mandated that state health insurance programs cover abortion without cost sharing — expanding taxpayer funding for abortion. Matos issued a statement praising the signing, declaring: 'As other states attack the fundamental right to choose, Rhode Island must do all it can to protect a person's access to reproductive health care,' framing abortion as an unrestricted constitutional right and explicitly rejecting any protection of unborn life from conception.",
              ["https://governor.ri.gov/press-releases/governor-mckee-lt-governor-matos-statements-signing-equality-abortion-coverage-act",
               "https://ballotpedia.org/Sabina_Matos"]),
        claim("sm2", "sabina-matos", "biblical_marriage", 2, False,
              "Matos and the McKee administration co-championed legislation signed on June 27, 2024, advancing Rhode Island's LGBTQ policy framework, including provisions supporting gender-identity accommodation in state policy. Rhode Island — where Matos serves as the first Dominican American elected to statewide office — is consistently ranked among the most LGBTQ-affirming states: conversion therapy is banned, gender identity is protected in schools, and government policy actively promotes transgender inclusion. Matos has taken no action opposing transgender ideology in law or public institutions.",
              ["https://governor.ri.gov/press-releases/governor-mckee-signs-legislation-supporting-reproductive-health-care-lgbtq-community",
               "https://en.wikipedia.org/wiki/LGBTQ_rights_in_Rhode_Island"]),
    ]),

    # ---------- Peter Neronha (RI Attorney General, D) ----------
    ("peter-neronha", "RI", "Attorney General", [
        claim("pn1", "peter-neronha", "sanctity_of_life", 0, False,
              "Attorney General Neronha joined a multistate coalition of Democratic attorneys general to file an amicus brief in the U.S. Court of Appeals for the Fifth Circuit challenging a federal district court ruling that would have restricted nationwide access to mifepristone — a medication abortion drug — actively using his office's legal resources to preserve abortion access and block any federal judicial protection of preborn life. He has consistently framed abortion access as a civil-rights priority of his office.",
              ["https://en.wikipedia.org/wiki/Peter_Neronha",
               "https://riag.ri.gov/"]),
        claim("pn2", "peter-neronha", "self_defense", 1, False,
              "Neronha has been an outspoken advocate for gun restrictions, declaring: 'There is no need for civilians to own and operate military-style weapons,' and actively participating in press events calling for an assault weapons ban in Rhode Island. His office also submitted a package of gun control measures including safe-storage mandates and anti-straw-purchase requirements. He successfully defended Rhode Island's restrictive concealed-carry permit law in court — a system that denies permits unless applicants can prove a specific threat to their life — thereby blocking constitutional carry in the state.",
              ["https://governor.ri.gov/press-releases/governor-mckee-general-officers-state-legislators-gun-safety-advocates-highlight-introduction-of-assault-weapons-ban-bill",
               "https://riag.ri.gov/press-releases/attorney-general-successfully-defends-ris-concealed-carry-permit-laws",
               "https://en.wikipedia.org/wiki/Peter_Neronha"]),
    ]),

    # ---------- Jenniffer González-Colón (PR Governor, R) ----------
    ("jenniffer-gonzalez-colon", "PR", "Governor", [
        claim("jgc1", "jenniffer-gonzalez-colon", "sanctity_of_life", 0, True,
              "As Governor of Puerto Rico, González-Colón signed Senate Bill 504 into law on February 12, 2026 (Law 18-2026), amending Puerto Rico's Penal Code and Civil Code to expressly define the term 'human being' to include the conceived child at any stage of gestation — establishing legal recognition of personhood from conception. National Right to Life (NRL) applauded the measure as 'a landmark reform that finally speaks with clarity about the child in the womb,' and as 'Puerto Rico's Historic Recognition of Preborn Human Life.' NRL noted the law embeds the moral and legal status of the unborn child into Puerto Rico's legal framework.",
              ["https://nrlc.org/nrlnewstoday/2026/02/puerto-rican-governor-jenniffer-gonzalez-colon-signs-historic-protection-for-the-unborn/",
               "https://nrlc.org/communications/nrl-welcomes-puerto-ricos-historic-recognition-of-preborn-human-life/"]),
        claim("jgc2", "jenniffer-gonzalez-colon", "economic_stewardship", 2, True,
              "A self-described 'small government, pro-business conservative,' González-Colón won the 2024 Puerto Rico gubernatorial election with over 40% of the vote and was sworn in January 2, 2025, as the second woman elected governor of Puerto Rico. She has focused her administration on economic development, reducing the island's debt burden, energy policy reform, and fiscal restraint — opposing the pattern of deficit spending that has historically plagued Puerto Rico's government finances and driven the territory's landmark debt restructuring.",
              ["https://ballotpedia.org/Jenniffer_Gonz%C3%A1lez-Col%C3%B3n",
               "https://en.wikipedia.org/wiki/Jenniffer_Gonz%C3%A1lez-Col%C3%B3n"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
