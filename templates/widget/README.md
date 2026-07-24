# Widget Template

A minimal processor-backed React widget for the Doover customer site. The
companion processor registers the remote component in the interpreter UI. The
widget renders static content without requesting any Doover data, while keeping
an example channel query commented out in `src/WidgetTemplate.tsx`.

Copy this folder, then replace each form of the placeholder name:

- `widget-template` for the package and repository name
- `WidgetTemplate` for the module federation scope, component, and built file
- `widget-template` CSS class names, if you add project-specific styles
- `Widget Template` for display text

Install and test the companion processor, then type-check and build the widget:

```bash
uv sync
uv run pytest
npm ci
npm run check
npm run build
```

The build creates `assets/WidgetTemplate.js`. Do not commit `node_modules`,
`dist`, or the generated `assets` directory.

The processor association is defined in three places:

- `src/widget_template/app_ui.py` registers `WidgetTemplate` as a
  `ui.RemoteComponent`, which makes it part of the interpreter UI.
- `src/widget_template/application.py` associates that UI with a Doover
  processor application.
- `doover_config.json` points `build_widget_command` and `widget` at the
  frontend build.

## Fetching data

The starter deliberately performs no requests. When the widget needs live
data, uncomment the imports and hook calls marked `DATA EXAMPLE` in
`src/WidgetTemplate.tsx`, then render the returned `data`, loading, and error
states.
