---
name: security-hygiene
description: Improve day-to-day security hygiene by identifying secrets exposure, dependency risks, and unsafe patterns, then proposing practical low-risk remediations. Use during code review, incident response, or pre-release checks.
---

# Security Hygiene

## When to Activate

- User asks for security review, hardening, or pre-release security checks.
- Changes touch authentication, authorization, data handling, or external integrations.
- There are concerns about leaked secrets, vulnerable dependencies, or risky defaults.

## Workflow

1. **Secrets handling audit**
   - Search for hardcoded credentials, tokens, private keys, and sensitive test fixtures.
   - Verify secret loading via environment/secret manager rather than source control.
2. **Dependency risk scan**
   - Inspect dependency manifests/lockfiles for known vulnerable or unmaintained packages.
   - Highlight exploitability and reachable attack surface, not just CVE presence.
3. **Unsafe pattern review**
   - Check for injection paths, insecure deserialization, weak crypto, disabled TLS checks, and overbroad permissions.
   - Validate authn/authz boundaries and least-privilege assumptions.
4. **Remediation guidance**
   - Prioritize fixes by impact and implementation risk.
   - Provide safe alternatives and migration notes to avoid breaking production behavior.
5. **Verification plan**
   - Recommend targeted tests/scans to confirm remediation and prevent regressions.

## Severity Model

- `critical`: active secret exposure, trivially exploitable remote compromise, or major auth bypass.
- `high`: realistic exploitation with significant data/system impact.
- `medium`: constrained exploitation or partial exposure.
- `low`: defense-in-depth or hygiene improvements.

## Output Template

- **Security posture summary**
- **Findings** (severity, evidence, exploitability)
- **Immediate containment** (if needed)
- **Recommended fixes** (ordered by risk reduction)
- **Follow-up controls** (tests, scanning, policy updates)
