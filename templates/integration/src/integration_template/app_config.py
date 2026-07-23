from pathlib import Path

from pydoover import config
from pydoover.processor import IngestionEndpointConfig


class IntegrationTemplateConfig(config.Schema):
    integration = IngestionEndpointConfig()


def export() -> None:
    IntegrationTemplateConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "integration_template",
    )
