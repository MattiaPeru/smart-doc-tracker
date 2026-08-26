const grid = document.querySelector("#document-grid");
const queueGrid = document.querySelector("#queue-grid");
const pendingGrid = document.querySelector("#pending-grid");
const message = document.querySelector("#message");
const filterLabel = document.querySelector("#filter-label");
const dialog = document.querySelector("#document-dialog");
const reviewDialog = document.querySelector("#review-dialog");

function showMessage(text, isError = false) {
  message.textContent = text;
  message.classList.toggle("error", isError);
  message.setAttribute("role", isError ? "alert" : "status");
  message.tabIndex = 0;
  message.title = "Click to dismiss";
  message.hidden = false;
}

function clearMessage() {
  message.hidden = true;
  message.removeAttribute("tabindex");
  message.removeAttribute("title");
}

message.addEventListener("click", clearMessage);
message.addEventListener("keydown", (event) => {
  if (event.key === "Enter" || event.key === " " || event.key === "Escape") {
    event.preventDefault();
    clearMessage();
  }
});

function expirationLabel(document) {
  if (!document.expiry_date) return "No expiry date";
  const labels = { expired: "Expired", soon: "Due soon", valid: "Valid" };
  return `${labels[document.expiration_status]} · ${document.expiry_date}`;
}

function escapeHtml(value) {
  const element = window.document.createElement("span");
  element.textContent = String(value);
  return element.innerHTML;
}

function renderDocuments(documents) {
  grid.replaceChildren();
  const counts = { expired: 0, soon: 0, valid: 0 };
  documents.forEach((item) => {
    if (counts[item.expiration_status] !== undefined) counts[item.expiration_status] += 1;
    const card = document.createElement("article");
    card.className = "document-card";
    card.tabIndex = 0;
    card.innerHTML = `<span class="status-bar ${item.expiration_status}"></span>
      <div><h3>${escapeHtml(item.document_type.replaceAll("_", " "))}</h3><p>${escapeHtml(item.summary)}</p></div>
      <div class="expiry"><small>Expiration</small>${escapeHtml(expirationLabel(item))}</div>`;
    const open = () => showDetail(item);
    card.addEventListener("click", open);
    card.addEventListener("keydown", (event) => { if (event.key === "Enter") open(); });
    grid.append(card);
  });
  if (!documents.length) grid.innerHTML = '<p class="empty">No matching documents.</p>';
  document.querySelector("#total-count").textContent = documents.length;
  document.querySelector("#expired-count").textContent = counts.expired;
  document.querySelector("#soon-count").textContent = counts.soon;
  document.querySelector("#valid-count").textContent = counts.valid;
}

function renderPending(items) {
  pendingGrid.replaceChildren();
  document.querySelector("#pending-count").textContent = items.length;
  items.forEach((item) => {
    const card = document.createElement("article");
    card.className = "document-card pending-card";
    card.tabIndex = 0;
    card.innerHTML = `<span class="status-bar pending"></span>
      <div><h3>${escapeHtml(item.document.document_type.replaceAll("_", " "))}</h3>
      <p>${escapeHtml(item.file_name)} · ${escapeHtml(item.document.summary)}</p></div>
      <div class="expiry">Review fields</div>`;
    const open = () => showEditor(item, true);
    card.addEventListener("click", open);
    card.addEventListener("keydown", (event) => { if (event.key === "Enter") open(); });
    pendingGrid.append(card);
  });
  if (!items.length) pendingGrid.innerHTML = '<p class="empty">No documents are awaiting confirmation.</p>';
}

function processingLabel(status) {
  const labels = {
    queued: "Waiting for processing",
    extracting: "OCR / text extraction",
    parsing: "Local LLM analysis",
    failed: "Processing failed",
  };
  return labels[status] || status.replaceAll("_", " ");
}

function renderQueue(items) {
  queueGrid.replaceChildren();
  document.querySelector("#queue-count").textContent = items.length;
  let queuedPosition = 0;
  items.forEach((item) => {
    const card = document.createElement("article");
    card.className = "document-card queue-card";
    const failed = item.status === "failed";
    if (item.status === "queued") queuedPosition += 1;
    const position = item.status === "queued" ? `Position ${queuedPosition}` : "In progress";
    card.innerHTML = `<span class="status-bar ${failed ? "expired" : "queue"}"></span>
      <div><h3>${escapeHtml(item.file_name)}</h3>
      <p>${escapeHtml(processingLabel(item.status))}</p></div>
      <div class="expiry">${failed
        ? `<span>Needs attention</span><button class="danger-button compact discard-job" type="button">Remove</button>`
        : escapeHtml(position)}</div>`;
    if (failed) {
      card.querySelector(".discard-job").addEventListener("click", () => discardFailedJob(item.id));
    }
    queueGrid.append(card);
  });
  if (!items.length) queueGrid.innerHTML = '<p class="empty">No documents are waiting to be processed.</p>';
}

