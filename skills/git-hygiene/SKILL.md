---
name: git-hygiene
description: Audit and configure git repository settings for consistency, encoding safety, and developer experience. Use when setting up a new repo, onboarding a project, or diagnosing line-ending, encoding, or diff issues. Covers .gitattributes, .gitignore, .editorconfig, and relevant git config.
---

# Git Hygiene

## When to Activate

- A new repository is being initialized or cloned.
- The user reports encoding, line-ending, or diff problems.
- The user asks to review or improve a project's git setup.
- You notice a repo is missing `.gitattributes` or `.editorconfig` during other work.

## Audit Workflow

1. **Detect languages and file types** in the repository (scan extensions, build tools, config files).
2. **Check for existing config** — read `.gitattributes`, `.gitignore`, `.editorconfig`, and any local `.git/config` overrides.
3. **Identify gaps** — compare what exists against the recommended baseline for the detected stack.
4. **Propose changes** — present a summary of what's missing or misconfigured, and draft the files. Never overwrite without showing the diff first.
5. **Apply changes** after user approval. Commit the config files in a dedicated commit with a clear message.

## `.gitattributes` Rules

Always include:

```
# Normalize all text files to LF
* text=auto eol=lf
```

Then add type-specific rules based on what the repo contains:

| Pattern | Attributes | When to add |
|---------|-----------|-------------|
| `*.md` `*.mdc` | `text eol=lf diff=markdown` | Always |
| `*.py` | `text eol=lf diff=python` | Python projects |
| `*.js` `*.ts` `*.jsx` `*.tsx` | `text eol=lf` | JS/TS projects |
| `*.json` `*.yaml` `*.yml` `*.toml` | `text eol=lf` | Always (config files) |
| `*.html` `*.css` `*.scss` | `text eol=lf` | Web projects |
| `*.sh` `*.bash` | `text eol=lf` | Always (scripts) |
| `*.bat` `*.cmd` | `text eol=crlf` | Windows scripts only |
| `*.png` `*.jpg` `*.gif` `*.ico` `*.webp` | `binary` | When images present |
| `*.woff` `*.woff2` `*.ttf` `*.eot` | `binary` | When fonts present |
| `*.zip` `*.tar.gz` `*.jar` | `binary` | When archives present |
| `*.pdf` | `binary` | When PDFs present |
| `*.lock` | `-diff` | Lock files (suppress noisy diffs) |

Use built-in diff drivers when available: `diff=python`, `diff=markdown`, `diff=html`, `diff=css`.

## `.editorconfig` Rules

Create if missing. Baseline:

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 2

[*.py]
indent_size = 4

[*.{md,mdc}]
trim_trailing_whitespace = false

[Makefile]
indent_style = tab
```

Adapt `indent_size` and `indent_style` by inspecting existing code in the repo. Do not impose a style that contradicts what's already established.

## `.gitignore` Review

- Check for common oversights: editor temp files, OS files (`.DS_Store`, `Thumbs.db`), build artifacts, dependency directories, environment files.
- Suggest additions but never remove existing entries without asking.
- Reference gitignore templates from github/gitignore when appropriate.

## Git Config Recommendations

When relevant, suggest (but never apply without confirmation):

- `diff.markdown.xfuncname = "^#{1,6} .*"` — heading-aware markdown diffs.
- `core.quotepath = false` — display UTF-8 filenames properly.
- `core.safecrlf = warn` — warn about line-ending conversion issues.
- `merge.conflictStyle = zdiff3` — better conflict markers.

These should be project-local (`git config --local`) unless the user explicitly wants them global.

## Communication Output

When reporting:

- List all files created or modified.
- Show a table of detected file types and the attributes applied.
- Note any existing settings that conflict with best practices, with an explanation of why.
- Flag anything left unchanged and why.
