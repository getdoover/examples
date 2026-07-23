"""Fast checks for the template's imports, schema, decoder, and parser."""

import base64
import json

from webhook_routing.application import (
    decode_ingestion_body,
    normalise_payload,
)


def test_decode_ingestion_body() -> None:
    encoded = base64.b64encode(json.dumps({"value": 12.5}).encode()).decode()
    assert decode_ingestion_body(encoded) == {"value": 12.5}
    assert decode_ingestion_body("not base64") is None


def test_normalise_payload() -> None:
    assert normalise_payload(
        {
            "agent_id": 123,
            "value": 42,
            "status": "ok",
            "recorded_at": "2026-01-01T00:00:00Z",
        }
    ) == {
        "agent_id": "123",
        "value": 42.0,
        "status": "ok",
        "recorded_at": "2026-01-01T00:00:00Z",
    }


def test_normalise_payload_rejects_invalid_values() -> None:
    assert normalise_payload({"value": "not-a-number"}) is None
    assert normalise_payload({"value": False}) is None
    assert normalise_payload([]) is None


def test_config_and_lambda_entry_point_import() -> None:
    from webhook_routing import handler
    from webhook_routing.app_config import WebhookRoutingConfig
    from webhook_routing.application import WebhookRouting

    assert isinstance(WebhookRoutingConfig.to_schema(), dict)
    assert handler
    assert WebhookRouting
