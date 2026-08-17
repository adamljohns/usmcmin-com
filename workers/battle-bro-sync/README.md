# Battle Brother Sync API

Magic-link email sign-in + cloud habit sync for
`/family-captain/battle-bro-form/viewform.html`.

## What it does

1. Captain enters email → receives a 20-minute magic link (Resend)
2. Link opens the form with `?magic=…` → session token stored locally
3. Habit board / memory syncs to D1 across devices
4. Pair Battle Brother by email invite code → live Shared habits (no paste pack required)

Manual share packs still work as a fallback when offline or unpaired.

## One-time setup (Adam)

```bash
cd workers/battle-bro-sync
npx wrangler login
npx wrangler d1 create usmcmin-battle-bro
# paste database_id into wrangler.toml
npx wrangler d1 execute usmcmin-battle-bro --file=./schema.sql
npx wrangler secret put RESEND_API_KEY
npx wrangler secret put SESSION_SECRET   # any long random string
npx wrangler deploy
```

Point DNS / Worker route:

- Recommended: `bb.usmcmin.com` → this Worker  
- Or set on the form page before the script:  
  `window.BB_API_BASE = 'https://usmcmin-battle-bro-sync.<account>.workers.dev'`

In Resend: verify `usmcmin.com` and send from `noreply@usmcmin.com` (or update `EMAIL_FROM`).

Until Resend is configured, `/api/bb/auth/request` returns `devMagicUrl` so you can test the loop without email.

## API

| Method | Path | Auth | Purpose |
|--------|------|------|---------|
| GET | `/api/bb/health` | no | health |
| POST | `/api/bb/auth/request` | no | `{email}` → magic link email |
| POST | `/api/bb/auth/verify` | no | `{token}` → `{sessionToken,user}` |
| POST | `/api/bb/auth/logout` | yes | revoke session |
| GET | `/api/bb/me` | yes | user + brother |
| GET/PUT | `/api/bb/sync` | yes | habit/memory state |
| POST | `/api/bb/pair/invite` | yes | `{email}` → invite code |
| POST | `/api/bb/pair/accept` | yes | `{code}` |
| POST | `/api/bb/pair/unlink` | yes | clear pairing |
| GET | `/api/bb/brother` | yes | brother's Shared habits |

## Cost shape

Cloudflare D1 + Worker free tiers cover a small Armada cohort. Resend free tier is enough for magic links at this scale.
