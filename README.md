# smart-doc-tracker
An intelligent, offline-first tool to manage personal paperwork. Combines Tesseract OCR and local LLMs to turn unstructured files into searchable, trackable data.

## Phase 1: local image OCR

The current proof of concept reads a local image, extracts raw text with a locally
installed Tesseract executable, and writes that text to standard output. No document
data is sent over the network or persisted.

Requirements:

- Python 3.11 or newer
- Tesseract OCR installed locally and available on `PATH`
- The relevant Tesseract language packs (for example, `eng` or `ita`)

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

Supported formats are BMP, JPEG, PNG, TIFF, and WebP. Run the deterministic,
offline test suite with:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```
