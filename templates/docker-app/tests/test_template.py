from docker_app_template import DockerAppTemplate, main


def test_template_imports() -> None:
    assert DockerAppTemplate(test_mode=True)
    assert main
