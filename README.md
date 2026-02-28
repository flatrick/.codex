# codex-home

Safe-to-share baseline for a Codex home directory.

## What this repo tracks

- `config.toml` and `config.template.toml`
- `rules/`
- `skills/` (your user-installed skills)

## What this repo does not track

The `.gitignore` blocks local state, logs, and secrets:

- `auth.json` (contains auth/access/refresh tokens)
- `sessions/` (conversation history)
- `shell_snapshots/` (environment snapshots)
- `skills/.system/` (built-in system skills, ignored by default)
- `state_*.sqlite*`, `models_cache.json`, `tmp/`, `vendor_imports/`

## Bootstrap on a new machine

1. Back up existing `~/.codex` if present.
2. Clone this repo into `~/.codex`.
3. If needed, create config from template:
   - `cp config.template.toml config.toml`
4. Start Codex and authenticate locally (this recreates `auth.json`).

## Safety checks before sharing publicly

- Run `git status` and `git diff --cached` before each commit.
- Never force-add ignored files (`git add -f auth.json` is unsafe).
- If a secret is ever committed, rotate it immediately.
