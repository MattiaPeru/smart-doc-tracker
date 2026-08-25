# Privacy and Security

## Objective

Smart Doc Tracker is designed so sensitive document content remains on the user's
host during normal operation. This is an architectural property with explicit
assumptions, not a guarantee against every host or supply-chain threat.

## Data inventory

| Data | Location | Sensitivity |
| --- | --- | --- |
| Original documents | Inbox and processed folders | High |
| Raw OCR/PDF text | Memory and ChromaDB fragments | High |
| Structured fields and summaries | MongoDB and ChromaDB | High |
| PDF section analyses | MongoDB | High |
| Embeddings | ChromaDB | Potentially sensitive |
| Source SHA-256 hashes | MongoDB | Sensitive metadata |
| Expiration notification text | Local desktop or planned local browser UI | Moderate |
| Operational status and counts | Terminal or planned job store | Low if content-free |

Embeddings are not anonymous. They must receive the same protection as the source
content. Raw OCR text is not stored in MongoDB, but indexing deliberately stores it
in ChromaDB.

## Trust boundaries

The trusted boundary includes the local operating system account, the Python
process, Tesseract, Ollama, Docker, MongoDB, ChromaDB, their local volumes, and the
configured document folders. Loopback restricts network reachability but does not
isolate one local user or process from another.

The application currently validates MongoDB, ChromaDB, and Ollama endpoints to
require an explicit loopback host and port. Remote hosts, credentials, query strings,
fragments, and unexpected URL paths are rejected.

## Offline operation

Normal processing must not perform outbound requests, model downloads, update
checks, analytics, telemetry, or remote backups. Chroma telemetry is disabled and
the client supplies embeddings explicitly so Chroma does not download a default
embedding model.

Initial installation can require network access for Python packages, Docker images,
Tesseract packages, and Ollama models. Prepare and verify those dependencies before
disconnecting the host. The scheduled runner uses `docker compose up --pull never`
to prevent image downloads during execution.

## Sensitive output

The CLI emits stable JSON results on standard output and progress or errors on
standard error. It should not log filenames, raw text, or extracted fields during
inbox automation. `--print-ocr-text` is an explicit diagnostic escape hatch and must
not be used in scheduled tasks, shared terminals, CI, screenshots, or support logs.

Desktop expiration alerts contain only normalized document type and expiration date.
Future browser notifications should use the same minimum disclosure by default and
should reveal additional fields only on an authenticated local detail view.

Exceptions exposed to users must describe the failing boundary without embedding a
model response, OCR content, question context, or database payload.

## Files and temporary data

Document paths must be explicit and normalized. Inbox discovery ignores symbolic
links. Processed files are moved without overwriting an existing filename.

The planned web uploader must:

- enforce request and file-size limits before processing;
- validate both extension and decoded content;
- generate server-side temporary names instead of trusting upload filenames;
- prevent path traversal and symbolic-link escapes;
- store temporary files inside one controlled local directory;
- remove incomplete files after success, cancellation, timeout, and exceptions;
- avoid returning absolute host paths to the browser.

## Planned local web threat model

Binding FastAPI to `127.0.0.1` is mandatory by default. A browser-facing service is
still exposed to malicious web pages, local malware, and other local users. Before
release, the web adapter must include:

- strict allowed hosts and origins;
- CSRF defenses for state-changing browser requests;
- secure, HTTP-only, same-site cookies if sessions are introduced;
- restrictive Content Security Policy and other browser security headers;
- validation and authorization for every document identifier;
- no document data in URLs, analytics, access logs, browser console logs, or caches;
- bounded upload, query, and job concurrency;
- confirmation and idempotency for deletion;
- disabled OpenAPI documentation in production if it reveals unnecessary surface.

Authentication is optional only for a strictly single-user loopback deployment with
a documented host trust assumption. Any LAN exposure changes the threat model and
requires authentication, TLS termination, access control, and a new ADR. It must not
be enabled merely by changing a host flag.

## Deletion and retention

Deletion is planned, not implemented. Before release, define whether archived source
files are application-managed or user-managed. The delete workflow must identify all
representations by document ID and remove, in a controlled order:

1. Chroma fragments for every embedding-model collection;
2. MongoDB `document_sections` records;
3. the MongoDB `documents` record;
4. the archived source file, only with explicit user intent and verified containment
   inside a managed directory;
5. transient upload and job artifacts.

Backups remain outside the live deletion boundary and require a documented retention
period. The UI must state whether deletion is reversible and whether backups may
retain data temporarily. Partial failures must be observable without exposing data.

## Backups and host controls

Backups must be local or handled by an organization-approved encrypted mechanism
outside this application's runtime. Protect database dumps, Docker volumes, processed
documents, and encryption keys with operating-system permissions and full-disk
encryption. Test restoration using synthetic data.

Recommended host controls include a dedicated OS account, automatic screen locking,
disk encryption, current security patches, restricted folder permissions, and an
explicit policy for cloud-synced folders. Do not place `data` or backups in a folder
automatically synchronized to a cloud provider when offline-only handling is required.

## Known limitations

The design does not defend against a compromised operating system, administrators,
malicious local processes, compromised Python or container dependencies, memory
inspection, insecure host backups, or user-directed disclosure. OCR and local model
outputs may also be inaccurate and must not be treated as authoritative without user
review.

Report vulnerabilities according to [SECURITY.md](../SECURITY.md).
