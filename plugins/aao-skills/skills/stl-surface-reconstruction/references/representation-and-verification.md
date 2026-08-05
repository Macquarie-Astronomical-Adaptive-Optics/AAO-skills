# Representation and verification guide

## Counts that are often confused

| Term | Meaning | What a small number implies |
| --- | --- | --- |
| Triangle or facet | One planar element in a mesh | A coarse faceted approximation |
| Mesh vertex | A shared triangle corner | Very few vertices retain only simple topology |
| Control point | A parameter of a spline curve or surface | The count must be stated per patch and by direction |
| Analytic surface | Plane, cylinder, cone, sphere, or torus | One surface may still have several trimmed boundaries |
| CAD face | A bounded portion of a surface | Face count differs from underlying surface count |
| Patch | One bounded analytic or spline region | Complex topology normally requires several patches |
| Feature | Hole, pocket, rib, boss, vent, or other design intent | A feature can create multiple faces and edges |

A planar face containing many circular inner boundaries can use one underlying
plane while still containing many edges and retaining many holes. State which
count is being constrained.

## Choosing the representation

Use a reduced mesh when the immediate need is visualization, collision review,
finite-element pre-processing, or manageable interchange and the original
topology should remain.

Use CAD reconstruction when downstream work needs editable dimensions,
analytic curvature, feature history, robust booleans, manufacturing drawings,
or STEP exchange. Converting every STL triangle into a B-rep face does not
recover design intent and is not a useful smooth-surface conversion.

Use an envelope or selected-subsystem model when the requested parameter count
cannot represent the complete topology. Preserve the complete reduced mesh as a
reference and label what the low-parameter model omits.

## Fidelity measurements

Measure in both directions:

- reference samples to the candidate surface detect candidate shrinkage,
  bridging, and missing regions;
- candidate samples to the reference surface detect bulges, new surfaces, and
  smoothing excursions.

Report sample count, mean, RMS, median, p95, p99, sampled maximum, source bounds,
and sampled maximum divided by the bounding-box diagonal. A sampled maximum is
not an exact Hausdorff distance.

Distance alone is insufficient. Also inspect:

- component count and intentional separations;
- boundary and non-manifold edge incidence;
- holes, vents, thin walls, and narrow passages;
- symmetry and repeated-feature spacing;
- sharp edges, fillets, and curvature continuity;
- sign or orientation changes in face normals;
- volume only when both models are closed and consistently oriented.

## Units

STL stores coordinates but no authoritative unit metadata. Obtain the unit from
the originating CAD/solver project or a known dimension. STEP requires a unit.
If an interim STEP is necessary, use a named serialization convention such as
“one STL coordinate unit encoded as one millimetre,” include a rescaling
warning, and do not present the resulting physical dimensions as confirmed.

## CAD reconstruction evidence

For every analytic feature or spline patch, record:

- source point or triangle selection rule;
- fitted primitive or spline degree and control net;
- residual statistics and rejected outliers;
- trims, holes, and adjacency assumptions;
- inferred symmetry or nominal dimensions;
- continuity target at adjoining patches;
- whether the region is observed, inferred, replaced, or omitted.

Round-trip the exported STEP through an independent import and check validity,
face and edge counts, bounds, units, holes, and intended part count.
