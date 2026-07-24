import asyncio
import json
import logging
from collections import defaultdict
from datetime import datetime
from typing import Any

from pydoover.models import File
from pydoover.reports import Application

from .app_config import ReportGeneratorConfig

log = logging.getLogger(__name__)


class ReportGenerator(Application):
    """Generate a JSON export of device UI state and tag values."""

    config: ReportGeneratorConfig
    config_cls = ReportGeneratorConfig

    async def generate(
        self,
        agent_ids: list[int],
        period_start: datetime,
        period_end: datetime,
    ) -> File:
        log.info("Fetching data for %d devices", len(agent_ids))
        ui_state_data, tag_values_data = await asyncio.gather(
            self.fetch_messages(
                "ui_state",
                period_start,
                period_end,
                agent_ids=agent_ids,
            ),
            self.fetch_messages(
                "tag_values",
                period_start,
                period_end,
                agent_ids=agent_ids,
            ),
        )

        output: dict[str, dict[str, list[dict[str, Any]]]] = {
            "ui_state": defaultdict(list),
            "tag_values": defaultdict(list),
        }
        for message in ui_state_data:
            output["ui_state"][str(message.channel.agent_id)].append(
                message.to_dict()
            )
        for message in tag_values_data:
            output["tag_values"][str(message.channel.agent_id)].append(
                message.to_dict()
            )

        json_data = json.dumps(output).encode("utf-8")
        log.info("Uploading file of size %d", len(json_data))
        return File(
            "report.json",
            "application/json",
            len(json_data),
            json_data,
        )
