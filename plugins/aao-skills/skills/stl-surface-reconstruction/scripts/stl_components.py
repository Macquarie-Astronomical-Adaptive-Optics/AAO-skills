#!/usr/bin/env python3
"""Inventory STL components and optionally retain only the largest component."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components


TRIANGLE_DTYPE = np.dtype(
    [
        ("normal", "<f4", (3,)),
        ("vertices", "<f4", (3, 3)),
        ("attribute", "<u2"),
    ]
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _looks_binary(path: Path) -> bool:
    if path.stat().st_size < 84:
        return False
    with path.open("rb") as stream:
        stream.seek(80)
        count_bytes = stream.read(4)
    if len(count_bytes) != 4:
        return False
    declared = struct.unpack("<I", count_bytes)[0]
    return path.stat().st_size == 84 + declared * TRIANGLE_DTYPE.itemsize


def read_stl(path: Path) -> tuple[str, str, np.ndarray]:
    if _looks_binary(path):
        with path.open("rb") as stream:
            header = stream.read(80)
            declared = struct.unpack("<I", stream.read(4))[0]
            triangles = np.fromfile(stream, dtype=TRIANGLE_DTYPE, count=declared)
        if len(triangles) != declared:
            raise ValueError(
                f"{path}: declares {declared} triangles but contains {len(triangles)}"
            )
        description = header.rstrip(b"\0").decode("ascii", "replace")
        return "binary STL", description, triangles

    vertices = []
    with path.open("r", encoding="utf-8", errors="replace") as stream:
        first_line = stream.readline().strip()
        for line_number, line in enumerate(stream, start=2):
            words = line.strip().split()
            if words and words[0].lower() == "vertex":
                if len(words) != 4:
                    raise ValueError(f"{path}:{line_number}: malformed vertex line")
                vertices.append(tuple(float(value) for value in words[1:]))
    if not vertices or len(vertices) % 3:
        raise ValueError(f"{path}: not a supported binary or ASCII STL")
    triangles = np.zeros(len(vertices) // 3, dtype=TRIANGLE_DTYPE)
    triangles["vertices"] = np.asarray(vertices, dtype="<f4").reshape(-1, 3, 3)
    _, normals = triangle_geometry(triangles["vertices"].astype(np.float64))
    triangles["normal"] = normals.astype("<f4")
    return "ASCII STL", first_line, triangles


def component_labels(vertices: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    points, inverse = np.unique(vertices.reshape(-1, 3), axis=0, return_inverse=True)
    faces = inverse.reshape(-1, 3)
    edges = np.vstack(
        (faces[:, [0, 1]], faces[:, [1, 2]], faces[:, [2, 0]])
    )
    rows = np.concatenate((edges[:, 0], edges[:, 1]))
    columns = np.concatenate((edges[:, 1], edges[:, 0]))
    graph = coo_matrix(
        (np.ones(len(rows), dtype=np.uint8), (rows, columns)),
        shape=(len(points), len(points)),
    ).tocsr()
    _, vertex_labels = connected_components(graph, directed=False)
    return points, faces, vertex_labels


def triangle_geometry(vertices: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    cross = np.cross(vertices[:, 1] - vertices[:, 0], vertices[:, 2] - vertices[:, 0])
    doubled_area = np.linalg.norm(cross, axis=1)
    normals = np.divide(
        cross,
        doubled_area[:, None],
        out=np.zeros_like(cross),
        where=doubled_area[:, None] > 0,
    )
    return doubled_area * 0.5, normals


def edge_statistics(faces: np.ndarray) -> dict[str, int]:
    edges = np.sort(
        np.vstack((faces[:, [0, 1]], faces[:, [1, 2]], faces[:, [2, 0]])),
        axis=1,
    )
    _, incidences = np.unique(edges, axis=0, return_counts=True)
    return {
        "unique": int(len(incidences)),
        "boundary_incidence_1": int(np.count_nonzero(incidences == 1)),
        "manifold_incidence_2": int(np.count_nonzero(incidences == 2)),
        "nonmanifold_incidence_gt_2": int(np.count_nonzero(incidences > 2)),
        "maximum_incidence": int(incidences.max(initial=0)),
    }


def analyse(triangles: np.ndarray) -> tuple[dict, np.ndarray, np.ndarray]:
    if not len(triangles):
        raise ValueError("cannot analyse an STL with no triangles")
    vertices = triangles["vertices"].astype(np.float64)
    points, faces, vertex_labels = component_labels(vertices)
    face_labels = vertex_labels[faces[:, 0]]
    number_of_components = int(vertex_labels.max(initial=-1)) + 1
    areas, _ = triangle_geometry(vertices)
    face_counts = np.bincount(face_labels, minlength=number_of_components)
    vertex_counts = np.bincount(vertex_labels, minlength=number_of_components)
    component_areas = np.bincount(
        face_labels, weights=areas, minlength=number_of_components
    )
    order = np.argsort(-face_counts)

    components = []
    for rank, component_id in enumerate(order):
        component_points = points[vertex_labels == component_id]
        component_faces = faces[face_labels == component_id]
        components.append(
            {
                "rank_by_triangle_count": rank,
                "component_id": int(component_id),
                "triangles": int(face_counts[component_id]),
                "unique_vertices": int(vertex_counts[component_id]),
                "surface_area": float(component_areas[component_id]),
                "bounds_min": component_points.min(axis=0).tolist(),
                "bounds_max": component_points.max(axis=0).tolist(),
                "edge_incidence": edge_statistics(component_faces),
            }
        )

    edge_lengths = np.linalg.norm(
        vertices[:, [1, 2, 0], :] - vertices[:, [0, 1, 2], :], axis=2
    ).reshape(-1)
    face_keys = np.sort(faces, axis=1)
    duplicate_triangles = len(face_keys) - len(np.unique(face_keys, axis=0))
    report = {
        "triangles": int(len(triangles)),
        "raw_triangle_vertices": int(vertices.shape[0] * 3),
        "unique_vertices_exact": int(len(points)),
        "bounds_min": points.min(axis=0).tolist(),
        "bounds_max": points.max(axis=0).tolist(),
        "bounds_size": np.ptp(points, axis=0).tolist(),
        "bounding_box_diagonal": float(np.linalg.norm(np.ptp(points, axis=0))),
        "surface_area": float(areas.sum()),
        "degenerate_triangles": int(
            np.count_nonzero(areas <= np.finfo(np.float32).eps)
        ),
        "duplicate_triangles_ignoring_winding": int(duplicate_triangles),
        "triangle_area_percentiles": dict(
            zip(
                ("minimum", "p01", "p05", "median", "p95", "p99", "maximum"),
                np.percentile(areas, (0, 1, 5, 50, 95, 99, 100)).tolist(),
            )
        ),
        "edge_length_percentiles": dict(
            zip(
                ("minimum", "p01", "p05", "median", "p95", "p99", "maximum"),
                np.percentile(edge_lengths, (0, 1, 5, 50, 95, 99, 100)).tolist(),
            )
        ),
        "connected_components": number_of_components,
        "component_connectivity_rule": "exact shared vertex coordinates",
        "components": components,
        "edge_incidence": edge_statistics(faces),
    }
    return report, face_labels, order


def remove_degenerate_and_duplicate_triangles(triangles: np.ndarray) -> np.ndarray:
    vertices = triangles["vertices"].astype(np.float64)
    areas, _ = triangle_geometry(vertices)
    candidates = triangles[areas > np.finfo(np.float32).eps]
    if not len(candidates):
        return candidates
    _, inverse = np.unique(
        candidates["vertices"].reshape(-1, 3), axis=0, return_inverse=True
    )
    keys = np.sort(inverse.reshape(-1, 3), axis=1)
    _, first = np.unique(keys, axis=0, return_index=True)
    return candidates[np.sort(first)]


def write_binary_stl(path: Path, triangles: np.ndarray, description: str) -> None:
    vertices = triangles["vertices"].astype(np.float64)
    _, normals = triangle_geometry(vertices)
    output = np.empty(len(triangles), dtype=TRIANGLE_DTYPE)
    output["normal"] = normals.astype("<f4")
    output["vertices"] = triangles["vertices"]
    output["attribute"] = 0
    header = description.encode("ascii", "replace")[:80].ljust(80, b"\0")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as stream:
        stream.write(header)
        stream.write(struct.pack("<I", len(output)))
        output.tofile(stream)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--keep-largest", type=Path, metavar="OUTPUT_STL")
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    source_format, header, triangles = read_stl(arguments.source)
    report, face_labels, order = analyse(triangles)
    report.update(
        {
            "source": arguments.source.name,
            "source_format": source_format,
            "source_header": header,
            "source_bytes": arguments.source.stat().st_size,
            "source_sha256": sha256(arguments.source),
            "coordinate_units": "unknown unless confirmed outside STL",
        }
    )

    if arguments.keep_largest:
        largest_id = int(order[0])
        selected = triangles[face_labels == largest_id]
        cleaned = remove_degenerate_and_duplicate_triangles(selected)
        write_binary_stl(
            arguments.keep_largest,
            cleaned,
            "Largest reviewed component; degenerate and duplicate faces removed",
        )
        cleaned_report, _, _ = analyse(cleaned)
        report["cleaned_output"] = {
            "path": arguments.keep_largest.name,
            "sha256": sha256(arguments.keep_largest),
            "triangles_before_face_cleanup": int(len(selected)),
            "triangles_after_face_cleanup": int(len(cleaned)),
            "analysis": cleaned_report,
        }

    rendered = json.dumps(report, indent=2, sort_keys=True)
    if arguments.report:
        arguments.report.parent.mkdir(parents=True, exist_ok=True)
        arguments.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
