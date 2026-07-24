# Tag Values Device Widget Example

A device-local Doover widget that displays every value in the current device's
`tag_values` channel. It is adapted from a working diagnostic widget and keeps
one complete vertical slice: Python app metadata and UI registration, a
module-federated React widget, channel data loading, value flattening, filtering,
and tests.

The widget is associated with `TagValuesWidgetApplication`, a Doover processor.
Its `TagValuesWidgetUI` registers the remote component in the interpreter UI,
while `doover_config.json` connects the processor handler, frontend build
command, and generated widget asset.

Unlike a dashboard widget that can query several agents, this widget uses the
agent supplied by the device page and does not request extended processor
permissions.

## Install and test

The Python host app and the frontend are independently installable:

```bash
uv sync
uv run pytest

cd dashboard-widget
npm ci
npm test
npm run typecheck
npm run build
```

The frontend build writes `dashboard-widget/assets/TagValuesWidget.js`. The
generated asset is ignored because Doover runs `build_widget_command` when
packaging the app.

To regenerate the checked-in schemas after changing the Python config or UI:

```bash
uv run export-config
uv run export-ui
```

## Project map

| Path | Purpose |
| --- | --- |
| `src/tag_values_widget/` | Companion processor and interpreter UI remote-component registration |
| `tests/` | Config, UI, and permission-boundary checks |
| `dashboard-widget/src/TagValuesWidget.tsx` | React component that reads the current agent |
| `dashboard-widget/src/tagValues.ts` | Tested flattening, filtering, and formatting helpers |
| `dashboard-widget/rsbuild.config.ts` | Module Federation and single-file bundle configuration |
| `doover_config.json` | App metadata and generated schemas |

## Adapting the example

Change the channel passed to `useAgentChannel` when inspecting another
device-local channel. Keep the remote-component `name`, `scope`, module exposure,
and output filename in sync if you rename the widget.
