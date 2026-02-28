---
name: dotnet-developer
description: .NET implementation, debugging, and quality workflow for C# and VB.NET. Supports .NET Framework and .NET 9.0+. Use when building features, refactoring, or maintaining .NET solutions, managing projects with the dotnet CLI or MSBuild, and ensuring high code quality through testing and modern C# patterns.
---

# .NET Developer

## Execution Workflow

1.  **Analyze Solution Structure**: Inspect `.sln` and `.*proj` files to understand project dependencies and targets.
2.  **Restore & Build**: Ensure dependencies are resolved using `dotnet restore` and the project builds with `dotnet build`.
3.  **Implement Changes**: Apply the smallest correct change, following established patterns in the codebase.
4.  **Test**: Update or add tests (xUnit, NUnit, or MSTest) and run them using `dotnet test`.
5.  **Verify Quality**: Check for linting issues or compiler warnings.
6.  **Summary**: Report behavioral impact, modified projects, and any new dependencies added.

## Implementation Rules

- **Maintain Patterns**: Respect existing architectural patterns (e.g., Clean Architecture, MVC, Repository pattern).
- **Modern Features**: Prefer modern C# features (e.g., file-scoped namespaces, primary constructors, collection expressions) when working in .NET 9.0+ projects.
- **Async/Await**: Use asynchronous programming correctly; avoid `Task.Wait()` or `Task.Result`.
- **DI and IoC**: Favor Dependency Injection; avoid hardcoding dependencies or using the Service Locator pattern.
- **Legacy Compatibility**: Ensure compatibility with .NET Framework if targeting legacy environments.

## Testing Rules

- **Test Nearest First**: Update existing test projects before creating new ones.
- **Behavioral Testing**: Assert on outcomes and behaviors rather than implementation details.
- **Mocking**: Use mocking frameworks (e.g., Moq, NSubstitute) only for external boundaries (database, APIs).
- **Deterministic Tests**: Ensure tests are stable and do not rely on external state or random data.

## Quality and Tooling

- **NuGet**: Use the `dotnet add package` command for managing dependencies. Keep versions consistent across the solution.
- **Nullable Context**: Respect and improve `Nullable` reference type annotations where enabled.
- **Logging**: Use `ILogger` for diagnostic output; avoid `Console.WriteLine`.
- **Formatting**: Adhere to the project's `.editorconfig` or default .NET style guidelines.

## Communication Output

- State clearly which projects within the solution were affected.
- List commands used for building and testing.
- Highlight any breaking changes or significant dependency updates.
