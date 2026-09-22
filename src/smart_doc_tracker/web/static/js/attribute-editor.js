import { UserFacingError } from "./errors.js";
import {
  containerEntries,
  containerKind,
  fieldLabel,
  groupedSingleFieldItems,
  isArrayKind,
} from "./attribute-model.js";

export function addFieldRow(container, key = "", value = "") {
  addValueNode(container, key, value, false);
}

export function addGroupRow(container, key = "") {
  const node = addValueNode(container, key, {}, false);
  node.querySelector(":scope > .attribute-row .nested-value").open = true;
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
  const fieldDetails = document.createElement("details");
  fieldDetails.className = "grouped-list-field";
  const fieldSummary = document.createElement("summary");
  const fieldSummaryContent = document.createElement("span");
  fieldSummaryContent.className = "grouped-list-field-summary";
  const summaryKey = document.createElement("span");
  summaryKey.className = "grouped-list-summary-key";
  summaryKey.textContent = itemField || "New field";
  const summaryCount = document.createElement("span");
  summaryCount.className = "grouped-list-summary-count";
  fieldSummaryContent.append(summaryKey, summaryCount);
  fieldSummary.append(fieldSummaryContent);
  const groupedRow = document.createElement("div");
  groupedRow.className = "grouped-list-row";
  const fieldInput = document.createElement("input");
  fieldInput.className = "grouped-list-key";
  fieldInput.setAttribute("aria-label", "Field name");
  fieldInput.value = itemField;
  const removeButton = document.createElement("button");
  removeButton.className = "secondary compact grouped-list-remove";
  removeButton.type = "button";
  removeButton.setAttribute("aria-label", `Remove ${itemField || "field"}`);
  removeButton.textContent = "\u00d7";
  fieldInput.addEventListener("input", () => {
    const currentName = fieldInput.value.trim();
    summaryKey.textContent = currentName || "New field";
    removeButton.setAttribute("aria-label", `Remove ${currentName || "field"}`);
  });
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
  removeButton.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    fieldDetails.remove();
    updateContainerSummary(node);
  });
  fieldDetails.append(fieldSummary, removeButton, groupedRow);
  if (!itemField) fieldDetails.open = true;
  container.append(fieldDetails);
  updateGroupedListSummary(fieldDetails);
}

function updateGroupedListSummary(fieldDetails) {
  const count = fieldDetails.querySelectorAll(".compact-list-item").length;
  fieldDetails.querySelector(".grouped-list-summary-count").textContent =
    `${count} ${count === 1 ? "item" : "items"}`;
}

function updateContainerSummary(node) {
  const kind = node.dataset.valueKind;
  const nested = node.querySelector(":scope > .attribute-row .nested-fields");
  const count = nested
    ? Array.from(nested.children).filter((child) => child.classList.contains("attribute-node")).length
    : node.querySelectorAll(":scope > .attribute-row .compact-list-item").length;
  node.querySelectorAll(":scope > .attribute-row .grouped-list-field").forEach(updateGroupedListSummary);
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

    const addActions = document.createElement("div");
    addActions.className = "nested-add-actions";
    const addButton = document.createElement("button");
    addButton.className = "secondary compact add-nested-field";
    addButton.type = "button";
    addButton.textContent = isArrayKind(node.dataset.valueKind) ? "Add item" : "Add field";
    const addChild = (childValue) => {
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
      const childNode = addValueNode(nested, childKey, childValue, fixedItemLabel);
      if (containerKind(childValue) === "object") {
        childNode.querySelector(":scope > .attribute-row .nested-value").open = true;
      }
      details.open = true;
      updateContainerSummary(node);
    };
    addButton.addEventListener("click", () => addChild(""));
    addActions.append(addButton);

    if (node.dataset.valueKind === "object" || node.dataset.valueKind === "array") {
      const addGroupButton = document.createElement("button");
      addGroupButton.className = "secondary compact add-nested-group";
      addGroupButton.type = "button";
      addGroupButton.textContent = node.dataset.valueKind === "array" ? "Add group item" : "Add group";
      addGroupButton.addEventListener("click", () => addChild({}));
      addActions.append(addGroupButton);
    }
    details.append(summary, labels, nested, addActions);
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
  return node;
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
    if (input.value === "") throw new UserFacingError("Enter a number or remove this field.");
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
        throw new UserFacingError("Give every field a name before saving.");
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
        throw new UserFacingError("Give every contact field a name before saving.");
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
      throw new UserFacingError("Give every field a name before saving.");
    }
    result[key] = readNodeValue(child);
  });
  return result;
}

export function editorPayload(form) {
  const data = new FormData(form);
  const extractedData = {};
  const fields = form.querySelector("#attribute-fields");
  directFieldNodes(fields).forEach((node) => {
    const keyInput = node.querySelector(":scope > .attribute-row > .attribute-key");
    const key = keyInput.value.trim();
    if (!key) {
      keyInput.focus();
      throw new UserFacingError("Give every field a name before saving.");
    }
    extractedData[key] = readNodeValue(node);
  });
  return {
    document_type: data.get("document_type"), summary: data.get("summary"),
    issue_date: data.get("issue_date") || null, expiry_date: data.get("expiry_date") || null,
    extracted_data: extractedData,
  };
}
