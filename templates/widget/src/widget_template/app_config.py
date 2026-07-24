"""Installation configuration for the widget template."""

from pathlib import Path

from pydoover import config


class WidgetTemplateConfig(config.Schema):
    position = config.ApplicationPosition()


def export() -> None:
    WidgetTemplateConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "widget_template",
    )
