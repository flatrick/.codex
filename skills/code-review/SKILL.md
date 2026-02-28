---
name: code-review
description: Perform PR-quality static code review with risk triage, focused findings, and merge readiness guidance. Use when reviewing proposed changes, preparing reviewer notes, or identifying high-impact defects before merge.
---

# Code Review

## When to Activate

- User asks for a PR review, static review, or pre-merge quality pass.
- A change spans critical paths (auth, billing, data integrity, migrations).
- You need reviewer-ready findings with severity and confidence.

## Review Workflow

1. **Scope the change**
   - Read the diff and identify impacted modules, interfaces, and tests.
   - Note risky change types: schema changes, auth logic, concurrency, state transitions, and error handling.
2. **Run static checks**
   - Execute repo linters/tests relevant to changed files.
   - Inspect type safety, null/edge handling, API contract changes, and backwards compatibility.
3. **Triaging findings**
   - Rank by **severity** (`critical`, `high`, `medium`, `low`) and **confidence** (`high`, `medium`, `low`).
   - Prioritize defects that can cause data loss, security exposure, outages, or silent corruption.
4. **Assess merge readiness**
   - Determine if the change is merge-ready, conditionally ready, or blocked.
   - List minimum required fixes and recommended follow-ups.

## Finding Format

For each issue, report:

- **Title**: concise risk statement
- **Severity / Confidence**
- **Evidence**: file and line references
- **Impact**: user/system consequence
- **Suggested fix**: minimal, concrete remediation

## Review Heuristics

Check first:

- Input validation and trust boundaries
- Error propagation and retry behavior
- Race conditions, locking, and idempotency
- Breaking API/DB contract changes
- Missing tests for high-risk branches
- Logging/observability gaps on failure paths

## Output Template

- **Summary**: what changed and overall risk
- **Top findings**: ordered by severity
- **Merge decision**: `ready` / `ready with conditions` / `blocked`
- **Required actions**: must-fix list
- **Optional follow-ups**: improvements that can be deferred
