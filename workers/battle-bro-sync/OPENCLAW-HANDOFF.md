# OpenClaw / Max — Wire Battle Brother magic-link sync (do it for Adam)

**Priority:** high  
**Goal:** Deploy the Battle Brother cloud sync API, turn on Resend email magic links, point DNS, verify sign-in works, leave an agent-callable API.

**Repo:** `adamljohns/usmcmin-com`  
**Branch / PR:** `cursor/battle-bro-magic-link-sync-127b` · https://github.com/adamljohns/usmcmin-com/pull/61  
**Form URL:** https://usmcmin.com/family-captain/battle-bro-form/viewform.html  
**Worker package:** `workers/battle-bro-sync/`  
**Desired API host:** `https://bb.usmcmin.com`

---

## STATUS (updated 2026-08-18)

| Step | Status | Notes |
|------|--------|-------|
| Resend account | **DONE** | Adam created account |
| Resend API key | **IN LOCAL NOTE / TEXTEDIT** | Prefer TextEdit window titled **`resend API key`**. Fallback: note starting with **`Sally AnneOCA…`** label **`Resend API key:`** |
| Resend domain `usmcmin.com` | **DONE** | Adam added, configured, authorized |
| Resend domain `usmcmin.org` | **DONE** | Adam added, configured, authorized |
| Cloudflare login | **DONE** (Adam signed in) | Drive his open tab |
| D1 + Worker deploy | **NOT DONE** | Part C — **Max do this next** |
| `bb.usmcmin.com` route | **NOT DONE** | Part B2 / Custom Domain |
| PR #61 merged to main | **CHECK** | Needed for Account panel on live site |
| Magic-link E2E test | **NOT DONE** | Part E |
| Agent session / service token | **NOT DONE** | Part F |

### Max — immediate actions (in order)

1. **Open the note whose title starts with `Sally AnneOCA`** (1Password / Notes — wherever Adam keeps it). Read the line labeled **`Resend API key:`**.  
   - Store/copy into 1Password item `Resend · usmcmin Battle Brother` → `api_key` if not already there.  
   - **Do not** paste the raw key into GitHub, Slack, or git commits.
2. ~~Resend domains~~ — **DONE** (`usmcmin.com` + `usmcmin.org`). Prefer From: `The Family Captain <noreply@usmcmin.com>` (matches Worker). `noreply@usmcmin.org` is also fine if you change `EMAIL_FROM`.
3. **Deploy Worker now (Part C)** using that key as `RESEND_API_KEY` (`npx wrangler secret put RESEND_API_KEY` → paste from the note).
4. Attach `bb.usmcmin.com`, merge PR #61 if needed, run Part E test.

---

## Success criteria (all must pass)

1. Worker `usmcmin-battle-bro-sync` is deployed.
2. D1 database `usmcmin-battle-bro` exists, schema applied, `database_id` in `wrangler.toml`.
3. Secrets set: `RESEND_API_KEY`, `SESSION_SECRET`.
4. Resend can send from `noreply@usmcmin.com` (domain `usmcmin.com` verified).
5. DNS/route: `bb.usmcmin.com` → this Worker.
6. `GET https://bb.usmcmin.com/api/bb/health` returns `{ ok: true }`.
7. On the form: enter Adam’s email → magic link arrives → sign-in works → Sync now works.
8. Merge PR #61 to `main` if not already merged (so Account panel is live on R2).
9. Write the two secrets somewhere Adam/OpenClaw can reuse later (1Password preferred). **Do not paste raw secrets into Slack/GitHub issues.**

---

## Part A — Resend (browser; tab already open)

**Adam already created the Resend account and stored the API key in the note starting with `Sally AnneOCA…` (label `Resend API key:`).**

1. ~~In the Resend dashboard, go to **API Keys**.~~ *(key created)*
2. ~~Create key~~ — **DONE**; name may vary.
3. **Max: read key from Adam’s note** (title starts with **`Sally AnneOCA`**, label **`Resend API key:`**) → optionally mirror into 1Password as:
   - Vault item: `Resend · usmcmin Battle Brother`
   - Field: `api_key`
   - **Never commit the key to git or paste into PR comments.**
4. ~~Go to **Domains** → Add **`usmcmin.com`**~~ — **DONE** (also **`usmcmin.org`** authorized).
5. ~~Add the DNS records…~~ — **DONE** (Adam configured/authorized both domains).
6. ~~Wait until domain status is **Verified**.~~ — **DONE**.
7. Confirm From address will be:  
   `The Family Captain <noreply@usmcmin.com>`  
   (matches Worker `EMAIL_FROM` / `wrangler.toml`). `usmcmin.org` is available as alternate if needed.

