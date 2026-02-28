---
name: frontend-qa
description: Run targeted UI regression checks, capture screenshots, and produce concise QA reports for visual and interaction changes. Use when validating front-end behavior before merge or release.
---

# Frontend QA

## When to Activate

- UI components, styles, layout, routing, or client-side state handling changed.
- User asks for regression checks, visual validation, or QA notes.
- You need evidence (screenshots + repro steps) for sign-off.

## QA Workflow

1. **Define scope**
   - Identify impacted pages/components and expected behavior.
   - Select core viewports (desktop + mobile when relevant).
2. **Run smoke checks**
   - Load app, verify no console/runtime errors, confirm primary navigation.
   - Validate critical interactions (forms, buttons, dialogs, loading/error states).
3. **Regression pass**
   - Compare changed behavior against baseline expectations.
   - Check accessibility basics: focus visibility, keyboard navigation, labels, and contrast red flags.
4. **Capture artifacts**
   - Take screenshots for each changed view/state.
   - Record exact route, viewport, and step sequence.
5. **Report outcomes**
   - Mark each scenario `pass`, `fail`, or `blocked` with reason.
   - Include high-signal defects first.

## Screenshot Guidance

For each artifact include:

- Scenario name
- URL/route
- Viewport/device preset
- Preconditions and user actions
- Expected vs actual result

Prefer deterministic states (seeded data or stable fixtures) to reduce flaky comparisons.

## QA Report Template

- **Change under test**
- **Environment** (branch/commit, browser, viewport)
- **Scenarios tested** (status + notes)
- **Defects found** (severity + repro)
- **Artifacts** (screenshots/links)
- **Release recommendation** (`ship`, `ship with caveats`, `hold`)
