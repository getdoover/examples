from pathlib import Path

from pydoover import ui


class TagValuesWidgetUI(ui.UI, default_open=True):
    widget = ui.RemoteComponent(
        name="TagValuesWidget",
        display_name="Tag Values",
        component_url="$config.app().dv_widget_url",
        scope="TagValuesWidget",
        module="./TagValuesWidget",
    )


def export() -> None:
    TagValuesWidgetUI(None, None, None).export(
        Path(__file__).parents[2] / "doover_config.json",
        "tag_values_widget",
    )
