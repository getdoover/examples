"""Processor lifecycle and event-handler stubs."""

from pydoover.models import (
    AggregateUpdateEvent,
    DeploymentEvent,
    ManualInvokeEvent,
    MessageCreateEvent,
    ScheduleEvent,
)
from pydoover.processor import Application

from .app_config import ProcessorTemplateConfig
from .app_tags import ProcessorTemplateTags
from .app_ui import ProcessorTemplateUI


class ProcessorTemplate(Application):
    config_cls = ProcessorTemplateConfig
    tags_cls = ProcessorTemplateTags
    ui_cls = ProcessorTemplateUI

    config: ProcessorTemplateConfig
    tags: ProcessorTemplateTags
    ui: ProcessorTemplateUI

    async def setup(self) -> None:
        pass

    async def close(self) -> None:
        pass

    async def on_message_create(self, event: MessageCreateEvent) -> None:
        pass

    async def on_aggregate_update(self, event: AggregateUpdateEvent) -> None:
        pass

    async def on_deployment(self, event: DeploymentEvent) -> None:
        pass

    async def on_schedule(self, event: ScheduleEvent) -> None:
        pass

    async def on_manual_invoke(self, event: ManualInvokeEvent) -> None:
        pass
