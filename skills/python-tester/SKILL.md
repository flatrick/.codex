---
name: python-tester
description: Design, write, and debug high-quality Python tests with a pytest focus, using structured checklists and best practices. Use when working in test-related Python files or when the user asks for help with tests, coverage, or debugging failures.
---

# Python Tester

## When to Use This Skill

Use this skill when:
- The user is working in test-related files (e.g. `tests/`, `test_*.py`, `*_test.py`).
- The user asks to write, improve, or debug tests for Python code.
- The user mentions pytest, fixtures, parametrization, mocking, or coverage.

If the repo clearly uses a different framework (e.g. `unittest`), adapt patterns but keep the same testing principles.

## General Principles

- Aim for **clear, behavior-focused tests**: each test should describe one behavior or scenario.
- Prefer **pytest** style: simple functions, fixtures, parametrization, and concise assertions.
- Keep **setup small and explicit**; use fixtures only when they improve readability or reuse.
- Make failures **diagnostic**: assertion messages and structure should make it obvious what went wrong.
- Trade minor duplication for clarity; avoid over-abstracting test helpers.

## Common Workflows and Checklists

### 1. Designing New Tests for a Function or Class

Checklist:
- [ ] Identify the core behaviors (happy path) from the code or requirements.
- [ ] Enumerate edge cases (empty inputs, invalid values, boundaries, error conditions).
- [ ] Decide on test structure: separate tests per behavior (`test_do_x_when_y`).
- [ ] Use parametrization when the same behavior is checked for multiple inputs.

Response structure:
1. **List behaviors and edge cases** you will cover (bullets).
2. **Provide pytest tests** in a single code block.
3. Optionally mention **how to run** them (e.g. `pytest tests/test_module.py`).

### 2. Improving Existing Tests

Checklist:
- [ ] Remove irrelevant or redundant assertions that do not add signal.
- [ ] Clarify test names to describe behavior and expectation.
- [ ] Simplify setup; extract useful fixtures only when several tests share the same pattern.
- [ ] Avoid testing implementation details when behavior-based tests are possible.

Response structure:
- Short note on **what you’re improving** (names, duplication, clarity).
- **Updated tests** with improved structure.
- 1–3 bullets explaining key changes (e.g. “grouped related assertions”, “replaced repeated literals with parametrization”).

### 3. Debugging Failing or Flaky Tests

Checklist:
- [ ] Restate the failure: which test, what assertion or error, and under what conditions.
- [ ] Look for **non-determinism** (time, randomness, network, shared state).
- [ ] Suggest **minimal inspection steps** (extra logging, prints, assertions, isolating the test).
- [ ] Propose **code or test changes** to make behavior deterministic and explicit.

Response structure:
- One-sentence **problem summary**.
- Likely causes with reference to the **relevant code section** or fixture.
- **Concrete change** in code or tests with explanation.
- Short **verification plan** (how to reproduce and confirm it’s fixed).

### 4. Structuring Test Suites

Checklist:
- [ ] Group tests by module or feature (`tests/test_feature_x.py`).
- [ ] Use fixtures in `conftest.py` for **shared cross-file setup** only when needed.
- [ ] Keep fixtures **focused**; avoid large “god fixtures” that do too much.
- [ ] Prefer **factory functions** or simple builders for test data rather than complex inheritance.

Guidelines:
- Match existing project patterns if they are consistent.
- When suggesting new structure, explain it briefly (1–2 sentences) and keep changes incremental.

## Pytest-Specific Guidelines

- Use **plain `assert`** statements; rely on pytest’s assertion introspection.
- Use `pytest.mark.parametrize` to cover multiple input/output combinations in one test.
- Prefer fixtures over `setUp`/`tearDown`-style classes in new pytest code.
- When mocking, prefer `monkeypatch` or `unittest.mock` helpers consistent with project style; avoid over-mocking.
- Use markers (e.g. `@pytest.mark.slow`, `@pytest.mark.integration`) only when they reflect real differences in cost or external dependencies.

## Coverage and Test Quality

- Focus first on **critical paths and invariants** rather than chasing a specific percentage.
- When the user asks about coverage:
  - Explain briefly how to run it with pytest (e.g. `pytest --cov=PACKAGE --cov-report=term-missing`).
  - Suggest new tests that cover untested but important branches or error paths.
- Avoid suggesting brittle tests that depend on internal implementation details unless explicitly requested.

## Tool-Specific Expert Guidance

