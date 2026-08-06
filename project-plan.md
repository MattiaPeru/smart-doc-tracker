# Project Plan: Local AI Document Vault

## 1. Project Overview
The goal is to build a "Privacy-First" local application that acts as a smart, comprehensive manager for personal documents (ID cards, insurance policies, contracts, invoices). 
Operating 100% offline to guarantee absolute data privacy, the application automates the digitization process. It extracts text via OCR, uses a local LLM to understand and structure the data into dynamic JSON schemas, and stores everything in a local MongoDB database. While the initial core feature is automated expiration tracking, the system is designed to scale into a fully searchable document hub where users can categorize, query, and manage their paperwork.

## 2. Tech Stack Architecture
*   **Language:** Python 3.11+
*   **OCR Module:** `pytesseract` (Tesseract) or `easyocr` (optimized for CPU processing).
*   **LLM Engine:** `Ollama` running locally (target models: `qwen2.5:3b` or `llama3.2:3b`).
*   **Data Validation:** `Pydantic` (to enforce structured JSON outputs from the LLM).
*   **Database:** `MongoDB` (running locally via Docker) managed with `pymongo`.
*   **Notifications:** `plyer` or `win10toast` for native OS desktop notifications.
*   **Scheduler:** `APScheduler` or built-in OS task scheduling.

## 3. Directory Structure
To maintain a modular and clean architecture, the project must strictly follow this directory layout:

```text
local-ai-doc-vault/
├── data/
│   ├── inbox/           # Directory to monitor for new incoming documents
│   └── processed/       # Destination for successfully parsed documents
├── src/                 # Main source code directory
│   ├── core/            # Core business logic (e.g., OCR processing, LLM parsing)
│   ├── infrastructure/  # External integrations (e.g., MongoDB, Notifications)
│   ├── models/          # Data schemas and Pydantic models
│   └── main.py          # Entry point and pipeline orchestrator
├── tests/               # Unit and integration tests
├── docker-compose.yml   # Docker configuration for local MongoDB instance
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 4. Implementation Roadmap

### Phase 1: Proof of Concept (OCR + Extraction)
*   Set up the Python environment (`venv`) and dependencies.
*   Implement a script to read a sample image file (e.g., a mockup ID card).
*   Integrate `pytesseract` to extract raw text from the image.
*   Output the raw text to the console for verification.

### Phase 2: AI Parsing & Structured Output
*   Define a `Pydantic` schema for a generic document model (e.g., fields for `title`, `category`, `issue_date`, `expiry_date`, `document_number`, `summary`).
*   Implement the connection to the local `Ollama` instance.
*   Develop the prompt logic to send the OCR raw text to the LLM, instructing it to understand the context and return a JSON response matching the Pydantic schema.
*   Parse and validate the output into a Python dictionary.

### Phase 3: Storage & Idempotency (MongoDB)
*   Set up the `docker-compose.yml` to spin up a local MongoDB container.
*   Initialize the `pymongo` client in `database.py` and connect to the local instance.
*   Implement a hashing mechanism (e.g., SHA-256) for incoming files to ensure the same document is not processed multiple times.
*   Create CRUD operations: `insert_document`, `get_document_by_id`, `get_all_documents`, and `get_expiring_documents(days_threshold)`.

### Phase 4: Active Monitoring (Expiration Tracking)
*   Develop a query function to retrieve documents expiring within a specific timeframe (e.g., 30 days) from MongoDB.
*   Integrate a native notification library (`plyer`) to trigger OS-level desktop alerts for these items.
*   Set up `APScheduler` to run the expiration check automatically on a daily basis.

### Phase 5: Pipeline Automation
*   Establish the `data/inbox` directory structure.
*   Implement a file system watcher (e.g., using `watchdog`) or a startup scanner that monitors the inbox folder.
*   Connect the full pipeline: new file detected -> OCR -> LLM Understanding -> MongoDB Insertion -> Move file to `data/processed`.

## 5. Known Edge Cases to Handle
*   **LLM Hallucinations:** The LLM might misinterpret date formats (e.g., confusing O and 0, or mixing DD/MM/YYYY with MM/DD/YYYY). Strict Pydantic validators must be in place to sanitize and standardize date strings.
*   **Hardware Constraints:** Processing large PDFs locally can lead to CPU throttling. The processing logic should handle files asynchronously or implement page-by-page extraction limits.
*   **Data Hygiene:** Any temporary image files generated during PDF-to-image conversion must be deleted immediately after OCR extraction.

## 6. Future Extensions (Scaling the Vault)
*   **Dynamic Schema Selection (Zero-Shot Classification):** Upgrade the LLM prompt to automatically classify the document type and dynamically select the most appropriate Pydantic schema based on the context.
*   **RAG Implementation (Chat with your Documents):** Store the extracted text and summaries in a local Vector DB (like `ChromaDB`) to enable a conversational interface for querying document details (e.g., "What is the deductible on my car insurance?").
*   **Local Web Dashboard:** Build a `Streamlit` or `FastAPI` interface to visualize the database, handle manual file uploads, display color-coded expiration warnings, and provide a search bar for the document vault.