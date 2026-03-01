# Codex Parity Execution Plan

## Current-State Gaps
- `skills/rust-developer` and `skills/rust-tester` were missing.
- `python-developer` and `python-tester` diverged from Cursor canonical skill bodies.
- No shared `skills-manifest.lock.json` existed for drift detection.
- `AGENTS.md` was missing as a primary instruction entrypoint.
- CI validation did not verify skill manifest integrity.

## Ordered Implementation Steps
1. Sync all shared `skills/*/SKILL.md` files from `~/.cursor` canonical source.
2. Add Rust skills (`rust-developer`, `rust-tester`) with Codex `agents/openai.yaml` adapters.
3. Keep Codex-only skills under `skills/.system/` unchanged.
4. Add `AGENTS.md` as primary instructions and keep `INSTRUCTIONS.md` mirrored.
5. Generate `skills-manifest.lock.json` with SHA256 hashes for the 14 shared skills.
6. Extend `.github/workflows/validate.yml` to enforce:
   - markdown lint/link checks including `AGENTS.md` and `PLAN.md`
   - required-file checks for `skills-manifest.lock.json`
   - rust adapter YAML existence checks
   - manifest hash verification against `skills/*/SKILL.md`
7. Run local validation and smoke checks.

## Validation Checklist
- [ ] `skills/` contains all 14 shared skills.
- [ ] Each shared skill in Codex has `skills/<name>/agents/openai.yaml`.
- [ ] `skills-manifest.lock.json` exists and hashes match current files.
- [ ] `AGENTS.md` and `INSTRUCTIONS.md` are synchronized.
- [ ] `uv run pytest` still works under the existing approved prefix.
- [ ] `python bootstrap.py` still generates valid `config.toml`.

## Rollback Notes
- Revert skill sync by restoring previous `skills/*/SKILL.md` versions from git.
- Remove Rust skills by deleting `skills/rust-developer` and `skills/rust-tester` only if parity strategy changes.
- Restore prior guardrails by resetting `AGENTS.md` and `INSTRUCTIONS.md` from git history.
- Revert CI behavior by restoring the previous `validate.yml`.

## Ongoing Maintenance Cadence
- **On every shared skill update:**
  - pull canonical changes from `~/.cursor/skills/*/SKILL.md`
  - regenerate `skills-manifest.lock.json`
  - rerun workflow validation
- **Weekly:** run parity check against `.cursor` and `.gemini` skill manifests.
- **Monthly:** review guardrails for medium-parity alignment while preserving Codex-specific constraints.
