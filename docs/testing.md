# Testing Guide

## Goals

Tests must establish functional behavior, validation, error policy, and local-only
privacy properties without requiring network access or real personal documents.

## Test layers

| Layer | Scope |
| --- | --- |
| Unit | Models, validators, parsers, hashing, serializers, URL checks |
| Component | Repository and adapter behavior through fakes |
| Pipeline | Cross-component sequencing, partial failures, idempotency |
| CLI | Argument validation, dispatch, output, and exit codes |
| Web | FastAPI routes, browser assets, durable jobs, and coordinated mutations |
| Script | Windows scheduling and runner safety properties |
| Manual smoke | Optional local Tesseract, Ollama, MongoDB, ChromaDB integration |

Automated tests use injected fakes and must not require Docker, Tesseract, Ollama,
MongoDB, or ChromaDB. Manual integration tests must use synthetic documents.

## Run the suite

```powershell
.venv\Scripts\python.exe -m pytest --cov --cov-report=term-missing
```

The configured coverage measurement includes branch coverage and fails below 80%.
The standard-library runner remains available:

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests -t . -v
```

Run the complete quality gate:

```powershell
.venv\Scripts\python.exe -m ruff format --check .
.venv\Scripts\python.exe -m ruff check .
.venv\Scripts\python.exe -m mypy
.venv\Scripts\python.exe -m pytest --cov --cov-report=term-missing
```

## Required test properties

Changes to ingestion must test supported and rejected inputs, empty extraction,
dependency failures, and PDF OCR fallback. Parsing changes must test malformed JSON,
duplicate keys, extra fields, date normalization, nested key validation, and missing
values.

Persistence changes must test idempotency, invalid identifiers, UTC normalization,
indexes, failed writes, invalid stored data, and deterministic ordering. Vector tests
must verify local URL validation, explicit embeddings, deterministic fragment IDs,
stale-fragment cleanup, query bounds, and malformed results.

Pipeline tests must verify stage order, dependency injection, per-file failure
isolation, archive behavior, Mongo/index partial failures, minimal notifications, and
that invalid data cannot reach persistence.

## Privacy tests

At minimum, tests should ensure that:

- remote, credential-bearing, path-bearing, and implicit-port endpoints fail closed;
- Chroma's default embedding function is disabled;
- automated paths do not print OCR text or dynamic fields;
- sensitive values do not appear in error messages;
- temporary artifacts are removed after every outcome;
- symbolic links and path escapes are rejected;
- notifications contain only approved fields;
- no automated test opens an external connection.

Use clearly synthetic fixtures such as invented policy numbers and names. Avoid
realistic tax identifiers, health data, addresses, or copied document layouts.

## FastAPI tests

The current offline web tests cover:

- loopback-only configuration and rejected public binds;
- upload size, extension, empty-file, and filename/path handling;
- typed request validation and stable sanitized errors;
- job state transitions, bounded concurrency, restart recovery, confirmation,
  rejection, and failed-job cleanup;
- browser disconnection without job loss;
- database filters that cannot inject arbitrary MongoDB operators;
- rejected external hosts, cross-origin writes, and missing CSRF proof;
- restrictive browser headers and disabled API documentation routes;
- durable metadata-only index-refresh manifests;
- metadata refresh after edits and coordinated MongoDB/Chroma deletion;
- browser rendering and on-demand indexed-content display without embeddings.

Still-required coverage before a broader deployment includes decoded-file signature
validation, authentication and authorization, cancellation, concurrent mutation
races, all-collection deletion, archived file policy, and partial-failure
reconciliation.

Use FastAPI's in-process test client or an equivalent ASGI transport. Override every
infrastructure dependency with a fake so HTTP tests remain deterministic and offline.

## Manual verification

Manual service tests are supplementary and must not replace automated tests. Run them
on a controlled host with synthetic documents, record dependency versions, and remove
all generated records, vectors, files, terminal captures, and backups afterward.

Never run destructive cleanup against broad or unresolved paths. Verify every target
is inside the designated test directory or test database first.
