# Fleet Overview Dashboard Widget

A focused processor-backed dashboard widget adapted from Doover's Vega level
sensor dashboard. Its companion processor registers the remote component in
the interpreter UI and grants the widget access to selected devices. It
demonstrates the parts that are specific to a dashboard:

- discovering devices granted to the dashboard app through `useDeviceMap`;
- batch-reading each device's `tag_values` with
  `useMultiAgentAggregates`;
- keeping those aggregates live and combining them into fleet-wide summaries;
- exposing a single-file Module Federation remote for the Doover customer site.

The example reads the tags emitted by the repository's
[on-message-processing example](../processor-on-message-processing/):
`measurement` and `status` beneath the `on_message_processing` app key.

## Build

```bash
uv sync
uv run pytest
npm ci
npm run check
npm run build
```

The deployable file is written to
`assets/FleetOverviewDashboardWidget.js`. Generated `assets`, `dist`, and
`node_modules` directories are intentionally ignored.

## Processor and interpreter UI association

The included `FleetOverviewDashboardApplication` owns the remote component.
`src/fleet_overview_dashboard/app_ui.py` places it in the interpreter UI, and
`doover_config.json` ties the processor, frontend build command, and generated
widget asset together.

The processor exposes a `DEVICE_MAP` through its extended permissions and
requests the fields used by the table:

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

Its remote UI element passes the app key and matches the scope/module exposed
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

The Doover host supplies the companion processor's agent ID through
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
