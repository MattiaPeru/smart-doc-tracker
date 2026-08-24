# Project Plan: Local AI Document Vault

## 1. Project Overview
The goal is to build a "Privacy-First" local application that acts as a smart, comprehensive manager for personal documents (ID cards, insurance policies, contracts, invoices). 
Operating 100% offline to guarantee absolute data privacy, the application automates the digitization process. It extracts text via OCR, uses a local LLM to understand and structure the data into dynamic JSON schemas using a **Hybrid Document Pattern (Base Envelope + Dynamic Payload)**, and stores everything in a local MongoDB database. While the initial core feature is automated expiration tracking, the system is designed to scale into a fully searchable document hub where users can categorize, query, and manage their paperwork regardless of the document type.

## 2. Tech Stack Architecture
*   **Language:** Python 3.11+
*   **OCR Module:** `pytesseract` (Tesseract) or `easyocr` (optimized for CPU processing).
*   **LLM Engine:** `Ollama` running locally (target models: `qwen2.5:3b` or `llama3.2:3b`).
*   **Data Validation:** `Pydantic` (to validate the Base Metadata envelope and dynamically capture document-specific fields).
*   **Database:** `MongoDB` (running locally via Docker) managed with `pymongo`.
*   **Notifications:** `plyer` or `win10toast` for native OS desktop notifications.
*   **Scheduler:** `APScheduler` or built-in OS task scheduling.

## 3. Directory Structure
```text
local-ai-doc-vault/
├── data/
│   ├── inbox/           # Directory to monitor for new incoming documents
│   └── processed/       # Destination for successfully parsed documents
├── src/
│   └── smart_doc_tracker/ # Installable package and canonical Python namespace
│       ├── core/        # Core business logic (e.g., OCR processing, LLM parsing)
│       ├── infrastructure/ # Local infrastructure adapters
│       ├── models/      # Hybrid Pydantic schemas (Base Envelope + Dynamic Payload)
│       └── __main__.py  # Python module entry point
├── tests/               # Unit and integration tests
├── docker-compose.yml   # Docker configuration for local MongoDB instance
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 4. Implementation Roadmap

### Phase 1: Proof of Concept (OCR + Extraction)
**Status: Implemented.**

*   Set up the Python environment (`venv`) and dependencies.
*   Implement a script to read a sample image file (e.g., a mockup ID card).
*   Integrate `pytesseract` to extract raw text from the image.
*   Output the raw text to the console for verification.

### Phase 2: Hybrid AI Parsing & Dynamic Structured Output
**Status: Implemented.**

*   Define a **Hybrid `Pydantic` Schema** consisting of:
    *   **Fixed Metadata Envelope:** Common required fields for system tasks (`document_type`, `summary`, `expiry_date`, `issue_date`).
    *   **Dynamic Payload (`extracted_data: Dict[str, Any]`):** A flexible dictionary field that captures all unique, document-specific attributes extracted by the LLM (e.g., tax code for ID cards, patient name for medical certificates, line items for invoices).
*   Implement the connection to the local `Ollama` instance.
*   Develop system prompts instructing the LLM to extract standard metadata into the fixed envelope while dynamically populating all other specific findings inside the `extracted_data` dictionary.
*   Parse, sanitize, and validate the LLM output into Python objects using Pydantic.

### Phase 3: Storage & Idempotency (MongoDB)
**Status: Implemented.**

*   Set up `docker-compose.yml` to spin up a local MongoDB container.
*   Initialize the `pymongo` client in `database.py` and connect to the local instance.
*   Implement a hashing mechanism (e.g., SHA-256) for incoming files to ensure the same document is not processed multiple times.
*   Create CRUD operations supporting both fixed envelope fields and dynamic sub-documents:
    *   `insert_document` (saving both envelope and `extracted_data`).
    *   `get_document_by_id`.
    *   `get_all_documents`.
    *   `get_expiring_documents(days_threshold)`.
    *   `search_by_dynamic_field(field_key, field_value)` (querying inside `extracted_data.<key>`).

### Phase 4: Active Monitoring (Expiration Tracking)
**Status: Implemented.**

*   Develop a query function to retrieve documents expiring within a specific timeframe (e.g., 30 days) from MongoDB via the standard `expiry_date` envelope field.
*   Integrate a native notification library (`plyer`) to trigger OS-level desktop alerts for these items.
*   Set up `APScheduler` to run the expiration check automatically on a daily basis.

### Phase 5: Pipeline Automation
**Status: Implemented.**

*   Establish the `data/inbox` directory structure.
*   Implement a startup scanner that processes the files currently in the inbox folder.
*   Connect the full pipeline: new file detected -> OCR -> Hybrid LLM Understanding -> MongoDB Insertion -> Move file to `data/processed`.

## 5. Known Edge Cases to Handle
*   **LLM Hallucinations & Unstructured Date Formats:** The LLM might return inconsistent dates inside both standard metadata and dynamic fields. Strict Pydantic validators/custom parsers must clean and convert dates to `datetime` objects before database insertion.
*   **Inconsistent Dynamic Key Naming:** Different runs on similar documents might generate slightly different keys in `extracted_data` (e.g., `tax_code` vs `fiscal_code`). System prompts must enforce clear naming conventions (snake_case, English keys).
*   **Hardware Constraints:** Processing large PDFs locally can lead to CPU throttling. The processing logic should handle files asynchronously or implement page-by-page extraction limits.
*   **Data Hygiene:** Any temporary image files generated during PDF-to-image conversion must be deleted immediately after OCR extraction.

## 6. Future Extensions (Scaling the Vault)
*   **RAG Implementation (Chat with your Documents):** Store the extracted text, summaries, and dynamic JSON values in a local Vector DB (like `ChromaDB`) to enable natural language queries across all document types.
*   **Local Web Dashboard:** Build a `Streamlit` or `FastAPI` interface to visualize documents, query dynamic JSON attributes, handle file uploads, and display color-coded expiration alerts.
