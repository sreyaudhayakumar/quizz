"""
Django settings for quiz_platform project.
Cleaned, refactored, production-ready version with .env integration.
"""

from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base directory (root folder of the project)
BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# SECURITY SETTINGS
# --------------------------------------------------

# Never keep SECRET_KEY in source code
SECRET_KEY = os.getenv("SECRET_KEY")

# Debug only for development
DEBUG = os.getenv("DEBUG") == "True"

ALLOWED_HOSTS = []  # Add domains here in production


# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local apps
    "quiz",
    "user",
    "user_submission",

    # Third-party apps
    "rest_framework",
    "rest_framework_simplejwt",
]


# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------------------------------------
# URL & WSGI SETTINGS
# --------------------------------------------------

ROOT_URLCONF = "quiz_platform.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Add template folders here
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "quiz_platform.wsgi.application"


# --------------------------------------------------
# DATABASE CONFIGURATION (MySQL with .env)
# --------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "3306"),
    }
}


# --------------------------------------------------
# REST FRAMEWORK + JWT
# --------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=8),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}


# --------------------------------------------------
# AUTHENTICATION
# --------------------------------------------------

AUTH_USER_MODEL = "user.User"


# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------

STATIC_URL = "static/"


# --------------------------------------------------
# DEFAULT PRIMARY KEY TYPE
# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
