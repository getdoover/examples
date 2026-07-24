# Template Name Report Generator

A minimal Doover report generator that exports `ui_state` and `tag_values`
messages as JSON, grouped by channel and device.

Copy this folder, then replace each form of the placeholder app name:

- `template-name` for the project and repository name
- `template_name` for the Python package and Doover app key
- `TemplateName` for Python classes
- `templateName` for camel-case identifiers, if you add any
- `Template Name` for display text

```bash
uv sync
uv run export-config
uv run pytest
./build.sh
```

The `generate` method is the main extension point. Change its channel queries
and output structure to suit the report your app needs.
