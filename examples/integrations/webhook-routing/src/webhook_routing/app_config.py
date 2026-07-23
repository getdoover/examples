"""Configuration shown when the integration is installed in Doover."""

from pathlib import Path

from pydoover import config
from pydoover.processor import ExtendedPermissionsConfig, IngestionEndpointConfig


class WebhookRoutingConfig(config.Schema):
    # IngestionEndpointConfig provides CIDR filtering, optional HMAC signing,
    # throttling, and endpoint token settings in the installation form.
    integration = IngestionEndpointConfig()

    # Sending to another agent requires explicit extended permissions. Keep
    # these grants as narrow as possible in each installation.
    permissions = ExtendedPermissionsConfig()


def export() -> None:
    """Write this schema into the app entry in doover_config.json."""
    WebhookRoutingConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "webhook_routing",
    )


if __name__ == "__main__":
    export()
