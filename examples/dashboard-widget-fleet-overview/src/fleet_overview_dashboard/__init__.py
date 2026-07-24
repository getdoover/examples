"""Lambda entry point for the fleet overview dashboard processor."""

from typing import Any

from pydoover.processor import run_app

from .application import FleetOverviewDashboardApplication


def handler(event: dict[str, Any], context: Any) -> None:
    run_app(FleetOverviewDashboardApplication(), event, context)
