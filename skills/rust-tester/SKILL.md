---
name: rust-tester
description: Design, write, and debug Rust tests with a cargo test focus, using unit and integration tests and common crates. Use when working in test modules, `tests/`, or when the user asks for help with tests, coverage, or debugging test failures.
---

# Rust Tester

## When to Use This Skill

Use this skill when:
- The user is working in test modules (`#[cfg(test)]`, `mod tests`), `tests/*.rs`, or doc-tests.
- The user asks to write, improve, or debug tests for Rust code.
- The user mentions `cargo test`, fixtures, mocking, coverage, or flaky/failing tests.

If the repo uses a different test harness, adapt patterns but keep the same testing principles.

## General Principles

- Aim for **clear, behavior-focused tests**: each test should describe one behavior or scenario.
- Prefer **cargo test** style: `#[test]` functions, `#[cfg(test)]` modules, integration tests in `tests/`.
- Keep **setup small and explicit**; use helpers or shared modules only when they improve readability or reuse.
- Make failures **diagnostic**: assertion messages and structure should make it obvious what went wrong.
- Trade minor duplication for clarity; avoid over-abstracting test helpers.

## Common Workflows and Checklists

### 1. Designing New Tests for a Function or Type

Checklist:
- [ ] Identify the core behaviors (happy path) from the code or requirements.
- [ ] Enumerate edge cases (empty inputs, invalid values, boundaries, error conditions).
- [ ] Decide on test structure: one `#[test]` per behavior (e.g. `test_parse_valid_input`, `test_parse_empty_returns_error`).
- [ ] Use multiple tests or a small test helper for several input/output combinations.

Response structure:
1. **List behaviors and edge cases** you will cover (bullets).
2. **Provide test code** in a single code block (unit tests in `#[cfg(test)] mod tests` or integration in `tests/`).
3. Mention **how to run** (e.g. `cargo test`, `cargo test -- parse_`).

### 2. Improving Existing Tests

Checklist:
- [ ] Remove irrelevant or redundant assertions that do not add signal.
- [ ] Clarify test names to describe behavior and expectation.
- [ ] Simplify setup; extract shared helpers only when several tests share the same pattern.
- [ ] Avoid testing implementation details when behavior-based tests are possible.

Response structure:
- Short note on **what you're improving** (names, duplication, clarity).
- **Updated tests** with improved structure.
- 1–3 bullets explaining key changes.

### 3. Debugging Failing or Flaky Tests

Checklist:
- [ ] Restate the failure: which test, what assertion or panic, and under what conditions.
- [ ] Look for **non-determinism** (time, randomness, shared state, order of execution).
- [ ] Suggest **minimal inspection steps** (logging, `dbg!`, isolate with `cargo test -- test_name`).
- [ ] Propose **code or test changes** to make behavior deterministic and explicit.

Response structure:
- One-sentence **problem summary**.
- Likely causes with reference to the **relevant code** or setup.
- **Concrete change** in code or tests with explanation.
- Short **verification plan** (how to reproduce and confirm it's fixed).

### 4. Structuring Test Suites

Checklist:
- [ ] Use `#[cfg(test)] mod tests` in the same file for **unit tests**; use `tests/*.rs` for **integration tests**.
- [ ] Put shared test helpers in a common module (e.g. `tests/common/mod.rs`) only when needed.
- [ ] Keep helpers **focused**; avoid large setup that does too much.
- [ ] Prefer simple constructors or builder-style helpers for test data.

Guidelines:
- Match existing project layout. When suggesting new structure, explain briefly (1–2 sentences) and keep changes incremental.

## cargo test and Tooling

- Default to **cargo test**; mention filtering: `cargo test -- test_name_substring`, `cargo test --package name`.
- Use **--no-fail-fast** to run all tests after the first failure when debugging.
- **Doc-tests**: include `/// # Example` in doc comments when they double as executable examples; run with `cargo test --doc` or as part of `cargo test`.
- **Async tests**: use the same runtime as the crate (e.g. `#[tokio::test]` for tokio); ensure test runtime is available in dev-dependencies if needed.

## Optional Tool Guidance (brief)

- **Coverage**: For coverage, use `cargo-tarpaulin` or `cargo-llvm-cov`; suggest running and interpreting reports to find untested branches or paths.
- **Property-based**: Use **proptest** when behavior is naturally expressed over many inputs or edge cases are hard to enumerate; keep strategies focused.
- **Mocking**: Use **mockall** (or similar) for external boundaries (e.g. IO, APIs); prefer dependency injection or traits to keep tests fast and deterministic.

## Examples

### Example: Add Tests for a Pure Function

User: "Write tests for `normalize_name`."

Assistant using this skill:
- Lists behaviors (e.g. trimming whitespace, lowercasing, handling empty).
- Provides a `#[cfg(test)] mod tests` with `#[test]` functions for typical and edge inputs.

### Example: Fix a Flaky Test

User: "This test sometimes fails in CI."

Assistant using this skill:
- Summarizes the flaky behavior.
- Identifies likely non-determinism (e.g. ordering, shared state, time).
- Suggests a more deterministic pattern (e.g. fixed seed, isolated data, explicit order).
- Provides updated test code that is stable across runs.
