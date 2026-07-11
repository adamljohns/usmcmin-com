#!/usr/bin/env python3
"""Enrichment batch 673: 5 Rhode Island Democratic state senators.

Federal pools fully exhausted; continuing the archetype_party_default
state-senator pool in RI (bottom of alphabet).  All five are Democrats;
claims document positions that do not align with the God-First/America-First
rubric (score_impact=False) and are sourced from the RI General Assembly
website, LegiScan, Boston Globe, GLAD Law, Rhode Island Current, Ballotpedia,
and official governor's press releases.

Targets (next 5 from the remaining RI pool after batch 672):
  Robert Britto      (District 18, East Providence / Rumford)
  Louis DiPalma      (District 12, Middletown / Tiverton / Newport — Finance Chair, AWB author)
  Melissa Murray     (District 24, Woonsocket / North Smithfield — first openly LGBTQ+ Woonsocket official)
  Meghan Kallman     (District 15, Pawtucket / Providence — EACA cosponsor)
  Mark McKenney      (District 30, Warwick — Senate Rules Chair, AWB sponsor, Freedom to Read Act)
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
    # ---------------- Robert Britto (RI-D, District 18) ----------------
    ("robert-britto", "RI", "Senator", [
        claim("rb1", "robert-britto", "self_defense", 1, False,
              "Voted YEA on S0359 (Rhode Island Assault Weapons Ban Act of 2025), which prohibits the "
              "manufacture, sale, and purchase of assault-style semi-automatic rifles, shotguns, and "
              "handguns beginning July 1, 2026 — opposing the rubric's defense of the unrestricted "
              "right to keep and bear semi-automatic arms. The bill passed the Senate 25–11 on June 20, 2025.",
              ["https://www.rilegislature.gov/journals/senatejournals/2025%20Senate%20Journals/06-20-2025.pdf",
               "https://legiscan.com/RI/bill/S0359/2025"]),
        claim("rb2", "robert-britto", "sanctity_of_life", 0, False,
              "Voted for Rhode Island's Equality in Abortion Coverage Act (EACA, 2023), which mandates "
              "that Medicaid and all state-regulated insurance plans cover abortion services with no "
              "cost-sharing — expanding taxpayer-funded abortion access statewide. Despite publicly "
              "stating 'I don't like the fact that anyone would have an abortion,' Britto cast a "
              "yea vote, showing legislative support for abortion access overrides any personal "
              "objection and rejects legal recognition of life from conception.",
              ["https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/",
               "https://ballotpedia.org/Robert_Britto"]),
    ]),

    # ---------------- Louis DiPalma (RI-D, District 12, Finance Chair) ----------------
    ("louis-dipalma", "RI", "Senator", [
        claim("ld1", "louis-dipalma", "self_defense", 1, False,
              "Primary sponsor and principal legislative architect of Rhode Island S0359 "
              "(Assault Weapons Ban Act of 2025), which bans the manufacture, sale, and "
              "purchase of assault-style firearms beginning July 1, 2026. DiPalma stated: "
              "'Banning assault weapons is a long overdue, common-sense step to address the "
              "serious public health issue of gun violence in Rhode Island. Research clearly "
              "shows a ban will save lives and make our communities safer.' Signed into law "
              "June 26, 2025.",
              ["https://legiscan.com/RI/bill/S0359/2025",
               "https://governor.ri.gov/press-releases/governor-mckee-signs-bill-banning-sale-assault-weapons"]),
        claim("ld2", "louis-dipalma", "biblical_marriage", 2, False,
              "Voted for Rhode Island S2262 (Health Care Provider Shield Act, 2024), which "
              "passed the RI Senate and was signed into law, shielding providers who deliver "
              "abortion care and gender-affirming (transgender) care from out-of-state "
              "prosecution. The law explicitly names gender-affirming procedures as protected "
              "health care — rejecting the rubric's position that the transgender ideology "
              "should be refused.",
              ["https://www.gladlaw.org/rhode-island-senate-passes-bill-to-safeguard-health-care-system-access-to-care/",
               "https://governor.ri.gov/press-releases/governor-mckee-signs-legislation-supporting-reproductive-health-care-lgbtq-community"]),
    ]),

    # ---------------- Melissa Murray (RI-D, District 24) ----------------
    ("melissa-murray", "RI", "Senator", [
        claim("mmu1", "melissa-murray", "biblical_marriage", 2, False,
              "Senate sponsor of S2262 (Rhode Island Health Care Provider Shield Act, 2024), "
              "which protects healthcare providers who deliver gender-affirming care and abortion "
              "services from out-of-state legal proceedings. Murray, who is the first openly "
              "LGBTQ+ elected official in Woonsocket, stated the law 'affirms Rhode Island's "
              "commitment to protect all citizens, especially LGBTQIA+ people.' Signed by "
              "Governor McKee in June 2024.",
              ["https://governor.ri.gov/press-releases/governor-mckee-signs-legislation-supporting-reproductive-health-care-lgbtq-community",
               "https://www.gladlaw.org/rhode-island-senate-passes-bill-to-safeguard-health-care-system-access-to-care/"]),
        claim("mmu2", "melissa-murray", "self_defense", 1, False,
              "Voted YEA on S0359 (Rhode Island Assault Weapons Ban Act of 2025), which bans "
              "the sale, manufacture, and purchase of assault-style semi-automatic firearms "
              "beginning July 1, 2026. The bill passed the Senate 25–11 on June 20, 2025.",
              ["https://www.rilegislature.gov/journals/senatejournals/2025%20Senate%20Journals/06-20-2025.pdf",
               "https://legiscan.com/RI/bill/S0359/2025"]),
        claim("mmu3", "melissa-murray", "sanctity_of_life", 0, False,
              "A longstanding abortion-rights advocate in the Rhode Island Senate who has "
              "publicly called for abortion protection bills to advance to full floor votes "
              "and has championed legislation expanding abortion access; represents Woonsocket, "
              "where she has built her career as an openly LGBTQ+ lawmaker on a platform of "
              "full reproductive freedom — rejecting legal personhood from conception.",
              ["https://ballotpedia.org/Melissa_Murray",
               "https://www.rilegislature.gov/senators/murray/Pages/Biography.aspx"]),
    ]),

    # ---------------- Meghan Kallman (RI-D, District 15) ----------------
    ("meghan-kallman", "RI", "Senator", [
        claim("mk1", "meghan-kallman", "sanctity_of_life", 0, False,
              "Cosponsored Rhode Island's Equality in Abortion Coverage Act (EACA, 2023), "
              "mandating Medicaid and private insurance coverage of abortion with no cost-sharing. "
              "Kallman has explicitly stated: 'Access to full-spectrum reproductive healthcare, "
              "including contraception, abortion, and birth support is crucial, and I will always, "
              "always fight for a future with full reproductive freedom for all — no matter who "
              "you are, where you live, or how much you make.' This posture rejects any "
              "legal recognition of life beginning at conception.",
              ["https://rhodeislandcurrent.com/2023/05/18/equality-in-abortion-coverage-act-becomes-law-in-rhode-island/",
               "https://ballotpedia.org/Meghan_Kallman"]),
        claim("mk2", "meghan-kallman", "self_defense", 1, False,
              "Voted YEA on S0359 (Rhode Island Assault Weapons Ban Act of 2025), which "
              "prohibits the sale, manufacture, and purchase of assault-style firearms "
              "effective July 1, 2026. The bill passed the Senate 25–11 on June 20, 2025. "
              "Kallman has stated she believes 'commonsense gun reform is overdue.'",
              ["https://www.rilegislature.gov/journals/senatejournals/2025%20Senate%20Journals/06-20-2025.pdf",
               "https://legiscan.com/RI/bill/S0359/2025"]),
        claim("mk3", "meghan-kallman", "biblical_marriage", 4, False,
              "Sponsored the Rhode Island Fair Housing Practices Act, which bars housing "
              "discrimination against renters based on gender identity or expression — "
              "encoding LGBTQ protections into state housing law and extending the state's "
              "promotion of gender-identity ideology into economic transactions, contrary "
              "to the rubric's opposition to government promotion of LGBTQ ideology.",
              ["https://ballotpedia.org/Meghan_Kallman",
               "https://legiscan.com/RI/people/meghan-kallman/id/22356"]),
    ]),

    # ---------------- Mark McKenney (RI-D, District 30) ----------------
    ("mark-mckenney", "RI", "Senator", [
        claim("mmc1", "mark-mckenney", "self_defense", 1, False,
              "Among the Rhode Island Senate Democrats who sponsored and advanced legislation "
              "to ban the sale of assault weapons, a stated legislative priority on his "
              "official campaign platform; supported S0359 (Assault Weapons Ban Act of 2025), "
              "which the Senate passed 25–11 on June 20, 2025 and Governor McKee signed "
              "into law on June 26, 2025.",
              ["https://www.markmckenney.com/meet-mark",
               "https://legiscan.com/RI/bill/S0359/2025"]),
        claim("mmc2", "mark-mckenney", "family_child_sovereignty", 0, False,
              "Championed the Freedom to Read Act in the Rhode Island Senate, legislation "
              "that restricts book-removal efforts in public school and library settings "
              "and opposes community and parental requests to pull materials from school "
              "library collections — placing state authority over library content above "
              "parental and community oversight rights, contrary to the rubric's defense "
              "of parental rights in education.",
              ["https://www.markmckenney.com/meet-mark",
               "https://ballotpedia.org/Mark_McKenney"]),
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
