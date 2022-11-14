from django.shortcuts import render
from django.conf import settings as django_settings
from django_simple_third_party_jwt import settings
from django_simple_third_party_jwt_dev_dashboard.forms import UserForm
from django_simple_third_party_jwt_dev_dashboard.settings import DEV_DASHBOARD_SETTINGS

import logging

logger = logging.getLogger(__name__)

jwt_refresh_url = DEV_DASHBOARD_SETTINGS.get('jwt_refresh_url', '')
jwt_verify_url = DEV_DASHBOARD_SETTINGS.get('jwt_verify_url', '')
jwt_token_url = DEV_DASHBOARD_SETTINGS.get('jwt_token_url', '')
dashboard_url = DEV_DASHBOARD_SETTINGS.get('dashboard_url', '')
third_party_jwt_url = DEV_DASHBOARD_SETTINGS.get('third_party_jwt_url', '')
admin_url = DEV_DASHBOARD_SETTINGS.get('admin_url', '')
swagger_url = DEV_DASHBOARD_SETTINGS.get('swagger_url', '')
redoc_url = DEV_DASHBOARD_SETTINGS.get('redoc_url', '')

debug = django_settings.DEBUG

dev_dashboard_setting = {
    'social_google_client_id': settings.SOCIAL_GOOGLE_CLIENT_ID,
    'jwt_token_url': jwt_token_url,
    'jwt_refresh_url': jwt_refresh_url,
    'jwt_verify_url': jwt_verify_url,
    'dashboard_url': dashboard_url,
    'third_party_jwt_url': third_party_jwt_url,
    'admin_url': admin_url,
    'swagger_url': swagger_url,
    'redoc_url': redoc_url,
    'debug': debug,
}


def dashboard(request):
    return render(
        request,
        "dashboard/dashboard.html",
        dev_dashboard_setting
    )

def jwt_login(request):
    dev_dashboard_setting_ = dev_dashboard_setting.copy()
    dev_dashboard_setting_['form'] = UserForm
    return render(
        request,
        "login.html",
        dev_dashboard_setting_
    )

