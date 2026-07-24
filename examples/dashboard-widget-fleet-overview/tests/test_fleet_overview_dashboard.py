import json
from pathlib import Path

from fleet_overview_dashboard.app_config import FleetOverviewDashboardConfig
from fleet_overview_dashboard.app_ui import FleetOverviewDashboardUI
from fleet_overview_dashboard.application import (
    FleetOverviewDashboardApplication,
)


def test_processor_registers_dashboard_widget_in_interpreter_ui() -> None:
    ui_schema = FleetOverviewDashboardUI(
        None,
        None,
        None,
    ).to_schema(resolve_config=False)
    widget = ui_schema["children"]["FleetOverview"]

    assert widget["componentUrl"] == "$config.app().dv_widget_url"
    assert widget["scope"] == "FleetOverviewDashboardWidget"
    assert widget["module"] == "./FleetOverviewDashboardWidget"
    assert widget["app_key"] == "$config.app().APP_KEY"
    assert FleetOverviewDashboardApplication.config_cls is FleetOverviewDashboardConfig
    assert FleetOverviewDashboardApplication.ui_cls is FleetOverviewDashboardUI


def test_processor_requests_device_map_fields_used_by_widget() -> None:
    properties = FleetOverviewDashboardConfig.to_schema()["properties"]
    permissions = properties["dv_proc_extended_permissions"]

    assert permissions["x-extraDeviceFields"] == [
        "group__id",
        "group__name",
        "id",
        "name",
        "display_name",
    ]


def test_doover_config_associates_processor_and_widget() -> None:
    config_path = Path(__file__).parents[1] / "doover_config.json"
    application = json.loads(config_path.read_text())["fleet_overview_dashboard"]

    assert application["type"] == "PRO"
    assert (
        application["lambda_config"]["Handler"]
        == "src.fleet_overview_dashboard.handler"
    )
    assert application["build_widget_command"] == "npm run build"
    assert application["widget"] == "assets/FleetOverviewDashboardWidget.js"
