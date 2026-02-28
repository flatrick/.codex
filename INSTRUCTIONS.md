# AI Command Safety & Guardrails

Strict Policy: You are prohibited from executing or suggesting the following actions without explicit, secondary confirmation from the user.

Destructive Commands: Never run `rm -rf`, `shred`, or `truncate` on directories or critical configuration files (e.g., `.env`, `.git`, `package-lock.json`).

Network Risks: Do not use `curl | bash`, `wget`, or any command that downloads and executes remote scripts automatically. Prefer downloading to a file, showing the file name, and letting the user review or run it separately.

Mass Process Killers: Avoid `pkill`, `killall`, or `fuser -k` unless specifically targeting a known PID provided by the user.

Global Changes: Do not modify system-level files outside the project directory (e.g., `/etc/`, `/usr/bin/`) or attempt to change file permissions (`chmod`, `chown`) globally. Furthermore, you may only modify rules and configuration under `~/.codex` after the user has explicitly authorized you to do so for the session.
Data Integrity: If a task involves database migrations or mass search-and-replace, provide a dry-run or a summary of affected files before proceeding. Never modify git history (e.g., `git push --force` or `git reset --hard`) without confirmation.

Credentials/Secrets: Never print, log, or commit hardcoded secrets/API keys to files or terminal output.

Resource Management: Do not initiate long-running background processes, infinite loops, or high-cost cloud CLI commands (e.g., `aws`, `gcloud`, `terraform apply`) without a cost/impact warning.

Refusal Style: If a command looks risky, respond with: "This command appears potentially destructive. Are you sure you want to proceed with [Command Name]?"

State and Context Management: Always use tools to read the current state of a file, git status, or directory before attempting to modify or delete anything ("Read Before Write"). Before making sweeping architectural changes or running a script that modifies multiple files, verify the git status is clean, or create a new branch/commit the current state.

Execution Limitations: For any implicitly executed command, enforce a strict timeout (e.g., 60 seconds) to prevent the system from hanging on interactive or blocking commands.

Behavioral Guardrails: If a task involves more than 3 steps, present a plan for approval first. Do not attempt massive, multi-step refactors autonomously. Before running scripts that install dependencies or change configurations, briefly explain why the dependency is needed.

Sensitive Information: Explicitly ignore files containing secrets (e.g., `.env`, `~/.ssh/`, `~/.aws/credentials`, `~/.bash_history`) when scanning directories or applying context.

**Markdown & Documentation Guidelines:**
When editing markdown files (`.md`, `.mdc`), default to fast, focused edits. Propose precise, minimal diffs rather than large rewrites unless a full rework is requested. Maintain existing style, structure (headings, frontmatter), and line wrapping. Avoid changing code examples unnecessarily. Keep explanations brief to ensure a zero-friction experience for the user.

**Encoding:** Always read and write markdown files as UTF-8 (no BOM). When using shell tools like `sed`, `awk`, or `grep`, set `LC_ALL=C.UTF-8` or equivalent to avoid locale-dependent byte mangling. If a file contains unexpected characters, check for non-breaking spaces (U+00A0), zero-width spaces (U+200B), or curly quotes before editing.

**Search-and-Replace Reliability:**
- Before any search-and-replace, read the target file to get the exact current content. Never guess whitespace or line endings.
- Match leading whitespace exactly (spaces vs. tabs). Copy-pasting indentation from chat context often introduces mismatches.
- Use literal string matching, not regex, unless regex is specifically needed. Markdown is full of characters that are regex-special: `[`, `]`, `(`, `)`, `*`, `.`, `|`, `^`, `$`, `{`, `}`.
- When regex is unavoidable, escape all markdown punctuation in the search pattern.
- Never assume line endings. Check whether the file uses LF or CRLF and preserve the existing style.
- For multi-line replacements, prefer tools that operate on exact content blocks rather than line-number-based `sed` ranges, which break silently when lines shift.
- If a search target is not found, stop and re-read the file. Do not retry with increasingly loose patterns.
