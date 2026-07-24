"""Interpreter UI registration for the widget template."""

from pathlib import Path

from pydoover import ui


class WidgetTemplateUI(ui.UI, default_open=True):
    widget = ui.RemoteComponent(
        name="WidgetTemplate",
        display_name="Widget Template",
        component_url="$config.app().dv_widget_url",
        scope="WidgetTemplate",
        module="./WidgetTemplate",
    )


def export() -> None:
    WidgetTemplateUI(None, None, None).export(
        Path(__file__).parents[2] / "doover_config.json",
        "widget_template",
    )
