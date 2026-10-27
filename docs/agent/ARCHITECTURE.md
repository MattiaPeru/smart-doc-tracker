# Agent Architecture Map

Smart Doc Tracker is an offline-first Python 3.11+ application. Dependencies point
inward toward typed domain models and narrow protocols; orchestration receives local
adapters through explicit dependency injection.

| Area | Location | Responsibility |
| --- | --- | --- |
| Domain models | `src/smart_doc_tracker/models/` | Validated document and RAG data |
| Interfaces | `src/smart_doc_tracker/interfaces/` | Narrow dependency contracts |
| OCR and parsing | `src/smart_doc_tracker/core/` | Local extraction, hashing, and parsing |
| Persistence | `src/smart_doc_tracker/db/` | MongoDB records and Chroma vector data |
| Local generation | `src/smart_doc_tracker/infrastructure/` | Loopback-only Ollama adapters |
| Orchestration | `pipeline.py`, `mutation_pipeline.py` | Cross-component sequencing and recovery |
| File lifecycle | `inbox.py` | Scan and archive local documents |
| Notifications | `src/smart_doc_tracker/notifier/` | Prepared desktop notifications |
| Use cases | `src/smart_doc_tracker/controllers/` | CLI-facing workflow coordination |
| CLI composition | `src/smart_doc_tracker/cli/`, `main.py` | Arguments, dependencies, and output |
| Web composition | `src/smart_doc_tracker/web/app.py`, `cli.py` | FastAPI dependencies, lifecycle, and local server startup |
| Web routes | `src/smart_doc_tracker/web/routes/` | HTTP adapters grouped by dashboard area |
| Web services | `src/smart_doc_tracker/web/` | Local chat, upload, confirmation, and durable job coordination |
| Scheduling | `scheduler.py` | Local daily foreground scheduling |

## Dependency boundaries

- `core.ocr` reads local images and returns raw text; it does not parse fields.
- `core.parser` converts raw text or pages into validated models.
- `db` persists and queries data; it does not orchestrate or notify.
- `notifier` accepts prepared notification data and does not receive OCR text.
- pipelines own sequencing, expected-error policy, and cross-store coordination.
- controllers and web routes translate user requests and format safe results.
- domain models must not depend on databases, HTTP, CLI, or local service clients.

All document processing remains on the host. Tesseract and PyMuPDF process files
locally; Ollama, MongoDB, ChromaDB, and FastAPI are restricted to loopback endpoints.
Do not introduce remote fallbacks, telemetry, hosted models, or cloud storage.

For detailed diagrams and deployment constraints, read
[`docs/architecture.md`](../architecture.md).
