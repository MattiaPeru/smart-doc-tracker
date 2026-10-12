from __future__ import annotations

import ast
from pathlib import Path
from unittest import TestCase


class SourceDocstringTests(TestCase):
    """Enforce concise documentation for every source function and method."""

    def test_every_source_function_has_a_docstring(self) -> None:
        """Report every source function or method missing a docstring."""
        source_root = Path(__file__).resolve().parents[1] / "src"
        missing: list[str] = []

        for source_path in sorted(source_root.rglob("*.py")):
            module = ast.parse(source_path.read_text(encoding="utf-8"))
            for node in ast.walk(module):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if ast.get_docstring(node) is None:
                        relative_path = source_path.relative_to(source_root.parent)
                        missing.append(f"{relative_path}:{node.lineno} ({node.name})")

        self.assertEqual(
            missing, [], "Missing function docstrings:\n" + "\n".join(missing)
        )
