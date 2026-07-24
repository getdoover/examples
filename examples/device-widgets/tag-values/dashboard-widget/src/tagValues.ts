export interface TagRow {
  id: string;
  path: string;
  type: string;
  value: string;
}

export function valueType(value: unknown): string {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}

export function displayValue(value: unknown): string {
  if (value === null) return "null";
  if (typeof value === "string") return value;
  if (typeof value === "undefined") return "undefined";
  if (
    typeof value === "number" ||
    typeof value === "boolean" ||
    typeof value === "bigint"
  ) {
    return String(value);
  }

  try {
    return JSON.stringify(value);
  } catch {
    return String(value);
  }
}

export function flattenValues(
  value: unknown,
  path = "",
): Array<{ path: string; value: unknown }> {
  if (Array.isArray(value)) {
    if (value.length === 0) return path ? [{ path, value }] : [];
    return value.flatMap((item, index) =>
      flattenValues(item, path ? `${path}.${index}` : String(index)),
    );
  }

  if (value !== null && typeof value === "object") {
    const entries = Object.entries(value as Record<string, unknown>);
    if (entries.length === 0) return path ? [{ path, value }] : [];
    return entries.flatMap(([key, item]) =>
      flattenValues(item, path ? `${path}.${key}` : key),
    );
  }

  return [{ path: path || "(root)", value }];
}

export function toTagRows(data: Record<string, unknown>): TagRow[] {
  return flattenValues(data)
    .map(({ path, value }) => ({
      id: path,
      path,
      type: valueType(value),
      value: displayValue(value),
    }))
    .sort((left, right) => left.path.localeCompare(right.path));
}

export function filterTagRows(rows: TagRow[], query: string): TagRow[] {
  const needle = query.trim().toLowerCase();
  if (!needle) return rows;

  return rows.filter((row) =>
    [row.path, row.type, row.value].some((value) =>
      value.toLowerCase().includes(needle),
    ),
  );
}

export function formatUpdated(value: unknown): string {
  const raw =
    typeof value === "string" || typeof value === "number" ? Number(value) : NaN;
  if (!Number.isFinite(raw) || raw <= 0) return "-";

  const milliseconds = raw < 100_000_000_000 ? raw * 1000 : raw;
  return new Date(milliseconds).toLocaleString();
}
