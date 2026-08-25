# ADR 0003: Local Persistence

- Status: Accepted
- Date: 2026-08-25

## Context

The application needs durable structured records, exact and date-based queries,
idempotent ingestion, and semantic retrieval. Original documents and derived data are
sensitive. One persistence engine does not serve both structured queries and vector
similarity equally well.

The planned FastAPI application adds browsing, filtering, asynchronous job state, and
deletion requirements.

## Decision

Use loopback-only MongoDB as the authoritative store for validated documents and PDF
section analyses. Use a unique SHA-256 source-file hash for idempotent insertion and
an expiration-date index for common queries.

Use loopback-only ChromaDB as a derived vector index. Keep original or archived files
in controlled local folders rather than inside MongoDB. Bind Docker ports explicitly
to `127.0.0.1` and persist databases in named local volumes.

The future web application will access these stores through repository interfaces.
It will not accept arbitrary MongoDB queries from clients. Job persistence, schema
versioning, reindexing, and coordinated deletion must be designed before the web
interface is production-ready.

## Consequences

Benefits:

- MongoDB supports flexible validated payloads and indexed date queries;
- ChromaDB supports local semantic retrieval;
- original files remain inspectable and separately manageable;
- source hashing avoids duplicate primary records.

Costs:

- MongoDB, ChromaDB, and the file archive can diverge;
- backup and restore must coordinate multiple representations;
- updates and deletion require explicit index synchronization;
- Docker and local volume operations add administrative overhead.

MongoDB is authoritative; ChromaDB can be rebuilt once a supported reindex workflow
exists. Raw OCR text used for rebuilding is not stored in MongoDB, so a full rebuild
also depends on access to managed source files and repeatable extraction.

## Follow-up requirements

- Add schema versioning and supported migrations.
- Add a full reconciliation and reindex workflow.
- Add repository methods for deleting primary records and sections.
- Add vector-index deletion across every embedding-model collection.
- Define source-file ownership and backup retention before exposing deletion.
