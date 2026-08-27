# Contributing

Thank you for contributing to Smart Doc Tracker. Changes must preserve the local-only
privacy model and the separation between extraction, parsing, persistence,
notifications, and orchestration.

## Before starting

Open an issue or design discussion for changes that affect persisted schemas,
privacy boundaries, public CLI or HTTP behavior, or deletion semantics.
Record durable architectural choices as an ADR under `docs/adr`.

Never commit real documents, OCR text, personal information, credentials, database
dumps, model outputs derived from private documents, or populated `data` folders.

## Development setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m pip install -r requirements-dev.txt
```

External dependencies used by manual integration runs must be installed locally.
Automated tests must use fakes at service boundaries and must not require MongoDB,
ChromaDB, Ollama, Tesseract, Docker, or network access unless explicitly marked as
manual tests.

## Design rules

- Target Python 3.11 or newer.
- Keep code, identifiers, comments, docstrings, exceptions, and logs in English.
- Use small typed interfaces and explicit dependency injection.
- Keep domain models independent from infrastructure adapters.
- Validate extracted or user-edited values before persistence.
- Do not add remote APIs, telemetry, analytics, hosted models, or remote storage.
- Accept local services only through validated loopback endpoints.
- Do not log document contents or sensitive fields.
- Clean temporary files deterministically, including after exceptions.
- Keep the CLI and FastAPI adapter thin; business workflows belong in
  application pipelines or controllers.

The web application must not call CLI commands as subprocesses. It invokes typed
application services directly. Keep long-running OCR, parsing, and indexing behind
explicit durable job state and bounded local concurrency; do not add additional web
workers without a tested cross-process claiming design.

## Quality checks

Run all checks before submitting a change:

```powershell
.venv\Scripts\python.exe -m ruff format --check .
.venv\Scripts\python.exe -m ruff check .
.venv\Scripts\python.exe -m mypy
.venv\Scripts\python.exe -m pytest --cov --cov-report=term-missing
```

Add focused tests for changed behavior. Verify failure paths, privacy properties,
validation, cleanup, and cross-store consistency where relevant. Branch coverage
must remain at or above 80%.

## Pull requests

A pull request should contain:

- a concise description of behavior and motivation;
- tests for the changed behavior;
- documentation and changelog updates when user-visible behavior changes;
- an ADR or migration plan for durable architecture or schema changes;
- confirmation that no sensitive fixtures or generated data are included.

Keep commits focused. Do not mix unrelated formatting, dependency, and behavior
changes. Reviewers must pay particular attention to outbound connections, logging,
filesystem paths, database migrations, and deletion behavior.
