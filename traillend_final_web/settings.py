"""
Django settings for traillend_final_web project.
"""

from pathlib import Path
import os
import json
import dj_database_url
import firebase_admin
from firebase_admin import credentials
from datetime import timedelta

# ==============================
# BASE DIRECTORY
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================
# FIREBASE ADMIN CONFIG (LOCAL + RENDER)
# ==============================
LOCAL_FIREBASE_PATH = BASE_DIR / "firebase_key.json"

if not firebase_admin._apps:
    if LOCAL_FIREBASE_PATH.exists():
        # ✔ Local development uses firebase_key.json file
        cred = credentials.Certificate(str(LOCAL_FIREBASE_PATH))
    else:
        # ✔ Render uses JSON stored inside a single environment variable
        firebase_json = os.environ.get("FIREBASE_CREDENTIALS")

        if not firebase_json:
            raise ValueError("Missing FIREBASE_CREDENTIALS environment variable")

        firebase_info = json.loads(firebase_json)
        cred = credentials.Certificate(firebase_info)

    firebase_admin.initialize_app(cred)


# ==============================
# DJANGO SECRET KEY
# ==============================
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-g%ec9@2x9!z^j=w$ssd4+n_3+o!hwg1op&-9^4@yo$s#i1)5n6"
)

# ==============================
# DEBUG MODE
# ==============================
DEBUG = os.environ.get("DEBUG", "False") == "True"


# ==============================
# ALLOWED HOSTS
# ==============================
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
    "10.147.69.115",
    "10.180.1.217",
    "192.168.43.118",
]


# ==============================
# INSTALLED APPS
# ==============================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",

    "django_extensions",
    "django_crontab",

    "core",
]


# ==============================
# MIDDLEWARE
# ==============================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==============================
# REST FRAMEWORK + JWT
# ==============================
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
    "UPDATE_LAST_LOGIN": True,
}


# ==============================
# CORS SETTINGS
# ==============================
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True


# ==============================
# URL CONFIGURATION
# ==============================
ROOT_URLCONF = "traillend_final_web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "core" / "templates"],
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


# ==============================
# DATABASE CONFIG (Render PostgreSQL)
# ==============================
DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}


# ==============================
# PASSWORD VALIDATION
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ==============================
# INTERNATIONALIZATION
# ==============================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Manila"
USE_I18N = True
USE_TZ = True


# ==============================
# STATIC FILES (Whitenoise + Render)
# ==============================
STATIC_URL = "/static/"

STATICFILES_DIRS = []
if (BASE_DIR / "static").exists():
    STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ==============================
# MEDIA FILES
# ==============================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ==============================
# EMAIL CONFIGURATION
# ==============================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "traillendsystem@gmail.com"
EMAIL_HOST_PASSWORD = "vityemepzgqcdamk"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# ==============================
# DEFAULT PRIMARY KEY
# ==============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "/login/"
