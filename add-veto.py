#!/usr/bin/env python3
"""add-veto.py — CONCURRENCY-SAFE writer for rollcall-vetoes.json.

WHY THIS EXISTS: the veto list is a shared file that Claude Code, Sheriff Roy and the
grind crons all append to. Everyone was doing read -> mutate -> json.dump, which is
last-writer-wins: on 2026-08-26 a concurrent rewrite silently erased two vetoes added
minutes earlier (IA:HF785, AK:HB61), and a vetoed bill immediately resurfaced in a
replay. A veto list that can lose entries is worse than none — it gives false
confidence that a rejected mapping can't come back.

This does read -> MERGE -> atomic replace under an exclusive lock, so concurrent writers
combine instead of clobbering. Existing reasons are never overwritten by a re-add.

Usage:
  add-veto.py ST:BILL "reason"  [ST:BILL "reason" ...]
  add-veto.py --list
"""
import fcntl, json, os, sys, tempfile

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rollcall-vetoes.json")


def load_locked(fh):
    fh.seek(0)
    raw = fh.read().strip()
    return json.loads(raw) if raw else {"_note": "", "vetoed": {}}


def main():
    args = sys.argv[1:]
    if not args or args[0] == "--list":
        d = json.load(open(PATH))
        v = d.get("vetoed") or {}
        print(f"{len(v)} vetoed bill(s)")
        for k in sorted(v):
            print(f"  {k}: {v[k][:100]}")
        return 0
    if len(args) % 2:
        sys.exit('usage: add-veto.py ST:BILL "reason" [ST:BILL "reason" ...]')
    pairs = list(zip(args[0::2], args[1::2]))

    # exclusive lock for the whole read-modify-write
    with open(PATH, "r+", encoding="utf-8") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            d = load_locked(fh)
            v = d.setdefault("vetoed", {})
            added, kept = [], []
            for key, reason in pairs:
                key = key.strip().upper()
                if key in v:
                    kept.append(key)          # never overwrite an existing rationale
                else:
                    v[key] = reason
                    added.append(key)
            tmp = tempfile.NamedTemporaryFile("w", delete=False, dir=os.path.dirname(PATH),
                                              encoding="utf-8")
            json.dump(d, tmp, indent=1, ensure_ascii=False)
            tmp.write("\n"); tmp.flush(); os.fsync(tmp.fileno()); tmp.close()
            os.replace(tmp.name, PATH)        # atomic
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)
    print(f"vetoes now {len(v)} — added {len(added)} {added or ''}"
          + (f", already present {kept}" if kept else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
