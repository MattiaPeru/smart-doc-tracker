# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project intends to follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- On-demand display of complete per-document ChromaDB content in the local dashboard,
  excluding embeddings.
- Loopback-only FastAPI dashboard with document browsing, exact dynamic-field filters,
  expiration status, and validated editing.
- Durable single-worker upload processing with restart recovery, explicit review,
  correction, confirmation, rejection, and collision-safe source archiving.
- Durable background refresh of summary and structured ChromaDB fragments after web
  edits.
- Coordinated dashboard deletion of MongoDB documents and sections plus fragments in
  the active ChromaDB collection, with compensating rollback where possible.

### Changed

- Local parser prompts now require real JSON arrays and objects, and valid nested JSON
  containers returned as strings are normalized before validation. Incomplete
  container placeholders trigger one corrective local retry and are rejected before
  persistence if they remain invalid.

### Planned

- Natural-language document questions from the dashboard.
- Pagination and richer browsing controls.
- Browser hardening beyond the current loopback-only deployment assumption.
- Full reconciliation and reindex commands across configured embedding collections.
- Coordinated deletion from MongoDB, ChromaDB, and the managed document archive.

Planned items are not part of the current release and may change before delivery.

## [0.1.0] - 2026-08-25

### Added

- Local image OCR and page-aware PDF extraction with OCR fallback.
- Local Ollama parsing into validated hybrid document records.
- Idempotent MongoDB persistence and structured PDF sections.
- Local ChromaDB indexing and grounded document questions.
- Inbox processing and safe processed-file archiving.
- Stored-document listing, retrieval, and validated updates.
- Expiration queries, desktop reminders, foreground scheduling, and Windows
  Scheduled Task support.
- Offline deterministic tests, strict type checking, linting, and branch coverage.
