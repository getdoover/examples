import json
from pathlib import Path

from tag_values_widget.app_config import TagValuesWidgetConfig
from tag_values_widget.app_ui import TagValuesWidgetUI
from tag_values_widget.application import TagValuesWidgetApplication


def test_widget_does_not_request_cross_device_permissions() -> None:
    properties = TagValuesWidgetConfig.to_schema()["properties"]
    assert "dv_proc_extended_permissions" not in properties


def test_remote_component_matches_frontend_exposure() -> None:
    ui_schema = TagValuesWidgetUI(None, None, None).to_schema(resolve_config=False)
    widget = ui_schema["children"]["TagValuesWidget"]

    assert widget["componentUrl"] == "$config.app().dv_widget_url"
    assert widget["scope"] == "TagValuesWidget"
    assert widget["module"] == "./TagValuesWidget"


def test_application_uses_widget_config_and_ui() -> None:
    assert TagValuesWidgetApplication.config_cls is TagValuesWidgetConfig
    assert TagValuesWidgetApplication.ui_cls is TagValuesWidgetUI


def test_doover_config_associates_processor_and_widget() -> None:
    config_path = Path(__file__).parents[1] / "doover_config.json"
    application = json.loads(config_path.read_text())["tag_values_widget"]

    assert application["type"] == "PRO"
    assert (
        application["lambda_config"]["Handler"]
        == "src.tag_values_widget.handler"
    )
    assert (
        application["build_widget_command"]
        == "npm --prefix dashboard-widget run build"
    )
    assert application["widget"] == "dashboard-widget/assets/TagValuesWidget.js"
    assert (
        application["ui_schema"]["children"]["TagValuesWidget"]["type"]
        == "uiRemoteComponent"
    )
