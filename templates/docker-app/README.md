# Minimal Doover Docker App

The smallest useful long-running Doover device app. It starts the managed
runtime and calls the SDK's default no-op `main_loop` once per second.

Copy the folder, rename `docker_app_template`, then override `setup`,
`main_loop`, or an event handler only when your app needs it.

```bash
uv sync
uv run pytest
docker build -t docker-app-template .
```

For a hardware polling example, see
[analog-input-scaling](../../examples/docker-apps/analog-input-scaling/).
