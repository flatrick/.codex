---
name: bash-developer
description: BASH (Bourne Again Shell) scripting, automation, and system utility development. Use when writing shell scripts, automating Linux/Unix tasks, managing system configurations, or developing command-line tools. Focuses on robust error handling, POSIX compatibility, and modern Bash features.
---

# Bash Developer

## Execution Workflow

1.  **Analyze Script Requirements**: Determine the target shell (e.g., `#!/bin/bash` vs `#!/bin/sh`) and environment dependencies.
2.  **Draft Script**: Write the smallest correct script or function using idiomatic Bash patterns.
3.  **Implement Error Handling**: Use `set -e`, `set -u`, `set -o pipefail`, and `trap` for robust execution.
4.  **Test**: Execute the script in a safe environment; verify logic with different inputs and edge cases.
5.  **Lint & Review**: Check for common pitfalls using tools like `shellcheck` if available.
6.  **Summary**: Describe the script's functionality, usage instructions, and any required environmental variables or permissions.

## Implementation Rules

- **Shebang**: Always include a proper shebang (e.g., `#!/usr/bin/env bash`).
- **Error Handling**: Use `set -euo pipefail` for safer scripts. Use `trap` to clean up temporary files or handle signals.
- **Variables**: Quote all variable expansions to prevent word splitting and globbing (e.g., `"$VAR"` instead of `$VAR`). Use local variables inside functions.
- **Portability**: Be mindful of differences between POSIX `sh` and Bash-specific features (`[[ ]]`, arrays, etc.). Prefer Bash features when the shebang specifies `/bin/bash`.
- **Logic**: Use `[[ ]]` for tests instead of `[ ]` for better functionality and safety.

## Scripting and Automation

- **Argument Parsing**: Use `getopts` or a standard `case` loop for robust command-line argument handling.
- **Functions**: Organize code into reusable functions with clear names and local scopes.
- **I/O Handling**: Use redirections and pipes effectively. Use `mktemp` for creating secure temporary files.
- **Logging**: Use descriptive output with prefixes (e.g., `[INFO]`, `[ERROR]`) and send errors to `stderr`.

## Quality and Tooling

- **Formatting**: Use consistent indentation (spaces or tabs as per project style).
- **Comments**: Document non-trivial logic, dependencies, and expected environmental variables.
- **Idempotency**: Ensure scripts can be run multiple times safely (e.g., check if a directory exists before creating it).

## Communication Output

- List the key scripts or functions implemented.
- Provide clear usage examples.
- Highlight any external command dependencies (e.g., `curl`, `jq`, `sed`).
