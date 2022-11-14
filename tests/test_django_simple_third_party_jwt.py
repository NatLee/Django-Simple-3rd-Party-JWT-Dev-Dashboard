from django.test import TestCase
from mock import Mock, patch

from django_simple_third_party_jwt.views import GoogleLogin

class LoginViewTests(TestCase):

    def test_get(self):
        request = Mock()
        request.return_value = {}

        view = GoogleLogin()

        with patch.object(GoogleLogin, 'post') as patched_proxy_method:
            handler = getattr(view, 'post')
            handler(request, credential=123)

        patched_proxy_method.assert_called_once_with(request, credential=123)

