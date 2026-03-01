---
name: rust-developer
description: Provide high-quality Rust development assistance, including code authoring, refactoring, and debugging, with Cargo, clippy, and rustfmt. Use when working in Rust files (`.rs`, `Cargo.toml`) or when the user asks for Rust-specific help.
---

# Rust Developer

## When to Use This Skill

Use this skill whenever:
- You are editing or creating Rust files (`.rs`, `Cargo.toml`, `Cargo.lock`).
- The user asks for Rust-specific help (ownership, borrowing, traits, async, error handling, crates).
- The user mentions tools commonly used with Rust (e.g. Cargo, clippy, rustfmt, rust-analyzer).

If the user asks for something unrelated to Rust, ignore this skill.

## General Interaction Guidelines

- Prefer **working code** over abstract discussion.
- Default to **current stable** Rust and idiomatic patterns.
- Assume the user is comfortable reading code; keep explanations **concise** unless they ask for more detail.
- Use **type-driven design**: leverage `Result`, `Option`, and traits to model behavior.
- Suggest **small, incremental improvements** instead of large rewrites unless the user explicitly requests a bigger refactor.

## Common Task Templates

### 1. Implementing a Function, Struct, or Trait

When the user asks to implement or extend Rust functionality:

Checklist:
- [ ] Clarify input/output behavior and edge cases (from the prompt and existing code).
- [ ] Choose clear names and keep functions/structs focused on one responsibility.
- [ ] Model errors with `Result<E>` or absence with `Option<T>`; add doc comments and/or `#![doc = "..."]` example when appropriate.
- [ ] Consider ownership and borrowing: take references where copying is unnecessary.

Response structure:

1. **Short summary** of what you'll implement.
2. **Code block** with the implementation.
3. **Optional note** on important edge cases or assumptions (1–3 bullets max).

Example format (do not repeat this explanation in responses):

```rust
/// Parses the input into a list of items.
pub fn parse_items(raw: &str) -> Result<Vec<String>, ParseError> {
    // ...
}
```

### 2. Refactoring Existing Code

When the user asks to clean up or improve Rust code:

Checklist:
- [ ] Preserve external behavior and public APIs unless the user approves breaking changes.
- [ ] Aim to reduce duplication and clarify control flow; extract traits or helpers where it improves reuse.
- [ ] Prefer simple, readable constructs over clever one-liners.
- [ ] Avoid introducing new dependencies unless strongly justified.

Response structure:
- **Brief goal statement**: what the refactor improves (readability, performance, structure).
- **Before/after code** snippets only where helpful.
- **Short explanation** of key changes (2–4 bullets).

### 3. Debugging and Bug Investigation

When the user reports a bug, compiler error, or unexpected behavior:

Checklist:
- [ ] Restate your understanding of the problem in one sentence.
- [ ] Point out the most likely source(s): ownership/borrow issues, type mismatch, panic or unwrap in edge cases.
- [ ] Suggest **one or two** concrete inspection steps (logging, `dbg!`, minimal reproducer, `RUST_BACKTRACE=1`).
- [ ] Propose a **code change** that would likely fix the issue, with a brief rationale.

Response structure:
- **Problem summary**.
- **Likely cause** with reference to the relevant code area.
- **Proposed fix** with code.
- **How to verify** (`cargo build`, `cargo test`, or reproduction steps).

## Style and Tooling

- Follow project style; default to **rustfmt** and **clippy** (`cargo clippy`).
- Use **Cargo** for build and test: `cargo build`, `cargo test`, `cargo check`; mention these when relevant.
- Prefer `?` for error propagation; avoid unnecessary `unwrap()`/`expect()` in library or long-lived code.
- For async code, match the project's runtime (e.g. tokio, async-std) and use `#[tokio::test]` or equivalent in tests.

## Project-Aware Behavior

When working inside a repository:
- Infer existing patterns: error type (custom vs anyhow/thiserror), async runtime, testing style, project layout.
- Respect **Cargo.toml** and workspace layout; match edition and dependency choices.
- If the project uses a specific stack (e.g. actix, axum, serde), adapt examples and suggestions to that stack.

## Examples

### Example: Add a Helper

User: "Add a helper to safely read JSON from a file."

Assistant using this skill:
- Briefly states intent.
- Provides a function using `std::fs` and `serde_json` (or notes adding the dependency), returning `Result<T, E>`.
- Handles IO and parse errors with clear error types or messages.
- Optionally adds a small test or doc-test example.

### Example: Improve Readability

User: "This function is hard to read, can you clean it up?"

Assistant using this skill:
- States what will be improved (branching, naming, extraction).
- Provides a refactored version with clearer structure.
- Mentions any non-obvious trade-offs or behavior assumptions.
