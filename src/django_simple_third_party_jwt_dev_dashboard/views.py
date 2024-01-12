from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.conf import settings as django_settings

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

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
    'social_microsoft_client_id': settings.SOCIAL_MICROSOFT_CLIENT_ID,
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
        "dashboard.html",
        dev_dashboard_setting
    )

@csrf_exempt
def login(request):
    # override registration login form
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # login
            auth_login(request, form.get_user())
            # redirect
            return HttpResponseRedirect(reverse('dev-dashboard'))
    else:
        form = AuthenticationForm(request)

    # copy settings and add `form`
    dev_dashboard_setting_copy = dev_dashboard_setting.copy()
    dev_dashboard_setting_copy['form'] = form
    
    return render(request, 'login.html', dev_dashboard_setting_copy)


@csrf_exempt
@login_required
def session_logout(request):
    # override session logout
    auth_logout(request)
    return HttpResponseRedirect(reverse('dev-dashboard'))

