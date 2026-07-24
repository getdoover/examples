# Doover Processor Template

The conventional file structure for a Doover processor with empty config, tags,
and UI classes. `application.py` contains no-op stubs for the public lifecycle
and processor event hooks.

Copy the folder, rename `processor_template`, then fill in only the classes and
handlers your app needs.

```bash
uv sync
uv run export-config
uv run export-ui
uv run pytest
./build.sh
```

For a real message-processing implementation, see the
[on-message-processing example](../../examples/processors/on-message-processing/).
