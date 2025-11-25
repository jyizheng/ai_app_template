from pathlib import Path
import dj_database_url
from common.config import SUPABASE_DB_URL

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "dev"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "django_app.urls"
WSGI_APPLICATION = "django_app.wsgi.application"

DATABASES = {
    "default": dj_database_url.parse(SUPABASE_DB_URL, ssl_require=True)
}

STATIC_URL = "/static/"
