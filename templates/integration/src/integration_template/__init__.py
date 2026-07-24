"""AWS Lambda entry point for the integration template."""

from typing import Any

from pydoover.processor import run_app

from .application import IntegrationTemplate


def handler(event: dict[str, Any], context: Any) -> None:
    run_app(IntegrationTemplate(), event, context)
