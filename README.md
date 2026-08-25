# Smart Doc Tracker

Smart Doc Tracker is a privacy-first application for extracting, organizing, and
searching personal documents on a single host. It combines local OCR, local language
models, validated structured data, local persistence, semantic search, and expiration
reminders.

The current interface is a command-line application. A local FastAPI web application
is planned for document upload, asynchronous processing, browsing, database queries,
expiration notifications, and coordinated document deletion. Planned features are
identified as such throughout the documentation.

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

Document deletion and the FastAPI web interface are not implemented yet.

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

Start local persistence services:

```powershell
docker compose up -d mongodb chromadb
```

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

Use `python -m smart_doc_tracker` if the console command is unavailable. Run
`smart-doc-tracker --help` for the complete CLI reference.

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
