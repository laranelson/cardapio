import os


from decouple import config, Csv
#from dj_database_url import parse as dburl

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'xwow4foo-tprx3yfdiey@z@ur^=_+mn3_73a1u3ilhfol@mh92'


DEBUG = True

# ALLOWED_HOSTS = config("ALLOWED_HOSTS", default=[], cast=Csv())
ALLOWED_HOSTS = ['*']

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


#BASE DE DADOS LOCAL - DESENVOLVIMENTO
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'menugo_db',
        'USER': 'menugo',
        'PASSWORD': 'j8QZB-e2WU_1m3fz2(',
        'HOST': 'menugo.domcloud.dev',
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

