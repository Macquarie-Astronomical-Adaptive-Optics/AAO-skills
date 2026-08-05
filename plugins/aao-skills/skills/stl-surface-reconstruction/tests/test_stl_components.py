from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np


SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = SKILL_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import stl_components as stl  # noqa: E402


def triangle_array(faces) -> np.ndarray:
    result = np.zeros(len(faces), dtype=stl.TRIANGLE_DTYPE)
    result["vertices"] = np.asarray(faces, dtype="<f4")
    return result


class StlComponentsTests(unittest.TestCase):
    def test_cli_keeps_largest_and_removes_bad_faces(self) -> None:
        a = (0.0, 0.0, 0.0)
        b = (1.0, 0.0, 0.0)
        c = (0.0, 1.0, 0.0)
        d = (0.0, 0.0, 1.0)
        fragment = ((10.0, 0.0, 0.0), (11.0, 0.0, 0.0), (10.0, 1.0, 0.0))
        faces = [
            (a, c, b),
            (a, b, d),
            (b, c, d),
            (c, a, d),
            (a, c, b),  # duplicate
            (a, a, b),  # degenerate
            fragment,
        ]

        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            source = directory / "source.stl"
            cleaned = directory / "cleaned.stl"
            report_path = directory / "report.json"
            stl.write_binary_stl(source, triangle_array(faces), "synthetic test")

            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS_DIR / "stl_components.py"),
                    str(source),
                    "--report",
                    str(report_path),
                    "--keep-largest",
                    str(cleaned),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
            )

            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["connected_components"], 2)
            self.assertEqual(report["duplicate_triangles_ignoring_winding"], 1)
            self.assertEqual(report["components"][0]["triangles"], 6)
            self.assertEqual(report["components"][1]["triangles"], 1)
            self.assertEqual(
                report["cleaned_output"]["triangles_before_face_cleanup"], 6
            )
            self.assertEqual(
                report["cleaned_output"]["triangles_after_face_cleanup"], 4
            )

            _, _, cleaned_triangles = stl.read_stl(cleaned)
            cleaned_report, _, _ = stl.analyse(cleaned_triangles)
            self.assertEqual(cleaned_report["connected_components"], 1)
            self.assertEqual(cleaned_report["triangles"], 4)
            self.assertEqual(cleaned_report["degenerate_triangles"], 0)
            self.assertEqual(
                cleaned_report["duplicate_triangles_ignoring_winding"], 0
            )
            self.assertEqual(
                cleaned_report["edge_incidence"]["boundary_incidence_1"], 0
            )

    def test_reads_ascii_stl(self) -> None:
        source_text = """solid example
facet normal 0 0 1
  outer loop
    vertex 0 0 0
    vertex 1 0 0
    vertex 0 1 0
  endloop
endfacet
endsolid example
"""
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "source-ascii.stl"
            source.write_text(source_text, encoding="utf-8")
            source_format, header, triangles = stl.read_stl(source)
            self.assertEqual(source_format, "ASCII STL")
            self.assertEqual(header, "solid example")
            self.assertEqual(len(triangles), 1)
            report, _, _ = stl.analyse(triangles)
            self.assertEqual(report["triangles"], 1)
            self.assertEqual(report["connected_components"], 1)


if __name__ == "__main__":
    unittest.main()
