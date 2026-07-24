from pathlib import Path

from pydoover import config


class TagValuesWidgetConfig(config.Schema):
    """Only standard app placement is needed for this device-local widget."""

    position = config.ApplicationPosition()


def export() -> None:
    TagValuesWidgetConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "tag_values_widget",
    )
