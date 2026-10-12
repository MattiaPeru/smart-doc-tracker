from __future__ import annotations

import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "generate_agent_reference.py"
SPEC = importlib.util.spec_from_file_location("agent_reference_generator", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generator)


class AgentReferenceGeneratorTests(TestCase):
    """Verify safe and deterministic public API reference generation."""

    def test_renders_public_api_without_importing_source_modules(self) -> None:
        """Parse signatures without executing module-level code or private objects."""
        with TemporaryDirectory() as directory:
            source_root = Path(directory) / "sample_package"
            source_root.mkdir()
            (source_root / "module.py").write_text(
                '''"""Sample module."""
raise RuntimeError("This module must not be imported")

class Service:
    """Perform local work."""
    location: str

    def run(self, value: int, *, enabled: bool = True) -> str:
        """Return a prepared value."""
        raise NotImplementedError

    def _private_method(self) -> None:
        raise NotImplementedError

def public_function(source: str | None = None) -> bool:
    """Inspect one source."""
    return source is not None

def _private_function() -> None:
    raise NotImplementedError
''',
                encoding="utf-8",
            )

            first = generator.render_reference(source_root)
            second = generator.render_reference(source_root)

        self.assertEqual(first, second)
        self.assertIn("`sample_package.module`", first)
        self.assertIn("`location: str`", first)
        self.assertIn("`run(self, value: int, *, enabled: bool = True) -> str`", first)
        self.assertIn("`public_function(source: str | None = None) -> bool`", first)
        self.assertNotIn("private_method", first)
        self.assertNotIn("private_function", first)

    def test_committed_reference_matches_the_current_public_api(self) -> None:
        """Require regeneration whenever the source public surface changes."""
        source_root = PROJECT_ROOT / "src" / "smart_doc_tracker"
        reference_path = PROJECT_ROOT / "docs" / "agent" / "PUBLIC_API.md"

        self.assertEqual(
            reference_path.read_text(encoding="utf-8"),
            generator.render_reference(source_root),
            "Run scripts/generate_agent_reference.py to refresh PUBLIC_API.md",
        )
