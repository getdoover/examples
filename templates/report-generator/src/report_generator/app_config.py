from pathlib import Path

from pydoover import config
from pydoover.processor import (
    ExtendedPermissionsConfig,
    ScheduleConfig,
    TimezoneConfig,
)


class ReportGeneratorConfig(config.Schema):
    dv_proc_extended_permissions = ExtendedPermissionsConfig()
    dv_proc_schedules = ScheduleConfig(
        allowed_modes=["cron"],
        default="cron(0 8 1 * ?)",
    )
    dv_proc_timezone = TimezoneConfig()


def export() -> None:
    ReportGeneratorConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "report_generator",
    )
