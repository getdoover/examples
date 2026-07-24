# Fleet Overview Dashboard Widget

A focused dashboard-level widget adapted from Doover's Vega level sensor
dashboard. It demonstrates the parts that are specific to a dashboard:

- discovering devices granted to the dashboard app through `useDeviceMap`;
- batch-reading each device's `tag_values` with
  `useMultiAgentAggregates`;
- keeping those aggregates live and combining them into fleet-wide summaries;
- exposing a single-file Module Federation remote for the Doover customer site.

The example reads the tags emitted by the repository's
[on-message-processing example](../../processors/on-message-processing/):
`measurement` and `status` beneath the `on_message_processing` app key.

## Build

```bash
npm ci
npm run check
npm run build
```

The deployable file is written to
`assets/FleetOverviewDashboardWidget.js`. Generated `assets`, `dist`, and
`node_modules` directories are intentionally ignored.

## Connect it to a dashboard app

The app that owns this widget must expose a `DEVICE_MAP` through its extended
permissions. Request the fields used by the table when defining that
permission:

```json
{
  "x-extraDeviceFields": [
    "id",
    "name",
    "display_name",
    "group__id",
    "group__name"
  ]
}
```

Its remote UI element must pass the app key and match the scope/module exposed
in `rsbuild.config.ts`:

```json
{
  "type": "uiRemoteComponent",
  "name": "FleetOverview",
  "displayString": "Fleet Overview",
  "componentUrl": "$config.app().dv_widget_url",
  "scope": "FleetOverviewDashboardWidget",
  "module": "./FleetOverviewDashboardWidget",
  "app_key": "$config.app().APP_KEY"
}
```

The Doover host supplies the current dashboard agent ID through
`useRemoteParams`. `useDeviceMap(agentId, appKey)` then reads only the devices
granted to that app; the widget deliberately does not fall back to another
app's permissions.

## Adapt the data

Change `TAG_ROOT` and the `TagValues` interface in
`src/FleetOverviewDashboardWidget.tsx` to match the producing app. Keep the
`fields` projection aligned with that root so large fleets do not fetch every
tag from every permitted device.

For historical charts, add `useMultiAgentChannelMessages` or query Doover data
series after this aggregate-based live view is working. The larger source
dashboard contains those patterns, but they are intentionally omitted here to
keep this example easy to understand and reuse.
