from pydoover.processor import run_app

from .app_config import TagValuesWidgetConfig
from .application import TagValuesWidgetApplication


def handler(event, context):
    """Run the lightweight host app for the device-local widget."""
    TagValuesWidgetConfig.clear_elements()
    return run_app(TagValuesWidgetApplication(), event, context)
