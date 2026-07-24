# Doover Integration Template

The conventional file structure for a Doover integration with empty tags and
UI classes. `application.py` contains no-op stubs for the public lifecycle and
integration event hooks.

The ingestion endpoint is the only preconfigured field because it is required
for receiving webhooks. Copy the folder, rename `integration_template`, then
fill in only the classes and handlers your app needs.

```bash
uv sync
uv run export-config
uv run export-ui
uv run pytest
./build.sh
```

For validation, audit, and agent routing, see the
[webhook-routing example](../../examples/integrations/webhook-routing/).
