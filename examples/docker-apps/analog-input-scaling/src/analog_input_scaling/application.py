"""Managed device polling loop for the example Docker app."""

import logging
from datetime import datetime, timezone

from pydoover.docker import Application

from .app_config import AnalogInputScalingAppConfig
from .app_tags import AnalogInputScalingAppTags
from .app_ui import AnalogInputScalingAppUI

log = logging.getLogger(__name__)


def scale_reading(
    value: float,
    input_minimum: float,
    input_maximum: float,
    output_minimum: float,
    output_maximum: float,
    *,
    clamp: bool = True,
) -> float:
    """Linearly map a raw reading into engineering units.

    Keeping conversion independent from platform I/O makes calibration logic
    easy to test. Reversed output ranges are supported; a zero-width input range
    is rejected because it cannot define a scale.
    """
    if input_minimum == input_maximum:
        raise ValueError("input minimum and maximum must be different")

    ratio = (value - input_minimum) / (input_maximum - input_minimum)
    scaled = output_minimum + ratio * (output_maximum - output_minimum)

    if not clamp:
        return scaled
    lower, upper = sorted((output_minimum, output_maximum))
    return min(max(scaled, lower), upper)


class AnalogInputScalingApplication(Application):
    config_cls = AnalogInputScalingAppConfig
    tags_cls = AnalogInputScalingAppTags
    ui_cls = AnalogInputScalingAppUI

    config: AnalogInputScalingAppConfig
    tags: AnalogInputScalingAppTags
    ui: AnalogInputScalingAppUI

    async def setup(self) -> None:
        """Prepare optional sensor power and the managed loop frequency."""
        frequency = float(self.config.polling_frequency.value)
        self.loop_target_period = 1 / frequency

        if self.config.power_pin.value is not None:
            await self.platform_iface.set_do(int(self.config.power_pin.value), True)

    async def main_loop(self) -> None:
        """Read one sample, convert it, and publish the resulting tags."""
        raw_value = await self.platform_iface.fetch_ai(int(self.config.ai_pin.value))
        if raw_value is None:
            log.warning("Analog input %s returned no value", self.config.ai_pin.value)
            return

        scaled_value = scale_reading(
            float(raw_value),
            float(self.config.input_minimum.value),
            float(self.config.input_maximum.value),
            float(self.config.output_minimum.value),
            float(self.config.output_maximum.value),
            clamp=bool(self.config.clamp_output.value),
        )

        log.debug("Raw input %s scaled to %s", raw_value, scaled_value)
        await self.tags.raw_input.set(float(raw_value))
        await self.tags.scaled_value.set(scaled_value)
        await self.tags.last_read_at.set(datetime.now(timezone.utc).isoformat())

    async def on_shutdown_at(self, _seconds: int) -> None:
        """Remove sensor power when the runtime begins a managed shutdown."""
        if self.config.power_pin.value is not None:
            await self.platform_iface.set_do(int(self.config.power_pin.value), False)
