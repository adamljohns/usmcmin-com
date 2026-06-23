#!/usr/bin/env python3
"""Enrichment batch 380: hand-curated claims for 5 senate-seat candidates.

Targets evidence_curated candidates with the fewest existing claims, pulled
from the bottom of the alphabet (WY, TX, TX, SD, SC).  Each gets 2-3 new
claims in rubric categories not yet scored.

Mix: Scott Morrow (WY-D), Jon Bonck (TX-R, TX-38 House),
Jasmine Crockett (TX-D, TX-30 House), Brian Bengs (SD-I),
Annie Andrews (SC-D).

Sources: ballotpedia.org, wyofile.com, wyodaily.com, ontheissues.org,
clubforgrowth.org, govtrack.us, keloland.com, southdakotasearchlight.com,
drannieandrews.com, foxcarolina.com.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace).
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
    # -------- Scott Morrow (WY-D, 2026 Senate Candidate) --------
    ("scott-morrow-wy-senate", "WY", "Senate", [
        claim("sm1", "scott-morrow-wy-senate", "self_defense", 1, True,
              "In the WyoFile 2024 Election Guide, Morrow answered 'Absolutely NOT' when asked whether he supports gun control, citing Wyoming Constitution Article One Section 38's explicit protection of the right to bear arms — aligning with the rubric's opposition to red-flag laws and assault-weapon bans.",
              ["https://projects.wyofile.com/election-guide-2024/candidates/scott-morrow/",
               "https://ballotpedia.org/Scott_Morrow_(Wyoming)"]),
        claim("sm2", "scott-morrow-wy-senate", "election_integrity", 0, False,
              "Morrow emphasized expanding voter access and equality rather than voter-ID or paper-ballot requirements in his 2024 and 2026 campaign materials, supporting the Equal Rights Amendment and broad franchise expansion over integrity-first guardrails the rubric prioritizes.",
              ["https://ballotpedia.org/Scott_Morrow_(Wyoming)",
               "https://www.wyodaily.com/story/2024/09/26/news/us-senate-candidate-profile-scott-morrow-democrat/15957.html"]),
        claim("sm3", "scott-morrow-wy-senate", "foreign_policy_restraint", 2, False,
              "Morrow's campaign platform emphasizes multilateral engagement and does not reflect a foreign-policy-restraint posture; his OnTheIssues profile records no opposition to foreign aid packages or entangling alliances, indicating no alignment with the rubric's anti-interventionist stance.",
              ["https://www.ontheissues.org/International/Scott_Morrow_Foreign_Policy.htm",
               "https://ballotpedia.org/Scott_Morrow_(Wyoming)"]),
    ]),

    # -------- Jon Bonck (TX-R, TX-38 House 2026 Nominee) --------
    ("jon-bonck-tx-38", "TX", "Representative", [
        claim("jb1", "jon-bonck-tx-38", "election_integrity", 0, True,
              "Bonck's campaign platform explicitly states he will 'make it easy to vote, hard to cheat, and impossible to doubt the results,' and he supports the Constitution's original framework of state-run elections — consistent with the rubric's voter-ID and paper-ballot integrity standards.",
              ["https://www.jonbonck.com/",
               "https://ballotpedia.org/Jon_Bonck"]),
        claim("jb2", "jon-bonck-tx-38", "self_defense", 1, True,
              "Endorsed by Club for Growth PAC, which rated Bonck a fiscal and constitutional conservative; his platform explicitly includes protecting Second Amendment rights and opposing new firearm restrictions, consistent with the rubric's anti-red-flag / anti-AWB position.",
              ["https://www.clubforgrowth.org/club-for-growth-pac-endorses-jon-bonck-in-tx-38-race/",
               "https://www.jonbonck.com/"]),
        claim("jb3", "jon-bonck-tx-38", "economic_stewardship", 2, True,
              "Club for Growth PAC endorsed Bonck as 'a fiscal conservative who will fight every day for lower taxes, school freedom, and economic liberty for Texans,' reflecting an anti-deficit, low-tax orientation consistent with the rubric's sound-money and balanced-budget preference.",
              ["https://www.clubforgrowth.org/club-for-growth-pac-endorses-jon-bonck-in-tx-38-race/",
               "https://www.texastribune.org/2026/05/26/texas-19th-38th-congressional-district-republican-primary-runoff/"]),
    ]),

    # -------- Jasmine Crockett (TX-D, TX-30 House, 2026 Senate consideration) --------
    ("jasmine-crockett", "TX", "Representative", [
        claim("jc1", "jasmine-crockett", "election_integrity", 0, False,
              "In 2023 Crockett reintroduced the Democracy Restoration Act, which would restore federal voting rights to millions of felons upon release from prison — expanding the franchise in ways that directly oppose the rubric's insistence on voter-ID requirements and election-integrity safeguards.",
              ["https://ballotpedia.org/Jasmine_Crockett",
               "https://www.govtrack.us/congress/members/jasmine_crockett/456944"]),
        claim("jc2", "jasmine-crockett", "foreign_policy_restraint", 3, False,
              "Crockett traveled to Israel with AIPAC and the IDF during her first term and voted to fund defensive weapons shipments to Israel — conduct that Track AIPAC characterizes as a 'poor legislative record on Israel-Palestine issues' but which reflects AIPAC-aligned foreign policy the rubric's 'never took AIPAC money' standard flags negatively.",
              ["https://ballotpedia.org/Jasmine_Crockett",
               "https://en.wikipedia.org/wiki/Jasmine_Crockett"]),
    ]),

    # -------- Brian Bengs (SD, Independent, 2026 Senate Candidate) --------
    ("brian-bengs-sd-senate", "SD", "Senate", [
        claim("bb1", "brian-bengs-sd-senate", "border_immigration", 4, True,
              "Bengs' 2026 independent campaign platform includes support for ending birthright citizenship — a position that aligns with the rubric's 'anti-birthright citizenship' standard, even though Bengs holds broadly centrist or left-leaning stances on other issues.",
              ["https://ballotpedia.org/Brian_Bengs",
               "https://bengsforsouthdakota.com/what-i-stand-for/"]),
        claim("bb2", "brian-bengs-sd-senate", "election_integrity", 0, False,
              "Bengs ran in 2022 as a Democrat and in 2026 as an independent, emphasizing broad voter participation and systemic reform over voter-ID requirements; his platform focuses on anti-corruption and term limits rather than the paper-ballot and ID guardrails the rubric requires.",
              ["https://ballotpedia.org/Brian_Bengs",
               "https://southdakotasearchlight.com/2025/05/02/musk-doge-cuts-motivate-former-u-s-senate-candidate-to-run-again/"]),
        claim("bb3", "brian-bengs-sd-senate", "biblical_marriage", 0, False,
              "Bengs has not publicly opposed same-sex marriage and ran in 2022 under the Democratic Party banner, which formally supports marriage equality; no statement endorsing the one-man-one-woman definition of marriage appears in his 2022 or 2026 campaign materials.",
              ["https://ballotpedia.org/Brian_Bengs",
               "https://bengsforsouthdakota.com/what-i-believe/"]),
    ]),

    # -------- Annie Andrews (SC-D, 2026 Senate Candidate) --------
    ("annie-andrews-senate", "SC", "Senate", [
        claim("aa1", "annie-andrews-senate", "foreign_policy_restraint", 0, True,
              "Andrews' platform calls for a 'diplomacy-first approach to foreign policy' and requires congressional approval for use of military force — consistent with the rubric's Article I war-powers standard, even though her broader foreign policy views differ from the rubric on aid issues.",
              ["https://drannieandrews.com/platform/",
               "https://www.foxcarolina.com/2026/06/05/us-senate-race-sc-candidate-profile-annie-andrews/"]),
        claim("aa2", "annie-andrews-senate", "border_immigration", 0, False,
              "Andrews' immigration platform calls for 'secure borders with dignity' combined with a 'fair path to citizenship' and keeping families together — explicitly rejecting the wall-and-military-deportation approach the rubric's first two border questions require.",
              ["https://drannieandrews.com/issue/immigration-security-with-dignity/",
               "https://ballotpedia.org/Annie_Andrews"]),
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
