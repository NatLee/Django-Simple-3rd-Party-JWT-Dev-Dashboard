# Django Simple 3rd Party JWT Dev Dashboard

This is a simple dashboard for showing multi login(JWT, session and 3rd party).

Dashboard is used with [Django-Simple-3rd-Party-JWT](https://github.com/NatLee/Django-Simple-3rd-Party-JWT).

## Installation

```bash
pip install django-simple-third-party-jwt-dev-dashboard
```

Check it in [Pypi](https://pypi.org/project/django-simple-third-party-jwt-dev-dashboard/).

## Quick Start

- `settings.py`

  Add the followings to your settings of project.

  - (MUST) Install app

  ```python
  INSTALLED_APPS += [
      # ---------------------------
      # debug relative package
      "rest_framework", # <------ MUST
      #"drf_yasg", # (OPTIONAL) for swagger
      'bootstrap3', # <------ MUST
      # 3rd party login
      'django_simple_third_party_jwt' # <------ MUST
      # debug dashboard
      'django_simple_third_party_jwt_dev_dashboard', # <------ MUST
      # ---------------------------
  ]
  ```

  - (MUST) Dashboard settings

  ```python
  # -------------- START - Dashboard Setting --------------
  DEV_DASHBOARD_SETTINGS = {
      'jwt_token_url': 'api/auth/token',
      'jwt_refresh_url': 'api/auth/token/refresh',
      'jwt_verify_url': 'api/auth/token/verify',
      'dashboard_url': 'api/__hidden_dev_dashboard',
      'admin_url': 'api/__hidden_admin',
      #'swagger_url': 'api/__hidden_swagger', # OPTIONAL
      #'redoc_url': 'api/__hidden_redoc', # OPTIONAL
  }
  # --------------- END - Dashboard Setting -----------------

  # -------------- START - 3rd party login Setting --------------
  LOGIN_REDIRECT_URL = '/' + DEV_DASHBOARD_SETTINGS['dashboard_url'] # <- (OPTIONAL) for redirect after login
  JWT_3RD_PREFIX = 'api' # <- (OPTIONAL) for 3rd party login
  # --------------- END - 3rd party login Setting -----------------
  ```

  - (MUST) Policy for Google API

  ```python
  # -------------- START - Policy Setting --------------
  SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"
  # SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"
  SECURE_CROSS_ORIGIN_OPENER_POLICY = None
  # -------------- END - Policy Setting -----------------
  ```

  - (OPTIONAL) Configuration for 3rd party login

  ```python
  VALID_REGISTER_DOMAINS = ["gmail.com", "hotmail.com"]

  # -------------- START - Google Auth Setting --------------
  SOCIAL_GOOGLE_CLIENT_ID = "376808175534-d6mefo6b1kqih3grjjose2euree2g3cs.apps.googleusercontent.com"
  # --------------- END - Google Auth Setting -----------------

  # -------------- START - Microsoft Auth Setting --------------
  SOCIAL_MICROSOFT_CLIENT_ID = '32346173-22bc-43b2-b6ed-f88f6a76e38c'
  SOCIAL_MICROSOFT_CLIENT_SECRET = 'K5z8Q~dIXDiFN5qjMjRjIx34cZOJ3Glkrg.dxcG9'
  # --------------- END - Microsoft Auth Setting -----------------

  ```

> You can regist `SOCIAL_GOOGLE_CLIENT_ID` on Google Cloud Platform.

  [Google Colud | API和服務 | 憑證](https://console.cloud.google.com/apis/credentials)

  1. Create a new project and create a new OAuth 2.0 Client ID.
    ![](https://i.imgur.com/7UKP3I7.png)

  2. Add `http://localhost:8000` to `Authorized JavaScript origins` and `Authorized redirect URIs`.
    ![](https://i.imgur.com/IoTRs4j.png)

> You can regist `SOCIAL_MICROSOFT_CLIENT_ID` on Microsoft Azure.

[Microsoft Entra 識別碼 | 應用程式註冊](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps)

  1. Create a new application.
    ![](https://i.imgur.com/my5UtXv.png)
  2. Add `http://localhost:8000/api/auth/microsoft/callback` to `Redirect URIs`
    ![](https://i.imgur.com/lsaZgMM.png)
  3. Get `Client ID` from `Overview` page.
    ![](https://i.imgur.com/5oo3xnI.png)
  4. Get `Client Secret` from `Certificates & secrets` page.
    ![](https://i.imgur.com/3F5ge7l.png)


- `urls.py`

  URL path for dashboard. (MUST)

  ```python
  # --------------- 3rd party login
  # app route
  urlpatterns += [
      path("", include("django_simple_third_party_jwt.urls")),
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
      path(settings.DEV_DASHBOARD_SETTINGS['jwt_token_url'], TokenObtainPairView.as_view(), name="token_get"),
      path(settings.DEV_DASHBOARD_SETTINGS['jwt_refresh_url'], TokenRefreshView.as_view(), name="token_refresh"),
      path(settings.DEV_DASHBOARD_SETTINGS['jwt_verify_url'], TokenVerifyView.as_view(), name="token_verify"),
  ]
  # ---------------------------------
  ```

When you added all settings, just run:

```bash
python manage.py runserver 0.0.0.0:8000
```

And visit `http://localhost:8000/api/__hidden_dev_dashboard`

![dashboard](https://i.imgur.com/cXwg2DS.png)

## Example

Check `./example/django_simple_third_party_jwt_dev_dashboard_example/`.

## More

There are several different settings can be added with this dashboard if you need.

- CORS Setting

```python
ALLOWED_HOSTS = ["*"]
LOGIN_REDIRECT_URL = "/"

# -------------- START - CORS Setting --------------
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1",
    "http://localhost",
]
# -------------- END - CORS Setting -----------------
```

- Swagger setting

```python
# -------------- Swagger Setting --------------
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Token(add prefix `Bearer` yourself)": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
    "LOGIN_URL": "/api/__hiddenadmin/login/",
    "LOGOUT_URL": "/api/__hiddenadmin/logout/",
}

# --------------------------------------------
```

- SimpleJWT setting

```python

# -------------- Start - SimpleJWT Setting --------------
from datetime import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=3600),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}
# -------------- END - SimpleJWT Setting --------------

```

## Misc tools

### Install & re-install package

* Linux

```bash
bash dev-reinstall.sh
```

* Windows

```powershell
./dev-reinstall.ps1
```
