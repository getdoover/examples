"""Companion processor that hosts the widget in the interpreter UI."""

from pydoover.processor import Application

from .app_config import WidgetTemplateConfig
from .app_ui import WidgetTemplateUI


class WidgetTemplateApplication(Application):
    config_cls = WidgetTemplateConfig
    ui_cls = WidgetTemplateUI
