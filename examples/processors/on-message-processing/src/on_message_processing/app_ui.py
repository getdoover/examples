"""Doover dashboard definition for the processor."""

from pathlib import Path

from pydoover import ui

from .app_tags import OnMessageProcessingTags


class OnMessageProcessingUI(ui.UI):
    # UI values bind to tags, so application code only has to update the tags.
    measurement = ui.NumericVariable(
        "Measurement",
        value=OnMessageProcessingTags.measurement,
        precision=2,
        ranges=[
            ui.Range("Low", 0, 25, ui.Colour.blue, show_on_graph=True),
            ui.Range("Normal", 25, 75, ui.Colour.green, show_on_graph=True),
            ui.Range("High", 75, 100, ui.Colour.yellow, show_on_graph=True),
        ],
    )
    status = ui.TextVariable("Status", value=OnMessageProcessingTags.status)
    source_time = ui.DateTimeVariable(
        "Source Time",
        value=OnMessageProcessingTags.source_time,
    )
    last_processed_at = ui.DateTimeVariable(
        "Last Processed",
        value=OnMessageProcessingTags.last_processed_at,
    )


def export() -> None:
    """Write this UI definition into doover_config.json."""
    OnMessageProcessingUI(None, None, None).export(
        Path(__file__).parents[2] / "doover_config.json",
        "on_message_processing",
    )


if __name__ == "__main__":
    export()
