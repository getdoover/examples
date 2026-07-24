"""Processor that hosts the dashboard widget and its device permissions."""

from pydoover.processor import Application

from .app_config import FleetOverviewDashboardConfig
from .app_ui import FleetOverviewDashboardUI


class FleetOverviewDashboardApplication(Application):
    config_cls = FleetOverviewDashboardConfig
    ui_cls = FleetOverviewDashboardUI
