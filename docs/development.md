# Development Guide

## Environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m pip install -r requirements-dev.txt
```

The package uses the `src` layout, targets Python 3.11 or newer, and exposes
`smart-doc-tracker` through `smart_doc_tracker.main:run` plus `smart-doc-tracker-web`
through `smart_doc_tracker.web.app:run`.

## Repository layout

```text
src/smart_doc_tracker/
|-- cli/                 # arguments, dependency container, JSON serialization
|-- controllers/         # CLI use-case coordination
|-- core/                # OCR, PDF, hashing, parsing
|-- db/                  # MongoDB and ChromaDB adapters
|-- infrastructure/      # local Ollama transport
|-- interfaces/          # typed protocols
|-- models/              # domain and RAG models
|-- notifier/            # local notification adapter
|-- web/                 # FastAPI routes, durable jobs, templates, static assets
|-- inbox.py             # local file discovery and archiving
|-- mutation_pipeline.py # coordinated MongoDB/ChromaDB mutations
|-- pipeline.py          # cross-component workflows
`-- scheduler.py         # daily scheduling
```

## Adding behavior

Start from a domain or application use case. Define the smallest interface required
by that use case, implement infrastructure behind it, inject the dependency, and keep
presentation logic in the CLI or FastAPI adapter.

Examples:

- a new OCR implementation implements `OCRExtractor` and does not parse fields;
- a new repository implements `DocumentRepository` and does not notify users;
- a new notifier receives prepared, privacy-safe notification content;
- error recovery and cross-stage sequencing belong in a pipeline;
- validation belongs in domain or request models before persistence.

Avoid shared mutable globals. Constructors and factories should make local service
choices explicit and test-replaceable.

## Privacy review

For every dependency or code path, verify:

- whether it opens a socket or downloads data automatically;
- whether it sends telemetry or performs update checks;
- whether it logs arguments, prompts, responses, filenames, or payloads;
- where it creates temporary files and how they are cleaned after failure;
- whether a URL can resolve outside loopback;
- whether test fixtures contain realistic personal information.

Dependencies with hidden remote behavior are not acceptable. Local-only endpoints
must fail closed.

## FastAPI development

The web adapter depends on shared typed services, not CLI subprocesses. Keep route
functions focused on HTTP parsing and response mapping; business sequencing belongs
in processing or mutation services.

Blocking OCR, PyMuPDF, Ollama, MongoDB, and Chroma work must remain behind bounded
execution. `async def` alone does not make blocking work asynchronous. The current
single-process design uses one upload worker and one index-refresh worker.

Upload sources and metadata are persisted under `data/processing_queue`, review data
under `data/pending_confirmation`, and refresh metadata under
`data/index_update_queue`. Preserve atomic manifest replacement, sanitized public
errors, explicit confirmation, restart recovery, and deterministic cleanup when
changing these workflows. Pending manifests intentionally contain sensitive raw and
structured content; job and refresh manifests must not.

Next priorities are decoded-content validation, explicit browser security controls,
bulk reconciliation/reindexing, and a documented archived-source deletion policy.
Do not run more than one web process until cross-process job claiming and concurrent
store/index/delete rules are designed and tested.

## Documentation changes

Update the README for capability-level changes, the user or operations guide for new
procedures, the data model for persistence changes, and the changelog for user-visible
behavior. Add an ADR for decisions that are expensive to reverse.

After changing a public class, function, method, model field, or protocol, regenerate
the compact agent API index without importing application modules:

```powershell
.venv\Scripts\python.exe scripts\generate_agent_reference.py
```

Keep planned behavior clearly marked until tests verify its implementation.

## Quality commands

```powershell
.venv\Scripts\python.exe -m ruff format --check .
.venv\Scripts\python.exe -m ruff check .
.venv\Scripts\python.exe -m mypy
.venv\Scripts\python.exe -m pytest --cov --cov-report=term-missing
```

Use `ruff format .` only for intentional formatting changes. See
[Testing](testing.md) and [Contributing](../CONTRIBUTING.md) for acceptance criteria.

## Releases

Before a release:

1. run the full offline quality suite;
2. review dependency and container changes;
3. verify documentation against `--help` and actual behavior;
4. add the release section and date to `CHANGELOG.md`;
5. update the package version consistently;
6. verify backup and migration instructions;
7. tag the exact reviewed commit.

Replace placeholder repository links and the security contact before publishing the
project outside its current organization.
