# On Message Processing Example

A working cloud-processor example adapted from the processor in
[Digital Matter](https://github.com/getdoover/digital_matter). It demonstrates
subscriptions, payload validation, tags, UI binding, calibration, and connection
status using a small vendor-neutral message.

Start with the [minimal processor template](../../../templates/processor/) when
you do not need these features yet.

## Run the example

```bash
uv sync
uv run pytest
uv run export-config
uv run export-ui
./build.sh
```

## Example input

The processor expects messages like this on `on_example_data`:

```json
{
  "value": 42.5,
  "status": "ok",
  "recorded_at": "2026-01-01T00:00:00Z"
}
```

The message is converted into tags, which in turn drive the exported UI. The
processor also updates the agent connection state whenever a valid message is
received.

## Project map

| Path | Purpose |
| --- | --- |
| `src/on_message_processing/__init__.py` | AWS Lambda entry point |
| `src/on_message_processing/app_config.py` | Installation configuration schema |
| `src/on_message_processing/app_tags.py` | Stable values exposed to other apps and the UI |
| `src/on_message_processing/app_ui.py` | Dashboard elements bound to tags |
| `src/on_message_processing/application.py` | Message processing and connection handling |
| `doover_config.json` | App metadata plus generated config/UI schemas |
| `build.sh` | Reproducible Lambda zip build |

Keep parsing and validation separate from side effects where practical. Pure
functions such as `normalise_message` are straightforward to unit test and make
vendor payload changes safer.
