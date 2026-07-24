# Doover Docker App Template

The conventional file structure for a Doover device app with empty config,
tags, and UI classes. `application.py` contains no-op stubs for the public
lifecycle, subscription-event, and shutdown hooks.

Copy the folder, rename `docker_app_template`, then fill in only the classes and
handlers your app needs.

```bash
uv sync
uv run export-config
uv run export-ui
uv run pytest
docker build -t docker-app-template .
```

For a hardware polling example, see
[analog-input-scaling](../../examples/docker-apps/analog-input-scaling/).
