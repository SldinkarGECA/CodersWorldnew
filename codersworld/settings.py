from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = "&j(44&nf#=)nm#gmyr1y$a^qxg3@b1!s*hh+ti8fjm91to-m0m"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "homepage.apps.HomepageConfig",
    "news.apps.NewsConfig",
    "courses.apps.CoursesConfig",
    "books.apps.BooksConfig",
    "blogs.apps.BlogsConfig",
    "accounts.apps.AccountsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "codersworld.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [(os.path.join(BASE_DIR, "templates")), ],
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

WSGI_APPLICATION = "codersworld.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# STATIC_ROOT = BASE_DIR / "static"
# STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "codersworld/static/"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

# save the media
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 25
EMAIL_HOST_USER = "beyousandy95@gmail.com"
EMAIL_HOST_PASSWORD = "detengrzpjnoaucf"
