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

## Operations (day-2)

### New machine setup verification checklist

After bootstrap, verify the machine is actually usable end-to-end:

- **Auth present**
  - Confirm `auth.json` exists after sign-in.
  - Run a simple Codex command that requires auth and confirm there is no auth prompt loop.
- **Config loaded**
  - Rebuild config and check for errors:
    - `CODEX_PROFILE="${CODEX_PROFILE:-safe}" python bootstrap.py`
  - Confirm `config.toml` was updated and reflects expected profile + local overrides.
- **Skills visible**
  - Ensure your user skills are present under `skills/`.
  - Start Codex and verify expected skills/tools are listed.
- **Sample prompt works**
  - Run a small "smoke" prompt (for example: ask for a summary of `README.md`) and confirm response + file access are working.

### Upgrade path (safe pulls + local overrides)

Use this sequence whenever updating from upstream:

1. Inspect local changes:
   - `git status`
2. If you have local edits, either commit them on a branch or stash safely:
   - `git stash push -u -m "pre-upgrade $(date +%F)"`
3. Fetch and fast-forward:
   - `git fetch origin`
   - `git pull --ff-only`
4. Re-apply local changes (if stashed):
   - `git stash pop`
5. Resolve merge conflicts with this priority:
   - Keep upstream changes in committed baseline files (`config.template.toml`, `profiles/*`, shared rules/skills).
   - Keep machine-specific intent in `config.local.toml` (re-apply manually when needed).
6. Rebuild config and smoke test:
   - `CODEX_PROFILE="${CODEX_PROFILE:-safe}" python bootstrap.py`
   - run one sample Codex prompt.

### Disaster recovery (restore + re-authenticate)

If the working copy becomes corrupted or misconfigured:

1. Preserve anything you may need:
   - `cp -a ~/.codex ~/.codex.backup.$(date +%F-%H%M%S)`
2. Re-clone a clean copy of this repo into `~/.codex`.
3. Recreate local-only files:
   - `cp config.local.example.toml config.local.toml`
   - restore any machine-specific edits from backup.
4. Rebuild effective config:
   - `CODEX_PROFILE="${CODEX_PROFILE:-safe}" python bootstrap.py`
5. Re-authenticate in Codex (generates fresh `auth.json`).
6. Validate with the checklist above (auth/config/skills/sample prompt).

### Secret incident response

If `auth.json` or any credential-bearing config is exposed:

1. **Containment (immediate)**
   - Revoke/terminate active auth sessions for the affected account(s).
   - Remove leaked files from any shared artifacts.
2. **Rotate in order**
   - Rotate provider/API credentials referenced by local overrides.
   - Re-authenticate Codex to mint fresh local auth state (`auth.json`).
   - Update machine-local secrets in `config.local.toml` (never commit this file).
3. **Repository hygiene**
   - Confirm leaked secrets are not present in Git history/branches still in use.
   - If committed, coordinate history cleanup and force token invalidation.
4. **Recovery validation**
   - Re-run bootstrap + smoke prompt.
   - Confirm no old sessions/tokens remain active.

### Troubleshooting matrix (IDE integrations)

| Symptom | Likely cause | What to check/fix | Local logs/state location |
| --- | --- | --- | --- |
| IDE extension cannot connect to Codex | Wrong workspace/home path | Verify extension points to `~/.codex` and repository exists | `~/.codex/` |
| Repeated auth prompts in IDE | Missing/expired auth state | Re-authenticate and confirm `auth.json` recreated | `~/.codex/auth.json` |
| Profile changes not reflected | `config.toml` not rebuilt | Re-run bootstrap and restart IDE extension/session | `~/.codex/config.toml`, `~/.codex/config.local.toml` |
| Skills missing in IDE UI | Skills not installed/synced | Check `skills/` contents and restart IDE integration | `~/.codex/skills/`, `~/.codex/skills/.system/` |
| Slow, stale, or inconsistent behavior | Corrupt local state/session cache | Close IDE, back up then clear transient state, restart | `~/.codex/sessions/`, `~/.codex/shell_snapshots/`, `~/.codex/tmp/`, `~/.codex/state_*.sqlite*` |

## Safety checks before sharing publicly

- Run `git status` and `git diff --cached` before each commit.
- Never force-add ignored files (`git add -f auth.json` is unsafe).
- If a secret is ever committed, rotate it immediately.
