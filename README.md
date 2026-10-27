# Smart Doc Tracker

Smart Doc Tracker is a privacy-first application for extracting, organizing, and
searching personal documents on a single host. It combines local OCR, local language
models, validated structured data, local persistence, semantic search, and expiration
reminders.

The project includes both a command-line interface and a local FastAPI dashboard for
asynchronous document uploads, browsing, exact dynamic-field queries, and expiration
alerts.

## Privacy model

Document processing is designed to remain on the host:

- Tesseract performs OCR locally.
- PyMuPDF reads PDFs locally and uses Tesseract for pages without usable text.
- Ollama provides local structured generation and embeddings.
- MongoDB and ChromaDB listen on explicit loopback addresses.
- Chroma telemetry is disabled and its default embedding function is not used.
- Raw OCR text is not stored in MongoDB, but it is stored as local Chroma fragments
  when a document is indexed.

Software installation, Docker image downloads, and `ollama pull` may use the network.
They must be completed separately before operating in an offline environment. See
[Privacy and security](docs/privacy-and-security.md) for assumptions and limitations.

## Current capabilities

- OCR for BMP, JPEG, PNG, TIFF, WebP, and PDF files.
- Direct extraction from digital PDFs with OCR fallback per page.
- Validated structured extraction with a hybrid fixed-and-dynamic schema.
- Idempotent MongoDB storage based on the source file SHA-256 hash.
- Page-aware structured storage for long PDFs.
- Local semantic search and grounded answers through ChromaDB and Ollama.
- Inbox processing with collision-safe archiving.
- Document listing, retrieval, and validated updates.
- Expiration checks, desktop notifications, and Windows Task Scheduler integration.
- Loopback-only dashboard with durable, single-worker upload processing.
- Review and correction of extracted data before storage and indexing.
- Exact dynamic-field filtering, indexed-content inspection, synchronized metadata
  updates, and coordinated record deletion from MongoDB and ChromaDB.

The dashboard does not yet expose natural-language questions, pagination, or deletion
of archived source files. The CLI does not provide a delete command.

## Requirements

- Python 3.11 or newer
- Tesseract OCR and the required language packs on `PATH`
- Ollama with `qwen2.5:3b` and `embeddinggemma`, or compatible local models
- Docker Desktop or another Docker Compose runtime
- Windows for the supplied Scheduled Task scripts

## Quick start

Create the environment and install the package:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
```

For CLI workflows, start local persistence services:

```powershell
docker compose up -d mongodb chromadb
```

The `smart-doc-tracker-web` command manages its own local service lifecycle. It starts
missing MongoDB and ChromaDB containers plus Ollama, waits until they are ready, and
stops only the services it started when the web server exits. Docker Desktop must be
running; existing services are left running.

Install the Ollama models before going offline:

```powershell
ollama pull qwen2.5:3b
ollama pull embeddinggemma
```

Process and store one document:

```powershell
smart-doc-tracker path\to\document.pdf --language ita --structured --store
```

Process the local inbox and check expirations within 30 days:

```powershell
smart-doc-tracker --days-threshold 30 --language ita
```

Ask a grounded question:

```powershell
smart-doc-tracker --ask-documents "Which policies expire this year?"
```

To diagnose a rejected generated answer on a private terminal, explicitly print the
local model response and validation reason:

```powershell
smart-doc-tracker --ask-documents "Which skills are in my CV?" --show-rag-validation-details
```

Use `python -m smart_doc_tracker` if the console command is unavailable. Run
`smart-doc-tracker --help` for the complete CLI reference.

## Local dashboard

Start the FastAPI dashboard after the local services and Ollama model are available:

```powershell
smart-doc-tracker-web
```

Open `http://127.0.0.1:8080`. The server only accepts a loopback bind address, uses
one upload worker, and durably resumes interrupted queued work after restart. Uploaded
PDF and image files are parsed locally, then staged for review. They are stored,
indexed, and archived only after explicit confirmation; rejection removes the staged
copy. Uploads are limited to 25 MB.

The server terminal shows local processing progress and safe error diagnostics. HTTP
access lines are hidden by default to keep the output readable. Use `--log-level error`
to show only errors, `--log-level debug` for additional framework diagnostics, or
`--access-log` to also show every HTTP request:

```powershell
smart-doc-tracker-web --log-level error
smart-doc-tracker-web --access-log
```

To inspect one chat request from retrieval through the final answer, start the server
with `--chat-debug`:

```powershell
smart-doc-tracker-web --chat-debug
```

The terminal trace groups events by request ID and includes the retrieval query,
matched file names and document fragments, the exact system and user prompts,
each raw Ollama response, validation failures, and the final answer or error.
The trace may contain private document text. Keep terminal output local and turn
this option off after debugging; normal server logs do not include document text.

Dashboard edits update MongoDB immediately and queue a durable refresh of the summary
and structured-data fragments in ChromaDB. Dashboard deletion removes MongoDB metadata
and PDF sections plus the active ChromaDB collection's fragments, but deliberately
leaves archived source files and backups untouched.

## Common commands

```powershell
smart-doc-tracker --process-inbox --language ita
smart-doc-tracker --list-stored
smart-doc-tracker --get-stored DOCUMENT_ID
smart-doc-tracker --update-stored DOCUMENT_ID --summary "Corrected summary"
smart-doc-tracker --check-expirations --days-threshold 14
smart-doc-tracker --monitor-expirations --check-time 09:00
```

Raw extracted text is printed only when `--print-ocr-text` is explicitly supplied.
That option can expose sensitive content in terminals, shell history captures, and
support recordings.

## Inbox automation

Place supported files in `data/inbox`. Successfully stored files move to
`data/processed`; failed files remain in the inbox. Unsupported files and symbolic
links are ignored. Existing processed filenames are never overwritten.

Custom folders can be provided with `--inbox-dir` and `--processed-dir`.

Install or update the Windows daily task:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\manage_expiration_task.ps1 Install -CheckTime 09:00 -DaysThreshold 30 -OcrLanguage ita
```

Remove it with:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\manage_expiration_task.ps1 Uninstall
```

## Development

```powershell
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.venv\Scripts\python.exe -m ruff format --check .
.venv\Scripts\python.exe -m ruff check .
.venv\Scripts\python.exe -m mypy
.venv\Scripts\python.exe -m pytest --cov --cov-report=term-missing
```

Tests are deterministic and must not require network access. Branch coverage must
remain at or above 80%.

## Documentation

- [User guide](docs/user-guide.md)
- [Architecture](docs/architecture.md)
- [Privacy and security](docs/privacy-and-security.md)
- [Operations](docs/operations.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Data model](docs/data-model.md)
- [Development guide](docs/development.md)
- [Testing guide](docs/testing.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Changelog](CHANGELOG.md)

## License

This project is available under the [MIT License](LICENSE).
