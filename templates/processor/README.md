# Minimal Doover Processor

The smallest useful Doover processor project. It deploys and starts, but uses
the SDK's default no-op event handlers, empty config, empty tags, and empty UI.

Copy the folder, rename `processor_template`, then add only the event method you
need, such as `on_message_create`, `on_schedule`, or `on_manual_invoke`.

```bash
uv sync
uv run pytest
./build.sh
```

For a real message-processing implementation, see the
[on-message-processing example](../../examples/processors/on-message-processing/).
