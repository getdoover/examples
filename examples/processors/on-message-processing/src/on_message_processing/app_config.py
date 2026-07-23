"""Configuration shown when the processor is installed in Doover."""

from pathlib import Path

from pydoover import config
from pydoover.processor import ManySubscriptionConfig


class OnMessageProcessingConfig(config.Schema):
    # The runtime invokes on_message_create for messages on these channels.
    # Change the default to the channel published by your integration.
    subscription = ManySubscriptionConfig(default=["on_example_data"], advanced=True)

    measurement_field = config.String(
        "Measurement Field",
        description="JSON field containing the numeric value to process.",
        default="value",
    )
    value_offset = config.Number(
        "Value Offset",
        description="Optional calibration offset added to each measurement.",
        default=0.0,
    )
    offline_after_minutes = config.Number(
        "Offline After (minutes)",
        description="Mark the source offline if another message does not arrive in time.",
        default=60.0,
        minimum=1.0,
    )

    # These standard fields control where the app appears on an agent page.
    position = config.ApplicationPosition()
    default_open = config.ApplicationDefaultOpen()


def export() -> None:
    """Write this schema into the app entry in doover_config.json."""
    OnMessageProcessingConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "on_message_processing",
    )


if __name__ == "__main__":
    export()
