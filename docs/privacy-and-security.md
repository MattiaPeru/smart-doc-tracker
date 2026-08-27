# Privacy and Security

## Objective

Smart Doc Tracker is designed so sensitive document content remains on the user's
host during normal operation. This is an architectural property with explicit
assumptions, not a guarantee against every host or supply-chain threat.

## Data inventory

| Data | Location | Sensitivity |
| --- | --- | --- |
| Original documents | Inbox and processed folders | High |
| Raw OCR/PDF text | Memory, pending-confirmation manifests, and ChromaDB fragments | High |
| Structured fields and summaries | MongoDB and ChromaDB | High |
| PDF section analyses | MongoDB | High |
| Embeddings | ChromaDB | Potentially sensitive |
| Source SHA-256 hashes | MongoDB | Sensitive metadata |
| Expiration notification text | Local desktop and browser UI | Moderate |
| Operational status and counts | Terminal and local job manifests | Low if content-free |

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
The dashboard displays document details only to the same-host browser and does not
claim to provide authentication between local users.

Exceptions exposed to users must describe the failing boundary without embedding a
model response, OCR content, question context, or database payload.

## Files and temporary data

Document paths must be explicit and normalized. Inbox discovery ignores symbolic
links. Processed files are moved without overwriting an existing filename.

The implemented web uploader:

- enforces a 25 MB streamed file-size limit and an extension allow list;
- strips directory components from the submitted filename and generates server-side
  temporary and queue names;
- keeps accepted work in controlled processing and confirmation directories;
- removes incomplete temporary copies after errors;
- avoids returning absolute host paths to the browser.

Accepted uploads survive restart in `data/processing_queue`. After parsing, the source,
raw text, and validated data survive in `data/pending_confirmation` until confirmation
or rejection. These directories are sensitive application storage, not disposable
cache. Decoded-content or magic-byte validation is not currently implemented.

## Local web threat model

The launcher accepts only `127.0.0.1` or `::1` and runs one Uvicorn worker. A
browser-facing loopback service is still exposed to malicious web pages, local
malware, and other local users. The current dashboard does not implement
authentication, CSRF tokens, explicit origin/host middleware, a restrictive Content
Security Policy, or disabled OpenAPI documentation. It must not be exposed to a LAN.

Before any broader or multi-user deployment, add and verify:

- strict allowed hosts and origins;
- CSRF defenses for state-changing browser requests;
- secure, HTTP-only, same-site cookies if sessions are introduced;
- restrictive Content Security Policy and other browser security headers;
- validation and authorization for every document identifier;
- no document data in URLs, analytics, access logs, browser console logs, or caches;
- bounded query concurrency in addition to the current bounded upload worker;
- idempotent deletion and explicit archived-file policy;
- disabled OpenAPI documentation in production if it reveals unnecessary surface.

Authentication is optional only for a strictly single-user loopback deployment with
a documented host trust assumption. Any LAN exposure changes the threat model and
requires authentication, TLS termination, access control, and a new ADR. It must not
be enabled merely by changing a host flag.

## Deletion and retention

Dashboard deletion removes fragments for the document from the active embedding-model
collection, then removes MongoDB sections and the primary record. It snapshots Chroma
content first and attempts restoration if MongoDB deletion fails. It does not remove:

1. fragments in collections created for other embedding models;
2. the archived source under `data/processed`;
3. backups;
4. unrelated pending or failed upload artifacts.

Backups remain outside the live deletion boundary and require a documented retention
period. Live deletion is not fully reversible and backups may retain data temporarily.
Partial failures are reported without exposing document content, but a full
reconciliation workflow is not yet available.

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
