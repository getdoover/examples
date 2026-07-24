import asyncio
import inspect

from docker_app_template import main
from docker_app_template.app_config import DockerAppTemplateConfig
from docker_app_template.app_tags import DockerAppTemplateTags
from docker_app_template.app_ui import DockerAppTemplateUI
from docker_app_template.application import DockerAppTemplate


def test_template_imports() -> None:
    assert DockerAppTemplate(test_mode=True)
    assert isinstance(DockerAppTemplateConfig.to_schema(), dict)
    assert isinstance(DockerAppTemplateUI(None, None, None).to_schema(), dict)
    assert DockerAppTemplateTags
    assert main


def test_lifecycle_and_event_handlers_are_async_stubs() -> None:
    for name in (
        "setup",
        "main_loop",
        "on_message_create",
        "on_message_update",
        "on_oneshot_message",
        "on_aggregate_update",
        "on_channel_sync",
        "on_shutdown_at",
        "check_can_shutdown",
    ):
        assert inspect.iscoroutinefunction(getattr(DockerAppTemplate, name))


def test_lifecycle_and_event_stubs_do_nothing() -> None:
    async def exercise() -> None:
        app = DockerAppTemplate(test_mode=True)
        await app.setup()
        await app.main_loop()
        await app.on_message_create(None)
        await app.on_message_update(None)
        await app.on_oneshot_message(None)
        await app.on_aggregate_update(None)
        await app.on_channel_sync(None)
        await app.on_shutdown_at(None)
        assert await app.check_can_shutdown() is True

    asyncio.run(exercise())
