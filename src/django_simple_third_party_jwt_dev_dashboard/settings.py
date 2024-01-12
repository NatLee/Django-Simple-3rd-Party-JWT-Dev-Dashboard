
from django.conf import settings

DEV_DASHBOARD_SETTINGS = getattr(settings, "DEV_DASHBOARD_SETTINGS", {
    'jwt_token_url': 'api/auth/token',
    'jwt_refresh_url': 'api/auth/token/refresh',
    'jwt_verify_url': 'api/auth/token/verify',
    'dashboard_url': 'api/__hidden_dev_dashboard',
    'admin_url': 'api/__hidden_admin',
    'swagger_url': 'api/__hidden_swagger',
    'redoc_url': 'api/__hidden_redoc',
})

JWT_3RD_PREFIX = getattr(settings, "JWT_3RD_PREFIX", 'api')

