#!/usr/bin/env python3
"""Directly decimate an STL and measure sampled bidirectional deviation.

Run as:
    blender -b --python reduce_and_measure_blender.py -- \
      input.stl output.stl report.json target_faces [preview.png]
"""

from __future__ import annotations

import json
import math
import statistics
import sys
from pathlib import Path

import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree


def arguments() -> tuple[Path, Path, Path, int, Path | None]:
    try:
        marker = sys.argv.index("--")
        values = sys.argv[marker + 1 :]
        source, output, report, target = values[:4]
        preview = Path(values[4]).resolve() if len(values) > 4 else None
    except (ValueError, IndexError):
        raise SystemExit(
            "usage: blender -b --python SCRIPT -- "
            "INPUT.stl OUTPUT.stl REPORT.json TARGET_FACES [PREVIEW.png]"
        )
    target_faces = int(target)
    if target_faces < 4:
        raise SystemExit("TARGET_FACES must be at least 4")
    return (
        Path(source).resolve(),
        Path(output).resolve(),
        Path(report).resolve(),
        target_faces,
        preview,
    )


def import_stl(path: Path):
    try:
        bpy.ops.wm.stl_import(filepath=str(path))
    except (AttributeError, RuntimeError):
        bpy.ops.import_mesh.stl(filepath=str(path))
    return bpy.context.active_object


def active_only(obj) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def export_stl(obj, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    active_only(obj)
    try:
        bpy.ops.wm.stl_export(
            filepath=str(path),
            export_selected_objects=True,
            ascii_format=False,
        )
    except (AttributeError, RuntimeError):
        bpy.ops.export_mesh.stl(filepath=str(path), use_selection=True, ascii=False)


def build_bvh(obj) -> BVHTree:
    vertices = [vertex.co.copy() for vertex in obj.data.vertices]
    polygons = [tuple(polygon.vertices) for polygon in obj.data.polygons]
    return BVHTree.FromPolygons(vertices, polygons, all_triangles=False)


def sampled_points(obj, maximum_vertices: int = 25000, maximum_faces: int = 25000):
    vertices = obj.data.vertices
    vertex_step = max(1, math.ceil(len(vertices) / maximum_vertices))
    for index in range(0, len(vertices), vertex_step):
        yield vertices[index].co.copy()
    polygons = obj.data.polygons
    face_step = max(1, math.ceil(len(polygons) / maximum_faces))
    for index in range(0, len(polygons), face_step):
        yield polygons[index].center.copy()


def nearest_distances(points, bvh: BVHTree) -> list[float]:
    distances = []
    for point in points:
        nearest = bvh.find_nearest(point)
        if nearest is not None:
            distances.append(float(nearest[3]))
    return distances


def summarise(distances: list[float]) -> dict[str, float | int]:
    ordered = sorted(distances)
    if not ordered:
        raise RuntimeError("surface-distance sampling returned no points")

    def percentile(fraction: float) -> float:
        position = fraction * (len(ordered) - 1)
        lower = math.floor(position)
        upper = math.ceil(position)
        if lower == upper:
            return ordered[lower]
        weight = position - lower
        return ordered[lower] * (1.0 - weight) + ordered[upper] * weight

    return {
        "samples": len(ordered),
        "mean": statistics.fmean(ordered),
        "rms": math.sqrt(statistics.fmean(value * value for value in ordered)),
        "median": percentile(0.5),
        "p95": percentile(0.95),
        "p99": percentile(0.99),
        "maximum": ordered[-1],
    }


def surface_deviation(reference, candidate) -> dict:
    reference_bvh = build_bvh(reference)
    candidate_bvh = build_bvh(candidate)
    reference_to_candidate = nearest_distances(
        sampled_points(reference), candidate_bvh
    )
    candidate_to_reference = nearest_distances(
        sampled_points(candidate), reference_bvh
    )
    maximum = max(max(reference_to_candidate), max(candidate_to_reference))
    return {
        "reference_to_candidate": summarise(reference_to_candidate),
        "candidate_to_reference": summarise(candidate_to_reference),
        "sampled_symmetric_hausdorff": maximum,
    }


def look_at(camera, target: Vector) -> None:
    camera.rotation_euler = (target - camera.location).to_track_quat("-Z", "Y").to_euler()


def render_candidate(candidate, output: Path, centre: Vector, span: float) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    for obj in [item for item in scene.objects if item.type == "MESH"]:
        obj.hide_render = obj != candidate

    material = bpy.data.materials.new("candidate-blue")
    material.diffuse_color = (0.08, 0.35, 0.75, 1.0)
    candidate.data.materials.clear()
    candidate.data.materials.append(material)

    bpy.ops.object.camera_add()
    camera = bpy.context.object
    scene.camera = camera
    camera.location = centre + Vector((1.6, -1.8, 1.2)).normalized() * span * 3.0
    look_at(camera, centre)
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = span * 1.18

    scene.render.engine = "BLENDER_WORKBENCH"
    scene.display.shading.light = "STUDIO"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "WORLD"
    scene.display.shading.color_type = "MATERIAL"
    scene.render.resolution_x = 1200
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.world.color = (0.92, 0.92, 0.92)
    scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)


def main() -> None:
    source, output, report_path, target_faces, preview = arguments()
    report_path.parent.mkdir(parents=True, exist_ok=True)

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    reference = import_stl(source)
    reference.name = "reference"
    reference_faces = len(reference.data.polygons)
    reference_vertices = len(reference.data.vertices)

    candidate = reference.copy()
    candidate.data = reference.data.copy()
    candidate.name = f"direct-decimation-target-{target_faces}"
    bpy.context.collection.objects.link(candidate)
    if target_faces < reference_faces:
        modifier = candidate.modifiers.new("quadric-edge-collapse", "DECIMATE")
        modifier.decimate_type = "COLLAPSE"
        modifier.ratio = target_faces / reference_faces
        modifier.use_collapse_triangulate = True
        active_only(candidate)
        bpy.ops.object.modifier_apply(modifier=modifier.name)

    deviation = surface_deviation(reference, candidate)
    corners = [reference.matrix_world @ Vector(corner) for corner in reference.bound_box]
    minimum = Vector(tuple(min(c[i] for c in corners) for i in range(3)))
    maximum = Vector(tuple(max(c[i] for c in corners) for i in range(3)))
    centre = (minimum + maximum) / 2.0
    span = max(maximum - minimum)
    diagonal = (maximum - minimum).length

    export_stl(candidate, output)
    if preview:
        render_candidate(candidate, preview, centre, span)

    report = {
        "source": source.name,
        "output": output.name,
        "coordinate_units": "unknown unless confirmed outside STL",
        "method": "Blender Decimate quadric edge collapse without smoothing",
        "target_faces": target_faces,
        "reference_faces_after_import": reference_faces,
        "reference_vertices_after_import": reference_vertices,
        "output_polygons_before_stl_export": len(candidate.data.polygons),
        "output_vertices_before_stl_export": len(candidate.data.vertices),
        "bounding_box_diagonal_mesh_units": diagonal,
        "surface_deviation_mesh_units": deviation,
        "sampled_symmetric_hausdorff_percent_of_bbox_diagonal": (
            100.0 * deviation["sampled_symmetric_hausdorff"] / diagonal
        ),
        "warning": (
            "Distances are deterministic sampled bidirectional nearest-surface "
            "estimates, not exact Hausdorff distances. Re-run component and edge "
            "checks on the exported STL."
        ),
    }
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
