"""Empty UI definition for the processor template."""

from pathlib import Path

from pydoover import ui


class ProcessorTemplateUI(ui.UI):
    pass


def export() -> None:
    ProcessorTemplateUI(None, None, None).export(
        Path(__file__).parents[2] / "doover_config.json",
        "processor_template",
    )
