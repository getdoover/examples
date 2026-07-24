import asyncio
import inspect

from integration_template import handler
from integration_template.app_config import IntegrationTemplateConfig
from integration_template.app_tags import IntegrationTemplateTags
from integration_template.app_ui import IntegrationTemplateUI
from integration_template.application import IntegrationTemplate


def test_template_imports() -> None:
    assert IntegrationTemplate()
    assert isinstance(IntegrationTemplateConfig.to_schema(), dict)
    assert isinstance(IntegrationTemplateUI(None, None, None).to_schema(), dict)
    assert IntegrationTemplateTags
    assert handler


def test_event_handlers_are_async_stubs() -> None:
    for name in (
        "setup",
        "close",
        "on_ingestion_endpoint",
        "on_message_create",
        "on_aggregate_update",
        "on_deployment",
        "on_schedule",
        "on_manual_invoke",
    ):
        assert inspect.iscoroutinefunction(getattr(IntegrationTemplate, name))


def test_event_stubs_do_nothing() -> None:
    async def exercise() -> None:
        app = IntegrationTemplate()
        await app.setup()
        await app.on_ingestion_endpoint(None)
        await app.on_message_create(None)
        await app.on_aggregate_update(None)
        await app.on_deployment(None)
        await app.on_schedule(None)
        await app.on_manual_invoke(None)
        await app.close()

    asyncio.run(exercise())
