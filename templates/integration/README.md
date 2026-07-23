# Minimal Doover Integration

The smallest useful webhook integration. It exposes Doover's standard ingestion
endpoint configuration and accepts events through the SDK's default no-op
handler.

Copy the folder, rename `integration_template`, then implement
`on_ingestion_endpoint` on `IntegrationTemplate`.

```bash
uv sync
uv run export-config
uv run pytest
./build.sh
```

For validation, audit, and agent routing, see the
[webhook-routing example](../../examples/integrations/webhook-routing/).
