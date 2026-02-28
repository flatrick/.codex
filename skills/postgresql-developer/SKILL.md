---
name: postgresql-developer
description: PostgreSQL database design, query optimization, and schema management. Use when developing complex queries, implementing JSONB-based document storage, optimizing performance via indexing and partitioning, or managing database migrations. Focuses on PostgreSQL-specific features like Window Functions, CTEs, and PL/pgSQL.
---

# PostgreSQL Developer

## Execution Workflow

1.  **Analyze Schema**: Inspect existing table structures, indexes, and constraints.
2.  **Draft SQL**: Develop the smallest correct SQL script (DDL or DML) to achieve the goal.
3.  **Optimize**: Use `EXPLAIN (ANALYZE, BUFFERS)` to identify bottlenecks or inefficient scan types.
4.  **Test**: Execute the query or migration in a local or dev environment; verify data correctness.
5.  **Audit Impact**: Check for side effects on locking (especially for large tables) and index usage.
6.  **Summary**: Describe the schema changes or query improvements, and any potential downtime or locking risks.

## Implementation Rules

- **PostgreSQL Best Practices**: Use PostgreSQL-specific features (e.g., `JSONB`, `DISTINCT ON`, Window Functions) where appropriate.
- **Set-Based Logic**: Prefer set-based operations over procedural loops or `PL/pgSQL` cursors.
- **Data Integrity**: Enforce constraints (Primary Keys, Foreign Keys, Check Constraints, Unique Indexes).
- **Idempotency**: Ensure DDL scripts are idempotent using `CREATE TABLE IF NOT EXISTS`, `ALTER TABLE ... ADD COLUMN IF NOT EXISTS`, etc.
- **Security**: Prevent SQL injection; use parameterized queries and secure configuration.

## Optimization Rules

- **Explain Analyze**: Use `EXPLAIN ANALYZE` to get actual runtimes and plan details.
- **Indexing Strategy**: Leverage appropriate index types (B-tree, GIN for JSONB, GiST for geometric/text search).
- **Vacuum and Analyze**: monitor bloat and ensure statistics are up to date after large data changes.
- **Partitioning**: Consider table partitioning for very large datasets to improve performance.

## Quality and Tooling

- **SQL Formatting**: Maintain consistent style (lowercase for snake_case identifiers, uppercase for keywords).
- **Comments**: Document non-obvious logic and complex queries.
- **Versioning**: Track schema changes in version control; follow established migration patterns.

## Communication Output

- List all database objects created or modified.
- Provide key takeaways from `EXPLAIN ANALYZE` output for optimized queries.
- Call out potential risks, such as long-running transactions or lock contention.
