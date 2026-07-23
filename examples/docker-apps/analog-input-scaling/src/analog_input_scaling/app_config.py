"""Hardware and scaling configuration for the example device app."""

from pathlib import Path

from pydoover import config


class AnalogInputScalingAppConfig(config.Schema):
    ai_pin = config.Integer(
        "Analog Input Pin",
        description="Platform-interface analog input number to poll.",
        position=0,
    )
    power_pin = config.Integer(
        "Sensor Power Pin",
        description="Optional digital output used to power the sensor.",
        default=None,
        position=1,
    )
    polling_frequency = config.Number(
        "Polling Frequency (Hz)",
        description="Number of sensor readings requested per second.",
        default=1.0,
        minimum=0.01,
        position=2,
    )
    input_minimum = config.Number(
        "Input Minimum",
        description="Raw sensor value corresponding to the output minimum.",
        default=4.0,
        position=3,
    )
    input_maximum = config.Number(
        "Input Maximum",
        description="Raw sensor value corresponding to the output maximum.",
        default=20.0,
        position=4,
    )
    output_minimum = config.Number(
        "Output Minimum",
        description="Engineering value produced at the input minimum.",
        default=0.0,
        position=5,
    )
    output_maximum = config.Number(
        "Output Maximum",
        description="Engineering value produced at the input maximum.",
        default=100.0,
        position=6,
    )
    output_units = config.String(
        "Output Units",
        description="Units displayed beside the scaled value.",
        default="%",
        position=7,
    )
    clamp_output = config.Boolean(
        "Clamp Output",
        description="Keep scaled values inside the configured output range.",
        default=True,
        position=8,
    )

    position = config.ApplicationPosition(position=9)
    default_open = config.ApplicationDefaultOpen(position=10)


def export() -> None:
    """Write this schema into the app entry in doover_config.json."""
    AnalogInputScalingAppConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "analog_input_scaling",
    )


if __name__ == "__main__":
    export()
