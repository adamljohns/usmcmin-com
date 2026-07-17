#!/usr/bin/env python3
"""Enrichment batch 724: hand-curated claims for 5 NY Republican State Senators.

archetype_curated federal senator/rep buckets fully exhausted; continuing the
state-level pivot. Targets five New York Republican State Senators with 0 claims
(archetype_party_default), taken from the bottom of the remaining alphabet:
  Mark Walczyk (SD-49), Mario Mattera (SD-2), Joseph Griffo (SD-53),
  Jake Ashby (SD-43), Jack Martins (SD-7).

Each claim cites >=1 reliable source and reflects documented voting record /
public positions on the God-First/America-First rubric categories.
Note: Jack Martins carries negative scores on 2A and life — those are accurate
rubric data points reflecting his SAFE Act and 2025 abortion-expansion votes.
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
    # --- Mark Walczyk (NY, State Senator SD-49, North Country; since Jan 2023) ---
    ("mark-walczyk", "NY", "State Senator", [
        claim("mw1", "mark-walczyk", "family_child_sovereignty", 0, True,
              "Publicly condemned NYSED guidance (2023) directing schools NOT to inform parents when a child expresses a different gender identity at school, calling it a dangerous precedent: 'The State Education Department has no right to shut parents out of their children's lives.' He also issued a separate press release demanding parental inclusion in medical and social decisions about their own children — opposing Albany's policy of withholding student gender information from families.",
              ["https://www.nysenate.gov/newsroom/press-releases/2023/mark-walczyk/senator-mark-walczyk-appalled-state-education-department",
               "https://www.northcountrynow.com/news/sen-walczyk-calls-nyss-most-recent-guidelines-students-gender-identity-schools-appalling"]),
        claim("mw2", "mark-walczyk", "self_defense", 1, True,
              "A staunch Second Amendment defender who opposed the 2022 Concealed Carry Improvement Act and introduced S2021 (2025) to allow licensed firearm holders to open carry, stating 'The right to bear arms as defined under the 2nd Amendment shall not be infringed.' He also introduced S7645 to repeal CCIA-imposed background-check fees on ammunition, calling them 'ridiculous and unconstitutional' — and co-sponsored S2635 to fully repeal the CCIA. After Remington Arms closed its Ilion, NY plant, he blamed Albany Democrats' Gun Industry Liability Law as the direct cause.",
              ["https://www.nysenate.gov/legislation/bills/2025/S2021",
               "https://www.nysenate.gov/newsroom/press-releases/2023/mark-walczyk/senator-walczyk-introduces-bill-repeal-new-fees"]),
        claim("mw3", "mark-walczyk", "election_integrity", 0, True,
              "Introduced S1885 (2025) requiring government-issued photo ID to cast a ballot and S2345 requiring the Board of Elections to verify citizenship of voter registrants through the federal SAVE program. Praised Trump's March 2025 executive order on election integrity, noting it mirrored his own sponsored legislation. Also celebrated a court ruling striking down New York City's noncitizen voting ordinance, stating: 'The Court's decision confirms our belief that expanding the franchise to noncitizens undermines the very foundation of our democratic system.'",
              ["https://www.nysenate.gov/legislation/bills/2025/S1885",
               "https://www.nysenate.gov/newsroom/press-releases/2025/mark-walczyk/senator-walczyk-celebrates-court-ruling-upholding-voting"]),
    ]),

    # --- Mario Mattera (NY, State Senator SD-2, Suffolk County; since Jan 2023) ---
    ("mario-mattera", "NY", "State Senator", [
        claim("mm1", "mario-mattera", "self_defense", 1, True,
              "Voted NAY on the Concealed Carry Improvement Act (S51001, July 1, 2022 extraordinary session), casting one of the 20 Republican No votes against legislation that expanded sensitive-location gun-free zones, imposed 'good moral character' licensing standards, and tightened magazine capacity rules — a party-line stand against post-Bruen gun restrictions documented in the LegiScan roll call.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://www.nysenate.gov/legislation/bills/2021/S51001"]),
        claim("mm2", "mario-mattera", "family_child_sovereignty", 0, True,
              "Publicly opposed New York Proposition One (the 2024 'Equal Rights Amendment') in a September 2024 interview, warning that a YES vote would allow 'minors not requiring parental consent to move forward with medical procedures such as transgender intervention' and would let schools override parental authority on children's bodies and identities — a direct defense of the parental rights standard the rubric measures.",
              ["https://messengerpapers.com/2024/09/proposition-one-a-conversation-with-senator-mattera/"]),
        claim("mm3", "mario-mattera", "border_immigration", 2, True,
              "Called on Governor Hochul to rescind New York's sanctuary state designation in a 2023 press release co-signed with fellow Long Island senators, stating: 'She must rescind the sanctuary state and hold the Biden administration responsible. They have endangered New Yorkers by implementing these unfair circumstances, designating New York a sanctuary state, and their poor vetting process, creating a dangerous situation for everyone.' He also joined the 2024 Senate Republican agenda ('A New Hope For The Empire State') that formally demanded ending sanctuary protections.",
              ["https://www.nysenate.gov/newsroom/press-releases/2023/jack-m-martins/li-senators-call-governor-protect-welfare-and-safety",
               "https://www.nysenate.gov/newsroom/press-releases/2024/mario-r-mattera/senator-mattera-joins-senate-minority-conference"]),
    ]),

    # --- Joseph Griffo (NY, State Senator SD-53, Oneida County / Rome-Utica) ---
    ("joseph-griffo", "NY", "State Senator", [
        claim("jg1", "joseph-griffo", "self_defense", 1, True,
              "Voted NAY on the NY SAFE Act (S2230, January 14, 2013), confirmed in the LegiScan roll call as one of 18 senators opposing the law's assault-weapon ban, 7-round magazine limit, and expanded firearms registry — calling it an 'unconstitutional attack on the freedoms of every legal gun owner.' Later sponsored S879 (2017) to repeal the SAFE Act statewide outside New York City, and co-sponsored S2635 (2023) to repeal the Concealed Carry Improvement Act, also joining a Senate Republican amicus brief to the U.S. Supreme Court challenging the CCIA (Docket 24-795).",
              ["https://legiscan.com/NY/rollcall/S02230/id/217503",
               "https://www.nysenate.gov/newsroom/press-releases/2017/joseph-griffo/senator-griffo-announces-legislation-would-repeal"]),
        claim("jg2", "joseph-griffo", "biblical_marriage", 0, True,
              "Voted NO on the Marriage Equality Act (A8354, June 24, 2011), which passed the NY Senate 33–29 and legalized same-sex marriage in New York — affirming the traditional one-man-one-woman definition of marriage. He also voted against a 2009 same-sex marriage bill that failed 38–24.",
              ["https://en.wikipedia.org/wiki/Joseph_Griffo",
               "https://en.wikipedia.org/wiki/Marriage_Equality_Act_(New_York)"]),
        claim("jg3", "joseph-griffo", "sanctity_of_life", 0, True,
              "Voted No on the Reproductive Health Act (S240, January 22, 2019), consistent with the unanimous Republican caucus opposition: the bill passed 38–24, with the 24 No votes comprising the entire Republican minority. The RHA removed all references to the unborn from New York's penal code, repealed criminal penalties for late-term abortions outside clinical settings, and authorized non-physicians to perform abortions — a sweeping abortion-expansion law Griffo opposed as part of unified Republican resistance.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://en.wikipedia.org/wiki/Reproductive_Health_Act"]),
    ]),

    # --- Jake Ashby (NY, State Senator SD-43, Capital District / Columbia-Washington; since Jan 2023) ---
    ("jake-ashby", "NY", "State Senator", [
        claim("ja1", "jake-ashby", "sanctity_of_life", 3, True,
              "Voted NO on the Medical Aid in Dying Act (S138, June 9, 2025), which passed the NY Senate 35–27 — and actively debated the bill on the Senate floor, making him among the most vocal opponents of legalizing assisted suicide in New York. His floor participation underscores a principled defense of natural death over state-sanctioned euthanasia, consistent with the rubric's anti-euthanasia standard.",
              ["https://en.wikipedia.org/wiki/Jake_Ashby",
               "https://www.nysenate.gov/legislation/bills/2025/S138"]),
        claim("ja2", "jake-ashby", "family_child_sovereignty", 0, True,
              "Sponsored the Age Verification Act (S3591, introduced January 2025), requiring adult-content websites to verify users are 18 or older before granting access, with civil penalties up to $50,000 per day for violations. The bill's sponsors' memo states: 'The internet is a dangerous place for children, rife with sexual material that is harmful to minors. The ease of access to this material is downright scary.' Backed by NY Family Action and garnered 30 co-sponsors by mid-2025.",
              ["https://www.nysenate.gov/legislation/bills/2025/S3591",
               "https://www.wamc.org/news/2025-08-26/state-lawmakers-look-to-pass-legislation-requiring-adult-website-users-to-verify-age"]),
        claim("ja3", "jake-ashby", "self_defense", 1, True,
              "Publicly opposed the Concealed Carry Improvement Act (CCIA) passed in the July 2022 extraordinary session, stating in a November 2022 interview: 'It feels like the Democrats are targeting these legal gun owners versus the people using firearms illegally.' He called for the governor and Legislature 'to be willing to revisit the legislation with an eye toward some needed adjustments — or even perhaps a full repeal' — a clear stand against the CCIA's expanded gun-free zones and heightened licensing burdens.",
              ["https://spectrumlocalnews.com/nys/central-ny/politics/2022/11/30/asm--ashby-prepares-move-to-state-senate",
               "https://www.nysenate.gov/legislation/bills/2023/S2635"]),
    ]),

    # --- Jack Martins (NY, State Senator SD-7, Nassau County; since Jan 2023) ---
    ("jack-martins", "NY", "State Senator", [
        claim("jm1", "jack-martins", "self_defense", 1, False,
              "Voted YES on the NY SAFE Act (S2230, January 14, 2013), one of only nine Republicans to cross party lines and join 34 Democrats in passing the law 43–18. The SAFE Act imposed an assault-weapon ban, a 7-round magazine limit, and an expanded firearms registry — measures the rubric's Second Amendment standard directly opposes. His vote placed him outside Republican caucus consensus on gun rights.",
              ["https://legiscan.com/NY/rollcall/S02230/id/217503",
               "https://nyfirearms.com/forums/firearms-news/42570-how-your-rep-voted-cuomos-safe-act.html"]),
        claim("jm2", "jack-martins", "sanctity_of_life", 0, False,
              "On January 21, 2025, voted YES on all five abortion-expansion bills passed by the NY Senate — including S.36-A (allowing abortion-pill prescribers to mask their identities to supply patients in other states), which passed 39–20 with only two Republicans in the Yes column: Martins and Stephen Chan. He also supported the NY State Abortion Clinical Training Program Act (passed 40–19), one of three Republicans voting yes. At a 2024 forum he said 'I will never make a decision for someone else when it comes to it,' framing abortion as a personal choice beyond legislative reach.",
              ["https://newyorkfamilies.org/2025/01/state-senate-votes-to-promote-protect-and-fund-abortion/",
               "https://www.nysenate.gov/newsroom/press-releases/2025/new-york-state-senate-expands-reproductive-protections-womens-health"]),
        claim("jm3", "jack-martins", "family_child_sovereignty", 0, True,
              "Co-sponsored the 'Our Schools, Our Rules Act' (October 2024, with Assembly Member Jake Blumencranz), prohibiting the NYSED Regionalization Initiative from forcing school districts to consolidate governance and share resources under state control beginning in 2026–2027. Martins also authored a Long Island Herald op-ed arguing the mandate was state overreach that would strip communities of local school board authority — a defense of parental and community sovereignty over education against Albany bureaucratic consolidation.",
              ["https://www.liherald.com/stories/jack-martins-new-york-education-regionalization-schools,211577",
               "https://www.nysenate.gov/newsroom/press-releases/2024/steven-d-rhoads/members-long-island-senate-republican-conference-local"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