This skill should use the following tools effectively whenever they are available in a project.

### Watcher Loops (pytest-watcher and similar)

- Encourage a **fast red/green loop**:
  - Use watch commands (`pytest-watcher`, `ptw`, IDE watch tasks) to re-run affected tests automatically.
  - Prefer short, focused watch scopes (a single test file or directory) when debugging or iterating.
- When suggesting watch-based workflows:
  - Keep commands short and copy-pastable.
  - Default to watching from the project root unless the project uses a strong per-package layout.

### Coverage (pytest-cov + coverage.py)

- Prefer `pytest-cov` for integrated test runs:
  - `pytest tests --cov=PACKAGE_OR_PATH --cov-report=term-missing`
  - For branch-sensitive projects, add `--cov-branch`.
- When coverage data already exists (a `.coverage` file):
  - Use `coverage report -m` for terminal summaries.
  - Use `coverage html` for detailed HTML reports (often under `htmlcov/` or `build/coverage_html/`).
- Emphasize:
  - Using coverage to **discover missing behaviors and branches**, not to blindly chase 100%.
  - Adding tests that close meaningful gaps (error paths, boundary branches, configuration fallbacks).

### Property-Based Testing (Hypothesis)

- Use Hypothesis when:
  - The behavior is naturally expressed over a **range of inputs** (numbers, strings, collections, data classes).
  - Edge cases are hard to enumerate manually, or regressions tend to appear at weird boundaries.
- Guidelines:
  - Use `@given(...)` with strategies from `hypothesis.strategies` that match the domain.
  - Keep properties focused and readable; avoid “mega-properties” that assert many unrelated things.
  - Let Hypothesis discover counterexamples; do not over-constrain strategies just to make tests pass.

### Snapshot / Approval Testing (pytest-approvaltests and similar)

- Use approval tests when:
  - The output is **rich but stable** (formatted text, JSON, reports, multi-line messages).
  - Behavior is easier to review visually than to assert piece by piece.
- Guidelines:
  - Keep approved artifacts human-readable (`*.approved.txt`, JSON with pretty formatting).
  - When a snapshot changes:
    - First, confirm the new behavior is expected.
    - Only then re-approve/update the snapshot.
  - Avoid using snapshots for highly volatile data (timestamps, random IDs) unless normalized first.

### Mocking, Environment Overrides, and Web API Integration

- For mocking:
  - Prefer pytest’s ecosystem: `pytest-mock`’s `mocker` fixture or `monkeypatch`, depending on the project.
  - Patch at the **usage site** (where a dependency is imported), not where it is defined.
  - Avoid over-mocking; keep integration points realistic where possible.
- For environment/config overrides:
  - Use `monkeypatch.setenv`, temporary config objects, or dependency injection patterns.
- For HTTP and web APIs (e.g. FastAPI + `httpx`):
  - Prefer async tests when the framework is async.
  - Test behavior via HTTP-level contracts (status codes, response shapes, side effects), not internals.

### Mutation Testing (cosmic-ray and similar tools)

- Use mutation testing when:
  - You want to **strengthen assertions** and catch “false confidence” in tests.
  - Critical logic must be guarded against subtle regressions.
- Guidelines:
  - Focus on a specific module or package at a time.
  - Interpret survivors (mutants that are not killed) as questions: “What behavior is not asserted?”
  - Improve tests with clearer, more targeted assertions rather than just adding more of the same pattern.

### Type-Driven Testing (Pyright and Type Checkers)

- Combine static typing with tests:
  - Use Pyright (or similar) to enforce contract correctness between modules.
  - Use tests to cover **runtime behaviors** that types alone cannot express.
- When a type error appears:
  - Prefer adjusting real types or test expectations instead of suppressing the error.
  - Use the error as a signal that either implementation or test assumptions are misaligned.

## Examples

### Example: Add Tests for a Pure Function

User: “Write tests for `normalize_name`.”

Assistant using this skill:
- Lists behaviors (e.g. trimming whitespace, lowercasing, handling `None` or empty).
- Provides a pytest test module with parametrized tests for typical and edge inputs.

### Example: Fix a Flaky Test

User: “This test sometimes fails in CI.”

Assistant using this skill:
- Summarizes the flaky behavior.
- Identifies likely non-determinism (e.g. time, ordering, shared state).
- Suggests a more deterministic pattern (e.g. fixed seed, isolated temp directory, explicit ordering).
- Provides updated test code that is stable across runs.

