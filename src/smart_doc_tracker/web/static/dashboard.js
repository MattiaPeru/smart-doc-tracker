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
    <div class="attribute-column-labels attribute-view-labels" aria-hidden="true"><span>Field name</span><span>Value</span></div>
    <div id="extracted-attributes" class="attribute-view"></div>
    <section class="indexed-content-section">
      <div class="attributes-heading"><h3>Complete indexed content</h3>
      <button id="load-indexed-content" class="secondary compact" type="button">Load content</button></div>
      <p class="sensitive-hint">Loads every summary, structured-data, and raw-text fragment stored locally in ChromaDB.</p>
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

function addFieldRow(container, key = "", value = "") {
  addValueNode(container, key, value, false);
}

function containerKind(value) {
  if (Array.isArray(value)) {
    const objects = value.length > 0 && value.every((item) => item !== null && typeof item === "object" && !Array.isArray(item));
    if (objects && value.every((item) => {
      const keys = Object.keys(item);
      return keys.length === 2 && keys.includes("type") && keys.includes("value") && typeof item.type === "string";
    })) return "typed-array";
    if (objects && value.every((item) => {
        const keys = Object.keys(item);
        const itemValue = item[keys[0]];
        return keys.length === 1
          && (itemValue === null || typeof itemValue !== "object");
      })) return "single-field-array";
    if (value.length > 0 && value.every((item) => item === null || typeof item !== "object")) {
      return "scalar-array";
    }
    return "array";
  }
  if (value !== null && typeof value === "object") return "object";
  return "scalar";
}

function isArrayKind(kind) {
  return kind === "array" || kind === "typed-array" || kind === "single-field-array" || kind === "scalar-array";
}

function fieldLabel(value) {
  const normalized = String(value).replaceAll("_", " ");
  return normalized.charAt(0).toUpperCase() + normalized.slice(1);
}

function containerEntries(kind, value, itemField = "") {
  if (kind === "typed-array") return value.map((item) => [item.type, item.value]);
  if (kind === "single-field-array") {
    return value.map((item, index) => [`${fieldLabel(itemField)} ${index + 1}`, item[itemField]]);
  }
  if (kind === "array") return Array.from(value.entries()).map(([index, item]) => [`Item ${index + 1}`, item]);
  return Object.entries(value);
}

function groupedSingleFieldItems(value) {
  const groups = new Map();
  value.forEach((item, originalIndex) => {
    const itemField = Object.keys(item)[0];
    if (!groups.has(itemField)) groups.set(itemField, []);
    groups.get(itemField).push({ value: item[itemField], originalIndex });
  });
  return groups;
}

function createKeyControl(key, isArrayItem) {
  if (isArrayItem) {
    const label = document.createElement("span");
    label.className = "attribute-key attribute-key-label";
    label.textContent = key;
    return label;
  }
  const input = document.createElement("input");
  input.className = "attribute-key";
  input.setAttribute("aria-label", "Field name");
  input.placeholder = "Field name";
  input.value = key;
  return input;
}

function displayScalarValue(value) {
  if (value === null || value === undefined) return "Not available";
  if (typeof value === "boolean") return value ? "Yes" : "No";
  return String(value);
}

