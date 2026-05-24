# RESOLUTE Citizen + Local — User Guide

A walkthrough of both tools the U.S.M.C. Ministries citizen-engagement stack
provides, for everyone who uses them — and for the maintainer (Adam) keeping
them current.

> **Two tools, one engine.** Both run on the same scrape → structured data →
> local-LLM brief → static-page-on-GitHub-Pages pipeline. Different domain,
> different audience.

| Tool | Where it lives | What it does |
|---|---|---|
| **RESOLUTE Citizen** | <https://usmcmin.com/citizen.html> | The candidate scorecard — 8,972 federal/state/local candidates scored on a tier-aware biblical rubric (60/40 federal · 70/30 state · 70/30 local) |
| **RESOLUTE Local** | <https://adamljohns.github.io/resolute-local/> | Live city-council civic-engagement tool — agendas, plain-English LLM briefs, calendar, draft-a-comment helper; currently Fredericksburg |

---

## Part 1 — For citizens (using the tools)

### A. Citizen Scorecard at usmcmin.com/citizen.html

**The 30-second tour:**
1. Open <https://usmcmin.com/citizen.html>. You'll see candidates as cards
   with a score (e.g., *Tim Kaine · 18/100 · F*) and a tier chip (*Federal
   rubric · 60/40*).
2. Search a name in the top filter, or filter by state, party, status, or
   rubric tier.
3. Click any card → full profile with the 13 categories, every scored
   question, primary-source citations, and a deep-dive link to each category's
   full rubric.
4. Top nav has a **Citizen ▾** dropdown exposing every supporting page
   (Find My Reps, Rankings, Compare, Scoring System, Council Watch, +
   cross-link to RESOLUTE Local).

**Common tasks:**

| I want to… | Go to | How |
|---|---|---|
| Look up a specific candidate | citizen.html | Type their name in the search box |
| See your federal + state reps | find-my-reps.html | Enter your address — pulls your House district + state legislators |
| Compare two candidates head-to-head | compare.html | Pick a race or two candidates, see scores side-by-side |
| Browse top-scoring candidates by state | citizen-rankings.html | Filter by state, party, office |
| See who's been voted out / retired | citizen-formers.html | Shows resolved candidacies (lost / retired / former) |
| Understand the rubric | scoring-system.html | Full explainer: 60/40 federal split, 70/30 state/local, what each tier weights |
| Read a category's full rubric | citizen/&lt;slug&gt;.html | E.g., citizen/sanctity-of-life.html — anchor Scripture, all 5 questions per tier, disqualifiers, key bills + orgs scored |
| Watch state ballot issues | citizen-issues.html | Track state-level constitutional amendments + ballot initiatives |
| Send a petition to your reps | petition.html | Pre-fills a template you edit + copy-to-email |
| Dispute a claim on a profile | Click *Dispute this claim* under any answered question | Opens email with the source line auto-quoted |

**Reading a profile (anatomy):**
- **Score header**: total /100 (e.g., 64/100 — B), plus God-First subtotal
  and Government-pillar subtotal (the latter changes per tier:
  *America First* for federal, *State First* for state, *Local First* for local).
- **Tier chip** under the score tells you which rubric is in play
  (e.g., *Local rubric · 70/30*).
- **Category cards**: 13 total, but only the ones applicable to this office's
  tier render. Each shows the score (e.g., 6/10), an icon, and a "deep dive →"
  link to the category page.
- **Per-question rows**: True/False/null. *True* = +2 points; *null* = "not
  yet verified from primary sources" (neither penalized nor credited).
- **Evidence drawer** (the small *i* button): expands the source citations for
  any answered question — typically AP / NBC / state SoS / official records.
- **"📍 Track this council live"** banner appears on Fredericksburg city
  officials' profiles → jumps to the civic tool for that city.

**Tier-aware labels (v5.6, May 2026):**
The same canonical category looks different depending on the office:
- A U.S. senator's *Sanctity of Life* category focuses on federal abortion
  law, SCOTUS confirmations, Hyde Amendment.
- A state senator's renders as **Sanctity of Life — State abortion law &
  funding** (state code, Medicaid, parental consent, clinic regulation).
- A mayor or DA's renders as **Sanctity of Life — Protect the Vulnerable**
  (DA priorities, no PP zoning, crisis-pregnancy support).

