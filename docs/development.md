# Development Guide

## Environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m pip install -r requirements-dev.txt
```

The package uses the `src` layout, targets Python 3.11 or newer, and exposes
`smart-doc-tracker` through `smart_doc_tracker.main:run`.

## Repository layout

```text
src/smart_doc_tracker/
├── cli/              # arguments, dependency container, JSON serialization
├── controllers/      # CLI use-case coordination
├── core/             # OCR, PDF, hashing, parsing
├── db/               # MongoDB and ChromaDB adapters
├── infrastructure/   # local Ollama transport
├── interfaces/       # typed protocols
├── models/           # domain and RAG models
├── notifier/         # local notification adapter
├── inbox.py          # local file discovery and archiving
├── pipeline.py       # cross-component workflows
└── scheduler.py      # daily scheduling
```

## Adding behavior

Start from a domain or application use case. Define the smallest interface required
by that use case, implement infrastructure behind it, inject the dependency, and keep
presentation logic in the CLI or planned API adapter.

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

## Planned FastAPI development

The web adapter should depend on shared application services, not on CLI controllers
or subprocess execution. Route functions should perform HTTP parsing, authorization,
and response mapping only.

Use asynchronous endpoints for efficient HTTP handling, but move blocking OCR,
PyMuPDF, Ollama, MongoDB, and Chroma work to a bounded execution layer. `async def`
alone does not make blocking work asynchronous. Define cancellation and shutdown
behavior before accepting jobs.

Recommended implementation sequence:

1. extract CLI-independent application service factories;
2. define upload, query, notification, and deletion use cases;
3. extend repository protocols with coordinated deletion and reindex support;
4. create typed API schemas that do not leak persistence objects;
5. implement a durable local job model or explicitly document prototype limits;
6. add loopback-only server configuration and browser security controls;
7. build the web UI against versioned local endpoints;
8. add end-to-end offline tests.

Do not run more than one worker until job claiming, scheduler leadership, and
concurrent store/index/delete rules are tested.

## Documentation changes

Update the README for capability-level changes, the user or operations guide for new
procedures, the data model for persistence changes, and the changelog for user-visible
behavior. Add an ADR for decisions that are expensive to reverse.

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
