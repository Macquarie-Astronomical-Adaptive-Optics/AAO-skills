---
name: telescope-geometry-honesty
description: Review or create telescope concept geometry, CAD-like exports, renders, and geometry generators so they remain physically connected, non-intersecting, export-consistent, and honest about concept maturity. Use for broadly shareable AAO telescope geometry work before presentation or manufacturing claims.
---

# Telescope Geometry Honesty

## Workflow

- Confirm that the geometry task is non-restricted and safe for broad AAO or approved-collaborator circulation.
- Treat attractive renders as untrusted until geometry checks pass. A good-looking model can still have floating parts, impossible penetrations, or missing interfaces.
- For CAD-like generation, prefer a source-controlled, STEP-first workflow: keep the geometry generator beside the exported STEP file, treat STL/GLB/DXF/images as secondary derived review outputs, and make the source-to-export command explicit. `text-to-cad` and its `build123d` CAD skill are useful reference patterns, not required dependencies.
- Before adding visual polish, check that the model includes the essential physical subsystems:
  - primary mirror and support cell
  - secondary mirror and explicit support structure
  - metering structure or optical tube
  - focal-plane package and detector support
  - radiator or thermal-control hardware when relevant
  - bus or payload interface
  - launch, deployment, or mounting interfaces when relevant
- If geometry is exported to more than one format, compare the released exports rather than trusting the source generator alone.
- When a missing subsystem, impossible load path, exporter mismatch, or stale artifact is found, record it as an explicit open gap instead of hiding it behind a nicer render.

## Sanity Checks

- `Connectivity`: no floating struts, brackets, spiders, supports, or hardware islands.
- `Whole assembly`: the non-exploded model resolves to one connected assembly unless a separation is intentional and documented.
- `Interference`: no solid-solid penetration except intentional joints, cutouts, clearances, or modeled interfaces.
- `Required parts`: optical, structural, thermal, detector, and interface subsystems are represented at the claimed maturity level.
- `Source/export trace`: every primary STEP or CAD-like artifact can be regenerated from a named source file and command.
- `Exporter parity`: STL, OpenSCAD, STEP, DXF, SVG, or other released views show the same interfaces and part families.
- `State inventory`: deployed and stowed configurations preserve persistent hardware unless changes are explicitly launch-only, disposable, or tooling.
- `Symmetry invariants`: repeated supports have consistent spacing, length, twist, and attachment logic.
- `Shield keep-clear`: membranes, shields, and panels include real cutouts or offsets where structure passes nearby.
- `Optical closure`: the focal plane, stop, baffles, supports, and clear apertures match the optical model.
- `Load-path honesty`: structural members in analysis also exist in released geometry or are called out as missing.

## Output Expectations

- Report geometry findings as concrete pass/fail/gap items tied to files or artifacts.
- Use labeled exploded, cutaway, or subsystem views when hidden structure matters.
- Do not call a package buildable if joints, fasteners, tolerances, deployment features, or inspection details are still placeholders.
