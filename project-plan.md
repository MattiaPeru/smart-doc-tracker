# Project Plan: Smart Doc Tracker

## 1. Objective

Smart Doc Tracker is a privacy-first, single-host document manager for personal
documents such as identity records, policies, contracts, and invoices. It extracts
text locally, converts uncertain model output into validated hybrid records, stores
and searches those records locally, and tracks expiration dates without sending
document data to remote services.

The privacy boundary assumes a trusted host and local operating-system account. It
does not promise protection from a compromised machine, privileged local users, or
supply-chain threats.

## 2. Implemented stack

- Python 3.11 or newer with typed application boundaries.
- Pillow, Tesseract through `pytesseract`, and PyMuPDF for local extraction.
- Loopback-only Ollama for structured generation and embeddings.
- Pydantic for the fixed metadata envelope and recursive dynamic payload.
- Loopback-only MongoDB for authoritative validated records and PDF sections.
- Loopback-only ChromaDB for derived semantic-search fragments.
- `plyer`, APScheduler, and Windows Task Scheduler scripts for reminders.
- FastAPI, Uvicorn, Jinja, CSS, and browser JavaScript for the local dashboard.
- Pytest, Ruff, mypy, and branch coverage for the offline quality gate.

Python dependencies and console entry points are defined in `pyproject.toml`.
Docker Compose provides MongoDB and ChromaDB only; Tesseract and Ollama remain host
dependencies.

## 3. Current architecture

```text
smart_doc_tracker/
|-- cli/ and controllers/ # CLI presentation and use-case dispatch
|-- core/                 # OCR, PDF extraction, hashing, parsing
|-- models/               # validated document and RAG models
|-- interfaces/           # narrow dependency protocols
|-- db/                   # MongoDB and ChromaDB adapters
|-- infrastructure/       # loopback-only Ollama adapters
|-- notifier/             # prepared local desktop notifications
|-- web/                  # FastAPI routes, durable jobs, review UI, assets
|-- pipeline.py           # document, inbox, RAG, and expiration orchestration
|-- mutation_pipeline.py  # coordinated MongoDB/ChromaDB mutations
`-- scheduler.py          # daily foreground scheduling
```

Sensitive runtime state may exist in MongoDB and ChromaDB volumes, `data/inbox`,
`data/processed`, `data/processing_queue`, `data/pending_confirmation`, and
`data/index_update_queue`.

## 4. Delivered phases

### Phase 1: Local extraction

**Status: Implemented.**

- OCR for supported image formats.
- Page-aware PDF text extraction with local OCR fallback.
- Explicit opt-in display of raw extracted text.

### Phase 2: Validated hybrid parsing

**Status: Implemented.**

- Fixed `document_type`, `summary`, `expiry_date`, and `issue_date` envelope.
- Recursive JSON-compatible `extracted_data` with English `snake_case` keys.
- Local Ollama generation, corrective retry, normalization, and strict validation.
- Page-bounded parsing and consolidation for long PDFs.

### Phase 3: Persistence and semantic search

**Status: Implemented.**

- SHA-256 idempotent MongoDB insertion and section storage.
- Exact dynamic-field and expiration queries.
- ChromaDB indexing of raw text, summary, and structured content with explicit local
  Ollama embeddings.
- Grounded CLI questions with validated source document IDs.

### Phase 4: Automation and reminders

**Status: Implemented.**

- Isolated inbox processing and collision-safe archiving.
- One-time and daily expiration checks with minimal desktop notifications.
- Windows Scheduled Task installation and offline-safe runner scripts.

### Phase 5: Local dashboard and review workflow

**Status: Implemented for single-user loopback deployment.**

- FastAPI dashboard bound only to IPv4 or IPv6 loopback with one worker.
- 25 MB uploads, durable single-worker processing, restart recovery, and safe status.
- Explicit correction and confirmation before persistence, indexing, and archiving.
- Browsing, exact filters, expiration status, validated edits, durable metadata-index
  refreshes, and on-demand indexed-content inspection without embeddings.
- Coordinated deletion from MongoDB and the active ChromaDB collection.

## 5. Current priorities

1. Add a supported bulk reconciliation and reindex workflow.
2. Define and implement archived-source deletion and backup-retention policy.
3. Extend deletion and reconciliation across every embedding-model collection.
4. Add decoded-file signature validation and stronger browser controls such as CSRF,
   explicit host/origin checks, and restrictive security headers.
5. Add dashboard RAG questions and pagination without weakening privacy boundaries.
6. Introduce schema versioning and tested migration procedures.

## 6. Known limitations

- MongoDB and ChromaDB do not provide a shared transaction; compensation reduces but
  cannot eliminate partial-failure risk.
- CLI metadata updates do not refresh ChromaDB. Dashboard edits refresh only summary
  and structured fragments in the active collection.
- Dashboard deletion leaves archived sources, backups, and other model collections.
- The dashboard has no authentication or hardened LAN/reverse-proxy deployment mode.
- Pending-confirmation manifests contain raw extracted text and require the same host
  protection as the databases.
- Local OCR and model results can be incomplete or inaccurate and require review.
