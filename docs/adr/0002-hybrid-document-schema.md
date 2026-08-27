# ADR 0002: Hybrid Document Schema

- Status: Accepted
- Date: 2026-08-25

## Context

The application must support many document categories whose fields are not known in
advance, while expiration tracking, browsing, and sorting require stable common
metadata. A rigid schema loses type-specific information; an entirely dynamic schema
makes validation and common queries unreliable.

Local model output is uncertain and must not be persisted without validation. The
web editor applies the same rules as automated extraction.

## Decision

Use a hybrid `DocumentData` model with a fixed envelope:

- `document_type`;
- `summary`;
- `expiry_date`;
- `issue_date`;

and one recursive, JSON-compatible `extracted_data` object for document-specific
values.

The fixed envelope rejects extra fields, normalizes common date forms and document
types, and applies length limits. Dynamic keys use English `snake_case` at every
level. Missing values remain explicit and ambiguous extraction results are preserved
as alternatives rather than invented or silently discarded.

HTTP request and response models remain separate from persistence records while delegating
domain validation to the same rules.

## Consequences

Benefits:

- common expiration and browsing queries remain predictable;
- new document types do not require a new MongoDB collection or immediate migration;
- local model output and user edits cross one validation boundary;
- unknown fields remain representable.

Costs:

- dynamic keys can still vary semantically between documents;
- arbitrary dynamic values have less static typing;
- cross-document analytics require normalization conventions;
- changes to the envelope require migrations and index review.

## Alternatives considered

A schema per document type was rejected because it would require continual model and
migration work. A completely unstructured JSON document was rejected because common
expiration, validation, and presentation behavior would be unreliable.
