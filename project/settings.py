from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key 
from datetime import timedelta
import dj_database_url 
from decouple import config 



BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# SECURITY SETTINGS
# -------------------------------------------------------------------

# Use environment variable for SECRET_KEY (never commit it in code)
SECRET_KEY = config("SECRET_KEY")

# Disable Debug in Production
DEBUG =  config("DEBUG",cast=bool)

# Set your domain(s) or server IP
ALLOWED_HOSTS =config("ALLOWED_HOSTS").split(",") 



# -------------------------------------------------------------------
# APPLICATIONS
# -------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'item',
    'axes',
]

# -------------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',   # optional caching
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # central template directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# -------------------------------------------------------------------
# DATABASE (switch to PostgreSQL/MySQL in production)
# -------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Replace with PostgreSQL for production
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES['default']=dj_database_url.parse(config("DATABASE_URL"))

# -------------------------------------------------------------------
# AUTHENTICATION
# -------------------------------------------------------------------
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'core:index'
LOGOUT_REDIRECT_URL = 'login'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------------------------------------------
# INTERNATIONALIZATION
# -------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------------
# STATIC & MEDIA
# -------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"  # collectstatic output

STATICFILES_DIRS = [BASE_DIR / 'core/static']  # dev assets

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 


AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = timedelta(minutes=30) 
AXES_LOCKOUT_CALLABLE = None


# -------------------------------------------------------------------
# SECURITY HEADERS
# -------------------------------------------------------------------
#SECURE_BROWSER_XSS_FILTER = True
#SECURE_CONTENT_TYPE_NOSNIFF = True
#X_FRAME_OPTIONS = "DENY"

# Force HTTPS
#SECURE_SSL_REDIRECT = False
#SESSION_COOKIE_SECURE = False
#CSRF_COOKIE_SECURE = False

# HTTP Strict Transport Security
# SECURE_HSTS_SECONDS = 31536000  # 1 year
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_PRELOAD = True

# -------------------------------------------------------------------
# LOGGING
# -------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
# Enable GZip compression
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',  # ✅ tracks failed logins
    'django.contrib.auth.backends.ModelBackend',  # default Django backend
]
