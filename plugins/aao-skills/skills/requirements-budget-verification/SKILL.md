---
name: requirements-budget-verification
description: Convert AAO telescope or instrument concepts into traceable requirements, budgets, verification matrices, test plans, and release gates. Use when a project needs machine-readable requirements, mass or power budgets, optical or thermal allocations, or evidence-backed design-status reporting.
---

# Requirements Budget Verification

## Workflow

- Confirm that the material is safe for the broad AAO skills repository. Put sensitive requirements, partner-private criteria, or controlled verification evidence in the restricted workflow.
- Start from the user-visible design promise: what the instrument must do, where it operates, what interfaces it must respect, and what evidence would prove progress.
- Prefer structured files such as YAML, JSON, CSV, or tables when the repository already has machine-readable config.
- Keep these objects distinct:
  - `requirements`: shall/should statements and source assumptions
  - `budgets`: allocated quantities with margins and owners
  - `verification matrix`: requirement paths mapped to methods, commands, artifacts, or open gaps
  - `test plan`: later campaign areas, acceptance logic, and evidence still needed
  - `release gate`: checks that must pass before outputs are called current
- Every scoped requirement should have at least one verification method or a named open gap.
- Budgets should not be decorative. Require positive margin or an explicit overrun/risk entry for mass, power, WFE, alignment, thermal, pointing, radiation, contamination, or other relevant categories.

## Checks

- Shared values, such as aperture, focal length, orbit, thermal targets, launcher, mass, and power, agree across narrative docs and structured config.
- Verification commands or artifacts are reproducible from a clean checkout where possible.
- Generated summaries cannot silently satisfy a gate if their inputs are stale.
- Screening evidence is labeled separately from engineering verification or test evidence.
- Requirement identifiers remain stable enough for reviews, TODOs, and test plans to refer to them.

## Output Expectations

- Produce traceable requirement tables, budget ledgers, verification matrices, or review findings.
- Point out missing owners, ambiguous units, stale assumptions, and unverified margins.
- Avoid marking a requirement verified unless the named evidence has actually been inspected or run.
