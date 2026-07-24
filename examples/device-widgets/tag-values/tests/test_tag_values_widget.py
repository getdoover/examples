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
