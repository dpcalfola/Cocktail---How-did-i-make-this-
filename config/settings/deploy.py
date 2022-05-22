from base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_env.SECRET_KEY['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Deploy DB info
DATABASES = secret_env.HOWDIMT_DATABASES_DEPLOY

CSRF_TRUSTED_ORIGINS = secret_env.CSRF_TRUSTED_ORIGINS_LIST_DEPLOY
