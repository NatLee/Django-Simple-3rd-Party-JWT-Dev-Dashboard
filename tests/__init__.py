import django
from django.conf import settings

settings.configure(
    SECRET_KEY='test',
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:"
        }
    },
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "rest_framework",
        "django_simple_third_party_jwt",
    ],
    MIDDLEWARE_CLASSES=[
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ],

    # -------------- START - Google Auth Setting --------------
    SECURE_REFERRER_POLICY = "no-referrer-when-downgrade",
    # SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups",
    SECURE_CROSS_ORIGIN_OPENER_POLICY = None,
    SOCIAL_GOOGLE_CLIENT_ID = (
        "376808175534-d6mefo6b1kqih3grjjose2euree2g3cs.apps.googleusercontent.com"
    ),
    LOGIN_REDIRECT_URL = "/",
    VALID_REGISTER_DOMAINS = ["gmail.com"],
    # --------------- END - Google Auth Setting -----------------
)

django.setup()