Same Scripture, same conviction; what changes is the chair making the call
and what evidence the rubric scores against.

---

### B. RESOLUTE Local at adamljohns.github.io/resolute-local

**Currently:** Fredericksburg, VA. Pattern generalizes to any Commonwealth
locality (see ADDING-CITIES.md). Expanding by request.

**The 30-second tour:**
1. Open <https://adamljohns.github.io/resolute-local/>. You'll see the city
   directory — Fredericksburg today, *Request your city* card for the rest.
2. Click *Open Fredericksburg* → live council page with: next meeting (date,
   time, agenda link, plain-English LLM brief), current council members with
   ward / contact, active issues this cycle, how-to-participate ladder
   (watch → email → public-comment), and a "Draft your public comment"
   tool.
3. Click *Add to my calendar* on the next meeting → downloads a `.ics` file
   you import to Apple/Google/Outlook calendar.
4. Click *Draft a public comment* → opens an editable template; click
   *Copy to clipboard*, paste into email or read at the podium.
5. Top nav links over to the **Scorecard ↗** (the same council members'
   scorecard pages on usmcmin.com) and the **Council Notes** page (past
   meetings, votes, policy analysis).

**Common tasks:**

| I want to… | How |
|---|---|
| Know what's on the next council meeting | Top section of the city page — date, agenda link, LLM brief |
| Calendar the next meeting | "📅 Add to my calendar" → opens `.ics` |
| Email a councilor | Click their name → opens email with city directory link |
| Read what just happened | Top nav → Council Notes |
| Draft a public comment to read at the podium | "✍️ Draft a public comment" → edits a template, copies to clipboard |
| Request RESOLUTE Local for my city | Council Notes page → bottom form |

The data refreshes **twice daily** (06:00 + 18:00 EDT) — a cron pulls the
official agenda center, transforms the snapshot into `data/<city>.json`, has
a local LLM (Qwen 3.6) write the citizen brief, and pushes any changes back
to GitHub for live deploy. You always see the latest published agenda + the
freshest brief without us touching anything.

---

## Part 2 — For Adam (maintenance)

This section is the **front door** to maintaining both tools. It's a
high-level map; the deep specifics live in the per-topic docs.

### Daily / weekly rhythm

| When | What | Where |
|---|---|---|
| **Every 12 h** (06/18 EDT) | FXBG agenda scrape → `data/fredericksburg.json` → push | `com.moop.fxbg-civic-rounds` (launchd) → `~/Scripts/resolute-local-publish.sh` |
| **Election nights** (Tue, Mar–Nov) | Web-verify result → update candidacy_status → cite source → rebuild + push | See **MAINTENANCE.md §3** ("Resolved-results pattern") |
| **Mondays 08:00** | Weekly election-sweep digest to Telegram (which races need attention) | `com.moop.scorecard-sweep` → `~/Scripts/scorecard-sweep-rounds.sh` |
| **Monthly** | Foreign-influence refresh (AIPAC / Soros / CCP donor data) | `apply-foreign-lobby-to-category.py` then rebuild |

### When you add a candidate

Read **CONTRIBUTING-PER-STATE.md** for the full pattern; the short version:
1. Edit `data/scorecard.json` (NEVER auto-format — keep `indent=2`, append to
   `candidates[]`, mind the schema in DATABASE-LAYOUT.md).
2. Run the build chain: `build-data.py → build-search-index.py →
   generate-profiles.py → build-category-pages.py → build-sitemap-xml.py`.
3. Verify the new profile renders correctly (tier, score, sources).
4. Commit. Push.

### When an election result lands

The **Cardinal Rule**: web-verify every result before publishing it. Model
recall is NOT sufficient for results inside the last ~12 months. AP / NBC /
CNN / state SoS live results — cite the source in the record's `sources[]`
before changing `candidacy_status` to `won` / `lost` / `lost_primary` /
`general_candidate`. See **MAINTENANCE.md §3** for the full procedure (and
the Harrell-vs-Massie case study explaining why this rule exists).

### When you add a city to RESOLUTE Local

See **resolute-local/ADDING-CITIES.md**. Short form: clone the FXBG scraper +
publisher + page, point at the new city's AgendaCenter / Legistar URL, add
a card to the resolute-local index, wire the publish wrapper. Two adapters
(CivicPlus/Granicus + Legistar) cover most of Virginia.

### When the rubric changes (rare)

