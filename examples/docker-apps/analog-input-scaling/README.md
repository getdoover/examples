# Analog Input Scaling Example

A working device-app example adapted from
[Analog Level Sensor](https://github.com/getdoover/analog-level-sensor). It polls
an analog input, scales it into an engineering value, publishes tags, and
displays the result in the Doover UI.

Start with the [minimal Docker app template](../../../templates/docker-app/)
when you only need an empty managed application loop.

## Run the example

```bash
uv sync
uv run pytest
uv run export-config
uv run export-ui
docker build -t analog-input-scaling .
```

## What the sample does

The app reads a configured analog input through Doover's `platform_interface`,
linearly maps the raw input range into an engineering range, and writes both
values to tags. An optional digital output can power the sensor, and is switched
off during a managed shutdown.

For example, the defaults map a 4–20 mA input onto 0–100%:

| Input | Scaled value |
| --- | ---: |
| 4 mA | 0% |
| 12 mA | 50% |
| 20 mA | 100% |

## Project map

| Path | Purpose |
| --- | --- |
| `Dockerfile` | Reproducible two-stage device image |
| `src/analog_input_scaling/__init__.py` | Container command entry point |
| `src/analog_input_scaling/app_config.py` | Hardware and scaling configuration |
| `src/analog_input_scaling/app_tags.py` | Raw/scaled values exposed to the platform |
| `src/analog_input_scaling/app_ui.py` | Dashboard elements bound to tags |
| `src/analog_input_scaling/application.py` | Polling loop, scaling, and safe shutdown |
| `doover_config.json` | Device-app metadata plus generated config/UI schemas |

## Hardware and deployment notes

- `platform_interface` is declared as a dependency in `doover_config.json` and
  supplies `fetch_ai` and `set_do`.
- The container inherits from `spaneng/doover_device_base`, matching current
  Doover device apps.
- The Dockerfile builds for the platform selected by the caller. The app
  metadata advertises both `linux/amd64` and `linux/arm64`.
- Keep blocking I/O out of `main_loop`; use asynchronous drivers or run blocking
  calls outside the event loop.
