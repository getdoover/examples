"""Webhook ingestion, validation, and device routing."""

import base64
import json
import logging
from typing import Any

from pydoover.models import IngestionEndpointEvent
from pydoover.processor import Application

from .app_config import WebhookRoutingConfig

log = logging.getLogger(__name__)

AUDIT_CHANNEL = "ingestion_events"
DEVICE_CHANNEL = "on_example_data"


def decode_ingestion_body(encoded_body: str) -> dict[str, Any] | None:
    """Decode the base64 JSON body supplied by a raw ingestion invocation.

    pydoover normally exposes the decoded object on ``event.payload``. Keeping
    this hook makes the integration compatible with direct ingestion events and
    gives provider-specific implementations one obvious decoding seam.
    """
    try:
        decoded = base64.b64decode(encoded_body, validate=True)
        payload = json.loads(decoded)
    except (ValueError, TypeError, json.JSONDecodeError):
        return None
    return payload if isinstance(payload, dict) else None


def normalise_payload(payload: Any) -> dict[str, Any] | None:
    """Validate the provider payload and return a stable internal message.

    Replace this function with provider-specific parsing. Downstream processors
    should depend on this small internal contract instead of a vendor's raw
    webhook shape.
    """
    if not isinstance(payload, dict):
        return None

    value = payload.get("value")
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None

    message = {
        "value": float(value),
        "status": str(payload.get("status", "unknown")),
        "recorded_at": (
            str(payload["recorded_at"])
            if payload.get("recorded_at") is not None
            else None
        ),
    }

    # Agent ID remains optional so valid but unmapped events are still audited.
    agent_id = payload.get("agent_id")
    if agent_id is not None:
        message["agent_id"] = str(agent_id)
    return message


class WebhookRouting(Application):
    config_cls = WebhookRoutingConfig
    config: WebhookRoutingConfig

    def parse_ingestion_event_payload(self, payload: str) -> dict[str, Any] | None:
        """Let pydoover convert the raw ingestion body before dispatch."""
        return decode_ingestion_body(payload)

    async def on_ingestion_endpoint(self, event: IngestionEndpointEvent) -> None:
        """Audit a valid webhook and forward it to its destination agent."""
        message = normalise_payload(event.payload)
        if message is None:
            log.warning("Ignoring malformed ingestion payload")
            return

        # Retaining a normalised event on the integration agent is invaluable
        # when diagnosing provider and routing issues.
        await self.api.create_message(AUDIT_CHANNEL, message)

        agent_id = message.get("agent_id")
        if agent_id is None:
            log.info("Valid event had no destination agent; audit only")
            return

        # ExtendedPermissionsConfig controls which remote agents this app may
        # address. Avoid accepting an untrusted raw agent_id in real providers;
        # resolve an authenticated serial/account identifier instead.
        await self.api.create_message(
            DEVICE_CHANNEL,
            # The destination processor does not need routing metadata. Build a
            # new object rather than mutating the message already sent to the
            # audit channel.
            {key: value for key, value in message.items() if key != "agent_id"},
            agent_id=agent_id,
        )
