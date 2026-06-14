# Fleet Command Center — how it stays current

The dashboard at `usmcmin.com/fleet/` is generated from live fleet state and an
accomplishments archive. Three loops keep it fresh — **none of them message Adam.**

## 1. Live status (every 30 min)
`com.moop.fleet-dashboard` → `~/Scripts/fleet-dashboard-refresh.sh` rebuilds the
pages from OpenClaw cron state + Hermes and pushes **only when the meaningful
state changes** (a job errors/recovers, a new win) — so the repo doesn't churn.

## 2. Auto-logged wins (daily, deterministic — no LLM, no hallucination)
`com.moop.fleet-activity-logger` (22:00) → `~/Scripts/fleet-activity-logger.py`
reads real activity from the last 24h and logs one factual win per agent:
- **git commits** in usmcmin-com / bible-reading-plan-bot / resolute-local
  (noise-filtered, aggregated) → the committing agents (chaps, sheriff-roy…)
- **cron output files** (ok + fresh today) → the non-git agents:
  Coach/Doc ← Garmin vitals, Sally ← Airbnb rounds, Rush ← news brief,
  Pops ← inbox sweep, Prof X ← newsletter, Carnegie ← consistency check.

## 3. Log a win by hand (you or any agent)
```bash
python3 ~/Scripts/fleet-log-win.py <agent-id> "Short title" "One-line detail"
# e.g.
python3 ~/Scripts/fleet-log-win.py carnegie "Caught a 4% metals drift" "Flagged in the AM cache before the daily post."
```
- Valid agent ids: main, hermes, preacher-john, chaps, carnegie, sally,
  coach-arnie, doc, sheriff-roy, prof-x, rush, pops, sgt-maj-mac, bg-hartwell.
- Idempotent (same title updates in place), keeps the 15 newest per agent.
- Agents call it the same way via their `exec` tool — the win lands on the
  board within 30 minutes, no Telegram to Adam.

Data file: `~/Scripts/fleet-accomplishments.json` (agent-id → list of `{date,title,detail}`).
