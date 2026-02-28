# Workflow Guidelines (Optional)

These are **preferences**, not hard safety rules. Use them to keep edits efficient and predictable.

## Markdown editing preferences
- Default to focused, minimal diffs.
- Preserve existing heading hierarchy, frontmatter, and wrapping style.
- Avoid rewriting code samples unless required by the task.
- Prefer concise explanations over long prose in documentation updates.

## Encoding preferences
- Read and write markdown as UTF-8 (no BOM).
- When using shell text tools, prefer a UTF-8 locale (for example `LC_ALL=C.UTF-8`).
- If edits fail unexpectedly, check for non-breaking spaces, zero-width characters, and smart quotes.

## Search-and-replace preferences
- Re-read target files before replacement; do not rely on stale snippets.
- Prefer literal matching over regex unless regex is required.
- Preserve indentation and line-ending style (LF/CRLF).
- If a match is not found, stop and re-check the exact file contents.
- Prefer exact-block replacements over fragile line-number-based substitutions.

## Suggested execution workflow
1. Inspect state (`git status`, target files).
2. Apply minimal edits.
3. Re-check diff for unintended changes.
4. Run relevant validations.
5. Summarize results with any risks or follow-ups.
