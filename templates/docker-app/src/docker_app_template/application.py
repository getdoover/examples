"""Docker app lifecycle and event-handler stubs."""

from datetime import datetime

from pydoover.docker import Application
from pydoover.models import (
    AggregateUpdateEvent,
    ChannelSyncEvent,
    MessageCreateEvent,
    MessageUpdateEvent,
    OneShotMessage,
)

from .app_config import DockerAppTemplateConfig
from .app_tags import DockerAppTemplateTags
from .app_ui import DockerAppTemplateUI


class DockerAppTemplate(Application):
    config_cls = DockerAppTemplateConfig
    tags_cls = DockerAppTemplateTags
    ui_cls = DockerAppTemplateUI

    config: DockerAppTemplateConfig
    tags: DockerAppTemplateTags
    ui: DockerAppTemplateUI

    async def setup(self) -> None:
        pass

    async def main_loop(self) -> None:
        pass

    async def on_message_create(self, event: MessageCreateEvent) -> None:
        pass

    async def on_message_update(self, event: MessageUpdateEvent) -> None:
        pass

    async def on_oneshot_message(self, event: OneShotMessage) -> None:
        pass

    async def on_aggregate_update(self, event: AggregateUpdateEvent) -> None:
        pass

    async def on_channel_sync(self, event: ChannelSyncEvent) -> None:
        pass

    async def on_shutdown_at(self, dt: datetime) -> None:
        pass

    async def check_can_shutdown(self) -> bool:
        return True
