#!/usr/bin/env python3
"""Enrichment batch 793: third claims for 5 WI Republican Assembly Members.

Primary archetype_curated federal pool was fully depleted by batch 757.
This batch adds third claims to WI Assembly Members that already carry
2 evidence_curated claims, drawn from the bottom of the WI roster:

  Chuck Wichgers  (WI-84) — co-authored 2025 AB 560 banning drop boxes
  Cindi Duchow    (WI-97) — authored 2023 AB 69 requiring armed school SROs
  David Steffen   (WI-4)  — co-authored 2023 AJR 77 anti-Zuckerbucks amendment
  Elijah Behnke   (WI-6)  — championed AB 882 / Act 218 (tactical medics carry)
  John Spiros     (WI-86) — co-authored 2025 AB 10 gun-safe sales-tax exemption

Sources: Wisconsin Legislature bill texts (docs.legis.wisconsin.gov),
Ballotpedia, en.wikipedia.org.

NOTE: writes scorecard.json MINIFIED to keep master ~35-36MB under
GitHub's 50MB limit.
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
    # --- Chuck Wichgers (WI-84) ---
    # Existing: sanctity_of_life, industry_capture
    # Adding:   election_integrity[0]
    ("chuck-wichgers-wi-84", "WI", "Assembly Member", [
        claim("cw3", "chuck-wichgers-wi-84", "election_integrity", 0, True,
              "Co-introduced Wisconsin Assembly Bill 560 (October 2025), which prohibits "
              "any municipality from employing a drop box or other physical receptacle "
              "for the receipt of voted absentee ballots other than receipt by mail or "
              "in-person at the municipal clerk's office. The bill restores the "
              "Wisconsin Supreme Court's 2022 Teigen v. Wisconsin Elections Commission "
              "ruling that had already found drop boxes unlawful under state statutes, "
              "and permanently codifies that prohibition in statute so that no future "
              "Elections Commission guidance can authorize them again. Wichgers was one "
              "of the primary co-authors of AB 560, alongside Representatives Brill, "
              "Piwowarczyk, Allen, Behnke, and others. Eliminating unsecured drop boxes "
              "reduces chain-of-custody vulnerabilities in absentee ballot collection "
              "and aligns with the God-First rubric's election-integrity standard of "
              "ensuring that every returned ballot can be traced to a verified voter "
              "through a secure, auditable process.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab560",
               "https://ballotpedia.org/Chuck_Wichgers"]),
    ]),

    # --- Cindi Duchow (WI-97) ---
    # Existing: sanctity_of_life, family_child_sovereignty
    # Adding:   self_defense[0]
    ("cindi-duchow-wi-97", "WI", "Assembly Member", [
        claim("cd3", "cindi-duchow-wi-97", "self_defense", 0, True,
              "Introduced Wisconsin Assembly Bill 69 (February 2023), which requires "
              "public schools that experience 100 or more incidents on school grounds "
              "during a semester — at least 25 of which result in arrests — to employ "
              "or contract for the employment of a sworn, armed law enforcement officer "
              "as a school resource officer. The bill also directs that American Rescue "
              "Plan Act federal funding be made available to reimburse school districts "
              "for the costs of employing armed school resource officers, removing a "
              "financial barrier to implementation. Duchow's legislation embodies the "
              "conviction that the answer to violent threats in schools is the presence "
              "of trained, armed defenders rather than restricting the law-abiding. "
              "By mandating armed protection as the statutory response to school "
              "violence, AB 69 reflects the God-First rubric's premise that the right "
              "of self-defense — and the defense of the innocent — is a proper and "
              "necessary governmental obligation, not an obstacle to be regulated away.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab69",
               "https://ballotpedia.org/Cindi_Duchow"]),
    ]),

    # --- David Steffen (WI-4) ---
    # Existing: sanctity_of_life, economic_stewardship
    # Adding:   election_integrity[0]
    ("david-steffen-wi-4", "WI", "Assembly Member", [
        claim("ds3", "david-steffen-wi-4", "election_integrity", 0, True,
              "Co-authored Wisconsin Assembly Joint Resolution 77 (September 2023), a "
              "proposed constitutional amendment that would prohibit state and local "
              "governments from using privately sourced moneys or equipment in "
              "connection with the conduct of elections. AJR 77 was first introduced "
              "in the 2021-22 session as Senate Joint Resolution 101 and must pass two "
              "consecutive legislative sessions before going to voters as a referendum. "
              "The measure directly targets the practice of accepting large private "
              "grants — such as the $8.8 million in 2020 Zuckerberg / CTCL funding "
              "that flowed into Wisconsin's five largest cities — to fund election "
              "administration, a practice critics argue creates two-tiered election "
              "infrastructure that advantages well-resourced, Democrat-leaning urban "
              "jurisdictions. Steffen's co-authorship reflects a commitment to ensuring "
              "that election administration is funded exclusively through public "
              "appropriations subject to legislative oversight, not private philanthropy "
              "with its own ideological or partisan agenda.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ajr77",
               "https://ballotpedia.org/David_Steffen"]),
    ]),

    # --- Elijah Behnke (WI-6) ---
    # Existing: sanctity_of_life, christian_liberty
    # Adding:   self_defense[0]
    ("elijah-behnke-wi-6", "WI", "Assembly Member", [
        claim("eb3", "elijah-behnke-wi-6", "self_defense", 0, True,
              "Championed Wisconsin Assembly Bill 882 (2023-24 session), which allows "
              "a tactical emergency medical services professional (tactical TEMS) — "
              "a person certified by the Law Enforcement Standards Board under "
              "Wisconsin statute 165.85(3) who provides emergency medical care in "
              "high-risk tactical law-enforcement environments — to carry a firearm "
              "in areas where carrying would otherwise be prohibited by law. AB 882 "
              "was tabled but its companion Senate Bill 829 advanced; the bill's "
              "substance was enacted as 2023 Wisconsin Act 218, signed into law on "
              "March 26, 2024. Act 218 expands lawful armed carry rights for a class "
              "of emergency responders whose role requires them to operate in active "
              "threat environments, removing a statutory prohibition that left them "
              "unarmed in exactly the situations where they most need to be armed. "
              "Behnke's authorship reflects the conviction that the right to keep "
              "and bear arms for the defense of persons should follow the defender "
              "into the field rather than being forfeited at a jurisdictional "
              "threshold.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab882",
               "https://docs.legis.wisconsin.gov/2023/related/acts/218.pdf",
               "https://ballotpedia.org/Elijah_Behnke"]),
    ]),

    # --- John Spiros (WI-86) ---
    # Existing: sanctity_of_life, election_integrity
    # Adding:   self_defense[1]
    ("john-spiros-wi-86", "WI", "Assembly Member", [
        claim("js3", "john-spiros-wi-86", "self_defense", 1, True,
              "Co-authored Wisconsin Assembly Bill 10 (February 2025), which creates "
              "a sales and use tax exemption for the sale of gun safes — secure "
              "storage units designed to prevent unauthorized access to firearms. "
              "AB 10 was introduced by Representative Neylon, Spiros, and others, "
              "with multiple Senate co-sponsors. By removing the sales tax from gun "
              "safes, the bill lowers the financial burden on responsible gun owners "
              "who choose to invest in secure storage, without mandating storage or "
              "creating a new regulatory layer. Spiros chairs the Assembly Committee "
              "on Criminal Justice and Public Safety, giving him outsized influence "
              "over firearms-related legislation. His co-authorship of AB 10 reflects "
              "the view that government should reduce the cost of responsible gun "
              "ownership rather than imposing fees, taxes, or regulations that "
              "function as de facto restrictions on the exercise of Second Amendment "
              "rights — a position consistent with the God-First rubric's "
              "anti-restriction standard.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab10",
               "https://ballotpedia.org/John_Spiros"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
