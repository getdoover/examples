"""Doover dashboard definition for the Docker app."""

from pathlib import Path

from pydoover import ui

from .app_tags import AnalogInputScalingAppTags


class AnalogInputScalingAppUI(ui.UI):
    scaled_value = ui.NumericVariable(
        "Scaled Value",
        value=AnalogInputScalingAppTags.scaled_value,
        precision=2,
        form=ui.Widget.radial,
    )
    raw_input = ui.NumericVariable(
        "Raw Input",
        value=AnalogInputScalingAppTags.raw_input,
        precision=3,
    )
    last_read_at = ui.DateTimeVariable(
        "Last Reading",
        value=AnalogInputScalingAppTags.last_read_at,
    )

    async def setup(self) -> None:
        """Apply installation-specific units and gauge ranges at runtime."""
        low, high = sorted(
            (
                float(self.config.output_minimum.value),
                float(self.config.output_maximum.value),
            )
        )
        midpoint = low + (high - low) * 0.2

        self.scaled_value.units = self.config.output_units.value
        self.scaled_value.ranges = [
            ui.Range("Low", low, midpoint, ui.Colour.blue),
            ui.Range("Normal", midpoint, high, ui.Colour.green),
        ]


def export() -> None:
    """Write this UI definition into doover_config.json."""
    AnalogInputScalingAppUI(None, None, None).export(
        Path(__file__).parents[2] / "doover_config.json",
        "analog_input_scaling",
    )


if __name__ == "__main__":
    export()
