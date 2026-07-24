"""Empty UI definition for the integration template."""

from pathlib import Path

from pydoover import ui


class IntegrationTemplateUI(ui.UI):
    pass


def export() -> None:
    IntegrationTemplateUI(None, None, None).export(
        Path(__file__).parents[2] / "doover_config.json",
        "integration_template",
    )
