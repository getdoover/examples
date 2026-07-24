"""AWS Lambda entry point for the processor template."""

from typing import Any

from pydoover.processor import run_app

from .application import ProcessorTemplate


def handler(event: dict[str, Any], context: Any) -> None:
    run_app(ProcessorTemplate(), event, context)
