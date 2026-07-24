"""Empty installation configuration for the processor template."""

from pathlib import Path

from pydoover import config


class ProcessorTemplateConfig(config.Schema):
    pass


def export() -> None:
    ProcessorTemplateConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "processor_template",
    )
