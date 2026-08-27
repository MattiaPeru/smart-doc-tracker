# ADR 0004: Local Retrieval-Augmented Generation

- Status: Accepted
- Date: 2026-08-25

## Context

Users need to ask questions across diverse personal documents. Sending documents or
queries to hosted embedding or generation services would violate the offline-first
boundary. Answer generation must also limit unsupported claims and identify the local
records used as sources.

## Decision

Generate embeddings with a locally installed Ollama model and store vectors in a
loopback-only ChromaDB service. Disable Chroma's default embedding function. Index
overlapping raw-text chunks, the validated summary, and the complete structured JSON.

Use a deterministic collection name per embedding-model name to avoid incompatible
vector dimensions. Retrieve a bounded number of fragments, treat their content as
untrusted data, and ask a local Ollama generator for a validated `DocumentAnswer`.
Reject answers that cite document IDs outside the retrieved context.

Use deterministic MongoDB queries instead of RAG when a question can be safely
recognized as a calendar-year expiration query.

The current web interface exposes indexed-content inspection but not the bounded
question use case. A future dashboard question flow must link answers to existing
local document views and must not log questions or retrieved content.

## Consequences

Benefits:

- document content and questions stay on the host during normal use;
- answers identify the records used as sources;
- structured and unstructured content are both retrievable;
- expiration questions can bypass probabilistic generation where appropriate.

Costs and limitations:

- embeddings and raw fragments are sensitive persisted data;
- answers can still be incomplete or inaccurate;
- changing an embedding model creates a separate empty collection;
- CLI updates do not refresh the vector index; dashboard edits durably refresh the
  summary and structured fragments but preserve raw-text fragments;
- MongoDB and ChromaDB can diverge after partial failures;
- prompt-injection defenses reduce risk but do not guarantee model behavior.

## Verification

Tests must confirm local URL validation, disabled default embeddings, bounded
retrieval, deterministic fragments, stale-fragment cleanup, validated answer shapes,
and rejection of ungrounded document IDs. The user interface must present answers as
assistance, not authoritative document interpretation.
