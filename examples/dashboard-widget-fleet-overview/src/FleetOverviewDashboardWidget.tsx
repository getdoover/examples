import "./styles.css";

import { useMemo } from "react";

import RemoteComponentWrapper from "customer_site/RemoteComponentWrapper";
import { useRemoteParams } from "customer_site/useRemoteParams";
import {
  type DeviceMapEntry,
  useDeviceMap,
  useMultiAgentAggregates,
} from "doover-js/react";

const TAG_ROOT = "on_message_processing";

interface DashboardWidgetProps {
  uiElement?: {
    app_key?: string;
  };
}

interface DashboardDevice extends DeviceMapEntry {
  group?: {
    id?: string | number | null;
    name?: string | null;
  } | null;
}

interface TagValues {
  on_message_processing?: {
    measurement?: unknown;
    status?: unknown;
    source_time?: unknown;
    last_processed_at?: unknown;
  };
}

interface DeviceRow {
  id: string;
  name: string;
  group: string;
  measurement: number | null;
  status: string;
  lastUpdated: number | null;
}

function finiteNumber(value: unknown): number | null {
  if (typeof value === "number" && Number.isFinite(value)) return value;
  if (typeof value !== "string" || value.trim() === "") return null;
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : null;
}

function epochMilliseconds(value: number | null | undefined): number | null {
  if (value == null || !Number.isFinite(value) || value <= 0) return null;
  return value < 100_000_000_000 ? value * 1_000 : value;
}

function formatMeasurement(value: number | null): string {
  return value == null
    ? "—"
    : new Intl.NumberFormat(undefined, { maximumFractionDigits: 2 }).format(value);
}

function formatUpdatedAt(value: number | null): string {
  if (value == null) return "No data";
  return new Intl.DateTimeFormat(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(value);
}

function normaliseStatus(value: unknown): string {
  return typeof value === "string" && value.trim()
    ? value.trim().toLowerCase()
    : "unknown";
}

function FleetOverviewDashboardWidgetInner({
  uiElement,
}: DashboardWidgetProps) {
  const params = useRemoteParams();
  const agentId =
    params?.agentId == null ? undefined : String(params.agentId);
  const appKey = uiElement?.app_key;

  const {
    devices,
    deviceIds,
    hasDeviceMap,
    isError: deviceMapError,
    isLoading: deviceMapLoading,
  } = useDeviceMap<DashboardDevice>(agentId, appKey);

  const { aggregatesByAgent, query } = useMultiAgentAggregates<TagValues>(
    "tag_values",
    deviceIds,
    { fields: [TAG_ROOT] },
  );

  const rows = useMemo<DeviceRow[]>(
    () =>
      devices
        .map((device) => {
          const aggregate = aggregatesByAgent[device.id];
          const telemetry = aggregate?.data?.on_message_processing;
          return {
            id: device.id,
            name: device.display_name || device.name || device.id,
            group: device.group?.name || "Ungrouped",
            measurement: finiteNumber(telemetry?.measurement),
            status: normaliseStatus(telemetry?.status),
            lastUpdated: epochMilliseconds(aggregate?.last_updated),
          };
        })
        .sort((left, right) => left.name.localeCompare(right.name)),
    [aggregatesByAgent, devices],
  );

  const measuredRows = rows.filter((row) => row.measurement != null);
  const average =
    measuredRows.length === 0
      ? null
      : measuredRows.reduce(
          (total, row) => total + (row.measurement ?? 0),
          0,
        ) / measuredRows.length;
  const okCount = rows.filter((row) => row.status === "ok").length;

  if (!agentId || !appKey) {
    return (
      <div className="fleet-message fleet-message-error">
        The dashboard host did not provide an agent ID and app key.
      </div>
    );
  }

  if (deviceMapLoading || (deviceIds.length > 0 && query.isLoading)) {
    return <div className="fleet-message">Loading permitted devices…</div>;
  }

  if (deviceMapError || query.isError) {
    return (
      <div className="fleet-message fleet-message-error">
        Device data could not be loaded. Check this app&apos;s extended
        permissions.
      </div>
    );
  }

  if (!hasDeviceMap) {
    return (
      <div className="fleet-message fleet-message-error">
        No DEVICE_MAP was found for <code>{appKey}</code>. Configure extended
        device permissions for this dashboard app.
      </div>
    );
  }

  if (rows.length === 0) {
    return (
      <div className="fleet-message">
        This dashboard app does not have permission to view any devices yet.
      </div>
    );
  }

  return (
    <section className="fleet-overview" aria-label="Fleet overview">
      <header className="fleet-header">
        <div>
          <p className="fleet-eyebrow">Live dashboard data</p>
          <h2>Fleet overview</h2>
        </div>
        {query.isFetching && <span className="fleet-refreshing">Refreshing…</span>}
      </header>

      <div className="fleet-summary">
        <article>
          <span>Permitted devices</span>
          <strong>{rows.length}</strong>
        </article>
        <article>
          <span>Status OK</span>
          <strong>
            {okCount} / {rows.length}
          </strong>
        </article>
        <article>
          <span>Average measurement</span>
          <strong>{formatMeasurement(average)}</strong>
        </article>
      </div>

      <div className="fleet-table-wrap">
        <table className="fleet-table">
          <thead>
            <tr>
              <th scope="col">Device</th>
              <th scope="col">Group</th>
              <th scope="col">Measurement</th>
              <th scope="col">Status</th>
              <th scope="col">Updated</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((row) => (
              <tr key={row.id}>
                <td>
                  <strong>{row.name}</strong>
                </td>
                <td>{row.group}</td>
                <td className="fleet-number">
                  {formatMeasurement(row.measurement)}
                </td>
                <td>
                  <span className="fleet-status" data-status={row.status}>
                    {row.status}
                  </span>
                </td>
                <td>
                  <time
                    dateTime={
                      row.lastUpdated == null
                        ? undefined
                        : new Date(row.lastUpdated).toISOString()
                    }
                  >
                    {formatUpdatedAt(row.lastUpdated)}
                  </time>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

const FleetOverviewDashboardWidget = (props: DashboardWidgetProps) => (
  <RemoteComponentWrapper>
    <FleetOverviewDashboardWidgetInner {...props} />
  </RemoteComponentWrapper>
);

export default FleetOverviewDashboardWidget;
