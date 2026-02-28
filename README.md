# codex-home

Safe-to-share baseline for a Codex home directory.

## What this repo tracks

- `config.template.toml` (canonical baseline)
- `profiles/` (shared profile overlays, e.g. `safe`, `fast`, `deep-review`)
- `config.local.example.toml` (machine-local override template)
- `rules/`
- `skills/` (your user-installed skills)

## Config layering convention

Use this deterministic, three-layer model on every machine:

1. `config.template.toml` (committed baseline)
2. `profiles/<name>.toml` (committed profile overlay)
3. `config.local.toml` (ignored machine-local overrides)

### Profile selection

- Select a profile with `CODEX_PROFILE` (defaults to `safe`):
  - `export CODEX_PROFILE=safe`

### Build `config.toml` from layers

Run this from the repo root to materialize a resolved `config.toml`:

```bash
CODEX_PROFILE="${CODEX_PROFILE:-safe}" python bootstrap.py
```

`bootstrap.py` applies the layering order (`config.template.toml` → `profiles/<name>.toml` → `config.local.toml`) and writes a deterministic `config.toml`.

> Local-copy fallback (no env var): copy one profile directly before editing local overrides:
> `cp profiles/safe.toml config.local.toml`

## What this repo does not track

The `.gitignore` blocks local state, logs, and secrets:

- `auth.json` (contains auth/access/refresh tokens)
- `config.local.toml` (machine-specific config overrides)
- `sessions/` (conversation history)
- `shell_snapshots/` (environment snapshots)
- `skills/.system/` (built-in system skills, ignored by default)
- `state_*.sqlite*`, `models_cache.json`, `tmp/`, `vendor_imports/`

## Bootstrap on a new machine

1. Back up existing `~/.codex` if present.
2. Clone this repo into `~/.codex`.
3. Choose a profile and export it (example: `export CODEX_PROFILE=safe`).
4. Create machine-local overrides from the example:
   - `cp config.local.example.toml config.local.toml`
   - edit `config.local.toml` as needed for model/sandbox/tool behavior.
5. Build `config.toml` from baseline + profile + local override (see command above).
6. Start Codex and authenticate locally (this recreates `auth.json`).

## Safety checks before sharing publicly

- Run `git status` and `git diff --cached` before each commit.
- Never force-add ignored files (`git add -f auth.json` is unsafe).
- If a secret is ever committed, rotate it immediately.
