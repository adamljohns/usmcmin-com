#!/usr/bin/env python3
"""Enrichment batch 356: 2-3 claims each for 5 Virginia State Senators — bottom of alphabet.

archetype_curated federal pool is fully exhausted (all evidence_curated).
This batch targets evidence_state Virginia State Senators with 0 prior claims,
selected from the reverse-alphabetical bottom of the bucket:

  • Michael Jones     (VA SD-15, D) — sponsored gun-restriction bills; co-sponsored abortion/same-sex amendments
  • Luther Cifers     (VA SD-10, R) — Christian conservative; voted against reproductive freedom amendment
  • Glen Sturtevant   (VA SD-12, R) — sponsored born-alive infant bill; warned against "most extreme" abortion amendment
  • Emily Jordan      (VA SD-17, R) — voted against reproductive freedom amendment & assault weapons ban
  • David Suetterlein (VA SD-4, R)  — supported complete abortion ban; voted against reproductive freedom amendment

Sources: lis.virginia.gov, vpap.org, ballotpedia.org, en.wikipedia.org, legiscan.com, vpm.org, virginiamercury.com
Writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
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
    # ---- Michael Jones (VA SD-15, D) ----
    ("michael-jones", "VA", "State Senate", [
        claim("mj1", "michael-jones", "self_defense", 1, False,
              "As a Virginia Delegate in 2024, Jones sponsored House Bill 22 banning the "
              "manufacture, importation, sale, possession, or transfer of auto sears — "
              "devices that convert semi-automatic firearms to fully automatic fire — "
              "making violations a Class 6 felony effective July 1, 2024. The bill "
              "represents an incremental expansion of state restrictions on legal "
              "firearm components, contrary to the rubric's defense of unrestricted "
              "Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Michael_Jones_(Virginia_politician)",
               "https://ballotpedia.org/Michael_Jones_(Virginia_state_representative)"]),
        claim("mj2", "michael-jones", "sanctity_of_life", 0, False,
              "Co-sponsored the Virginia constitutional amendment (SJ247/2025) to enshrine "
              "a broad 'right to reproductive freedom' in the state constitution — "
              "explicitly rejecting any legislative recognition of personhood from "
              "conception. The amendment, which Jones helped advance through the House "
              "of Delegates, would prohibit the Commonwealth from regulating abortion "
              "in any way that burdens that right.",
              ["https://www.mikejonesva.com/",
               "https://legiscan.com/VA/bill/SJR247/2025"]),
        claim("mj3", "michael-jones", "biblical_marriage", 0, False,
              "Co-sponsored the Virginia constitutional amendment (2025 session) to "
              "enshrine equal marriage rights for same-sex couples in the state "
              "constitution, codifying a legal definition of marriage that rejects "
              "the one-man-one-woman standard the rubric requires. Jones has also "
              "authored legislation extending insurance benefits to same-sex and "
              "unmarried cohabiting couples.",
              ["https://en.wikipedia.org/wiki/Michael_Jones_(Virginia_politician)",
               "https://ballotpedia.org/Michael_Jones_(Virginia_state_representative)"]),
    ]),

    # ---- Luther Cifers (VA SD-10, R) ----
    ("luther-cifers", "VA", "State Senate", [
        claim("lc1", "luther-cifers", "sanctity_of_life", 0, True,
              "A self-described Christian conservative who, in January 2025, cast a NO "
              "vote on SJ247 — the constitutional amendment to create an unlimited 'right "
              "to reproductive freedom' in Virginia — standing with all 19 Senate "
              "Republicans in opposing the measure. His vote reflects a rejection of "
              "abortion-on-demand and support for the state's authority to protect "
              "unborn life.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://ballotpedia.org/Luther_Cifers"]),
        claim("lc2", "luther-cifers", "self_defense", 1, True,
              "Voted NO on SB749 (2026), Virginia's sweeping assault-firearms ban that "
              "prohibits the purchase, sale, manufacture, or transfer of semi-automatic "
              "centerfire rifles with detachable magazines and certain features, as well "
              "as magazines holding more than 15 rounds. All 19 Senate Republicans, "
              "including Cifers, opposed the bill on Second Amendment grounds; "
              "Governor Spanberger signed it into law May 2026.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://www.ammoland.com/2026/03/virginia-assault-firearms-ban-sb749-passes-legislature/"]),
    ]),

    # ---- Glen Sturtevant (VA SD-12, R) ----
    ("glen-sturtevant", "VA", "State Senate", [
        claim("gs1", "glen-sturtevant", "sanctity_of_life", 0, True,
              "Introduced SB548 (2025 session), which would have required that born-alive "
              "infants — babies who survive an attempted abortion — receive the same "
              "medical treatment and care as any other live-born child, with criminal "
              "penalties for non-compliance. The Democrat-controlled Senate killed the "
              "bill in committee. Sturtevant publicly declared the Democrats' "
              "competing abortion constitutional amendment 'the most extreme abortion "
              "amendment in the nation' because it bars the state from regulating "
              "abortion in any way.",
              ["https://lis.virginia.gov/session-details/20251/member-information/S0099/member-details",
               "https://www.osvnews.com/radical-abortion-amendment-passes-virginia-general-assembly-despite-pro-life-advocacy/"]),
        claim("gs2", "glen-sturtevant", "self_defense", 1, True,
              "Voted NO on SB749 (2026), the Democrat-sponsored assault-firearms ban "
              "banning sale and purchase of 'assault firearms' and magazines over 15 "
              "rounds. Sturtevant joined all 18 other Senate Republicans in opposing "
              "the bill; the NRA and Virginia Citizens Defense League (VCDL) both "
              "opposed the measure as unconstitutional.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://www.gunowners.org/va03052026/"]),
        claim("gs3", "glen-sturtevant", "sanctity_of_life", 1, True,
              "Voted NO on SJ247 (January 2025), the constitutional amendment to embed "
              "an unlimited 'right to reproductive freedom' in Virginia's constitution "
              "with no exceptions for gestational limits, parental consent, or health "
              "regulations. Sturtevant warned the amendment 'would protect' human "
              "traffickers and adults who impregnate minors by preventing prosecution "
              "if the victim obtains an abortion in Virginia.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://www.osvnews.com/radical-abortion-amendment-passes-virginia-general-assembly-despite-pro-life-advocacy/"]),
    ]),

    # ---- Emily Jordan (VA SD-17, R) ----
    ("emily-jordan", "VA", "State Senate", [
        claim("ej1", "emily-jordan", "sanctity_of_life", 0, True,
              "Voted NO on SJ247 (January 21, 2025), the Virginia Senate's constitutional "
              "amendment to create an unlimited 'right to reproductive freedom.' "
              "All 19 Senate Republicans cast NO votes, including Jordan, rejecting "
              "the amendment that would have removed all state authority to protect "
              "unborn life from conception.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://ballotpedia.org/Emily_Jordan"]),
        claim("ej2", "emily-jordan", "self_defense", 1, True,
              "Voted NO on SB749 (February 2026), Virginia's assault-firearms ban "
              "prohibiting the sale, purchase, manufacture, and transfer of "
              "semi-automatic centerfire rifles with detachable magazines and "
              "certain features, along with magazines over 15 rounds. Jordan "
              "joined all Senate Republicans in opposing the measure on Second "
              "Amendment grounds; the bill passed 21-19 on a party-line vote.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://virginiamercury.com/2026/05/15/spanberger-signs-assault-weapons-ban-package-of-criminal-justice-and-energy-bills/"]),
    ]),

    # ---- David Suetterlein (VA SD-4, R) ----
    ("david-suetterlein", "VA", "State Senate", [
        claim("ds1", "david-suetterlein", "sanctity_of_life", 0, True,
              "Suetterlein supported in committee a bill that would have banned abortion "
              "in Virginia completely — with only limited exceptions — and imposed felony "
              "penalties for performing illegal abortions. He has repeatedly stated "
              "he views abortion as 'a tragedy' and has advocated for increasing "
              "contraceptive access and family life education to reduce abortion "
              "demand, while opposing the broader availability of elective abortion.",
              ["https://www.roanokerambler.com/roanoke-area-state-senate-candidate-david-suetterlein-interview-question-answer/",
               "https://ballotpedia.org/David_Suetterlein"]),
        claim("ds2", "david-suetterlein", "sanctity_of_life", 1, True,
              "Voted NO on SJ247 (January 21, 2025), the constitutional amendment "
              "to embed an absolute 'right to reproductive freedom' in the Virginia "
              "constitution — a measure that would prohibit any state regulation of "
              "abortion at any stage of pregnancy. Suetterlein was among all 19 "
              "Senate Republicans who rejected the amendment.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://www.vpm.org/news/2025-01-20/virginia-constitutional-amendments-abortion-marriage-equality-voting-rights"]),
        claim("ds3", "david-suetterlein", "self_defense", 1, True,
              "Voted NO on SB749 (2026), Virginia's assault-firearms and high-capacity "
              "magazine ban. Suetterlein has a track record of passing more than 50 "
              "bills into law, many with bipartisan support, but drew a clear line "
              "against gun restrictions, opposing the Democrat-backed firearms ban "
              "on constitutional grounds alongside all Senate Republicans.",
              ["https://lis.virginia.gov/bill-details/20261/SB749",
               "https://www.suetterlein.com/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
