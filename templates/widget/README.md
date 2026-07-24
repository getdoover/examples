# Widget Template

A minimal React widget for the Doover customer site. It renders static content
without requesting any Doover data, while keeping an example channel query
commented out in `src/WidgetTemplate.tsx`.

Copy this folder, then replace each form of the placeholder name:

- `widget-template` for the package and repository name
- `WidgetTemplate` for the module federation scope, component, and built file
- `widget-template` CSS class names, if you add project-specific styles
- `Widget Template` for display text

Install, type-check, and build the widget:

```bash
npm ci
npm run check
npm run build
```

The build creates `assets/WidgetTemplate.js`. Do not commit `node_modules`,
`dist`, or the generated `assets` directory.

## Fetching data

The starter deliberately performs no requests. When the widget needs live
data, uncomment the imports and hook calls marked `DATA EXAMPLE` in
`src/WidgetTemplate.tsx`, then render the returned `data`, loading, and error
states.
