# myportfolio/settings/local.py
from .base import *

# Allow any host during local development
ALLOWED_HOSTS = ["*"]

# Use SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myportpholio',
        'USER': 'postgres',
        'PASSWORD': 'Nanera372',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])
SECURE_SSL_REDIRECT = False
