import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'replace-this-with-a-secret-key'
DEBUG = True
ALLOWED_HOSTS = [
    "payroll-service-1078816020262-1078816020262.africa-south1.run.app",
    "payroll-service-1078816020262.africa-south1.run.app",
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    "https://payroll-service-1078816020262-1078816020262.africa-south1.run.app",
    "https://payroll-service-1078816020262.africa-south1.run.app",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'payroll_system.urls'
WSGI_APPLICATION = 'payroll_system.wsgi.application'

}

# Templates configuration so Django finds templates/registration/login.html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

# Login redirects
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Harare'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'


import os

'.format(os.environ.get('CLOUD_SQL_CONNECTION_NAME', ''))),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}


import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'payrolldb'),
        'USER': os.environ.get('DB_USER', 'payroll_user'),
        'PASSWORD': os.environ.get('DB_PASS', ''),
        'HOST': os.environ.get('DB_HOST', '/cloudsql/{}'.format(os.environ.get('CLOUD_SQL_CONNECTION_NAME', ''))),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}
