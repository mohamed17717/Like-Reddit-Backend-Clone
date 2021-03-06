import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u2(09zm@p^^zm#y^43tb#36^vwm&&^26*wz-wo&%!y%)&5kt&q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
  '127.0.0.1'
]


# Application definition
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  # apps
  'core',
  'accounts',
  'categories',
  'follows',
  'impressions',
  'notifications',
  'posts',
  'privates',
  'reports',
  'rewards',
  'saves',
  'threads',
  'states',

  # third parties
  'rest_framework',
  'djoser',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',

  'core.middleware.ErrorDataBaseIntegrityHandlerMiddleware'
]

ROOT_URLCONF = 'dj.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],
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

WSGI_APPLICATION = 'dj.wsgi.application'


# Database
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
  { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
  { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
  { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
  { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'


# Django 3 Conf
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email Setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# DJOSER
REST_FRAMEWORK = {
  'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
  'PAGE_SIZE': 5,

  'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
  ),
}

SIMPLE_JWT = {
  'AUTH_HEADER_TYPES': ('JWT',),
  'ACCESS_TOKEN_LIFETIME': timedelta(days=10),
  'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
}

DJOSER = {
  'LOGIN_FIELD': 'email',
  'USER_CREATE_PASSWORD_RETYPE': True,
  'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
  'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
  'SEND_CONFIRMATION_EMAIL': True,
  'SET_PASSWORD_RETYPE': True,
  'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
  'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
  'ACTIVATION_URL': 'activate/{uid}/{token}',
  'SEND_ACTIVATION_EMAIL': True,
  'SERIALIZERS': {
    'user_create': 'accounts.serializers.UserCreateSerializer',
    'user': 'accounts.serializers.UserCreateSerializer',
    'user_delete': 'djoser.serializers.UserDeleteSerializer',
  }
}
