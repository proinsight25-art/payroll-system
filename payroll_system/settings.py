import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'replace-this-with-a-secret-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    "payroll-service-1078816020262-1078816020262.africa-south1.run.app",
    "payroll-service-1078816020262.africa-south1.run.app",
    "localhost",
    "127.0.0.1",
    "payroll-service-n7gqakiylq-bq.a.run.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://payroll-service-1078816020262-1078816020262.africa-south1.run.app",
    "https://payroll-service-1078816020262.africa-south1.run.app",
]

# Applications and middleware
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # add your apps here
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

ROOT_URLCONF = 'payroll_system.urls'
WSGI_APPLICATION = 'payroll_system.wsgi.application'

# Templates configuration so Django finds templates/registration/login.html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Auth redirects
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Harare'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Database configuration (reads from environment variables)
# Prefer explicit DB_HOST; otherwise build from CLOUD_SQL_CONNECTION_NAME
CLOUD_SQL_CONNECTION_NAME = os.environ.get('CLOUD_SQL_CONNECTION_NAME', '')
# If DB_HOST is explicitly provided use it; otherwise, if CLOUD_SQL_CONNECTION_NAME is set,
# use the Cloud SQL unix socket path; otherwise default to empty string (localhost or other env).
DEFAULT_DB_HOST = os.environ.get('DB_HOST') or (f"/cloudsql/{CLOUD_SQL_CONNECTION_NAME}" if CLOUD_SQL_CONNECTION_NAME else os.environ.get('DB_HOST', ''))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Logging (basic default; adjust as needed)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {
        'handlers': ['console'],
        'level': os.environ.get('DJANGO_LOG_LEVEL', 'INFO'),
    },
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Include top-level static/ directory so collectstatic finds repo assets
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

# TEMPORARY: avoid ManifestStaticFilesStorage until manifest is fixed
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