If domain verification is blocked, stop and report which DNS records are pending. Do not invent records.

**If the note is missing or the label changed:** Adam regenerates a Resend API key and updates the `Sally AnneOCA…` note (or tells Max the new note title). Do not ask him to paste the key into public chat.

---

## Part B — Cloudflare DNS + Worker route (browser; Adam signed in)

### B1. DNS for Resend
In Cloudflare → domain **usmcmin.com** → **DNS**:
- Add every record Resend requested (TXT/CNAME as shown).
- Proxy status: follow Resend’s guidance (usually DNS-only / grey cloud for some email auth records).

### B2. DNS for API host
Add:

| Type | Name | Target | Proxy |
|------|------|--------|-------|
| CNAME | `bb` | `usmcmin-battle-bro-sync.<ACCOUNT_SUBDOMAIN>.workers.dev` **OR** Workers custom domain binding | Proxied (orange) is fine if using Workers Custom Domains |

Preferred path: use **Workers → usmcmin-battle-bro-sync → Settings → Domains & Routes → Custom Domain → `bb.usmcmin.com`**. Cloudflare will create the DNS record for you. Prefer that over hand-rolled CNAME.

### B3. API token for terminal (if wrangler login is painful)
Cloudflare → My Profile → API Tokens → Create Token  
- Template: **Edit Cloudflare Workers**  
- Include account that owns `usmcmin.com`  
- Store in 1Password: `Cloudflare · Workers API Token (usmcmin)`  
- Also note **Account ID** (Workers overview right sidebar).

Export for shell (on the machine that will run wrangler):

```bash
export CLOUDFLARE_API_TOKEN='…from 1Password…'
export CLOUDFLARE_ACCOUNT_ID='…account id…'
```

---

## Part C — Terminal deploy (from usmcmin-com repo)

Worktree must include PR #61 files. If on `main` without the worker folder yet, checkout the PR branch or merge first.

```bash
cd /path/to/usmcmin-com
git fetch origin
git checkout cursor/battle-bro-magic-link-sync-127b   # or merge PR #61 into main first
cd workers/battle-bro-sync

# Node 20+ recommended
npm install

# Auth: either prior `wrangler login` OR CLOUDFLARE_API_TOKEN env
npx wrangler whoami

# Create D1 (only once)
npx wrangler d1 create usmcmin-battle-bro
```

Copy the printed `database_id` into `wrangler.toml`:

```toml
[[d1_databases]]
binding = "DB"
database_name = "usmcmin-battle-bro"
database_id = "PASTE_ID_HERE"
```

Commit that ID on the branch (safe; not a secret).

```bash
# Apply schema (remote)
npx wrangler d1 execute usmcmin-battle-bro --remote --file=./schema.sql

# Secrets (paste from 1Password when prompted — do not echo into shell history if avoidable)
npx wrangler secret put RESEND_API_KEY
# paste Resend key

npx wrangler secret put SESSION_SECRET
# paste a long random string, e.g. openssl rand -hex 32

# Deploy
npx wrangler deploy
```

Then attach custom domain `bb.usmcmin.com` (dashboard or):

```bash
npx wrangler domains add bb.usmcmin.com
# if CLI supports it in this wrangler version; else use dashboard Custom Domains
```

Confirm vars in `wrangler.toml` / dashboard:

- `APP_ORIGIN=https://usmcmin.com`
- `EMAIL_FROM=The Family Captain <noreply@usmcmin.com>`
- `CORS_ORIGINS=https://usmcmin.com,http://127.0.0.1:8888,http://localhost:8888`

---

## Part D — Merge site UI if needed

If Account · Cloud Sync panel is not on live form yet:

1. Merge https://github.com/adamljohns/usmcmin-com/pull/61 into `main`.
2. Wait 2–4 minutes for R2 GitHub Action deploy.
3. Hard-refresh: https://usmcmin.com/family-captain/battle-bro-form/viewform.html

Confirm page source includes `battle-bro-cloud.js` and the **Account · Cloud Sync** card. Default API base in JS is `https://bb.usmcmin.com`.

---

## Part E — End-to-end test (browser)

