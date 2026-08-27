import { addFieldRow, editorPayload } from "./attribute-editor.js";
import { renderAttributeView } from "./attribute-view.js";
import { requestError, userMessage, UserFacingError } from "./errors.js";
import { clearMessage, showMessage } from "./messages.js";

const grid = document.querySelector("#document-grid");
const queueGrid = document.querySelector("#queue-grid");
const pendingGrid = document.querySelector("#pending-grid");
const filterLabel = document.querySelector("#filter-label");
const dialog = document.querySelector("#document-dialog");
const reviewDialog = document.querySelector("#review-dialog");


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
    extracting: "Reading document",
    parsing: "Organizing information",
    failed: "We couldn't process this document",
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
    <div class="attribute-column-labels attribute-view-labels" aria-hidden="true"><span>Field name</span><span>Value</span></div>
    <div id="extracted-attributes" class="attribute-view"></div>
    <section class="indexed-content-section">
      <div class="attributes-heading"><h3>Complete indexed content</h3>
      <button id="load-indexed-content" class="secondary compact" type="button">Load content</button></div>
      <p class="sensitive-hint">Shows all the content saved for this document.</p>
      <div id="indexed-content" aria-live="polite"></div>
    </section>
    <div class="actions dialog-actions"><button id="edit-document" type="button">Edit</button>
    <button id="delete-document" class="danger-button" type="button">Delete</button></div>`;
  renderAttributeView(detail.querySelector("#extracted-attributes"), item.extracted_data);
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
  container.textContent = "Loading document content...";
  try {
    const response = await fetch(`/api/documents/${documentId}/indexed-content`);
    if (!response.ok) {
      throw requestError(response, "We couldn't load this document's content. Please try again.");
    }
    const payload = await response.json();
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
    container.textContent = userMessage(error, "We couldn't load this document's content. Please try again.");
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
      <div class="attribute-column-labels" aria-hidden="true"><span>Field name</span><span>Value</span></div>
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


async function saveEditor(event, identifier, isPending) {
  event.preventDefault();
  const form = event.currentTarget;
  const submitButton = form.querySelector('button[type="submit"]');
  const originalButtonText = submitButton.textContent;
  submitButton.disabled = true;
  submitButton.classList.add("is-saving");
  submitButton.textContent = "Saving...";
  form.setAttribute("aria-busy", "true");
  clearMessage();
  try {
    const endpoint = isPending ? `/api/pending-documents/${identifier}/confirm` : `/api/documents/${identifier}`;
    const response = await fetch(endpoint, {
      method: isPending ? "POST" : "PUT", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(editorPayload(form)),
    });
    if (!response.ok) {
      throw requestError(response, "We couldn't save the document. Check the information and try again.");
    }
    const saved = await response.json();
    reviewDialog.close();
    if (isPending) {
      showMessage("Document added successfully.");
    } else {
      showMessage("Changes saved. Search will be ready shortly.");
      monitorDocumentUpdate(saved.index_update_id);
    }
    Promise.all([loadDocuments(), loadPendingDocuments()]).catch(() => {
      showMessage("Changes are saved. Refresh the page to see the latest information.");
    });
  } catch (error) {
    const editorMessage = form.querySelector("#editor-message");
    editorMessage.textContent = userMessage(error, "We couldn't save the document. Please try again.");
    editorMessage.hidden = false;
    editorMessage.scrollIntoView({ block: "nearest" });
  } finally {
    submitButton.disabled = false;
    submitButton.classList.remove("is-saving");
    submitButton.textContent = originalButtonText;
    form.removeAttribute("aria-busy");
  }
}

async function monitorDocumentUpdate(updateId) {
  if (!updateId) return;
  for (let attempt = 0; attempt < 120; attempt += 1) {
    try {
      const response = await fetch(`/api/document-updates/${updateId}`);
      if (!response.ok) return;
      const update = await response.json();
      if (update.status === "completed") {
        showMessage("Changes saved successfully.");
        return;
      }
      if (update.status === "failed") {
        showMessage("Changes are saved. Search is taking longer than expected.");
        return;
      }
    } catch (_error) {
      return;
    }
    await new Promise((resolve) => window.setTimeout(resolve, 500));
  }
  showMessage("Changes are saved. Search is taking longer than expected.");
}

async function discardFailedJob(jobId) {
  if (!window.confirm("Remove this upload from the list?")) return;
  try {
    const response = await fetch(`/api/jobs/${jobId}`, { method: "DELETE" });
    if (!response.ok) throw requestError(response, "We couldn't remove this upload. Please try again.");
    showMessage("Upload removed.");
    await loadProcessingQueue();
  } catch (error) { showMessage(userMessage(error, "We couldn't remove this upload. Please try again."), true); }
}

async function deleteDocument(documentId) {
  if (!window.confirm("Delete this document? This action cannot be undone.")) return;
  try {
    const response = await fetch(`/api/documents/${documentId}`, { method: "DELETE" });
    if (!response.ok) throw requestError(response, "We couldn't delete this document. Please try again.");
    dialog.close();
    showMessage("Document deleted successfully.");
    await loadDocuments();
  } catch (error) { showMessage(userMessage(error, "We couldn't delete this document. Please try again."), true); }
}

async function rejectPending(pendingId) {
  if (!window.confirm("Discard this document? This action cannot be undone.")) return;
  try {
    const response = await fetch(`/api/pending-documents/${pendingId}`, { method: "DELETE" });
    if (!response.ok) {
      throw requestError(response, "We couldn't discard this document. Please try again.");
    }
    reviewDialog.close();
    showMessage("Document discarded.");
    await loadPendingDocuments();
  } catch (error) {
    showMessage(userMessage(error, "We couldn't discard this document. Please try again."), true);
  }
}

async function loadDocuments(parameters = new URLSearchParams()) {
  try {
    const response = await fetch(`/api/documents?${parameters}`);
    if (!response.ok) throw requestError(response, "We couldn't load your documents. Please try again.");
    const payload = await response.json();
    renderDocuments(payload);
  } catch (error) { showMessage(userMessage(error, "We couldn't load your documents. Please try again."), true); }
}

async function loadPendingDocuments() {
  try {
    const response = await fetch("/api/pending-documents");
    if (!response.ok) throw requestError(response, "We couldn't load documents awaiting review. Please try again.");
    const payload = await response.json();
    renderPending(payload);
  } catch (error) { showMessage(userMessage(error, "We couldn't load documents awaiting review. Please try again."), true); }
}

async function loadProcessingQueue() {
  try {
    const response = await fetch("/api/jobs");
    if (!response.ok) throw requestError(response, "We couldn't load documents being processed. Please try again.");
    const payload = await response.json();
    renderQueue(payload);
  } catch (error) { showMessage(userMessage(error, "We couldn't load documents being processed. Please try again."), true); }
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
    if (!response.ok) {
      throw requestError(response, "We couldn't upload this document. Choose a non-empty PDF or image and try again.");
    }
    const job = await response.json();
    form.reset();
    document.querySelector("#language").value = "eng";
    await loadProcessingQueue();
    selectView("queue");
    monitorJob(job.id).catch((error) => showMessage(
      userMessage(error, "We couldn't process this document. Please try again."), true,
    ));
  } catch (error) {
    showMessage(userMessage(error, "We couldn't upload this document. Please try again."), true);
  }
});

async function monitorJob(jobId) {
  while (true) {
    const response = await fetch(`/api/jobs/${jobId}`);
    if (!response.ok) throw requestError(response, "We couldn't check this document's progress. Please try again.");
    const job = await response.json();
    await loadProcessingQueue();
    if (job.status === "awaiting_confirmation") {
      await loadPendingDocuments();
      selectView("pending");
      return;
    }
    if (job.status === "failed") {
      throw new UserFacingError("We couldn't process this document. Check the file and try again.");
    }
    await new Promise((resolve) => window.setTimeout(resolve, 800));
  }
}

Promise.all([loadDocuments(), loadProcessingQueue(), loadPendingDocuments()]);
window.setInterval(() => {
  loadProcessingQueue();
  loadPendingDocuments();
}, 2000);
