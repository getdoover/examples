"""Lambda entry point for the example processor."""

from typing import Any

from pydoover.processor import run_app

from .application import OnMessageProcessing


def handler(event: dict[str, Any], context: Any) -> None:
    """Hand an AWS Lambda invocation to the pydoover processor runtime."""
    run_app(OnMessageProcessing(), event, context)