1. Open https://usmcmin.com/family-captain/battle-bro-form/viewform.html
2. Account panel should say cloud is reachable (or at least accept magic link).
3. Enter Adam’s real email → **Email magic link**.
4. Open the email → click link (`?magic=…`).
5. Confirm “Signed in”.
6. Habit Board → check a box → **Sync now**.
7. In another browser/profile (or Incognito): magic-link again with same email → habit check should appear after sync.
8. Optional pair test: second email account → invite / accept code → Shared habits visible.

Health check:

```bash
curl -s https://bb.usmcmin.com/api/bb/health
# expect: {"ok":true,"service":"battle-bro-sync",...}
```

---

## Part F — Agent / bot access (required by Adam)

Humans use magic links. **Agents should not drive the form UI.** They should call the API.

### F1. Add a service token path (implement if missing)

If not already in Worker, add:

- Secret: `AGENT_SERVICE_TOKEN` (long random)
- Header: `Authorization: Bearer <AGENT_SERVICE_TOKEN>`
- Optional header: `X-BB-Actor-Email: captain@email.com` to act as a user for sync read/write in ops/debug
- Or simpler ops endpoints:
  - `GET /api/bb/health` (no auth)
  - Document that agent automation uses a dedicated “ops” user signed in via one stored session token created once by Max

**Minimum viable for agents today (no code change):**

1. Max completes one magic-link sign-in as `usmcministries2022@gmail.com` (or designated bot mailbox).
2. From DevTools → Application → Local Storage on the form origin, copy `fc_bb_session_v1` JSON (`sessionToken`).
3. Store in 1Password: `Battle Brother · Agent Session`.
4. Agent calls:

```bash
API=https://bb.usmcmin.com
TOKEN='…sessionToken…'

curl -s -H "Authorization: Bearer $TOKEN" "$API/api/bb/me"
curl -s -H "Authorization: Bearer $TOKEN" "$API/api/bb/sync"
curl -s -X PUT -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  "$API/api/bb/sync" \
  -d '{"state":{"profile":{"name":"Agent"},"habits":{"items":[],"checks":{}},"submissions":[]}}'
```

**Better follow-up (ask coding agent after deploy):** add `AGENT_SERVICE_TOKEN` middleware so bots don’t depend on a browser session blob.

### F2. What agents can do once wired

| Action | Endpoint |
|--------|----------|
| Health | `GET /api/bb/health` |
| Who am I | `GET /api/bb/me` |
| Pull habits/memory | `GET /api/bb/sync` |
| Push habits/memory | `PUT /api/bb/sync` |
| Invite brother | `POST /api/bb/pair/invite` `{"email":"…"}` |
| Accept invite | `POST /api/bb/pair/accept` `{"code":"…"}` |
| Brother shared board | `GET /api/bb/brother` |

FormSubmit weekly email path stays as-is for human weekly form submit.

---

## Part G — Report back to Adam

When done, reply with:

- [ ] Resend domain verified  
- [ ] `bb.usmcmin.com` health OK  
- [ ] Magic link received + sign-in OK  
- [ ] Cross-device sync OK  
- [ ] PR #61 merged / live Account panel  
- [ ] 1Password items created (names only)  
- [ ] Agent session or service token stored  
- [ ] Any blockers (DNS pending, Resend reject, wrangler auth, etc.)

**Do not** include raw API keys in the report.

---

## Failure cheatsheet

| Symptom | Fix |
|---------|-----|
| Form says cloud unreachable | DNS/custom domain not live; CORS; wrong `BB_API_BASE` |
| Magic link request OK but no email | Resend domain unverified / wrong From / API key |
| `devMagicUrl` returned | `RESEND_API_KEY` secret missing on Worker |
| 401 on sync | Session expired — request new magic link |
| D1 errors | `database_id` wrong or schema not applied `--remote` |
| CORS error from usmcmin.com | Add origin to `CORS_ORIGINS` and redeploy |

---

## Files Max may edit

- `workers/battle-bro-sync/wrangler.toml` — only to paste `database_id` / routes  
- Optionally small Worker patch for `AGENT_SERVICE_TOKEN`  
- Do **not** rewrite habit form content unless deploy requires `window.BB_API_BASE` override

---

## One-sentence brief for Max

Adam already has Resend and Cloudflare open—use those tabs to create a Resend key, verify `usmcmin.com`, deploy `workers/battle-bro-sync` with D1 + secrets, attach `bb.usmcmin.com`, merge PR #61 if needed, prove magic-link sync, and stash keys/session in 1Password so agents can call the API without clicking the form.
