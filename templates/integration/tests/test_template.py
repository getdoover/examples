from integration_template import IntegrationTemplate, handler
from integration_template.app_config import IntegrationTemplateConfig


def test_template_imports() -> None:
    assert IntegrationTemplate()
    assert isinstance(IntegrationTemplateConfig.to_schema(), dict)
    assert handler
