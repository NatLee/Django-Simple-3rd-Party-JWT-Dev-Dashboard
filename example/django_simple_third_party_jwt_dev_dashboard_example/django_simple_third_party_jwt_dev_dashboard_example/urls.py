"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include
from django.conf import settings

urlpatterns = []


# --------------- 3rd party login
# app route
urlpatterns += [
    path(settings.DEV_DASHBOARD_SETTINGS['third_party_jwt_url'] + "/", include("django_simple_third_party_jwt.urls")),
]
# ------------------------------

# --------------- Dashboard
urlpatterns += [
    # debug dashboard
    path(settings.DEV_DASHBOARD_SETTINGS['dashboard_url'] + "/", include("django_simple_third_party_jwt_dev_dashboard.urls")),
]
# ------------------------------


# --------------- Admin
urlpatterns += [
    # admin
    path(settings.DEV_DASHBOARD_SETTINGS['admin_url'] + "/", admin.site.urls),
]
# ------------------------------

# --------------- JWT
from rest_framework_simplejwt.views import (
    TokenVerifyView, TokenObtainPairView, TokenRefreshView
)
urlpatterns += [
    path(
        settings.DEV_DASHBOARD_SETTINGS['jwt_token_url'],
        TokenObtainPairView.as_view(), name="token-get"
    ),
    path(
        settings.DEV_DASHBOARD_SETTINGS['jwt_refresh_url'],
        TokenRefreshView.as_view(), name="token-refresh"
    ),
    path(
        settings.DEV_DASHBOARD_SETTINGS['jwt_verify_url'],
        TokenVerifyView.as_view(), name="token-verify"
    ),
]
# ---------------------------------

'''
# ----------------------- Swagger
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny, IsAdminUser
schema_view = get_schema_view(
    openapi.Info(
        title="DEV DASHBOARD API",
        default_version="v1",
        description="DEV API",
    ),
    public=True,
    permission_classes=(AllowAny,)
    #permission_classes = (IsAdminUser,) # 限制is_staff才可使用
)

urlpatterns += [
    re_path(
        r"^api/__hidden_swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^api/__hidden_swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^api/__hidden_redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
# --------------------------------------------

'''


