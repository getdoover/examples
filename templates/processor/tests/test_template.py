import asyncio
import inspect

from processor_template import handler
from processor_template.app_config import ProcessorTemplateConfig
from processor_template.app_tags import ProcessorTemplateTags
from processor_template.app_ui import ProcessorTemplateUI
from processor_template.application import ProcessorTemplate


def test_template_imports() -> None:
    assert ProcessorTemplate()
    assert isinstance(ProcessorTemplateConfig.to_schema(), dict)
    assert isinstance(ProcessorTemplateUI(None, None, None).to_schema(), dict)
    assert ProcessorTemplateTags
    assert handler


def test_event_handlers_are_async_stubs() -> None:
    for name in (
        "setup",
        "close",
        "on_message_create",
        "on_aggregate_update",
        "on_deployment",
        "on_schedule",
        "on_manual_invoke",
    ):
        assert inspect.iscoroutinefunction(getattr(ProcessorTemplate, name))


def test_event_stubs_do_nothing() -> None:
    async def exercise() -> None:
        app = ProcessorTemplate()
        await app.setup()
        await app.on_message_create(None)
        await app.on_aggregate_update(None)
        await app.on_deployment(None)
        await app.on_schedule(None)
        await app.on_manual_invoke(None)
        await app.close()

    asyncio.run(exercise())
