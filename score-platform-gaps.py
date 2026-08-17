#!/usr/bin/env python3
"""
score-platform-gaps.py — Tier-3 party-platform scoring for null rubric cells.

Principal lock 2026-08-17: score from official party platform when no individual
or affiliated-source evidence exists. Annotates cells with kind=party_platform.

Reads mappings from data/party-platforms.json. Only fills NULL cells on active
candidates registered with matching party who are not yet evidence-scored.

Usage:
  python3 score-platform-gaps.py --dry-run
  python3 score-platform-gaps.py --apply [--limit N] [--state XX]
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

REPO = Path(__file__).parent
SCORECARD = REPO / "data" / "scorecard.json"
PLATFORMS = REPO / "data" / "party-platforms.json"

TIER_KEYS = {"federal": "federal", "state": "state", "local": "local"}
CONF_EVIDENCE = ("evidence_federal", "evidence_state", "evidence_local", "evidence")


def load_platform_maps() -> dict[str, dict]:
    """party -> platform dict with cells + _meta."""
    data = json.loads(PLATFORMS.read_text())
    out: dict[str, dict] = {}
    for plat in data.get("platforms", []):
        party = plat.get("party")
        if not party:
            continue
        out[party] = plat
    return out


def candidate_tier(c: dict) -> str:
    return c.get("level") or "federal"


def is_evidence_scored(c: dict) -> bool:
    conf = ((c.get("profile") or {}).get("confidence") or "")
    return any(conf.startswith(p) for p in CONF_EVIDENCE)


def applicable_categories(sc: dict, tier: str) -> dict[str, list]:
    qkey = {"federal": "questions", "state": "questions_state", "local": "questions_local"}.get(
        tier, "questions"
    )
    cats = {}
    for cat in sc.get("categories", []):
        qs = cat.get(qkey) or cat.get("questions") or []
        appl = cat.get("applicable_at") or []
        applicable = []
        for qi, _ in enumerate(qs):
            tiers = appl[qi] if qi < len(appl) else []
            if tier in tiers:
                applicable.append(qi)
        if applicable:
            cats[cat["id"]] = applicable
    return cats


def build_dossier(sc: dict, limit: int | None, state_filter: str | None) -> dict:
    platforms = load_platform_maps()
    today = date.today().isoformat()
    records = {}
    touched = 0

    for c in sc.get("candidates", []):
        if (c.get("status") or "active") in ("lost", "former", "deceased", "withdrew", "not_running"):
            continue
        if is_evidence_scored(c):
            continue
        party = (c.get("party") or "").upper()
        if party not in platforms:
            continue
        st = (c.get("state") or "").upper()
        if state_filter and st != state_filter.upper():
            continue
        tier = candidate_tier(c)
        plat = platforms[party]
        tier_map = (plat.get("cells") or {}).get(tier) or (plat.get("cells") or {}).get("all") or {}
        if not tier_map:
            continue

        plat_meta = plat.get("_meta") or plat

        scores = c.get("scores") or {}
        appl = applicable_categories(sc, tier)
        evidence: dict[str, dict] = {}
        cells_set = 0

        for cat_id, q_indices in appl.items():
            cat_cells = tier_map.get(cat_id) or {}
            cur = scores.get(cat_id) or []
            for qi in q_indices:
                cur_val = cur[qi] if qi < len(cur) else None
                if cur_val is not None:
                    continue
                plat_val = cat_cells.get(str(qi))
                if plat_val is None:
                    continue
                url = plat_meta.get("url") or plat_meta.get("official_url") or ""
                note = (
                    f"Scored from the {plat_meta.get('name', party + ' platform')} "
                    f"({cat_id} q{qi}) — no individual statement found."
                )
                evidence.setdefault(cat_id, {})[str(qi)] = {
                    "v": bool(plat_val),
                    "src": [url] if url else [],
                    "note": note,
                    "kind": "party_platform",
                }
                cells_set += 1

        if not cells_set:
            continue
        slug = c["slug"]
        key = f"{slug}@{st}" if st else slug
        records[key] = {
            "profile": {
                "confidence": f"party_platform_{tier}",
                "confidence_note": f"Tier-3 party platform fill {today}; policy docs/scorecard-evidence-policy-2026-08-16.md",
                "last_refined": today,
            },
            "evidence": evidence,
            "notes_append": f"[{today} platform pass] {cells_set} cell(s) from official party platform (annotated).",
        }
        touched += 1
        if limit and touched >= limit:
            break

    return {
        "_meta": {
            "author": "score-platform-gaps",
            "date": today,
            "note": f"Tier-3 party platform gap fill — {touched} record(s)",
        },
        "reset_unspecified": False,
        "records": records,
    }


def main():
    dry = "--dry-run" in sys.argv
    apply = "--apply" in sys.argv
    if not dry and not apply:
        print("usage: score-platform-gaps.py --dry-run | --apply [--limit N] [--state XX]")
        raise SystemExit(1)

    limit = None
    state_filter = None
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1])
        if a == "--state" and i + 1 < len(args):
            state_filter = args[i + 1]

    sc = json.loads(SCORECARD.read_text())
    dossier = build_dossier(sc, limit, state_filter)
    n = len(dossier["records"])
    cells = sum(len(r.get("evidence", {})) for r in dossier["records"].values())
    print(f"platform gap fill: {n} record(s), ~{cells} categories touched")

    if dry:
        for key, rec in list(dossier["records"].items())[:10]:
            ev_count = sum(len(v) for v in rec.get("evidence", {}).values())
            print(f"  {key}: {ev_count} cells")
        if n > 10:
            print(f"  ... and {n - 10} more")
        return

    if n == 0:
        print("nothing to apply")
        return

    out = REPO / "refinements" / f"platform-gaps-{date.today().isoformat()}.json"
    out.write_text(json.dumps(dossier, indent=2), encoding="utf-8")
    print(f"wrote {out}")
    subprocess.run([sys.executable, str(REPO / "refine-records.py"), str(out)], cwd=REPO, check=True)


if __name__ == "__main__":
    main()
