"""Integration lifecycle and event-handler stubs."""

from pydoover.models import (
    AggregateUpdateEvent,
    DeploymentEvent,
    IngestionEndpointEvent,
    ManualInvokeEvent,
    MessageCreateEvent,
    ScheduleEvent,
)
from pydoover.processor import Application

from .app_config import IntegrationTemplateConfig
from .app_tags import IntegrationTemplateTags
from .app_ui import IntegrationTemplateUI


class IntegrationTemplate(Application):
    config_cls = IntegrationTemplateConfig
    tags_cls = IntegrationTemplateTags
    ui_cls = IntegrationTemplateUI

    config: IntegrationTemplateConfig
    tags: IntegrationTemplateTags
    ui: IntegrationTemplateUI

    async def setup(self) -> None:
        pass

    async def close(self) -> None:
        pass

    async def on_ingestion_endpoint(self, event: IngestionEndpointEvent) -> None:
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
