"""
Django settings for User Service.
"""

import os
from socket import gethostname, gethostbyname
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv('DEBUG', None) == "true" else False
APP_DEBUG = True if os.getenv('APP_DEBUG', None) == "true" else False

# Allowed hosts for the application
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') + ["127.0.0.1", ] + [gethostname(), gethostbyname(gethostname())]

# Current environment (dev, prod, etc.)
ENVIRONMENT = os.getenv('ENVIRONMENT')

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Using PostgreSQL database
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),  # Default host is localhost
        'PORT': os.getenv('DB_PORT', 5432),  # Default port for PostgreSQL
        'OPTIONS': json.loads(
             os.getenv('DB_OPTIONS', '{}')  # Additional DB options (SSL, etc.)
         ),
    },
}

# Application definition (Installed apps)
INSTALLED_APPS = [
    'django.contrib.auth',            # Core authentication framework
    'django.contrib.contenttypes',    # Core Django content types framework
    'rest_framework',                 # Django REST Framework
    'users',                          # Custom users app
]

# Migration modules configuration
MIGRATION_MODULES = {
    'users': 'migrations.users',
}

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',          # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',   # Session management
    'django.middleware.common.CommonMiddleware',              # Common HTTP operations
    'django.middleware.csrf.CsrfViewMiddleware',               # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',# Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',   # Message framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protection against clickjacking
]

# API prefix for this service
API_PREFIX = 'api/v1/user/'

# Required for Django 3.2+ to avoid warnings about primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Overriding the default middleware list (may be intentional for specific setups)
MIDDLEWARE = []

# Root URL configuration module
ROOT_URLCONF = 'settings.urls'

# Custom user model
AUTH_USER_MODEL = 'users.User'

# REST framework settings (commented out, can be enabled if needed)
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
# }

# Template engine settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Template directories
        'APP_DIRS': True,  # Look for templates inside app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # Request context processor
                'django.contrib.auth.context_processors.auth',  # Auth context processor
                'django.contrib.messages.context_processors.messages',  # Messages context processor
            ],
        },
    },
]

# WSGI application path
WSGI_APPLICATION = 'settings.wsgi.application'

# Password validation configuration
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Prevents passwords similar to user attributes
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Enforces a minimum password length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Prevents common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Prevents passwords that are entirely numeric
    },
]

# Internationalization settings
# https://docs.djangoproject.com/en/5.2/topics/i18n/
LANGUAGE_CODE = 'en-us'

# Default time zone
TIME_ZONE = 'UTC'

USE_I18N = True  # Enable Django's translation system

USE_TZ = True  # Enable timezone-aware datetimes

# Static files (CSS, JavaScript, Images) configuration
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
