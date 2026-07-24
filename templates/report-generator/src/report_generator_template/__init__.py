"""Report Generator Template entry point."""

from typing import Any

from pydoover.processor import run_app

from .app_config import ReportGeneratorTemplateConfig
from .application import ReportGeneratorTemplate


def handler(event: dict[str, Any], context: Any) -> None:
    """Run the report generator."""
    ReportGeneratorTemplateConfig.clear_elements()
    run_app(ReportGeneratorTemplate(), event, context)
