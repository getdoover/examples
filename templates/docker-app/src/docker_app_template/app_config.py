"""Empty installation configuration for the Docker app template."""

from pathlib import Path

from pydoover import config


class DockerAppTemplateConfig(config.Schema):
    pass


def export() -> None:
    DockerAppTemplateConfig.export(
        Path(__file__).parents[2] / "doover_config.json",
        "docker_app_template",
    )
