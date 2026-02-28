---
name: python-tester
description: Python testing strategy and implementation for existing codebases. Use when Codex needs to design or update pytest test suites, reproduce and isolate bugs, add regression coverage, improve flaky tests, validate edge cases, or tighten confidence for refactors and releases.
---

# Python Tester

## Test Workflow

1. Identify expected behavior and failure modes from code, docs, and existing tests.
2. Reproduce the issue or gap with the smallest failing test.
3. Choose the right test layer: unit, integration, API, or end-to-end.
4. Implement deterministic tests with clear fixtures and assertions.
5. Run targeted tests first, then broader suite checks.
6. Report coverage added, residual risk, and follow-up recommendations.

## Test Design Rules

- Prefer behavior-focused assertions over implementation details.
- Keep tests independent and order-agnostic.
- Use parameterization for repeated input/output patterns.
- Minimize mocking; mock only unstable or external boundaries.
- Name tests to describe scenario and expected outcome.

## Bug Reproduction and Regression

- Capture the bug with a failing test before changing production code when feasible.
- Reduce reproductions to minimal inputs to speed diagnosis.
- Convert every fixed bug into a stable regression test.
- Document assumptions for nondeterministic behaviors (time, random, network).

## Data and Fixtures

- Build reusable fixtures for shared setup while keeping local setup explicit.
- Use factory helpers to create valid defaults and targeted overrides.
- Avoid hidden global state in fixtures.
- Clean up temporary files, DB rows, and environment mutations.

## Verification and Reporting

When finishing a testing task:

- List tests added or updated and the behavior each covers.
- Include commands run and whether they passed.
- Call out gaps that remain untested and why.
