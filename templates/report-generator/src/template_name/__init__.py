"""Template Name report generator entry point."""

from typing import Any

from pydoover.processor import run_app

from .app_config import TemplateNameConfig
from .application import TemplateNameReportGenerator


def handler(event: dict[str, Any], context: Any) -> None:
    """Run the report generator."""
    TemplateNameConfig.clear_elements()
    run_app(TemplateNameReportGenerator(), event, context)
