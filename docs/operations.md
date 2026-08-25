# Operations

## Deployment profile

Version 0.1.0 is a single-host application. Python, Tesseract, Ollama, and the CLI run
on the host. Docker Compose runs MongoDB and ChromaDB with named volumes and ports
bound to `127.0.0.1`.

The planned FastAPI service must also bind to `127.0.0.1` by default and run as a
single application process until durable job coordination is implemented.

## Start and stop

Start storage services without changing their data volumes:

```powershell
docker compose up -d mongodb chromadb
docker compose ps
```

Stop containers while retaining data:

```powershell
docker compose stop
```

Remove containers while retaining named volumes:

```powershell
docker compose down
```

Do not use `docker compose down --volumes` unless permanent deletion of both
databases has been explicitly approved and a verified backup exists when required.

Start Ollama using the host's normal service mechanism. Health and model checks must
not trigger automatic downloads in offline operation.

## Health checks

```powershell
docker compose ps
docker compose exec -T mongodb mongosh --quiet --eval "db.adminCommand('ping').ok"
```

ChromaDB has a Compose health check. A complete smoke test uses a synthetic document,
verifies storage and a local question, and then removes the synthetic data through an
approved maintenance procedure. Document deletion is not yet implemented, so avoid
using real data for disposable smoke tests.

## Windows Scheduled Task

Install or update the daily task:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\manage_expiration_task.ps1 Install -CheckTime 09:00 -DaysThreshold 30 -OcrLanguage ita
```

The task runs as the current interactive user with limited privileges. It can wake a
sleeping computer and run after a missed start, but it cannot run while the computer
is powered off. The runner starts Docker Desktop if required, starts MongoDB and
ChromaDB with `--pull never`, waits for health, then processes the inbox and checks
expirations.

Remove the task:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\manage_expiration_task.ps1 Uninstall
```

## Backup

Back up all authoritative representations together:

- MongoDB database `smart_doc_tracker`;
- every ChromaDB collection used by configured embedding models;
- `data/processed` or the configured archive directory;
- local configuration needed to reproduce model and service choices.

MongoDB can be exported with `mongodump` from the local container or a compatible
local tool. ChromaDB 1.5.9 has no application-level backup command in this project;
stop writes and use an organization-approved consistent backup of its named volume.
Do not copy a live database volume and assume consistency without testing.

Backup artifacts contain sensitive data. Store them locally with restricted
permissions and encryption, record their creation time and application version, and
test restores using synthetic data. Never upload them to an unapproved cloud service.

## Restore

Restore into an isolated local environment first:

1. stop application writers and scheduled jobs;
2. verify the backup manifest, version, and integrity hashes;
3. restore MongoDB, ChromaDB, and the processed archive from the same backup set;
4. start services and run health checks;
5. compare document counts and selected synthetic records;
6. verify that RAG results reference existing MongoDB IDs;
7. resume scheduled processing.

If MongoDB is restored without the matching Chroma state, semantic search may be
stale or incomplete. A future reindex command is required for supported recovery.

## Updates

Before updating:

1. read [CHANGELOG.md](../CHANGELOG.md);
2. create and verify a backup;
3. stop scheduled tasks and application processes;
4. review dependency and container changes for telemetry or network behavior;
5. run the offline test suite;
6. apply required schema migrations before resuming writes.

Container and Python dependency versions should be pinned for production deployment.
The repository currently uses compatible version ranges for several Python packages,
so a company deployment should additionally maintain a reviewed lock file.

## Retention and deletion

Live record deletion is not implemented. Do not manually delete only MongoDB records,
because raw fragments may remain searchable in ChromaDB and archived files may remain
on disk. Until coordinated deletion exists, use a documented administrator procedure
that identifies every representation and records any partial failure.

When FastAPI deletion is delivered, operations must define:

- whether source archives are managed by the application;
- soft-delete or immediate hard-delete policy;
- backup retention and expiry;
- reconciliation for partial cross-store failures;
- audit events that contain IDs and outcomes but no document contents.

## Planned FastAPI service

Run the future server with one worker and an explicit loopback bind. The exact command
will be documented only when the API package exists. Do not publish a speculative
production command or expose port `8000` broadly; ChromaDB already uses that port in
the current Compose file.

Operational readiness for the web release requires bounded upload size, background
job limits, graceful shutdown, restart recovery, health/readiness endpoints without
sensitive data, access-log redaction, and exactly one active expiration scheduler.

## Monitoring

The application intentionally has no telemetry or remote monitoring. Local
operational monitoring may record service availability, queue length, aggregate job
counts, durations, and error categories. It must not record filenames, questions,
raw text, structured fields, embeddings, model responses, or document identifiers
unless an approved local audit policy explicitly requires sanitized identifiers.

See [Troubleshooting](troubleshooting.md) for common failures.
