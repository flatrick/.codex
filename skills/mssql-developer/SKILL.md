---
name: mssql-developer
description: MS SQL Server and T-SQL development, optimization, and schema management. Use when designing databases, writing complex stored procedures, troubleshooting performance issues using execution plans, or implementing data migrations. Focuses on MS SQL specific features like CTEs, window functions, and advanced indexing.
---

# MS SQL / T-SQL Developer

## Execution Workflow

1.  **Analyze Schema**: Inspect existing table structures, relationships, and constraints.
2.  **Draft SQL**: Develop the smallest correct SQL script (DDL or DML) to achieve the goal.
3.  **Optimize**: Use `EXPLAIN` or execution plan analysis to identify bottlenecks or missing indexes.
4.  **Test**: Execute the query or procedure in a safe environment; verify results against expected data.
5.  **Audit Impact**: Check for side effects on performance, locks, or dependent objects (views, triggers).
6.  **Summary**: Describe the schema changes or query improvements, and any potential downtime considerations.

## Implementation Rules

- **T-SQL Best Practices**: Use modern T-SQL features (e.g., CTEs, `CROSS APPLY`, Window Functions) for readability and performance.
- **Set-Based Logic**: Avoid cursors or procedural loops where set-based operations are possible.
- **Constraints**: Enforce data integrity using primary keys, foreign keys, and unique/check constraints.
- **Idempotency**: Ensure DDL scripts are idempotent (using `IF NOT EXISTS` or similar checks).
- **Security**: Prevent SQL injection; use parameterized queries and follow the principle of least privilege.

## Optimization Rules

- **Execution Plans**: Always check the execution plan for high-impact queries.
- **Indexing Strategy**: Ensure appropriate use of clustered and non-clustered indexes. Avoid over-indexing.
- **SARGability**: Write queries that can leverage indexes (avoid functions on columns in `WHERE` clauses).
- **Statistics**: Be aware of stale statistics; recommend `UPDATE STATISTICS` if necessary.

## Quality and Tooling

- **SQL Formatting**: Adhere to consistent casing (uppercase for keywords) and indentation.
- **Comments**: Document complex logic, especially within stored procedures or triggers.
- **Versioning**: Maintain schema changes in version control; use migration scripts if the project follows a migration-based approach.

## Communication Output

- State clearly which objects were modified or created.
- Provide example execution results or performance benchmarks if applicable.
- Call out any risks related to large data sets or locking during execution.
