"""Minimal Doover Docker app entry point."""

from pydoover.docker import Application, run_app


class DockerAppTemplate(Application):
    """No-op device app; override only the lifecycle methods your app needs."""


def main() -> None:
    run_app(DockerAppTemplate())
