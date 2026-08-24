from __future__ import annotations

import tomllib
from pathlib import Path
from unittest import TestCase

import smart_doc_tracker

PROJECT_ROOT = Path(__file__).resolve().parents[1]


class PackagingTests(TestCase):
    """Verify the installable package and its canonical namespace."""

    def test_project_exposes_the_canonical_package(self) -> None:
        """Import the package only through the public project namespace."""
        package_path = Path(smart_doc_tracker.__file__).resolve()

        self.assertEqual(smart_doc_tracker.__version__, "0.1.0")
        self.assertEqual(package_path.parent.name, "smart_doc_tracker")

    def test_pyproject_declares_the_console_entry_point(self) -> None:
        """Keep the installed command tied to the package entry point."""
        configuration = tomllib.loads(
            (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        )

        self.assertEqual(
            configuration["project"]["scripts"]["smart-doc-tracker"],
            "smart_doc_tracker.main:run",
        )
        self.assertEqual(
            configuration["tool"]["setuptools"]["packages"]["find"]["include"],
            ["smart_doc_tracker*"],
        )