function addAttributeViewNode(container, key, value) {
  const kind = containerKind(value);
  if (kind === "scalar-array") {
    const row = document.createElement("div");
    row.className = "attribute-view-row compact-list-view-row";
    const keyLabel = document.createElement("span");
    keyLabel.className = "attribute-view-key";
    keyLabel.textContent = key;
    const values = document.createElement("span");
    values.className = "compact-list-view-values";
    value.forEach((item) => {
      const itemValue = document.createElement("span");
      itemValue.className = "compact-list-view-value";
      itemValue.textContent = displayScalarValue(item);
      values.append(itemValue);
    });
    row.append(keyLabel, values);
    container.append(row);
    return;
  }
  if (kind === "single-field-array") {
    const details = document.createElement("details");
    details.className = "nested-value attribute-view-group grouped-list-view";
    const summary = document.createElement("summary");
    const summaryContent = document.createElement("span");
    summaryContent.className = "attribute-view-summary-content";
    const keyLabel = document.createElement("span");
    keyLabel.className = "attribute-view-key";
    keyLabel.textContent = key;
    const countLabel = document.createElement("span");
    countLabel.textContent = `${value.length} ${value.length === 1 ? "item" : "items"}`;
    summaryContent.append(keyLabel, countLabel);
    summary.append(summaryContent);

    const children = document.createElement("div");
    children.className = "attribute-view-children";
    groupedSingleFieldItems(value).forEach((items, itemField) => {
      const row = document.createElement("div");
      row.className = "attribute-view-row compact-list-view-row";
      const fieldLabel = document.createElement("span");
      fieldLabel.className = "attribute-view-key";
      fieldLabel.textContent = itemField;
      const values = document.createElement("span");
      values.className = "compact-list-view-values";
      items.forEach((item) => {
        const itemValue = document.createElement("span");
        itemValue.className = "compact-list-view-value";
        itemValue.textContent = displayScalarValue(item.value);
        values.append(itemValue);
      });
      row.append(fieldLabel, values);
      children.append(row);
    });
    details.append(summary, children);
    container.append(details);
    return;
  }
  if (kind === "scalar") {
    const row = document.createElement("div");
    row.className = "attribute-view-row";
    const keyLabel = document.createElement("span");
    keyLabel.className = "attribute-view-key";
    keyLabel.textContent = key;
    const valueLabel = document.createElement("span");
    valueLabel.className = "attribute-view-value";
    valueLabel.textContent = displayScalarValue(value);
    row.append(keyLabel, valueLabel);
    container.append(row);
    return;
  }

  const details = document.createElement("details");
  details.className = "nested-value attribute-view-group";
  const summary = document.createElement("summary");
  const summaryContent = document.createElement("span");
  summaryContent.className = "attribute-view-summary-content";
  const keyLabel = document.createElement("span");
  keyLabel.className = "attribute-view-key";
  keyLabel.textContent = key;
  const countLabel = document.createElement("span");
  const itemField = kind === "single-field-array" ? Object.keys(value[0])[0] : "";
  const entries = containerEntries(kind, value, itemField);
  const noun = isArrayKind(kind) ? (entries.length === 1 ? "item" : "items") : (entries.length === 1 ? "field" : "fields");
  countLabel.textContent = `${entries.length} ${noun}`;
  summaryContent.append(keyLabel, countLabel);
  summary.append(summaryContent);
  details.append(summary);

  const children = document.createElement("div");
  children.className = "attribute-view-children";
  entries.forEach(([childKey, childValue]) => {
    addAttributeViewNode(children, childKey, childValue);
  });
  details.append(children);
  container.append(details);
}

function renderAttributeView(container, data) {
  Object.entries(data).forEach(([key, value]) => addAttributeViewNode(container, key, value));
  if (!container.children.length) container.textContent = "No extracted attributes.";
}

function createScalarControl(value) {
  let input;
  if (typeof value === "boolean") {
    input = document.createElement("select");
    [["true", "Yes"], ["false", "No"]].forEach(([optionValue, label]) => {
      const option = document.createElement("option");
      option.value = optionValue;
      option.textContent = label;
      input.append(option);
    });
    input.value = String(value);
  } else {
    input = document.createElement("input");
    input.value = value === null || value === undefined ? "" : String(value);
    input.placeholder = value === null ? "Not available" : "Value";
    if (typeof value === "number") {
      input.type = "number";
      input.step = "any";
    }
  }
  input.className = "attribute-value";
  input.setAttribute("aria-label", "Field value");
  return input;
}

function scalarType(value) {
  return value === null || value === undefined ? "null" : typeof value;
}

function addCompactListItem(container, value, onRemove = null, originalIndex = null) {
  const item = document.createElement("div");
  item.className = "compact-list-item";
  item.dataset.scalarType = scalarType(value);
  if (originalIndex !== null) item.dataset.originalIndex = String(originalIndex);
  item.append(createScalarControl(value));

  const removeButton = document.createElement("button");
  removeButton.className = "secondary compact compact-list-remove";
  removeButton.type = "button";
  removeButton.setAttribute("aria-label", "Remove list item");
  removeButton.textContent = "\u00d7";
  removeButton.addEventListener("click", () => {
    item.remove();
    if (onRemove) onRemove();
  });
  item.append(removeButton);
  container.append(item);
}

function addGroupedListRow(container, node, itemField, items) {
  const groupedRow = document.createElement("div");
  groupedRow.className = "grouped-list-row";
  const fieldInput = document.createElement("input");
  fieldInput.className = "grouped-list-key";
  fieldInput.setAttribute("aria-label", "Field name");
  fieldInput.value = itemField;
  const list = document.createElement("div");
  list.className = "compact-list-editor";
  items.forEach((item) => addCompactListItem(
    list,
    item.value,
    () => updateContainerSummary(node),
    item.originalIndex,
  ));
  const addButton = document.createElement("button");
  addButton.className = "secondary compact add-compact-list-item";
  addButton.type = "button";
  addButton.textContent = "Add item";
  addButton.addEventListener("click", () => {
    addCompactListItem(list, "", () => updateContainerSummary(node));
    list.append(addButton);
    updateContainerSummary(node);
  });
  list.append(addButton);
  groupedRow.append(fieldInput, list);
  container.append(groupedRow);
}

