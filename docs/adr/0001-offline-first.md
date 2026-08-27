# ADR 0001: Offline-First Architecture

- Status: Accepted
- Date: 2026-08-25

## Context

The application processes identity documents, contracts, invoices, policies, and
other potentially sensitive files. Hosted OCR, language models, telemetry, and remote
storage would transmit content outside the user's machine and complicate consent,
retention, and regulatory controls.

The FastAPI interface introduces an HTTP server and browser, but it does not change
the privacy objective.

## Decision

All document ingestion, OCR, parsing, validation, persistence, retrieval, generation,
notification, and scheduling will operate on one local host.

MongoDB, ChromaDB, Ollama, and the FastAPI server must use explicit loopback
bindings by default. The application will reject remote service endpoints and will
not include cloud services, hosted models, analytics, telemetry, remote storage, or
remote fallbacks.

Dependencies and models may be downloaded only as a separate, operator-controlled
installation activity. Normal scheduled execution must not download resources.

The web interface is a local inbound adapter over the same application services.
LAN or Internet exposure is not supported by this decision and requires a new threat
model and superseding ADR.

## Consequences

Benefits:

- sensitive content remains within the defined host boundary during normal use;
- the system can operate without Internet connectivity;
- data locations and retention are directly inspectable;
- service endpoint validation can fail closed.

Costs:

- users install and operate Tesseract, Ollama, MongoDB, and ChromaDB;
- performance depends on local hardware;
- model quality and availability depend on installed local models;
- remote collaboration and hosted monitoring are intentionally unavailable;
- loopback does not protect against hostile local processes or a compromised host.

## Verification

Tests must reject non-loopback configurations and replace infrastructure with fakes.
Dependency updates must be reviewed for downloads, telemetry, update checks, and
remote fallbacks. Deployment documentation must identify installation steps that can
use the network.
