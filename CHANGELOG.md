# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project intends to follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned

- A loopback-only FastAPI web application.
- Asynchronous document upload and processing with visible job status.
- Document browsing and validated search from the web interface.
- In-application expiration notifications.
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
