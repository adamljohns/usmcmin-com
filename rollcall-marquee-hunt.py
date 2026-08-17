#!/usr/bin/env python3
"""rollcall-marquee-hunt.py — find the bills worth targeting with --bills.

The classifier skips ~90% of swept bills, so blanket sweeps waste LLM time to find the
two bills that matter. This hunts vote-first instead: for a state's session it scans
strong-signal titles, pulls each bill, and reports only those that ALREADY have a large
CONTESTED final roll call — i.e. bills that would actually score a chamber if the
classifier accepts them. Feed the winners to legiscan-rollcall-engine.py --bills.

Usage: rollcall-marquee-hunt.py ST [--prior] [--scan N] [--min-voters N]
"""
import re, sys
sys.path.insert(0, ".")
from legiscan_client import LegiScanClient

STRONG = re.compile(r"abortion|reproduct|heartbeat|firearm|handgun|assault weapon|red flag|carry|"
                    r"transgender|gender|marriage|school choice|voucher|charter|parental right|"
                    r"parents|voter|election|ballot|citizenship|immigra|sanctuary|bail|religio|"
                    r"prayer|obscen|puberty|biological sex|born alive|life", re.I)
FINAL = re.compile(r"third reading|final passage|final action|passage|floor vote|concur|"
                   r"ought to pass|\botpa?\b|second reading|2nd reading", re.I)
ITL = re.compile(r"inexpedient to legislate|\bitl\b", re.I)
TABLE = re.compile(r"\btable\b|\blay on\b", re.I)


def main():
    st = sys.argv[1].upper()
    prior = "--prior" in sys.argv
    scan = int(sys.argv[sys.argv.index("--scan") + 1]) if "--scan" in sys.argv else 60
    minv = int(sys.argv[sys.argv.index("--min-voters") + 1]) if "--min-voters" in sys.argv else 30

    ls = LegiScanClient()
    sess = ls.pull("getSessionList", state=st).get("sessions") or []
    reg = sorted([s for s in sess if not s.get("special")] or sess,
                 key=lambda s: (s.get("year_start") or 0, s.get("session_id")), reverse=True)
    pick = reg[1] if (prior and len(reg) > 1) else reg[0]
    ml = ls.pull("getMasterList", id=pick["session_id"]).get("masterlist") or {}
    bills = [v for v in ml.values() if isinstance(v, dict) and STRONG.search(v.get("title") or "")]
    print(f"{st} session {pick['session_id']} {pick.get('session_name')}"
          f"{' [PRIOR]' if pick is not reg[0] else ''} — {len(bills)} strong-signal, scanning {scan}")

    hits = []
    for b in bills[:scan]:
        try:
            bill = ls.pull("getBill", id=b["bill_id"]).get("bill") or {}
        except Exception:
            continue
        for rc in (bill.get("votes") or []):
            desc = rc.get("desc") or ""
            if TABLE.search(desc) or re.search(r"not\s+concur", desc, re.I):
                continue
            if not (FINAL.search(desc) or ITL.search(desc)):
                continue
            y, n = int(rc.get("yea") or 0), int(rc.get("nay") or 0)
            if y + n < minv:
                continue
            # Surface anything with a real minority; the ENGINE applies the true gate
            # (>=25% losing side OR genuine party divergence, which needs member data).
            if min(y, n) < 6:
                continue
            hits.append((y + n, b.get("number"), (b.get("title") or "")[:70], f"{y}-{n}", desc[:28]))
            break

    hits.sort(reverse=True)
    print(f"\n{len(hits)} bill(s) with a large contested final roll call:")
    for tot, num, title, tally, desc in hits[:12]:
        print(f"  {num:9} {tot:4} voters {tally:>9}  {desc:30} {title}")
    if hits:
        print("\n--bills " + ",".join(h[1] for h in hits[:10]))


if __name__ == "__main__":
    main()
