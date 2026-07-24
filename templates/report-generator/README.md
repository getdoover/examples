# Report Generator Template

A minimal Doover report generator that exports `ui_state` and `tag_values`
messages as JSON, grouped by channel and device.

Copy this folder, then replace each form of the placeholder app name:

- `report-generator-template` for the project and repository name
- `report_generator_template` for the Python package and Doover app key
- `ReportGeneratorTemplate` for Python classes
- `reportGeneratorTemplate` for camel-case identifiers, if you add any
- `Report Generator Template` for display text

```bash
uv sync
uv run export-config
uv run pytest
./build.sh
```

The `generate` method is the main extension point. Change its channel queries
and output structure to suit the report your app needs.
