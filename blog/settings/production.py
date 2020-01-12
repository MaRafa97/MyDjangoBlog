from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['rafadjangoblog.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'dde6h9c42kcgtu',
        'USER':'otvvqjucpjcgfy',
        'PASSWORD':'68e454bfb71c050f8a4e17bcbf7a4ee1f82d6b772b3179cb87b974e7c73479e1',
        'HOST':'ec2-174-129-32-200.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
