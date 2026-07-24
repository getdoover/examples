"""Lambda entry point for the widget template's companion processor."""

from typing import Any

from pydoover.processor import run_app

from .application import WidgetTemplateApplication


def handler(event: dict[str, Any], context: Any) -> None:
    run_app(WidgetTemplateApplication(), event, context)
