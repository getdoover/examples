"""Empty UI definition for the Docker app template."""

from pathlib import Path

from pydoover import ui


class DockerAppTemplateUI(ui.UI):
    pass


def export() -> None:
    DockerAppTemplateUI(None, None, None).export(
        Path(__file__).parents[2] / "doover_config.json",
        "docker_app_template",
    )
