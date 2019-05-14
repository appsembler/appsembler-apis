
import mock
import pytest

class AwsSettingsType(object):
    AWS = u'aws'


class ProdSettingsType(object):
    PRODUCTION = u'production'


@pytest.mark.parametrize('klass, expected_val', [
    (AwsSettingsType, AwsSettingsType.AWS),
    (ProdSettingsType, ProdSettingsType.PRODUCTION),
    ])
def test_production_settings_name(klass, expected_val):
    key = 'openedx.core.djangoapps.plugins.constants'
    module = mock.Mock()
    setattr(module, 'SettingsType', klass)
    with mock.patch.dict('sys.modules', {key: module}):
        from appsembler_apis.apps import production_settings_name
        name = production_settings_name()
        assert name == expected_val


def test_appsembler_apis_config_name():
    from appsembler_apis.apps import AppsemblerApisConfig
    assert AppsemblerApisConfig.name == 'appsembler_apis'
    assert AppsemblerApisConfig.verbose_name == 'Appsembler APIs'