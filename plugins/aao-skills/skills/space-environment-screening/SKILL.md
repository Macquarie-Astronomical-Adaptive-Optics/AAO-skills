---
name: space-environment-screening
description: Screen broadly shareable space-instrument concepts against orbit environment, thermal loading, radiation, contamination, survival, and operations assumptions. Use when AAO work involves LEO, sun-synchronous orbit, deep-space astronomy, spacecraft payloads, or space-based telescope trades.
---

# Space Environment Screening

## Workflow

- Confirm that the task does not include restricted mission details, protected launcher data, controlled requirements, or partner-private spacecraft information.
- State the environmental frame before calculating: orbit or trajectory, altitude, inclination, eclipse assumptions, pointing law, Sun keepout, Earth view, mission duration, and operating or survival mode.
- Separate public-confirmed mission facts from assumptions and placeholders.
- Screen environment in coupled passes:
  - solar flux, Sun angle, and shadowing
  - Earth IR and albedo
  - thermal transients and survival temperatures
  - radiation dose, displacement damage, and single-event exposure
  - coating or detector degradation
  - contamination, venting, and cleanliness assumptions
  - operations constraints such as safe mode, decontamination, or heater duty cycle
- Label simple models as `screening-level` and state which standards, detailed analyses, or vendor data would be needed later.

## Checks

- Spacecraft or payload surfaces have plausible Sun, Earth, radiator, and deep-space views.
- Hot, cold, eclipse, survival, and powered states are not conflated.
- Detector, electronics, coatings, adhesives, and mechanisms are screened against the relevant environment, not just the optics.
- Shielding assumptions are stated in material and thickness terms when radiation numbers are reported.
- Pointing and keepout assumptions are consistent with the claimed science mode.
- Environment inputs flow into requirements, budgets, and verification gaps.

## Output Expectations

- Return assumptions, screening calculations, and risk notes in a traceable form.
- Flag values that need mission-specific analysis, standards lookup, vendor confirmation, or spacecraft-interface data.
- Do not imply qualification or flight acceptance from a screening calculation.
