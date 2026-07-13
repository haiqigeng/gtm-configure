from __future__ import annotations

import subprocess
import sys
import shutil
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReleaseChecksTest(unittest.TestCase):
    def test_release_check_passes_for_current_release(self) -> None:
        for cache in ROOT.rglob("__pycache__"):
            shutil.rmtree(cache)
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "check_release.py"),
                "--tag",
                "v2026.7.13",
                "--release-notes",
                str(ROOT / "CHANGELOG.md"),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_runtime_package_contains_only_runtime_files(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "build_skill_package.py"),
                "--output",
                str(ROOT / "dist" / "test-configure-gtm.zip"),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        archive = ROOT / "dist" / "test-configure-gtm.zip"
        self.assertTrue(archive.exists())
        self.assertNotIn(b"README.md", archive.read_bytes())


if __name__ == "__main__":
    unittest.main()
