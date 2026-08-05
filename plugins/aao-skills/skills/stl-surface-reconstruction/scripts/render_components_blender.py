#!/usr/bin/env python3
"""Render disconnected STL components in different colours with Blender.

Run as:
    blender -b --python render_components_blender.py -- input.stl output_dir
"""

from __future__ import annotations

import sys
from pathlib import Path

import bpy
from mathutils import Vector


def arguments() -> tuple[Path, Path]:
    try:
        marker = sys.argv.index("--")
        source, output = sys.argv[marker + 1 : marker + 3]
    except (ValueError, IndexError):
        raise SystemExit("usage: blender -b --python SCRIPT -- INPUT.stl OUTPUT_DIR")
    return Path(source).resolve(), Path(output).resolve()


def import_stl(path: Path):
    try:
        bpy.ops.wm.stl_import(filepath=str(path))
    except (AttributeError, RuntimeError):
        bpy.ops.import_mesh.stl(filepath=str(path))
    return bpy.context.active_object


def material(name: str, colour: tuple[float, float, float, float]):
    result = bpy.data.materials.new(name)
    result.diffuse_color = colour
    return result


def look_at(camera, target: Vector) -> None:
    direction = target - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def render_view(
    scene,
    camera,
    centre: Vector,
    span: float,
    output_dir: Path,
    name: str,
    direction: tuple[float, float, float],
) -> None:
    unit = Vector(direction).normalized()
    camera.location = centre + unit * span * 3.0
    look_at(camera, centre)
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = span * 1.18
    scene.render.filepath = str(output_dir / f"components-{name}.png")
    bpy.ops.render.render(write_still=True)


def main() -> None:
    source, output_dir = arguments()
    output_dir.mkdir(parents=True, exist_ok=True)

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    imported = import_stl(source)

    bpy.context.view_layer.objects.active = imported
    imported.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.separate(type="LOOSE")
    bpy.ops.object.mode_set(mode="OBJECT")

    objects = [obj for obj in bpy.context.selected_objects if obj.type == "MESH"]
    objects.sort(key=lambda obj: len(obj.data.polygons), reverse=True)
    if not objects:
        raise RuntimeError(f"no mesh objects imported from {source}")

    main_material = material("largest-component", (0.08, 0.35, 0.75, 1.0))
    fragment_material = material("other-components", (0.85, 0.08, 0.04, 1.0))
    for index, obj in enumerate(objects):
        obj.name = f"component-{index:02d}-{len(obj.data.polygons)}-triangles"
        obj.data.materials.clear()
        obj.data.materials.append(main_material if index == 0 else fragment_material)

    corners = []
    for obj in objects:
        corners.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    minimum = Vector(tuple(min(c[i] for c in corners) for i in range(3)))
    maximum = Vector(tuple(max(c[i] for c in corners) for i in range(3)))
    centre = (minimum + maximum) / 2.0
    span = max(maximum - minimum)

    bpy.ops.object.camera_add()
    camera = bpy.context.object
    scene = bpy.context.scene
    scene.camera = camera
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

    views = {
        "isometric": (1.6, -1.8, 1.2),
        "top": (0.0, 0.0, 1.0),
        "front": (0.0, -1.0, 0.0),
        "side": (1.0, 0.0, 0.0),
    }
    for name, direction in views.items():
        render_view(scene, camera, centre, span, output_dir, name, direction)

    bpy.ops.wm.save_as_mainfile(filepath=str(output_dir / "components-review.blend"))


if __name__ == "__main__":
    main()