function updateContainerSummary(node) {
  const kind = node.dataset.valueKind;
  const nested = node.querySelector(":scope > .attribute-row .nested-fields");
  const count = nested
    ? Array.from(nested.children).filter((child) => child.classList.contains("attribute-node")).length
    : node.querySelectorAll(":scope > .attribute-row .compact-list-item").length;
  const noun = isArrayKind(kind) ? (count === 1 ? "item" : "items") : (count === 1 ? "field" : "fields");
  node.querySelector(":scope > .attribute-row .nested-summary-text").textContent = `${count} ${noun}`;
}

function renumberArrayItems(container, parentNode) {
  const prefix = parentNode.dataset.valueKind === "single-field-array"
    ? fieldLabel(parentNode.dataset.itemField)
    : "Item";
  Array.from(container.children)
    .filter((child) => child.classList.contains("attribute-node"))
    .forEach((child, index) => {
      child.querySelector(":scope > .attribute-row > .attribute-key").textContent = `${prefix} ${index + 1}`;
    });
}

function addValueNode(container, key, value, isArrayItem) {
  const node = document.createElement("div");
  node.className = "attribute-node";
  node.dataset.valueKind = containerKind(value);

  const row = document.createElement("div");
  row.className = "attribute-row";
  row.append(createKeyControl(key, isArrayItem));

  const valueCell = document.createElement("div");
  valueCell.className = "attribute-value-cell";
  if (node.dataset.valueKind === "scalar-array") {
    const list = document.createElement("div");
    list.className = "compact-list-editor";
    value.forEach((item) => addCompactListItem(list, item));
    const addButton = document.createElement("button");
    addButton.className = "secondary compact add-compact-list-item";
    addButton.type = "button";
    addButton.textContent = "Add item";
    addButton.addEventListener("click", () => {
      addCompactListItem(list, "");
      list.append(addButton);
    });
    list.append(addButton);
    valueCell.append(list);
  } else if (node.dataset.valueKind === "single-field-array") {
    const details = document.createElement("details");
    details.className = "nested-value grouped-list-editor";
    const summary = document.createElement("summary");
    const summaryText = document.createElement("span");
    summaryText.className = "nested-summary-text";
    summary.append(summaryText);

    const labels = document.createElement("div");
    labels.className = "attribute-column-labels nested-column-labels";
    labels.setAttribute("aria-hidden", "true");
    labels.innerHTML = "<span>Field name</span><span>Value</span>";

    const groupedRows = document.createElement("div");
    groupedRows.className = "grouped-list-rows";
    groupedSingleFieldItems(value).forEach((items, itemField) => {
      addGroupedListRow(groupedRows, node, itemField, items);
    });
    const addFieldButton = document.createElement("button");
    addFieldButton.className = "secondary compact add-nested-field";
    addFieldButton.type = "button";
    addFieldButton.textContent = "Add field";
    addFieldButton.addEventListener("click", () => {
      addGroupedListRow(groupedRows, node, "", [{ value: "", originalIndex: null }]);
      details.open = true;
      updateContainerSummary(node);
    });
    details.append(summary, labels, groupedRows, addFieldButton);
    valueCell.append(details);
  } else if (node.dataset.valueKind === "scalar") {
    node.dataset.scalarType = scalarType(value);
    valueCell.append(createScalarControl(value));
  } else {
    const details = document.createElement("details");
    details.className = "nested-value";
    const summary = document.createElement("summary");
    const summaryText = document.createElement("span");
    summaryText.className = "nested-summary-text";
    summary.append(summaryText);

    const labels = document.createElement("div");
    labels.className = "attribute-column-labels nested-column-labels";
    labels.setAttribute("aria-hidden", "true");
    labels.innerHTML = node.dataset.valueKind === "single-field-array"
      ? "<span>Item</span><span>Value</span>"
      : "<span>Field name</span><span>Value</span>";

    const nested = document.createElement("div");
    nested.className = "nested-fields";
    const entries = containerEntries(node.dataset.valueKind, value, node.dataset.itemField);
    for (const [childKey, childValue] of entries) {
      const fixedItemLabel = node.dataset.valueKind === "array" || node.dataset.valueKind === "single-field-array";
      addValueNode(nested, childKey, childValue, fixedItemLabel);
    }

    const addButton = document.createElement("button");
    addButton.className = "secondary compact add-nested-field";
    addButton.type = "button";
    addButton.textContent = isArrayKind(node.dataset.valueKind) ? "Add item" : "Add field";
    addButton.addEventListener("click", () => {
      const count = directFieldNodes(nested).length + 1;
      let childKey = "";
      let fixedItemLabel = false;
      if (node.dataset.valueKind === "array") {
        childKey = `Item ${count}`;
        fixedItemLabel = true;
      } else if (node.dataset.valueKind === "single-field-array") {
        childKey = `${fieldLabel(node.dataset.itemField)} ${count}`;
        fixedItemLabel = true;
      }
      addValueNode(nested, childKey, "", fixedItemLabel);
      details.open = true;
      updateContainerSummary(node);
    });
    details.append(summary, labels, nested, addButton);
    valueCell.append(details);
  }
  row.append(valueCell);

  const removeButton = document.createElement("button");
  removeButton.className = "secondary compact remove-field";
  removeButton.type = "button";
  removeButton.setAttribute("aria-label", `Remove ${key || "field"}`);
  removeButton.textContent = "\u00d7";
  removeButton.addEventListener("click", () => {
    const parentNode = container.closest(".attribute-node");
    node.remove();
    if (parentNode && ["array", "single-field-array"].includes(parentNode.dataset.valueKind)) {
      renumberArrayItems(container, parentNode);
    }
    if (parentNode) updateContainerSummary(parentNode);
  });
  row.append(removeButton);
  node.append(row);
  container.append(node);
  if (node.dataset.valueKind !== "scalar" && node.dataset.valueKind !== "scalar-array") {
    updateContainerSummary(node);
  }
}

