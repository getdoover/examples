"""Minimal Doover integration entry point."""

from typing import Any

from pydoover.processor import Application, run_app

from .app_config import IntegrationTemplateConfig


class IntegrationTemplate(Application):
    """No-op integration; override on_ingestion_endpoint to handle webhooks."""

    config_cls = IntegrationTemplateConfig


def handler(event: dict[str, Any], context: Any) -> None:
    run_app(IntegrationTemplate(), event, context)
