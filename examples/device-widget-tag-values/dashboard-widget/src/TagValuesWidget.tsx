import "./styles.css";

import { useMemo, useState } from "react";

import RemoteComponentWrapper from "customer_site/RemoteComponentWrapper";
import { useRemoteParams } from "customer_site/useRemoteParams";
import { useAgentChannel } from "doover-js/react";

import { filterTagRows, formatUpdated, toTagRows } from "./tagValues";

function TagValuesWidgetContent() {
  const params = useRemoteParams();
  const agentId = params?.agentId == null ? undefined : String(params.agentId);
  const [filter, setFilter] = useState("");

  const {
    data,
    last_updated: lastUpdated,
    isLoading,
    isError,
  } = useAgentChannel<Record<string, unknown>>(agentId, "tag_values");

  const rows = useMemo(() => toTagRows(data ?? {}), [data]);
  const visibleRows = useMemo(
    () => filterTagRows(rows, filter),
    [filter, rows],
  );

  if (!agentId) {
    return (
      <div className="tag-values-state">
        Open this widget on a device to inspect its tag values.
      </div>
    );
  }

  if (isLoading) {
    return <div className="tag-values-state">Loading tag values…</div>;
  }

  if (isError) {
    return (
      <div className="tag-values-state tag-values-error">
        Could not load tag values.
      </div>
    );
  }

  return (
    <section className="tag-values-widget">
      <header className="tag-values-header">
        <div>
          <strong>Tag Values</strong>
          <span>
            {visibleRows.length} values · updated {formatUpdated(lastUpdated)}
          </span>
        </div>
        <input
          aria-label="Filter tag values"
          onChange={(event) => setFilter(event.target.value)}
          placeholder="Filter tag or value"
          type="search"
          value={filter}
        />
      </header>

      <div className="tag-values-table-wrap">
        <table className="tag-values-table">
          <thead>
            <tr>
              <th>Tag path</th>
              <th>Type</th>
              <th>Value</th>
              <th>Updated</th>
            </tr>
          </thead>
          <tbody>
            {visibleRows.map((row) => (
              <tr key={row.id}>
                <td>
                  <code>{row.path}</code>
                </td>
                <td>{row.type}</td>
                <td>
                  <code>{row.value}</code>
                </td>
                <td>{formatUpdated(lastUpdated)}</td>
              </tr>
            ))}
            {visibleRows.length === 0 && (
              <tr>
                <td className="tag-values-empty" colSpan={4}>
                  {rows.length === 0
                    ? "No tag values found."
                    : "No tag values match the filter."}
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </section>
  );
}

const TagValuesWidget = () => (
  <RemoteComponentWrapper>
    <TagValuesWidgetContent />
  </RemoteComponentWrapper>
);

export default TagValuesWidget;
