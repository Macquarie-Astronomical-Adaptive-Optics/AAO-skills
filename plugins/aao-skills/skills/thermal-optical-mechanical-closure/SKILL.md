---
name: thermal-optical-mechanical-closure
description: Perform or review screening-level STOP-style closure for telescope concepts by linking thermal cases, structural deformation, alignment stability, and optical performance budgets. Use for AAO optical systems where focus, line of sight, wavefront error, or plate scale can be affected by thermal or mechanical behavior.
---

# Thermal Optical Mechanical Closure

## Workflow

- Confirm that the work is broadly shareable. Move sensitive requirements, partner-private models, or controlled design data to the restricted workflow.
- Define the performance quantities before calculating: focus shift, line-of-sight drift, wavefront error, plate-scale change, vignetting, obscuration, or detector alignment.
- Establish cases explicitly: nominal, hot, cold, survival, launch-relaxed, powered, unpowered, or other task-specific states.
- Trace each case through the same chain:
  1. Thermal boundary conditions and heat paths.
  2. Material properties, conductance, radiative coupling, and gradients.
  3. Structural expansion, support deflection, or alignment change.
  4. Optical perturbation and performance metric.
  5. Requirement or budget margin.
- Keep proxy calculations labeled `screening-level` until supported by engineering-grade thermal, structural, and optical models.
- Tie every claimed margin to the input case and requirement. Do not report a single green number if one subsystem or case is untested.

## Checks

- Thermal nodes or gradients correspond to physical parts or explicitly documented abstractions.
- Structural support families carry the intended subsystem mass and axes in the required cases.
- Perturbations are applied to the optics in physical units with signs and coordinate frames stated.
- Budget closure includes residual margin for focus, line of sight, WFE, thermal gradient, structural alignment, and pointing where relevant.
- Hot/cold or launch-relaxed cases cannot silently reuse nominal assumptions.
- Generated summaries are tied to the current design inputs, not stale output files.

## Output Expectations

- Produce a short chain of evidence rather than isolated thermal, structural, or optical tables.
- Call out missing material data, unverified supports, absent test evidence, or coordinate-frame uncertainty.
- State whether the result is a sanity check, screening result, or engineering closure.
