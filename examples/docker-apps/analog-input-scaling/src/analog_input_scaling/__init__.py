"""Container entry point for the example device application."""

from pydoover.docker import run_app

from .application import AnalogInputScalingApplication


def main() -> None:
    """Start the managed pydoover application loop."""
    run_app(AnalogInputScalingApplication())
