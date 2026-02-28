---
name: ci-cd-operator
description: Diagnose CI/CD pipeline failures and improve release hygiene with fast triage, root-cause isolation, and safe remediation plans. Use when builds fail, deployments regress, or release confidence is low.
---

# CI/CD Operator

## When to Activate

- CI jobs are failing, flaky, slow, or unexpectedly skipped.
- Deployment/release stages are blocked or producing inconsistent outcomes.
- User requests pipeline hardening, release checks, or incident triage.

## Diagnostic Workflow

1. **Collect signals**
   - Identify failing stage, first bad run, and recent config/code changes.
   - Separate deterministic failures from flaky/transient failures.
2. **Local reproduction**
   - Re-run equivalent commands locally with CI-like environment variables where possible.
   - Confirm toolchain/runtime version mismatches.
3. **Root-cause isolation**
   - Classify failure: dependency, test, infra, permissions/secrets, artifact, or rollout logic.
   - Narrow to smallest failing step and verify with one confirming check.
4. **Remediation plan**
   - Propose least-risk fix first, then medium-term hardening.
   - Add guardrails: caching strategy, retries, timeouts, matrix tuning, and clearer failure logs.
5. **Release hygiene**
   - Validate changelog/version bump, migration order, rollback path, and post-deploy verification.

## High-Value Checks

- Pin and verify runtime/tool versions.
- Ensure lockfiles and dependency install strategy match CI.
- Detect hidden coupling between jobs/stages.
- Verify artifact naming, retention, and promotion integrity.
- Confirm deployment gates and rollback criteria are explicit.

## Output Template

- **Pipeline status summary**
- **Root cause** (with evidence)
- **Immediate fix** (safe + minimal)
- **Hardening actions** (prioritized)
- **Release readiness** (`ready`, `needs fixes`, `blocked`)