function showDetail(item) {
  const detail = document.querySelector("#document-detail");
  detail.innerHTML = `<p class="eyebrow">${escapeHtml(expirationLabel(item))}</p>
    <h2>${escapeHtml(item.document_type.replaceAll("_", " "))}</h2>
    <dl class="detail-grid">
      <dt>Summary</dt><dd>${escapeHtml(item.summary)}</dd>
      <dt>Issue date</dt><dd>${escapeHtml(item.issue_date || "Not available")}</dd>
      <dt>Expiry date</dt><dd>${escapeHtml(item.expiry_date || "Not available")}</dd>
      <dt>Record ID</dt><dd><code>${escapeHtml(item.id)}</code></dd>
    </dl>
    <h3>Extracted attributes</h3>
    <pre>${escapeHtml(JSON.stringify(item.extracted_data, null, 2))}</pre>
    <section class="indexed-content-section">
      <div class="attributes-heading"><h3>Complete indexed content</h3>
      <button id="load-indexed-content" class="secondary compact" type="button">Load content</button></div>
      <p class="sensitive-hint">Loads every summary, structured-data, and raw-text fragment stored locally in ChromaDB.</p>
      <div id="indexed-content" aria-live="polite"></div>
    </section>
    <div class="actions dialog-actions"><button id="edit-document" type="button">Edit</button>
    <button id="delete-document" class="danger-button" type="button">Delete</button></div>`;
  detail.querySelector("#load-indexed-content").addEventListener("click", (event) => {
    loadIndexedContent(item.id, event.currentTarget, detail.querySelector("#indexed-content"));
  });
  detail.querySelector("#edit-document").addEventListener("click", () => {
    dialog.close();
    showEditor({ id: item.id, document: item }, false);
  });
  detail.querySelector("#delete-document").addEventListener("click", () => deleteDocument(item.id));
  dialog.showModal();
}

async function loadIndexedContent(documentId, button, container) {
  button.disabled = true;
  button.textContent = "Loading...";
  container.textContent = "Reading local index...";
  try {
    const response = await fetch(`/api/documents/${documentId}/indexed-content`);
    const payload = await response.json();
    if (!response.ok) throw new Error(apiError(payload, "Indexed content could not be loaded."));
    container.replaceChildren();
    payload.fragments.forEach((fragment) => {
      const article = document.createElement("article");
      article.className = "indexed-fragment";
      const heading = document.createElement("h4");
      heading.textContent = `${fragment.source.replaceAll("_", " ")} · ${fragment.fragment_id}`;
      const content = document.createElement("pre");
      content.textContent = fragment.content;
      article.append(heading, content);
      container.append(article);
    });
    if (!payload.fragments.length) container.textContent = "No indexed content is available for this document.";
    button.textContent = "Reload content";
  } catch (error) {
    container.textContent = error.message;
    button.textContent = "Try again";
  } finally {
    button.disabled = false;
  }
}

function showEditor(item, isPending) {
  const documentData = item.document;
  const detail = document.querySelector("#review-detail");
  detail.innerHTML = `<p class="eyebrow">${isPending ? "Confirm extracted data" : "Edit stored document"}</p>
    <h2>${isPending ? escapeHtml(item.file_name) : "Document fields"}</h2>
    <form id="document-editor">
      <label for="edit-document-type">Document type</label>
      <input id="edit-document-type" name="document_type" maxlength="100" required value="${escapeHtml(documentData.document_type)}">
      <label for="edit-summary">Summary</label>
      <textarea id="edit-summary" name="summary" maxlength="1000" required>${escapeHtml(documentData.summary)}</textarea>
      <div class="date-fields">
        <div><label for="edit-issue-date">Issue date</label><input id="edit-issue-date" name="issue_date" type="date" value="${escapeHtml(documentData.issue_date || "")}"></div>
        <div><label for="edit-expiry-date">Expiry date</label><input id="edit-expiry-date" name="expiry_date" type="date" value="${escapeHtml(documentData.expiry_date || "")}"></div>
      </div>
      <div class="attributes-heading"><h3>Extracted attributes</h3><button id="add-field" class="secondary compact" type="button">Add field</button></div>
      <div id="attribute-fields"></div>
      <div id="editor-message" class="editor-message" role="alert" hidden></div>
      <div class="actions dialog-actions"><button type="submit">${isPending ? "Confirm and save" : "Save changes"}</button>
      ${isPending ? '<button id="reject-pending" class="danger-button" type="button">Reject</button>' : ""}</div>
    </form>`;
  const fields = detail.querySelector("#attribute-fields");
  Object.entries(documentData.extracted_data).forEach(([key, value]) => addFieldRow(fields, key, value));
  detail.querySelector("#add-field").addEventListener("click", () => addFieldRow(fields));
  detail.querySelector("#document-editor").addEventListener("submit", (event) => saveEditor(event, item.id, isPending));
  if (isPending) detail.querySelector("#reject-pending").addEventListener("click", () => rejectPending(item.id));
  reviewDialog.showModal();
}

