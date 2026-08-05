---
name: stl-surface-reconstruction
description: Clean, diagnose, reduce, render, and route STL meshes into lighter review meshes or CAD-style analytic and spline surface reconstructions. Use for broadly shareable AAO Ansys or FEA exports with floating fragments, excessive triangle counts, open or non-manifold topology, requests for smoother surfaces, or targets stated as very few points, faces, surfaces, patches, or control points.
---

# STL Surface Reconstruction

## Scope and safety

- Confirm that the geometry and derived measurements are safe for broad AAO or
  approved-collaborator circulation. Keep restricted, partner-private,
  commercially sensitive, controlled, and Defence-adjacent geometry out of this
  public skill repository.
- Work in the approved project repository, not inside this skill directory.
- Preserve the source STL byte-for-byte in a repo-local ignored data directory.
  Record its name, size, SHA-256 digest, and provenance before processing.
- Treat STL coordinates as unitless until the originating CAD or solver unit is
  confirmed. Never silently assign millimetres, metres, or inches.

## Translate the requested outcome

Before choosing an algorithm, distinguish these different operations:

- `Component cleanup`: remove detached islands or debris after inspecting them.
- `Decimation`: reduce triangle and vertex counts while remaining a mesh.
- `Smoothing`: move vertices and therefore change geometry.
- `Remeshing`: replace the triangulation and possibly the topology.
- `CAD reconstruction`: replace facets with planes, cylinders, cones, tori, and
  bounded spline or NURBS patches, preferably in STEP.

When a request says “fewer than 20 points” or similar, determine whether it
means total mesh vertices, control points per spline patch, analytic surfaces,
CAD faces, or feature count. Fewer than twenty total points cannot retain holes,
vents, multiple branches, or irregular topology. Offer an envelope or selected
subsystem only when that is the intended approximation.

Read [references/representation-and-verification.md](references/representation-and-verification.md)
when deciding between a reduced mesh and a CAD-style reconstruction.

## Workflow

### 1. Create a contained work area

Use a structure such as:

```text
mesh-reconstruction/
  data/raw/       # ignored source files
  data/derived/   # ignored generated geometry and renders
  reports/        # small measurements suitable for review
  scripts/        # project-specific generators, if needed
```

Ignore the data directory, not the scripts and reports. Verify the copied source
hash against the original.

### 2. Inventory before cleanup

Run the bundled component analyser where NumPy and SciPy are available:

```bash
python scripts/stl_components.py SOURCE.stl --report components.json
```

Record at least:

- binary or ASCII STL format and source header;
- triangle count, exact unique vertex count, bounds, and bounding-box diagonal;
- degenerate and duplicate faces;
- exact vertex-connected component count;
- triangle count, surface area, and bounds per component;
- boundary, manifold, and non-manifold edge incidence;
- unknown or confirmed coordinate units.

Do not infer that the largest component is automatically the wanted part.
Render components in different colours and inspect their locations. A small
component can be a required insert, boss, support, or separate assembly part.

For Blender 4, create component review renders with:

```bash
blender -b --python scripts/render_components_blender.py -- SOURCE.stl OUTPUT_DIR
```

### 3. Remove confirmed fragments

Only after the component inventory and visual review support the decision, keep
the largest component with:

```bash
python scripts/stl_components.py SOURCE.stl \
  --report cleanup-report.json \
  --keep-largest CLEANED.stl
```

The script writes a binary STL, removes zero-area and duplicate faces, and
recomputes face normals. Re-run the analyser on the result. Report open and
non-manifold edges as remaining gaps rather than calling the output repaired or
watertight.

If more than one component is intentional, write a project-specific selector
using component bounds or explicit IDs; do not broaden `--keep-largest` into an
unreviewed fleet rule.

### 4. Establish a faithful reduction baseline

Try direct quadric edge-collapse decimation before geometric smoothing. Produce
a reduction ladder appropriate to the source size, such as 100k, 20k, 5k, and
1k triangles, and measure each candidate.

With Blender:

```bash
blender -b --python scripts/reduce_and_measure_blender.py -- \
  CLEANED.stl REDUCED.stl reduction-report.json 20000 reduced-preview.png
```

The bundled script reports sampled bidirectional nearest-surface deviation. Use
both reference-to-candidate and candidate-to-reference directions, and report
the sampled maximum as a percentage of the source bounding-box diagonal.

After Blender export, run `stl_components.py` again to remove any new degenerate
or duplicate faces and recheck connectivity and edge incidence.

### 5. Reject damaging smoothing

Do not describe smooth shading as geometric smoothing. If applying Laplacian,
Taubin, HC, bilateral, voxel, Poisson, or other filters:

- preserve and measure a direct-decimation baseline;
- constrain or separately assess boundaries and sharp features;
- render identical views before and after;
- check openings, thin walls, symmetry, clearances, and disconnected regions;
- measure bidirectional surface deviation;
- reject a candidate when a lower polygon count hides feature loss or large
  local movement.

### 6. Route genuine CAD reconstruction

For a smooth surface model rather than a lighter STL:

1. Segment dominant analytic regions such as planes, cylinders, cones, spheres,
   and tori.
2. Fit repeated features jointly when symmetry or a design grid is supported by
   the source.
3. Bound irregular residual regions and fit the smallest justified set of
   spline patches.
4. Record fit residuals per feature or patch and identify inferred or replaced
   geometry.
5. Keep the parametric generator beside the STEP output and make the
   source-to-export command explicit.
6. Round-trip the STEP file and verify face count, edge count, bounds, validity,
   units, and intended holes or inner wires.

An analytic reconstruction of only one plate or envelope is a subsystem
prototype, not a conversion of the complete part. Label omissions explicitly.

### 7. Use remote compute carefully

For longer work on `raksasa` or another approved host:

- confirm the project privacy boundary before transfer;
- inspect host reachability and load without interrupting existing jobs;
- use an isolated environment and an explicit task directory;
- record installed package versions and exact commands;
- retrieve reports and intended artifacts, then verify them locally;
- do not claim that a remote job succeeded until its outputs have been reopened.

## Acceptance checks

Report each item as `pass`, `fail`, or `gap`:

- `Source preservation`: copied hash equals the original hash.
- `Component decision`: removed and retained components have recorded evidence.
- `Topology`: connectivity and edge incidence measured after every export.
- `Fidelity`: bidirectional deviation and feature checks meet a stated tolerance.
- `Units`: source unit confirmed, or every scaled export carries an explicit
  convention and rescaling warning.
- `Representation`: mesh reduction is not presented as CAD reconstruction.
- `CAD trace`: STEP can be regenerated and passes a round-trip check.
- `Visual review`: consistent orthographic and isometric views were inspected.
- `Maturity`: open or non-manifold surfaces are not called manufacturing-ready
  solids.

## Output expectations

Provide:

- the preserved ignored source path and SHA-256 digest;
- a component inventory with the fragment-removal rationale;
- the cleaned mesh and its topology report;
- one accepted reduced candidate with triangle/vertex counts and deviation;
- rejected-candidate measurements when smoothing or remeshing fails;
- any STEP reconstruction with its generator, assumptions, unit convention, and
  round-trip result;
- a static preview plus simple viewing instructions for an installed local 3D
  tool such as Blender, MeshLab, FreeCAD, or the target CAD system.

Do not publish source or derived project geometry merely because the reusable
skill is public.
