---
name: powershell-developer
description: PowerShell v7+ scripting, automation, and module development. Use when writing cross-platform automation scripts, managing infrastructure, developing PowerShell modules, or optimizing pipeline performance. Focuses on modern PowerShell features (v7+), error handling, and security best practices.
---

# PowerShell Developer

## Execution Workflow

1.  **Analyze Environment**: Check PowerShell version (`$PSVersionTable`) and available modules.
2.  **Draft Script**: Write the smallest correct script or function to achieve the goal.
3.  **Implement Error Handling**: Use `try...catch...finally` and `ErrorAction` to handle expected and unexpected failures.
4.  **Test**: Execute the script in a safe environment; verify output and state changes.
5.  **Verify Compatibility**: Ensure the script works across platforms (Linux/Windows) if required.
6.  **Summary**: Describe the script's purpose, key functions, and any required modules or permissions.

## Implementation Rules

- **PowerShell v7+ Best Practices**: Use modern features like the Ternary operator (`? :`), Pipeline chain operators (`&&`, `||`), and `Parallel` foreach loops.
- **Pipeline Usage**: Lean into the PowerShell pipeline for idiomatic data processing.
- **Strong Typing**: Use type accelerators and explicit typing for function parameters.
- **Error Handling**: Always use `try/catch` for critical operations. Use `$ErrorActionPreference = 'Stop'` for deterministic failure.
- **Security**: Avoid `Invoke-Expression` on untrusted input; use `Get-Credential` or secret management for sensitive data.

## Scripting and Automation

- **Module Design**: Follow standard module structure (Manifest, Public/Private functions).
- **Function Naming**: Use approved Verb-Noun pairs (e.g., `Get-Item`, `Set-Value`).
- **Dependency Management**: Clearly state required modules in the script header or module manifest.
- **Logging**: Use `Write-Verbose`, `Write-Debug`, and `Write-Information` for structured output.

## Quality and Tooling

- **Formatting**: Adhere to the PSScriptAnalyzer rules or the project's `.editorconfig`.
- **Documentation**: Use Comment-Based Help (`.SYNOPSIS`, `.DESCRIPTION`, `.PARAMETER`).
- **Idempotency**: Ensure scripts can be run multiple times without causing unintended side effects.

## Communication Output

- List the primary functions or scripts created.
- State any environmental prerequisites (modules, permissions, PWSH version).
- Highlight any significant performance improvements or automation achievements.
