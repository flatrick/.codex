---
name: python-developer
description: Provide high-quality Python development assistance, including code authoring, refactoring, testing, and debugging, with concise templates and checklists. Use when working in Python files or when the user asks for Python-specific help.
---

# Python Developer

## When to Use This Skill

Use this skill whenever:
- You are editing or creating Python files (`.py`, `pyproject.toml`, `setup.cfg`, `tox.ini`, `pytest.ini`).
- The user asks for Python-specific help (writing code, refactoring, tests, packaging, typing, or debugging).
- The user mentions frameworks or tools commonly used with Python (e.g. pytest, FastAPI, Django, Click, Poetry, pip, venv).

If the user asks for something unrelated to Python, ignore this skill.

## General Interaction Guidelines

- Prefer **working code** over abstract discussion.
- Default to **modern Python** (3.10+ where possible) and standard library features.
- Assume the user is comfortable reading code; keep explanations **concise** unless they ask for more detail.
- Use **type hints** in new or significantly modified functions when it improves clarity.
- Suggest **small, incremental improvements** instead of large rewrites unless the user explicitly requests a bigger refactor.

## Common Task Templates

### 1. Implementing a New Function or Class

When the user asks to implement or extend Python functionality:

Checklist:
- [ ] Clarify input/output behavior and edge cases (from the prompt and existing code).
- [ ] Choose clear names and keep functions focused on one responsibility.
- [ ] Add type hints when they clarify usage.
- [ ] Provide at least one example usage or test if appropriate.

Response structure:

1. **Short summary** of what you’ll implement.
2. **Code block** with the implementation.
3. **Optional note** on important edge cases or assumptions (1–3 bullets max).

Example format (do not repeat this explanation in responses):

```python
def parse_items(raw: str) -> list[str]:
    ...
```

### 2. Refactoring Existing Code

When the user asks to clean up or improve Python code:

Checklist:
- [ ] Preserve external behavior and public APIs unless the user approves breaking changes.
- [ ] Aim to reduce duplication and clarify control flow.
- [ ] Prefer simple, readable constructs over clever one-liners.
- [ ] Avoid introducing new dependencies unless strongly justified.

Response structure:
- **Brief goal statement**: what the refactor improves (readability, performance, structure).
- **Before/after code** snippets only where helpful.
- **Short explanation** of key changes (2–4 bullets).

### 3. Writing or Updating Tests (pytest-focused)

Default to `pytest` unless the repository clearly uses another framework.

Checklist:
- [ ] Identify the core behaviors and edge cases to test.
- [ ] Use clear, descriptive test names (`test_what_expectation`).
- [ ] Keep each test focused on one behavior.
- [ ] Prefer fixtures for shared setup when it improves clarity.

Response structure:
- **List of behaviors** being tested.
- **Test code** in a single code block.
- Mention how to **run the tests** if not obvious (e.g. `pytest path/to/test_file.py`).

### 4. Debugging and Bug Investigation

When the user reports a bug, error trace, or unexpected behavior:

Checklist:
- [ ] Restate your understanding of the problem in one sentence.
- [ ] Point out the most likely source(s) based on the stack trace or symptoms.
- [ ] Suggest **one or two** concrete inspection steps (print/logging, assertions, minimal reproducer).
- [ ] Propose a **code change** that would likely fix the issue, with a brief rationale.

Response structure:
- **Problem summary**.
- **Likely cause** with reference to the relevant code area.
- **Proposed fix** with code.
- **How to verify** (test or reproduction steps).

## Style and Best Practices

- Follow **PEP 8** style unless the project clearly uses a different convention.
- Use **f-strings** for string interpolation in new code.
- Prefer `pathlib.Path` over raw string paths for new filesystem work.
- For concurrency, prefer `asyncio` for async I/O and `concurrent.futures`/`multiprocessing` for CPU-bound tasks; match the project’s existing patterns.
- When choosing data structures, pick the simplest one that expresses intent (e.g. `dataclass` for simple structured data, `Enum` for fixed choices).

## Project-Aware Behavior

When working inside a repository:
- Infer the existing patterns: import style, type checking level (e.g. `mypy`), testing framework, project layout.
- Match the project’s **dependency management** tool (e.g. `pip`, `Poetry`, `pip-tools`) when suggesting installation commands.
- Respect existing configuration files (`pyproject.toml`, `setup.cfg`, `tox.ini`, `pytest.ini`) and avoid contradicting them.

If the repository clearly uses a specific stack (e.g. Django, FastAPI, Click), adapt examples and suggestions to that stack.

## Examples

### Example: Add a Utility Function

User: “Add a helper to safely read JSON from a file.”

Assistant using this skill:
- Briefly states intent.
- Provides a typed function using `pathlib.Path`.
- Handles common errors with clear exceptions or return values.
- Optionally adds a small pytest-style test example.

### Example: Improve Readability

User: “This function is hard to read, can you clean it up?”

Assistant using this skill:
- States what will be improved (branching complexity, naming).
- Provides a refactored version with better structure.
- Mentions any non-obvious trade-offs or behavior assumptions.

