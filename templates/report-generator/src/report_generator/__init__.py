"""Report Generator entry point."""

from typing import Any

from pydoover.processor import run_app

from .app_config import ReportGeneratorConfig
from .application import ReportGenerator


def handler(event: dict[str, Any], context: Any) -> None:
    """Run the report generator."""
    ReportGeneratorConfig.clear_elements()
    run_app(ReportGenerator(), event, context)
