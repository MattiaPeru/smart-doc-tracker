const grid = document.querySelector("#document-grid");
const message = document.querySelector("#message");
const filterLabel = document.querySelector("#filter-label");
const dialog = document.querySelector("#document-dialog");

function showMessage(text, isError = false) {
  message.textContent = text;
  message.classList.toggle("error", isError);
  message.hidden = false;
}

function clearMessage() {
  message.hidden = true;
}

function expirationLabel(document) {
  if (!document.expiry_date) return "No expiry date";
  const labels = { expired: "Expired", soon: "Due soon", valid: "Valid" };
  return `${labels[document.expiration_status]} · ${document.expiry_date}`;
}

function renderDocuments(documents) {
  grid.replaceChildren();
  const counts = { expired: 0, soon: 0, valid: 0 };
  documents.forEach((item) => {
    if (counts[item.expiration_status] !== undefined) counts[item.expiration_status] += 1;
    const card = document.createElement("article");
    card.className = "document-card";
    card.tabIndex = 0;
    card.innerHTML = `
      <span class="status-bar ${item.expiration_status}"></span>
      <div><h3>${escapeHtml(item.document_type.replaceAll("_", " "))}</h3><p>${escapeHtml(item.summary)}</p></div>
      <div class="expiry"><small>Expiration</small>${escapeHtml(expirationLabel(item))}</div>`;
    const open = () => showDetail(item);
    card.addEventListener("click", open);
    card.addEventListener("keydown", (event) => { if (event.key === "Enter") open(); });
    grid.append(card);
  });
  if (!documents.length) {
    grid.innerHTML = '<p class="empty">No matching documents.</p>';
  }
  document.querySelector("#total-count").textContent = documents.length;
  document.querySelector("#expired-count").textContent = counts.expired;
  document.querySelector("#soon-count").textContent = counts.soon;
  document.querySelector("#valid-count").textContent = counts.valid;
}

function escapeHtml(value) {
  const element = window.document.createElement("span");
  element.textContent = String(value);
  return element.innerHTML;
}

function showDetail(item) {
  const detail = document.querySelector("#document-detail");
  detail.innerHTML = `
    <p class="eyebrow">${escapeHtml(expirationLabel(item))}</p>
    <h2>${escapeHtml(item.document_type.replaceAll("_", " "))}</h2>
    <dl class="detail-grid">
      <dt>Summary</dt><dd>${escapeHtml(item.summary)}</dd>
      <dt>Issue date</dt><dd>${escapeHtml(item.issue_date || "Not available")}</dd>
      <dt>Expiry date</dt><dd>${escapeHtml(item.expiry_date || "Not available")}</dd>
      <dt>Record ID</dt><dd><code>${escapeHtml(item.id)}</code></dd>
    </dl>
    <h3>Extracted attributes</h3>
    <pre>${escapeHtml(JSON.stringify(item.extracted_data, null, 2))}</pre>`;
  dialog.showModal();
}

async function loadDocuments(parameters = new URLSearchParams()) {
  clearMessage();
  try {
    const response = await fetch(`/api/documents?${parameters}`);
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.detail || "Documents could not be loaded.");
    renderDocuments(payload);
  } catch (error) {
    showMessage(error.message, true);
  }
}

document.querySelector("#query-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const data = new FormData(event.currentTarget);
  const parameters = new URLSearchParams({
    field_key: data.get("field_key"),
    field_value: data.get("field_value"),
  });
  filterLabel.textContent = `${data.get("field_key")} = ${data.get("field_value")}`;
  loadDocuments(parameters);
});

document.querySelector("#clear-query").addEventListener("click", () => {
  document.querySelector("#query-form").reset();
  filterLabel.textContent = "All records";
  loadDocuments();
});

document.querySelector("#refresh-button").addEventListener("click", () => loadDocuments());
document.querySelector("#close-dialog").addEventListener("click", () => dialog.close());

document.querySelector("#upload-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  clearMessage();
  const status = document.querySelector("#job-status");
  status.hidden = false;
  status.textContent = "Uploading…";
  try {
    const response = await fetch("/api/uploads", { method: "POST", body: new FormData(event.currentTarget) });
    const job = await response.json();
    if (!response.ok) throw new Error(job.detail || "Upload failed.");
    await monitorJob(job.id, status);
  } catch (error) {
    status.textContent = "Upload failed.";
    showMessage(error.message, true);
  }
});

async function monitorJob(jobId, status) {
  while (true) {
    const response = await fetch(`/api/jobs/${jobId}`);
    const job = await response.json();
    if (!response.ok) throw new Error(job.detail || "Job status is unavailable.");
    status.textContent = `Processing status: ${job.status}`;
    if (job.status === "completed") {
      showMessage(job.inserted ? "Document stored successfully." : "Document was already stored.");
      document.querySelector("#upload-form").reset();
      document.querySelector("#language").value = "eng";
      await loadDocuments();
      return;
    }
    if (job.status === "failed") throw new Error(job.error);
    await new Promise((resolve) => window.setTimeout(resolve, 800));
  }
}

loadDocuments();
