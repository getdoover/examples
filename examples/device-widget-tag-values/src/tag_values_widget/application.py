from pydoover.processor import Application

from .app_config import TagValuesWidgetConfig
from .app_ui import TagValuesWidgetUI


class TagValuesWidgetApplication(Application):
    """Hosts a widget whose data access stays scoped to the current device."""

    config_cls = TagValuesWidgetConfig
    ui_cls = TagValuesWidgetUI
