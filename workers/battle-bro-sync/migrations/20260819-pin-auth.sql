-- PIN auth + reset tokens (idempotent)
ALTER TABLE users ADD COLUMN password_hash TEXT;
CREATE TABLE IF NOT EXISTS reset_tokens (
  token_hash TEXT PRIMARY KEY,
  email TEXT NOT NULL COLLATE NOCASE,
  expires_at TEXT NOT NULL,
  used_at TEXT
);