function directFieldNodes(container) {
  return Array.from(container.children).filter((child) => child.classList.contains("attribute-node"));
}

function readScalarValue(node) {
  const input = node.querySelector(":scope > .attribute-row .attribute-value");
  return readScalarControl(input, node.dataset.scalarType);
}

function readScalarControl(input, valueType) {
  if (valueType === "boolean") return input.value === "true";
  if (valueType === "number") {
    if (input.value === "") throw new Error("Numeric fields cannot be empty.");
    return Number(input.value);
  }
  if (valueType === "null" && input.value === "") return null;
  return input.value;
}

function readNodeValue(node) {
  if (node.dataset.valueKind === "scalar") return readScalarValue(node);
  if (node.dataset.valueKind === "scalar-array") {
    const items = node.querySelectorAll(":scope > .attribute-row .compact-list-item");
    return Array.from(items).map((item) => readScalarControl(
      item.querySelector(".attribute-value"),
      item.dataset.scalarType,
    ));
  }
  if (node.dataset.valueKind === "single-field-array") {
    const records = [];
    node.querySelectorAll(":scope > .attribute-row .grouped-list-row").forEach((row, groupIndex) => {
      const fieldInput = row.querySelector(".grouped-list-key");
      const itemField = fieldInput.value.trim();
      if (!itemField) {
        fieldInput.focus();
        throw new Error("Every field must have a name.");
      }
      row.querySelectorAll(".compact-list-item").forEach((item, itemIndex) => {
        const originalIndex = item.dataset.originalIndex;
        records.push({
          order: originalIndex === undefined ? Number.MAX_SAFE_INTEGER : Number(originalIndex),
          groupIndex,
          itemIndex,
          value: {
            [itemField]: readScalarControl(
              item.querySelector(".attribute-value"),
              item.dataset.scalarType,
            ),
          },
        });
      });
    });
    records.sort((left, right) => left.order - right.order
      || left.groupIndex - right.groupIndex
      || left.itemIndex - right.itemIndex);
    return records.map((record) => record.value);
  }
  const nested = node.querySelector(":scope > .attribute-row .nested-fields");
  const children = directFieldNodes(nested);
  if (node.dataset.valueKind === "array") return children.map(readNodeValue);
  if (node.dataset.valueKind === "typed-array") {
    return children.map((child) => {
      const keyInput = child.querySelector(":scope > .attribute-row > .attribute-key");
      const type = keyInput.value.trim();
      if (!type) {
        keyInput.focus();
        throw new Error("Every contact field must have a name.");
      }
      return { type, value: readNodeValue(child) };
    });
  }
  const result = {};
  children.forEach((child) => {
    const keyInput = child.querySelector(":scope > .attribute-row > .attribute-key");
    const key = keyInput.value.trim();
    if (!key) {
      keyInput.focus();
      throw new Error("Every field must have a name.");
    }
    result[key] = readNodeValue(child);
  });
  return result;
}

function editorPayload(form) {
  const data = new FormData(form);
  const extractedData = {};
  const fields = form.querySelector("#attribute-fields");
  directFieldNodes(fields).forEach((node) => {
    const keyInput = node.querySelector(":scope > .attribute-row > .attribute-key");
    const key = keyInput.value.trim();
    if (!key) {
      keyInput.focus();
      throw new Error("Every field must have a name.");
    }
    extractedData[key] = readNodeValue(node);
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
