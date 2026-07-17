#!/usr/bin/env python3
"""Enrichment batch 726: 5 North Dakota Republican State Senators with 0 claims.

Continuing the ND state-senator pivot from batch 725. Targets reverse-alpha
bucket top-5: Robert Erbele (D28), Randy Lemm (D20), Randy Burckhard (D5),
Paul Thomas (D6), Michelle Powers (D46).

Key sourced bills:
  SB 2392 (2023) — CBDC prohibition, passed 42-5; Erbele/Lemm/Burckhard named in yea list.
  HB 1303 (2025) — anti-sanctuary, passed 41-5; all five targets confirmed YES.
  SB 2307 (2025) — library explicit-content removal; Erbele YES per billsponsor.com.
  HB 1168/1176 (2025) — property tax reform; Burckhard+Thomas co-sponsors; Powers YES 46-0.
  SB 2244 (2025) — parental rights in education; Lemm listed co-sponsor.
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


TARGETS = [
    # ----------- Robert Erbele (ND-28, Lehr, State Senator since 2000) -----------
    ("robert-erbele", "ND", "State Senator", [
        claim("re1", "robert-erbele", "economic_stewardship", 0, True,
              "Voted YES on SB 2392 (2023), which amended North Dakota's definition of "
              "'deposit account' to exclude central bank digital currency, effectively "
              "prohibiting CBDC from being treated as money in the state. The bill passed "
              "42-5 with only Democrats voting no; Erbele was named in the explicit yea list.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2392.html",
               "https://fastdemocracy.com/bill-search/nd/68/bills/NDB00005607/"]),
        claim("re2", "robert-erbele", "family_child_sovereignty", 0, True,
              "Voted YES on SB 2307 (2025), which required public and school libraries to "
              "remove sexually explicit material from general-access areas so minors cannot "
              "access it without parental involvement. The Senate passed the bill 27-20; "
              "Erbele's YES vote is confirmed in billsponsor.com records. Governor Armstrong "
              "ultimately vetoed it, citing 'overreach,' but Erbele supported the child-"
              "protection measure.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo2307.html",
               "https://www.billsponsor.com/bills/651483/north-dakota-senate-bill-2307-session-69"]),
        claim("re3", "robert-erbele", "border_immigration", 2, True,
              "Voted YES on HB 1303 (2025), which strengthened North Dakota's prohibition on "
              "sanctuary city policies, created a Sanctuary Compliance Fund, and established "
              "financial penalties for non-compliant jurisdictions. The Senate passed 41-5; "
              "Erbele's YES was explicitly confirmed — all 5 NO votes were Democrats.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1303.html",
               "https://fastdemocracy.com/bill-search/nd/69/bills/NDB00006121/"]),
    ]),

    # ----------- Randy Lemm (ND-20, State Senator since 2018) -----------
    ("randy-lemm", "ND", "State Senator", [
        claim("rl1", "randy-lemm", "economic_stewardship", 0, True,
              "Voted YES on SB 2392 (2023), prohibiting central bank digital currency in North "
              "Dakota by excluding CBDC from the state's definition of 'deposit account.' The "
              "bill passed 42-5; Lemm was named in the explicit yea list alongside fellow "
              "Republican senators.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2392.html",
               "https://fastdemocracy.com/bill-search/nd/68/bills/NDB00005607/"]),
        claim("rl2", "randy-lemm", "family_child_sovereignty", 0, True,
              "Co-sponsored SB 2244 (2025), creating explicit legal protections for parental "
              "involvement in a child's education. Lemm was listed as one of six co-sponsors "
              "of the bill in the 69th Legislative Assembly, demonstrating a direct commitment "
              "to parental rights in the educational sphere.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo2244.html",
               "https://legiscan.com/ND/text/SB2244/id/3065174"]),
        claim("rl3", "randy-lemm", "border_immigration", 2, True,
              "Voted YES on HB 1303 (2025), the anti-sanctuary city enforcement bill that "
              "created financial penalties for jurisdictions that obstruct immigration "
              "enforcement. The Senate passed 41-5; Lemm's YES was explicitly confirmed. "
              "He also co-sponsored SCR 4002 (2025), urging Congress to allow landowners to "
              "terminate perpetual federal easements — a property-rights/anti-overreach stance.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1303.html",
               "https://fastdemocracy.com/bill-search/nd/69/bills/NDB00006121/"]),
    ]),

    # ----------- Randy Burckhard (ND-5, Minot, State Senator since 2011, Pres. Pro Tem 2021) -----------
    ("randy-burckhard", "ND", "State Senator", [
        claim("rb1", "randy-burckhard", "economic_stewardship", 0, True,
              "Voted YES on SB 2392 (2023), prohibiting CBDC in North Dakota by amending "
              "the definition of 'deposit account' to exclude central bank digital currency. "
              "The bill passed 42-5; Burckhard was named in the explicit yea list.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2392.html",
               "https://fastdemocracy.com/bill-search/nd/68/bills/NDB00005607/"]),
        claim("rb2", "randy-burckhard", "economic_stewardship", 2, True,
              "Co-sponsored HB 1168 (2025), a property tax reform bill to reduce school "
              "district property taxes approximately 16% with state replacement funding and "
              "cap local government levy growth at 3% annually. Burckhard was one of two "
              "Senate co-sponsors. The 2025 session ultimately adopted HB 1176, a related "
              "bill creating a $1,600 primary-residence credit as part of a $473M relief "
              "package, which passed the Senate 46-0.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1168.html",
               "https://northdakotamonitor.com/2025/05/02/north-dakota-legislature-adopts-historic-property-tax-bill-on-final-day-of-session/"]),
        claim("rb3", "randy-burckhard", "border_immigration", 2, True,
              "Voted YES on HB 1303 (2025), strengthening North Dakota's anti-sanctuary law "
              "with financial penalties for non-compliant jurisdictions. Senate passed 41-5; "
              "Burckhard's YES was explicitly confirmed. All 5 NO votes were Democrats.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1303.html",
               "https://fastdemocracy.com/bill-search/nd/69/bills/NDB00006121/"]),
    ]),

    # ----------- Paul Thomas (ND-6, Velva, took office Dec 2024, farmer) -----------
    ("paul-thomas", "ND", "State Senator", [
        claim("pt1", "paul-thomas", "border_immigration", 2, True,
              "Voted YES on HB 1303 (2025), which prohibited sanctuary city policies in North "
              "Dakota, created the Sanctuary Compliance Fund, and attached financial penalties "
              "for non-compliant jurisdictions. The Senate passed 41-5; Thomas's YES was "
              "explicitly confirmed. All 5 NO votes were Democrat senators.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1303.html",
               "https://fastdemocracy.com/bill-search/nd/69/bills/NDB00006121/"]),
        claim("pt2", "paul-thomas", "economic_stewardship", 2, True,
              "Co-sponsored HB 1168 (2025), the ND property tax reform bill reducing school "
              "district property taxes ~16% with state funding and capping local levy growth "
              "at 3% annually — a direct tax-relief and fiscal-restraint measure. Thomas also "
              "sponsored SB 2342 (2025), creating the Value-Added Milk Processing Facility "
              "Incentive Program to build in-state agricultural capacity and reduce dependence "
              "on federal programs, stating: 'What we're doing … is putting an incentive out "
              "there that this is the need we have in this state.'",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1168.html",
               "https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo2342.html",
               "https://northdakotamonitor.com/2025/03/17/north-dakota-dairy-farm-plans-to-add-processing-bill-would-add-state-incentives/"]),
    ]),

    # ----------- Michelle Powers (ND-46, Fargo, took office Dec 2024) -----------
    ("michelle-powers", "ND", "State Senator", [
        claim("mp1", "michelle-powers", "border_immigration", 2, True,
              "Voted YES on HB 1303 (2025), prohibiting sanctuary city policies in North Dakota "
              "with financial enforcement through the Sanctuary Compliance Fund. The Senate "
              "passed 41-5; Powers's YES was explicitly confirmed — all 5 NO votes were "
              "Democrats.",
              ["https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1303.html",
               "https://fastdemocracy.com/bill-search/nd/69/bills/NDB00006121/"]),
        claim("mp2", "michelle-powers", "family_child_sovereignty", 0, True,
              "Ran on an explicit platform of protecting children from harmful content and "
              "sexualized ideology, stating she would fight against 'pornography in schools, "
              "children changing their sex, and children attending drag shows.' Powers "
              "described herself as 'a lifelong North Dakota conservative fighting for the "
              "state she grew up in that believed in freedom of speech and protection of "
              "children and the vulnerable.'",
              ["https://www.powersfordistrict46.com/meet-michelle.html"],
              kind="position"),
        claim("mp3", "michelle-powers", "economic_stewardship", 2, True,
              "Voted YES on HB 1176 (2025), the historic ND property tax relief bill creating "
              "a $1,600 primary-residence credit and tripling the existing credit as part of "
              "a $473M property tax relief package for the 2025-27 biennium. The Senate "
              "passed it unanimously 46-0; Governor Armstrong signed it into law.",
              ["https://northdakotamonitor.com/2025/05/02/north-dakota-legislature-adopts-historic-property-tax-bill-on-final-day-of-session/",
               "https://ndlegis.gov/assembly/69-2025/regular/bill-overview/bo1176.html"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
