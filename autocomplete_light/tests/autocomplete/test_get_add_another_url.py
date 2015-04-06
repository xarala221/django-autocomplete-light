import mock

from django import test
from django.test import override_settings

import autocomplete_light.shortcuts as autocomplete_light


try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django < 1.5
    from django.conf.urls.defaults import patterns, url

urlpatterns = [
    url(r'nokwarg/$', mock.Mock, name='test_nokwarg'),
    url(r'onekwarg/(?P<param>\w+)/$', mock.Mock, name='test_onekwarg'),
]


@override_settings(ROOT_URLCONF='autocomplete_light.tests.autocomplete.test_get_add_another_url')
class GetAddAnotherUrlTestCase(test.TestCase):

    def generate_url(self, name, kwargs=None):
        class TestAutocomplete(autocomplete_light.AutocompleteBase):
            add_another_url_name = name
            add_another_url_kwargs = kwargs

        return TestAutocomplete().get_add_another_url()

    def test_no_kwargs(self):
        self.assertEquals(self.generate_url('test_nokwarg'),
                          '/nokwarg/?_popup=1')

    def test_with_kwargs(self):
        self.assertEquals(self.generate_url('test_onekwarg', {'param': 'bar'}),
                          '/onekwarg/bar/?_popup=1')
