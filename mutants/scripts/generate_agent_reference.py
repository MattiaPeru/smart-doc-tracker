"""Generate a compact public API reference without importing project modules."""

from __future__ import annotations

import argparse
import ast
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_ROOT = PROJECT_ROOT / "src" / "smart_doc_tracker"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "docs" / "agent" / "PUBLIC_API.md"
PUBLIC_DUNDER_METHODS = frozenset({"__enter__", "__exit__", "__init__"})


def _is_public(name: str) -> bool:
    """Return whether a name belongs in the generated public reference."""
    return not name.startswith("_") or name in PUBLIC_DUNDER_METHODS


def _annotation(node: ast.expr) -> str:
    """Render one annotation while preserving its source-level meaning."""
    return ast.unparse(node)


def _parameter(argument: ast.arg) -> str:
    """Render a parameter name and its annotation when one was declared."""
    annotation = (
        f": {_annotation(argument.annotation)}"
        if argument.annotation is not None
        else ""
    )
    return f"{argument.arg}{annotation}"


def _default(node: ast.expr | None) -> str:
    """Render one default value for a callable signature."""
    return f" = {ast.unparse(node)}" if node is not None else ""


def _format_arguments(arguments: ast.arguments) -> str:
    """Render Python arguments, including positional-only and keyword-only markers."""
    rendered: list[str] = []
    positional = [*arguments.posonlyargs, *arguments.args]
    defaults: list[ast.expr | None] = [None] * (
        len(positional) - len(arguments.defaults)
    ) + list(arguments.defaults)

    for index, (argument, default) in enumerate(zip(positional, defaults, strict=True)):
        rendered.append(f"{_parameter(argument)}{_default(default)}")
        if arguments.posonlyargs and index + 1 == len(arguments.posonlyargs):
            rendered.append("/")

    if arguments.vararg is not None:
        rendered.append(f"*{_parameter(arguments.vararg)}")
    elif arguments.kwonlyargs:
        rendered.append("*")

    for argument, default in zip(
        arguments.kwonlyargs, arguments.kw_defaults, strict=True
    ):
        rendered.append(f"{_parameter(argument)}{_default(default)}")

    if arguments.kwarg is not None:
        rendered.append(f"**{_parameter(arguments.kwarg)}")
    return ", ".join(rendered)


def _summary(node: ast.AST) -> str | None:
    """Return the first non-empty line of an object's docstring."""
    docstring = ast.get_docstring(node, clean=True)
    if docstring is None:
        return None
    return next((line.strip() for line in docstring.splitlines() if line.strip()), None)


def _function_signature(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> str:
    """Render a public function or method signature."""
    prefix = "async " if isinstance(node, ast.AsyncFunctionDef) else ""
    return_type = f" -> {_annotation(node.returns)}" if node.returns is not None else ""
    return f"{prefix}{node.name}({_format_arguments(node.args)}){return_type}"


def _class_fields(node: ast.ClassDef) -> list[str]:
    """Collect public annotated fields declared directly on a class."""
    fields: list[str] = []
    for child in node.body:
        if not isinstance(child, ast.AnnAssign) or not isinstance(
            child.target, ast.Name
        ):
            continue
        if not _is_public(child.target.id):
            continue
        fields.append(
            f"{child.target.id}: {_annotation(child.annotation)}{_default(child.value)}"
        )
    return fields


def _render_class(node: ast.ClassDef) -> list[str]:
    """Render one class and its direct public surface."""
    bases = ", ".join(ast.unparse(base) for base in node.bases)
    heading = f"### `{node.name}{f'({bases})' if bases else ''}`"
    lines = [heading, ""]
    summary = _summary(node)
    if summary:
        lines.extend([summary, ""])

    fields = _class_fields(node)
    if fields:
        lines.extend(["Fields:", ""])
        lines.extend(f"- `{field}`" for field in fields)
        lines.append("")

    methods = [
        child
        for child in node.body
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
        and _is_public(child.name)
    ]
    if methods:
        lines.extend(["Methods:", ""])
        for method in methods:
            description = _summary(method)
            suffix = f" — {description}" if description else ""
            lines.append(f"- `{_function_signature(method)}`{suffix}")
        lines.append("")
    return lines


def _module_name(source_root: Path, source_path: Path) -> str:
    """Return the import-style name for a source path."""
    relative = source_path.relative_to(source_root)
    parts = list(relative.with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join([source_root.name, *parts]).rstrip(".")


def render_reference(source_root: Path) -> str:
    """Render the package's public API as deterministic Markdown."""
    source_root = source_root.resolve()
    lines = [
        "# Public API Reference",
        "",
        "<!-- Generated by scripts/generate_agent_reference.py. Do not edit. -->",
        "",
        "This file contains signatures and concise docstrings only. It is generated",
        "from the Python AST, so project modules and local services are never imported",
        "or started. Private names are intentionally omitted.",
        "",
    ]

    for source_path in sorted(source_root.rglob("*.py")):
        module = ast.parse(source_path.read_text(encoding="utf-8"), source_path)
        public_nodes = [
            node
            for node in module.body
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
            and _is_public(node.name)
        ]
        if not public_nodes:
            continue

        relative_path = (
            Path("src") / source_path.relative_to(source_root.parent)
        ).as_posix()
        lines.extend(
            [
                f"## `{_module_name(source_root, source_path)}`",
                "",
                f"Source: [`{relative_path}`](../../{relative_path})",
                "",
            ]
        )
        module_summary = _summary(module)
        if module_summary:
            lines.extend([module_summary, ""])

        for node in public_nodes:
            if isinstance(node, ast.ClassDef):
                lines.extend(_render_class(node))
                continue
            description = _summary(node)
            suffix = f" — {description}" if description else ""
            lines.extend([f"- `{_function_signature(node)}`{suffix}", ""])

    return "\n".join(lines).rstrip() + "\n"


def write_reference(source_root: Path, output_path: Path) -> None:
    """Atomically write a generated reference and clean temporary files on failure."""
    content = render_reference(source_root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with NamedTemporaryFile(
            "w",
            encoding="utf-8",
            newline="\n",
            dir=output_path.parent,
            prefix=f".{output_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_file.write(content)
            temporary_path = Path(temporary_file.name)
        os.replace(temporary_path, output_path)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def _parse_arguments() -> argparse.Namespace:
    """Parse command-line paths for reference generation."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    return parser.parse_args()


def main() -> int:
    """Generate the configured Markdown API reference."""
    arguments = _parse_arguments()
    write_reference(arguments.source_root, arguments.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
