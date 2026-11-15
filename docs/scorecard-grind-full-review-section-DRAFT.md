# DRAFT section for ~/.openclaw/shared-memory/context/scorecard-grind.md

*Drafted 2026-11-09 by Claude Code (branch `feat/scorecard-full-review`). Max applies it; this file is not the live doc.*

---

## Full review mode (`--full-review`) — every politician, every cell, local models

**What it is.** The hourly grind fills blank cells. The full review re-reads a politician end to end:
roster truth (still in office? party, district, term dates), every rubric cell (re-check stored answers,
fill blanks), contact fields, and the citations already on the record. Principal order: Adam, Max TG 8996,
2026-11-08. Same standard as the church full review. Ticket:
`~/.openclaw/workspace/scorecard-full-review-strike-ticket-2026-11-09.md`.

**Code:** `usmcmin-com/scripts/full-review/` — `select_batch.py` (order), `fetch.py` (pages + local models),
`build_patch.py` (deterministic gates, patch, HOLD queue, public counts), `apply.py` (not run live
without Adam's go), `round.sh` (orchestrator), `test_full_review.py` (gate tests).

**Run a round (dry run, the only mode until Adam's go):**

    cd <usmcmin-com checkout on the feat/scorecard-full-review branch>
    bash scripts/full-review/round.sh                      # new round, batch 25 (max 60: FULL_REVIEW_BATCH=60)
    bash scripts/full-review/round.sh --resume <round-id>  # finish a round that paused at the grind yield point

Log: `~/Library/Logs/scorecard-full-review.log`. Output (NOT in the repo, never deployed):
`~/.openclaw/state/scorecard-full-review/rounds/<round-id>/{review-patch.json,hold.json,obs/,pages/}`,
plus `hold-queue.json` (latest round per politician) and `ledger.json` (rotation). Public counts only:
`data/full-review-stats.json`, shown on `usmcmin.com/stats.html` under "Full review".

**Selection order:** (a) Fredericksburg + Virginia (Fredericksburg leads every cycle, then VA federal /
state / local in rotation); (b) sitting federal delegation, then 2026 race records; (c) records with fewer
than 3 cited cells or no headline letter; (d) the rest. Never-reviewed first, then oldest. Default quota for
25: a=10, b=8, c=5, d=2; unused share falls through (`FULL_REVIEW_QUOTA=a:12,b:8,c:3,d:2`).

**Shares the grind lock.** `round.sh` takes `/tmp/scorecard-refine-local.lock` (the grind's own mkdir lock;
owner noted in `/tmp/scorecard-refine-local.lock.owner`). It waits for a running grind round (up to 25 min),
never starts between :04 and :10 (lets the :07 grind take the lock first), stops taking new politicians at
HH:00 and releases the lock before the grind's HH:07 start, then resumes on the next call. A detached guardian
frees the lock if the round is killed (the grind has no stale-lock check). Worst case one grind round skipped.

**Models (no cloud, no paid API):** LM Studio `127.0.0.1:1234`. `qwen/qwen3.6-35b-a3b` (no-think) proposes;
`gemma-4-31b-it` cross-checks each surviving quote: on topic? right direction? about THIS official? meets the
WHOLE rule or only part of it? Search: SearXNG `127.0.0.1:8888` (one query, only when the record has no site;
only .gov hits naming the person are kept). Brave is not used. Pages: <= 1 request/second/host; CivicPlus
(fredericksburgva.gov) sometimes blocks us, then the Wayback copy is read and every change from it is HOLD.

**The gates (a finding that fails any of them is dropped or held, never scored):**

1. Rule text: the cell's question must be found on the published rubric page
   (`usmcmin.com/citizen/<category>.html`, or `scoring-system.html`); the patch quotes it beside the evidence
   with the page's binary rule ("Each question is binary (True / False / null). True earns +2 points.").
   No rule text, no score: HOLD `needs-ruling`.
2. Literal quote: the evidence quote must be on the cited page (case, whitespace, curly quotes normalized;
   nothing else). XML and link evidence is matched against the raw page.
3. On topic: the quote must carry a word from that question's own topic list (a pro-life line cannot fill the
   euthanasia or abolition cell) and pass the Gemma cross-check.
4. Scope: the page must name the official (first + last within two words, or "Last, First", or title +
   surname). Third-party passages must name them. Joint statements and passages naming another actor are
   HOLD. Contact/social fills only from the official page; a city site's own accounts are dropped.
5. Full standard: a quote that meets only part of a rule (a restriction is not abolition, a reform is not
   repeal) is HOLD `needs-ruling`, never TRUE.
6. Strongest evidence first: roll call / bill sponsor field > official's own government page > campaign
   site > endorsing/rating org > news/aggregator. News/aggregator alone is HOLD `needs-ruling`.
7. PAC / foreign-lobby cells (`sanctity_of_life[4]`, `foreign_policy_restraint[3]`) are never filled from
   page text; the patch reports hit / no-hit / not-run / answered-without-search-citation.
8. One quote backs at most 2 cells. Slogans and fragments stay blank.

**Gate auto vs HOLD.** Auto (would apply on a live run): only high-confidence fills of an EMPTY website,
term date, or office phone from an official structured source or official page, for a non-Virginia record.
HOLD for Roy QA: every score change, anything replacing a stored value, every Fredericksburg/Virginia
official, a first headline grade or a letter move, out-of-office / currency flags, dedupe / different-person
flags (never auto), uncited answered cells, dead or off-person citations, one source backing 3+ cells,
site-config or archive-copy evidence, and party-null records that would show 100/A.

**Apply (after Adam's go only).** `apply.py <review-patch.json>` prints the dossier; `--check` runs
`refine-records.py --dry-run` on it (read-only). `--live` refuses unless `FULL_REVIEW_APPLY_GO=<round-id>`;
it re-fetches every quote, takes the shared lock, works in an isolated worktree off origin/main and goes
through `commit_refinement.py` (path-scoped push = deploy). HOLD rows apply only when their `change_id` is
listed in `--approved <file>` by Roy/Adam. Flags, rulings and re-checks never apply through it.

**Who does what.** Claude Code / Cursor build and run rounds. Roy QAs the HOLD queue (approve change_ids;
he does not edit scorecard.json). Adam rules on `needs-ruling` rows. Verification of a round is done by a
separate agent per `VERIFY-HOWTO-scorecard-full-review.md` in the branch.
