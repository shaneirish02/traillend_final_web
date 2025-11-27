"""
Django settings for traillend_final_web project.
Clean version for Railway Deployment
"""

import os
from pathlib import Path
from datetime import timedelta
import dj_database_url
import firebase_admin
from firebase_admin import credentials

# ============================================
# BASE DIR
# ============================================
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================
# SECRET KEY & DEBUG (from Railway env)
# ============================================
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

DEBUG = os.environ.get("DEBUG", "False") == "True"


# ============================================
# ALLOWED HOSTS
# ============================================
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".railway.app",
    ".up.railway.app",
]


# ============================================
# FIREBASE CONFIG (local + Railway support)
# ============================================
firebase_key_path = BASE_DIR / "firebase_key.json"

if not firebase_admin._apps:
    if firebase_key_path.exists():
        # local development
        cred = credentials.Certificate(str(firebase_key_path))
    else:
        # Production (Railway environment variables)
        firebase_cred = {
            "type": os.environ.get("FIREBASE_TYPE"),
            "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
            "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
            "private_key": os.environ.get("FIREBASE_PRIVATE_KEY", "").replace("\\n", "\n"),
            "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
            "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_CERT_URL"),
        }
        cred = credentials.Certificate(firebase_cred)

    firebase_admin.initialize_app(cred)


# ============================================
# INSTALLED APPS
# ============================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',

    'core',
]


# ============================================
# MIDDLEWARE
# ============================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ============================================
# REST FRAMEWORK + JWT
# ============================================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=31),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}


# ============================================
# CORS
# ============================================
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True


# ============================================
# URL CONFIG
# ============================================
ROOT_URLCONF = "traillend_final_web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "core/templates"],
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

WSGI_APPLICATION = "traillend_final_web.wsgi.application"


# ============================================
# DATABASE — USE RAILWAY DATABASE_URL
# ============================================
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}


# ============================================
# PASSWORD VALIDATION
# ============================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ============================================
# TIMEZONE
# ============================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Manila"
USE_I18N = True
USE_TZ = True


# ============================================
# STATIC & MEDIA
# ============================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


# ============================================
# EMAIL SMTP
# ============================================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
