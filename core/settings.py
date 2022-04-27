import os
# import pymysql
# pymysql.install_as_MySQLdb()
from decouple import config
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)


# DB_HOST = config('DATABASE_FFZ_HOST')
# DB_NAME = config('DATABASE_FFZ_DATABASE_NAME')
# DB_FARMERS = config('DATABASE_FARMER_DATABASE_NAME')
# DB_USERNAME = config('DATABASE_FFZ_USERNAME')
# DB_PASSWORD = config('DATABASE_FFZ_PASSWORD')

# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1')]
# ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'authentication.FFZUser'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'apps.home',  # Enable the inner home (home)
    'apps.authentication',
    'apps.common',
    'apps.farmers',
    'apps.inventory',
    'apps.locations',
    'apps.logs',
    'apps.offers',
    'apps.orders',
    'apps.payments',
    'apps.products',
    'apps.ffzusers',
    'apps.reports',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         # 'NAME': 'farmersfz',
#         # 'USER': 'root',
#         # 'PASSWORD': 'lockit',
#         # 'HOST': 'host.docker.internal',
#         # 'HOST': '172.16.0.57',
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'testdb',
#         'USER': 'root',
#         'PASSWORD': 'roo@123',
#         'OPTIONS': {
#             'charset': 'utf8mb4'
#         },
#         'HOST': 'localhost',
#         'PORT': '3306',
#     },
#     # 'farmers': {
#     #     'ENGINE': 'django.db.backends.mysql',
#     #     'NAME': DB_FARMERS,
#     #     'USER': DB_USERNAME,
#     #     'PASSWORD': DB_PASSWORD,
#     #     'HOST': DB_HOST,
#     #     'PORT': '3306',
#     # }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'farmersfz_production_clone_20210807',
        'USER': 'api_server',
        'PASSWORD': 'c7a9cce341bf1b7d63125a97d8b98750#FZ',
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
        'HOST': '3.6.112.246',
        'PORT': '3306',
    },
    'farmers': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'farmer',
        'USER': 'api_server',
        'PASSWORD': 'c7a9cce341bf1b7d63125a97d8b98750#FZ',
        'HOST': '3.6.112.246',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)


#############################################################
#############################################################
