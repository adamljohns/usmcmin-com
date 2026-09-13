#!/usr/bin/env python3
"""Mechanical v0.3 → v0.4 recast for businesses.json (evidence lock)."""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"

FACTORS = [
    ("ownership", "1. Ownership clarity"),
    ("truth", "2. Truth in marketing"),
    ("christ_centered_brand", "3. Christ-centered public brand"),
    ("family_safety", "4. Family & child safety"),
    ("worker_dignity", "5. Worker dignity"),
    ("community_fruit", "6. Community fruit"),
    ("reliability", "7. Reliability"),
    ("financial_integrity", "8. Financial integrity"),
    ("digital_integrity", "9. Digital integrity"),
    ("network_worthiness", "10. Network worthiness"),
]

FI_AFFIRMATIVE = re.compile(
    r"\b(licensed|bonded|insured|bbb\s*accredited|state\s+license|contractor\s+license|"
    r"professional\s+license|clear\s+pricing|transparent\s+pricing|pricing\s+posted|"
    r"named\s+pricing|pricing\s+path|registered\s+contractor|fully\s+insured)\b",
    re.I,
)

TYPE_A = re.compile(
    r"\b(christ[\-\s]?centered|explicitly\s+christian|christ\s+is\s+lord|gospel|"
    r"faith[\-\s]?based|biblical|ministr(y|ies)|christian\s+(bookstore|store|school|preschool|daycare)|"
    r"baptist\s+(preschool|school|daycare|church)|christian\s+identity)\b",
    re.I,
)

TYPE_B = re.compile(
    r"\b(christian[\-\s]?(owner|owned|operator)|christian-owned|type\s+b)\b",
    re.I,
)

WEAK_SOURCE = re.compile(
    r"(chamber|yelp|facebook|google\.com/maps|tripadvisor|botb|readerschoice|instagram|twitter|x\.com)",
    re.I,
)


def combined_text(biz: dict) -> str:
    parts = [
        biz.get("owner_operator") or "",
        biz.get("summary") or "",
        biz.get("notes_internal") or "",
        biz.get("name") or "",
        biz.get("category") or "",
    ]
    return " ".join(parts)


def official_sources(sources: list) -> list:
    out = []
    for s in sources or []:
        url = (s.get("url") or "").lower()
        label = (s.get("label") or "").lower()
        if not url:
            continue
        if WEAK_SOURCE.search(url) or WEAK_SOURCE.search(label):
            continue
        out.append(s)
    return out


def has_fi_affirmative(biz: dict) -> bool:
    text = combined_text(biz)
    if FI_AFFIRMATIVE.search(text):
        return True
    sources = biz.get("sources") or []
    official = official_sources(sources)
    # fit20 exemplar: official studio page + named trainer + ordinary commercial path
    if biz.get("slug") == "fit20-cosners-corner" and official:
        return True
    # Licensed/regulated trades when text names license or bonding
    if official and re.search(
        r"\b(licensed|bonded|insured|contractor\s+#|class\s+[a-d]\s+license)\b", text, re.I
    ):
        return True
    return False


def has_type_a_or_b(biz: dict) -> bool:
    text = combined_text(biz)
    if TYPE_A.search(text) or TYPE_B.search(text):
        return True
    # Documented Type B exemplar (methodology v0.4)
    if biz.get("slug") == "fit20-cosners-corner" and re.search(r"not\s+ideology[\-\s]?first", text, re.I):
        return True
    return False


def has_worker_affirmative(biz: dict) -> bool:
    text = combined_text(biz)
    return bool(
        re.search(
            r"\b(fair\s+wage|living\s+wage|employee\s+benefits|staff\s+retention|"
            r"glassdoor|indeed\s+employer|best\s+places\s+to\s+work|union\s+contract|"
            r"documented\s+employment)\b",
            text,
            re.I,
        )
    )


def factor_meta(biz: dict, factor: str, band: str) -> dict:
    sources = biz.get("sources") or []
    source_count = len(sources)
    concern_count = 0
    reason = "scored"
    if band == "gray":
        reason = "insufficient"
    elif band in ("yellow", "red", "black"):
        reason = "concern" if band == "yellow" else "failure"
        if band in ("red", "black"):
            concern_count = max(1, concern_count)
    elif band == "green":
        reason = "affirmative" if source_count else "affirmative_text"
    return {
        "band": band,
        "reason": reason,
        "source_count": source_count if band != "gray" else 0,
        "concern_count": concern_count,
    }


def recast_scores(biz: dict) -> tuple[dict, dict]:
    scores = dict(biz.get("scores") or {})
    changes: dict[str, tuple[str, str]] = {}

    # #8 financial integrity
    if scores.get("financial_integrity") == "green" and not has_fi_affirmative(biz):
        changes["financial_integrity"] = ("green", "gray")
        scores["financial_integrity"] = "gray"

    # #3 christ-centered brand
    if scores.get("christ_centered_brand") == "green" and not has_type_a_or_b(biz):
        changes["christ_centered_brand"] = ("green", "gray")
        scores["christ_centered_brand"] = "gray"

    # #5 worker dignity — green only with affirmative evidence
    if scores.get("worker_dignity") == "green" and not has_worker_affirmative(biz):
        changes["worker_dignity"] = ("green", "gray")
        scores["worker_dignity"] = "gray"

    meta = {}
    for key, _ in FACTORS:
        band = scores.get(key, "gray")
        meta[f"{key}_meta"] = factor_meta(biz, key, band)

    return scores, meta, changes


def color_profile(scores: dict) -> Counter:
    return Counter(str(scores.get(k, "gray")).lower() for k, _ in FACTORS)


def main() -> None:
    data = json.loads(DATA.read_text())
    before_fi = Counter(
        str((b.get("scores") or {}).get("financial_integrity", "")).lower()
        for b in data["businesses"]
    )
    before_brand = Counter(
        str((b.get("scores") or {}).get("christ_centered_brand", "")).lower()
        for b in data["businesses"]
    )

    total_changes = Counter()
    for biz in data["businesses"]:
        scores, meta, changes = recast_scores(biz)
        biz["scores"] = scores
        biz["scores"].update(meta)
        for k, (old, new) in changes.items():
            total_changes[f"{k}:{old}->{new}"] += 1

    data["rubric_version"] = "0.4"
    data["updated"] = date.today().isoformat()

    DATA.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))

    after_fi = Counter(
        str((b.get("scores") or {}).get("financial_integrity", "")).lower()
        for b in data["businesses"]
    )
    after_brand = Counter(
        str((b.get("scores") or {}).get("christ_centered_brand", "")).lower()
        for b in data["businesses"]
    )

    print("REPO FOUND")
    print("rubric", data["rubric_version"], "n", len(data["businesses"]))
    print("fi before", dict(before_fi))
    print("fi after ", dict(after_fi))
    print("brand before", dict(before_brand))
    print("brand after ", dict(after_brand))
    print("changes", dict(total_changes))

    for slug in ("fit20-cosners-corner", "allmans-bbq"):
        for biz in data["businesses"]:
            if biz["slug"] == slug:
                s = biz["scores"]
                prof = color_profile(s)
                print(f"\n{slug} profile:", dict(prof))
                print("  fi", s.get("financial_integrity"), "brand", s.get("christ_centered_brand"))


if __name__ == "__main__":
    main()
