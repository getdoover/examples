"""Minimal Doover processor entry point."""

from typing import Any

from pydoover.processor import Application, run_app


class ProcessorTemplate(Application):
    """No-op processor; override only the event handlers your app needs."""


def handler(event: dict[str, Any], context: Any) -> None:
    run_app(ProcessorTemplate(), event, context)
