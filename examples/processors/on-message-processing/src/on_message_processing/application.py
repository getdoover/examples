"""Message-to-tag processing for the example cloud processor."""

import logging
from datetime import datetime, timedelta, timezone
from typing import Any

from pydoover.models import ConnectionStatus, MessageCreateEvent
from pydoover.processor import Application

from .app_config import OnMessageProcessingConfig
from .app_tags import OnMessageProcessingTags
from .app_ui import OnMessageProcessingUI

log = logging.getLogger(__name__)


def normalise_message(data: Any, measurement_field: str) -> dict[str, Any] | None:
    """Validate a vendor payload and return the fields used by this app.

    Keep vendor-specific parsing in a small pure function like this. Returning
    ``None`` deliberately ignores malformed messages without partially updating
    tags. Booleans are rejected because Python otherwise treats them as numbers.
    """
    if not isinstance(data, dict):
        return None

    value = data.get(measurement_field)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None

    return {
        "measurement": float(value),
        "status": str(data.get("status", "unknown")),
        "source_time": (
            str(data["recorded_at"]) if data.get("recorded_at") is not None else None
        ),
    }


class OnMessageProcessing(Application):
    config_cls = OnMessageProcessingConfig
    tags_cls = OnMessageProcessingTags
    ui_cls = OnMessageProcessingUI

    config: OnMessageProcessingConfig
    tags: OnMessageProcessingTags
    ui: OnMessageProcessingUI

    async def on_message_create(self, event: MessageCreateEvent) -> None:
        """Process every message delivered by the configured subscriptions."""
        parsed = normalise_message(
            event.message.data,
            self.config.measurement_field.value,
        )
        if parsed is None:
            log.warning("Ignoring malformed message from %s", event.channel.name)
            return

        now = datetime.now(timezone.utc)
        calibrated_value = parsed["measurement"] + self.config.value_offset.value

        await self.tags.measurement.set(calibrated_value)
        await self.tags.status.set(parsed["status"])
        if parsed["source_time"] is not None:
            await self.tags.source_time.set(parsed["source_time"])
        await self.tags.last_processed_at.set(now.isoformat())

        # Connection state lets Doover surface a stale or silent data source.
        await self.ping_connection(
            online_at=now,
            connection_status=ConnectionStatus.periodic_unknown,
            offline_at=now + timedelta(minutes=self.config.offline_after_minutes.value),
        )
