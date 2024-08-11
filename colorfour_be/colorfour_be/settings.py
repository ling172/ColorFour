from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
	os.getenv("FRONTEND_URL"),
	os.getenv("NGROK_URL"),
]

FRONTEND_URL = os.getenv("FRONTEND_URL")

INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"django.contrib.sites",
	"rest_framework",
	"rest_framework.authtoken",
	"dj_rest_auth",
	"dj_rest_auth.registration",
	"allauth",
	"allauth.account",
	"allauth.socialaccount",
	"allauth.socialaccount.providers.google",
	"allauth.socialaccount.providers.line",
	"corsheaders",

	"color_analyzer",
	"wardrobe_manager",
	"outfit_recommender",
	"shopping_advisor",
	"social_platform",
	"outfit_scheduler",
	"line",
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
	"allauth.account.auth_backends.AuthenticationBackend",
	"django.contrib.auth.backends.ModelBackend",
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_PASSWORD_REQUIRED = False
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
ACCOUNT_SIGNUP_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
	"line": {
		"APP": {
			"client_id": os.getenv("LINE_LOGIN_CHANNEL_ID"),
			"secret": os.getenv("LINE_LOGIN_CHANNEL_SECRET"),
		},
		"SCOPE": [ "profile", "openid", "email"],
		'OAUTH_GET_PARAMS': {
			'redirect_uri': 'https://upward-gorgeous-bedbug.ngrok-free.app/accounts/line/login/callback/',
		}
	},
	"google": {
		"APP": {
			"client_id": os.getenv("GOOGLE_CLIENT_ID"),
			"secret": os.getenv("GOOGLE_CLIENT_SECRET"),
			"key": "",
		},
		"SCOPE": [
			"profile",
			"email",
		],
		"AUTH_PARAMS": {
			"access_type": "online",
		},
	},
}

SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"
ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"

REST_FRAMEWORK = {
	"DEFAULT_AUTHENTICATION_CLASSES": [
		"dj_rest_auth.jwt_auth.JWTCookieAuthentication",
	],
	"DEFAULT_PERMISSION_CLASSES": [
		"rest_framework.permissions.IsAuthenticated",
	],
}

from datetime import timedelta

SIMPLE_JWT = {
	"ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
	"REFRESH_TOKEN_LIFETIME": timedelta(days=1),
	"ROTATE_REFRESH_TOKENS": True,
	"BLACKLIST_AFTER_ROTATION": True,
	"AUTH_HEADER_TYPES": ("Bearer",),
	"AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
	"AUTH_COOKIE": "access_token",
	"AUTH_COOKIE_SECURE": True,
	"AUTH_COOKIE_HTTP_ONLY": True,
	"AUTH_COOKIE_PATH": "/",
	"AUTH_COOKIE_SAMESITE": "Lax",
}


MIDDLEWARE = [
	"django.middleware.security.SecurityMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"corsheaders.middleware.CorsMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
	"allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "colorfour_be.urls"

TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		# os.path.join(BASE_DIR, 'templates'),
		"DIRS": [],
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

WSGI_APPLICATION = "colorfour_be.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.mysql",
		"NAME": os.getenv("DATABASE_NAME"),
		"USER": os.getenv("DATABASE_USER"),
		"PASSWORD": os.getenv("DATABASE_PASSWORD"),
		"HOST": os.getenv("DATABASE_HOST"),
		"PORT": os.getenv("DATABASE_PORT"),
	}
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
	},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-Hant"
TIME_ZONE = "Asia/Taipei"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]

# MEDIA_URL = 'media/'
# MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
	"version": 1,
	"disable_existing_loggers": False,
	"formatters": {
		"verbose": {
			"format": "{levelname} {asctime} {module} {message}",
			"style": "{",
		},
		"simple": {
			"format": "{levelname} {message}",
			"style": "{",
		},
	},
	"handlers": {
		"console": {
			"level": "DEBUG",
			"class": "logging.StreamHandler",
			"formatter": "verbose",
		},
	},
	"loggers": {
		# "django": {
		#     "handlers": ["console"],
		#     "level": "DEBUG",
		#     "propagate": True,
		# },
		"": {
			"handlers": ["console"],
			"level": "DEBUG",
		},
	},
}
