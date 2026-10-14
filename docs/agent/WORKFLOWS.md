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
  -> verify MongoDB and ChromaDB after insertion or deletion
  -> retain a durable pending insertion until both stores and its source link commit
  -> retry incomplete confirmations when local services recover
  -> remove or restore the archived source during deletion
```

MongoDB and ChromaDB do not provide a shared transaction. The web confirmation
manifest tracks partial inserts across restarts and keeps them out of the completed
document list. A stopped Chroma service leaves the MongoDB record pending for
automatic retry. Two insertion errors while Chroma remains reachable cause both
store entries to be cleaned and the original upload to move to the failed upload
queue. Retrying that job starts again with OCR. Keep snapshot, compensation, and
operator-visible failure behavior in the mutation pipeline.

## Document questions

```text
question + optional process-local conversation ID
  -> bounded temporary history lookup
  -> explicit expiry-year detection
     -> DocumentRepository date query
  OR
  -> DocumentQuestionPipeline
     -> contextual DocumentVectorIndex query
     -> previously cited local document fragments (follow-up questions only)
     -> local TextGenerator
     -> validated DocumentAnswer
  -> completed exchange retained in memory until cleared, expired, or shutdown
```

Calendar-year expiry questions bypass vector retrieval. General answers may cite
only document identifiers present in the locally retrieved context. Temporary chat
history is bounded, isolated by conversation ID, never persisted, and used only to
resolve follow-up references; document context remains the sole factual evidence.

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
                                          -> rejected          -> inserting -> indexed
Any active state may become failed with a sanitized public reason. A confirmed
document remains in insertion until MongoDB and ChromaDB are both verified; the
server retries incomplete insertions periodically. Repeated reachable index errors
move the source to the failed processing queue for an explicit OCR retry or removal.
```

Job manifests exclude OCR text. Pending-confirmation data is sensitive and remains
local. Preserve atomic manifest replacement, restart recovery, explicit user
confirmation, and deterministic cleanup.
