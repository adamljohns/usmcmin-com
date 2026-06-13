#!/usr/bin/env python3
"""Enrichment batch 182: hand-curated claims for 5 federal House members.

Targets evidence_federal representatives with 0 claims, taken from the
BOTTOM of the alphabet (CA + AZ). All D members.

Candidates: Sam Liccardo (CA-16 D), Mike Thompson (CA-04 D),
Maxine Waters (CA-43 D), Jared Huffman (CA-02 D),
Yassamin Ansari (AZ-03 D).

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
    # ---------------- Sam Liccardo (CA-16, D) ----------------
    ("sam-liccardo", "CA", "Representative", [
        claim("sl1", "sam-liccardo", "self_defense", 1, False,
              "As San Jose mayor, signed the nation's first ordinance requiring gun owners to carry mandatory liability insurance and pay an annual fee (Jan 25, 2022); ordinance survived federal court challenges. As U.S. Representative, cosponsored H.R.1307, the Office of Gun Violence Prevention Act of 2025 — actively extending rather than rolling back gun-control infrastructure.",
              ["https://en.wikipedia.org/wiki/Sam_Liccardo",
               "https://www.congress.gov/bill/119th-congress/house-bill/1307"]),
        claim("sl2", "sam-liccardo", "border_immigration", 2, False,
              "As mayor of San Jose (2014–2022), presided over and maintained the city's sanctuary policies prohibiting city police from cooperating with federal immigration detainer requests; his public record and House voting history reflect no repudiation of those anti-enforcement sanctuary stances.",
              ["https://ballotpedia.org/Sam_Liccardo",
               "https://en.wikipedia.org/wiki/Sam_Liccardo"]),
    ]),

    # ---------------- Mike Thompson (CA-04, D) ----------------
    ("mike-thompson-ca-04", "CA", "Representative", [
        claim("mt1", "mike-thompson-ca-04", "self_defense", 1, False,
              "Chairs the House Gun Violence Prevention Task Force since its founding; introduced the Federal Extreme Risk Protection Order Act to expand red-flag laws nationwide; publicly called for full ATF funding — firmly opposing constitutional carry and any rollback of gun restrictions.",
              ["https://mikethompson.house.gov/issues/gun-violence-prevention",
               "https://en.wikipedia.org/wiki/Mike_Thompson_(California_politician)"]),
        claim("mt2", "mike-thompson-ca-04", "border_immigration", 2, False,
              "Co-introduced the 'Police not ICE Act' (2025) with Rep. Nydia Velázquez to prohibit ICE and CBP officers from wearing clothing bearing the word 'police,' explicitly to shield immigrant communities from federal enforcement personnel — directly undermining anti-sanctuary enforcement.",
              ["https://mikethompson.house.gov/newsroom/press-releases/thompson-velazquez-seek-block-immigration-feds-identifying-local-police",
               "https://ballotpedia.org/Mike_Thompson_(California)"]),
    ]),

    # ---------------- Maxine Waters (CA-43, D) ----------------
    ("maxine-waters", "CA", "Representative", [
        claim("mw1", "maxine-waters", "sanctity_of_life", 0, False,
              "Lifetime 100% rating from NARAL Pro-Choice America and an F rating from the Susan B. Anthony List; cosponsored the Women's Health Protection Act of 2025 (H.R.12) to enshrine a federal right to abortion with no gestational limits — directly opposing life-at-conception personhood protections.",
              ["https://ballotpedia.org/Maxine_Waters",
               "https://www.congress.gov/bill/119th-congress/house-bill/12"]),
        claim("mw2", "maxine-waters", "biblical_marriage", 1, False,
              "Received the 2025 PFLAG National Champion of Justice award; voted for the Respect for Marriage Act (2022) codifying same-sex marriage in federal law; has a decades-long legislative record opposing any one-man-one-woman definition of marriage.",
              ["https://ballotpedia.org/Maxine_Waters",
               "https://en.wikipedia.org/wiki/Maxine_Waters"]),
    ]),

    # ---------------- Jared Huffman (CA-02, D) ----------------
    ("jared-huffman", "CA", "Representative", [
        claim("jh1", "jared-huffman", "christian_liberty", 0, False,
              "The only Member of Congress to openly deny belief in God ('I suppose you could say I don't believe in God' — Washington Post, 2017); co-founded the Congressional Freethought Caucus in April 2018 to 'protect the secular character of government' and counter Christian nationalism — actively working to remove religious expression from public life.",
              ["https://en.wikipedia.org/wiki/Jared_Huffman",
               "https://huffman.house.gov/media-center/in-the-news/this-lawmaker-isnt-sure-that-god-exists-now-hes-finally-decided-to-tell-people"]),
        claim("jh2", "jared-huffman", "self_defense", 1, False,
              "Maintains a dedicated 'Gun Violence' policy page on his official House website advocating expanded background checks, assault-weapons legislation, and magazine limits; a consistent supporter of gun-control measures across multiple Congresses — opposing constitutional carry and opposing repeal of existing gun restrictions.",
              ["https://huffman.house.gov/policy-issues/gun-violence",
               "https://ballotpedia.org/Jared_Huffman"]),
    ]),

    # ---------------- Yassamin Ansari (AZ-03, D) ----------------
    ("yassamin-ansari", "AZ", "Representative", [
        claim("ya1", "yassamin-ansari", "sanctity_of_life", 0, False,
              "Introduced the Reproductive Healthcare Leave Act of 2026, which explicitly lists 'pregnancy terminations' as a qualifying procedure for paid leave — facilitating and normalizing abortion access rather than protecting the unborn from conception.",
              ["https://ansari.house.gov/media/press-releases/ansari-introduces-legislative-package-that-finally-recognizes-womens-pain",
               "https://en.wikipedia.org/wiki/Yassamin_Ansari"]),
        claim("ya2", "yassamin-ansari", "biblical_marriage", 2, False,
              "A vocal champion of LGBTQ+ rights including transgender recognition; as Phoenix City Council member and now U.S. Representative, has actively promoted policies affirming gender-identity ideology in law and policy — not rejecting it.",
              ["https://ballotpedia.org/Yassamin_Ansari",
               "https://en.wikipedia.org/wiki/Yassamin_Ansari"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
