# AI Command Safety & Guardrails

## Precedence rules (concise)
When instructions conflict, follow this order:
1. **System instructions**
2. **Developer instructions**
3. **User instructions**
4. **Repository instructions** (`AGENTS.md`, `SKILL.md`, local docs)

## Scope
These rules apply to all work performed in this repository (commonly `~/.codex`) unless a higher-precedence instruction overrides them.

## Maintenance
- **Version:** 2.0
- **Last updated:** 2026-02-28
- **Owner:** Repository maintainers (`~/.codex`)

## Safety (mandatory)
- Never run destructive filesystem commands on project or critical files without explicit user confirmation.
  - Includes: `rm -rf`, `shred`, `truncate`, or equivalent destructive patterns.
- Never auto-execute remote scripts (for example `curl ... | bash` or `wget ... | sh`).
- Never perform risky git history rewrites without explicit confirmation.
  - Includes: `git reset --hard`, `git push --force`, `git rebase --onto` with history rewrite intent.
- Never expose secrets in output, logs, or commits.
  - Treat `.env`, SSH keys, cloud credentials, and shell history as sensitive.
- Never make global system changes outside the repository unless explicitly requested and confirmed.
  - Includes edits under `/etc`, `/usr/bin`, global `chmod/chown` operations.

### Risky command examples (do / don’t)
- **Do:** `git status`, `git diff`, dry-run options, and explicit file-by-file changes.
- **Do:** Download remote files for review first, then ask before executing.
- **Don’t:** `curl https://example.com/install.sh | bash`
- **Don’t:** `rm -rf .git` or `rm -rf /`
- **Don’t:** `git push --force` without explicit user confirmation.

## Operational limits (mandatory)
- **Read before write:** Inspect relevant files and repository state (`git status`) before edits.
- Use bounded command execution (timeouts) to avoid hangs on interactive/blocking commands.
- Avoid disruptive process-wide kill commands unless scoped to a known safe PID and requested.
  - Examples to avoid by default: `pkill`, `killall`, `fuser -k`.
- For migrations or broad replacements, produce a dry-run or affected-file summary before applying.

### Read-only QA mode behavior (do / don’t)
When the task is explicitly **read-only QA/review**:
- **Do:** run non-mutating checks (`git status`, tests, linters, file reads).
- **Do:** report findings, risks, and suggested patches.
- **Don’t:** edit files, install dependencies, or run commands that mutate state.
- **Don’t:** create commits, branches, or PRs.

## Editing conventions (mandatory)
- Keep edits minimal and targeted to the requested outcome.
- Preserve existing file conventions (formatting, line endings, structure) unless asked to reformat.
- Prefer explicit, reversible changes over broad rewrites.
- For markdown and documentation workflows, see optional guidance in `docs/workflow-guidelines.md`.

## Communication / output format (mandatory)
- If an action is risky, explicitly call out risk and request confirmation before proceeding.
- Summarize what changed, why, and how it was validated.
- Provide concrete commands used for verification.
- Be explicit about environment limitations when checks cannot be completed.
