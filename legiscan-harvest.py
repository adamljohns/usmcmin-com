#!/usr/bin/env python3
"""14-day LegiScan Public API harvest for the RESOLUTE Citizen grind.

Prefetches people_id + sponsorship payloads into ~/.openclaw/cache/legiscan/ and
banks profile.records_website (+ profile.legiscan_people_id) on state legislators
so local-politician-extract.py can score from API text before the free key expires.

Does NOT score cells. Scoring still goes through the verbatim + Gemma gates.

Usage:
  LEGISCAN_MONTHLY_BUDGET=28000 python3 legiscan-harvest.py [--dry] [--limit N] [--states VA,MD]
  python3 legiscan-harvest.py --status          # spend + cache inventory
  python3 legiscan-harvest.py --write-scorecard # persist banked URLs/ids into scorecard.json
"""
from __future__ import annotations

import argparse, json, os, sys, time
from pathlib import Path

from legiscan_client import LegiScanClient, LegiScanBudgetExceeded, LegiScanError

ROOT = Path(__file__).resolve().parent
SCORECARD = ROOT / "data" / "scorecard.json"
INDEX = Path(os.path.expanduser("~/.openclaw/cache/legiscan/harvest-index.json"))


def load_scorecard():
    return json.loads(SCORECARD.read_text())


def state_legislators(data, states=None):
    want = {s.upper() for s in states} if states else None
    out = []
    for c in data.get("candidates") or []:
        if c.get("level") != "state":
            continue
        st = (c.get("state") or "").upper()
        if want and st not in want:
            continue
        out.append(c)
    return out


def needs_work(c):
    """Prioritize unscored / thin-evidence legislators."""
    prof = c.get("profile") or {}
    conf = str(prof.get("confidence") or "")
    if conf.startswith("evidence_"):
        return False  # already evidence-scored — skip for sprint headroom
    return True


def save_index(idx):
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(json.dumps(idx, indent=1) + "\n")


def load_index():
    if INDEX.exists():
        try:
            return json.loads(INDEX.read_text())
        except Exception:
            pass
    return {"people": {}, "updated": None}


def cmd_status(client):
    idx = load_index()
    print(f"queries_this_month: {client.queries_this_month}/{client.monthly_budget}")
    print(f"harvest_index_people: {len(idx.get('people') or {})}")
    cache = client.cache_dir
    n = len(list(cache.glob("*.json"))) if cache.exists() else 0
    print(f"cache_files: {n} under {cache}")
    print(f"key_expires_note: renew/cancel decision by 2026-08-28 (status page)")


def harvest(client, *, dry=False, limit=0, states=None, write_scorecard=False):
    data = load_scorecard()
    cands = [c for c in state_legislators(data, states) if needs_work(c)]
    # impact order: already-banked records_website first (cheap resolve), then others
    cands.sort(key=lambda c: (0 if (c.get("profile") or {}).get("records_website") else 1,
                              c.get("state") or "", c.get("name") or ""))
    if limit:
        cands = cands[:limit]

    idx = load_index()
    people = idx.setdefault("people", {})
    resolved = prefetched = banked = skipped = errors = 0
    mutated = False

    print(f"harvest pool: {len(cands)} unscored state legislators"
          + (f" states={states}" if states else "")
          + (" DRY" if dry else ""))

    for i, c in enumerate(cands, 1):
        slug = c.get("slug")
        name = c.get("name") or ""
        st = (c.get("state") or "").upper()
        key = f"{slug}@{st}"
        prof = c.setdefault("profile", {})
        url = prof.get("records_website")
        pid = prof.get("legiscan_people_id") or (people.get(key) or {}).get("people_id")

        try:
            if not pid:
                if dry:
                    print(f"  [{i}/{len(cands)}] DRY resolve {key}")
                    skipped += 1
                    continue
                meta = client.parse_people_url(url) if url else None
                pid = client.resolve_people_id(
                    st, name,
                    people_id=(meta or {}).get("people_id"),
                    slug=(meta or {}).get("slug"),
                )
                if not pid:
                    print(f"  [{i}/{len(cands)}] MISS {key}")
                    errors += 1
                    continue
                resolved += 1
                people[key] = {
                    "people_id": pid, "name": name, "state": st, "slug": slug,
                    "resolved": time.strftime("%Y-%m-%dT%H:%M:%S"),
                }
                if not url:
                    url = f"https://legiscan.com/{st}/people/{slug}/id/{pid}"
                    prof["records_website"] = url
                    banked += 1
                    mutated = True
                elif "/id/" not in url:
                    prof["records_website"] = f"https://legiscan.com/{st}/people/{(meta or {}).get('slug') or slug}/id/{pid}"
                    mutated = True
                if prof.get("legiscan_people_id") != pid:
                    prof["legiscan_people_id"] = pid
                    mutated = True

            # Prefetch sponsorships into cache (extractor will reuse)
            if not dry:
                # warm sponsorships + recent session master lists (cache makes repeats free)
                body = client.sponsored_list(pid)
                for sess in (body.get("sessions") or [])[:2]:
                    try:
                        client.master_list(sess["session_id"])
                    except LegiScanError as e:
                        print(f"  warn master {sess.get('session_id')}: {e}")
                prefetched += 1
                people[key] = {
                    **(people.get(key) or {}),
                    "people_id": pid, "name": name, "state": st, "slug": slug,
                    "prefetched": time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "records_website": prof.get("records_website"),
                }
            print(f"  [{i}/{len(cands)}] OK {key} people_id={pid} q={client.queries_this_month}")
        except LegiScanBudgetExceeded as e:
            print(f"BUDGET STOP at {key}: {e}")
            break
        except LegiScanError as e:
            print(f"  [{i}/{len(cands)}] ERR {key}: {e}")
            errors += 1

        if i % 25 == 0:
            idx["updated"] = time.strftime("%Y-%m-%dT%H:%M:%S")
            save_index(idx)

    idx["updated"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    save_index(idx)

    if write_scorecard and mutated and not dry:
        # atomic-ish write
        tmp = SCORECARD.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n")
        tmp.replace(SCORECARD)
        print(f"wrote scorecard.json (+records_website / legiscan_people_id banks)")
        print("NEXT: python3 build-data.py && python3 generate-profiles.py  (or let grind round do it)")

    print(f"done: resolved={resolved} prefetched={prefetched} banked_urls={banked} "
          f"errors={errors} queries={client.queries_this_month}/{client.monthly_budget}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--states", default="", help="Comma list, e.g. VA,MD,TX")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--write-scorecard", action="store_true",
                    help="Persist records_website + legiscan_people_id into data/scorecard.json")
    args = ap.parse_args()

    # Sprint default: burn up to Public tier minus a 2k safety cushion
    os.environ.setdefault("LEGISCAN_MONTHLY_BUDGET", "28000")
    client = LegiScanClient()

    if args.status:
        cmd_status(client)
        return

    states = [s.strip().upper() for s in args.states.split(",") if s.strip()] or None
    harvest(client, dry=args.dry, limit=args.limit, states=states,
            write_scorecard=args.write_scorecard)


if __name__ == "__main__":
    main()
