from django.utils.translation import gettext_lazy as _

from pathlib import Path
from decouple import config

import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")], default="*"
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "corsheaders",
    "rest_framework",
    "ckeditor",
    'ckeditor_uploader',
    "modeltranslation",
    # local apps
    "app_settings",
    "app_inquery",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # multi language
    "django.middleware.locale.LocaleMiddleware",
    # cors-headers
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
SQL_LITE_DATABASE = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
}

if config("USE_MYSQL", default=False, cast=bool):
    MYSQL_DATABASE = {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("MYSQL_NAME"),
        "USER": config("MYSQL_USER"),
        "PASSWORD": config("MYSQL_PASS"),
        "HOST": config("MYSQL_HOST"),
        "PORT": config("MYSQL_PORT", cast=int),
    }

if config("USE_POSTGRES", default=False, cast=bool):
    POSTGRES_SQL_DATABASE = {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_NAME"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASS"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT", cast=int),
    }


def get_default_detabase(default_database=config("DEFAULT_DATABASE_NAME", default="")):
    match default_database.upper():
        case "MYSQL":
            return MYSQL_DATABASE
        case "POSTGRESQL":
            return POSTGRES_SQL_DATABASE
        case _:
            return SQL_LITE_DATABASE


DATABASES = {"default": get_default_detabase()}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ___django settings___ #
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# Media files (Images, Files)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# Internationalization
LANGUAGES = [
    ("en", _("English")),
    ("fa", _("Persian")),
]
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ___Request Api Options___ #
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_REGEX_WHITELIST = config(
    "CORS_ORIGIN_REGEX_WHITELIST",
    cast=lambda v: [s.strip() for s in v.split(",")],
    default="*",
)
CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    cast=lambda v: [s.strip() for s in v.split(",")],
    default="http://localhost:8000",
)

# __CKEditor Settings__ #
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}
