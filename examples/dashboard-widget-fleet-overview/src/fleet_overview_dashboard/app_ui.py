"""Interpreter UI registration for the fleet overview dashboard."""

from pathlib import Path

from pydoover import ui


class FleetOverviewDashboardUI(ui.UI, default_open=True):
    widget = ui.RemoteComponent(
        name="FleetOverview",
        display_name="Fleet Overview",
        component_url="$config.app().dv_widget_url",
        scope="FleetOverviewDashboardWidget",
        module="./FleetOverviewDashboardWidget",
        app_key="$config.app().APP_KEY",
    )


def export() -> None:
    FleetOverviewDashboardUI(None, None, None).export(
        Path(__file__).parents[2] / "doover_config.json",
        "fleet_overview_dashboard",
    )
