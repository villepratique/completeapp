"""

https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# import django_heroku
from pathlib import Path
import os

print(os.environ.get('MJ_APIKEY_PUBLIC'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'wzy)z&uowsq1po#f=1ml+!-pr^-7$8(s++iq27o*ci)_n0pyd)')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["127.0.0.1"]
ALLOWED_HOSTS = ["127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'generator',
    'core',
    'booking',

    'debug_toolbar'
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates'),
            ],
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

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),)

STATICFILES_DIRS = [
    BASE_DIR / "generator/static",
    BASE_DIR / "booking/static",
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




AUTH_USER_MODEL = 'core.User'
LOGIN_REDIRECT_URL = '/'
SECURE_SSL_REDIRECT = False
# config/settings.py
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))

SITE_URL="http://127.0.0.1:8000"

INTERNAL_IPS = [
    "127.0.0.1",
]

# appkey = "bg7a0e0asp0aks2"
# appSecret = "olj0w74gh1l7bn7"
# accessToken = ""

accessToken = os.environ.get('DROPBOX_ACCESS_TOKEN')
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

DROPBOX_OAUTH2_TOKEN=accessToken

# django_heroku.settings(locals())


