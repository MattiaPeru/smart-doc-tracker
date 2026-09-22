import {
  containerEntries,
  containerKind,
  groupedSingleFieldItems,
  isArrayKind,
} from "./attribute-model.js";

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
      const fieldDetails = document.createElement("details");
      fieldDetails.className = "grouped-list-field grouped-list-view-field";
      const fieldSummary = document.createElement("summary");
      const fieldSummaryContent = document.createElement("span");
      fieldSummaryContent.className = "grouped-list-field-summary";
      const summaryKey = document.createElement("span");
      summaryKey.className = "attribute-view-key";
      summaryKey.textContent = itemField;
      const summaryCount = document.createElement("span");
      summaryCount.textContent = `${items.length} ${items.length === 1 ? "item" : "items"}`;
      fieldSummaryContent.append(summaryKey, summaryCount);
      fieldSummary.append(fieldSummaryContent);
      const row = document.createElement("div");
      row.className = "attribute-view-row compact-list-view-row";
      const fieldSpacer = document.createElement("span");
      fieldSpacer.setAttribute("aria-hidden", "true");
      const values = document.createElement("span");
      values.className = "compact-list-view-values";
      items.forEach((item) => {
        const itemValue = document.createElement("span");
        itemValue.className = "compact-list-view-value";
        itemValue.textContent = displayScalarValue(item.value);
        values.append(itemValue);
      });
      row.append(fieldSpacer, values);
      fieldDetails.append(fieldSummary, row);
      children.append(fieldDetails);
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

export function renderAttributeView(container, data) {
  Object.entries(data).forEach(([key, value]) => addAttributeViewNode(container, key, value));
  if (!container.children.length) container.textContent = "No attributes available.";
}

