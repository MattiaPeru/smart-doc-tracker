# Troubleshooting

Use sanitized diagnostics only. Never paste document contents, model responses,
database dumps, personal paths, or `--print-ocr-text` output into public issues.

## First checks

```powershell
.venv\Scripts\python.exe --version
docker compose ps
ollama list
tesseract --version
smart-doc-tracker --help
```

Confirm that Python is 3.11 or newer and that commands resolve inside the intended
virtual environment.

## The command is not found

Activate `.venv` and reinstall the editable package:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m smart_doc_tracker --help
```

The module form bypasses console-script path issues.

## Tesseract is unavailable

If the application reports that the local Tesseract executable was not found, verify
`tesseract --version` in the same terminal and add the installation directory to the
user `PATH`. Restart the terminal afterward.

If extraction fails only for one language, install the corresponding Tesseract
language data and verify it with:

```powershell
tesseract --list-langs
```

Use the exact language code with `--language`, such as `eng` or `ita`.

## An image or PDF cannot be processed

Confirm that the file is regular, readable, and has a supported extension. Password-
protected PDFs are not supported. PDFs with fewer than 20 usable text characters on
a page use OCR fallback, which requires Tesseract.

Try text extraction without `--structured` to isolate OCR/PDF problems from Ollama
problems. Use only synthetic data with `--print-ocr-text` when collecting diagnostics.

## Ollama is unavailable or returns invalid output

Verify that Ollama is running on `http://127.0.0.1:11434` and the selected model is
already installed:

```powershell
ollama list
```

The application deliberately rejects remote URLs, missing ports, credentials, HTTPS,
paths, and query strings. A model can still produce invalid structured JSON; retry
with a supported local instruct model and review the source document quality.

Do not include the generated response in public bug reports because it may reproduce
sensitive source content.

## MongoDB is unavailable

```powershell
docker compose up -d mongodb
docker compose ps mongodb
docker compose logs --tail 50 mongodb
docker compose exec -T mongodb mongosh --quiet --eval "db.adminCommand('ping').ok"
```

Sanitize logs before sharing them. The configured URI must use `mongodb://` with an
explicit loopback host and port and no credentials, database path, query, or fragment.

## ChromaDB or document questions fail

```powershell
docker compose up -d chromadb
docker compose ps chromadb
docker compose logs --tail 50 chromadb
ollama list
```

Check that `embeddinggemma`, or the model passed through `--embedding-model`, is
installed. Each embedding-model name maps to a separate Chroma collection. Changing
the model does not migrate existing documents into the new collection.

If MongoDB contains a document but RAG cannot find it, indexing may have failed after
the MongoDB write. There is currently no supported bulk reindex command. Reprocessing
the exact file can upsert its index, provided the required local services are healthy.

After a metadata update, semantic search may still contain the originally indexed
summary and structured payload. This is a known current consistency limitation.

## Inbox files do not move

Failed files intentionally remain in the inbox. Verify extension, permissions,
Tesseract, Ollama, MongoDB, and ChromaDB. Unsupported files and symbolic links are
skipped. Inbox and processed directories must resolve to different locations.

If the target filename already exists, the application creates a numbered name. It
does not overwrite an archived document.

## Notifications do not appear

Run a one-time foreground check first:

```powershell
smart-doc-tracker --check-expirations --days-threshold 30
```

Confirm that at least one document expires from today through the inclusive threshold
and that OS notifications are permitted for the Python process. Windows Scheduled
Tasks run as the current interactive user specifically so desktop notifications can
be shown.

## The Windows Scheduled Task fails

Confirm that:

- `.venv\Scripts\python.exe` exists;
- Docker Desktop and its CLI are installed;
- the MongoDB and ChromaDB images already exist locally;
- Tesseract and the selected Ollama models are installed;
- the task user can access the repository and document folders;
- the task completes within its ten-minute execution limit.

Run `scripts\run_expiration_check.ps1` manually from a private terminal to obtain a
sanitized error. Reinstalling the task updates its configuration.

## Planned FastAPI problems

The web service is not implemented. When it is added, troubleshooting must cover job
queue saturation, abandoned uploads, browser origin or CSRF rejection, partial
deletion, stale indexing, and restart recovery. API access logs must be configured so
uploaded filenames, search queries, and document identifiers are not recorded.

## Requesting support

Provide the application version, operating-system version, sanitized command shape,
dependency versions, exit status, and error category. Follow [SECURITY.md](../SECURITY.md)
for vulnerabilities and [CONTRIBUTING.md](../CONTRIBUTING.md) for ordinary defects.
