---
name: space-telescope-concept
description: Develop broadly shareable space-telescope concept studies for AAO, including first-order optical prescriptions, mission assumptions, orbit and launcher constraints, thermal and radiation screening, mass and power budgets, and verification planning. Use only for non-restricted concepts safe for AAO or approved-collaborator circulation.
---

# Space Telescope Concept

## Workflow

- Confirm that the task is safe for broad AAO or approved-collaborator circulation. Move controlled, security-sensitive, commercially sensitive, partner-private, or clearance-dependent material to the restricted workflow.
- Start by pinning the concept frame: science case, wavelength range, aperture, focal ratio, field of view, detector package, orbit, pointing constraints, launcher or package envelope, thermal targets, mass, power, and concept maturity.
- Keep requirements, design assumptions, public facts, inferred values, and open gaps in separate sections.
- Prefer machine-readable requirements, budgets, and verification matrices when the repository already uses structured config.
- Build the concept in this order:
  1. First-order optical prescription and field coverage.
  2. Detector and focal-plane package.
  3. Mechanical load paths and launch envelope.
  4. Thermal architecture and radiator/shielding assumptions.
  5. Radiation, contamination, and survival screening.
  6. Verification evidence and residual risk.
- Treat optics, thermal behavior, mechanical deformation, and launch packaging as one coupled design problem. Do not polish renders or narratives before basic closure is checked.
- Label approximate models as `screening-level` and state what would be needed for engineering closure.

## Checks

- Optical: aperture, focal length, focal ratio, obscuration, field coverage, plate scale, focus location, vignetting, and obvious stray-light paths.
- Mechanical: launch loads, support-family load paths, deployed and stowed package envelopes, mass properties, and minimum structural interfaces.
- Thermal: hot/cold cases, survival cases, radiator view, shield assumptions, gradients, and heater/control assumptions.
- Space environment: Sun, Earth IR, albedo, eclipse or transient assumptions, total dose, displacement damage, single-event exposure, and coating degradation.
- Verification: every scoped requirement should have at least one named verification method or an explicit open gap.

## Output Expectations

- Produce concept briefs, trade studies, checklists, or repository edits that separate facts from assumptions.
- Flag public-confirmed values separately from ICD-pending or partner-supplied assumptions.
- Do not imply flight readiness, buildability, or access to detailed launcher/interface data unless the evidence is present.
