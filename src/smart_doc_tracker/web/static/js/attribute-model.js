export function containerKind(value) {
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

export function isArrayKind(kind) {
  return kind === "array" || kind === "typed-array" || kind === "single-field-array" || kind === "scalar-array";
}

export function fieldLabel(value) {
  const normalized = String(value).replaceAll("_", " ");
  return normalized.charAt(0).toUpperCase() + normalized.slice(1);
}

export function containerEntries(kind, value, itemField = "") {
  if (kind === "typed-array") return value.map((item) => [item.type, item.value]);
  if (kind === "single-field-array") {
    return value.map((item, index) => [`${fieldLabel(itemField)} ${index + 1}`, item[itemField]]);
  }
  if (kind === "array") return Array.from(value.entries()).map(([index, item]) => [`Item ${index + 1}`, item]);
  return Object.entries(value);
}

export function groupedSingleFieldItems(value) {
  const groups = new Map();
  value.forEach((item, originalIndex) => {
    const itemField = Object.keys(item)[0];
    if (!groups.has(itemField)) groups.set(itemField, []);
    groups.get(itemField).push({ value: item[itemField], originalIndex });
  });
  return groups;
}

