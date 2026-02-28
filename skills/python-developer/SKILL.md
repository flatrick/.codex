---
name: python-developer
description: Python implementation, debugging, refactoring, and quality workflow for production codebases. Use when Codex needs to build or modify Python features, diagnose runtime/test failures, improve typing and lint compliance, optimize performance, or add and maintain pytest coverage in existing projects.
---

# Python Developer

## Execution Workflow

1. Confirm scope from the user request and current code context.
2. Inspect the relevant modules, tests, and project tooling before editing.
3. Implement the smallest correct change that satisfies the request.
4. Add or update tests to cover behavior changes and edge cases.
5. Run quality gates (tests, type checks, lint/format commands already used by the repo).
6. Summarize behavioral impact, touched files, and remaining risks.

## Implementation Rules

- Preserve existing architecture and naming patterns unless the user asks for redesign.
- Prefer explicit, readable code over clever abstractions.
- Keep functions focused and side effects obvious.
- Avoid broad try/except blocks that hide actionable errors.
- Maintain backward compatibility for public functions unless the user approves breaking changes.

## Testing Rules

- Update nearest existing test module first; create new tests only when needed.
- Cover happy path, expected failures, and one meaningful edge case.
- For bug fixes, add a regression test that fails before the fix and passes after.
- Use deterministic test data; avoid time/network randomness unless explicitly required.

## Typing and Quality

- Add or improve type hints on modified public functions.
- Resolve static type issues in touched code instead of suppressing by default.
- Keep docstrings concise and focused on non-obvious behavior.
- Use project-native tooling for linting, formatting, and typing.

## Communication Output

When reporting completion:

- State what changed and why.
- List verification commands run and outcomes.
- Call out any task you could not complete and what is still needed.
