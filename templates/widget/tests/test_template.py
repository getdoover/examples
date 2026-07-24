import json
from pathlib import Path

from widget_template.app_config import WidgetTemplateConfig
from widget_template.app_ui import WidgetTemplateUI
from widget_template.application import WidgetTemplateApplication


def test_processor_registers_widget_in_interpreter_ui() -> None:
    ui_schema = WidgetTemplateUI(None, None, None).to_schema(resolve_config=False)
    widget = ui_schema["children"]["WidgetTemplate"]

    assert widget["componentUrl"] == "$config.app().dv_widget_url"
    assert widget["scope"] == "WidgetTemplate"
    assert widget["module"] == "./WidgetTemplate"
    assert WidgetTemplateApplication.config_cls is WidgetTemplateConfig
    assert WidgetTemplateApplication.ui_cls is WidgetTemplateUI


def test_doover_config_associates_processor_and_widget() -> None:
    config_path = Path(__file__).parents[1] / "doover_config.json"
    application = json.loads(config_path.read_text())["widget_template"]

    assert application["type"] == "PRO"
    assert application["lambda_config"]["Handler"] == "src.widget_template.handler"
    assert application["build_widget_command"] == "npm run build"
    assert application["widget"] == "assets/WidgetTemplate.js"
