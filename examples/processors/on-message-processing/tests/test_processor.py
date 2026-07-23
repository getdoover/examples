"""Fast checks for the template's imports, schemas, UI, and pure parser."""

from on_message_processing.application import normalise_message


def test_normalise_message() -> None:
    assert normalise_message(
        {"value": 42, "status": "ok", "recorded_at": "2026-01-01T00:00:00Z"},
        "value",
    ) == {
        "measurement": 42.0,
        "status": "ok",
        "source_time": "2026-01-01T00:00:00Z",
    }


def test_normalise_message_rejects_invalid_values() -> None:
    assert normalise_message({"value": "not-a-number"}, "value") is None
    assert normalise_message({"value": True}, "value") is None
    assert normalise_message([], "value") is None


def test_config_and_ui_export_sources_are_valid() -> None:
    from on_message_processing.app_config import OnMessageProcessingConfig
    from on_message_processing.app_ui import OnMessageProcessingUI

    assert isinstance(OnMessageProcessingConfig.to_schema(), dict)
    assert isinstance(OnMessageProcessingUI(None, None, None).to_schema(), dict)


def test_lambda_entry_point_imports() -> None:
    from on_message_processing import handler
    from on_message_processing.application import OnMessageProcessing

    assert handler
    assert OnMessageProcessing
