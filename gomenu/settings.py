"""
Django settings for gomenu project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url

#import django_heroku
import sentry_sdk
from decouple import config, Csv
#from dj_database_url import parse as dburl
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default=[], cast=Csv())

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # MyApps
    "core",
    "restaurants",
    "menus",
    "products",
    "orders",
    # QRcode
    "qr_code",
    # Admin ordering
    "admin_ordering",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Django DebugToolbar
# Y

ROOT_URLCONF = "gomenu.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "gomenu.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# default_dburl = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")

# DATABASES = {
#     "default": config("DATABASE_URL", default=default_dburl, cast=dburl),
# }

#BASE DE DADOS LOCAL - DESENVOLVIMENTO
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cardapio_db',
        'USER': 'postgres',
        'PASSWORD': 'n3140n',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Required by Django > 3.2
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Redirect to home URL after login # TODO(Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = "dashboard"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Configuration for dev environment
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Media Files (Uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

COLLECTFAST_ENABLED = False

# Configure Django App for Heroku.
#django_heroku.settings(locals())

# Force ssl if run in Heroku
# if "DYNO" in os.environ:  # pragma: no cover
#     SECURE_SSL_REDIRECT = True
#     SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# STORAGE CONFIGURATION IN S3 AWS
# -----------------------------------------------------------------------------
# Uploaded Media Files
# -----------------------------------------------------------------------------
AWS_ACCESS_KEY_ID = config("DJANGO_AWS_ACCESS_KEY_ID", default=False)
if AWS_ACCESS_KEY_ID:  # pragma: no cover
    COLLECTFAST_ENABLED = True
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
    INSTALLED_APPS.append("s3_folder_storage")
    INSTALLED_APPS.append("storages")
    AWS_SECRET_ACCESS_KEY = config("DJANGO_AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config("DJANGO_AWS_STORAGE_BUCKET_NAME")
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }
    AWS_PRELOAD_METADATA = True
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_CUSTOM_DOMAIN = None

    AWS_DEFAULT_ACL = "public-read"

    # AWS cache settings, don't change unless you know what you're doing:
    AWS_EXPIRY = 60 * 60 * 24 * 7

    # Revert the following and use str after the above-mentioned bug is fixed in
    # either django-storage-redux or boto
    control = f"max-age={AWS_EXPIRY:d}, s-maxage={AWS_EXPIRY:d}, must-revalidate"

    # Upload Media Folder
    DEFAULT_FILE_STORAGE = "s3_folder_storage.s3.DefaultStorage"
    DEFAULT_S3_PATH = "media"
    MEDIA_ROOT = f"/{DEFAULT_S3_PATH}/"
    MEDIA_URL = f"//{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{DEFAULT_S3_PATH}/"

    # Static Assets
    # -------------------------------------------------------------------------
    STATICFILES_STORAGE = "s3_folder_storage.s3.StaticStorage"
    STATIC_S3_PATH = "static"
    STATIC_ROOT = f"/{STATIC_S3_PATH}/"
    STATIC_URL = f"//{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{STATIC_S3_PATH}/"
    ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

# -----------------------------------------------------------------------------

# Cloudinary
CLOUDINARY_URL = config('CLOUDINARY_URL', default=False)

if CLOUDINARY_URL:  # pragma: no cover
    if AWS_ACCESS_KEY_ID:
        # Usa Cloudinary apenas quando AWS não foi configurado
        pass
    else:
        INSTALLED_APPS.remove('django.contrib.staticfiles')
        INSTALLED_APPS = [
            'cloudinary_storage',
            'django.contrib.staticfiles',
            'cloudinary',
        ] + INSTALLED_APPS

        COLLECTFAST_ENABLED = False

        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'
        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticCloudinaryStorage'

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Sentry
sentry_sdk.init(dsn=config('SENTRY_DSN'), integrations=[DjangoIntegration()])
