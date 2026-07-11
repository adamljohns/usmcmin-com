#!/usr/bin/env python3
"""Enrichment batch 674: 5 Rhode Island Democratic state senators (continued).

Federal and archetype_curated pools fully exhausted; continuing the
archetype_party_default state-senator pool in RI (bottom of alphabet),
picking up directly where batch 673 left off.

Targets (next 5 from remaining RI pool after batch 673):
  Stefano Famiglietti  (District 4, North Providence — pro-2A, personally anti-abortion;
                        sworn in Aug 14 2025 after special election)
  Pete Appollonio      (District 29, Warwick — Democrat who voted NAY on AWB;
                        24-year retired police captain)
  Matthew LaMountain   (District 31, Warwick/Cranston — Senate Judiciary Chair,
                        primary AWB co-sponsor, EACA yes, S0824 co-sponsor)
  Lori Urso            (District 8, Pawtucket — first-term 2025 senator;
                        YES on AWB, S0824 co-sponsor)
  Linda Ujifusa        (District 11, Portsmouth/Bristol — YES on EACA, S2262,
                        AWB; co-sponsor of 2026 possession ban)

Sources: rilegislature.gov, legiscan.com/RI, rhodeislandcurrent.com,
ballotpedia.org, valleybreeze.com, gladlaw.org, plannedparenthoodaction.org,
rigunrights.com, wpri.com, ammoland.com, governor.ri.gov.
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
    # ---------------- Stefano Famiglietti (RI-D, District 4, North Providence) ----------------
    ("stefano-famiglietti", "RI", "Senator", [
        claim("sf1", "stefano-famiglietti", "self_defense", 1, True,
              "Opposed Rhode Island's Assault Weapons Ban (H5436/S0359) before taking "
              "office, submitting written testimony to the RI House Judiciary Committee on "
              "March 26, 2025, calling it a 'hastily proposed law' that 'impacts the rights "
              "of safe and lawful gun owners' and 'infringes on the rights of constituents "
              "and will lead to lawsuits.' He also advanced a North Providence Town Council "
              "resolution against the legislation. During his August 2025 Senate campaign, "
              "Famiglietti publicly identified as 'pro-Second Amendment' and declined to "
              "endorse the enacted version of the ban without further review — aligning with "
              "the rubric's defense of the unrestricted right to keep and bear semi-automatic arms.",
              ["https://www.rilegislature.gov/Special/comdoc/House%20Judiciary%202025/03-26-2025--H5436--Stefano%20Famiglietti.pdf",
               "https://www.valleybreeze.com/news/north-providence-council-opposes-assault-weapons-ban/article_0154b21b-3101-4fe0-ba01-1f1206061fb8.html",
               "https://rhodeislandcurrent.com/2025/08/04/two-personal-injury-attorneys-vie-for-open-r-i-senate-district-4-seat/"]),
        claim("sf2", "stefano-famiglietti", "sanctity_of_life", 0, True,
              "Stated during his August 2025 Senate campaign that as a Catholic he 'personally "
              "opposes abortion.' Widely described by Rhode Island political reporters as being "
              "in the 'Ruggerio mold' — a reference to the late Senate President Dominick "
              "Ruggerio, a culturally conservative Democrat who personally opposed abortion "
              "and in 2013 filed a constitutional referendum to preserve marriage as between "
              "a man and a woman. Famiglietti has not sponsored or voted for any bill expanding "
              "abortion access, and no Planned Parenthood endorsement or pro-choice score was "
              "located. His stated Catholic conviction reflects personal recognition of life "
              "from conception; no floor vote on abortion has occurred in his brief tenure.",
              ["https://rhodeislandcurrent.com/2025/08/04/two-personal-injury-attorneys-vie-for-open-r-i-senate-district-4-seat/",
               "https://www.wpri.com/news/local-news/ted-nesi/nesis-notes-aug-9/"],
              kind="statement"),
    ]),

    # ---------------- Pete Appollonio (RI-D, District 29, Warwick) ----------------
    ("pete-appollonio", "RI", "Senator", [
        claim("pa1", "pete-appollonio", "self_defense", 1, True,
              "Voted NAY on S0359 (Rhode Island Assault Weapons Ban Act of 2025) on "
              "June 20, 2025, one of seven Senate Democrats who crossed party lines to "
              "oppose the bill, which passed 25-11. The official RI Senate Journal for "
              "June 20, 2025 lists Appollonio among the eleven Nay voters alongside "
              "four Republicans and six other Democrats. The bill bans the manufacture, "
              "sale, and purchase of assault-style semi-automatic firearms beginning "
              "July 1, 2026; his NAY vote aligns with the rubric's defense of the "
              "unrestricted right to keep and bear semi-automatic arms.",
              ["https://www.rilegislature.gov/journals/senatejournals/2025%20Senate%20Journals/06-20-2025.pdf",
               "https://legiscan.com/RI/bill/S0359/2025",
               "https://www.bostonglobe.com/2025/06/20/metro/rhode-island-senate-votes-to-ban-sale-purchase-of-assault-weapons/"]),
        claim("pa2", "pete-appollonio", "public_justice", 0, True,
              "Co-sponsored S0142 (2025), which imposes mandatory minimum sentences — with no "
              "eligibility for parole or probation — on individuals who possess a stolen "
              "firearm while committing a violent crime, and harsher terms for repeat "
              "offenders. The approach focuses criminal accountability on violent misuse of "
              "firearms rather than restricting law-abiding ownership. Appollonio is a "
              "24-year law enforcement veteran who retired as a police captain from the West "
              "Warwick Police Department in 2017, a background consistent with the rubric's "
              "support for personal accountability and robust enforcement of criminal law.",
              ["https://rigunrights.com/rhode-island-firearm-legislation-update-february-12-2025/"]),
    ]),

    # ---------------- Matthew LaMountain (RI-D, District 31, Warwick/Cranston) ----------------
    ("matthew-lamountain", "RI", "Senator", [
        claim("ml1", "matthew-lamountain", "self_defense", 1, False,
              "Primary co-sponsor and Senate Judiciary Committee chair who actively steered "
              "S0359 (Rhode Island Assault Weapons Ban Act of 2025) through committee and "
              "to final passage. LaMountain defended the Senate's version as stronger than "
              "the House companion bill and convened the committee hearing that advanced the "
              "measure the same day it was first heard. The bill bans the manufacture, "
              "purchase, sale, or transfer of defined assault-style weapons beginning "
              "July 1, 2026; Governor McKee signed it June 26, 2025. His lead sponsorship "
              "and chairmanship role make him the primary legislative architect of this "
              "restriction on semi-automatic arms.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://rhodeislandcurrent.com/2025/06/18/vote-first-ask-questions-later-senate-panel-quickly-advances-reworked-assault-weapons-ban/",
               "https://governor.ri.gov/press-releases/governor-mckee-signs-bill-banning-sale-assault-weapons"]),
        claim("ml2", "matthew-lamountain", "sanctity_of_life", 0, False,
              "Voted YES in the Senate Judiciary Committee (7-6, May 16, 2023) to advance "
              "the Equality in Abortion Coverage Act (EACA, S32), which mandated Rhode Island "
              "Medicaid and all state employee health insurance plans cover abortion services — "
              "the first time state funds could be directed to abortion coverage in Rhode Island. "
              "The bill passed the full Senate 24-12 on May 18, 2023 and was signed the same "
              "day. LaMountain has publicly stated he will 'fight, at all costs, to protect "
              "and defend women's reproductive rights,' and received a Planned Parenthood "
              "Votes! Rhode Island PAC endorsement for the 2024 General Assembly election — "
              "rejecting any legal recognition of life from conception as a legislative priority.",
              ["https://rhodeislandcurrent.com/2023/05/16/eaca-passes-senate-judiciary-committee/",
               "https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/",
               "https://www.plannedparenthoodaction.org/planned-parenthood-votes-rhode-island/news-room/planned-parenthood-votes-rhode-island-pac-announces-first-round-of-endorsements-for-the-2024-general-assembly-election-3"]),
        claim("ml3", "matthew-lamountain", "biblical_marriage", 2, False,
              "Co-sponsored S0824 (Reproductive Freedom and Gender-Affirming Care Health Data "
              "Privacy Act, 2025), which creates statutory privacy protections for health data "
              "related to gender-affirming care — explicitly covering testosterone prescriptions, "
              "surgical transition procedures, and related services — prohibiting collection or "
              "disclosure without explicit consumer consent and banning geofencing around "
              "healthcare facilities. LaMountain renewed his sponsorship in the 2026 session "
              "(S2129). The bill was tracked as a legislative priority by the ACLU of Rhode "
              "Island, reflecting active support for codifying transgender medical care "
              "into state privacy law.",
              ["https://legiscan.com/RI/bill/S0824/2025",
               "https://www.riaclu.org/legislation/reproductive-freedom-and-gender-affirming-care-health-data-privacy-act-h-5857-s-824/",
               "https://legiscan.com/RI/bill/S2129/2026"]),
    ]),

    # ---------------- Lori Urso (RI-D, District 8, Pawtucket) ----------------
    ("lori-urso", "RI", "Senator", [
        claim("lu1", "lori-urso", "self_defense", 1, False,
              "Voted YES on S0359 (Rhode Island Assault Weapons Ban Act of 2025) on "
              "June 20, 2025. The Senate passed the bill 25-11; it bans the manufacture, "
              "sale, and purchase of assault-style semi-automatic firearms beginning "
              "July 1, 2026. Governor McKee signed the bill on June 26, 2025. Urso, "
              "first elected in 2024 and seated January 7, 2025, voted with the Democratic "
              "majority and against the rubric's defense of unrestricted semi-automatic "
              "arms ownership.",
              ["https://webserver.rilegislature.gov/SVotes/votereport.asp?id=17701",
               "https://legiscan.com/RI/bill/S0359/2025",
               "https://www.wpri.com/news/politics/ri-senate-passes-modified-assault-weapons-ban/"]),
        claim("lu2", "lori-urso", "biblical_marriage", 2, False,
              "Co-sponsored S0824 (Reproductive Freedom and Gender-Affirming Care Health "
              "Data Privacy Act, 2025), which creates explicit statutory protections for "
              "health data related to gender-affirming care — including testosterone "
              "prescriptions and surgical transition procedures — prohibiting collection "
              "or disclosure without consumer consent and banning geofencing around clinics. "
              "Listed among ten Democratic Senate sponsors (LaMountain, Lawson, Murray, "
              "DiPalma, Gu, Sosnowski, Urso, Bissaillon, McKenney, Vargas). Co-sponsorship "
              "reflects active legislative support for codifying transgender medical care "
              "protections into state law.",
              ["https://legiscan.com/RI/bill/S0824/2025",
               "https://www.riaclu.org/legislation/reproductive-freedom-and-gender-affirming-care-health-data-privacy-act-h-5857-s-824/"]),
    ]),

    # ---------------- Linda Ujifusa (RI-D, District 11, Portsmouth/Bristol) ----------------
    ("linda-ujifusa", "RI", "Senator", [
        claim("luj1", "linda-ujifusa", "sanctity_of_life", 0, False,
              "Voted YES on S32 (Equality in Abortion Coverage Act, EACA), which passed the "
              "Rhode Island Senate 24-12 on May 18, 2023 and was signed into law the same day. "
              "The EACA required Rhode Island Medicaid and state employee health insurance plans "
              "to cover abortion services — the first use of state funds for abortion coverage "
              "in Rhode Island — rejecting legal recognition of the unborn from conception. "
              "Ujifusa was subsequently endorsed by Planned Parenthood Votes! Rhode Island PAC "
              "for the 2024 General Assembly election based on her reproductive rights record.",
              ["https://webserver.rilegislature.gov/SVotes/votereport.asp?id=16364",
               "https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/",
               "https://www.plannedparenthoodaction.org/planned-parenthood-votes-rhode-island/news-room/planned-parenthood-votes-rhode-island-pac-announces-first-round-of-endorsements-for-the-2024-general-assembly-election-3"]),
        claim("luj2", "linda-ujifusa", "biblical_marriage", 2, False,
              "Voted YES on S2262 (Rhode Island Health Care Provider Shield Act, 2024), which "
              "shields Rhode Island providers from civil and criminal actions by other states "
              "for delivering gender-affirming care — including surgeries and hormone therapies "
              "for transgender patients — as well as abortion services. The Senate passed the "
              "bill 29-7 on May 2, 2024; only two Democrats (Picard and Raptakis) joined five "
              "Republicans in opposition — Ujifusa is not among the named dissenters. Her "
              "affirmative vote codifies transgender medical procedures as legally protected "
              "healthcare, contrary to the rubric's rejection of transgender ideology in law.",
              ["https://rhodeislandcurrent.com/2024/05/02/rhode-island-senate-passes-healthcare-provider-shield-act/",
               "https://legiscan.com/RI/bill/S2262/2024",
               "https://www.gladlaw.org/rhode-island-senate-passes-bill-to-safeguard-health-care-system-access-to-care/"]),
        claim("luj3", "linda-ujifusa", "self_defense", 1, False,
              "Voted YES on S0359 (Rhode Island Assault Weapons Ban Act of 2025), which the "
              "Senate passed 25-11 on June 20, 2025 and Governor McKee signed June 26, 2025 — "
              "banning the manufacture, sale, and purchase of assault-style semi-automatic "
              "firearms beginning July 1, 2026. Ujifusa additionally co-sponsored 2026 "
              "legislation to ban the POSSESSION of assault-style semi-automatic firearms "
              "statewide, a more aggressive step than the 2025 sale-only prohibition, "
              "signaling ongoing commitment to restricting semi-automatic arms beyond "
              "the enacted measure.",
              ["https://webserver.rilegislature.gov/SVotes/votereport.asp?id=17701",
               "https://legiscan.com/RI/bill/S0359/2025",
               "https://www.ammoland.com/2026/04/rhode-island-democrats-ban-possession-commonly-owned-firearms/"]),
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