function addFieldRow(container, key = "", value = "") {
  const row = document.createElement("div");
  row.className = "attribute-row";
  const serialized = typeof value === "string" ? value : JSON.stringify(value);
  const keyInput = document.createElement("input");
  keyInput.className = "attribute-key";
  keyInput.setAttribute("aria-label", "Attribute name");
  keyInput.placeholder = "field_name";
  keyInput.value = key;
  keyInput.required = true;

  const valueInput = document.createElement("input");
  valueInput.className = "attribute-value";
  valueInput.setAttribute("aria-label", "Attribute value");
  valueInput.placeholder = "Value or JSON";
  valueInput.value = serialized;

  const removeButton = document.createElement("button");
  removeButton.className = "secondary compact remove-field";
  removeButton.type = "button";
  removeButton.setAttribute("aria-label", "Remove attribute");
  removeButton.textContent = "\u00d7";
  removeButton.addEventListener("click", () => row.remove());

  row.append(keyInput, valueInput, removeButton);
  container.append(row);
}

function editorPayload(form) {
  const data = new FormData(form);
  const extractedData = {};
  form.querySelectorAll(".attribute-row").forEach((row) => {
    const key = row.querySelector(".attribute-key").value.trim();
    const valueInput = row.querySelector(".attribute-value");
    const rawValue = valueInput.value.trim();
    if (!key) throw new Error("Every custom field must have a name.");
    if (/^[\[{]+$/.test(rawValue)) {
      valueInput.focus();
      throw new Error(`Field "${key}" contains incomplete JSON. Replace it with valid JSON (for example []) or remove the field.`);
    }
    try { extractedData[key] = JSON.parse(rawValue); } catch (_error) { extractedData[key] = rawValue; }
  });
  return {
    document_type: data.get("document_type"), summary: data.get("summary"),
    issue_date: data.get("issue_date") || null, expiry_date: data.get("expiry_date") || null,
    extracted_data: extractedData,
  };
}

function apiError(payload, fallback) {
  if (Array.isArray(payload.detail)) return payload.detail.map((item) => item.msg).join("; ");
  return payload.detail || fallback;
}

async function saveEditor(event, identifier, isPending) {
  event.preventDefault();
  const form = event.currentTarget;
  clearMessage();
  try {
    const endpoint = isPending ? `/api/pending-documents/${identifier}/confirm` : `/api/documents/${identifier}`;
    const response = await fetch(endpoint, {
      method: isPending ? "POST" : "PUT", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(editorPayload(form)),
    });
    const payload = await response.json();
    if (!response.ok) throw new Error(apiError(payload, "The document could not be saved."));
    reviewDialog.close();
    showMessage(isPending ? "Document confirmed and stored." : "Document updated in both local stores.");
    await Promise.all([loadDocuments(), loadPendingDocuments()]);
  } catch (error) {
    const editorMessage = form.querySelector("#editor-message");
    editorMessage.textContent = error.message;
    editorMessage.hidden = false;
    editorMessage.scrollIntoView({ block: "nearest" });
  }
}

async function discardFailedJob(jobId) {
  if (!window.confirm("Remove this failed upload and its local queued file?")) return;
  try {
    const response = await fetch(`/api/jobs/${jobId}`, { method: "DELETE" });
    if (!response.ok) throw new Error(apiError(await response.json(), "The failed upload could not be removed."));
    showMessage("Failed upload removed.");
    await loadProcessingQueue();
  } catch (error) { showMessage(error.message, true); }
}

async function deleteDocument(documentId) {
  if (!window.confirm("Delete this document from MongoDB and ChromaDB?")) return;
  try {
    const response = await fetch(`/api/documents/${documentId}`, { method: "DELETE" });
    if (!response.ok) throw new Error(apiError(await response.json(), "The document could not be deleted."));
    dialog.close();
    showMessage("Document deleted from both local stores.");
    await loadDocuments();
  } catch (error) { showMessage(error.message, true); }
}

async function rejectPending(pendingId) {
  if (!window.confirm("Reject this upload and remove its temporary local file?")) return;
  const response = await fetch(`/api/pending-documents/${pendingId}`, { method: "DELETE" });
  if (!response.ok) {
    showMessage(apiError(await response.json(), "The pending document could not be rejected."), true);
    return;
  }
  reviewDialog.close();
  showMessage("Pending document rejected.");
  await loadPendingDocuments();
}

async function loadDocuments(parameters = new URLSearchParams()) {
  try {
    const response = await fetch(`/api/documents?${parameters}`);
    const payload = await response.json();
    if (!response.ok) throw new Error(apiError(payload, "Documents could not be loaded."));
    renderDocuments(payload);
  } catch (error) { showMessage(error.message, true); }
}

async function loadPendingDocuments() {
  try {
    const response = await fetch("/api/pending-documents");
    const payload = await response.json();
    if (!response.ok) throw new Error(apiError(payload, "Pending documents could not be loaded."));
    renderPending(payload);
  } catch (error) { showMessage(error.message, true); }
}

async function loadProcessingQueue() {
  try {
    const response = await fetch("/api/jobs");
    const payload = await response.json();
    if (!response.ok) throw new Error(apiError(payload, "The processing queue could not be loaded."));
    renderQueue(payload);
  } catch (error) { showMessage(error.message, true); }
}

function selectView(view) {
  ["documents", "queue", "pending"].forEach((name) => {
    document.querySelector(`#${name}-panel`).hidden = name !== view;
    document.querySelector(`#${name}-tab`).classList.toggle("active", name === view);
  });
  if (view === "queue") loadProcessingQueue();
  if (view === "pending") loadPendingDocuments();
}

document.querySelector("#query-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const data = new FormData(event.currentTarget);
  const parameters = new URLSearchParams({ field_key: data.get("field_key"), field_value: data.get("field_value") });
  filterLabel.textContent = `${data.get("field_key")} = ${data.get("field_value")}`;
  loadDocuments(parameters);
});
document.querySelector("#clear-query").addEventListener("click", () => {
  document.querySelector("#query-form").reset();
  filterLabel.textContent = "All records";
  loadDocuments();
});
document.querySelector("#documents-tab").addEventListener("click", () => selectView("documents"));
document.querySelector("#queue-tab").addEventListener("click", () => selectView("queue"));
document.querySelector("#pending-tab").addEventListener("click", () => selectView("pending"));
document.querySelector("#refresh-button").addEventListener("click", () => Promise.all([loadDocuments(), loadProcessingQueue(), loadPendingDocuments()]));
document.querySelector("#close-dialog").addEventListener("click", () => dialog.close());
document.querySelector("#close-review-dialog").addEventListener("click", () => reviewDialog.close());

document.querySelector("#upload-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  clearMessage();
  try {
    const response = await fetch("/api/uploads", { method: "POST", body: new FormData(form) });
    const job = await response.json();
    if (!response.ok) throw new Error(apiError(job, "Upload failed."));
    form.reset();
    document.querySelector("#language").value = "eng";
    await loadProcessingQueue();
    selectView("queue");
    monitorJob(job.id).catch((error) => showMessage(error.message, true));
  } catch (error) {
    showMessage(error.message, true);
  }
});

async function monitorJob(jobId) {
  while (true) {
    const response = await fetch(`/api/jobs/${jobId}`);
    const job = await response.json();
    if (!response.ok) throw new Error(apiError(job, "Job status is unavailable."));
    await loadProcessingQueue();
    if (job.status === "awaiting_confirmation") {
      await loadPendingDocuments();
      selectView("pending");
      return;
    }
    if (job.status === "failed") throw new Error(job.error);
    await new Promise((resolve) => window.setTimeout(resolve, 800));
  }
}

Promise.all([loadDocuments(), loadProcessingQueue(), loadPendingDocuments()]);
window.setInterval(() => {
  loadProcessingQueue();
  loadPendingDocuments();
}, 2000);
