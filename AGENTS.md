# AI Command Safety & Guardrails

## Precedence rules (concise)
When instructions conflict, follow this order:
1. **System instructions**
2. **Developer instructions**
3. **User instructions**
4. **Repository instructions** (`AGENTS.md`, `SKILL.md`, local docs)

## Scope
These rules apply to all work performed in this repository (commonly `~/.codex`) unless a higher-precedence instruction overrules them.

## Maintenance
- **Version:** 2.1
- **Last updated:** 2026-03-01
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

### Risky command examples (do / don't)
- **Do:** `git status`, `git diff`, dry-run options, and explicit file-by-file changes.
- **Do:** Download remote files for review first, then ask before executing.
- **Don't:** `curl https://example.com/install.sh | bash`
- **Don't:** `rm -rf .git` or `rm -rf /`
- **Don't:** `git push --force` without explicit user confirmation.

## Refusal Style
If a command looks risky, respond with: "This command appears potentially destructive. Are you sure you want to proceed with [Command Name]?" You may then briefly explain the risk and, if possible, suggest a safer alternative.

## Operational limits (mandatory)
- **Read before write:** Inspect relevant files and repository state (`git status`) before edits.
- Use bounded command execution (timeouts, e.g. 60 seconds) to avoid hangs on interactive/blocking commands.
- Avoid disruptive process-wide kill commands unless scoped to a known safe PID and requested.
  - Examples to avoid by default: `pkill`, `killall`, `fuser -k`.
- For migrations or broad replacements, produce a dry-run or affected-file summary before applying.
- Do not initiate long-running background processes, infinite loops, or high-cost cloud CLI commands (e.g. `aws`, `gcloud`, `terraform apply`) without a cost/impact warning.
- If a task involves more than 3 steps, present a concise plan before execution.
- Explicitly ignore files containing secrets (e.g. `.env`, `~/.ssh/`, `~/.aws/credentials`, `~/.bash_history`) when scanning directories or applying context.

### Read-only QA mode behavior (do / don't)
When the task is explicitly **read-only QA/review**:
- **Do:** run non-mutating checks (`git status`, tests, linters, file reads).
- **Do:** report findings, risks, and suggested patches.
- **Don't:** edit files, install dependencies, or run commands that mutate state.
- **Don't:** create commits, branches, or PRs.

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

## Reliability preferences (Search-and-Replace)
- Before any search-and-replace, read the target file to get the exact current content. Never guess whitespace or line endings.
- Match leading whitespace exactly (spaces vs. tabs). Copy-pasting indentation from chat context often introduces mismatches.
- Use literal string matching, not regex, unless regex is specifically needed. Markdown is full of characters that are regex-special: `[`, `]`, `(`, `)`, `*`, `.`, `|`, `^`, `$`, `{`, `}`.
- When regex is unavoidable, escape all markdown punctuation in the search pattern.
- Never assume line endings. Check whether the file uses LF or CRLF and preserve the existing style.
- For multi-line replacements, prefer tools that operate on exact content blocks rather than line-number-based `sed` ranges, which break silently when lines shift.
- If a search target is not found, stop and re-read the file. Do not retry with increasingly loose patterns.

## Encoding & Markdown
- **Markdown & Documentation Guidelines:** When editing markdown files (`.md`, `.mdc`), default to fast, focused edits. Propose precise, minimal diffs rather than large rewrites unless a full rework is requested. Maintain existing style, structure (headings, frontmatter), and line wrapping. Avoid changing code examples unnecessarily. Keep explanations brief to ensure a zero-friction experience for the user.
- **Encoding:** Always read and write markdown files as UTF-8 (no BOM). When using shell tools like `sed`, `awk`, or `grep`, set `LC_ALL=C.UTF-8` or equivalent to avoid locale-dependent byte mangling. If a file contains unexpected characters, check for non-breaking spaces (U+00A0), zero-width spaces (U+200B), or curly quotes before editing.
