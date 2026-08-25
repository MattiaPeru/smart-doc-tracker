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

The current metadata update path does not reindex ChromaDB. Consumers must treat
semantic results as potentially stale after an update.

## Planned FastAPI schemas

HTTP request and response schemas must be separate from persistence records. They may
reuse domain validation but must not expose MongoDB internals, host paths, raw model
responses, or arbitrary query operators.

Recommended resource shapes include:

- `DocumentSummary`: ID, normalized envelope fields, and safe status information;
- `DocumentDetail`: validated document plus explicit source-file availability;
- `DocumentUpdate`: optional validated editable fields;
- `ProcessingJob`: opaque ID, state, timestamps, safe error category, and progress;
- `DocumentQuestion`: bounded question and retrieval limit;
- `DocumentAnswer`: answer and existing source document IDs;
- `DeletionRequest`: explicit source-file choice and confirmation token;
- `DeletionResult`: per-representation outcome without sensitive content.

Uploaded filenames are presentation metadata, not trusted filesystem paths. Job
records must not store OCR text. Database filtering must use an allow-listed query
model rather than accepting raw MongoDB dictionaries from the browser.

## Evolution and migration

Any persisted schema change requires:

1. a documented version and ADR when the change is architectural;
2. a forward migration and tested rollback or recovery plan;
3. validation against both old and new synthetic records;
4. an index migration or rebuild plan;
5. backup verification before production execution.

Do not silently reinterpret existing dynamic keys. Prefer additive migrations and
explicit normalized aliases.
