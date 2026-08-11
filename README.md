# smart-doc-tracker
An intelligent, offline-first tool to manage personal paperwork. Combines Tesseract OCR and local LLMs to turn unstructured files into searchable, trackable data.

## Local OCR and structured parsing

The application reads a local image, extracts raw text with Tesseract, and can pass
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
python -m pip install -r requirements.txt
```

Run OCR on a sample image:

```powershell
python src/main.py path\to\sample.png --language ita
```

Run OCR followed by validated local AI parsing:

```powershell
python src/main.py path\to\sample.png --language ita --structured
```

Process an image and store its validated data in local MongoDB:

```powershell
python src/main.py path\to\sample.png --language ita --structured --store
```

The command prints the MongoDB document ID, SHA-256 source-file hash, insertion
status, and validated document data. Repeating it with the same file returns
`"inserted": false` and does not create a duplicate.

List all documents stored by this project:

```powershell
python src/main.py --list-stored
```

Read one document using the `id` printed by either command:

```powershell
python src/main.py --get-stored 64b64b64b64b64b64b64b64b
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
from core.file_hash import calculate_file_sha256
from db.database import MongoDocumentRepository

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

Supported formats are BMP, JPEG, PNG, TIFF, and WebP. Run the deterministic,
offline test suite with:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```
