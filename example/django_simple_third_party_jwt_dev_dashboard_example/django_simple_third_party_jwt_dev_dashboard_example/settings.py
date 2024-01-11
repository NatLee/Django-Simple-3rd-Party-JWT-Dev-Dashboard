"""
Django settings for this project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&1=1suv8zt()jcxx_yn2p0d424fv0pk16_h8^1vxuz6yl#kmo_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ---------------------------
    # debug relative package
    "rest_framework", # <------
    #"drf_yasg", # for swagger, optional
    'bootstrap3', # <------
    # 3rd party login
    'django_simple_third_party_jwt', # <------
    # debug dashboard
    'django_simple_third_party_jwt_dev_dashboard', # <------
    # ---------------------------
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_simple_third_party_jwt_dev_dashboard_example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_simple_third_party_jwt_dev_dashboard_example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#########################################
#########################################
#########################################


# -------------- START - Policy Setting --------------
SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"
# SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"
SECURE_CROSS_ORIGIN_OPENER_POLICY = None
# -------------- END - Policy Setting -----------------

# -------------- START - Dashboard Setting --------------
DEV_DASHBOARD_SETTINGS = {
    'jwt_token_url': 'api/auth/token',
    'jwt_refresh_url': 'api/auth/token/refresh',
    'jwt_verify_url': 'api/auth/token/verify',
    'dashboard_url': 'api/__hidden_dev_dashboard',
    'third_party_jwt_url': 'api',
    'admin_url': 'api/__hidden_admin',
    #'swagger_url': 'api/__hidden_swagger', # optional
    #'redoc_url': 'api/__hidden_redoc', # optional
}
# --------------- END - Dashboard Setting -----------------

# New settings for django_simple_third_party_jwt
LOGIN_REDIRECT_URL = '/' + DEV_DASHBOARD_SETTINGS['dashboard_url']
MICROSOFT_CALLBACK_PATH = "api/auth/microsoft/callback"
MICROSOFT_SIGNIN_PATH = "api/auth/microsoft/signin"
# ----------------------------------------------

#########################################
#########################################
#########################################




