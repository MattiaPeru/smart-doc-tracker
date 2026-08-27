# Agent Repository Guide

Use this directory as the first navigation layer for Smart Doc Tracker. It describes
the stable boundaries of the codebase without requiring a full source-tree scan.

## Reading order

1. Read [Architecture](ARCHITECTURE.md) to locate the responsible package.
2. Read [Workflows](WORKFLOWS.md) when a change crosses component boundaries.
3. Search [Public API Reference](PUBLIC_API.md) for exact public signatures.
4. Open only the implementation modules and focused tests relevant to the task.

The reference is an index, not a substitute for source inspection. Behavioral fixes,
security reviews, and implementation changes still require reading the affected code
and tests.

## Keeping the reference current

Run this command after changing a public class, function, method, model field, or
protocol:

```powershell
.venv\Scripts\python.exe scripts\generate_agent_reference.py
```

The generator uses Python's standard-library AST parser. It does not import project
modules, connect to local services, read documents, or make network requests. A test
fails when the committed reference is stale.

The broader human-facing design documentation remains in [Architecture](../architecture.md),
[Data model](../data-model.md), and the architecture decision records in `docs/adr/`.
