from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        
        # Configuración postgresql
        
        # "ENGINE": "django.db.backends.postgresql_psycopg2",
        # "NAME": BASE_DIR / "learnin_bi",
        # "USER": "ADMIN",
        # "PASSWORD": "Password123.",
        # "HOST":"localhost",
        # "PORT":"5432",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
# STATICFILES_DIR = [BASE_DIR.child('static')]