See **v5-rubric-draft.md** for the full three-tier design and the per-tier
question scaffolding. The v5.6 per-tier labels live in `data/scorecard.json`
under each category as `label_state`, `label_local`, `description_state`,
`description_local`. Adding a new tier-specific framing = edit those fields,
re-run `build-category-pages.py` + `generate-profiles.py`. No re-score
needed — display layer only.

### Common fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Local profile shows federal-tier label ("Sanctity of Life" without subtitle) | Office text contains "U.S. Senator" → classifier returned `federal` | Remove the federal-flavored phrase from `office` field; rebuild |
| Brief on FXBG city page is stale | Local LLM down at scrape time | Restart `llama-server` on :1235; next cron pass picks up |
| Council member missing from FXBG page | Not yet added to `data/fredericksburg.json` (auto-published) | Add to canonical roster in `publish-fredericksburg.py`; re-run wrapper |
| Mobile hamburger nav doesn't open | `assets/js/main.js` not loaded on this page | Check `<script src="assets/js/main.js" defer></script>` near `</body>` |
| Site-wide nav drift returns | A new HTML page bypassed the unifier | Run `python3 unify-nav.py` (idempotent) |

### Build pipeline (in order)

```
data/scorecard.json     ← canonical data
   ↓
build-data.py           ← validate + derive computed fields
build-search-index.py   ← write data/search-index.json (home-page cards)
generate-profiles.py    ← write candidates/<state>/<slug>.html × 8,972
build-category-pages.py ← write citizen/<slug>.html × 13
build-sitemap-xml.py    ← write sitemap.xml
```

Every step is idempotent. Run `MAINTENANCE.md §6 "Full rebuild"` after any
rubric / scoring change.

### Key docs

| File | Purpose |
|---|---|
| `MAINTENANCE.md` | Maintenance playbook — daily/weekly procedures, cardinal rules, dual-record + dedup patterns |
| `DATABASE-LAYOUT.md` | scorecard.json schema reference — every field, every status value |
| `CONTRIBUTING-PER-STATE.md` | How to add a candidate, with the per-state template |
| `v5-rubric-draft.md` | The three-tier rubric design + per-tier question scaffolding |
| `KNOWN-STALE-RECORDS.md` | Records that need verification on next pass |
| `unify-nav.py` | Idempotent nav unifier (re-run after adding a new top-level HTML page) |
| `resolute-local/ADDING-CITIES.md` | How to stand up RESOLUTE Local for a new municipality |
| `bow-business-tools/FRAMING.md` | Design framing for the not-yet-built Bow & Arrow business tools |

### Cron schedule

```bash
launchctl list | grep com.moop
# com.moop.fxbg-civic-rounds   ← 06/18 EDT, FXBG scrape + publish
# com.moop.scorecard-sweep     ← Mon 08:00, weekly election digest
# com.moop.news-rss-rounds     ← every 2h 7-21, Intel Desk feed
```

All scripts log to `~/.openclaw/logs/` and notify via
`~/.hermes/bin/notify-adam.sh --level info|warning|urgent|report` when
something needs your attention.

---

## Part 3 — For everyone (how the project hangs together)

**The methodology** (one engine, three uses):

```
public source(s)  →  cron scraper  →  structured JSON  →  local-LLM brief  →  static web tool
   (gov agendas,     (per-domain      (committed to       (Qwen :1235          (GitHub Pages)
    election data,    cron)            the repo)           where needed)
    PAC filings)
```

- **RESOLUTE Citizen** = this engine pointed at candidate data → scorecard.
- **RESOLUTE Local** = same engine pointed at city agendas → civic tool.
- **(Designed)** **Bow & Arrow business tools** = same engine pointed at
  commercial listings + Christian-business directories → real-estate +
  partnership finder (see `bow-business-tools/FRAMING.md`).

**The conviction** (the *why*):
> "When the righteous are in authority, the people rejoice; but when the
> wicked beareth rule, the people mourn." — **Proverbs 29:2**

Faithful citizens who know what their officials actually do — at every
tier of government — can vote, petition, comment, and run accordingly. This
toolkit lowers the friction to make that engagement possible in ten
minutes a month rather than ten hours.

---

*Last updated: 2026-05-23 · maintained by Adam Johns ·
[usmcministries2022@gmail.com](mailto:usmcministries2022@gmail.com)*
