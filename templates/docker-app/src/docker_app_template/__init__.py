"""Container entry point for the Docker app template."""

from pydoover.docker import run_app

from .application import DockerAppTemplate


def main() -> None:
    run_app(DockerAppTemplate())
