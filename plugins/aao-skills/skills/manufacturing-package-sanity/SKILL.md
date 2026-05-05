---
name: manufacturing-package-sanity
description: Review or assemble broadly shareable concept manufacturing packages for AAO optical and telescope systems, including BOMs, CAD-like exports, drawings, materials, interfaces, tolerances, assembly notes, and inspection evidence. Use to prevent concept renders from being mistaken for build-ready packages.
---

# Manufacturing Package Sanity

## Workflow

- Confirm that drawings, part details, suppliers, tolerances, and interface data are safe for broad AAO or approved-collaborator circulation.
- State the package maturity: concept sketch, screening model, prototype package, review package, or build package.
- Tie every released part back to a geometry source, material, coating or finish, mass assumption, and subsystem role where available.
- When CAD is generated from code, prefer a STEP-first package pattern: commit or identify the source generator, primary STEP export, and exact regeneration command; use STL/GLB/DXF/renders only as secondary review products. `text-to-cad`/`build123d` is a useful example pattern, not a substitute for package evidence.
- Check that the package contains the build-relevant objects implied by the claim:
  - part list or BOM
  - drawings or export files
  - material and finish assumptions
  - joints, fasteners, flexures, adhesives, or bonding assumptions
  - tolerances and datums
  - assembly and alignment sequence
  - inspection or metrology plan
  - procurement or make/buy assumptions
  - state notes for deployed, stowed, launch-only, disposable, or tooling hardware
- Treat missing joints, fasteners, tolerances, and inspection steps as package gaps, not minor documentation cleanup.

## Checks

- Exported geometry, BOM, drawings, and mass properties describe the same part families.
- Primary CAD exports can be regenerated from source and have not drifted from the BOM, drawings, or reported mass properties.
- Parts used in analysis are present in the package or explicitly listed as missing.
- Interfaces are specific enough to understand load paths and alignment constraints.
- Deployed and stowed packages preserve persistent hardware inventory unless differences are documented.
- Rendered or visual artifacts do not hide inaccessible joints, impossible assembly order, or ambiguous supports.
- The package separates buildable detail from placeholders and concept-only geometry.

## Output Expectations

- Return a gap list, package checklist, or concrete edits that improve traceability.
- Avoid saying `buildable`, `ready`, or `released` unless the relevant evidence exists and has been checked.
- Flag any sensitive manufacturing information that belongs in a restricted repository.
