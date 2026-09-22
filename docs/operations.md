# Operations

## Deployment profile

Version 0.1.0 is a single-host application. Python, Tesseract, Ollama, and the CLI run
on the host. Docker Compose runs MongoDB and ChromaDB with named volumes and ports
bound to `127.0.0.1`.

The FastAPI dashboard runs on the host, binds to `127.0.0.1` by default, and uses one
application process. Upload and index-refresh jobs are durable on local disk but are
not coordinated across multiple processes.

## Start and stop

The `smart-doc-tracker-web` command starts missing MongoDB and ChromaDB containers and
a missing Ollama process automatically. On shutdown it stops only the services
started for that server run. Docker Desktop remains a host prerequisite and is not
stopped by the application.

For CLI workflows, start storage services without changing their data volumes:

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

For CLI workflows, start Ollama using the host's normal service mechanism. Health and
model checks must not trigger automatic downloads in offline operation.

Start the dashboard (its managed services are checked before FastAPI is created):

```powershell
smart-doc-tracker-web
```

The default URL is `http://127.0.0.1:8080`. Only `127.0.0.1` and `::1` are accepted
by `--host`; `--port` accepts values from 1 through 65535. Run exactly one process.

## Health checks

```powershell
docker compose ps
docker compose exec -T mongodb mongosh --quiet --eval "db.adminCommand('ping').ok"
```

ChromaDB has a Compose health check. A complete smoke test uses a synthetic document,
verifies storage and a local question, and then deletes the live record through the
dashboard. The archived synthetic source remains under `data/processed` and must be
removed separately through an approved, path-verified maintenance procedure.

## Windows Scheduled Task

Install or update the daily task:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\manage_expiration_task.ps1 Install -CheckTime 09:00 -OcrLanguage ita
```

The task runs as the current interactive user with limited privileges. It can wake a
sleeping computer and run after a missed start, but it cannot run while the computer
is powered off. The runner starts Docker Desktop if required, starts MongoDB and
ChromaDB with `--pull never`, waits for health, then processes the inbox and checks
expirations.
The expiration check reads the current dashboard reminder default at every run, so
changing the setting does not require reinstalling the task.

Remove the task:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\manage_expiration_task.ps1 Uninstall
```

## Backup

Back up all authoritative representations together:

- MongoDB database `smart_doc_tracker`;
- every ChromaDB collection used by configured embedding models;
- `data/processed` or the configured archive directory;
- `data/processing_queue`, `data/pending_confirmation`, and
  `data/index_update_queue` while the dashboard has unfinished work;
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

Dashboard deletion coordinates the active ChromaDB collection with the MongoDB
document and its section records. It does not delete archived source files, backups,
or fragments in collections associated with other embedding-model configurations.
The CLI has no deletion command.

Before deletion, verify which embedding model is configured. Afterward, retain or
remove the archived source according to the local retention policy using an explicit,
path-verified procedure. A complete production policy still needs backup expiry,
cross-collection reconciliation, source-file ownership, and privacy-safe audit rules.

## Dashboard operations

The server enforces a 25 MB upload limit and one processing worker. Accepted upload,
pending-confirmation, and index-refresh state survives a normal restart in local data
folders. Shutdown waits for accepted in-process jobs, so allow it to complete.

There is no supported multi-worker deployment, bulk reindex command, health/readiness
API, authentication layer, or hardened reverse-proxy profile. Do not expose port 8080
outside loopback; port 8000 belongs to ChromaDB in the Compose configuration.

## Monitoring

The application intentionally has no telemetry or remote monitoring. Local
operational monitoring may record service availability, queue length, aggregate job
counts, durations, and error categories. It must not record filenames, questions,
raw text, structured fields, embeddings, model responses, or document identifiers
unless an approved local audit policy explicitly requires sanitized identifiers.

See [Troubleshooting](troubleshooting.md) for common failures.
