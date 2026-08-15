# LegiScan 14-Day Sprint (2026-08-14 → 2026-08-28)

Public API key issued **2026-08-14**, status page shows **Expires 2026-08-28**.
Public tier = **30,000 queries / month**, free. Soft client budget = **28,000**
(2k cushion). Goal: bank every reachable state-legislator sponsorship record so
the local grind can evidence-score the ~2/3 with no campaign site.

## Billing / cancel (read this)

- **Public API is free.** The expiry is a **key window**, not an automatic paid
  conversion we have observed. Still: on **2026-08-28** (or sooner if LegiScan
  emails a paid upsell), open [legiscan.com/legiscan](https://legiscan.com/legiscan)
  → API Status / account and **do not start a paid Pull/Push plan** unless Adam
  explicitly approves donations-funded spend.
- Options after expiry:
  1. **Renew free Public key** (preferred while audience is small).
  2. **Stay dark** and keep using the on-disk cache under
     `~/.openclaw/cache/legiscan/` (no new pulls).
  3. Later: paid Pull API if donations cover it — Principal GO only.

## Query budget (30k)

| Phase | What | Est. queries | Days |
|------:|------|-------------:|-----:|
| A | `getSessionList` + `getSessionPeople` for 50 states (cache 7d) | ~150 | 1 |
| B | Resolve + `getSponsoredList` for unscored state legislators (~5k) | ~5,000–6,000 | 1–7 |
| C | `getMasterList` for sessions touched (titles for join) | ~200–400 | overlapping |
| D | Headroom for `getBill` / `getRollCall` on rubric bills only | ~15,000–20,000 | 7–14 |
| — | **Soft stop** | **28,000** | — |

Daily burn target if smooth: ~2,000/day. Check spend:

```bash
LEGISCAN_MONTHLY_BUDGET=28000 python3 legiscan-harvest.py --status
# or
python3 -c 'import json;print(json.load(open("/Users/moop_bot_pro/.openclaw/cache/legiscan/spend.json")))'
```

## Commands (exec owners: Max / Hermes / Claude Code)

```bash
cd ~/.openclaw/workspace/usmcmin-com

# Day 1 — VA/MD proof (limit)
LEGISCAN_MONTHLY_BUDGET=28000 python3 legiscan-harvest.py --states VA,MD --limit 100 --write-scorecard
python3 build-data.py && python3 generate-profiles.py

# Days 2–7 — nationwide unscored state legislators
LEGISCAN_MONTHLY_BUDGET=28000 python3 legiscan-harvest.py --write-scorecard

# Grind consumes the banked records_website via legiscan_client automatically
SCORECARD_REFINE_BATCH=25 bash ~/.openclaw/bin/scorecard-refine-local.sh
```

## What agents may do

| Agent | May pull LegiScan? | May update scorecard? |
|-------|--------------------|------------------------|
| **Max** | Yes (harvest + grind) | Yes via grind / commit helpers |
| **Sheriff Roy** | Yes (lookup + QA cite) | **Propose only** via `resolute-qa` / `legiscan-resolute` — never hand-edit JSON |
| **Rush** | Yes (cite sponsorships/votes in briefs) | Propose only; no direct JSON edit |
| **Chaps** | Yes (read for pastoral/civic context) | **No scoring mutations** — route scorecard writes to Max/Roy |

Hard law unchanged: party ≠ evidence; verbatim quote required; wrong cell on a
named official is potential libel.

## Success criteria by 2026-08-28

1. Soft budget spent on **useful** cache (people + sponsorships + master lists), not burns.
2. `profile.legiscan_people_id` + `records_website` banked for as many unscored state legislators as resolve.
3. Local grind converting LegiScan text into cited TRUE/FALSE cells (Hinebaugh smoke: 4 cells).
4. Principal decision logged: renew free key **or** pause pulls **or** paid plan.
