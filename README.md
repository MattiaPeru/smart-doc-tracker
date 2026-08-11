# smart-doc-tracker
An intelligent, offline-first tool to manage personal paperwork. Combines Tesseract OCR and local LLMs to turn unstructured files into searchable, trackable data.

## Local OCR and structured parsing

The application reads a local image, extracts raw text with Tesseract, and can pass
that text to an Ollama model running exclusively on the loopback interface. The
model output is sanitized and validated as a hybrid Pydantic document: a fixed
metadata envelope plus a flexible `extracted_data` payload. No document data is
sent to remote services or persisted.

Requirements:

- Python 3.11 or newer
- Tesseract OCR installed locally and available on `PATH`
- The relevant Tesseract language packs (for example, `eng` or `ita`)
- Ollama installed locally with a model such as `qwen2.5:3b` (structured mode only)

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

Supported formats are BMP, JPEG, PNG, TIFF, and WebP. Run the deterministic,
offline test suite with:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```
