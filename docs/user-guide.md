# User Guide

## Scope

This guide covers the implemented command-line application. The final section
describes the planned FastAPI web interface and must not be interpreted as current
functionality.

## Prepare the local services

Install Python 3.11 or newer, Tesseract with the required language packs, Ollama, and
Docker. Create the virtual environment and install the package as shown in the
[README](../README.md).

Start MongoDB and ChromaDB:

```powershell
docker compose up -d mongodb chromadb
```

Confirm Ollama is running and the chosen structured and embedding models are already
installed locally.

## Process one document

Extract text only:

```powershell
smart-doc-tracker path\to\image.png --language ita
```

Extract and validate structured data:

```powershell
smart-doc-tracker path\to\document.pdf --language ita --structured
```

Persist and index the result:

```powershell
smart-doc-tracker path\to\document.pdf --language ita --structured --store
```

Storage requires structured parsing. A repeated file is recognized by SHA-256 and
does not create another primary MongoDB record. The output indicates whether the
record was newly inserted.

Use `--model`, `--ollama-url`, `--embedding-model`, and `--chroma-url` only for
locally installed services. Non-loopback endpoints are rejected.

## Process the inbox

Place supported files under `data/inbox`, then run:

```powershell
smart-doc-tracker --process-inbox --language ita
```

The command creates inbox and processed folders when necessary. Successful files
move to `data/processed`. Failed files remain available for inspection or retry.
Unsupported files, directories, and symbolic links remain untouched. Use custom
folders with:

```powershell
smart-doc-tracker --process-inbox --inbox-dir D:\Docs\inbox --processed-dir D:\Docs\processed --language ita
```

The complete daily workflow processes the inbox and checks expirations:

```powershell
smart-doc-tracker --days-threshold 30 --language ita
```

It returns a non-zero status if one or more inbox documents fail, even though the
expiration check still runs.

## Browse and edit records

List all records:

```powershell
smart-doc-tracker --list-stored
```

Read one record:

```powershell
smart-doc-tracker --get-stored DOCUMENT_ID
```

Update validated fields:

```powershell
smart-doc-tracker --update-stored DOCUMENT_ID --summary "Corrected summary" --expiry-date 2031-06-30
```

Editable fields are `document_type`, `summary`, `expiry_date`, `issue_date`, and
`extracted_data`. Pass `null` to a date option to clear it. Replace the complete
dynamic payload with a JSON object:

```powershell
smart-doc-tracker --update-stored DOCUMENT_ID --extracted-data-json '{"policy_number":"P-456"}'
```

Dynamic keys must use English `snake_case`. Updates preserve the source hash and
creation timestamp. The current update command does not rebuild the Chroma index;
semantic results may therefore reflect the originally indexed data until a future
reconciliation command is implemented.

Deletion is not available in the current CLI.

## Ask local questions

```powershell
smart-doc-tracker --ask-documents "Which insurance policies mention Rome?"
```

Use `--rag-results N` to control the maximum number of retrieved fragments. Answers
contain the document IDs used as sources. The answer is generated locally and can be
incomplete or inaccurate; inspect the referenced records before acting on it.

Questions about expirations in a specific or current year use normalized MongoDB
dates when recognized, providing deterministic results.

## Expiration reminders

Run one check:

```powershell
smart-doc-tracker --check-expirations --days-threshold 30
```

Run a foreground daily monitor:

```powershell
smart-doc-tracker --monitor-expirations --check-time 09:00 --days-threshold 30
```

The window is inclusive from today through the threshold. Documents already expired
before today are not included. Desktop notifications disclose only the normalized
document type and expiration date.

For Windows Scheduled Task installation, see [Operations](operations.md).

## Sensitive diagnostics

`--print-ocr-text` prints the exact extracted content to standard error. Use it only
on a private terminal and clear any captured output according to your data policy.
It is not required for normal operation.

Exit status `0` means the requested workflow completed, `1` means an operational or
processing failure, and `2` means invalid command input. `argparse` can also terminate
with status `2` for syntax errors.

## Local web interface

The local FastAPI application provides:

- drag-and-drop document upload;
- asynchronous progress and failure status;
- paginated document browsing and detail views;
- on-demand display of every summary, structured-data, and raw-text fragment
  stored for a document in local ChromaDB;
- validated edits and exact database filters;
- local natural-language questions with source links;
- an expiration dashboard and minimal in-app notifications;
- confirmed document deletion with an explicit description of affected data.

The application supports one user on the same host and binds only to loopback.
Uploading a document will return immediately to a job-status view while OCR, parsing,
storage, and indexing continue through a bounded local worker. Closing the browser
does not silently discard an accepted job.

Before confirming deletion, the UI must state whether the archived original file is
also removed and whether a backup may retain a copy. A successful result must mean
that MongoDB metadata and sections, Chroma fragments, and selected managed files have
all been handled according to policy.
