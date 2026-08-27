# Agent Workflow Map

## Single-document processing

```text
CLI or web request
  -> controller / durable upload job
  -> DocumentProcessingPipeline
  -> OCRExtractor or PDFPageExtractor
  -> StructuredDocumentParser or LongStructuredDocumentParser (optional)
  -> DocumentRepository (optional)
  -> DocumentVectorIndex (optional)
  -> sanitized result
```

Inputs are a local image or PDF path plus explicit processing options. Outputs are
`DocumentProcessingResult` and, when storage is enabled, `DocumentInsertResult`.
Parsing must produce validated `DocumentData` before persistence. A failed inbox item
stays in place; a successful one is archived under the processed folder.

## Document mutation

```text
controller or web route
  -> DocumentMutationPipeline
  -> snapshot repository and vector state
  -> update or delete repository record
  -> update or delete indexed fragments
  -> compensate from snapshots when a later operation fails
```

MongoDB and ChromaDB do not provide a shared transaction. Keep snapshot,
compensation, and operator-visible failure behavior together in the mutation
pipeline.

## Document questions

```text
question
  -> explicit expiry-year detection
     -> DocumentRepository date query
  OR
  -> DocumentQuestionPipeline
     -> DocumentVectorIndex query
     -> local TextGenerator
     -> validated DocumentAnswer
```

Calendar-year expiry questions bypass vector retrieval. General answers may cite
only document identifiers present in the locally retrieved context.

## Expiration notifications

```text
CLI, combined workflow, or scheduler
  -> ExpirationTrackingPipeline
  -> DocumentRepository date-window query
  -> prepared ExpirationNotification
  -> NotificationSender
```

The notifier receives a display label and normalized expiry date, never raw OCR text
or the dynamic extracted payload.

## Web upload lifecycle

```text
queued -> extracting -> parsing -> awaiting_confirmation -> confirmed
                                          |                    |
                                          -> rejected          -> indexed
Any active state may become failed with a sanitized public reason.
```

Job manifests exclude OCR text. Pending-confirmation data is sensitive and remains
local. Preserve atomic manifest replacement, restart recovery, explicit user
confirmation, and deterministic cleanup.
