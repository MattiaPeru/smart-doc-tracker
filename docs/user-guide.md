# User Guide

## Scope

This guide covers the implemented command-line application and the loopback-only
FastAPI dashboard. Both use the same local services and validated domain model.

## Prepare the local services

Install Python 3.11 or newer, Tesseract with the required language packs, Ollama, and
Docker. Create the virtual environment and install the package as shown in the
[README](../README.md).

For CLI commands, start MongoDB and ChromaDB:

```powershell
docker compose up -d mongodb chromadb
```

The `smart-doc-tracker-web` command starts missing MongoDB, ChromaDB, and Ollama
services automatically and stops only the services it started when the server exits.
Docker Desktop must be running before starting the web command. Confirm the chosen
structured and embedding models are already installed locally; startup never
downloads models.

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
creation timestamp. CLI updates do not rebuild the Chroma index; semantic results may
therefore reflect the originally indexed data. Dashboard edits instead queue a
durable refresh of the summary and structured-data fragments while preserving the
original raw-text fragments.

Deletion is not available in the current CLI.

## Ask local questions

```powershell
smart-doc-tracker --ask-documents "Which insurance policies mention Rome?"
```

Use `--rag-results N` to control the maximum number of retrieved fragments. Answers
contain the document IDs used as sources. The answer is generated locally and can be
incomplete or inaccurate; inspect the referenced records before acting on it.

When a generated answer is rejected, use the following option on a private terminal
to print the rejected local-model response and the exact validation reason:

```powershell
smart-doc-tracker --ask-documents "Which skills are in my CV?" --show-rag-validation-details
```

The diagnostic output can contain sensitive excerpts from indexed documents. It is
not printed unless the option is explicitly supplied.

Questions about expirations in a specific or current year use normalized MongoDB
dates when recognized, providing deterministic results.

## Expiration reminders

Set the default reminder in the left side of the dashboard. Documents inherit that
value dynamically unless their edit form contains a custom number of days. Leaving
the document-specific field empty restores inheritance from the current default.

Run one check:

```powershell
smart-doc-tracker --check-expirations --days-threshold 30
```

Run a foreground daily monitor:

```powershell
smart-doc-tracker --monitor-expirations --check-time 09:00 --days-threshold 30
```

Omit `--days-threshold` in either expiration-only mode to use the dashboard default.

The window is inclusive from today through the threshold. Documents already expired
before today are not included. Desktop notifications disclose only the normalized
document type and expiration date.

For Windows Scheduled Task installation, see [Operations](operations.md).

## Sensitive diagnostics

`--print-ocr-text` prints the exact extracted content to standard error. Use it only
on a private terminal and clear any captured output according to your data policy.
It is not required for normal operation.

`--show-rag-validation-details` similarly prints a rejected local model response and
its validation reason to standard error. Do not use it in shared terminals, CI,
scheduled tasks, screenshots, or support logs.

Exit status `0` means the requested workflow completed, `1` means an operational or
processing failure, and `2` means invalid command input. `argparse` can also terminate
with status `2` for syntax errors.

## Local web interface

Start the local dashboard:

```powershell
smart-doc-tracker-web
```

Use `--host ::1` for IPv6 loopback or `--port PORT` to select another local port.
Public bind addresses are rejected and Uvicorn always runs one worker. Open
`http://127.0.0.1:8080` by default.

The implemented dashboard provides:

- drag-and-drop document upload;
- durable single-worker processing with visible extraction, parsing, and failure
  status;
- review and correction of validated extracted data before it is committed;
- document browsing and detail views;
- on-demand display of every summary, structured-data, and raw-text fragment
  stored for a document in local ChromaDB;
- validated edits with durable background refresh of indexed metadata;
- exact dynamic-field filters;
- expiration status and in-page alerts;
- a persistent default reminder and optional per-document reminder overrides;
- confirmed deletion from MongoDB and the active ChromaDB collection.

Uploads accept supported images and PDFs up to 25 MB. The server copies an accepted
upload into `data/processing_queue`, resumes interrupted queued work after restart,
and moves a successful parse into `data/pending_confirmation`. Pending manifests
contain the validated data and raw extracted text required for later indexing, so
protect these folders like the databases. Confirming stores and indexes the document,
then archives its source under `data/processed`; rejecting removes the staged source.
Failed jobs remain locally available until dismissed from the queue.

Dashboard deletion removes the primary MongoDB record, its PDF sections, and all
fragments for that document in the currently configured Chroma collection. It does
not remove `data/processed` files, other embedding-model collections, or backups.
Natural-language questions and pagination remain CLI-only or unavailable in the
dashboard.
