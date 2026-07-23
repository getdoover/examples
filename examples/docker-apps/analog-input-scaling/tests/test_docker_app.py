"""Fast checks for scaling, imports, config, and UI definitions."""

import pytest

from analog_input_scaling.application import scale_reading


def test_scale_reading() -> None:
    assert scale_reading(4, 4, 20, 0, 100) == 0
    assert scale_reading(12, 4, 20, 0, 100) == 50
    assert scale_reading(20, 4, 20, 0, 100) == 100


def test_scale_reading_clamps_by_default() -> None:
    assert scale_reading(0, 4, 20, 0, 100) == 0
    assert scale_reading(24, 4, 20, 0, 100) == 100
    assert scale_reading(24, 4, 20, 0, 100, clamp=False) == 125


def test_scale_reading_rejects_zero_width_input() -> None:
    with pytest.raises(ValueError, match="must be different"):
        scale_reading(10, 4, 4, 0, 100)


def test_config_and_ui_export_sources_are_valid() -> None:
    from analog_input_scaling.app_config import AnalogInputScalingAppConfig
    from analog_input_scaling.app_ui import AnalogInputScalingAppUI

    assert isinstance(AnalogInputScalingAppConfig.to_schema(), dict)
    assert isinstance(AnalogInputScalingAppUI(None, None, None).to_schema(), dict)


def test_container_entry_point_imports() -> None:
    from analog_input_scaling import main
    from analog_input_scaling.application import AnalogInputScalingApplication

    assert main
    assert AnalogInputScalingApplication
