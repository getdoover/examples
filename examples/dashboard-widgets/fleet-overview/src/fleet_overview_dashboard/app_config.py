"""Permissions and placement for the fleet overview dashboard."""

from pathlib import Path

from pydoover import config
from pydoover.processor import ExtendedPermissionsConfig


class FleetOverviewDashboardConfig(config.Schema):
    extended_permissions = ExtendedPermissionsConfig(
        extra_fields=[
            "group__id",
            "group__name",
            "id",
            "name",
            "display_name",
        ]
    )
    position = config.ApplicationPosition()


def export() -> None:
    FleetOverviewDashboardConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "fleet_overview_dashboard",
    )
