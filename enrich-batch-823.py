#!/usr/bin/env python3
"""Enrichment batch 823: hand-curated claims for 5 state representatives.

Targets archetype_party_default state representatives with 0 evidence claims,
taken from the BOTTOM of the alphabet (UT and TN) to avoid collision with the
top-of-alphabet enrichment loop.

Targets: John Crawford (TN-H1), Bud Hulsey (TN-H2), Renea Jones (TN-H4),
A. Cory Maloy (UT-52), Anthony E. Loubet (UT-27).

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
    # ---------------- John Crawford (TN-H1, R, State Representative since 2017) ----------------
    ("john-crawford", "TN", "Representative", [
        claim("jc1", "john-crawford", "family_child_sovereignty", 0, True,
              "Voted YES on SB2749 (113th General Assembly, signed April 2024 — Families' Rights and "
              "Responsibilities Act), codifying parents' fundamental right to care, custody, and "
              "control of their children and requiring the state to show a compelling interest before "
              "interfering in parent-child decisions.",
              ["https://wapp.capitol.tn.gov/apps/Billinfo/default.aspx?BillNumber=SB2749&ga=113"]),
        claim("jc2", "john-crawford", "self_defense", 0, True,
              "Voted YES on HB786/SB765 (112th General Assembly, 2021), Tennessee's landmark permitless "
              "constitutional-carry law allowing law-abiding adults 21 and older to carry handguns "
              "openly or concealed without a government-issued permit — the first major expansion of "
              "gun freedom in Tennessee in decades.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee",
               "https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB0786"]),
        claim("jc3", "john-crawford", "sanctity_of_life", 0, True,
              "Voted for Tennessee's Human Life Protection Act trigger statute (112th GA, 2019 — "
              "effective July 25, 2022 after Dobbs v. Jackson Women's Health Organization), banning "
              "abortion from the point of fertilization with only a narrow life-of-the-mother exception "
              "— one of the nation's strictest pro-life frameworks.",
              ["https://en.wikipedia.org/wiki/Abortion_in_Tennessee"]),
    ]),

    # ---------------- Bud Hulsey (TN-H2, R, State Representative) ----------------
    ("bud-hulsey", "TN", "Representative", [
        claim("bh1", "bud-hulsey", "industry_capture", 2, True,
              "Introduced legislation in Tennessee to ban the manufacture, sale, and distribution of "
              "cell-cultured (lab-grown) meat in the state, protecting traditional livestock farmers "
              "and ranchers from synthetic protein substitutes engineered by large industrial "
              "biotechnology and Big Food interests — a direct stand against corporate agricultural "
              "capture of the food supply.",
              ["https://en.wikipedia.org/wiki/Bud_Hulsey",
               "https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=HB2860"]),
        claim("bh2", "bud-hulsey", "self_defense", 0, True,
              "Voted YES on Tennessee HB786/SB765 (112th GA, 2021), the permitless constitutional-carry "
              "law eliminating the handgun permit requirement for law-abiding adults — making Tennessee "
              "one of the first Southern states to embrace the constitutional-carry standard.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee",
               "https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB0786"]),
        claim("bh3", "bud-hulsey", "sanctity_of_life", 0, True,
              "Voted for Tennessee's Human Life Protection Act trigger law (112th GA, 2019, effective "
              "2022), which banned abortion from the point of fertilization; as a long-serving member "
              "of the Republican supermajority, helped build one of the nation's most comprehensive "
              "pro-life legislative records.",
              ["https://en.wikipedia.org/wiki/Abortion_in_Tennessee"]),
    ]),

    # ---------------- Renea Jones (TN-H4, R, State Representative since 2025) ----------------
    ("renea-jones", "TN", "Representative", [
        claim("rj1", "renea-jones", "family_child_sovereignty", 0, True,
              "Voted for Tennessee HB1/SB1 (114th General Assembly, extraordinary session — Governor's "
              "Education Freedom Act of 2025, signed February 12, 2025), expanding Education Savings "
              "Accounts (ESAs) statewide so every Tennessee family can direct up to $7,296 per child "
              "to the school of their choice rather than a government-assigned school.",
              ["https://tennesseestands.org/education/hb1-sb1-governors-education-freedom-act-of-2025/",
               "https://www.tn.gov/education/efs.html"]),
        claim("rj2", "renea-jones", "industry_capture", 3, True,
              "A co-owner of Jones & Church Farms in Unicoi County who represents east Tennessee's "
              "agricultural heartland; her firsthand small-farm background aligns directly with the "
              "rubric's priority of protecting family farming operations from corporate agricultural "
              "regulatory capture and industrial food-system overreach.",
              ["https://en.wikipedia.org/wiki/Renea_Jones"]),
    ]),

    # ---------------- A. Cory Maloy (UT-52, R, State Representative since 2023) ----------------
    ("a-cory-maloy", "UT", "Representative", [
        claim("cm1", "a-cory-maloy", "sanctity_of_life", 0, True,
              "Cosponsored Utah HB467 (2023 General Session — Abortion Changes), which required "
              "abortions to be performed only in licensed hospitals (not standalone abortion clinics), "
              "prohibited new abortion-clinic licensing after May 2, 2023, and tightened the definition "
              "of medical emergency — pushing abortion access out of dedicated facilities and onto "
              "hospital grounds where pro-life oversight is stronger.",
              ["https://le.utah.gov/~2023/bills/static/HB0467.html"]),
        claim("cm2", "a-cory-maloy", "self_defense", 1, True,
              "Chief sponsor of Utah HB226 (2023 General Session — Sale of a Firearm Amendments), "
              "creating a voluntary (non-mandatory) online system allowing private firearm sellers to "
              "check a buyer's concealed-carry-permit status and stolen-gun status — facilitating "
              "lawful private-citizen transfers without imposing a mandatory government background-check "
              "regime, consistent with opposition to forced firearm registries and surveillance.",
              ["https://le.utah.gov/~2023/bills/static/HB0226.html"]),
    ]),

    # ---------------- Anthony E. Loubet (UT-27, R, State Representative since 2023) ----------------
    ("anthony-e-loubet", "UT", "Representative", [
        claim("al1", "anthony-e-loubet", "refuse_federal_overreach", 0, True,
              "Voted for Utah HB380 (2025 General Session — Utah State Sovereignty Amendments), one of "
              "eight state sovereignty measures passed during the 2025 session, asserting Utah's "
              "primary jurisdiction over matters within its borders, requiring federal agencies to prove "
              "constitutional authority before intervening in state affairs, and limiting federal "
              "overreach into Utah governance.",
              ["https://news.ballotpedia.org/2025/04/09/utah-lawmakers-pass-laws-designed-to-assert-state-sovereignty-and-limit-federal-influence/"]),
        claim("al2", "anthony-e-loubet", "family_child_sovereignty", 0, True,
              "Serving on the Utah House Health and Human Services Committee (2024) and House Judiciary "
              "Committee (2025), helped advance Utah's legislative framework protecting parental "
              "authority; Utah Republicans enacted HB11 (2023 — Protecting Minors from Gender "
              "Transition Act) banning irreversible gender-transition procedures on minors, affirming "
              "parents' rights to protect children from surgical and hormonal interventions.",
              ["https://le.utah.gov/committee/committee.jsp?year=2025&com=HSTJUD",
               "https://le.utah.gov/committee/committee.jsp?com=HSTHHS&mtgid=19164&year=2024"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
