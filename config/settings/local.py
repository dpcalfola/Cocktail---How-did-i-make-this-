from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_env.SECRET_KEY['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DB information from secrets
# DB_1 Home network
# DATABASES = secret_env.HOWDIMT_DATABASES

# DB_2 External connect
DATABASES = secret_env.HOWDIMT_DATABASES_ONLINE_SERVER

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


CSRF_TRUSTED_ORIGINS = secret_env.CSRF_TRUSTED_ORIGINS_LIST_LOCAL
