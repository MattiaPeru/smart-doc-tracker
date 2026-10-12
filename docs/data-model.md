# Data Model

## Domain document

`DocumentData` is the validated boundary between uncertain extraction and trusted
persistence:

```json
{
  "document_type": "insurance_policy",
  "summary": "A vehicle insurance policy",
  "expiry_date": "2030-12-31",
  "issue_date": "2025-01-01",
  "notification_days_before": null,
  "extracted_data": {
    "policy_number": "P-123",
    "holder": {
      "city": "Rome"
    }
  }
}
```

The fixed envelope supports common workflows. `extracted_data` preserves fields that
vary by document type without creating a collection per type.

## Validation and normalization

- Unknown top-level fields are rejected.
- Strings are trimmed.
- `document_type` is required, limited to 100 characters, and normalized to lowercase
  `snake_case`.
- `summary` is required and limited to 1,000 characters.
- Dates are optional and normalized from `YYYY-MM-DD`, `DD/MM/YYYY`, `DD-MM-YYYY`,
  or `YYYY/MM/DD`.
- `extracted_data` is optional and defaults to an empty object when no additional
  facts are available.
- `notification_days_before` is either `null` to follow the current application
  default or an integer from 0 through 3,650 for a document-specific override.
- Empty, `none`, `null`, `n/a`, `unknown`, and `not_applicable` date strings become
  `null`.
- Dynamic keys at every nesting level must use English `snake_case`.
- Dynamic values must be JSON-compatible; non-finite numbers are rejected.
- Missing or ambiguous values must remain `null`, be omitted from the dynamic data,
  or be represented explicitly as alternatives. They must not be invented.

## MongoDB collections

### `documents`

| Field | MongoDB type | Meaning |
| --- | --- | --- |
| `_id` | ObjectId | Primary local identifier |
| `file_hash` | string | Lowercase SHA-256 of the source file |
| `created_at` | UTC datetime | Initial insertion time |
| `document_type` | string | Normalized category |
| `summary` | string | Validated concise summary |
| `expiry_date` | UTC datetime or null | Date stored at midnight UTC |
| `issue_date` | UTC datetime or null | Date stored at midnight UTC |
| `notification_days_before` | integer or null | Per-document reminder override |
| `extracted_data` | object | Validated dynamic payload |

Indexes:

- unique ascending `file_hash` for idempotent insertion;
- ascending `expiry_date` for expiration queries.

Updates replace the validated domain fields while preserving `_id`, `file_hash`, and
`created_at`.

### `document_sections`

Long PDFs store page-aware analyses separately:

| Field | Meaning |
| --- | --- |
| `document_id` | Parent `documents._id` |
| `chunk_number` | Positive one-based section number |
| `page_from`, `page_to` | Inclusive positive page range |
| `structured_data` | Validated section-level `DocumentData` |

The pair `(document_id, chunk_number)` is unique. Raw page text is not stored in this
collection.

## Long-document consolidation

PDF pages are grouped into bounded page-aware text chunks. Each chunk is parsed and
validated. Consolidation selects common document types and dates, joins distinct
summaries, recursively merges dynamic mappings, and records conflicting candidates
instead of silently discarding them.

## ChromaDB representation

Every indexed document creates:

- one `summary` fragment;
- one `structured_data` fragment containing sorted JSON;
- overlapping `raw_text` fragments, currently 2,000 characters with 200-character
  overlap by default.

Fragment IDs combine the MongoDB document ID and deterministic suffixes. Metadata
contains the MongoDB `document_id` and source category. Embeddings are produced by a
local Ollama model. Each embedding-model name maps to a deterministic separate
collection to prevent vector-dimension conflicts.

ChromaDB therefore contains sensitive raw text even though MongoDB does not.

## Consistency model

MongoDB is authoritative for validated records and expiration queries. ChromaDB is a
derived search index. The current workflow writes MongoDB before ChromaDB and has no
cross-database transaction. Reconciliation and supported full reindexing are planned.

CLI metadata updates do not reindex ChromaDB. Dashboard updates durably queue a
refresh of the summary and structured-data fragments in the active collection; raw
text is preserved. Failed refresh jobs can still leave semantic results stale.

Dashboard confirmation compensates a failed new insert by deleting the new MongoDB
record, sections, and active-collection fragments where possible. Dashboard deletion
snapshots active-collection fragments, deletes them and the MongoDB record plus
sections, and restores the Chroma snapshot if the MongoDB operation fails. Archived
source files, backups, and collections created for other embedding models are outside
these live mutation boundaries.

## FastAPI schemas and durable local state

HTTP response schemas are separate from persistence records. They reuse domain
validation without exposing file hashes, host paths, raw model responses, embeddings,
or arbitrary MongoDB operators.

Implemented resource shapes include:

- `DocumentResponse`: ID, validated document fields, creation time, and expiration
  status;
- `DocumentUpdateResponse`: the stored document plus an opaque index-refresh ID;
- `UploadJobResponse`: opaque ID, sanitized filename, timestamps, safe status, and a
  generic failure message;
- `PendingDocumentResponse`: validated editable data without raw text or local paths;
- `IndexUpdateJobResponse`: opaque refresh ID and status only;
- `DocumentIndexedContentResponse`: fragment IDs, categories, and content, explicitly
  excluding embeddings.

Uploaded filenames are presentation metadata, not trusted filesystem paths. Job
manifests do not store OCR text. Pending-confirmation manifests do store raw text and
validated data locally because confirmation can happen after a restart. Database
filtering accepts only validated dot-separated `snake_case` paths and exact
JSON-compatible values, never raw MongoDB dictionaries.

## Evolution and migration

Any persisted schema change requires:

1. a documented version and ADR when the change is architectural;
2. a forward migration and tested rollback or recovery plan;
3. validation against both old and new synthetic records;
4. an index migration or rebuild plan;
5. backup verification before production execution.

Do not silently reinterpret existing dynamic keys. Prefer additive migrations and
explicit normalized aliases.
