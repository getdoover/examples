# Webhook Routing Example

A working webhook-integration example adapted from the
[Digital Matter integration](https://github.com/getdoover/digital_matter). It
demonstrates decoding, validation, audit messages, extended permissions, and
routing normalised data to a device agent.

Start with the [minimal integration template](../../../templates/integration/)
when you only need an empty ingestion endpoint.

## Run the example

```bash
uv sync
uv run pytest
uv run export-config
./build.sh
```

## Example webhook

```json
{
  "agent_id": "123456789",
  "value": 42.5,
  "status": "ok",
  "recorded_at": "2026-01-01T00:00:00Z"
}
```

The integration stores the normalised payload on its own `ingestion_events`
channel. When `agent_id` is present, it also publishes the data to that agent's
`on_example_data` channel, ready for the on-message-processing example.

## Security notes

- Restrict **CIDR Ranges** to the provider's documented source addresses.
- Configure request signing when the provider supports it.
- Grant **Extended Permissions** only to the devices or groups the integration
  must address.
- Do not trust arbitrary identifiers from a public webhook in production. Map
  an authenticated provider identity to an approved Doover agent instead.

## Project map

| Path | Purpose |
| --- | --- |
| `src/webhook_routing/__init__.py` | AWS Lambda entry point |
| `src/webhook_routing/app_config.py` | Ingestion and permission configuration |
| `src/webhook_routing/application.py` | Payload decoding, validation, audit, and routing |
| `doover_config.json` | App metadata plus generated config schema |
| `build.sh` | Reproducible Lambda zip build |
