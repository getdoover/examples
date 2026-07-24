import { describe, expect, it } from "vitest";

import {
  displayValue,
  filterTagRows,
  flattenValues,
  formatUpdated,
  toTagRows,
  valueType,
} from "./tagValues";

describe("tag value shaping", () => {
  it("flattens nested objects and arrays into stable paths", () => {
    expect(
      flattenValues({
        location: { latitude: -27.5, longitude: 151.9 },
        alarms: ["high", "offline"],
      }),
    ).toEqual([
      { path: "location.latitude", value: -27.5 },
      { path: "location.longitude", value: 151.9 },
      { path: "alarms.0", value: "high" },
      { path: "alarms.1", value: "offline" },
    ]);
  });

  it("keeps empty nested collections visible", () => {
    expect(flattenValues({ details: {}, samples: [] })).toEqual([
      { path: "details", value: {} },
      { path: "samples", value: [] },
    ]);
  });

  it("sorts rows and filters across path, type, and value", () => {
    const rows = toTagRows({ zeta: false, alpha: 42 });

    expect(rows.map((row) => row.path)).toEqual(["alpha", "zeta"]);
    expect(filterTagRows(rows, "BOOL")).toEqual([rows[1]]);
    expect(filterTagRows(rows, "42")).toEqual([rows[0]]);
  });

  it("formats primitive values and recognises arrays", () => {
    expect(displayValue(null)).toBe("null");
    expect(displayValue({ ok: true })).toBe('{"ok":true}');
    expect(valueType([])).toBe("array");
  });

  it("accepts timestamps in seconds or milliseconds", () => {
    expect(formatUpdated(0)).toBe("-");
    expect(formatUpdated("not-a-date")).toBe("-");
    expect(formatUpdated(1_700_000_000)).toBe(
      formatUpdated(1_700_000_000_000),
    );
  });
});
