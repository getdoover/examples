import asyncio
import json
from datetime import UTC, datetime
from types import SimpleNamespace

from report_generator_template import (
    ReportGeneratorTemplate,
    ReportGeneratorTemplateConfig,
    handler,
)


class Message:
    def __init__(self, agent_id: int, value: object):
        self.channel = SimpleNamespace(agent_id=agent_id)
        self.value = value

    def to_dict(self) -> dict[str, object]:
        return {"value": self.value}


def test_template_imports() -> None:
    assert ReportGeneratorTemplate()
    assert isinstance(ReportGeneratorTemplateConfig.to_schema(), dict)
    assert handler


def test_generate_groups_messages_by_channel_and_device() -> None:
    generator = ReportGeneratorTemplate()

    async def fetch_messages(channel: str, *_args, **_kwargs):
        return [Message(123, channel)]

    generator.fetch_messages = fetch_messages
    start = datetime(2026, 1, 1, tzinfo=UTC)
    report = asyncio.run(generator.generate([123], start, start))

    assert report.filename == "report.json"
    assert report.content_type == "application/json"
    assert report.size == len(report.data)
    assert json.loads(report.data) == {
        "ui_state": {"123": [{"value": "ui_state"}]},
        "tag_values": {"123": [{"value": "tag_values"}]},
    }
