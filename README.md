# smart-doc-tracker
An intelligent, offline-first tool to manage personal paperwork. Combines Tesseract OCR and local LLMs to turn unstructured files into searchable, trackable data.

## Local OCR, PDF extraction, and structured parsing

The application reads local images and PDFs, extracts text locally, and can pass
that text to an Ollama model running exclusively on the loopback interface. The
model output is sanitized and validated as a hybrid Pydantic document: a fixed
metadata envelope plus a flexible `extracted_data` payload. Validated documents
can be persisted in a loopback-only MongoDB instance. No document data is sent
to remote services.

Requirements:

- Python 3.11 or newer
- Tesseract OCR installed locally and available on `PATH`
- The relevant Tesseract language packs (for example, `eng` or `ita`)
- Ollama installed locally with a model such as `qwen2.5:3b` (structured mode only)
- Docker Desktop or another local Docker Compose runtime (storage only)

Create and activate a virtual environment, then install the Python dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
```

This installs the `smart_doc_tracker` Python package and the
`smart-doc-tracker` command. The equivalent module form is
`python -m smart_doc_tracker`.

Run OCR on a sample image:

```powershell
smart-doc-tracker path\to\sample.png --language ita
```

Run OCR followed by validated local AI parsing:

```powershell
smart-doc-tracker path\to\sample.png --language ita --structured
```

Process an image and store its validated data in local MongoDB:

```powershell
smart-doc-tracker path\to\sample.png --language ita --structured --store
```

Process a PDF of any document type in bounded page-aware sections:

```powershell
smart-doc-tracker path\to\document.pdf --language ita --structured --store
```

Digital PDF pages are read directly. Pages without a usable text layer fall back
to local Tesseract OCR. Long PDFs are split into bounded sections before local
Ollama processing; the default client context is 8,192 tokens with at most 2,048
generated tokens per request. The consolidated record is stored in `documents`,
while page ranges and partial structured results are stored in
`document_sections`. Raw PDF text is not persisted in MongoDB.

The command prints the MongoDB document ID, SHA-256 source-file hash, insertion
status, and validated document data. Repeating it with the same file returns
`"inserted": false` and does not create a duplicate.

## Inbox automation

Place supported image or PDF documents in `data/inbox`, then run the complete local
pipeline with:

```powershell
smart-doc-tracker --process-inbox --language ita
```

The startup scanner creates `data/inbox` and `data/processed` when needed. Each
supported file goes through OCR, validated local Ollama parsing, and idempotent
MongoDB storage before it is moved to `data/processed`. A failed file remains in
the inbox for inspection or retry, and unsupported entries are left untouched.
If a processed filename already exists, the scanner selects a numbered filename
instead of overwriting it.

The command prints aggregate counts only; it does not log filenames, OCR text,
or extracted fields. Use custom local folders when needed:

```powershell
smart-doc-tracker --process-inbox --inbox-dir D:\Docs\inbox --processed-dir D:\Docs\processed
```

## Run the complete pipeline now

With MongoDB already available on the local loopback interface, one command runs
the complete application workflow: connect to MongoDB, process the inbox, store
and archive valid documents, then send expiration notifications for the selected
inclusive window:

```powershell
smart-doc-tracker --days-threshold 30 --language ita
```

Only `--days-threshold` is required. The OCR language defaults to `eng`, while
the inbox and processed folders default to `data/inbox` and `data/processed`.
The expiration check still runs when an individual inbox document fails, and the
command returns a non-zero exit code after reporting the aggregate results.

List all documents stored by this project:

```powershell
smart-doc-tracker --list-stored
```

Read one document using the `id` printed by either command:

```powershell
smart-doc-tracker --get-stored 64b64b64b64b64b64b64b64b
```

The default Ollama endpoint is `http://127.0.0.1:11434`. The client rejects remote
hosts, HTTPS endpoints, credentials, URL paths, and endpoints without an explicit
port. A different locally installed model can be selected with `--model`.

Structured output has this shape:

```json
{
  "document_type": "insurance_policy",
  "summary": "A vehicle insurance policy",
  "expiry_date": "2030-12-31",
  "issue_date": "2025-01-01",
  "extracted_data": {
    "policy_number": "P-123"
  }
}
```

## Local MongoDB storage

Start MongoDB on the loopback interface:

```powershell
docker compose up -d
```

Use the local repository from Python:

```python
from smart_doc_tracker.core.file_hash import calculate_file_sha256
from smart_doc_tracker.db.database import MongoDocumentRepository

file_hash = calculate_file_sha256("path/to/document.png")
with MongoDocumentRepository.connect() as repository:
    result = repository.insert_document(document, file_hash=file_hash)
    documents = repository.get_all_documents()
```

`insert_document` is idempotent: the unique SHA-256 file hash prevents duplicate
records, including under concurrent inserts. The repository also supports lookup
by ID, inclusive expiration windows, and exact nested searches such as
`search_by_dynamic_field("holder.city", "Rome")`. MongoDB URIs are rejected
unless they use plain `mongodb://` with an explicit loopback host and port.
The `documents` collection stores validated structured data and the source-file
hash; it does not copy the original image bytes into MongoDB.

## Local expiration monitoring

Run one expiration check and send a desktop notification for each document that
expires today or within the next 30 days:

```powershell
smart-doc-tracker --check-expirations
```

Use a different inclusive window when needed:

```powershell
smart-doc-tracker --check-expirations --days-threshold 14
```

Keep the application running in the foreground and perform the same check every
day at 09:00 in the host's local timezone:

```powershell
smart-doc-tracker --monitor-expirations --check-time 09:00 --days-threshold 30
```

The monitoring process must remain running. Stop it with `Ctrl+C`. Alerts contain
only the normalized document type and expiration date; OCR text and dynamic
document fields are never included. MongoDB, native notifications, and scheduling
remain local to the host.

### Automatic Windows task

Install a Windows Scheduled Task that performs the complete pipeline every day
at 09:00, independently of VS Code:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\manage_expiration_task.ps1 Install -CheckTime 09:00 -DaysThreshold 30 -OcrLanguage ita
```

The task runs as the current interactive Windows user so desktop notifications
can be displayed. It is configured to run as soon as possible after startup and
sign-in when the scheduled time was missed, and it may wake a sleeping computer.
A fully powered-off computer cannot run the check until it is started.

The scheduled runner verifies the Docker daemon. If needed, it starts Docker
Desktop and waits up to two minutes for it to become ready. It then starts the
project MongoDB service, without permitting an image pull, and waits for a
successful local database ping. Immediately after MongoDB is ready, it processes
the current inbox with the configured OCR language and then checks expirations.
An inbox failure does not suppress expiration reminders, but the scheduled task
still reports a failed result. Docker Desktop, the MongoDB image, Tesseract,
Ollama, and the selected local model must already be installed locally.

Running the install command again updates the existing task. Remove it with:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\manage_expiration_task.ps1 Uninstall
```

Supported formats are BMP, JPEG, PNG, TIFF, WebP, and PDF.

## Development checks

Install the package and local development tools in the virtual environment:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Run formatting, linting, static type checking, and the deterministic offline test
suite with branch coverage:

```powershell
.venv\Scripts\python.exe -m ruff format --check .
.venv\Scripts\python.exe -m ruff check .
.venv\Scripts\python.exe -m mypy
.venv\Scripts\python.exe -m pytest --cov --cov-report=term-missing
```

Coverage must remain at or above 80%. The existing standard-library test command
remains available when only the test suite is needed:

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests -t . -v
```
