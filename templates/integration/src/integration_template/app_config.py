"""Ingestion endpoint configuration for the integration template."""

from pathlib import Path

from pydoover import config
from pydoover.processor import IngestionEndpointConfig


class IntegrationTemplateConfig(config.Schema):
    # This is the only non-empty template field because an integration needs an
    # endpoint before it can receive a webhook.
    integration = IngestionEndpointConfig()


def export() -> None:
    IntegrationTemplateConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "integration_template",
    )
